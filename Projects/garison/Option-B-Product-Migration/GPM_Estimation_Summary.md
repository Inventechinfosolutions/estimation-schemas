# GPM — Estimation Summary (Internal)

**Project:** Garrison Catalogue Product Migration to Existing Website (Option B)  
**Client:** Garrison Industries  
**Project code:** GPM  
**As of:** 2026-10-06  
**Related estimate:** GMC — Option A, full catalogue platform (`../GMC_Estimation_Summary.md`)

## Totals

| Metric | Hours |
|--------|------:|
| Software — go-live features | 536 |
| Per-product verification (350 products × 0.25 h) | 88 |
| **Recommended go-live total** | **624** |
| Optional features (F01-005 doors/in-stock, F03-006 combinations) | 70 |
| All-in (excluding optional per-product verification for doors/in-stock) | 694 |

## Source catalogue sizing

- Confirmed: **201 moulding products** in 21 categories (Baseboard 45, Casing 41, Backband 21, D4S 21, Crown 18, Doorstop 10, Inspire 9, Cove 7, others ≤ 5).
- Not countable remotely: 16 multi-word categories (for example Chair Rail, Quarter Round, Half Round, Panel Mould, Base Shoe, Window Stool, Tongue & Groove, Plinth/Corner Block) and Combinations — the source returned access errors for these URLs.
- Planning quantity: **350**. Variance charged at 0.25 h per product (automated path) or 0.75 h per product if manual capture is needed.
- Data per product: category, code, thickness × width, style, species options, one isometric image (about 541×402 px). No drawings, PDFs or descriptions.

## Per-module hours

| # | Module | Type | Features | Hours |
|---|--------|------|---------:|------:|
| 01 | Catalogue Data Extraction & Preparation | Technical | 5 | 214 |
| 02 | Product Data Store on Existing Website | Technical | 2 | 62 |
| 03 | Catalogue Pages on Existing Website | Business | 6 | 208 |
| 04 | Website Integration, SEO & Go-live | Shared | 4 | 122 |

## Hours by estimation area (software)

| Area | Hours |
|------|------:|
| UI | 144 |
| API | 246 |
| Database | 21 |
| Integration | 56 |
| Testing | 112 |
| Documentation | 27 |

## Comparison with Option A

| | Option A (GMC) | Option B (GPM) |
|---|---:|---:|
| Go-live hours | 4057 | 624 |
| Admin portal / self-service | Yes | No |
| Indicative duration | 17–20 weeks (5–6 people) | 7–8 weeks (2 people) or about 5 weeks (3 people) |

## Critical assumptions and risks

1. **Content rights:** Brenlo's images, codes and product data are Brenlo's. Garrison must hold written permission (for example as an authorised Brenlo dealer) before go-live. This is a go/no-go dependency.
2. **Source code (go/no-go):** Garrison owns and will hand over the complete, current source code of www.garrisonindustries.ky (templates, themes, plugins, build files and database), together with server/hosting, database and DNS access. The code must match the live site and Garrison must have the right to modify it. No admin logins are currently available, so all changes are made in code. If the source code cannot be provided or is out of date, this estimate does not apply; the alternatives are rebuilding the affected pages (re-estimate) or adopting Option A. The site resolves to a self-hosted cloud server; its SSL certificate did not validate during our review.
3. The source site may block automated extraction (some category URLs already return access errors). Contingency: supplier data file from Brenlo, or manual capture at the higher rate.
4. No admin portal: every later product change needs a developer.
5. Thin product content (no descriptions) limits SEO value compared with Option A.
