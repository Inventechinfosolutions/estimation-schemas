#!/usr/bin/env python3
"""Convert SoW_CDRMS_Detailed.md to a professionally formatted Word document."""

from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

ROOT = Path(__file__).resolve().parent
MD_PATH = ROOT / "SoW_CDRMS_Detailed.md"
DOCX_PATH = ROOT / "SoW_CDRMS_Detailed.docx"

NAVY = RGBColor(0x1B, 0x3A, 0x5F)
ACCENT = RGBColor(0x2E, 0x5A, 0x88)
HEADER_BG = "1B3A5F"
ALT_ROW = "F3F6FA"
MUTED = RGBColor(0x55, 0x55, 0x55)


def set_run_font(run, *, size=11, bold=False, color=None, name="Calibri"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    if color is not None:
        run.font.color.rgb = color


def add_formatted_runs(paragraph, text: str, *, size=11, color=None):
    """Render markdown-ish **bold** and strip [link](url) to link text."""
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            set_run_font(run, size=size, bold=True, color=color)
        else:
            run = paragraph.add_run(part)
            set_run_font(run, size=size, bold=False, color=color)


def set_cell_shading(cell, hex_color: str):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), hex_color)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


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


def style_paragraph(p, *, space_before=0, space_after=6, line_spacing=1.15):
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line_spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE


def parse_table(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    rows = []
    i = start
    while i < len(lines) and lines[i].strip().startswith("|"):
        row = lines[i].strip()
        if re.match(r"^\|[\s\-|:]+\|$", row):
            i += 1
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        rows.append(cells)
        i += 1
    return rows, i


def add_table(doc: Document, rows: list[list[str]]):
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


def add_horizontal_line(doc: Document):
    p = doc.add_paragraph()
    style_paragraph(p, space_before=4, space_after=10)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "12")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "1B3A5F")
    pBdr.append(bottom)
    pPr.append(pBdr)


def build_cover(doc: Document, meta: dict[str, str]):
    for _ in range(3):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("BANGALORE DEVELOPMENT AUTHORITY (BDA)")
    set_run_font(run, size=14, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, space_before=18, space_after=6)
    run = p.add_run("Statement of Work (SOW)")
    set_run_font(run, size=20, bold=True, color=NAVY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    style_paragraph(p, space_before=6, space_after=18)
    run = p.add_run("Correct Dimension Report Management System (CDRMS)")
    set_run_font(run, size=16, bold=True, color=ACCENT)

    add_horizontal_line(doc)

    for key in ("Document Type", "Version", "Status", "Prepared by"):
        if key in meta:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            style_paragraph(p, space_before=2, space_after=2)
            run = p.add_run(f"{key}: ")
            set_run_font(run, size=11, bold=True, color=MUTED)
            run = p.add_run(meta[key])
            set_run_font(run, size=11, color=MUTED)

    doc.add_page_break()


def configure_styles(doc: Document):
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


def add_page_numbers(doc: Document):
    section = doc.sections[0]
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("BDA | CDRMS Statement of Work  |  Page ")
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


def convert(md_text: str) -> Document:
    lines = md_text.splitlines()
    doc = Document()
    configure_styles(doc)

    # Extract cover meta from early bold lines
    meta: dict[str, str] = {}
    body_start = 0
    for i, line in enumerate(lines):
        m = re.match(r"\*\*(.+?):\*\*\s*(.+)", line.strip())
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
        if line.startswith("## Table of Contents"):
            body_start = i
            break

    build_cover(doc, meta)

    # Skip title H1s and meta; start from TOC or Introduction
    i = body_start
    skip_toc = True  # Word TOC not needed as static list; keep it as a section

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            add_horizontal_line(doc)
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
            if title == "Table of Contents" and skip_toc:
                # Include TOC as a clean numbered list without markdown links
                p = doc.add_heading(title, level=1)
                style_paragraph(p, space_before=6, space_after=8)
                i += 1
                while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and lines[i].strip() != "---":
                    item = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", lines[i].strip())
                    bp = doc.add_paragraph(style="List Number")
                    style_paragraph(bp, space_before=0, space_after=2)
                    bp.clear()
                    add_formatted_runs(bp, item, size=10)
                    i += 1
                continue
            p = doc.add_heading(title, level=1)
            style_paragraph(p, space_before=14, space_after=8)
            i += 1
            continue

        if stripped.startswith("# "):
            # Already used on cover
            i += 1
            continue

        if stripped.startswith("- "):
            # Nested bullets: lines starting with spaces then -
            indent = len(line) - len(line.lstrip(" "))
            style = "List Bullet"
            p = doc.add_paragraph(style=style)
            if indent >= 2:
                p.paragraph_format.left_indent = Inches(0.35)
            style_paragraph(p, space_before=0, space_after=3)
            p.clear()
            add_formatted_runs(p, stripped[2:].strip(), size=11)
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            p = doc.add_paragraph(style="List Number")
            style_paragraph(p, space_before=0, space_after=3)
            p.clear()
            add_formatted_runs(p, re.sub(r"^\d+\.\s+", "", stripped), size=11)
            i += 1
            continue

        if stripped.startswith("**") and stripped.endswith("**") and stripped.count("**") == 2:
            p = doc.add_paragraph()
            style_paragraph(p, space_before=8, space_after=4)
            run = p.add_run(stripped.strip("*"))
            set_run_font(run, size=11, bold=True, color=NAVY)
            i += 1
            continue

        if stripped.startswith("**End of Statement"):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            style_paragraph(p, space_before=18, space_after=6)
            run = p.add_run(stripped.strip("*"))
            set_run_font(run, size=10, bold=True, color=MUTED)
            i += 1
            continue

        # Normal paragraph
        p = doc.add_paragraph()
        style_paragraph(p, space_before=2, space_after=6)
        add_formatted_runs(p, stripped, size=11)
        i += 1

    add_page_numbers(doc)
    return doc


def main():
    md = MD_PATH.read_text(encoding="utf-8")
    doc = convert(md)
    doc.save(DOCX_PATH)
    print(f"Wrote {DOCX_PATH}")


if __name__ == "__main__":
    main()
