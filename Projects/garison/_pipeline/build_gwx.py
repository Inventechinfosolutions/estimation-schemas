"""Build Garrison Option 1 (GWM) and Option 2 (GWA) estimation artefacts, plus the three-option comparison.

Run from repo root:
    .venv/bin/python Projects/garison/_pipeline/build_gwx.py
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
import gwx_data  # noqa: E402

GARRISON = HERE.parent
TODAY = dt.date.today().isoformat()
GMC = json.loads((GARRISON / "GMC_Registry.json").read_text())["totals"]

PLANNED_PRODUCTS = 350
CONFIRMED_PRODUCTS = 201
PAGES = 15

# AI fees: list prices checked October 2026 (OpenAI GPT Image 2 standard tier, 1024-1536 px, incl. image input tokens)
AI_PRICE = {"Standard quality": 0.07, "High quality": 0.23}
AI_LINES = [("Style exploration and 20-product pilot", 200),
            (f"Product images ({PLANNED_PRODUCTS} products × about 4 candidates incl. regenerations)", PLANNED_PRODUCTS * 4),
            ("Lifestyle and category scenes (about 25 scenes × 10 candidates)", 250)]
AI_CONTINGENCY = 0.25
AI_BUDGET_CAP = 600
AI_VARIANT_GENS = PLANNED_PRODUCTS * 3 * 2

COMMON_MODULES = [
    dict(nn="01", name="Discovery & Website Design", type="Business",
         summary="Discovery of the current site from its public pages, information architecture, wireframes and visual design",
         source="Explicit (client request: website design)",
         in_scope="Content capture, sitemap, wireframes, style guide, component library, page designs, prototype",
         out_scope="New logo or brand identity; copywriting; photography",
         actors="Delivery business analyst and designer; Garrison business owner", deps="Garrison business owner availability",
         notes="Source code and admin logins are not needed; the site is rebuilt",
         purpose="Understand what the current website contains and design the new website before it is built.",
         reqs=["Capture all useful content and URLs from the current public website.", "Agree a sitemap and page wireframes.",
               "Produce an approved visual design for every page template on desktop and mobile."],
         accept=["Garrison approves the page list, wireframes and visual designs in writing."]),
    dict(nn="02", name="Website Build", type="Business",
         summary="Static website foundation, home page, company pages, contact form and existing content migration",
         source="Explicit (client request: website design)",
         in_scope="Layout, navigation, components, home, about, services, gallery, content pages, enquiry form, migrated content",
         out_scope="Admin portal or content management system; e-commerce; customer accounts",
         actors="Visitor; Delivery developer", deps="Module 01",
         notes="No admin portal: content held in version-controlled files and changed by a developer",
         purpose="Build the new Garrison website from the approved designs.",
         reqs=["Responsive site with header, navigation, footer and reusable components.", "Home page, company and service pages populated with migrated content.",
               "Enquiry form delivering to Garrison's existing mailbox with spam protection."],
         accept=["All confirmed pages are live on staging, match the approved designs and pass testing."]),
    dict(nn="03", name="Product Catalogue Pages", type="Business",
         summary="Mouldings landing page, category listings with filters, product detail, search and product enquiry",
         source="Explicit (client request); F03-006 Optional",
         in_scope="Public catalogue pages generated from the one-time dataset", out_scope="Quotes, pricing, cart, customer accounts",
         actors="Visitor", deps="Modules 02 and 04", notes="Fixed fields and filters",
         purpose="Present the migrated products so visitors can browse, filter, search and enquire.",
         reqs=["Landing page with category tiles and style shortcuts.", "Category listing with style, thickness, width and species filters.",
               "Product page with image, code, dimensions, species, similar products and Request Information.", "Search by code, category, style and size."],
         accept=["A visitor can go from the home page to a product and send an enquiry that names the product."]),
    dict(nn="04", name="One-time Product Data Migration", type="Technical",
         summary="Extraction, image handling, normalisation, Garrison review workbook and catalogue data build",
         source="Explicit (client request); F04-006 Optional",
         in_scope="Brenlo moulding products; one-time set-up of categories, styles and products; refresh procedure",
         out_scope="Admin portal; new product descriptions or drawings; doors and sheet goods unless F04-006 is taken",
         actors="Delivery developer; Garrison catalogue owner (review)", deps="Brenlo permission (go/no-go)",
         notes="Replaces admin activities: catalogue, categories and products are set up once from the reviewed dataset",
         purpose="Set up the catalogue once from the source, with Garrison approving the product list, instead of building an admin portal.",
         reqs=["Extract moulding products from the source catalogue (or a supplier data file).", "Normalise dimensions, categories, styles and species.",
               "Garrison reviews and signs off the product list in a workbook.", "Generate the website's catalogue data from the signed-off dataset."],
         accept=["Every approved product is published; the reconciliation report shows no unexplained gaps."]),
    dict(nn="05", name="Hosting, SEO & Launch", type="Shared",
         summary="SEO and redirects, hosting, SSL and DNS cutover, analytics, quality assurance, testing and launch",
         source="Derived", in_scope="Hosting set-up, DNS cutover preserving email, SEO, analytics, testing, launch, handover",
         out_scope="Hosting fees; ongoing support after warranty; paid advertising",
         actors="Delivery developer and QA; Garrison domain contact", deps="Domain/DNS access",
         notes="Google Workspace email records preserved",
         purpose="Launch the new website on Garrison's domain securely, discoverably and without email disruption.",
         reqs=["SEO-ready URLs, metadata, sitemap and 301 redirects from current URLs.", "Hosting, SSL and DNS cutover with email preserved.",
               "Analytics with consent; full testing; user acceptance testing and handover."],
         accept=["Site live on garrisonindustries.ky with valid SSL, working email and no broken redirects."]),
]

AI_MODULE = dict(
    nn="06", name="AI Product Imagery", type="Technical",
    summary="Original AI-assisted product images built from profile silhouettes, plus lifestyle scenes, review and provenance records",
    source="Explicit (client request: AI image generation); F06-007 Optional",
    in_scope="Style guide and pilot, silhouettes, base renders, AI generation, review, scenes, disclosure and provenance",
    out_scope="Photography; legal opinion; AI service fees (shown separately as pass-through cost)",
    actors="Delivery imagery specialist and developer; Garrison business owner", deps="Module 04; Garrison legal review",
    notes="Brenlo photographs are not published and not sent to the AI service",
    purpose="Replace copied product photographs with original, accurate AI-assisted images.",
    reqs=["Agree an image style and approve a 20-product pilot.", "Create a dimension-accurate silhouette per product.",
          "Render each profile and add realistic finish with an AI service; review and approve one image per product.",
          "Create lifestyle and category scenes; disclose AI-assisted images and keep a provenance register."],
    accept=["Every published product has an approved, accurate image recorded in the provenance register."])

OPTIONS = {
    "GWM": dict(
        code="GWM", folder="Option-1-Website-Design-Migration", label="Option 1",
        project="Garrison Website Design & Product Catalogue Migration (Option 1)",
        short="Website design and product migration",
        features=gwx_data.option1, modules=COMMON_MODULES,
        volume=[("Per-product data verification", PLANNED_PRODUCTS, 0.25), ("Existing page content migration", PAGES, 1.5)],
        ai=False),
    "GWA": dict(
        code="GWA", folder="Option-2-Website-AI-Imagery", label="Option 2",
        project="Garrison Website Design, Product Catalogue Migration & AI Product Imagery (Option 2)",
        short="Website design, product migration and AI product images",
        features=gwx_data.option2, modules=COMMON_MODULES + [AI_MODULE],
        volume=[("Per-product data verification", PLANNED_PRODUCTS, 0.25), ("Existing page content migration", PAGES, 1.5),
                ("Profile silhouette preparation (operator time)", PLANNED_PRODUCTS, 0.3), ("AI image review and selection", PLANNED_PRODUCTS, 0.2)],
        ai=True),
}

RESULTS = {}


# ---------------------------------------------------------------- helpers
def vol_hours(cfg):
    return [(n, q, r, math.ceil(q * r)) for n, q, r in cfg["volume"]]


def vol_total(cfg):
    return sum(h for *_, h in vol_hours(cfg))


def ai_cost():
    gens = sum(n for _, n in AI_LINES)
    out = {k: round(gens * p, 2) for k, p in AI_PRICE.items()}
    with_cont = {k: math.ceil(v * (1 + AI_CONTINGENCY)) for k, v in out.items()}
    return gens, out, with_cont


def short(desc, limit=150):
    s = desc.split(". ")[0].rstrip(".")
    if len(s) <= limit:
        return s
    return s[:limit].rsplit(" ", 1)[0] + " …"


def weeks(hours, people):
    return hours / (people * 40)


def setup(cfg):
    feats = cfg["features"]()
    mods = [dict(m) for m in cfg["modules"]]
    root = GARRISON / cfg["folder"]
    b.ROOT, b.CODE, b.PROJECT, b.FEATURES, b.MODULES = root, cfg["code"], cfg["project"], feats, mods
    for m in mods:
        m["slug"] = b.slugify(m["name"])
        m["folder"] = f"modules/{m['nn']}-{m['slug']}"
    for f in feats:
        f.setdefault("notes", "Go-live")
        f["slug"] = b.slugify(f["name"])
        f["nn"], f["seq"] = f["id"][1:3], f["id"][4:]
        f["hours"] = sum(r[3] for r in b.rows(f))
        f["areas"] = b.area_totals(f)
    for m in mods:
        ms = b.feats(m)
        m["hours"] = sum(f["hours"] for f in ms)
    return root, feats, mods


# ---------------------------------------------------------------- SOW
def rights_section(cfg):
    lines = ["- **Brenlo content (go/no-go):** Brenlo's product data, product codes and photographs are Brenlo's content. Garrison should hold written "
             "permission from Brenlo (for example as an authorised dealer or distributor) before publishing them. If Garrison is not a Brenlo dealer, "
             "it should not present Brenlo product codes as its own range."]
    if cfg["ai"]:
        lines += [
            "- **AI images reduce but do not remove the legal risk.** Brenlo photographs are not published and are not sent to the AI service. "
            "However, the silhouettes are traced from Brenlo references unless Garrison supplies its own drawings or samples, so the profiles shown "
            "are still Brenlo's product designs. Product data and codes still need permission.",
            "- **Accuracy and misrepresentation:** AI-assisted images may differ in detail from the physical product. Images are labelled "
            "'illustrative' and checked against dimension-accurate silhouettes before publication.",
            "- **Ownership of AI output:** in many jurisdictions purely AI-generated images may not be protected by copyright, so Garrison may not be "
            "able to stop others from copying them.",
            "- **AI service terms and indemnity:** only services licensed for commercial use are used. Some providers (for example Adobe Firefly "
            "under qualifying enterprise plans) offer output indemnity, but this typically excludes outputs based on image inputs that themselves "
            "infringe. Our design only sends our own base renders and text prompts.",
            "- **Legal review:** Garrison's legal counsel (Cayman Islands) should review the approach before go-live. This document is not legal advice."]
    lines += ["- Extraction reads public pages only, with throttled requests and no circumvention of access controls.",
              "- Enquiry form: spam protection, input validation, no enquiry data stored on the website.",
              "- HTTPS with automatic certificate renewal; no admin login surface."]
    return lines


def write_sow(cfg, root, feats, mods):
    code, ai = cfg["code"], cfg["ai"]
    go = sum(f["hours"] for f in feats if f["notes"] == "Go-live")
    s = [f"# SoW {code} — Detailed Statement of Work", "", f"## {cfg['project']}", "",
         f"**Client:** {b.CLIENT}  ", f"**Project code:** {code}  ", "**Document type:** Detailed Statement of Work (estimation ready)  ",
         "**Version:** 1.0  ",
         "**Relationship to other proposals:** One of three options. Option 1 — website design and product migration (GWM). "
         "Option 2 — Option 1 plus AI product images (GWA). Option 3 — Premium online catalogue platform with admin portal (GMC).", "", "---", "",
         "## 1. Introduction", "",
         "Garrison Industries wants a redesigned website at www.garrisonindustries.ky that includes the moulding products shown in the Brenlo online "
         "catalogue (https://brenlo.com/catalogue/). Garrison has advised that its products rarely change, so catalogue set-up (categories, styles, "
         "products and reference data) is a **one-time activity** and **no administration portal is required**.", "",
         "Because the current website's source code and admin logins are not available, the website is **rebuilt** from its public content in a new "
         "design. Products are extracted from the source catalogue, reviewed and approved by Garrison in a workbook, and published as catalogue pages. "
         "Later changes are made by a developer."]
    if ai:
        s += ["", "In this option, product images are **not copied** from the source catalogue. Each product gets an original, AI-assisted image "
              "generated from a dimension-accurate profile silhouette, and the website receives AI-generated lifestyle imagery."]
    s += ["", "## 2. Project Overview", "", "| Item | Description |", "|------|-------------|",
          "| Source | Brenlo public online catalogue: Moulding section (by category and style) |",
          "| Target | New Garrison website on garrisonindustries.ky (rebuilt; current source code not required) |",
          "| Business problem | Current website does not show individual moulding profiles and needs a modern design |",
          "| Outcome | Redesigned website with a browsable, searchable moulding catalogue and enquiry form |",
          "| Maintenance model | Developer-maintained content files and product dataset (no admin portal) |",
          f"| Product images | {'Original AI-assisted images generated from profile silhouettes' if ai else 'Source catalogue images, optimised (permission required)'} |",
          "", "### 2.1 Source catalogue observations", "", "| Observation | Implication |", "|-------------|-------------|",
          "| 37 moulding types, styles Classic / Modern / Transitional / Inspire, and Combinations | Taxonomy mirrored or renamed by Garrison |",
          f"| {CONFIRMED_PRODUCTS} products confirmed in 21 categories; 16 multi-word categories could not be counted remotely | Planning quantity **{PLANNED_PRODUCTS} products** |",
          "| Each product: category, code, thickness × width (fractions), style, species options, one isometric image (about 541×402 px) | Compact data; low per-product effort |",
          "| No drawings, PDFs or descriptions | Product pages show facts and image only unless Garrison supplies text |",
          "", "### 2.2 Current website observations", "", "| Observation | Implication |", "|-------------|-------------|",
          "| Self-hosted on a cloud virtual server; SSL certificate did not validate during review | New hosting with valid SSL |",
          "| Automated requests were refused by the server | Content captured page by page in a browser where needed |",
          "| Company email on Google Workspace | DNS cutover must keep MX and email authentication records |",
          "| No source code or admin logins available | Website rebuilt from public content; only domain/DNS access needed |",
          "", "## 3. Project Objectives", "",
          "1. Deliver a modern, responsive Garrison website in an approved new design.",
          "2. Migrate the useful content of the current website, with redirects from current URLs.",
          "3. Publish the agreed moulding products with category, style, dimensions, species and image.",
          "4. Let visitors browse, filter, search and send product enquiries to Garrison's mailbox.",
          "5. Set up the catalogue once, without an admin portal, with a documented refresh procedure."]
    if ai:
        s.append("6. Provide original, accurate AI-assisted product and lifestyle images with disclosure and a provenance record.")
    s += ["", "## 4. In Scope / Out of Scope", "", "### In Scope", ""]
    s += [f"- {m['name']}: {m['in_scope']}" for m in mods]
    s += ["", "### Out of Scope", "",
          "- Administration portal, user roles, publishing workflow and configurable product framework (available in Option 3)",
          "- New logo or brand identity, copywriting, photography",
          "- New product descriptions, technical drawings or PDFs",
          "- E-commerce, pricing, quotes, customer accounts",
          "- Hosting, domain and third-party service fees" + (" (AI service fees are shown separately)" if ai else ""),
          "- Obtaining permission from Brenlo and legal advice (Garrison responsibility)",
          "- Combinations pages and Interior Doors / In-Stock products unless the optional features are taken"]
    s += ["", "## 5. Solution Expectations (Business-level Only)", "",
          "- Fast, secure, statically generated website with no admin login surface.",
          "- Content and product data held in version-controlled files; one prepared dataset drives all catalogue pages.",
          "- Garrison approves the product list once through a review workbook instead of an admin portal.",
          "- Later changes: developer edits the dataset or content, rebuilds on staging, verifies and releases."]
    if ai:
        s.append("- Product image geometry comes from dimension-accurate silhouettes; the AI service adds finish, lighting and realism only.")
    s += ["", "## 6. Consolidated Functional Modules", ""]
    for m in mods:
        mf = [f for f in feats if f["nn"] == m["nn"]]
        s += [f"### {m['nn']}. {m['name']}", "", f"**Purpose:** {m['purpose']}", "", "**Functional requirements:**"]
        s += [f"- {r}" for r in m["reqs"]]
        s += ["", "**Acceptance criteria:**"] + [f"- {a}" for a in m["accept"]]
        s += ["", "#### Key capabilities (feature outline)", "", "| Feature ID | Capability | Description |", "|------------|------------|-------------|"]
        s += [f"| {f['id']} | {f['name']} | {short(f['desc'])}{' (Optional)' if f['notes'] == 'Optional' else ''} |" for f in mf]
        s += ["", "---", ""]
    flow = ("Discovery and content capture → wireframes and design approval → website build → product extraction → normalisation → "
            + ("reference capture → silhouettes → pilot approval → base renders and AI images → image review → " if ai else "image optimisation → ")
            + "Garrison review workbook sign-off → catalogue data build → testing → user acceptance testing → DNS cutover → handover.")
    s += ["## 7. End-to-End Workflow", "", flow, "",
          "Product refresh after go-live: developer updates the dataset" + (" and generates images for new products" if ai else "")
          + " → build on staging → verification → production release.", "",
          "## 8. Access Control", "", "No administration portal or user roles. All website pages are public. Content, dataset"
          + (", imagery tools" if ai else "") + " and deployment are used only by the delivery team and later maintenance developers.", "",
          "## 9. Channels", "", "Responsive website (desktop, tablet, mobile). No mobile app.", "",
          "## 10. Integrations", "", "| Integration | Purpose | Notes |", "|-------------|---------|-------|",
          "| Brenlo public catalogue | One-time source of product data" + (" and internal reference images" if ai else " and images")
          + " | Throttled extraction, or a supplier data file |",
          "| Transactional email service | Enquiry and acknowledgement emails | Authenticated alongside Google Workspace |",
          "| Spam protection service | Enquiry form protection | For example Turnstile or reCAPTCHA |",
          "| Web analytics | Visitor and enquiry insights | Loaded after cookie consent |",
          "| Hosting and DNS | Website hosting, SSL, domain | Email records preserved |"]
    if ai:
        s += ["| AI image generation service | Finish and lighting on base renders; lifestyle scenes | Commercial licence; spending cap |",
              "| 3D rendering tool | Dimension-accurate base renders from silhouettes | Scripted batch rendering |"]
    s += ["", "## 11. Compliance, Security & Content Rights", ""] + rights_section(cfg)
    s += ["", "## 12. Non-Functional Requirements", "", "| Area | Requirement |", "|------|-------------|",
          "| Performance | Key templates meet Core Web Vitals 'good'; images optimised and lazy-loaded |",
          "| Compatibility | Current Chrome, Edge, Safari, Firefox; iOS and Android phones |",
          "| Accessibility | WCAG 2.1 AA basics (contrast, alt text, keyboard navigation, headings) |",
          "| SEO | Unique titles, sitemap, structured data, 301 redirects from current URLs |",
          "| Maintainability | Documented content update and product refresh procedures |", "",
          "## 13. Data Migration & Volume Basis", "", "| Item | Quantity | Rate (hours) | Hours |", "|------|---------:|-------------:|------:|"]
    s += [f"| {n} | {q} | {r} | {h} |" for n, q, r, h in vol_hours(cfg)]
    s += ["", f"Products beyond {PLANNED_PRODUCTS} and pages beyond {PAGES} are charged at the same rates.", ""]
    sec = 14
    if ai:
        gens, raw, cont = ai_cost()
        s += [f"## {sec}. AI Service Cost (pass-through, separate from effort)", "", "| Item | Generations |", "|------|------------:|"]
        s += [f"| {n} | {g} |" for n, g in AI_LINES] + [f"| **Total** | **{gens}** |", ""]
        s += ["| Price basis (per generation, incl. image input) | Fees | With 25% contingency |", "|------|-----:|-----:|"]
        s += [f"| {k} (about USD {p:.2f}) | USD {raw[k]:,.0f} | USD {cont[k]:,.0f} |" for k, p in AI_PRICE.items()]
        s += ["", f"Recommended AI service budget cap: **USD {AI_BUDGET_CAP}**. Optional finish variants (F06-007, up to 3 per product): about "
              f"{AI_VARIANT_GENS} generations, USD {AI_VARIANT_GENS * AI_PRICE['Standard quality']:,.0f}–{AI_VARIANT_GENS * AI_PRICE['High quality']:,.0f}. "
              "An indemnified enterprise service (for example Adobe Firefly) is priced by provider quote.", ""]
        sec += 1
    phases = ["Discovery and design: content capture, wireframes, visual design approval.",
              "Build: website foundation, pages, content migration and catalogue templates.",
              "Product migration: extraction, normalisation" + (", silhouettes, AI pilot and image generation" if ai else ", images")
              + ", Garrison review and sign-off.",
              "Launch: testing, user acceptance testing, DNS cutover, handover."]
    s += [f"## {sec}. Phased Delivery", ""] + [f"{i}. {p}" for i, p in enumerate(phases, 1)]
    s += ["", "Optional: Combinations pages (F03-006); Interior Doors and In-Stock products (F04-006)" + ("; finish variant images (F06-007)." if ai else "."), ""]
    sec += 1
    deliv = ["Redesigned website live on garrisonindustries.ky", "Approved design files and style guide", "Master product dataset (CSV/JSON)",
             "Extraction, normalisation and catalogue build scripts with refresh procedure", "Reconciliation report, test report and handover document",
             "Hosting and DNS runbook"]
    if ai:
        deliv += ["Approved AI-assisted product and scene images with provenance register", "Image style guide, prompt templates and silhouettes"]
    s += [f"## {sec}. Deliverables", ""] + [f"- {d}" for d in deliv] + [""]
    sec += 1
    s += [f"## {sec}. Acceptance Criteria (Program Level)", "", "| Perspective | Criterion |", "|-------------|-----------|",
          "| Visitor | Can browse, filter, search, view a product and send a product enquiry on any device |",
          "| Garrison | Approved designs implemented; approved product set live with correct data" + (" and approved images" if ai else "") + " |",
          "| Data | Reconciliation shows the agreed product count published with zero unexplained gaps |",
          "| Technical | Valid SSL, working email after cutover, no broken redirects |", ""]
    sec += 1
    assume = ["Garrison holds written permission from Brenlo to use its product data" + ("" if ai else " and images") + " before go-live (go/no-go).",
              "Current website source code and admin logins are not needed; Garrison provides domain/DNS (registrar) access.",
              f"Planning quantity: {PLANNED_PRODUCTS} moulding products and about {PAGES} existing pages; actuals confirmed early.",
              "Products change rarely; later changes are made by a developer (no admin portal).",
              "Garrison supplies brand assets and approves content; no new copywriting or photography.",
              "Two review rounds each for wireframes, designs, the product workbook and user acceptance testing.",
              "Hosting and third-party fees are paid by Garrison."]
    if ai:
        assume += ["AI service fees are pass-through and capped at the agreed budget.",
                   "Garrison's legal counsel reviews the AI imagery approach before go-live.",
                   "Where Garrison has its own drawings or samples, these replace source references for silhouettes."]
    s += [f"## {sec}. Assumptions & Dependencies", ""] + [f"{i}. {a}" for i, a in enumerate(assume, 1)] + [""]
    sec += 1
    s += [f"## {sec}. Appendices", "", "### Appendix A — Module & Feature Index", "",
          "| Module | Module Name | Type | Feature IDs (count) |", "|--------|-------------|------|---------------------|"]
    for m in mods:
        mf = [f for f in feats if f["nn"] == m["nn"]]
        s.append(f"| {m['nn']} | {m['name']} | {m['type']} | {mf[0]['id']} … {mf[-1]['id']} ({len(mf)}) |")
    s += ["", "### Appendix B — Comparison of the Three Options", "",
          "| Aspect | Option 1 — Design + Migration | Option 2 — Option 1 + AI Images | Option 3 — Premium Platform |", "|---|---|---|---|",
          "| New website design | Yes | Yes | Catalogue application integrated with website |",
          "| Product data from source catalogue | Yes, one time | Yes, one time | Yes, via governed import |",
          "| Product images | Source images (permission needed) | Original AI-assisted images | Source or Garrison images, with rights tracking |",
          "| Admin portal and roles | No | No | Yes |",
          "| Self-service product changes | No (developer) | No (developer) | Yes |",
          "| Publishing workflow and rights gate | No | No | Yes |", "",
          "### Appendix C — Risks", "", "| Risk | Mitigation |", "|------|-----------|",
          "| Brenlo does not permit use of its data" + ("" if ai else " or images") + " | Confirm before build; use Garrison's own data |",
          "| Source site blocks extraction | Supplier data file or manual capture at a higher per-product rate |",
          "| Registrar/DNS access unavailable | Garrison recovers access before cutover |",
          "| Product count higher than planned | Per-product rate for extra products |"]
    if ai:
        s += ["| AI images distort profile shapes | Geometry from silhouettes and base renders; review against silhouettes |",
              "| AI costs exceed estimate | Spending cap on the AI account; cost tracked per batch |",
              "| Legal challenge over AI derivatives | Legal review, disclosure, provenance register, Garrison drawings where available |"]
    (root / f"SoW_{code}_Detailed.md").write_text("\n".join(s) + "\n")


# ---------------------------------------------------------------- modules, registry, summaries
def write_modules_and_registry(cfg, root, feats, mods):
    code = cfg["code"]
    out = [f"# {cfg['project']} — Module List", "", f"Source: `SoW_{code}_Detailed.md`", "",
           "| # | Module | Type | Summary | Source |", "|---|--------|------|---------|--------|"]
    out += [f"| {m['nn']} | {m['name']} | {m['type']} | {m['summary']} | {m['source'].split(' ')[0]} |" for m in mods]
    out += ["", "---", "", "## Module Details", ""]
    for m in mods:
        out += [f"### {m['nn']}. {m['name']}", "", f"- **Type:** {m['type']}", f"- **Summary:** {m['summary']}.", f"- **Source:** {m['source']}",
                f"- **In Scope:** {m['in_scope']}", f"- **Out of Scope:** {m['out_scope']}", f"- **Key Actors:** {m['actors']}",
                f"- **Dependencies:** {m['deps']}", f"- **Notes:** {m['notes']}",
                "- **Features:** " + ", ".join(f"{f['id']} {f['name']}" for f in b.feats(m)), ""]
    (root / f"{code}_Modules.md").write_text("\n".join(out))

    all_h, go, opt = b.totals()
    vt = vol_total(cfg)
    reg = dict(project_code=code, project_name=cfg["project"], client=b.CLIENT, output_root=f"Projects/garison/{cfg['folder']}",
               related_estimates=["GWM (Option 1)", "GWA (Option 2)", "GMC (Option 3 — Premium)"], sow=f"SoW_{code}_Detailed.md",
               updated_at=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
               volume=[dict(item=n, quantity=q, rate_hours=r, hours=h) for n, q, r, h in vol_hours(cfg)],
               totals=dict(software_go_live_hours=go, software_optional_hours=opt, software_all_hours=all_h, volume_hours=vt,
                           go_live_total_hours=go + vt, feature_count=len(feats), module_count=len(mods)),
               modules=[dict(nn=m["nn"], name=m["name"], slug=m["slug"], type=m["type"], folder=m["folder"], feature_count=len(b.feats(m)),
                             total_hours=m["hours"],
                             features=[dict(id=f["id"], seq=f["seq"], name=f["name"], slug=f["slug"], file=f["file"], hours=f["hours"],
                                            notes=f["notes"], areas=f["areas"]) for f in b.feats(m)]) for m in mods])
    if cfg["ai"]:
        gens, raw, cont = ai_cost()
        reg["ai_service_cost_usd"] = dict(generations=gens, price_per_generation=AI_PRICE, fees=raw, with_contingency=cont,
                                          budget_cap=AI_BUDGET_CAP, optional_variant_generations=AI_VARIANT_GENS)
    (root / f"{code}_Registry.json").write_text(json.dumps(reg, indent=2, ensure_ascii=False) + "\n")


def comparison_rows():
    o1, o2 = RESULTS["GWM"], RESULTS["GWA"]
    return [
        ["Software effort (go-live features)", o1["go"], o2["go"], GMC["go_live_hours"]],
        ["Volume-based effort (products, pages, images)", o1["vol"], o2["vol"], "Population by Garrison via admin portal"],
        ["**Total go-live effort (hours)**", f"**{o1['go'] + o1['vol']}**", f"**{o2['go'] + o2['vol']}**", f"**{GMC['go_live_hours']}**"],
        ["Optional features (hours)", o1["opt"], o2["opt"], GMC["optional_hours"]],
        ["AI service fees (pass-through)", "—", f"USD {o2['ai'][0]:,}–{o2['ai'][1]:,} (cap USD {AI_BUDGET_CAP})", "—"],
        ["New website design included", "Yes", "Yes", "No (design phase excluded from estimate)"],
        ["Admin portal and roles", "No", "No", "Yes"],
        ["Product images", "Source images (permission needed)", "Original AI-assisted images", "Source or Garrison images, rights tracked"],
        ["Later product changes", "Developer", "Developer", "Garrison self-service"],
        ["Indicative duration", o1["duration"], o2["duration"], "17–20 weeks (5–6 people)"],
    ]


def duration_text(total):
    w3, w4 = weeks(total, 3), weeks(total, 4)
    return f"About {math.ceil(w3)} weeks with 3 people, or {math.ceil(w4)} weeks with 4"


def write_summaries(cfg, root, feats, mods):
    code = cfg["code"]
    all_h, go, opt = b.totals()
    vh, vt = vol_hours(cfg), vol_total(cfg)
    areas = b.area_sum(feats)
    s = [f"# {code} — Estimation Summary (Internal)", "", f"**Project:** {cfg['project']}  ", f"**Client:** {b.CLIENT}  ", f"**Project code:** {code}  ",
         f"**As of:** {TODAY}  ", f"**Source:** `SoW_{code}_Detailed.md` · feature indexes under `modules/*/features/_index.md`", "",
         "## Totals", "", "| Metric | Hours |", "|--------|------:|", f"| Software — go-live features | {go} |"]
    s += [f"| {n} ({q} × {r} h) | {h} |" for n, q, r, h in vh]
    s += [f"| **Recommended go-live total** | **{go + vt}** |", f"| Optional features | {opt} |", f"| All-in | {all_h + vt} |", ""]
    if cfg["ai"]:
        gens, raw, cont = ai_cost()
        s += ["## AI service cost (separate from hours)", "", "| Item | Generations |", "|------|------------:|"]
        s += [f"| {n} | {g} |" for n, g in AI_LINES] + [f"| **Total** | **{gens}** |", "", "| Price basis | Fees (USD) | +25% contingency (USD) |", "|---|---:|---:|"]
        s += [f"| {k} @ {p:.2f} | {raw[k]:,.0f} | {cont[k]:,} |" for k, p in AI_PRICE.items()]
        s += ["", f"Budget cap recommended: USD {AI_BUDGET_CAP}. Prices: OpenAI GPT Image 2 list prices checked October 2026 "
              "(about USD 0.053 medium / 0.211 high per 1024×1024 output, plus image input tokens; Batch API halves output cost).", ""]
    s += ["## Per-module hours", "", "| # | Module | Type | Features | Hours |", "|---|--------|------|---------:|------:|"]
    s += [f"| {m['nn']} | {m['name']} | {m['type']} | {len(b.feats(m))} | {m['hours']} |" for m in mods]
    s += ["", "## Hours by estimation area (software)", "", "| Area | Hours | Share |", "|------|------:|------:|"]
    s += [f"| {a} | {h} | {b.pct(h, all_h)} |" for a, h in areas.items()]
    s += ["", "Design artefacts (wireframes, visual designs, scenes) are sized on the UI scale.", "",
          "## Timeline check", "", f"Go-live total {go + vt} h ≈ {weeks(go + vt, 3):.1f} weeks with 3 people or {weeks(go + vt, 4):.1f} weeks with 4 "
          "(40 h/person-week), before project management.", "",
          "## Three-option comparison", "", "| | Option 1 (GWM) | Option 2 (GWA) | Option 3 Premium (GMC) |", "|---|---:|---:|---:|"]
    s += [f"| {' | '.join(str(c) for c in r)} |" for r in comparison_rows()] if "GWA" in RESULTS and "GWM" in RESULTS else ["| (generated after both options are built) | | | |"]
    risks = [t[2:] for t in rights_section(cfg)[:6 if cfg["ai"] else 1]] + [
        "Website rebuilt from public pages; current source code not needed. Domain/registrar access is required.",
        "Google Workspace MX/SPF/DKIM/DMARC records must be preserved at cutover.",
        f"Planning quantities: {PLANNED_PRODUCTS} products, {PAGES} pages; variance at the volume rates.",
        "Option 3 (GMC) excludes UX/UI design and project management; Options 1 and 2 include design but not project management."]
    s += ["", "## Critical assumptions and risks", ""] + [f"{i}. {t}" for i, t in enumerate(risks, 1)] + [""]
    (root / f"{code}_Estimation_Summary.md").write_text("\n".join(s))

    fw = [f"# {code} — Feature-wise Estimation Summary (Internal)", "", f"**Project:** {cfg['project']}  ", f"**As of:** {TODAY}", "",
          "## Grand totals", "", "| Bucket | Hours |", "|--------|------:|", f"| Software go-live | {go} |", f"| Volume-based lines | {vt} |",
          f"| **Go-live total** | **{go + vt}** |", f"| Optional software | {opt} |", "", "## Feature-wise detail", ""]
    for m in mods:
        fw += [f"### {m['nn']} — {m['name']}", "", "| Feature ID | Feature Name | UI | API | DB | Integ. | Test | Docs | Hours | Notes |",
               "|------------|--------------|---:|---:|---:|---:|---:|---:|------:|-------|"]
        for f in b.feats(m):
            a = f["areas"]
            fw.append(f"| {f['id']} | {f['name']} | {a['UI']} | {a['API']} | {a['Database']} | {a['Integration']} | {a['Testing']} | "
                      f"{a['Documentation']} | {f['hours']} | {f['notes']} |")
        fw += ["", f"**Module total: {m['hours']} hours**", ""]
    fw += ["### Volume-based lines", "", "| Item | Quantity | Rate (h) | Hours |", "|------|---------:|---------:|------:|"]
    fw += [f"| {n} | {q} | {r} | {h} |" for n, q, r, h in vh] + [""]
    (root / f"{code}_Estimation_Summary_FeatureWise.md").write_text("\n".join(fw))


# ---------------------------------------------------------------- client docx
def heading_block(doc, title, subtitle, code):
    for text, size, bold in [(title, 22, True), (subtitle, 15, True), (f"Prepared for {b.CLIENT} · Effort in person-hours", 11, False),
                             (f"Date: {TODAY}" + (f" · Project code: {code}" if code else ""), 10, False)]:
        p = doc.add_paragraph()
        r = p.add_run(text)
        r.bold, r.font.size, r.font.color.rgb = bold, b.Pt(size), b.NAVY


def client_rights(cfg):
    out = ["Brenlo's product data, codes and photographs belong to Brenlo. Garrison should hold written permission from Brenlo (for example as an "
           "authorised dealer) before they are published. This is a go/no-go condition."]
    if cfg["ai"]:
        out += ["AI-assisted images reduce, but do not remove, the legal risk. Brenlo photographs are not published or given to the AI service, but the "
                "profile shapes are still Brenlo's designs unless Garrison provides its own drawings or samples, and the product data still needs permission.",
                "Images are labelled as illustrative and checked against dimension-accurate outlines, so visitors are not misled about the product.",
                "Purely AI-generated images may not be protected by copyright in some jurisdictions, so Garrison may not be able to stop others reusing them.",
                "Only AI services licensed for commercial use will be used. Some providers offer output indemnity under enterprise plans, usually excluding "
                "outputs based on image inputs that themselves infringe; our approach sends only our own renders and text prompts.",
                "We recommend Garrison's legal counsel reviews this approach before go-live. This document is not legal advice."]
    return out


def write_client_docx(cfg, root, feats, mods):
    code, ai = cfg["code"], cfg["ai"]
    all_h, go, opt = b.totals()
    vh, vt = vol_hours(cfg), vol_total(cfg)
    doc = b.base_doc()
    heading_block(doc, "Effort Estimate", cfg["project"], code)
    n = 0

    def h1(t):
        nonlocal n
        n += 1
        doc.add_heading(f"{n}. {t}", level=1)

    h1("Introduction")
    doc.add_paragraph("This document estimates the effort to redesign the Garrison website (www.garrisonindustries.ky) and publish the moulding products "
                      "from the Brenlo online catalogue on it" + (", with original AI-assisted product images." if ai else "."))
    doc.add_paragraph("Garrison has advised that products change rarely, so catalogue set-up (categories, styles, products and reference data) is done once "
                      "and no administration portal is included. Garrison approves the product list through a review workbook; later changes are made by a "
                      "developer. Because the current website's source code and admin logins are not available, the website is rebuilt from its public "
                      "content in a new design; only domain access is needed.")
    if ai:
        doc.add_paragraph("Product images are not copied from the source catalogue. Each product's outline is drawn to its published dimensions, rendered "
                          "in 3D, and finished with an AI image service for a realistic look. Lifestyle images for the home page and category banners are "
                          "also generated.")

    h1("Summary Totals")
    rows = [["Software and design (included features)", go]] + [[f"{n_} ({q} × {r} h)", h] for n_, q, r, h in vh]
    rows += [["**Recommended total**", f"**{go + vt}**"], ["Optional features", opt]]
    add = b.add_table
    add(doc, ["Bucket", "Person-hours"], rows, num_cols=(1,))
    if ai:
        gens, raw, cont = ai_cost()
        h1("AI Service Cost (separate from effort)")
        doc.add_paragraph("AI image service fees are a pass-through cost paid at provider rates, shown separately from effort. Estimates use current list "
                          "prices for a leading commercial image model and include image inputs.")
        add(doc, ["Item", "Generations"], [[n_, g] for n_, g in AI_LINES] + [["**Total**", f"**{gens}**"]], num_cols=(1,))
        add(doc, ["Price basis", "Fees (USD)", "With 25% contingency (USD)"],
            [[f"{k} (about USD {p:.2f} per image)", f"{raw[k]:,.0f}", f"{cont[k]:,}"] for k, p in AI_PRICE.items()], num_cols=(1, 2))
        doc.add_paragraph(f"Recommended budget cap: USD {AI_BUDGET_CAP}, enforced as a spending limit on the AI account. Optional finish variants "
                          f"(up to three per product) add about USD {AI_VARIANT_GENS * AI_PRICE['Standard quality']:,.0f}–"
                          f"{AI_VARIANT_GENS * AI_PRICE['High quality']:,.0f}. Enterprise services with output indemnity are priced by provider quote.")

    h1("Module-wise Summary")
    add(doc, ["Module", "Features", "Hours"], [[f"{m['nn']}. {m['name']}", len(b.feats(m)), m["hours"]] for m in mods]
        + [["**Software total**", f"**{len(feats)}**", f"**{all_h}**"]], num_cols=(1, 2))

    h1("Feature-wise Detail")
    for m in mods:
        doc.add_heading(f"{m['nn']}. {m['name']}", level=2)
        add(doc, ["Feature ID", "Feature Name", "Hours", "Notes"],
            [[f["id"], f["name"], f["hours"], "Included" if f["notes"] == "Go-live" else "Optional"] for f in b.feats(m)]
            + [["", "**Module total**", f"**{m['hours']}**", ""]], num_cols=(2,))

    h1("Volumes and Rates")
    doc.add_paragraph(f"{CONFIRMED_PRODUCTS} moulding products were confirmed in 21 categories of the source catalogue; the remaining categories are "
                      f"counted at project start. The estimate uses {PLANNED_PRODUCTS} products and about {PAGES} existing website pages.")
    add(doc, ["Item", "Basis"], [[n_, f"{r} hours × {q}"] for n_, q, r, _ in vh]
        + [["Additional products or pages", "Same rates per item"], ["Manual capture if automated extraction is not possible", "0.75 hours per product"]])

    h1("Content Rights and Legal Considerations")
    for t in client_rights(cfg):
        doc.add_paragraph(t, style="List Bullet")

    h1("Indicative Delivery Phasing")
    for t in ["Discovery and design: content capture, wireframes, visual design approval.",
              "Build: website foundation, pages, content migration and catalogue pages.",
              "Product set-up: extraction, preparation" + (", product outlines, image pilot and AI image generation" if ai else ", images")
              + ", Garrison review and sign-off.",
              "Launch: testing, user acceptance testing, domain switch-over and handover."]:
        doc.add_paragraph(t, style="List Number")
    doc.add_paragraph(f"Indicative duration: {duration_text(go + vt)}, subject to timely approvals and access.")

    h1("Items Not Included")
    for t in ["Administration portal, user roles and publishing workflow", "New logo or brand identity, copywriting and photography",
              "New product descriptions, technical drawings or documents", "E-commerce, pricing or quoting",
              "Hosting, domain and third-party service fees" + (" (AI fees are listed separately above)" if ai else ""),
              "Obtaining permission from Brenlo, and legal advice", "Project management (quoted separately if required)"]:
        doc.add_paragraph(t, style="List Bullet")

    h1("Key Assumptions and Dependencies")
    for t in ["Garrison provides domain/registrar access; the current website's source code is not required.",
              "Company email on Google Workspace continues to work; its records are preserved at switch-over.",
              f"Planning quantities of {PLANNED_PRODUCTS} products and {PAGES} pages; variance at the stated rates.",
              "Garrison supplies brand assets and approves content, designs and the product list within two review rounds each.",
              "Products change rarely; later changes are made by a developer."] + (
              ["AI service fees are paid at cost within the agreed cap.", "Garrison's counsel reviews the AI imagery approach before go-live."] if ai else []):
        doc.add_paragraph(t, style="List Number")

    h1("Comparison of the Three Options")
    add(doc, ["", "Option 1: Design + Migration", "Option 2: + AI Images", "Option 3: Premium Platform"], comparison_rows())

    h1("Disclaimer")
    doc.add_paragraph("Estimates are indicative. Final effort depends on the confirmed product and page counts, approval turnaround and access to the "
                      "source catalogue" + (", and AI service pricing at the time of generation." if ai else "."))
    doc.save(root / f"{code}_Estimation_Summary_FeatureWise_Client.docx")


# ---------------------------------------------------------------- comparison document
def write_comparison():
    o1, o2 = RESULTS["GWM"], RESULTS["GWA"]
    md = ["# Garrison Website & Catalogue — Estimation Options", "", f"**Client:** {b.CLIENT}  ", f"**Date:** {TODAY}", "",
          "Garrison has advised that products change rarely, so catalogue set-up is a one-time activity. Options 1 and 2 therefore have no administration "
          "portal; Option 3 is the full platform with self-service administration.", "",
          "## Options at a glance", "",
          "| | Option 1: Design + Migration | Option 2: + AI Images | Option 3: Premium Platform |", "|---|---|---|---|"]
    md += [f"| {' | '.join(str(c) for c in r)} |" for r in comparison_rows()]
    md += ["", "## What each option delivers", "",
           "- **Option 1 — Website design and product migration.** New website design and build (home, company pages, contact form, catalogue pages "
           "with filters and search), one-time migration of moulding products with their details and images from the Brenlo catalogue, SEO, "
           "hosting and launch. No admin portal.",
           "- **Option 2 — Option 1 plus AI product images.** As Option 1, but product images are original AI-assisted renders built from "
           "dimension-accurate outlines instead of copied photographs, plus AI lifestyle and banner images. AI service fees are pass-through.",
           "- **Option 3 — Premium online catalogue platform.** Admin portal with roles, configurable categories and attributes, publishing workflow, "
           "content rights tracking, bulk import and advanced search. Excludes the UX/UI design phase and project management.", "",
           "## Legal note", "",
           "All options use Brenlo's product data; Garrison should hold Brenlo's written permission. Option 2 avoids publishing Brenlo photographs but "
           "the profiles shown remain Brenlo designs, and AI images carry their own considerations (accuracy, ownership, provider terms). Garrison's "
           "counsel should review before go-live. This is not legal advice.", "",
           "## Detailed estimates", "",
           "- Option 1: Option-1-Website-Design-Migration/GWM_Estimation_Summary_FeatureWise_Client.docx",
           "- Option 2: Option-2-Website-AI-Imagery/GWA_Estimation_Summary_FeatureWise_Client.docx",
           "- Option 3: GMC_Estimation_Summary_FeatureWise_Client.docx", ""]
    (GARRISON / "Garrison_Estimation_Options_Comparison.md").write_text("\n".join(md))

    doc = b.base_doc()
    heading_block(doc, "Estimation Options", "Garrison Website & Moulding Catalogue", None)
    doc.add_heading("1. Background", level=1)
    doc.add_paragraph("Garrison has advised that products change rarely, so catalogue set-up is a one-time activity. Options 1 and 2 therefore have no "
                      "administration portal; Option 3 is the full platform with self-service administration.")
    doc.add_heading("2. Options at a Glance", level=1)
    b.add_table(doc, ["", "Option 1: Design + Migration", "Option 2: + AI Images", "Option 3: Premium Platform"], comparison_rows())
    doc.add_heading("3. What Each Option Delivers", level=1)
    for line in md[md.index("## What each option delivers") + 2: md.index("## Legal note") - 1]:
        b.add_runs(doc.add_paragraph(style="List Bullet"), line[2:])
    doc.add_heading("4. Legal Note", level=1)
    doc.add_paragraph(md[md.index("## Legal note") + 2])
    doc.add_heading("5. Detailed Estimates", level=1)
    for t in ["Option 1: Website Design & Product Catalogue Migration — detailed effort estimate (separate document)",
              "Option 2: Website Design, Product Catalogue Migration & AI Product Imagery — detailed effort estimate (separate document)",
              "Option 3: Online Moulding Catalogue Platform — detailed effort estimate (separate document)"]:
        doc.add_paragraph(t, style="List Bullet")
    doc.save(GARRISON / "Garrison_Estimation_Options_Comparison.docx")


# ---------------------------------------------------------------- main
def build(cfg, final=False):
    root, feats, mods = setup(cfg)
    root.mkdir(parents=True, exist_ok=True)
    write_sow(cfg, root, feats, mods)
    b.validate()
    b.write_features()
    write_modules_and_registry(cfg, root, feats, mods)
    all_h, go, opt = b.totals()
    vt = vol_total(cfg)
    ai = ai_cost()[2] if cfg["ai"] else None
    RESULTS[cfg["code"]] = dict(go=go, opt=opt, all=all_h, vol=vt, duration=duration_text(go + vt),
                                ai=(ai["Standard quality"], ai["High quality"]) if ai else None)
    if final:
        write_summaries(cfg, root, feats, mods)
        b.md_to_docx(root / f"SoW_{cfg['code']}_Detailed.md", root / f"SoW_{cfg['code']}_Detailed.docx")
        write_client_docx(cfg, root, feats, mods)
        print(f"{cfg['code']}: {len(feats)} features · software go-live {go} · volume {vt} · total {go + vt} · optional {opt}")
        for m in mods:
            print(f"  {m['nn']} {m['name']}: {len(b.feats(m))} features, {m['hours']} h")


def main():
    for cfg in OPTIONS.values():
        build(cfg)
    for cfg in OPTIONS.values():
        build(cfg, final=True)
    write_comparison()
    print("Comparison written.")


if __name__ == "__main__":
    main()
