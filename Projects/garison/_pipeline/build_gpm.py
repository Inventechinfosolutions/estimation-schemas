"""Build GPM (Option B — product migration) estimation artefacts.

Run from repo root:
    .venv/bin/python Projects/garison/_pipeline/build_gpm.py
"""
from __future__ import annotations

import datetime as dt
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_gmc as b  # noqa: E402
from gpm_data import FEATURES  # noqa: E402

ROOT = HERE.parent / "Option-B-Product-Migration"
CODE = "GPM"
PROJECT = "Garrison Catalogue Product Migration to Existing Website (Option B)"
TODAY = dt.date.today().isoformat()

PLANNED_PRODUCTS = 350
CONFIRMED_PRODUCTS = 201
VERIFY_RATE = 0.25
MANUAL_RATE = 0.75

MODULES = [
    dict(nn="01", name="Catalogue Data Extraction & Preparation", type="Technical",
         summary="Throttled extraction, image optimisation, normalisation and Garrison review workbook",
         source="Explicit (client request); F01-005 Optional",
         in_scope="Moulding products and images from the source catalogue; normalisation; review workbook",
         out_scope="New content creation; doors and sheet goods unless F01-005 is taken",
         actors="Delivery developer; Garrison catalogue owner (review)", deps="Brenlo permission; F04-001",
         notes="Supplier data file can replace extraction if Brenlo provides one"),
    dict(nn="02", name="Product Data Store on Existing Website", type="Technical",
         summary="Product storage, idempotent loader with rollback, media hosting",
         source="Derived", in_scope="Data store in existing stack; loader; media sync",
         out_scope="Admin portal", actors="Delivery developer", deps="F04-001",
         notes="Developer-maintained; no admin portal"),
    dict(nn="03", name="Catalogue Pages on Existing Website", type="Business",
         summary="Landing page, category listings with filters, product detail, search, enquiry handoff",
         source="Explicit (client request); F03-006 Optional",
         in_scope="Public catalogue templates in existing theme", out_scope="Customer accounts, quotes, e-commerce",
         actors="Visitor", deps="Module 02; F04-002", notes="Fixed fields and filters"),
    dict(nn="04", name="Website Integration, SEO & Go-live", type="Shared",
         summary="Code onboarding, environments, navigation/theme, SEO, reconciliation and go-live",
         source="Derived", in_scope="Staging, backup, theme integration, SEO, UAT, deployment",
         out_scope="Hosting migration, SSL remediation, redesign", actors="Delivery developer; Garrison hosting contact",
         deps="Garrison source code and access", notes="Changes only via staging with rollback"),
]

b.ROOT, b.CODE, b.PROJECT, b.FEATURES, b.MODULES = ROOT, CODE, PROJECT, FEATURES, MODULES
for m in MODULES:
    m["slug"] = b.slugify(m["name"])
    m["folder"] = f"modules/{m['nn']}-{m['slug']}"
for f in FEATURES:
    f.setdefault("notes", "Go-live")
    f["slug"] = b.slugify(f["name"])
    f["nn"], f["seq"] = f["id"][1:3], f["id"][4:]
    f["hours"] = sum(r[3] for r in b.rows(f))
    f["areas"] = b.area_totals(f)

feats, totals, area_sum, pct, add_table, base_doc = b.feats, b.totals, b.area_sum, b.pct, b.add_table, b.base_doc


def volume_hours(n=PLANNED_PRODUCTS, rate=VERIFY_RATE):
    return math.ceil(n * rate)


def write_modules_and_registry():
    out = [f"# {PROJECT} — Module List", "", f"Source: `SoW_{CODE}_Detailed.md`", "",
           "| # | Module | Type | Summary | Source |", "|---|--------|------|---------|--------|"]
    out += [f"| {m['nn']} | {m['name']} | {m['type']} | {m['summary']} | {m['source'].split(' ')[0]} |" for m in MODULES]
    out += ["", "---", "", "## Module Details", ""]
    for m in MODULES:
        out += [f"### {m['nn']}. {m['name']}", "", f"- **Type:** {m['type']}", f"- **Summary:** {m['summary']}.",
                f"- **Source:** {m['source']}", f"- **In Scope:** {m['in_scope']}", f"- **Out of Scope:** {m['out_scope']}",
                f"- **Key Actors:** {m['actors']}", f"- **Dependencies:** {m['deps']}", f"- **Notes:** {m['notes']}",
                "- **Features:** " + ", ".join(f"{f['id']} {f['name']}" for f in feats(m)), ""]
    (ROOT / f"{CODE}_Modules.md").write_text("\n".join(out))

    all_h, go, opt = totals()
    reg = dict(project_code=CODE, project_name=PROJECT, client=b.CLIENT, output_root="Projects/garison/Option-B-Product-Migration",
               related_estimate="GMC (Option A — full catalogue platform)", sow=f"SoW_{CODE}_Detailed.md",
               updated_at=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               volume=dict(planned_products=PLANNED_PRODUCTS, confirmed_products=CONFIRMED_PRODUCTS,
                           verification_rate_hours=VERIFY_RATE, manual_capture_rate_hours=MANUAL_RATE,
                           verification_hours=volume_hours()),
               totals=dict(software_go_live_hours=go, software_optional_hours=opt, software_all_hours=all_h,
                           go_live_including_verification=go + volume_hours(), feature_count=len(FEATURES), module_count=len(MODULES)),
               modules=[dict(nn=m["nn"], name=m["name"], slug=m["slug"], type=m["type"], folder=m["folder"],
                             feature_count=len(feats(m)), total_hours=m["hours"],
                             features=[dict(id=f["id"], seq=f["seq"], name=f["name"], slug=f["slug"], file=f["file"],
                                            hours=f["hours"], notes=f["notes"], areas=f["areas"]) for f in feats(m)]) for m in MODULES])
    (ROOT / f"{CODE}_Registry.json").write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n")


def write_summaries():
    all_h, go, opt = totals()
    vh = volume_hours()
    areas = area_sum(FEATURES)
    s = [f"# {CODE} — Estimation Summary (Internal)", "", f"**Project:** {PROJECT}  ", f"**Client:** {b.CLIENT}  ",
         f"**Project code:** {CODE}  ", f"**As of:** {TODAY}  ", "**Related estimate:** GMC — Option A, full catalogue platform (`../GMC_Estimation_Summary.md`)", "",
         "## Totals", "", "| Metric | Hours |", "|--------|------:|",
         f"| Software — go-live features | {go} |",
         f"| Per-product verification ({PLANNED_PRODUCTS} products × {VERIFY_RATE} h) | {vh} |",
         f"| **Recommended go-live total** | **{go + vh}** |",
         f"| Optional features (F01-005 doors/in-stock, F03-006 combinations) | {opt} |",
         f"| All-in (excluding optional per-product verification for doors/in-stock) | {all_h + vh} |", "",
         "## Source catalogue sizing", "",
         f"- Confirmed: **{CONFIRMED_PRODUCTS} moulding products** in 21 categories (Baseboard 45, Casing 41, Backband 21, D4S 21, Crown 18, Doorstop 10, Inspire 9, Cove 7, others ≤ 5).",
         "- Not countable remotely: 16 multi-word categories (for example Chair Rail, Quarter Round, Half Round, Panel Mould, Base Shoe, Window Stool, Tongue & Groove, Plinth/Corner Block) and Combinations — the source returned access errors for these URLs.",
         f"- Planning quantity: **{PLANNED_PRODUCTS}**. Variance charged at {VERIFY_RATE} h per product (automated path) or {MANUAL_RATE} h per product if manual capture is needed.",
         "- Data per product: category, code, thickness × width, style, species options, one isometric image (about 541×402 px). No drawings, PDFs or descriptions.", "",
         "## Per-module hours", "", "| # | Module | Type | Features | Hours |", "|---|--------|------|---------:|------:|"]
    s += [f"| {m['nn']} | {m['name']} | {m['type']} | {len(feats(m))} | {m['hours']} |" for m in MODULES]
    s += ["", "## Hours by estimation area (software)", "", "| Area | Hours |", "|------|------:|"]
    s += [f"| {a} | {h} |" for a, h in areas.items()]
    s += ["", "## Comparison with Option A", "",
          "| | Option A (GMC) | Option B (GPM) |", "|---|---:|---:|",
          f"| Go-live hours | 4057 | {go + vh} |",
          "| Admin portal / self-service | Yes | No |",
          "| Indicative duration | 17–20 weeks (5–6 people) | 7–8 weeks (2 people) or about 5 weeks (3 people) |", "",
          "## Critical assumptions and risks", "",
          "1. **Content rights:** Brenlo's images, codes and product data are Brenlo's. Garrison must hold written permission (for example as an authorised Brenlo dealer) before go-live. This is a go/no-go dependency.",
          "2. **Source code (go/no-go):** Garrison owns and will hand over the complete, current source code of www.garrisonindustries.ky "
          "(templates, themes, plugins, build files and database), together with server/hosting, database and DNS access. The code must match the live site "
          "and Garrison must have the right to modify it. No admin logins are currently available, so all changes are made in code. "
          "If the source code cannot be provided or is out of date, this estimate does not apply; the alternatives are rebuilding the affected pages "
          "(re-estimate) or adopting Option A. The site resolves to a self-hosted cloud server; its SSL certificate did not validate during our review.",
          "3. The source site may block automated extraction (some category URLs already return access errors). Contingency: supplier data file from Brenlo, or manual capture at the higher rate.",
          "4. No admin portal: every later product change needs a developer.",
          "5. Thin product content (no descriptions) limits SEO value compared with Option A.", ""]
    (ROOT / f"{CODE}_Estimation_Summary.md").write_text("\n".join(s))

    fw = [f"# {CODE} — Feature-wise Estimation Summary (Internal)", "", f"**Project:** {PROJECT}  ", f"**As of:** {TODAY}", "",
          "## Grand totals", "", "| Bucket | Hours |", "|--------|------:|", f"| Software go-live | {go} |",
          f"| Per-product verification | {vh} |", f"| **Go-live total** | **{go + vh}** |", f"| Optional software | {opt} |", "",
          "## Feature-wise detail", ""]
    for m in MODULES:
        fw += [f"### {m['nn']} — {m['name']}", "",
               "| Feature ID | Feature Name | UI | API | DB | Integ. | Test | Docs | Hours | Notes |",
               "|------------|--------------|---:|---:|---:|---:|---:|---:|------:|-------|"]
        for f in feats(m):
            a = f["areas"]
            fw.append(f"| {f['id']} | {f['name']} | {a['UI']} | {a['API']} | {a['Database']} | {a['Integration']} | "
                      f"{a['Testing']} | {a['Documentation']} | {f['hours']} | {f['notes']} |")
        fw += ["", f"**Module total: {m['hours']} hours**", ""]
    fw += ["### Volume-based line", "", "| Item | Quantity | Rate (h) | Hours |", "|------|---------:|---------:|------:|",
           f"| Per-product verification (automated extraction path) | {PLANNED_PRODUCTS} | {VERIFY_RATE} | {vh} |",
           f"| Contingency: manual capture per product (if extraction blocked) | per product | {MANUAL_RATE} | — |", ""]
    (ROOT / f"{CODE}_Estimation_Summary_FeatureWise.md").write_text("\n".join(fw))


def write_client_docx():
    all_h, go, opt = totals()
    vh = volume_hours()
    doc = base_doc()
    for text, size, bold in [("Product Migration Effort Estimate", 22, True), ("Garrison Catalogue Product Migration to Existing Website", 15, True),
                             (f"Prepared for {b.CLIENT} · Option B · Effort in person-hours", 11, False), (f"Date: {TODAY} · Project code: {CODE}", 10, False)]:
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold, r.font.size, r.font.color.rgb = bold, b.Pt(size), b.NAVY

    doc.add_heading("1. Introduction", level=1)
    doc.add_paragraph("This document estimates the effort to move the moulding products shown in the Brenlo online catalogue onto the existing "
                      "Garrison website (www.garrisonindustries.ky). The products are extracted, prepared and reviewed by Garrison, then published as "
                      "catalogue pages within the current website and theme: a mouldings landing page, category listings with filters, product "
                      "pages, search and a product enquiry link.")
    doc.add_paragraph("This option has no administration portal. After go-live, product changes are made by a developer updating the prepared "
                      "dataset and reloading it. For Garrison self-service maintenance, see Option A (full catalogue platform).")

    doc.add_heading("2. Summary Totals", level=1)
    add_table(doc, ["Bucket", "Person-hours"], [
        ["Software (go-live features)", go],
        [f"Per-product verification ({PLANNED_PRODUCTS} products)", vh],
        ["**Recommended total**", f"**{go + vh}**"],
        ["Optional features", opt]], num_cols=(1,))

    doc.add_heading("3. Module-wise Summary", level=1)
    add_table(doc, ["Module", "Features", "Hours"],
              [[f"{m['nn']}. {m['name']}", len(feats(m)), m["hours"]] for m in MODULES] + [["**Software total**", f"**{len(FEATURES)}**", f"**{all_h}**"]],
              num_cols=(1, 2))

    doc.add_heading("4. Feature-wise Detail", level=1)
    for m in MODULES:
        doc.add_heading(f"{m['nn']}. {m['name']}", level=2)
        add_table(doc, ["Feature ID", "Feature Name", "Hours", "Notes"],
                  [[f["id"], f["name"], f["hours"], "Included" if f["notes"] == "Go-live" else "Optional"] for f in feats(m)]
                  + [["", "**Module total**", f"**{m['hours']}**", ""]], num_cols=(2,))

    doc.add_heading("5. Product Volume and Rates", level=1)
    doc.add_paragraph(f"The moulding catalogue was reviewed category by category. {CONFIRMED_PRODUCTS} products were confirmed in 21 categories; the "
                      f"remaining categories will be counted at project start. The estimate uses a planning quantity of {PLANNED_PRODUCTS} products.")
    add_table(doc, ["Item", "Basis"], [
        ["Per-product verification (included above)", f"{VERIFY_RATE} hours per product × {PLANNED_PRODUCTS} products"],
        ["Additional products beyond the planning quantity", f"{VERIFY_RATE} hours per product"],
        ["Manual capture, if automated extraction is not possible", f"{MANUAL_RATE} hours per product"],
        ["Optional doors and sheet goods products", f"{VERIFY_RATE} hours per product, plus the optional feature hours"]])

    doc.add_heading("6. Indicative Delivery Phasing", level=1)
    for t in ["Onboarding: source code and access, technical assessment, staging environment and backup.",
              "Data preparation: extraction, image optimisation, normalisation and Garrison review workbook.",
              "Website build: product data store, catalogue pages, navigation, theme and SEO.",
              "Go-live: reconciliation, user acceptance testing, production deployment and handover."]:
        doc.add_paragraph(t, style="List Number")
    doc.add_paragraph("Indicative duration: 7–8 weeks with two developers, or about 5 weeks with three, subject to timely access and review.")

    doc.add_heading("7. Items Not Included", level=1)
    for t in ["Administration portal, user roles and publishing workflow", "Writing new product descriptions, technical drawings or documents",
              "Website redesign, hosting migration or SSL certificate remediation", "E-commerce, pricing or quoting",
              "Obtaining permission from Brenlo to reproduce product data and images"]:
        doc.add_paragraph(t, style="List Bullet")

    doc.add_heading("8. Key Assumptions and Dependencies", level=1)
    for t in ["Garrison holds written permission from Brenlo to reproduce its product data and images on the Garrison website before go-live.",
              "Garrison owns and provides the complete, current source code of its website (including themes, plugins and database), with the right "
              "to modify it, plus server, database and hosting access. If the source code is not available, this estimate does not apply and will be revised.",
              "The existing website technology can host new page templates and product data.",
              "The source catalogue remains accessible for automated extraction; otherwise a supplier data file or the manual capture rate applies.",
              "Product pages show the information available in the source catalogue: code, category, style, dimensions, species and image.",
              "Enquiries use the existing Garrison contact form or email.",
              "Garrison completes the product review within two review rounds."]:
        doc.add_paragraph(t, style="List Number")

    doc.add_heading("9. Disclaimer", level=1)
    doc.add_paragraph("Estimates are indicative. Final effort depends on the existing website technology, the confirmed product count and "
                      "the accessibility of the source catalogue.")
    doc.save(ROOT / f"{CODE}_Estimation_Summary_FeatureWise_Client.docx")


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    b.validate()
    b.write_features()
    write_modules_and_registry()
    write_summaries()
    b.md_to_docx(ROOT / f"SoW_{CODE}_Detailed.md", ROOT / f"SoW_{CODE}_Detailed.docx")
    write_client_docx()
    all_h, go, opt = totals()
    print(f"Features {len(FEATURES)} · software go-live {go} · verification {volume_hours()} · optional {opt}")
    for m in MODULES:
        print(f"  {m['nn']} {m['name']}: {len(feats(m))} features, {m['hours']} h")


if __name__ == "__main__":
    main()
