# CLAIM — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 2,989 hours · **Go-live:** 2,989 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Access Control, Person–Post–Role & Forensic Audit | Shared | 10 | 503 | 16.8% |
| 02 | FE Master Import (from existing application) | Business | 4 | 267 | 8.9% |
| 03 | Asset Attachment & Recovered Funds | Business | 6 | 234 | 7.8% |
| 04 | Depositor Master & Identity Verification | Business | 10 | 495 | 16.6% |
| 05 | Investment Portfolio Management | Business | 8 | 386 | 12.9% |
| 06 | Claim Notification & Intake | Business | 5 | 268 | 9.0% |
| 07 | Claim Verification, Evaluation & Approval | Business | 5 | 233 | 7.8% |
| 08 | Settlement, Payment & Closure | Business | 5 | 255 | 8.5% |
| 09 | Operational Reports, Lists & Special Court Outputs | Business | 7 | 348 | 11.6% |
| | **Total** | | **60** | **2,989** | **100%** |

## 01 — Access Control, Person–Post–Role & Forensic Audit (503 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Person master | 45 | Unique Person; later claim actions stored against Person, not a shared login |
| F01-002 | Post, Role-to-Post and Post-to-Person mapping | 78 | Post catalogue; Role-to-Post; Post-to-Person with effective dates and history |
| F01-003 | RBAC menus and need-to-know visibility | 61 | Menus and records follow current Post/Roles; denied access is audited |
| F01-004 | Official staff identity | 32 | Official or administered email only; personal consumer email refused as primary identity |
| F01-005 | OTP before account activation | 43 | Email and mobile OTP must succeed before Active; OTP after success is not acceptable |
| F01-006 | Two-Factor Authentication (staff) | 70 | Staff login requires second factor; OOK claimants are not enrolled in staff 2FA |
| F01-007 | Joiner–mover–leaver; no credential sharing | 41 | Leaver deactivated; joiner gets new Person and credentials; no copy of previous login |
| F01-008 | Constrained OOK claimant access | 39 | OOK path only, open window, own pack; in-KA claimants get no self-service account |
| F01-009 | Claim-pack document rights | 32 | View vs download by Post; who viewed/downloaded which document is recorded |
| F01-010 | Forensic and login/security audit | 62 | Register of who/what/when/before-after/channel including login, 2FA, mapping and claim actions |

## 02 — FE Master Import (from existing application) (267 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Import FE details | 78 | Import unique ID, name and aliases as read-only; no Create FE dossier |
| F02-002 | Import Directors and Promoters | 59 | Import FE people references for accused/colluder lists; no re-typing the FE people master |
| F02-003 | Import Investment Schemes | 57 | Schemes selectable on notification, investment and intake; no free-text scheme names |
| F02-004 | Refresh imported FE reference data | 73 | Refresh FE, directors, promoters and schemes without duplicate FE identities |

## 03 — Asset Attachment & Recovered Funds (234 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Attached asset register | 41 | Claim-side asset registration against imported FE; search by FE or identification |
| F03-002 | Title, e-Khata and dues tracking | 32 | Title-transfer, e-Khata progress, dues obtained/paid; auction complete blocked if path not recorded |
| F03-003 | Attachment order and valuation e-format | 43 | Upload attachment order; enter valuation e-format summary; consume EVAL pack when linked — no GIS capture |
| F03-004 | Auction tracking and recovered funds | 56 | Auction milestones including e-Governance points; recovered amount must match settlement fund |
| F03-005 | Asset documents, status and history | 34 | Uploads, status changes, replayable who/when/previous/new status history |
| F03-006 | Depositor and FE asset association | 28 | FE link mandatory; depositor link where applicable; used later in reports and claim checks |

## 04 — Depositor Master & Identity Verification (495 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | OCR, translation and format conversion | 76 | OCR/translate/convert working copies; original scan/JPEG/PDF unchanged |
| F04-002 | Unique depositor profile (four-parameter match) | 55 | Four Authority-defined parameters; continue on existing profile across FEs or confirm new unique profile |
| F04-003 | KYC capture | 37 | Personal, Aadhaar, PAN, contacts, deposit/refund banks, nominee and legal-heir details |
| F04-004 | Address and pin-code verification | 30 | Pin code tallied to actual areas; discrepancy and RPAD re-verification recorded |
| F04-005 | Name and address tally across ID sources | 35 | Side-by-side Aadhaar, PAN, EPIC, passbook and claim form; match or differ before proceeding |
| F04-006 | Auto mismatch query generation | 49 | Query created on disagreement; identity not clean until closed per policy |
| F04-007 | Penny-drop verification recording | 51 | Record contracted-bank penny-drop against refund account; visible on depositor and payment trail |
| F04-008 | Special depositor and claim situations | 66 | Ineligible, deceased, legal heir, joint, third-party, lost receipt, cash investment — flagged, papers, routed to resolution |
| F04-009 | Aadhaar and PAN verification | 62 | Unverified Aadhaar is not identity proof; unverified capture remains visible as unverified only |
| F04-010 | Depositor documents, status and history | 34 | Structured fields and status history on the profile; not a PDF published on a home page |

## 05 — Investment Portfolio Management (386 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Investment record capture | 43 | FE and scheme from import only; customer ID, bond/MOU, receipt, dates, amounts, promised interest, amount received |
| F05-002 | Interest and outstanding auto-calculation | 44 | Interest received, promised vs paid, outstanding; interest paid as principal repaid where rule applies; stored for audit |
| F05-003 | Maturity and violation analytics | 39 | Flags investments whose maturity date is violated; used in verification or categorisation |
| F05-004 | Depositor / colluder / accused categorisation | 43 | Rule-based proposal using imported Director/Promoter names; Officer accepts or overrides with remarks |
| F05-005 | Bank returns analysis and claim cross-check | 66 | Analyse scanned bank-return data after transfer; matches/exceptions recorded on claim or investment |
| F05-006 | Bank-officer verification requests | 32 | Email request unless bank already submitted data; reply or timeout recorded on the same record |
| F05-007 | Cross-FE comparison (FIR / seized-FE via existing app) | 76 | Compare local investments/claims/assets; FIR/seized lookup to existing FE app; no local FE dossier |
| F05-008 | Excess payment analysis | 43 | Flag excesses on bank and cash transactions; Officer records outcome; analysis and decision audited |

## 06 — Claim Notification & Intake (268 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Claim notification and window | 41 | Publish notification with imported FE/schemes and period; close window refuses intake |
| F06-002 | Staff-mediated claim intake (in-Karnataka) | 66 | Counter originals; Submit blocked unless full mandatory pack and fields; claimant does not self-file |
| F06-003 | Constrained online claim submission (OOK) | 60 | OOK submit during open window; same mandatory pack as F06-002; same block-and-list-gaps |
| F06-004 | Claim pack validation and document uploads | 56 | Shared Submit rule for F06-002 and F06-003; incomplete pack never stored as submitted; F07-002 is after first Submit |
| F06-005 | Existing limited online access outcomes | 45 | Retrieve existing OOK/limited-access outcomes; do not send claimant to a new mass public portal |

## 07 — Claim Verification, Evaluation & Approval (233 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Officer verification checklist | 46 | Identity, investment, scheme, customer ID, deposits, uploads, bank, previous returns, existing claims, eligibility |
| F07-002 | Additional document request loop | 49 | Request after first Submit; prior checklist ticks retained when evaluation resumes |
| F07-003 | Agentic verification assists (non-generative) | 52 | Rule-based highlights only; Officer must confirm or reject; no generative compose; assists audited |
| F07-004 | Verification report for Competent Authority | 39 | Report generated from checklist and remarks; CA opens that report, not a blank claim |
| F07-005 | Claim approval decisions | 47 | Approved / Partially Approved / Rejected / Pending Clarification with remarks; Pending returns to Officer |

## 08 — Settlement, Payment & Closure (255 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Settlement fund and net payable calculation | 56 | Recovered amount from Module 03 must match; eligible, previous returns/settlements, net payable |
| F08-002 | Payment batch generation (NEFT / RTGS) | 60 | Select approved claims with net payable; NEFT or RTGS; batch ID; confirm list before transfer |
| F08-003 | Payment reference and status recording | 57 | Payment reference, transaction number, status pending/success/failed/reversed per claim in the batch |
| F08-004 | Claim closure and balance update | 43 | Close only on success as policy requires; failed/reversed leaves claim open; investment balance and payment history updated |
| F08-005 | Payment forensic audit | 39 | Who generated batch, who recorded bank references, each status change and closure — Person, Post, timestamp, channel |

## 09 — Operational Reports, Lists & Special Court Outputs (348 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Equitable distribution statement | 50 | From approved input format (recovered funds, approved claims); output for Special Court filing |
| F09-002 | Special Court filing report | 48 | Same class of approved inputs; on-screen review and filing copy; no re-key of settlement figures |
| F09-003 | Parameterised operational lists | 41 | Claimant, accused, colluder, address and vendor lists; Post-restricted; Vakalat/Caveat not in this SOW |
| F09-004 | Claim decision dashboards | 53 | Filters by imported FE, scheme, window or status; counts and exceptions; menus follow Module 01 |
| F09-005 | Legacy web app and document-software hooks | 64 | Send/retrieve agreed claim outcomes to legacy/web app; Idea/Adobe working copies; no second unofficial claim ledger |
| F09-006 | Structured operational reports | 56 | Depositor, asset, claim, verification, status, historical, user/activity from structured records — not homepage PDFs |
| F09-007 | Role / Post mapping reports | 36 | Current and history who was mapped, effective dates, who changed mapping; for access audit, not granting access |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Identity and FE import | 01, 02 |
| P2 — Recovery feed | 03 |
| P3 — Depositor, investment, intake | 04, 05, 06 |
| P4 — Verification and settlement | 07, 08 |
| P5 — Reports and Special Court outputs | 09 |

## Exclusions (not in feature hours)

- FE Management dossier rebuild
- Legal Management Application
- GIS field valuation (eValueI / eValueM)
- Generative AI
- Hardware, hosting AMC, scanning bureau
- Market intelligence and police investigation process
