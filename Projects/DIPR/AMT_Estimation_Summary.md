# AMT — Estimation Summary (Internal) — Ultra Detailed

**Project:** Advertisement Monitoring Tool (AMT)  
**Client:** DIPR, Government of Karnataka  
**Source:** SoW_AMT_Detailed.md (tender + Inventech pre-bid)  
**Modules:** 10 · **Features:** 52 · **Artefact line items:** 870  
**Basis:** Estimation Master — ultra-detailed named UI / API / Database / Integration / Testing / Documentation artefacts

## Totals

| Scope | Hours |
|-------|------:|
| Recommended go-live (core) | **4134** |
| Optional / conditional | **330** |
| All-in | **4464** |

## Estimation Master — all-in line-item roll-up

| Area | Hours | % of all-in | Artefact rows |
|------|------:|------------:|--------------:|
| UI | **1352** | 30.3% | 252 |
| API | **1338** | 30.0% | 229 |
| Database | **292** | 6.5% | 112 |
| Integration | **320** | 7.2% | 26 |
| Testing | **956** | 21.4% | 160 |
| Documentation | **206** | 4.6% | 91 |
| **Total** | **4464** | 100% | **870** |

## Per-module totals (with area line items)

| # | Module | Type | Feat | Lines | UI | API | DB | Int | Test | Doc | Total |
|---|--------|------|-----:|------:|---:|----:|---:|----:|-----:|----:|------:|
| 01 | User & Access Management | Shared | 5 | 104 | 126 | 158 | 33 | 24 | 100 | 20 | **461** |
| 02 | Master Data & System Configuration | Business | 5 | 103 | 148 | 138 | 37 | 4 | 74 | 19 | **420** |
| 03 | Campaign Management | Business | 7 | 132 | 232 | 220 | 45 | 0 | 122 | 23 | **642** |
| 04 | Creative Asset Inventory | Business | 5 | 81 | 140 | 114 | 23 | 8 | 72 | 12 | **369** |
| 05 | Proof-of-Display Capture & Verification | Business | 6 | 105 | 198 | 176 | 38 | 16 | 116 | 23 | **567** |
| 06 | Mobile Field Application | Business | 5 | 90 | 122 | 158 | 27 | 76 | 116 | 21 | **520** |
| 07 | Reporting & Analytics | Business | 6 | 79 | 168 | 128 | 30 | 8 | 100 | 24 | **458** |
| 08 | Notifications & Alerts | Shared | 4 | 57 | 76 | 66 | 19 | 48 | 62 | 14 | **285** |
| 09 | Integration Hub | Technical | 4 | 57 | 58 | 86 | 19 | 112 | 80 | 22 | **377** |
| 10 | Platform Security & Compliance Controls | Technical | 5 | 62 | 84 | 94 | 21 | 24 | 114 | 28 | **365** |
| | **Grand total** | | **52** | **870** | **1352** | **1338** | **292** | **320** | **956** | **206** | **4464** |

## Optional / conditional commercial line items

| Feature ID | Name | Hours | Line items | Why optional |
|------------|------|------:|-----------:|--------------|
| F01-003 | Optional SSO integration | 101 | 19 | SSO optional; IdP/protocol TBD |
| F05-005 | Third-party verification provision | 105 | 17 | Third-party PoD vendor/APIs/licenses TBD |
| F08-003 | SMS notification provision | 72 | 14 | SMS gateway credentials TBD |
| F09-003 | Third-party analytics provision | 52 | 11 | Third-party analytics vendor TBD |

## Indicative commercial development line items (Annexure-II style)

| Line item | Hours |
|-----------|------:|
| One-time development — core go-live | 4134 |
| Optional SSO integration (F01-003) | 101 |
| Optional third-party PoD verification (F05-005) | 105 |
| Optional SMS notifications (F08-003) | 72 |
| Optional third-party analytics connector (F09-003) | 52 |
| **All-in development effort** | **4464** |

> Prototype workshops, training & KT, hosting/AMC, and third-party license fees remain outside feature hours.

## Open assumptions / risks

1. DIPR systems list / API sandbox pending.
2. Mobile assumed cross-platform/PWA-capable unless native dual stack mandated.
3. PoD validation rules finalized in Phase 1.
4. Government hosting preferred.
5. KPI dictionary finalized before dashboard freeze.

## Suggested next actions

1. Review ultra-detailed artefact catalogue in `AMT_Estimation_Summary_FeatureWise.md`.
2. Confirm optional commercial lines for the bid.
3. Share `AMT_Estimation_Summary_FeatureWise_Client.docx`.
