"""Consolidated three-option estimate with a simple features list, an options matrix and a 20% feature-level reduction.

Run from repo root:
    .venv/bin/python Projects/garison/_pipeline/build_consolidated.py
"""
from __future__ import annotations

import datetime as dt
import math
import sys
from copy import deepcopy
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build_gmc as b  # noqa: E402

GMC_FEATURES, GMC_MODULES = deepcopy(b.FEATURES), deepcopy(b.MODULES)

import build_gwx as g  # noqa: E402
import gwx_data  # noqa: E402

REDUCTION = 0.20
FACTOR = 1 - REDUCTION
OUT = g.GARRISON / "Garrison_Consolidated_Estimation_3_Options"
DISPLAY_NAME = {"Environments & Deployment Pipeline": "Environments & Deployment Automation"}


def simple(desc, limit=110):
    s = desc.split(". ")[0].rstrip(".").replace("deployment pipeline", "deployment process")
    if ":" in s[:limit]:
        return s[:s.index(":")]
    if len(s) <= limit:
        return s
    cut = max(s.rfind(", ", 0, limit), s.rfind(" (", 0, limit), s.rfind(" with ", 0, limit))
    if s[:cut].count("(") > s[:cut].count(")"):
        cut = s.rfind(" (", 0, cut)
    return s[:cut] if cut > 15 else s[:limit].rsplit(" ", 1)[0]


def red(h):
    return int(h * FACTOR + 0.5)


def option_data(feats, mods, volume, label, title, code):
    feats = [f for f in feats if f.get("notes") != "Optional"]
    rows_by_module = []
    for m in mods:
        mf = [f for f in feats if f["id"][1:3] == m["nn"]]
        items = [dict(id=f["id"], name=DISPLAY_NAME.get(f["name"], f["name"]),
                      desc=simple(f["desc"]),
                      hours=red(f["hours"]), optional=f.get("notes") == "Optional") for f in mf]
        rows_by_module.append(dict(nn=m["nn"], name=m["name"], items=items, hours=sum(i["hours"] for i in items),
                                   go=sum(i["hours"] for i in items if not i["optional"])))
    go = sum(i["hours"] for m in rows_by_module for i in m["items"] if not i["optional"])
    opt = sum(i["hours"] for m in rows_by_module for i in m["items"] if i["optional"])
    vol = [(n, q, round(r * FACTOR, 3), int(q * r * FACTOR + 0.5)) for n, q, r in volume]
    vt = sum(v[3] for v in vol)
    return dict(label=label, title=title, code=code, modules=rows_by_module, go=go, opt=opt, vol=vol, vt=vt, total=go + vt,
                count=len(feats))


def build_options():
    out = {}
    for code, cfg in g.OPTIONS.items():
        _, feats, mods = g.setup(cfg)
        out[code] = option_data(feats, mods, cfg["volume"], cfg["label"], cfg["short"], code)
    feats3, mods3 = premium_with_website()
    out["GMC"] = option_data(feats3, mods3, [("Existing page content migration", g.PAGES, 1.5)], "Option 3",
                             "Premium online catalogue platform with website design", "GMC")
    return out


PREMIUM_WEBSITE = {"F01-001": "F14-001", "F01-002": "F14-002", "F01-003": "F14-003",
                   "F02-001": "F15-001", "F02-002": "F15-002", "F02-003": "F15-003", "F02-005": "F15-004"}


def premium_with_website():
    """Premium platform plus the same website design and company-page features as Options 1 and 2.
    The contact form (F02-004) is omitted because the premium Product Enquiry module covers it."""
    feats = deepcopy(GMC_FEATURES)
    for f in feats:
        f.setdefault("notes", "Go-live")
    for f in deepcopy(gwx_data.M01 + gwx_data.M02):
        if f["id"] in PREMIUM_WEBSITE:
            f["id"] = PREMIUM_WEBSITE[f["id"]]
            f.setdefault("notes", "Go-live")
            f["hours"] = sum(r[3] for r in b.rows(f))
            feats.append(f)
    mods = deepcopy(GMC_MODULES) + [dict(nn="14", name="Website Discovery & Design"), dict(nn="15", name="Website Build & Content Migration")]
    return feats, mods


GROUP_OF_MODULE = {
    "GWM": {"01": "Website", "02": "Website", "03": "What visitors see", "04": "Products and pictures", "05": "Going live and running the website"},
    "GMC": {"01": "Managing the catalogue (behind the scenes)", "02": "Managing the catalogue (behind the scenes)", "03": "Managing the catalogue (behind the scenes)",
            "04": "Managing the catalogue (behind the scenes)", "05": "Managing the catalogue (behind the scenes)", "06": "Managing the catalogue (behind the scenes)",
            "07": "Managing the catalogue (behind the scenes)", "08": "What visitors see", "09": "What visitors see", "10": "What visitors see",
            "11": "Going live and running the website", "12": "Products and pictures", "13": "Going live and running the website", "14": "Website", "15": "Website"},
}
GROUP_OF_MODULE["GWA"] = {**GROUP_OF_MODULE["GWM"], "06": "Products and pictures"}


def group_hours(o):
    groups = {cap: 0 for cap, vals in MATRIX if vals is None}
    for m in o["modules"]:
        groups[GROUP_OF_MODULE[o["code"]][m["nn"]]] += sum(i["hours"] for i in m["items"] if not i["optional"])
    for name, _, _, h in o["vol"]:
        groups["Website" if "page" in name.lower() else "Products and pictures"] += h
    return groups


def dur(hours, a, bb):
    return f"About {math.ceil(hours / (a * 40))} to {math.ceil(hours / (bb * 40))} weeks, team of {bb} to {a}" if a != bb else ""


def fmt(n):
    return f"{n:,}"


MATRIX = [
    ("Website", None),
    ("New website design, including the home page and company pages", ("Yes", "Yes", "Yes")),
    ("Content moved over from the current website", ("Yes", "Yes", "Yes")),
    ("Contact form", ("Enquiries are emailed to Garrison", "Enquiries are emailed to Garrison",
     "Each enquiry goes to the right person, and all enquiries are kept in one list")),
    ("What visitors see", None),
    ("Product page", ("Code, size, style, wood type and one picture", "Same as Option 1",
     "Everything in Option 1, plus a description, a profile drawing visitors can zoom into, finish colours, available lengths, "
     "more pictures and downloadable product sheets")),
    ("Product filters", ("Style, thickness, width and wood type", "Same as Option 1",
     "More filters, such as finish, use, collection and height, which Garrison can change itself")),
    ("Search", ("By code, type, style or size", "Same as Option 1", "Same as Option 1, with suggestions as you type")),
    ("Related products", ("Similar sizes are shown automatically", "Same as Option 1",
     "Garrison picks the matching products, such as the casing that goes with a crown")),
    ("Trim combinations (mouldings shown together as a set)", ("No", "No",
     "Yes, with each part linked to its own product page")),
    ("Product collections chosen by Garrison", ("No", "No",
     "Yes. Garrison can create its own collections, such as Best Sellers, Colonial Look (a matching crown, casing and baseboard) "
     "or In Stock in Cayman, and each one gets its own page")),
    ("Products and pictures", None),
    ("Setting up the products at the start", ("We transfer the products once, and Garrison approves the list in a spreadsheet", "Same as Option 1",
     "Garrison uploads the products from a spreadsheet itself, at launch and at any time later")),
    ("Product pictures", ("Brenlo's existing pictures (Brenlo's permission is required)",
     "New pictures made with AI for all 350 products. Each product is first drawn to its exact shape, then given a realistic finish "
     "and checked by our team. Room and banner pictures for the website are also included",
     "Several pictures per product, from Brenlo or from Garrison's own photography, uploaded by Garrison")),
    ("Product sheets and installation guides (PDF downloads)", ("No", "No", "Yes")),
    ("Adding a new product type, such as doors", ("Needs new development work", "Needs new development work",
     "Garrison sets it up itself, with no development needed")),
    ("Managing the catalogue (behind the scenes)", None),
    ("Product changes after go-live", ("Made by our developer on request", "Made by our developer on request",
     "Made by Garrison's own staff at any time")),
    ("Staff logins", ("No", "No", "Yes, with different access levels, such as edit only or edit and approve")),
    ("Approval before a product goes live", ("Garrison reviews the spreadsheet once, before launch", "Garrison reviews the spreadsheet once, before launch",
     "A manager reviews and approves every change before it goes live")),
    ("Showing or hiding a product", ("Done by our developer", "Done by our developer", "Done by Garrison in one click")),
    ("Change history", ("No", "No", "Yes, a full record of who changed what and when")),
    ("Permission to use Brenlo's content", ("Garrison confirms once", "Garrison confirms once, and we keep a record of how each AI picture was made",
     "Recorded for each product, and nothing without permission can go live")),
    ("Going live and running the website", None),
    ("Google search setup", ("Set up at launch", "Same as Option 1", "Set up at launch and updated automatically when products change")),
    ("Visitor reports", ("Pages and products viewed, and enquiries received", "Same as Option 1",
     "More detail, including searches that found no results")),
    ("Hosting and upkeep", ("Simple, low-cost hosting", "Same as Option 1",
     "Higher hosting cost, with automatic backups, monitoring and extra security")),
    ("Cost of changes after go-live", ("Developer time for each change", "Developer time for each change, plus AI charges for any new pictures",
     "No developer cost for product changes")),
]

OPTION_HEADS = "Option 1: Website and Products | Option 2: Website, Products and AI Pictures | Option 3: Premium Catalogue Platform"


def long_date(iso):
    return dt.date.fromisoformat(iso).strftime("%-d %B %Y")


PREMIUM_VALUE = {
    "01": ("Staff logins and access levels",
           "Each staff member has their own login. Garrison decides who can edit and who can approve, and can see who changed what"),
    "02": ("Setting up product types, styles and wood types",
           "Garrison can add or rename product types (crown, casing, baseboard), styles, product groups, wood types and finishes itself"),
    "03": ("The right details for each product type",
           "Each product type shows its own details (for example a crown shows its angle; a door shows its height and panel style). "
           "New product types can be added without a developer"),
    "04": ("Adding and editing products",
           "Simple forms for descriptions, sizes, finishes, lengths, pictures, drawings and PDF sheets. Copy a similar product to save time, "
           "hide old products and bring them back, and preview a page before it goes live"),
    "05": ("Matching products and trim combinations",
           "Show which products go together (for example the casing that matches a crown) and build combinations from several products"),
    "06": ("Checking and approving before going live",
           "Warns if something important is missing; a manager approves before publishing; show or hide one or many products at once; email reminders"),
    "07": ("Tracking permission to use Brenlo's content",
           "Records where each product's details and pictures came from and whether Garrison may use them. Anything without permission cannot go live"),
    "08": ("Richer product pages for visitors", "Drawings visitors can zoom into, size tables, finish colours and combination pages"),
    "09": ("Better search and product choices",
           "Search stays up to date automatically, gives suggestions while typing, and Garrison chooses how visitors narrow down products"),
    "10": ("Handling enquiries", "Each enquiry goes to the right person and is kept in a list so nothing is missed"),
    "11": ("Google listing and visitor reports",
           "The Google listing updates itself when products change; detailed reports on what visitors look at and search for"),
    "12": ("Adding many products at once",
           "Upload many products from a spreadsheet and many pictures in one go, check them on screen, then publish"),
    "13": ("Security, backups and reliability",
           "Fast-loading pictures, protection against hackers and harmful files, automatic backups, monitoring, and a separate test "
           "website for trying changes safely"),
}

SCENARIOS = [
    ("Add five new mouldings", "Send the details to our developer. About 2–4 hours of work, usually done within a few working days",
     "Staff add them in a simple form (or upload a spreadsheet), a manager approves, and they are live the same day"),
    ("Remove a product that is no longer sold", "Our developer makes the change (about 1 hour)", "Hide it with one click"),
    ("Start selling interior doors, which need different details (height, width, panel style)", "New development, about 40 hours",
     "Garrison sets up 'Doors' in the control panel and adds the products. No developer needed"),
    ("Update the sizes of 100 products from a supplier's spreadsheet",
     "Our developer updates the products and Garrison checks the spreadsheet again (about 4–8 hours)",
     "Staff upload the spreadsheet, check the changes on screen and confirm"),
    ("Add a drawing or an installation guide (PDF) to a product", "Not possible without new development", "Upload it on the product"),
    ("Find out who changed a product and when", "Ask our developer", "Look at the product's change history"),
    ("Show that Garrison is allowed to use a picture, if asked", "Only the spreadsheet Garrison signed", "Each product shows where its content came from and the permission"),
    ("Follow up on enquiries", "Search the email inbox", "A list of all enquiries, showing which ones have been answered"),
]


AI_PART_NAMES = {
    "F06-001": "Agreeing the picture style and a trial on 20 products",
    "F06-002": "Tool for drawing each product's outline",
    "F06-003": "Turning each outline into a 3D picture and adding a realistic finish with AI",
    "F06-004": "Screen for checking and choosing the best picture for each product",
    "F06-005": "Room and banner pictures for the website",
    "F06-006": "'Illustrative picture' labels and a record of how each picture was made",
}


def option2_section(o1, o2, gh):
    def mod(o, nn):
        return next(m for m in o["modules"] if m["nn"] == nn)

    def vol(o, word):
        return next(v for v in o["vol"] if word in v[0].lower())

    m4a, m4b, m6 = mod(o1, "04"), mod(o2, "04"), mod(o2, "06")
    details = sum(i["hours"] for i in m4a["items"] if not i["optional"] and i["id"] != "F04-002")
    pics1 = next(i["hours"] for i in m4a["items"] if i["id"] == "F04-002")
    pics2 = next(i["hours"] for i in m4b["items"] if i["id"] == "F04-002")
    check, outline, review = vol(o2, "verification"), vol(o2, "silhouette"), vol(o2, "review")
    ai = [i for i in m6["items"] if not i["optional"]]
    ai_total = sum(i["hours"] for i in ai)
    p1, p2 = gh["GWM"]["Products and pictures"], gh["GWA"]["Products and pictures"]
    assert details + pics1 + check[3] == p1 and details + pics2 + check[3] + ai_total + outline[3] + review[3] == p2
    per_product = outline[3] + review[3]
    out = ["## 4. What the Extra Cost of Option 2 Pays For", "",
           f"Option 2 has the same product work as Option 1, plus about {p2 - p1} hours to create a new, accurate picture for each of the "
           f"{g.PLANNED_PRODUCTS} products instead of using Brenlo's photos. This is why 'Products and pictures' is {p2} hours in Option 2 "
           f"and {p1} hours in Option 1.", "",
           "| Part of the work | Option 1 | Option 2 |", "|---|---:|---:|",
           f"| Copying the product details from Brenlo, tidying them up, Garrison's spreadsheet check and loading them into the website | {details} | {details} |",
           f"| Product pictures: copying Brenlo's photos (Option 1), or keeping them only as private references (Option 2) | {pics1} | {pics2} |",
           f"| Checking each product's details ({check[1]} products × {check[2]} hours) | {check[3]} | {check[3]} |"]
    out += [f"| {AI_PART_NAMES[i['id']]} | — | {i['hours']} |" for i in ai]
    out += [f"| Drawing each product's outline at its real size ({outline[1]} products × {outline[2]} hours) | — | {outline[3]} |",
            f"| Checking and choosing each AI picture ({review[1]} products × {review[2]} hours) | — | {review[3]} |",
            f"| **Total** | **{p1}** | **{p2}** |", "",
            "### Why each picture needs work", "",
            "An AI tool cannot draw a correct moulding just from its name. Asked for a '5¼-inch colonial crown', it draws a crown that looks "
            "right but has the wrong shape. Because visitors choose mouldings by their exact shape, every picture must be accurate. For each "
            "product we:", "",
            "1. Draw the real outline of the moulding at its real size.",
            "2. Turn the outline into a plain 3D picture, so the shape is exactly right.",
            "3. Let the AI add a realistic wood or paint finish and lighting.",
            "4. Check the picture against the outline before it goes on the website.", "",
            f"Steps 1 and 4 are repeated for all {g.PLANNED_PRODUCTS} products ({per_product} hours). The remaining {ai_total} hours set up the "
            "process once. AI service fees are separate (see the summary table).", "",
            "### Ways to reduce the cost of Option 2", "",
            "| Choice | Saving | What changes |", "|---|---|---|",
            f"| Garrison provides its own drawings of its profiles | Most of the {outline[3]} hours of outline drawing | Depends on Garrison having the drawings |",
            f"| Leave out the room and banner pictures | {next(i['hours'] for i in ai if i['id'] == 'F06-005')} hours | "
            "Use stock photos or Garrison's own photos instead |",
            "| Let the AI create pictures without the outline and 3D steps | About 150 hours | Pictures will often show the wrong shape, which is risky for a product catalogue |",
            "| Use AI only for room, banner and category pictures; product pages show a clean outline drawing | Roughly 250–300 hours (quoted on request) | "
            "Product pictures look technical rather than like photographs |", ""]
    return out


def write(opts):
    o1, o2, o3 = opts["GWM"], opts["GWA"], opts["GMC"]
    gens, raw, cont = g.ai_cost()
    ai_fee = f"USD {cont['Standard quality']:,} to {cont['High quality']:,}, capped at USD {g.AI_BUDGET_CAP}"
    durations = {"GWM": f"About {math.ceil(o1['total'] / 120)} weeks, team of 3", "GWA": f"About {math.ceil(o2['total'] / 120)} weeks, team of 3",
                 "GMC": dur(o3["total"], 6, 5)}

    md = ["# Garrison Website & Moulding Catalogue — Consolidated Estimate", "", f"**Client:** {b.CLIENT}  ", f"**Date:** {g.TODAY}  ",
          "**Effort unit:** person-hours", "", "## 1. Introduction", "",
          "This document brings together three options for Garrison Industries' website and moulding catalogue. Garrison has advised that "
          "products change rarely, so Options 1 and 2 set up the catalogue once and have no administration portal. Option 3 is the full "
          "platform with self-service administration.", "",
          "- **Option 1 — Website design and product migration:** new website design and build, with the Brenlo moulding products and their details migrated once.",
          "- **Option 2 — Option 1 plus AI product images:** as Option 1, with original AI-assisted product images and lifestyle imagery instead of copied photographs.",
          "- **Option 3 — Premium online catalogue platform:** the same new website design and company pages as Options 1 and 2, plus admin portal, configurable catalogue, publishing workflow, rights tracking, bulk import and advanced search.", "",
          "## 2. Summary of Options", "",
          f"| Item | {OPTION_HEADS} |", "|---|---|---|---|",
          f"| Number of features | {o1['count']} | {o2['count']} | {o3['count']} |",
          f"| Website and feature development (hours) | {fmt(o1['go'])} | {fmt(o2['go'])} | {fmt(o3['go'])} |",
          f"| Product, page and picture setup (hours) | {fmt(o1['vt'])} | {fmt(o2['vt'])} | {fmt(o3['vt'])} |",
          f"| **Total effort (hours)** | **{fmt(o1['total'])}** | **{fmt(o2['total'])}** | **{fmt(o3['total'])}** |",
          f"| AI picture service charges (paid at actual cost, in addition to the hours) | Not applicable | {ai_fee} | Not applicable |",
          f"| Estimated timeline | {durations['GWM']} | {durations['GWA']} | {durations['GMC']} |", "",
          "## 3. Options Matrix", "",
          "All three options include the same new website. The main difference is who looks after the product catalogue once the "
          "website is live.", "",
          "- **Options 1 and 2:** We set up the products once. Any later changes are made by our developer.",
          "- **Option 3:** Garrison gets its own easy-to-use control panel, so its staff can add, edit, review and publish products "
          "themselves. The product pages also carry much more detail.", "",
          f"| Feature | {OPTION_HEADS} |",
          "|---|---|---|---|"]
    gh = {c: group_hours(opts[c]) for c in ("GWM", "GWA", "GMC")}
    for c, o in opts.items():
        assert sum(gh[c].values()) == o["total"], (c, gh[c], o["total"])
    for cap, vals in MATRIX:
        if vals is None:
            md.append(f"| **{cap}** | " + " | ".join(f"**{fmt(gh[c][cap])} hours**" if gh[c][cap] else "**Not included**" for c in ("GWM", "GWA", "GMC")) + " |")
        else:
            md.append(f"| {cap} | {' | '.join(vals)} |")
    md += [f"| **Total effort (hours)** | **{fmt(o1['total'])}** | **{fmt(o2['total'])}** | **{fmt(o3['total'])}** |", "",
           "The hours shown on each section row are the effort for that section.", ""]

    extra = o3["total"] - o1["total"]
    hidden = sum(m["go"] for m in o3["modules"] if m["nn"] not in ("14", "15"))
    md += option2_section(o1, o2, gh)
    md += ["## 5. What the Extra Cost of Option 3 Pays For", "",
           f"Option 3 costs about {fmt(extra)} hours more than Option 1. The website part is about the same in both. The difference is in "
           f"the products: Option 1 spends {fmt(o1['total'] - gh['GWM']['Website'])} hours setting them up once, while Option 3 spends "
           f"{fmt(hidden)} hours on Garrison's own control panel and richer product pages.", "",
           "Most of this work is in the control panel, the screens Garrison staff use to manage products. Visitors never see it, which is why "
           "the difference is hard to spot just by looking at the website. The table shows what the extra hours pay for.", "",
           "| What Garrison gets | What it means | Hours |", "|---|---|---:|"]
    md += [f"| {PREMIUM_VALUE[m['nn']][0]} | {PREMIUM_VALUE[m['nn']][1]} | {m['go']} |" for m in o3["modules"] if m["nn"] in PREMIUM_VALUE]
    md += [f"| **Total** | | **{fmt(hidden)}** |", ""]

    md += ["## 6. Everyday Situations After Go-live", "", "What happens when Garrison wants to make common changes:", "",
           "| Situation | Options 1 and 2 | Option 3 |", "|---|---|---|"]
    md += [f"| {a} | {b_} | {c} |" for a, b_, c in SCENARIOS]
    md += ["", "In Option 2, each new product also needs a new AI picture.", "",
           "## 7. Which Option Is Right for Garrison", "",
           "- **Option 1** is right if the product range will stay small and rarely change, Garrison is happy to ask a developer for the occasional "
           "change, and it wants the lowest cost and the quickest launch. Brenlo's permission to use its pictures is needed.",
           "- **Option 2** is right in the same situation if Garrison prefers its own new pictures instead of using Brenlo's.",
           "- **Option 3** is right if Garrison plans to sell more types of products (for example doors, sheet goods or products from other "
           "suppliers), several staff will look after the catalogue, it wants drawings and PDF sheets on product pages, it wants changes "
           "approved before they go live, or it does not want to rely on a developer for product changes.", "",
           "Option 3 is an investment in a catalogue that Garrison runs and grows itself. If the range will stay as it is, Option 1 or 2 is the "
           "better value. Garrison can also start with Option 1 or 2 and move to Option 3 later: the product information we prepare can be "
           "loaded into Option 3, so that work is not wasted.", ""]

    sec = 8
    for o in (o1, o2, o3):
        md += [f"## {sec}. {o['label']} — {o['title'][0].upper() + o['title'][1:]}: Features", ""]
        for m in o["modules"]:
            md += [f"### {o['label']} · {m['nn']}. {m['name']}", "", "| Feature ID | Feature | Description | Hours |", "|---|---|---|---:|"]
            md += [f"| {i['id']} | {i['name']} | {i['desc']} | {i['hours']} |" for i in m["items"]]
            md += [f"| | **Module total** | | **{m['hours']}** |", ""]
        if o["vol"]:
            md += [f"### {o['label']} · Product, page and image effort", "", "| Item | Quantity | Hours per item | Hours |", "|---|---:|---:|---:|"]
            md += [f"| {n} | {q} | {r} | {h} |" for n, q, r, h in o["vol"]] + [f"| **Total** | | | **{o['vt']}** |", ""]
        md += [f"**{o['label']} total: {fmt(o['go'])} feature hours" + (f" + {o['vt']} product, page and image hours = {fmt(o['total'])} hours" if o["vt"] else "") + ".**", ""]
        if o is o2:
            md += ["AI service fees are paid at provider rates, separately from effort: about "
                   f"{gens:,} image generations, {ai_fee}, including 25% contingency.", ""]
        sec += 1

    md += [f"## {sec}. Key Assumptions", "",
           f"1. Planning quantities: {g.PLANNED_PRODUCTS} moulding products and about {g.PAGES} existing website pages; extra items at the same per-item rates.",
           "2. Options 1 and 2 rebuild the website from its public content; only domain/registrar access is needed, and company email records are preserved.",
           "3. Garrison approves designs, content and the product list within two review rounds each.",
           "4. In Options 1 and 2, later product changes are made by a developer.",
           "5. Option 3 includes the same website design, home page, company pages and content migration as Options 1 and 2; "
           "its product enquiry module replaces the separate contact form. Administration portal screens follow the agreed design system.",
           "6. Project management, hosting fees, third-party fees, copywriting and photography are not included in any option.", ""]
    sec += 1
    md += [f"## {sec}. Content Rights", "",
           "All options use Brenlo's product data; Garrison should hold Brenlo's written permission before publication. Option 2 avoids publishing "
           "Brenlo photographs, but the profiles shown remain Brenlo designs, and AI-assisted images carry their own considerations (accuracy, ownership, "
           "provider terms). Garrison's legal counsel should review the chosen option before go-live. This document is not legal advice.", ""]
    sec += 1
    md += [f"## {sec}. Disclaimer", "", "Estimates are indicative and subject to confirmation of product and page counts, approval turnaround, "
           "access to the source catalogue and, for Option 2, AI service pricing at the time of generation.", ""]

    OUT.with_suffix(".md").write_text("\n".join(md))
    b.md_to_docx(OUT.with_suffix(".md"), OUT.with_suffix(".docx"))
    write_client(md, o1, o2, o3)


CLIENT_OUT = g.GARRISON / "Garrison_Estimation_Options_Client"


def add_serial_numbers(lines):
    """Prepend a Sl. No. column to every table; bold rows (group headings and totals) stay unnumbered."""
    out, n, prev_table = [], 0, False
    for line in lines:
        is_table = line.startswith("|")
        if is_table and not prev_table:
            n = 0
            out.append("| Sl. No. " + line)
        elif is_table and set(line) <= set("|:- "):
            out.append("|---:" + line)
        elif is_table and line.startswith("| **"):
            out.append("| " + line)
        elif is_table:
            n += 1
            out.append(f"| {n} " + line)
        else:
            out.append(line)
        prev_table = is_table
    return out


def write_client(md, o1, o2, o3):
    """Client copy: Summary of Options and Options Matrix only, renumbered, with the notes the client needs to read them alone."""
    a, z = md.index("## 2. Summary of Options"), md.index("## 4. What the Extra Cost of Option 2 Pays For")
    body = [l.replace("## 2. Summary of Options", "## 1. Summary of Options").replace("## 3. Options Matrix", "## 2. Options Matrix")
            for l in md[a:z]]
    body = add_serial_numbers(body)
    out = ["# Garrison Website and Moulding Catalogue: Estimate Options", "", f"**Client:** {b.CLIENT}  ", f"**Date:** {long_date(g.TODAY)}", "",
           "This document sets out three options for Garrison's new website and moulding catalogue. Each option includes a new website "
           "design. The options differ in how the product catalogue is set up and how it is maintained after the website goes live.", ""] + body
    out += ["## 3. Important Notes", "",
            f"1. All hours are our team's effort. They assume about {g.PLANNED_PRODUCTS} moulding products and about {g.PAGES} pages "
            "on the current website. Additional products or pages will be charged at the same rate.",
            "2. None of the options include project management, hosting or domain charges, other third-party fees, new written content "
            "or photography.",
            "3. Garrison will need written permission from Brenlo to use Brenlo's product information. Options 1 and 3 also need "
            "permission to use Brenlo's pictures.",
            "4. Garrison will need to give us access to its domain settings so the new website can go live. Company email will not be affected.",
            "5. In Option 2, the AI picture service is charged at actual cost and will not exceed the limit shown in the summary.",
            "6. These are indicative estimates. We will confirm them once the final number of products and pages is known.", ""]
    CLIENT_OUT.with_suffix(".md").write_text("\n".join(out))
    b.md_to_docx(CLIENT_OUT.with_suffix(".md"), CLIENT_OUT.with_suffix(".docx"))


def main():
    opts = build_options()
    write(opts)
    for o in opts.values():
        print(f"{o['label']} ({o['code']}): features {o['go']} + volume {o['vt']} = {o['total']}")


if __name__ == "__main__":
    main()
