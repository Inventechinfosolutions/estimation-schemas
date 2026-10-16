# BPA — Estimation Summary (Internal)

**Project:** BDA Post-Auction Award, Payment and Completion Management Module  
**Client:** Bangalore Development Authority (BDA)  
**Project code:** BPA  
**As of:** 2026-10-14  
**Source:** `SoW_BPA_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Value |
|--------|------:|
| Modules | 16 |
| Features | 75 |
| **Recommended go-live hours** | **4766** |
| Conditional hours | 49 |
| **All-in hours** | **4815** |
| All-in person-days (8 h) | 602 |

Conditional: F09-002 Kaveri Registration Data Exchange (Conditional) (49 h).

## Per-module hours

| # | Module | Type | Features | Hours | % of all-in |
|---|--------|------|---------:|------:|------------:|
| 01 | User, Role & Access Management | Shared | 4 | 515 | 10.7% |
| 02 | Auction Rules & Configuration | Business | 6 | 499 | 10.4% |
| 03 | KPPP Result Intake & Site Package | Business | 5 | 502 | 10.4% |
| 04 | Result Verification & Approval | Business | 5 | 400 | 8.3% |
| 05 | Successful Bidder Notification & Account | Business | 4 | 233 | 4.8% |
| 06 | Payment & Instalment Management | Business | 9 | 766 | 15.9% |
| 07 | Case Forwarding & Deputy Secretary Processing | Business | 5 | 293 | 6.1% |
| 08 | Draft Sale Deed | Business | 4 | 182 | 3.8% |
| 09 | Registration Recording & Completion | Business | 4 | 175 | 3.6% |
| 10 | Bidder Tracking Portal | Business | 5 | 169 | 3.5% |
| 11 | Dashboards, MIS & Reports | Business | 5 | 235 | 4.9% |
| 12 | Notification Service | Shared | 4 | 199 | 4.1% |
| 13 | Integration Hub | Technical | 4 | 223 | 4.6% |
| 14 | Audit, Security & Compliance | Technical | 4 | 192 | 4.0% |
| 15 | Platform Operations & Support | Technical | 4 | 121 | 2.5% |
| 16 | Legacy Case Migration | Technical | 3 | 111 | 2.3% |

## Hours by module type

| Type | Hours | % |
|------|------:|---:|
| Business | 3454 | 71.7% |
| Shared | 714 | 14.8% |
| Technical | 647 | 13.4% |

## Hours by estimation area

| Area | Hours | % |
|------|------:|---:|
| UI | 1360 | 28.2% |
| API | 2140 | 44.4% |
| Database | 223 | 4.6% |
| Integration | 212 | 4.4% |
| Testing | 724 | 15.0% |
| Documentation | 156 | 3.2% |

## Top 10 features by effort

| Feature | Name | Hours |
|---------|------|------:|
| F01-003 | Permission Matrix & DS-wise Data Isolation | 147 |
| F06-002 | Online Instalment Payment & Receipt | 145 |
| F01-002 | Staff User Management & Role Assignment | 142 |
| F01-001 | Staff Authentication & Session Security | 136 |
| F03-001 | KPPP Result Receipt through API | 135 |
| F04-003 | Multi-Level Result Approval Workflow | 129 |
| F06-004 | Daily Bank Reconciliation | 112 |
| F03-004 | CDRMS Site Package Retrieval & Case File Creation | 111 |
| F04-001 | Site-wise Result Review Workbench | 109 |
| F02-001 | Instalment & Payment Rule Configuration | 105 |

## Timeline check against the RFP

The RFP expects development complete by T + 75 days and go-live by T + 100 days, with a minimum team of a project manager, technical lead, two developers, a UI/UX designer and a QA engineer. Go-live effort of **4766 hours** equals about **30 weeks** for four build-and-test engineers at 40 hours per week. Meeting T + 75 days (about 11 weeks, less SRS and prototype time) needs roughly **15 full-time engineers** over 8 build weeks. Plan a larger build team than the RFP minimum, reuse a proven workflow, notification and integration base, or agree a phased go-live (payments and tracking first, report builder and Kaveri later).

## Not included in feature hours

- Project management, SRS, integration study and UI/UX prototype phase
- Training (two rounds per role), bidder help guide and video tutorials
- VAPT by a CERT-In empanelled auditor (before go-live and annual)
- On-site deployment of two professionals during implementation and support
- Warranty (1 year) and operation and maintenance (3 years), including on-site support engineer
- Hosting, gateway, SMS / WhatsApp / e-mail charges, DSC tokens and certificates

## Open assumptions / risks

1. KPPP API may not be provided; the controlled upload route (F03-002) is fully estimated as a fallback and both routes are in scope.
2. CDRMS read API and status update API are available; otherwise a file-based exchange is needed.
3. Payment gateway is BDA's existing provider with standard settlement files; one bank format assumed.
4. e-Sign / DSC: server-side signing service or officer USB token signing through a signer utility, confirmed in SRS.
5. Kaveri exchange (F09-002) is conditional and kept outside go-live hours.
6. Legacy pending cases provided by BDA in the migration templates; data cleansing is BDA's responsibility.
7. WhatsApp is built behind a switch and enabled only when BDA provides the business account.

## Suggested next actions

1. Review modules, features and hours with the delivery lead.
2. Decide team size and phasing against the T + 100 days go-live (see timeline check).
3. Confirm KPPP API, CDRMS API, gateway, e-Sign and Kaveri positions during the integration study.
4. Share the client Word export: `BPA_Estimation_Summary_FeatureWise_Client.docx`.
