# CLT — Estimation Summary (Internal)

**Project:** Online Computer Literacy Test (CLT) and Digital Certification System  
**Client:** Karnataka State Electronics Development Corporation Limited (KEONICS)  
**Project code:** CLT  
**As of:** 2026-10-14  
**Source:** `SoW_CLT_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Value |
|--------|------:|
| Modules | 18 |
| Features | 90 |
| **Recommended go-live hours** | **5136** |
| Conditional hours | 50 |
| **All-in hours** | **5186** |
| All-in person-days (8 h) | 648 |

Conditional: F06-005 Field Test & Difficulty Calibration (50 h).

## Per-module hours

| # | Module | Type | Features | Hours | % of all-in |
|---|--------|------|---------:|------:|------------:|
| 01 | Access Control & Staff User Management | Shared | 3 | 316 | 6.1% |
| 02 | Examination Configuration & Masters | Business | 6 | 360 | 6.9% |
| 03 | CLT Web Portal & Mobile Application | Business | 4 | 230 | 4.4% |
| 04 | Candidate Registration & eKYC | Business | 6 | 423 | 8.2% |
| 05 | Online Test Booking, Fees & Hall Ticket | Business | 6 | 361 | 7.0% |
| 06 | Question Bank & Content Authoring Tool | Business | 8 | 470 | 9.1% |
| 07 | Question Paper Generation & Mock Test | Business | 4 | 176 | 3.4% |
| 08 | Test Centre Operations & Candidate Validation | Business | 6 | 320 | 6.2% |
| 09 | Online Examination Engine | Business | 7 | 474 | 9.1% |
| 10 | Screen Proctoring & Malpractice Management | Business | 6 | 391 | 7.5% |
| 11 | Evaluation, Results & Digital Certification | Business | 6 | 253 | 4.9% |
| 12 | Central Monitoring Centre & Examination Monitoring Unit | Business | 4 | 219 | 4.2% |
| 13 | MIS, Dashboards & Reports | Business | 4 | 181 | 3.5% |
| 14 | Notifications & Helpdesk | Shared | 4 | 192 | 3.7% |
| 15 | Integration Hub | Technical | 6 | 393 | 7.6% |
| 16 | Security, Audit & Compliance | Technical | 4 | 185 | 3.6% |
| 17 | Platform, Performance & Operations | Technical | 4 | 159 | 3.1% |
| 18 | Legacy CLT Data Porting | Technical | 2 | 83 | 1.6% |

## Hours by module type

| Type | Hours | % |
|------|------:|---:|
| Business | 3858 | 74.4% |
| Shared | 508 | 9.8% |
| Technical | 820 | 15.8% |

## Hours by estimation area

| Area | Hours | % |
|------|------:|---:|
| UI | 1572 | 30.3% |
| API | 2150 | 41.5% |
| Database | 255 | 4.9% |
| Integration | 296 | 5.7% |
| Testing | 724 | 14.0% |
| Documentation | 189 | 3.6% |

## Top 10 features by effort

| Feature | Name | Hours |
|---------|------|------:|
| F06-002 | Bilingual Rich-Content Question Authoring | 119 |
| F01-001 | Staff Authentication & Session Security | 107 |
| F09-007 | Secure Exam Client & Device Compatibility | 107 |
| F01-002 | Staff User, Role & Centre Mapping | 106 |
| F01-003 | Permission Matrix & Data Scope | 103 |
| F03-004 | Candidate Mobile Application | 98 |
| F04-003 | Prospective Candidate & Non-KGID Registration with eKYC | 92 |
| F04-001 | Candidate OTP Login & Account | 90 |
| F04-002 | Government Employee Registration with KGID & HRMS Validation | 90 |
| F09-002 | Rich MCQ Delivery & Navigation | 90 |

## Timeline check against the RFP

The RFP expects FRS at T + 1 month, design at T + 1.5 months, development and UAT deployment at T + 2 months, UAT at T + 2.5 months and go-live with Safe-to-Host at T + 3 months. Allowing build to start once the FRS is drafted gives about **7 build weeks**. Go-live effort of **5136 hours** over 7 weeks at 40 hours per week needs roughly **18 full-time build-and-test engineers**, plus project management, design, DevOps and security. This is a high-risk timeline. Options: a larger team with parallel streams (candidate journey, question bank, exam engine and proctoring, integrations), reuse of an existing exam platform base, or agreement with KEONICS on a phased go-live (registration, booking and question bank first; full proctoring analytics, query tool and calibration after the first sessions).

## Video recording sizing (go-live scope)

Screen plus webcam recording at about 350 MB per candidate per 90-minute session gives about **700 GB per full session** of 2,000 candidates. With 90-day retention and the expected session load, plan for several TB of SDC object storage and at least 50 Mbps per centre and 200 Mbps into SDC at peak. Storage and bandwidth are SDC provisions; the capacity plan (F17-002) fixes the figures before go-live.

## Not included in feature hours

- Project management, FRS and design documentation phase
- Question content creation by SMEs (at least 2,000 questions at launch, 5% growth per year) and Technical Committee costs
- Need-based offsite helpdesk staffing and dedicated numbers
- Safe-to-Host audit fee (annual, CERT-In empanelled auditor) and SSL certificates
- Training, user manuals beyond technical documentation, and how-to videos
- Warranty (12 months) and comprehensive AMC (3 years)
- Exit management and knowledge transfer services
- SDC hosting, storage and bandwidth; payment gateway, SMS, Aadhaar and e-Sign transaction charges

## Open assumptions / risks

1. HRMS provides look-up by KGID and accepts result push; otherwise a file-based exchange is needed.
2. Aadhaar authentication and eKYC through the state AUA / KUA via CeG; onboarding is outside our control.
3. CeG HSM partition and client libraries are available for key management and signing.
4. Centres permit installation of the secure exam client on Windows, Linux or macOS terminals with webcams.
5. Kannada typing layout (Nudi / KGP or InScript) is fixed in the FRS.
6. Field test and calibration (F06-005) is conditional and outside go-live hours.
7. Legacy CLT data is provided in templates; cleansing is KEONICS' responsibility.
8. The RFP contract period wording varies (3 years 3 months vs 2 + 2 years); confirm during pre-bid.

## Suggested next actions

1. Review modules, features and hours with the delivery lead.
2. Decide team size and phasing against the T + 3 months go-live (see timeline check).
3. Raise pre-bid queries on HRMS APIs, AUA / KUA, HSM, storage for video recordings and typing layout.
4. Share the client Word export: `CLT_Estimation_Summary_FeatureWise_Client.docx`.
