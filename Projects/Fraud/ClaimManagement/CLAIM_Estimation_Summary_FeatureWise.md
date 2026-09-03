# CLAIM — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 4,533 hours · **Go-live:** 4,533 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Access Control, Person–Post–Role & Forensic Audit | Shared | 10 | 753 | 16.6% |
| 02 | FE Master Import (from existing application) | Business | 4 | 361 | 8.0% |
| 03 | Asset Attachment & Recovered Funds | Business | 6 | 372 | 8.2% |
| 04 | Depositor Master & Identity Verification | Business | 10 | 739 | 16.3% |
| 05 | Investment Portfolio Management | Business | 8 | 586 | 12.9% |
| 06 | Claim Notification & Intake | Business | 5 | 384 | 8.5% |
| 07 | Claim Verification, Evaluation & Approval | Business | 5 | 465 | 10.3% |
| 08 | Settlement, Payment & Closure | Business | 5 | 371 | 8.2% |
| 09 | Operational Reports, Lists & Special Court Outputs | Business | 7 | 502 | 11.1% |
| | **Total** | | **60** | **4,533** | **100%** |

## 01 — Access Control, Person–Post–Role & Forensic Audit (753 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Person master | 67 | Unique Person; later claim actions stored against Person, not a shared login |
| F01-002 | Post, Role-to-Post and Post-to-Person mapping | 100 | Post catalogue; Role-to-Post; Post-to-Person with effective dates and history |
| F01-003 | RBAC menus and need-to-know visibility | 83 | Menus and records follow current Post/Roles; denied access is audited |
| F01-004 | Official staff identity | 60 | Official or administered email only; personal consumer email refused as primary identity |
| F01-005 | OTP before account activation | 71 | Email and mobile OTP must succeed before Active; OTP after success is not acceptable |
| F01-006 | Two-Factor Authentication (staff) | 92 | Staff login requires second factor; OOK claimants are not enrolled in staff 2FA |
| F01-007 | Joiner–mover–leaver; no credential sharing | 69 | Leaver deactivated; joiner gets new Person and credentials; no copy of previous login |
| F01-008 | Constrained OOK claimant access | 61 | OOK path only, open window, own pack; in-KA claimants get no self-service account |
| F01-009 | Claim-pack document rights | 60 | View vs download by Post; who viewed/downloaded which document is recorded |
| F01-010 | Forensic and login/security audit | 90 | Register of who/what/when/before-after/channel including login, 2FA, mapping and claim actions |

## 02 — FE Master Import (from existing application) (361 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Import FE details | 100 | Import unique ID, name and aliases as read-only; no Create FE dossier |
| F02-002 | Import Directors and Promoters | 81 | Import FE people references for accused/colluder lists; no re-typing the FE people master |
| F02-003 | Import Investment Schemes | 79 | Schemes selectable on notification, investment and intake; no free-text scheme names |
| F02-004 | Refresh imported FE reference data | 101 | Refresh FE, directors, promoters and schemes without duplicate FE identities |

## 03 — Asset Attachment & Recovered Funds (372 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Attached asset register | 63 | Claim-side asset registration against imported FE; search by FE or identification |
| F03-002 | Title, e-Khata and dues tracking | 60 | Title-transfer, e-Khata progress, dues obtained/paid; auction complete blocked if path not recorded |
| F03-003 | Attachment order and valuation e-format | 71 | Upload attachment order; enter valuation e-format summary; consume EVAL pack when linked — no GIS capture |
| F03-004 | Auction tracking and recovered funds | 78 | Auction milestones including e-Governance points; recovered amount must match settlement fund |
| F03-005 | Asset documents, status and history | 50 | Uploads, status changes, replayable who/when/previous/new status history |
| F03-006 | Depositor and FE asset association | 50 | FE link mandatory; depositor link where applicable; used later in reports and claim checks |

## 04 — Depositor Master & Identity Verification (739 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | OCR, translation and format conversion | 104 | OCR/translate/convert working copies; original scan/JPEG/PDF unchanged |
| F04-002 | Unique depositor profile (four-parameter match) | 77 | Four Authority-defined parameters; continue on existing profile across FEs or confirm new unique profile |
| F04-003 | KYC capture | 65 | Personal, Aadhaar, PAN, contacts, deposit/refund banks, nominee and legal-heir details |
| F04-004 | Address and pin-code verification | 58 | Pin code tallied to actual areas; discrepancy and RPAD re-verification recorded |
| F04-005 | Name and address tally across ID sources | 63 | Side-by-side Aadhaar, PAN, EPIC, passbook and claim form; match or differ before proceeding |
| F04-006 | Auto mismatch query generation | 71 | Query created on disagreement; identity not clean until closed per policy |
| F04-007 | Penny-drop verification recording | 79 | Record contracted-bank penny-drop against refund account; visible on depositor and payment trail |
| F04-008 | Special depositor and claim situations | 88 | Ineligible, deceased, legal heir, joint, third-party, lost receipt, cash investment — flagged, papers, routed to resolution |
| F04-009 | Aadhaar and PAN verification | 84 | Unverified Aadhaar is not identity proof; unverified capture remains visible as unverified only |
| F04-010 | Depositor documents, status and history | 50 | Structured fields and status history on the profile; not a PDF published on a home page |

## 05 — Investment Portfolio Management (586 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Investment record capture | 59 | FE and scheme from import only; customer ID, bond/MOU, receipt, dates, amounts, promised interest, amount received |
| F05-002 | Interest and outstanding auto-calculation | 66 | Interest received, promised vs paid, outstanding; interest paid as principal repaid where rule applies; stored for audit |
| F05-003 | Maturity and violation analytics | 67 | Flags investments whose maturity date is violated; used in verification or categorisation |
| F05-004 | Depositor / colluder / accused categorisation | 71 | Rule-based proposal using imported Director/Promoter names; Officer accepts or overrides with remarks |
| F05-005 | Bank returns analysis and claim cross-check | 88 | Analyse scanned bank-return data after transfer; matches/exceptions recorded on claim or investment |
| F05-006 | Bank-officer verification requests | 60 | Email request unless bank already submitted data; reply or timeout recorded on the same record |
| F05-007 | Cross-FE comparison (FIR / seized-FE via existing app) | 104 | Compare local investments/claims/assets; FIR/seized lookup to existing FE app; no local FE dossier |
| F05-008 | Excess payment analysis | 71 | Flag excesses on bank and cash transactions; Officer records outcome; analysis and decision audited |

## 06 — Claim Notification & Intake (384 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Claim notification and window | 63 | Publish notification with imported FE/schemes and period; close window refuses intake |
| F06-002 | Staff-mediated claim intake (in-Karnataka) | 88 | Counter originals; Submit blocked unless full mandatory pack and fields; claimant does not self-file |
| F06-003 | Constrained online claim submission (OOK) | 82 | OOK submit during open window; same mandatory pack as F06-002; same block-and-list-gaps |
| F06-004 | Claim pack validation and document uploads | 78 | Shared Submit rule for F06-002 and F06-003; incomplete pack never stored as submitted; F07-002 is after first Submit |
| F06-005 | Existing limited online access outcomes | 73 | Retrieve existing OOK/limited-access outcomes; do not send claimant to a new mass public portal |

## 07 — Claim Verification, Evaluation & Approval (465 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Officer verification checklist | 74 | Identity, investment, scheme, customer ID, deposits, uploads, bank, previous returns, existing claims, eligibility |
| F07-002 | Additional document request loop | 71 | Request after first Submit; prior checklist ticks retained when evaluation resumes |
| F07-003 | Agentic verification assists (non-generative) | 74 | Rule-based highlights only; Officer must confirm or reject; no generative compose; assists audited |
| F07-004 | Verification report for Competent Authority | 119 | Report generated from checklist and remarks; CA opens that report, not a blank claim |
| F07-005 | Claim approval decisions | 127 | Approved / Partially Approved / Rejected / Pending Clarification with remarks; Pending returns to Officer |

## 08 — Settlement, Payment & Closure (371 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Settlement fund and net payable calculation | 78 | Recovered amount from Module 03 must match; eligible, previous returns/settlements, net payable |
| F08-002 | Payment batch generation (NEFT / RTGS) | 82 | Select approved claims with net payable; NEFT or RTGS; batch ID; confirm list before transfer |
| F08-003 | Payment reference and status recording | 79 | Payment reference, transaction number, status pending/success/failed/reversed per claim in the batch |
| F08-004 | Claim closure and balance update | 65 | Close only on success as policy requires; failed/reversed leaves claim open; investment balance and payment history updated |
| F08-005 | Payment forensic audit | 67 | Who generated batch, who recorded bank references, each status change and closure — Person, Post, timestamp, channel |

## 09 — Operational Reports, Lists & Special Court Outputs (502 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Equitable distribution statement | 72 | From approved input format (recovered funds, approved claims); output for Special Court filing |
| F09-002 | Special Court filing report | 70 | Same class of approved inputs; on-screen review and filing copy; no re-key of settlement figures |
| F09-003 | Parameterised operational lists | 63 | Claimant, accused, colluder, address and vendor lists; Post-restricted; Vakalat/Caveat not in this SOW |
| F09-004 | Claim decision dashboards | 81 | Filters by imported FE, scheme, window or status; counts and exceptions; menus follow Module 01 |
| F09-005 | Legacy web app and document-software hooks | 86 | Send/retrieve agreed claim outcomes to legacy/web app; Idea/Adobe working copies; no second unofficial claim ledger |
| F09-006 | Structured operational reports | 78 | Depositor, asset, claim, verification, status, historical, user/activity from structured records — not homepage PDFs |
| F09-007 | Role / Post mapping reports | 52 | Current and history who was mapped, effective dates, who changed mapping; for access audit, not granting access |

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
