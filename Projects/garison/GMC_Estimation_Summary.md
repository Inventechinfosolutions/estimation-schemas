# GMC — Estimation Summary (Internal)

**Project:** Garrison Online Moulding Catalogue Platform  
**Client:** Garrison Industries  
**Project code:** GMC  
**As of:** 2026-10-05  
**Source:** `SoW_GMC_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Value |
|--------|------:|
| Modules | 13 |
| Features | 53 |
| **Recommended go-live hours** | **4057** |
| Optional / conditional hours | 68 |
| **All-in hours** | **4125** |

Optional hours: F12-004 Catalogue Export & Bulk Update (68 h).

## Per-module hours

| # | Module | Type | Features | Hours | % of all-in |
|---|--------|------|---------:|------:|------------:|
| 01 | Administrator Access & Role Management | Shared | 4 | 397 | 9.6% |
| 02 | Catalogue Taxonomy & Master Data | Business | 3 | 215 | 5.2% |
| 03 | Dynamic Attribute & Dimension Framework | Business | 4 | 350 | 8.5% |
| 04 | Product Profile Management | Business | 7 | 550 | 13.3% |
| 05 | Combinations & Product Relationships | Business | 3 | 228 | 5.5% |
| 06 | Content Governance & Publishing Workflow | Business | 5 | 483 | 11.7% |
| 07 | External Source, Provenance & Content Rights | Business | 3 | 215 | 5.2% |
| 08 | Public Catalogue Experience | Business | 5 | 389 | 9.4% |
| 09 | Search & Filtering | Business | 4 | 317 | 7.7% |
| 10 | Product Enquiry | Business | 3 | 150 | 3.6% |
| 11 | SEO, Analytics & Website Integration | Shared | 4 | 254 | 6.2% |
| 12 | Catalogue Data Import & Bulk Operations | Technical | 4 | 342 | 8.3% |
| 13 | Platform Security, Performance & Operations | Technical | 4 | 235 | 5.7% |

## Hours by module type

| Type | Hours |
|------|------:|
| Business | 2897 |
| Shared | 651 |
| Technical | 577 |

## Hours by estimation area

| Area | Hours | % |
|------|------:|---:|
| UI | 1382 | 33.5% |
| API | 1576 | 38.2% |
| Database | 193 | 4.7% |
| Integration | 156 | 3.8% |
| Testing | 710 | 17.2% |
| Documentation | 108 | 2.6% |

## Timeline check against the proposal

The proposal states an indicative 10–12 week duration. Go-live effort of **4057 hours** corresponds to about **20.3 weeks with a 5-person team** or **16.9 weeks with a 6-person team** at 40 hours per person-week, before project management, UX/UI design and population labour. Delivering in 12 weeks would need about **8.5 full-time engineers**; otherwise extend the timeline to roughly 17–20 weeks or trim scope (candidates: F12-004, F11-004 insight dashboard, F07-003 dashboard, F09-004 suggestions, F03-003 impact management).

## Not included in feature hours

- Project management, discovery workshops and UX/UI design phase (wireframes, visual design)
- Initial catalogue population labour (extraction, normalisation, drawing preparation) — commercial lines B and C, per product
- Hosting, CDN, email, analytics and search service subscriptions
- Independent penetration testing; AMC / post-warranty support (commercial line D)

## Open assumptions / risks

1. Access model User → Role → Permissions with four default roles; no public login.
2. Dedicated search engine available in the hosting environment (choice at discovery).
3. Website integration via sub-path or sub-domain; CMS plugin embedding would need re-estimation.
4. Garrison confirms third-party content rights; the platform records and enforces, but does not verify legally.
5. Initial product count unknown; population labour priced separately.
6. English only; inches primary with optional millimetre display.
7. No e-commerce, pricing, inventory, CRM or ERP.

## Suggested next actions

1. Review modules, features and hours with the delivery lead; decide on F12-004 (optional).
2. Reconcile hours with the proposal's 10–12 week timeline and team plan (see timeline check).
3. Confirm website platform, hosting and search engine in discovery.
4. Use the client Word export: `GMC_Estimation_Summary_FeatureWise_Client.docx`.
