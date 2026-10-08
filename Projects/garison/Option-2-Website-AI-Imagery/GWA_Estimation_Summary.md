# GWA — Estimation Summary (Internal)

**Project:** Garrison Website Design, Product Catalogue Migration & AI Product Imagery (Option 2)  
**Client:** Garrison Industries  
**Project code:** GWA  
**As of:** 2026-10-07  
**Source:** `SoW_GWA_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Hours |
|--------|------:|
| Software — go-live features | 1078 |
| Per-product data verification (350 × 0.25 h) | 88 |
| Existing page content migration (15 × 1.5 h) | 23 |
| Profile silhouette preparation (operator time) (350 × 0.3 h) | 105 |
| AI image review and selection (350 × 0.2 h) | 70 |
| **Recommended go-live total** | **1364** |
| Optional features | 91 |
| All-in | 1455 |

## AI service cost (separate from hours)

| Item | Generations |
|------|------------:|
| Style exploration and 20-product pilot | 200 |
| Product images (350 products × about 4 candidates incl. regenerations) | 1400 |
| Lifestyle and category scenes (about 25 scenes × 10 candidates) | 250 |
| **Total** | **1850** |

| Price basis | Fees (USD) | +25% contingency (USD) |
|---|---:|---:|
| Standard quality @ 0.07 | 130 | 162 |
| High quality @ 0.23 | 426 | 532 |

Budget cap recommended: USD 600. Prices: OpenAI GPT Image 2 list prices checked October 2026 (about USD 0.053 medium / 0.211 high per 1024×1024 output, plus image input tokens; Batch API halves output cost).

## Per-module hours

| # | Module | Type | Features | Hours |
|---|--------|------|---------:|------:|
| 01 | Discovery & Website Design | Business | 3 | 149 |
| 02 | Website Build | Business | 5 | 183 |
| 03 | Product Catalogue Pages | Business | 6 | 206 |
| 04 | One-time Product Data Migration | Technical | 6 | 231 |
| 05 | Hosting, SEO & Launch | Shared | 5 | 149 |
| 06 | AI Product Imagery | Technical | 7 | 251 |

## Hours by estimation area (software)

| Area | Hours | Share |
|------|------:|------:|
| UI | 384 | 32.8% |
| API | 408 | 34.9% |
| Database | 23 | 2.0% |
| Integration | 100 | 8.6% |
| Testing | 196 | 16.8% |
| Documentation | 58 | 5.0% |

Design artefacts (wireframes, visual designs, scenes) are sized on the UI scale.

## Timeline check

Go-live total 1364 h ≈ 11.4 weeks with 3 people or 8.5 weeks with 4 (40 h/person-week), before project management.

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
2. **AI images reduce but do not remove the legal risk.** Brenlo photographs are not published and are not sent to the AI service. However, the silhouettes are traced from Brenlo references unless Garrison supplies its own drawings or samples, so the profiles shown are still Brenlo's product designs. Product data and codes still need permission.
3. **Accuracy and misrepresentation:** AI-assisted images may differ in detail from the physical product. Images are labelled 'illustrative' and checked against dimension-accurate silhouettes before publication.
4. **Ownership of AI output:** in many jurisdictions purely AI-generated images may not be protected by copyright, so Garrison may not be able to stop others from copying them.
5. **AI service terms and indemnity:** only services licensed for commercial use are used. Some providers (for example Adobe Firefly under qualifying enterprise plans) offer output indemnity, but this typically excludes outputs based on image inputs that themselves infringe. Our design only sends our own base renders and text prompts.
6. **Legal review:** Garrison's legal counsel (Cayman Islands) should review the approach before go-live. This document is not legal advice.
7. Website rebuilt from public pages; current source code not needed. Domain/registrar access is required.
8. Google Workspace MX/SPF/DKIM/DMARC records must be preserved at cutover.
9. Planning quantities: 350 products, 15 pages; variance at the volume rates.
10. Option 3 (GMC) excludes UX/UI design and project management; Options 1 and 2 include design but not project management.
