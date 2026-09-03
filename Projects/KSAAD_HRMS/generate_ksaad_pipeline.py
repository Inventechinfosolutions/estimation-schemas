#!/usr/bin/env python3
"""
End-to-end generator for KSAAD HRMS / KSAAD Digital Platform pipeline artefacts.

Outputs (under this project folder):
  - SoW_KSAAD_HRMS_Detailed.md + .docx  (Step 1)
  - KSAAD_HRMS_Modules.md              (Step 2)
  - modules/{NN}-{slug}/README.md
  - modules/{NN}-{slug}/features/*.md + features/_index.md (Step 5)
  - KSAAD_HRMS_Registry.json         (Step 3 & Step 5 capture)
  - KSAAD_HRMS_Estimation_Summary.md + _FeatureWise.md (Step 6)
  - KSAAD_HRMS_Estimation_Summary_FeatureWise_Client.docx (Step 7)

Notes:
- Hours are computed from the repo's Estimation Master in feature_schema.md (copied here).
- This script intentionally keeps content "consultant-authored" at the document level
  (client DOCX export is produced from feature index tables; no CONTROL/pipeline mentions).
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "SoW_KSAAD_HRMS_Detailed.md"
DOCX_PATH = ROOT / "SoW_KSAAD_HRMS_Detailed.docx"

PROJECT_CODE = "KSAAD_HRMS"
PROJECT_NAME = "KSAAD Digital Platform"
OUTPUT_ROOT = ROOT

# --- Estimation Master (from feature_schema.md) ---
UI_HOURS = {
    "Simple": 2,
    "Easy": 4,
    "Medium": 6,
    "Complex": 12,
    "Very High": 16,
}
API_HOURS = {
    "Simple": 2,
    "Easy": 4,
    "Medium": 6,
    "Complex": 8,
    "Very High": 16,
}
DB_HOURS = {
    "Simple": 1,
    "Easy": 2,
    "Medium": 4,
    "Complex": 6,
    "Very High": 10,
}
INTEGRATION_HOURS = {
    "Simple": 4,
    "Easy": 8,
    "Medium": 16,
    "Complex": 24,
    "Very High": 40,
}
TESTING_HOURS = {
    "Simple": 2,
    "Easy": 4,
    "Medium": 6,
    "Complex": 8,
    "Very High": 12,
}
DOC_HOURS = {
    "Simple": 1,
    "Easy": 2,
    "Medium": 3,
    "Complex": 4,
    "Very High": 6,
}


NAVY = RGBColor(0x1B, 0x3A, 0x5F)
ACCENT = RGBColor(0x2E, 0x5A, 0x88)
HEADER_BG = "1B3A5F"
ALT_ROW = "F3F6FA"
MUTED = RGBColor(0x55, 0x55, 0x55)


def slugify(text: str) -> str:
    """Derive kebab-case slugs using CONTROL numbering_schema rules (approx)."""
    s = text.strip().lower()
    s = s.replace("&", "and")
    # keep letters/digits/spaces/hyphens only
    # NOTE: use `\s` (whitespace) not `\\s` (literal backslash-s)
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = s.replace("_", "-")
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def hours_for(category: str, complexity: str) -> int:
    if category == "UI":
        return UI_HOURS[complexity]
    if category == "API":
        return API_HOURS[complexity]
    if category == "DB":
        return DB_HOURS[complexity]
    if category == "Integration":
        return INTEGRATION_HOURS[complexity]
    if category == "Testing":
        return TESTING_HOURS[complexity]
    if category == "Documentation":
        return DOC_HOURS[complexity]
    raise ValueError(category)


def estimate_total(items: List[Tuple[str, str]]) -> int:
    return sum(hours_for(cat, comp) for cat, comp in items)


sys.path.insert(0, str(ROOT))
from ksaad_feature_specs import FeatureDef, ModuleDef, build_modules  # noqa: E402


def _md_cell(text: str) -> str:
    return str(text).replace("|", "/").replace("\n", " ").strip()


def _md_bullets(items: List[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def _md_numbered(items: List[str]) -> str:
    return "\n".join(f"{i}. {item}" for i, item in enumerate(items, start=1))


def feature_estimate_rows(feature: FeatureDef) -> List[Tuple[str, str, str, int]]:
    rows: List[Tuple[str, str, str, int]] = []
    for name, complexity in feature.ui:
        rows.append((name, "UI", complexity, hours_for("UI", complexity)))
    for name, complexity in feature.api:
        rows.append((name, "API", complexity, hours_for("API", complexity)))
    for name, complexity in feature.db:
        rows.append((name, "DB", complexity, hours_for("DB", complexity)))
    for name, complexity in feature.integration:
        rows.append((name, "Integration", complexity, hours_for("Integration", complexity)))
    rows.append(
        (
            f"{feature.name} feature tests",
            "Testing",
            feature.testing,
            hours_for("Testing", feature.testing),
        )
    )
    rows.append(
        (
            f"{feature.name} implementation documentation",
            "Documentation",
            feature.documentation,
            hours_for("Documentation", feature.documentation),
        )
    )
    return rows


def module_nn_str(nn: int) -> str:
    return f"{nn:02d}"


def feature_id(nn: int, seq: int) -> str:
    return f"F{nn:02d}-{seq:03d}"


def feature_filename(nn: int, seq: int, feature_slug: str) -> str:
    return f"F{nn:02d}-{seq:03d}-{feature_slug}.md"


def write_feature_file(module: ModuleDef, feature: FeatureDef) -> Tuple[str, int, str, str]:
    nn = module.nn
    seq = feature.seq
    fid = feature_id(nn, seq)
    fslug = slugify(feature.name)

    module_slug = slugify(module.name)
    folder = ROOT / "modules" / f"{module_nn_str(nn)}-{module_slug}" / "features"
    folder.mkdir(parents=True, exist_ok=True)

    path = folder / feature_filename(nn, seq, fslug)

    estimate_rows = feature_estimate_rows(feature)
    total = sum(hours for _, _, _, hours in estimate_rows)

    ui_table = "\n".join(
        f"| {_md_cell(name)} | {complexity} |" for name, complexity in feature.ui
    )
    api_table = "\n".join(
        f"| {_md_cell(name)} | {complexity} |" for name, complexity in feature.api
    )
    est_table = "\n".join(
        f"| {_md_cell(name)} | {category} | {complexity} | {hours} |"
        for name, category, complexity, hours in estimate_rows
    )

    md = f"""# {fid} — {feature.name}

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | {fid} |
| **Feature Name** | {feature.name} |
| **Module** | {module_nn_str(nn)} — {module.name} |

### Description
{feature.description}

### Business Objective
{feature.objective}

### Actors
{feature.actors}

### User Journey
{_md_numbered(feature.journey)}

### Functional Capabilities
{_md_bullets(feature.capabilities)}

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
{ui_table}

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
{api_table}

### Inputs
{feature.inputs}

### Outputs
{feature.outputs}

### Business Rules
{_md_bullets(feature.rules)}

### Validations
{_md_bullets(feature.validations)}

### Calculations
{feature.calculations}

### Workflow
{feature.workflow}

### Search Requirements
{feature.search}

### Documents
{feature.documents}

### Reports
{feature.reports}

### Notifications
{feature.notifications}

### Security
{feature.security}

### Integrations
{feature.integrations}

### Dependencies
{feature.dependencies}

### Assumptions
{_md_bullets(feature.assumptions)}

### Risks
{feature.risks}

### Non Functional Requirements
{feature.nfr}

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
{est_table}
| **Total** | | | **{total}** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
"""

    path.write_text(md, encoding="utf-8")
    notes = feature.notes or feature.objective
    return fid, total, feature.name, notes


def write_module_index(module: ModuleDef, rows: List[Tuple[str, str, int, str]]) -> None:
    module_slug = slugify(module.name)
    idx_path = ROOT / "modules" / f"{module_nn_str(module.nn)}-{module_slug}" / "features" / "_index.md"
    idx_path.parent.mkdir(parents=True, exist_ok=True)

    lines = ["# Feature Index", "", f"## {module_nn_str(module.nn)} — {module.name}", ""]
    lines.append("| Feature ID | Feature Name | Total Hours | Notes |")
    lines.append("|---|---|---:|---|")

    total = 0
    for fid, name, hours, notes in rows:
        total += hours
        safe_notes = str(notes).replace("|", "/")
        lines.append(f"| {fid} | {name} | {hours} | {safe_notes} |")

    lines.append("")
    lines.append(f"**Module Total:** **{total}** hours")
    idx_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_modules_file(modules: List[ModuleDef]) -> None:
    path = ROOT / f"{PROJECT_CODE}_Modules.md"
    title = f"# {PROJECT_NAME} — Module List"

    # Source is the combination of both provided documents.
    src = "Source: Ksaad_HRMS_FRS.docx + RFP_HRMS_KSAAD (1).docx"

    lines = [title, "", src, "", "| # | Module | Type | Summary | Source |", "|---|--------|------|---------|--------|"]
    for m in modules:
        lines.append(f"| {m.nn:02d} | {m.name} | {m.module_type} | {m.summary} | FRS/RFP |")

    lines += ["", "***Module Details***", ""]
    for m in modules:
        ms = f"{m.nn:02d}. {m.name}"
        lines += [
            f"### {ms}",
            f"- **Type:** {m.module_type}",
            f"- **Summary:** {m.summary}",
            "- **Source:** Derived from scope and functional areas in the provided documents.",
            "- **In Scope:** Core capabilities and workflows described for the module.",
            "- **Out of Scope:** Any unrelated platform products not required for KSAAD Digital Platform functionality.",
            "- **Key Actors:** Authorised staff users, approvers, auditors, and institution users scoped by RBAC.",
            "- **Dependencies:** Module 01 governance; Module 13 DMS where document handling is needed; reporting readiness depends on Module 14.",
            "- **Notes:** Designed to be estimable as a cohesive delivery unit.",
            "",
        ]

    lines += ["***Excluded / Embedded Capabilities***", ""]  # lightweight statement
    lines += [
        "- Generic workflow engine internals are governed centrally and embedded in Module 01 governance.",
        "- File storage hardware, annual maintenance, and classroom training are typically out of feature scope and are excluded from estimates unless separately ordered.",
        "",
        "***Assumptions***",
        "",
        "- Module and feature IDs originate in the Step 1 SOW to preserve alignment with downstream extraction.",
        "- Document management is treated as a shared evidence product (Module 13) while evidence attachment is embedded where required in other modules.",
        "",
        "***Risks***",
        "",
        "- Role hierarchy ambiguity could affect approval routing and segregation of duties.",
        "- Integration targets not finalised early could increase delivery risk for operational reliability.",
        "",
    ]

    path.write_text("\n".join(lines), encoding="utf-8")


def write_module_folder_readme(mod: ModuleDef) -> None:
    slug = slugify(mod.name)
    folder = ROOT / "modules" / f"{mod.nn:02d}-{slug}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "README.md").write_text(
        "\n".join(
            [
                f"# {mod.nn:02d}. {mod.name}",
                "",
                f"Type: {mod.module_type}",
                f"Summary: {mod.summary}",
                "Features: (pending generation)",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def write_registry(modules: List[ModuleDef], feature_map: Dict[int, List[Dict[str, Any]]]) -> None:
    reg = {
        "project_code": PROJECT_CODE,
        "project_name": PROJECT_NAME,
        "output_root": str(OUTPUT_ROOT),
        "updated_at": now_iso(),
        "modules": [],
    }

    for m in modules:
        slug = slugify(m.name)
        folder = f"modules/{m.nn:02d}-{slug}"
        feats = feature_map[m.nn]
        total_hours = sum(f["hours"] for f in feats)
        reg["modules"].append(
            {
                "nn": f"{m.nn:02d}",
                "name": m.name,
                "slug": slug,
                "type": m.module_type,
                "folder": folder,
                "feature_count": len(feats),
                "total_hours": total_hours,
                "features": feats,
            }
        )

    (ROOT / f"{PROJECT_CODE}_Registry.json").write_text(json.dumps(reg, indent=2), encoding="utf-8")


def write_internal_summaries(modules: List[ModuleDef], feature_rows: Dict[int, List[Tuple[str, str, int, str]]]) -> None:
    # Compute totals from index rows.
    totals_by_module: List[Tuple[int, str, str, int, int]] = []
    grand = 0
    feature_count = 0

    for m in modules:
        rows = feature_rows[m.nn]
        m_total = sum(r[2] for r in rows)
        grand += m_total
        feature_count += len(rows)
        totals_by_module.append((m.nn, m.name, m.module_type, len(rows), m_total))

    # Step 6 internal summary
    summary_path = ROOT / f"{PROJECT_CODE}_Estimation_Summary.md"
    go_live = grand
    optional = 0

    lines = [
        f"# {PROJECT_CODE} — Estimation Summary",
        "",
        f"> **Detailed module & feature-wise hours:** [`{PROJECT_CODE}_Estimation_Summary_FeatureWise.md`]({PROJECT_CODE}_Estimation_Summary_FeatureWise.md)",
        "",
        f"Source: `SoW_{PROJECT_CODE}_Detailed.md`",
        f"Modules file: `{PROJECT_CODE}_Modules.md`",
        "Internal roll-up from module feature indexes. Hours from Estimation Master.",
        "",
        "---",
        "",
        "## Totals",
        "",
        f"- **Modules:** {len(modules)}",
        f"- **Features:** {feature_count}",
        f"- **Grand total:** **{grand:,} hours**",
        f"- **Recommended go-live:** **{go_live:,} hours**",
        f"- **Optional / conditional:** **{optional} hours**",
        "",
        "## Per-module totals",
        "",
        "| # | Module | Type | Features | Hours |",
        "|---|--------|------|---------:|------:|",
    ]
    for nn, name, mtype, fcount, mhours in totals_by_module:
        lines.append(f"| {nn:02d} | {name} | {mtype} | {fcount} | {mhours:,} |")
    lines.append(f"| | **Total** | | **{feature_count}** | **{grand:,}** |")

    lines += [
        "",
        "## Go-live vs optional",
        "",
        f"- Go-live (all modules 01–16): **{go_live:,} hours**",
        f"- Optional in this baseline: **{optional} hours**",
        "",
        "## Assumptions / risks carried forward",
        "",
        "1. Feature IDs and module numbering align with Step 1 SOW capability IDs.",
        "2. Segregation of duties is enforced through RBAC and maker-checker governance in Module 01.",
        "3. Document management is treated as a shared evidence product (Module 13) consumed by audit and HR workflows.",
        "",
        "## Suggested next actions",
        "",
        "1. Validate role hierarchy with KSAAD and confirm approval routing rules.",
        "2. Review integration targets early so that Module 12 can be finalised without delivery delays.",
        "3. Share the client Word estimate for RFP / commercial discussion.",
        "",
        "---",
        "",
        "*End of internal roll-up*",
        "",
    ]
    summary_path.write_text("\n".join(lines), encoding="utf-8")

    # Step 6 feature-wise summary
    fw_path = ROOT / f"{PROJECT_CODE}_Estimation_Summary_FeatureWise.md"
    lines2 = [
        f"# {PROJECT_CODE} — Estimation Summary (Feature-Wise)",
        "",
        "Internal detail. Hours from Estimation Master via feature files.",
        "",
        f"**Grand total:** {grand:,} hours · **Go-live:** {go_live:,} · **Optional:** {optional}",
        "",
        "## Module-wise summary",
        "",
        "| # | Module | Type | Features | Hours | % of go-live |",
        "|---|--------|------|---------:|------:|-------------:|",
    ]
    for nn, name, mtype, fcount, mhours in totals_by_module:
        pct = (mhours / go_live * 100) if go_live else 0
        lines2.append(f"| {nn:02d} | {name} | {mtype} | {fcount} | {mhours:,} | {pct:.1f}% |")
    lines2.append(f"| | **Total** | | **{feature_count}** | **{grand:,}** | **100%** |")

    # per module feature tables
    lines2 += ["", "## Indicative phasing", "", "| Phase | Modules |", "|-------|---------|"]
    lines2 += [
        "| P1 — Access, masters and identity governance | 01, 02, 13 |",
        f"| P2 — HR and office administration | 03, 04, 05, 06 |",
        f"| P3 — Audit planning and field execution | 07, 08 |",
        f"| P4 — Objections/recovery and financial operations | 09, 10, 11 |",
        f"| P5 — Integrations, reporting and knowledge | 12, 14, 15 |",
        f"| P6 — Institution interaction | 16 |",
        "",
    ]

    lines2 += ["## Exclusions (not in feature hours)", ""]
    lines2 += [
        "- Hosting infrastructure and annual maintenance (AMC), unless separately ordered.",
        "- Hardware purchase and deployment tickets.",
        "- Classroom training and scanning bureau operations, unless separately ordered.",
        "",
    ]

    # Feature rows copied from module feature definitions (from index rows)
    for m in modules:
        rows = feature_rows[m.nn]
        m_total = sum(r[2] for r in rows)
        lines2 += ["", f"## {m.nn:02d} — {m.name} ({m_total:,} hours)", ""]
        lines2 += ["| Feature ID | Feature Name | Hours | Notes |", "|---|---|---:|---|"]
        for fid, fname, hours, notes in rows:
            lines2.append(f"| {fid} | {fname} | {hours} | {str(notes).replace('|','/')} |")

    fw_path.write_text("\n".join(lines2) + "\n", encoding="utf-8")


# --- Markdown -> DOCX conversion (simple approach, consistent with existing repo scripts) ---
def set_run_font(run, *, size: int = 11, bold: bool = False, color=None, name: str = "Calibri") -> None:
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    if color is not None:
        run.font.color.rgb = color


def add_formatted_runs(paragraph, text: str, *, size: int = 11, color=None):
    """Render very small subset of markdown: **bold** and strip links to text."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and part.count("**") == 2:
            run = paragraph.add_run(part[2:-2])
            set_run_font(run, size=size, bold=True, color=color)
        else:
            run = paragraph.add_run(part)
            set_run_font(run, size=size, bold=False, color=color)


def style_paragraph(p, *, space_before=0, space_after=6, line_spacing=1.15):
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE


def set_table_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "CBD5E1")
        borders.append(el)
    tblPr.append(borders)


def set_cell_shading(cell, hex_color: str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def parse_table(lines: List[str], start: int) -> Tuple[List[List[str]], int]:
    rows: List[List[str]] = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = lines[i].strip()
        if re.match(r"^\|[\\s\\-\\|:]+\\|$", row):
            i += 1
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        rows.append(cells)
        i += 1
    return rows, i


def add_table(doc: Document, rows: List[List[str]]):
    if not rows:
        return
    cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=cols)
    table.autofit = True
    set_table_borders(table)

    for r_idx, row in enumerate(rows):
        for c_idx in range(cols):
            cell = table.rows[r_idx].cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            style_paragraph(p, space_before=2, space_after=2, line_spacing=1.05)
            val = row[c_idx] if c_idx < len(row) else ""
            add_formatted_runs(
                p,
                val,
                size=9 if r_idx == 0 else 10,
                color=RGBColor(0xFF, 0xFF, 0xFF) if r_idx == 0 else None,
            )
            if r_idx == 0:
                set_cell_shading(cell, HEADER_BG)
                for run in p.runs:
                    run.bold = True
            elif r_idx % 2 == 0:
                set_cell_shading(cell, ALT_ROW)
    doc.add_paragraph()


def add_page_numbers(doc: Document, footer_label: str):
    section = doc.sections[0]
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run(f" KSAAD | {footer_label} | Page ")
    set_run_font(run, size=8, color=MUTED)

    fld_char_begin = OxmlElement("w:fldChar")
    fld_char_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_char_end = OxmlElement("w:fldChar")
    fld_char_end.set(qn("w:fldCharType"), "end")
    run2 = p.add_run()
    run2._r.append(fld_char_begin)
    run2._r.append(instr)
    run2._r.append(fld_char_end)
    set_run_font(run2, size=8, color=MUTED)


def markdown_to_docx(md_text: str, doc_title: str, footer_label: str) -> Document:
    lines = md_text.splitlines()
    doc = Document()

    # basic styles
    section = doc.sections[0]
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    section.left_margin = Inches(0.95)
    section.right_margin = Inches(0.95)

    styles = doc.styles
    styles["Normal"].font.name = "Calibri"
    styles["Normal"].font.size = Pt(11)
    styles["Normal"]._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    for style_name, size, color in (
        ("Heading 1", 16, NAVY),
        ("Heading 2", 13, ACCENT),
        ("Heading 3", 11, NAVY),
    ):
        st = styles[style_name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = color
        st._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    # Cover
    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("KARNATAKA STATE AUDIT AND ACCOUNTS DEPARTMENT (KSAAD)")
    set_run_font(run, size=13, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, space_before=10, space_after=6)
    run = p.add_run(doc_title)
    set_run_font(run, size=18, bold=True, color=ACCENT)

    doc.add_paragraph()
    doc.add_page_break()

    # parse body
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("|"):
            rows, i = parse_table(lines, i)
            add_table(doc, rows)
            continue
        if stripped.startswith("### "):
            p = doc.add_heading(stripped[4:].strip(), level=2)
            style_paragraph(p, space_before=12, space_after=6)
            i += 1
            continue
        if stripped.startswith("## "):
            title = stripped[3:].strip()
            if title.lower() == "table of contents":
                # ignore TOC (usually not in our SOW anyway)
                i += 1
                continue
            p = doc.add_heading(title, level=1)
            style_paragraph(p, space_before=14, space_after=8)
            i += 1
            continue
        if stripped.startswith("# "):
            i += 1
            continue
        # unordered bullets
        if stripped.startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            style_paragraph(p, space_before=0, space_after=3)
            p.clear()
            add_formatted_runs(p, stripped[2:].strip(), size=11)
            i += 1
            continue
        # numbered list
        if re.match(r"^\\d+\\.\\s+", stripped):
            p = doc.add_paragraph(style="List Number")
            style_paragraph(p, space_before=0, space_after=3)
            p.clear()
            add_formatted_runs(p, re.sub(r"^\\d+\\.\\s+", "", stripped), size=11)
            i += 1
            continue

        # horizontal rule marker
        if stripped == "---":
            # insert blank line; Word borders not necessary for baseline
            doc.add_paragraph()
            i += 1
            continue

        # bold standalone lines
        if stripped.startswith("**") and stripped.endswith("**") and stripped.count("**") == 2:
            p = doc.add_paragraph()
            style_paragraph(p, space_before=8, space_after=4)
            run = p.add_run(stripped.strip("*"))
            set_run_font(run, size=11, bold=True, color=NAVY)
            i += 1
            continue

        p = doc.add_paragraph()
        style_paragraph(p, space_before=2, space_after=6)
        add_formatted_runs(p, stripped, size=11)
        i += 1

    add_page_numbers(doc, footer_label)
    return doc


def write_step1_sow(modules: List[ModuleDef]) -> None:
    # SOW is where module and feature IDs are seeded; no hours should appear.
    lines: List[str] = []

    lines += [
        f"# SoW {PROJECT_CODE} — Detailed Statement of Work",
        "",
        "## Introduction",
        "KSAAD requests a production-grade, workflow-driven digital platform covering audit operations, HRMS and office administration workflows,",
        "supported by auditable governance, role-based access control and integrated evidence handling.",
        "",
        "## Project Overview",
        f"The {PROJECT_NAME} platform will digitize end-to-end departmental processes across Head Office (HO), Regional Offices (ROs),",
        "Local Audit Circles (LACs) and Auditee Institutions to improve transparency, accountability and audit readiness.",
        "",
        "## Project Objectives",
        "- Standardize audit lifecycle and administrative workflows across units.",
        "- Provide reliable audit evidence management and traceable approvals.",
        "- Improve timeliness through configurable workflows and escalation triggers.",
        "- Provide MIS reporting, dashboards and exportable outputs for oversight.",
        "",
        "## In Scope / Out of Scope",
        "### In Scope",
        "- Functional modules listed in Section 6 (Consolidated Functional Modules).",
        "- Role-based access, maker-checker governance patterns and auditable logging.",
        "- Document management capabilities required for controlled evidence handling.",
        "- Reporting, dashboards and standard exports for audit, HR and office operations.",
        "",
        "### Out of Scope",
        "- Detailed technical architecture, class diagrams and UI wireframes (covered in design stage).",
        "- Hardware procurement, hosting infrastructure and AMC items unless separately ordered.",
        "- Classroom training and scanning bureau operations unless separately ordered.",
        "",
        "## Solution Expectations (Business-level Only)",
        "- Configuration-driven workflows and approvals.",
        "- Enterprise-grade audit traceability and evidence retention.",
        "- Usability for internal operations and role-scoped outputs for stakeholders.",
        "",
        "## Consolidated Functional Modules",
        "",
    ]

    # Module sections with key capabilities and feature IDs
    for m in modules:
        lines += [
            f"### {m.nn:02d}. {m.name}",
            f"**Purpose:** {m.summary}",
            "",
            "**Functional requirements:**",
            f"- Provide the required workflows and role-scoped processing aligned to KSAAD audit and administration practices.",
            f"- Enforce security, access controls, and audit-grade traceability.",
            f"- Provide reliable outputs for review, reporting and oversight.",
            "",
            "**Acceptance criteria:**",
            "- Transactions and approvals are processed through governed workflow states with complete history.",
            "- Role-scoped access prevents unauthorised viewing/acting.",
            "- Reporting and MIS outputs can be generated from controlled operational records.",
            "",
            "#### Key capabilities (feature outline)",
            "| Feature ID | Capability | Description |",
            "|---|---|---|",
        ]

        for f in m.features:
            fid = feature_id(m.nn, f.seq)
            cap = f.notes or f.objective
            desc = f.description.split(".")[0].strip()
            lines.append(f"| {fid} | {_md_cell(cap)} | {_md_cell(desc)} |")
        lines += ["", ""]

    lines += [
        "## End-to-End Workflows",
        "- RBAC and governance enabled entry into operational workspaces.",
        "- Transaction intake with maker-checker approvals and audit trail recording.",
        "- Document evidence handling and controlled access for review.",
        "- Reporting outputs and dashboard views for oversight and monitoring.",
        "",
        "## Access Control / RBAC",
        "Staff access is Person → Post → Role → Permissions. A Person is mapped to a Post; Roles and permissions attach to the Post. Approval routing uses the supervising Post on the Post master.",
        "Institution users (Module 16) are not staff Posts. Maker–checker applies where a change or transaction requires a checker. Every action is logged against the acting Person and Post.",
        "",
        "## Channels",
        "- Staff users with role-scoped access for operational execution.",
        "- Oversight and approval users for governed reviews and decisions.",
        "- Auditee institution users where the documents and approvals require institution participation.",
        "",
        "## Integrations",
        "- Internal platform services for workflow, reporting and evidence management.",
        "- Configurable integration hooks for interoperable data exchange with trusted systems where required by the programme.",
        "",
        "## Audit, Compliance & Security",
        "- Audit trail for actions, approvals and evidence references.",
        "- Secure authentication and permission checks.",
        "- Compliance reporting and secure access to evidence packs.",
        "",
        "## Non-Functional Requirements",
        "- Performance and availability suitable for enterprise operations.",
        "- Secure handling of confidential evidence and audit data.",
        "- Scalability for modular feature expansion.",
        "",
        "## Data Migration",
        "Legacy data migration is out of scope unless separately specified; reference configuration and master setups are handled through the platform.",
        "",
        "## Phased Delivery",
        "- Phase 1: Access governance, master configuration and evidence foundation.",
        "- Phase 2: HRMS and office administration workflows.",
        "- Phase 3: Audit planning and field execution capabilities.",
        "- Phase 4: Objections/recovery and billing/collections.",
        "- Phase 5: Integrations, reporting and knowledge services.",
        "- Phase 6: External and institution interaction rollout.",
        "",
        "## Deliverables",
        "- Production-grade modules, features and governed workflows.",
        "- Test-ready build with audit-grade evidence handling and role-based access enforcement.",
        "- Documentation for configuration, operation and maintenance handover.",
        "",
        "## Acceptance Criteria (Program Level)",
        "- End-to-end workflows execute with approvals and auditable history.",
        "- Reporting and dashboards reflect controlled operational records with correct access filters.",
        "- Evidence management supports controlled upload, versioning and sharing.",
        "",
        "## Expected Benefits",
        "- Improved audit readiness and compliance transparency.",
        "- Reduced manual workflows and improved timeliness.",
        "- Better visibility through operational dashboards and reporting exports.",
        "",
        "## Assumptions & Dependencies",
        "- KSAAD provides final role hierarchy and approval routing rules.",
        "- Integration targets are confirmed early for Module 12 work planning.",
        "- Document evidence handling requirements are clarified during design.",
        "",
        "## Vendor Response Expectations",
        "- Provide a production-quality build aligned to the functional scope and acceptance criteria.",
        "- Maintain traceability, validation and security for enterprise governance.",
        "",
        "## Appendices",
        "- Appendix A — Module & Feature Index (summary).",
        "",
        "| Module | Module Name | Type | Feature IDs (count) |",
        "|---|---|---|---|",
    ]
    for m in modules:
        fids = ", ".join(feature_id(m.nn, f.seq) for f in m.features)
        lines.append(f"| {m.nn:02d} | {m.name} | {m.module_type} | {fids} ({len(m.features)}) |")

    md = "\n".join(lines) + "\n"
    MD_PATH.write_text(md, encoding="utf-8")


def write_step7_client_docx(modules: List[ModuleDef], module_feature_rows: Dict[int, List[Tuple[str, str, int, str]]]) -> None:
    # Create client export based purely on generated feature indexes.
    # This mirrors the repo's SPLOCA approach (cover + tables) but removes pipeline mentions.
    grand = sum(sum(r[2] for r in rows) for rows in module_feature_rows.values())
    feature_count = sum(len(rows) for rows in module_feature_rows.values())

    doc = Document()
    section = doc.sections[0]
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    section.left_margin = Inches(0.95)
    section.right_margin = Inches(0.95)

    styles = doc.styles
    styles["Normal"].font.name = "Calibri"
    styles["Normal"].font.size = Pt(11)

    for _ in range(2):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("KARNATAKA STATE AUDIT & ACCOUNTS DEPARTMENT")
    set_run_font(run, size=14, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Client Copy · Effort in person-hours")
    set_run_font(run, size=12, bold=False, color=MUTED)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Module & Feature-wise Effort Estimate")
    set_run_font(run, size=20, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(PROJECT_NAME)
    set_run_font(run, size=16, bold=True, color=ACCENT)

    doc.add_page_break()

    # Purpose
    h = doc.add_heading("1. Purpose", level=1)
    style_paragraph(h, space_before=0, space_after=8)
    p = doc.add_paragraph()
    p.add_run(
        "This estimate sets out indicative person-hours to design, build, test and document "
        f"{PROJECT_NAME} as covered in the functional scope. Hours cover application software "
        "for the modules listed below and assume enterprise-grade build quality with validation, "
        "error handling, logging and security."
    )

    # Totals table
    h = doc.add_heading("2. Summary totals", level=1)
    style_paragraph(h, space_before=0, space_after=8)
    rows = [
        ["Item", "Person-hours"],
        ["Recommended go-live", f"{grand:,}"],
        ["Optional / conditional", "0"],
        ["All-in (this baseline)", f"{grand:,}"],
        ["Features", str(feature_count)],
        ["Modules", str(len(modules))],
    ]
    add_table(doc, rows)

    # Module-wise summary
    h = doc.add_heading("3. Module-wise summary", level=1)
    rows = [["Module", "Type", "Features", "Hours", "% of go-live"]]
    go = grand
    for m in modules:
        feats = module_feature_rows[m.nn]
        mhours = sum(r[2] for r in feats)
        pct = f"{(mhours / go * 100):.1f}%" if go else "0%"
        rows.append([f"{m.nn:02d}. {m.name}", m.module_type, str(len(feats)), f"{mhours:,}", pct])
    rows.append(["Total", "", str(feature_count), f"{grand:,}", "100%"])
    add_table(doc, rows)

    # Feature-wise estimate
    h = doc.add_heading("4. Feature-wise estimate", level=1)
    for m in modules:
        feats = module_feature_rows[m.nn]
        mhours = sum(r[2] for r in feats)
        doc.add_heading(f"{m.nn:02d}. {m.name} — {mhours:,} hours", level=2)
        frows = [["Feature ID", "Feature Name", "Hours", "Notes"]]
        for fid, fname, hours, notes in feats:
            frows.append([fid, fname, str(hours), str(notes).replace("|", "/")])
        add_table(doc, frows)

    # Exclusions
    h = doc.add_heading("5. Items not included in feature hours", level=1)
    for e in [
        "Hosting infrastructure and annual maintenance (AMC), unless separately ordered.",
        "Hardware procurement and deployment tickets.",
        "Classroom training and scanning bureau operations, unless separately ordered.",
    ]:
        doc.add_paragraph(e, style="List Bullet")

    # Assumptions
    h = doc.add_heading("6. Planning assumptions", level=1)
    for a in [
        "Role hierarchy and approval routing rules must be confirmed with KSAAD for correct maker-checker behaviour.",
        "Document handling requirements should be finalised early for evidence packs and controlled sharing.",
        "Integration targets for interoperable exchanges should be confirmed during design planning to avoid delivery risk.",
    ]:
        doc.add_paragraph(a, style="List Bullet")

    h = doc.add_heading("7. Disclaimer", level=1)
    doc.add_paragraph(
        "These figures are indicative person-hours for planning and commercial discussion. "
        "They assume a production-quality build with validation, error handling, logging, security and unit testing."
    )

    add_page_numbers(doc, PROJECT_NAME)
    out = ROOT / f"{PROJECT_CODE}_Estimation_Summary_FeatureWise_Client.docx"
    doc.save(out)
    print(f"Wrote {out}")


def main() -> None:
    modules = build_modules()

    modules_root = ROOT / "modules"
    if modules_root.exists():
        shutil.rmtree(modules_root)

    # Step 2–3: modules file and folders
    write_modules_file(modules)
    for m in modules:
        write_module_folder_readme(m)

    # Step 5: features and per-module indexes + data to registry/summaries
    feature_rows: Dict[int, List[Tuple[str, str, int, str]]] = {}
    feature_map_for_registry: Dict[int, List[Dict[str, Any]]] = {}

    for m in modules:
        rows: List[Tuple[str, str, int, str]] = []
        feat_entries: List[Dict[str, Any]] = []
        module_slug = slugify(m.name)
        for f in m.features:
            fid, total, fname, notes = write_feature_file(m, f)
            fslug = slugify(fname)
            seq = f.seq
            file = f"modules/{m.nn:02d}-{module_slug}/features/{feature_filename(m.nn, seq, fslug)}"
            feat_entries.append(
                {
                    "id": fid,
                    "seq": f"{seq:03d}",
                    "name": fname,
                    "slug": fslug,
                    "file": file,
                    "hours": total,
                }
            )
            rows.append((fid, fname, total, notes))
        write_module_index(m, rows)
        feature_rows[m.nn] = rows
        feature_map_for_registry[m.nn] = feat_entries

    # Step 3 capture: registry
    write_registry(modules, feature_map_for_registry)

    # Step 6 summaries
    write_internal_summaries(modules, feature_rows)

    # Step 1: SOW (after modules/features exist; but SOW needs IDs—IDs are stable)
    write_step1_sow(modules)
    doc = markdown_to_docx(MD_PATH.read_text(encoding="utf-8"), "Detailed Statement of Work (SOW)", "KSAAD SOW")
    doc.save(DOCX_PATH)
    print(f"Wrote {DOCX_PATH}")

    # Step 7: client export
    write_step7_client_docx(modules, feature_rows)


if __name__ == "__main__":
    main()

