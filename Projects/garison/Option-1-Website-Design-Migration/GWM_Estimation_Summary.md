# GWM — Estimation Summary (Internal)

**Project:** Garrison Website Design & Product Catalogue Migration (Option 1)  
**Client:** Garrison Industries  
**Project code:** GWM  
**As of:** 2026-10-07  
**Source:** `SoW_GWM_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Hours |
|--------|------:|
| Software — go-live features | 862 |
| Per-product data verification (350 × 0.25 h) | 88 |
| Existing page content migration (15 × 1.5 h) | 23 |
| **Recommended go-live total** | **973** |
| Optional features | 70 |
| All-in | 1043 |

## Per-module hours

| # | Module | Type | Features | Hours |
|---|--------|------|---------:|------:|
| 01 | Discovery & Website Design | Business | 3 | 149 |
| 02 | Website Build | Business | 5 | 183 |
| 03 | Product Catalogue Pages | Business | 6 | 206 |
| 04 | One-time Product Data Migration | Technical | 6 | 245 |
| 05 | Hosting, SEO & Launch | Shared | 5 | 149 |

## Hours by estimation area (software)

| Area | Hours | Share |
|------|------:|------:|
| UI | 326 | 35.0% |
| API | 308 | 33.0% |
| Database | 18 | 1.9% |
| Integration | 68 | 7.3% |
| Testing | 166 | 17.8% |
| Documentation | 46 | 4.9% |

Design artefacts (wireframes, visual designs, scenes) are sized on the UI scale.

## Timeline check

Go-live total 973 h ≈ 8.1 weeks with 3 people or 6.1 weeks with 4 (40 h/person-week), before project management.

## Three-option comparison

| | Option 1 (GWM) | Option 2 (GWA) | Option 3 Premium (GMC) |
|---|---:|---:|---:|
| Software effort (go-live features) | 862 | 1078 | 4057 |
| Volume-based effort (products, pages, images) | 111 | 286 | Population by Garrison via admin portal |
| **Total go-live effort (hours)** | **973** | **1364** | **4057** |
| Optional features (hours) | 70 | 91 | 68 |
| AI service fees (pass-through) | — | USD 162–532 (cap USD 600) | — |
| New website design included | Yes | Yes | No (design phase excluded from estimate) |
| Admin portal and roles | No | No | Yes |
| Product images | Source images (permission needed) | Original AI-assisted images | Source or Garrison images, rights tracked |
| Later product changes | Developer | Developer | Garrison self-service |
| Indicative duration | About 9 weeks with 3 people, or 7 weeks with 4 | About 12 weeks with 3 people, or 9 weeks with 4 | 17–20 weeks (5–6 people) |

## Critical assumptions and risks

1. **Brenlo content (go/no-go):** Brenlo's product data, product codes and photographs are Brenlo's content. Garrison should hold written permission from Brenlo (for example as an authorised dealer or distributor) before publishing them. If Garrison is not a Brenlo dealer, it should not present Brenlo product codes as its own range.
2. Website rebuilt from public pages; current source code not needed. Domain/registrar access is required.
3. Google Workspace MX/SPF/DKIM/DMARC records must be preserved at cutover.
4. Planning quantities: 350 products, 15 pages; variance at the volume rates.
5. Option 3 (GMC) excludes UX/UI design and project management; Options 1 and 2 include design but not project management.
