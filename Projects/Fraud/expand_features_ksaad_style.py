#!/usr/bin/env python3
"""Rewrite Fraud feature files to the KSAAD estimation grain.

Keeps each feature's domain specification. Adds the 8-step who/how journey,
named screens, logical APIs, and bills each screen/API independently using
the Estimation Master (same pattern as KSAAD_HRMS).
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent

UI_HOURS = {"Simple": 2, "Easy": 4, "Medium": 6, "Complex": 12, "Very High": 16}
API_HOURS = {"Simple": 2, "Easy": 4, "Medium": 6, "Complex": 8, "Very High": 16}
DB_HOURS = {"Simple": 1, "Easy": 2, "Medium": 4, "Complex": 6, "Very High": 10}
INTEGRATION_HOURS = {"Simple": 4, "Easy": 8, "Medium": 16, "Complex": 24, "Very High": 40}
TESTING_HOURS = {"Simple": 2, "Easy": 4, "Medium": 6, "Complex": 8, "Very High": 12}
DOC_HOURS = {"Simple": 1, "Easy": 2, "Medium": 3, "Complex": 4, "Very High": 6}

HOURS = {
    "UI": UI_HOURS,
    "API": API_HOURS,
    "DB": DB_HOURS,
    "Integration": INTEGRATION_HOURS,
    "Testing": TESTING_HOURS,
    "Documentation": DOC_HOURS,
}

PROJECTS = [
    ROOT / "ClaimManagement",
    ROOT / "LegalManagement",
    ROOT / "Valuation",
]


def hours_for(category: str, complexity: str) -> int:
    return HOURS[category][complexity]


def md_cell(text: str) -> str:
    return str(text).replace("|", "/").replace("\n", " ").strip()


def section_body(text: str, heading: str) -> str:
    pat = rf"^### {re.escape(heading)}\s*\n(.*?)(?=^### |^## |\Z)"
    m = re.search(pat, text, re.M | re.S)
    body = m.group(1).strip() if m else ""
    body = re.split(r"^## ", body, maxsplit=1, flags=re.M)[0].strip()
    return body


def numbered_items(block: str) -> List[str]:
    items = []
    for line in block.splitlines():
        m = re.match(r"^\d+\.\s+(.*)$", line.strip())
        if m:
            items.append(m.group(1).strip())
    return items


def bullet_items(block: str) -> List[str]:
    items = []
    for line in block.splitlines():
        m = re.match(r"^[-*]\s+(.*)$", line.strip())
        if m:
            items.append(m.group(1).strip())
    if items:
        return items
    return [block.strip()] if block.strip() else []


def parse_est_table(text: str) -> List[Tuple[str, str, str, int]]:
    chunks = re.split(r"^## Section 2[^\n]*\n", text, flags=re.M)
    body = chunks[-1] if len(chunks) > 1 else ""
    rows: List[Tuple[str, str, str, int]] = []
    for line in body.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0] in {"Artifact", "---", "**Total**"} or cells[0].startswith("---"):
            continue
        if cells[0].startswith("**"):
            continue
        name, cat, comp, hrs = cells[0], cells[1], cells[2], cells[3]
        if cat not in HOURS:
            continue
        try:
            h = int(re.sub(r"[^\d]", "", hrs) or "0")
        except ValueError:
            h = hours_for(cat, comp) if comp in HOURS[cat] else 0
        rows.append((name, cat, comp, h))
    return rows


def header_field(text: str, field: str) -> str:
    m = re.search(rf"\|\s*\*\*{re.escape(field)}\*\*\s*\|\s*(.*?)\s*\|", text)
    return m.group(1).strip() if m else ""


def noun_of(name: str) -> str:
    n = re.sub(r"\s*\([^)]*\)\s*", " ", name).strip().lower()
    n = re.sub(r"\s+", " ", n)
    return n or "record"


def classify(name: str, journey: str, workflow: str) -> str:
    n = name.lower()
    blob = f"{name}\n{journey}\n{workflow}".lower()
    if re.search(r"\bmaster\b|catalogue|catalog|coding$", n):
        return "master"
    if re.search(
        r"\binbox\b|maker.?checker|approve or reject|approves or rejects|"
        r"pending clarification|decision panel|submit for (checker|approval)",
        blob,
    ):
        return "txn"
    if re.search(r"\bapproval decisions\b|\bapprover\b", n):
        return "txn"
    return "work"


def split_actors(actors: str, kind: str, name: str) -> Tuple[str, str]:
    parts = [re.sub(r"\.+$", "", p.strip()) for p in re.split(r";|/", actors) if p.strip()]
    first = parts[0] if parts else "Authorised user"
    second = parts[1] if len(parts) > 1 else "Supervising Post / Competent Authority where a decision exists"
    if kind == "txn" and re.search(r"decision|approval|review and", name, re.I):
        return second if len(parts) > 1 else "The officer who submitted the record", first
    return first, second


def eight_journey(
    kind: str,
    maker: str,
    approver: str,
    steps: List[str],
    workflow: str,
    name: str,
) -> List[str]:
    maker = re.sub(r"\.+$", "", maker).strip()
    approver = re.sub(r"\.+$", "", approver).strip()
    s0 = steps[0] if steps else f"{maker} opens {name}."
    s1 = steps[1] if len(steps) > 1 else f"{maker} updates the record and saves."
    s2 = steps[2] if len(steps) > 2 else (steps[-1] if steps else workflow)
    rest = " ".join(steps[3:]) if len(steps) > 3 else ""
    if kind == "txn":
        return [
            f"Who creates: {maker}",
            f"How they create: {s0}",
            f"How they edit: {s1} Draft or returned records can be edited; decided records are not silently overwritten.",
            f"How they send for approval: {s2} {workflow}".strip(),
            f"How the approver sees pending items: {approver} opens the pending inbox for this feature and opens a row.",
            f"How the approver decides: {approver} approves, rejects or returns with remarks. {rest}".strip(),
            f"How the applicant sees history: {maker} opens history on the record (actor Person, Post, time, status, remarks).",
            f"How the approver / auditor sees history: {approver} and auditor open the same history for items in their scope.",
        ]
    if kind == "master":
        return [
            f"Who creates: {maker}",
            f"How they create: {s0}",
            f"How they edit: {s1}",
            f"How they send for approval: {s2 if 'check' in (workflow + s2).lower() or 'approv' in (workflow + s2).lower() else workflow or 'Create/update is saved with audit. Checker applies only if this master requires maker–checker.'}",
            f"How the approver sees pending items: {'Checker opens the pending change inbox.' if 'check' in workflow.lower() or 'approv' in workflow.lower() else 'No approval inbox unless maker–checker is later required. Auditor opens the register.'}",
            f"How the approver decides: {'Checker approves or rejects with remarks.' if 'check' in workflow.lower() or 'approv' in workflow.lower() else 'No decision on this master beyond save; auditor reads history.'}",
            f"How the maker sees history: {maker} opens change history on the record (who changed what, when).",
            f"How the checker / auditor sees history: Auditor (and checker if used) open the same history.",
        ]
    return [
        f"Who creates: {maker}",
        f"How they create: {s0}",
        f"How they edit: {s1}",
        f"How they send for approval: {s2} {workflow}".strip(),
        f"How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. {maker} works from the register or workbench.",
        f"How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.",
        f"How the user sees history: {maker} opens history on the record. {rest}".strip(),
        f"How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.",
    ]


def merge_named(
    base: List[Tuple[str, str]],
    existing: List[Tuple[str, str]],
) -> List[Tuple[str, str]]:
    out = list(base)
    have = {n.lower() for n, _ in out}
    for name, comp in existing:
        if name.lower() not in have:
            out.append((name, comp))
            have.add(name.lower())
    return out


def artefacts_for(
    kind: str,
    name: str,
    noun: str,
    existing: List[Tuple[str, str, str, int]],
) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]], str, str]:
    existing_ui = [(n, c) for n, cat, c, _ in existing if cat == "UI"]
    existing_api = [(n, c) for n, cat, c, _ in existing if cat == "API"]
    existing_db = [(n, c) for n, cat, c, _ in existing if cat == "DB"]
    existing_int = [(n, c) for n, cat, c, _ in existing if cat == "Integration"]
    existing_test = next((c for n, cat, c, _ in existing if cat == "Testing"), "Complex")
    existing_doc = next((c for n, cat, c, _ in existing if cat == "Documentation"), "Medium")

    form_c = next((c for n, c in existing_ui if re.search(r"form|workbench|matrix|wizard|canvas|editor", n, re.I)), None)
    primary_ui = existing_ui[0] if existing_ui else None

    if kind == "txn":
        form_name, form_comp = (primary_ui if primary_ui else (f"{noun.capitalize()} form (create and edit)", "Complex"))
        if primary_ui and re.search(r"register|inbox|history", primary_ui[0], re.I) and len(existing_ui) > 1:
            form_name, form_comp = existing_ui[1]
        ui = [
            (f"My {noun} register", "Medium"),
            (form_name, form_comp),
            ("Submit confirmation", "Simple"),
            (f"Approver {noun} inbox", "Complex"),
            (f"{noun.capitalize()} decision panel (approve / reject / return)", "Medium"),
            (f"My {noun} history", "Medium"),
            (f"Team {noun} history (approver)", "Medium"),
        ]
        api = [
            (f"Save draft {noun}", "Medium"),
            (f"Update draft {noun}", "Medium"),
            (existing_api[0][0] if existing_api else f"Submit {noun} for approval", existing_api[0][1] if existing_api else "Complex"),
            (f"Withdraw {noun}", "Easy"),
            ("Approver inbox query", "Medium"),
            (f"Approve, reject or return {noun}", "Complex"),
            ("Applicant history query", "Medium"),
            ("Team history query", "Medium"),
        ]
        db = existing_db or [(f"{noun.capitalize()} record and status history", "Medium")]
        integration = existing_int  # only real channels already estimated
        ui = merge_named(ui, [x for x in existing_ui if x[0].lower() not in {u[0].lower() for u in ui}])
        api = merge_named(api, existing_api[1:])
        testing = existing_test if existing_test in TESTING_HOURS else "Very High"
        documentation = existing_doc if existing_doc in DOC_HOURS else "Medium"
        return ui, api, db, integration, testing, documentation

    if kind == "master":
        reg = existing_ui[0] if existing_ui else (f"{noun.capitalize()} register + search", "Complex")
        form = existing_ui[1] if len(existing_ui) > 1 else (f"{noun.capitalize()} create/edit form", form_c or "Medium")
        if len(existing_ui) == 1:
            form = (f"{noun.capitalize()} create/edit form", "Medium")
        ui = [reg, form, (f"{noun.capitalize()} change history", "Medium")]
        api = [
            (existing_api[0][0] if existing_api else f"Create {noun}", existing_api[0][1] if existing_api else "Complex"),
            (f"Update {noun}", "Medium"),
            (f"Search {noun} register", "Medium"),
            (f"Read {noun} change history", "Easy"),
        ]
        db = existing_db or [(f"{noun.capitalize()} identity persistence", "Medium")]
        integration = existing_int or [(f"Internal handoff of {noun} to consuming modules", "Simple")]
        ui = merge_named(ui, existing_ui[2:])
        api = merge_named(api, existing_api[1:])
        return ui, api, db, integration, existing_test, existing_doc

    if len(existing_ui) == 1:
        ui = [
            (f"My {noun} list / queue", "Medium"),
            existing_ui[0],
            (f"{noun.capitalize()} history", "Medium"),
        ]
    elif existing_ui:
        ui = list(existing_ui)
        if not any("history" in n.lower() for n, _ in ui):
            ui.append((f"{noun.capitalize()} history", "Medium"))
    else:
        ui = [
            (f"{noun.capitalize()} register", "Medium"),
            (f"{noun.capitalize()} form (create and edit)", "Complex"),
            (f"{noun.capitalize()} history", "Medium"),
        ]
    api = [
        (existing_api[0][0] if existing_api else f"Save {noun}", existing_api[0][1] if existing_api else "Complex"),
        (f"Update {noun}", "Medium"),
        (f"Search {noun}", "Medium"),
        (f"Read {noun} history", "Easy"),
    ]
    db = existing_db or [(f"{noun.capitalize()} persistence", "Medium")]
    integration = existing_int
    api = merge_named(api, existing_api[1:])
    testing = existing_test if existing_test in TESTING_HOURS else "Complex"
    documentation = existing_doc if existing_doc in DOC_HOURS else "Medium"
    return ui, api, db, integration, testing, documentation


def render_feature(
    *,
    fid: str,
    name: str,
    module: str,
    description: str,
    objective: str,
    actors: str,
    journey: List[str],
    capabilities: str,
    ui: List[Tuple[str, str]],
    api: List[Tuple[str, str]],
    inputs: str,
    outputs: str,
    rules: str,
    validations: str,
    calculations: str,
    workflow: str,
    search: str,
    documents: str,
    reports: str,
    notifications: str,
    security: str,
    integrations: str,
    dependencies: str,
    assumptions: str,
    risks: str,
    nfr: str,
    db: List[Tuple[str, str]],
    integration: List[Tuple[str, str]],
    testing: str,
    documentation: str,
) -> Tuple[str, int]:
    def bullets(block: str) -> str:
        items = bullet_items(block)
        if not items:
            return block
        if all(i.startswith("- ") or True for i in items):
            return "\n".join(f"- {i.lstrip('- ').strip()}" for i in items if i.strip())
        return block

    ui_table = "\n".join(f"| {md_cell(n)} | {c} |" for n, c in ui)
    api_table = "\n".join(f"| {md_cell(n)} | {c} |" for n, c in api)
    est: List[Tuple[str, str, str, int]] = []
    for n, c in ui:
        est.append((n, "UI", c, hours_for("UI", c)))
    for n, c in api:
        est.append((n, "API", c, hours_for("API", c)))
    for n, c in db:
        est.append((n, "DB", c, hours_for("DB", c)))
    for n, c in integration:
        est.append((n, "Integration", c, hours_for("Integration", c)))
    est.append((f"{name} feature tests", "Testing", testing, hours_for("Testing", testing)))
    est.append((f"{name} implementation documentation", "Documentation", documentation, hours_for("Documentation", documentation)))
    total = sum(h for *_, h in est)
    est_table = "\n".join(f"| {md_cell(n)} | {cat} | {c} | {h} |" for n, cat, c, h in est)
    journey_md = "\n".join(f"{i}. {j}" for i, j in enumerate(journey, 1))

    md = f"""# {fid} — {name}

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | {fid} |
| **Feature Name** | {name} |
| **Module** | {module} |

### Description
{description}

### Business Objective
{objective}

### Actors
{actors}

### User Journey
{journey_md}

### Functional Capabilities
{bullets(capabilities)}

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
{inputs}

### Outputs
{outputs}

### Business Rules
{bullets(rules)}

### Validations
{bullets(validations)}

### Calculations
{calculations}

### Workflow
{workflow}

### Search Requirements
{search}

### Documents
{documents}

### Reports
{reports}

### Notifications
{notifications}

### Security
{security}

### Integrations
{integrations}

### Dependencies
{dependencies}

### Assumptions
{bullets(assumptions)}

### Risks
{risks}

### Non Functional Requirements
{nfr}

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
    return md, total


def rewrite_file(path: Path) -> Tuple[str, str, int]:
    text = path.read_text(encoding="utf-8")
    fid = header_field(text, "Feature ID") or path.stem.split("-")[0] + "-" + path.stem.split("-")[1]
    name = header_field(text, "Feature Name")
    module = header_field(text, "Module")
    description = section_body(text, "Description")
    objective = section_body(text, "Business Objective")
    actors = section_body(text, "Actors")
    journey_block = section_body(text, "User Journey")
    steps = numbered_items(journey_block)
    capabilities = section_body(text, "Functional Capabilities")
    inputs = section_body(text, "Inputs")
    outputs = section_body(text, "Outputs")
    rules = section_body(text, "Business Rules")
    validations = section_body(text, "Validations")
    calculations = section_body(text, "Calculations")
    workflow = section_body(text, "Workflow")
    search = section_body(text, "Search Requirements")
    documents = section_body(text, "Documents")
    reports = section_body(text, "Reports")
    notifications = section_body(text, "Notifications")
    security = section_body(text, "Security")
    integrations = section_body(text, "Integrations")
    dependencies = section_body(text, "Dependencies")
    assumptions = section_body(text, "Assumptions")
    risks = section_body(text, "Risks")
    nfr = section_body(text, "Non Functional Requirements")
    existing = parse_est_table(text)
    kind = classify(name, journey_block, workflow)
    noun = noun_of(name)
    maker, approver = split_actors(actors, kind, name)
    if steps and steps[0].lower().startswith("who creates"):
        steps = [
            re.sub(r"^(Who creates|How they [^:]+|How the [^:]+):\s*", "", s, flags=re.I).strip()
            for s in steps
        ]
        steps = [s for s in steps if s][:4]
    journey = eight_journey(kind, maker, approver, steps, workflow, name)
    ui, api, db, integration, testing, documentation = artefacts_for(kind, name, noun, existing)
    md, total = render_feature(
        fid=fid,
        name=name,
        module=module,
        description=description,
        objective=objective,
        actors=actors,
        journey=journey,
        capabilities=capabilities,
        ui=ui,
        api=api,
        inputs=inputs,
        outputs=outputs,
        rules=rules,
        validations=validations,
        calculations=calculations,
        workflow=workflow,
        search=search,
        documents=documents,
        reports=reports,
        notifications=notifications,
        security=security,
        integrations=integrations,
        dependencies=dependencies,
        assumptions=assumptions,
        risks=risks,
        nfr=nfr,
        db=db,
        integration=integration,
        testing=testing,
        documentation=documentation,
    )
    path.write_text(md, encoding="utf-8")
    return fid, name, total


def update_index(idx: Path, hours_by_id: Dict[str, int]) -> int:
    text = idx.read_text(encoding="utf-8")
    lines = []
    total = 0
    for line in text.splitlines():
        if re.match(r"^\|\s*F\d{2}-\d{3}\s*\|", line.strip()):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            fid = cells[0]
            if fid in hours_by_id and len(cells) >= 3:
                cells[2] = str(hours_by_id[fid])
                total += hours_by_id[fid]
                line = "| " + " | ".join(cells) + " |"
            elif len(cells) >= 3:
                total += int(re.sub(r"[^\d]", "", cells[2]) or "0")
        if re.search(r"\*\*Module Total:\*\*", line):
            line = f"**Module Total:** **{total}** hours"
        lines.append(line)
    idx.write_text("\n".join(lines) + ("\n" if not text.endswith("\n") else ""), encoding="utf-8")
    return total


def expand_project(root: Path) -> None:
    reg_path = next(root.glob("*_Registry.json"))
    reg = json.loads(reg_path.read_text(encoding="utf-8"))
    for mod in reg["modules"]:
        folder = root / mod["folder"] / "features"
        hours_by_id: Dict[str, int] = {}
        for feat in mod["features"]:
            fpath = root / feat["file"]
            if not fpath.exists():
                raise SystemExit(f"Missing {fpath}")
            fid, _name, total = rewrite_file(fpath)
            hours_by_id[fid] = total
            feat["hours"] = total
        idx = folder / "_index.md"
        module_total = update_index(idx, hours_by_id)
        mod["total_hours"] = module_total
        mod["feature_count"] = len(mod["features"])
    reg["updated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg_path.write_text(json.dumps(reg, indent=2) + "\n", encoding="utf-8")
    grand = sum(m["total_hours"] for m in reg["modules"])
    fcount = sum(m["feature_count"] for m in reg["modules"])
    print(f"{reg.get('project_code', root.name)}: {fcount} features, {grand} hours")


def main() -> None:
    for proj in PROJECTS:
        expand_project(proj)


if __name__ == "__main__":
    main()
