# Claim Management System (KPID / SPLOCA) — Module List

Source: `SoW_CLAIM_Detailed.md` (v1.7)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Access Control, Person–Post–Role & Forensic Audit | Shared | Person, Post, Role mapping, official identity, OTP, 2FA, OOK access, document rights, forensic audit — **shared programme IAM** | Explicit in SOW |
| 02 | FE Master Import (from existing application) | Business | Import FE details, Directors/Promoters and Investment Schemes; refresh; no FE dossier | Explicit in SOW |
| 03 | Asset Attachment & Recovered Funds | Business | Attached-asset register, title/e-Khata, valuation e-format summary, auction tracking, recovered funds | Explicit in SOW |
| 04 | Depositor Master & Identity Verification | Business | Unique depositor profile, OCR, KYC, address/tally, mismatch, penny-drop, Aadhaar/PAN, special situations | Explicit in SOW |
| 05 | Investment Portfolio Management | Business | Investment capture, interest/outstanding, maturity flags, categorisation, bank returns, excess payment | Explicit in SOW |
| 06 | Claim Notification & Intake | Business | Claim window, in-KA staff-mediated intake, constrained OOK submit, mandatory document pack | Explicit in SOW |
| 07 | Claim Verification, Evaluation & Approval | Business | Officer checklist, additional docs, agentic assists, verification report, CA decision | Explicit in SOW |
| 08 | Settlement, Payment & Closure | Business | Net payable, NEFT/RTGS batch, payment status, closure, payment forensic audit | Explicit in SOW |
| 09 | Operational Reports, Lists & Special Court Outputs | Business | Equitable distribution, Special Court filing, lists, dashboards, structured reports, mapping reports | Explicit in SOW |

---

## Module Details

### 01. Access Control, Person–Post–Role & Forensic Audit

- **Type:** Shared
- **Slug:** `access-control-person-post-role`
- **Summary:** Programme-wide Person–Post–Role identity, official email, OTP before activation, 2FA, joiner–mover–leaver, constrained OOK access, claim-pack document rights and forensic/login audit. **Consumed by Legal Management and GIS field valuation.**
- **Source:** Explicit in SOW §6 Module 01; website review 12-08-2026.
- **In Scope:** F01-001 … F01-010 — Person master; Post / Role-to-Post / Post-to-Person; RBAC menus and need-to-know; official staff identity; OTP before activation; staff 2FA; joiner–mover–leaver with no credential sharing; constrained OOK claimant access; claim-pack document rights; forensic and login/security audit.
- **Out of Scope:** Second user directory inside Legal or Valuation; citizen mass portal accounts for in-KA claimants; SSO/AD unless later ordered.
- **Key Actors:** Administrator, Officer, Competent Authority, auditor; OOK claimant (constrained path only).
- **Dependencies:** None (foundational for the programme).
- **Notes:** Access model is **Person → Post → Role**. Legal and Valuation SOWs must not rebuild this module.

### 02. FE Master Import (from existing application)

- **Type:** Business
- **Slug:** `fe-master-import`
- **Summary:** Import and refresh FE identity, Directors/Promoters and Investment Schemes from the existing FE application; no FE dossier rebuild.
- **Source:** Explicit in SOW §6 Module 02; BPF Module 1 remainder stays in existing app.
- **In Scope:** F02-001 … F02-004.
- **Out of Scope:** FIR, court notifications, company banks, case status, seized corpus, unique FE code generation, FE Management screens.
- **Key Actors:** Officer, Administrator.
- **Dependencies:** 01 Access; existing FE application.
- **Notes:** Read-only references used by Modules 03–09.

### 03. Asset Attachment & Recovered Funds

- **Type:** Business
- **Slug:** `asset-attachment-recovered-funds`
- **Summary:** Claim-side attached-asset register, title/e-Khata/dues, valuation e-format summary, auction tracking and recovered amount for settlement.
- **Source:** Explicit in SOW §6 Module 03; BPF Module 2.
- **In Scope:** F03-001 … F03-006. Consume accepted GIS valuation pack / auction-display photos from Valuation F07-007 when linked.
- **Out of Scope:** GIS field valuation (eValueI/eValueM); 3(2) field capture; valuer Android; CA valuation Accept (those are EVAL).
- **Key Actors:** Officer, settlement Officer, Competent Authority.
- **Dependencies:** 01 Access; 02 FE import; Valuation SOW for field valuation outputs.
- **Notes:** Auction **sale execution and recovered funds** live here; Valuation only selects display photos and releases the pack.

### 04. Depositor Master & Identity Verification

- **Type:** Business
- **Slug:** `depositor-master-identity-verification`
- **Summary:** Unique cross-FE depositor profile, OCR, KYC, address and ID tally, mismatch queries, penny-drop, verified Aadhaar/PAN, special situations, document history.
- **Source:** Explicit in SOW §6 Module 04; BPF Module 3; proceedings items 2–5 (claim identity).
- **In Scope:** F04-001 … F04-010.
- **Out of Scope:** Mass public claimant portal for in-KA; treating unverified Aadhaar as proof.
- **Key Actors:** Officer, assisting staff, auditor; OOK claimant (own pack only).
- **Dependencies:** 01 Access; 02 FE import.
- **Notes:** Four matching parameters are Authority-confirmed, not named in source.

### 05. Investment Portfolio Management

- **Type:** Business
- **Slug:** `investment-portfolio-management`
- **Summary:** Capture investments, auto-calculate interest and outstanding, maturity/violation flags, depositor/colluder/accused categorisation, bank-return analysis, excess payment.
- **Source:** Explicit in SOW §6 Module 05; BPF Module 4.
- **In Scope:** F05-001 … F05-008. FIR/seized lookup via existing FE app only.
- **Out of Scope:** Local FE dossier; police investigation process.
- **Key Actors:** Officer, bank officer (external reply).
- **Dependencies:** 01 Access; 02 FE/schemes; 04 Depositor.
- **Notes:** Agentic assists are rule-based, not generative.

### 06. Claim Notification & Intake

- **Type:** Business
- **Slug:** `claim-notification-intake`
- **Summary:** Publish claim windows; staff-mediated in-KA intake from originals; constrained OOK online submit; mandatory full document pack at Submit.
- **Source:** Explicit in SOW §6 Module 06; BPF 3A/3B.
- **In Scope:** F06-001 … F06-005. Submit blocked until identity, investment, bank, affidavit, statement of investment, and nominee/heir (if applicable) are present.
- **Out of Scope:** Rebuild of sploca.org PDF portal; in-KA self-service filing.
- **Key Actors:** Officer, Administrator, OOK claimant.
- **Dependencies:** 01 Access (including OOK); 02 FE/schemes; 04 Depositor; 05 Investment.
- **Notes:** Channel split is statutory (BSA 2023 originals for in-KA).

### 07. Claim Verification, Evaluation & Approval

- **Type:** Business
- **Slug:** `claim-verification-evaluation-approval`
- **Summary:** Officer verification checklist, additional-document loop, non-generative agentic assists, verification report, CA approval decisions.
- **Source:** Explicit in SOW §6 Module 07; BPF 3C and Claim Approval.
- **In Scope:** F07-001 … F07-005.
- **Out of Scope:** Generative AI drafting; Legal CMS petitions.
- **Key Actors:** Officer, Competent Authority.
- **Dependencies:** 01 Access; 06 Intake; 04–05 identity and portfolio.
- **Notes:** Human confirmation required on every assist.

### 08. Settlement, Payment & Closure

- **Type:** Business
- **Slug:** `settlement-payment-closure`
- **Summary:** Settlement fund and net payable, NEFT/RTGS batches, payment reference/status, closure and balance update, payment forensic audit.
- **Source:** Explicit in SOW §6 Module 08; BPF 4A/4B.
- **In Scope:** F08-001 … F08-005. Recovered amount must match Module 03 totals.
- **Out of Scope:** Bank core payment gateway product; valuer billing (EVAL Module 08).
- **Key Actors:** Officer, Competent Authority, auditor.
- **Dependencies:** 01 Access; 03 Recovered funds; 07 Approved claims.
- **Notes:** Failed/reversed payment cannot close the claim as settled.

### 09. Operational Reports, Lists & Special Court Outputs

- **Type:** Business
- **Slug:** `operational-reports-lists-special-court`
- **Summary:** Equitable distribution and Special Court filing outputs, parameterised lists, dashboards, structured operational reports, Role/Post mapping reports, legacy/document-software hooks.
- **Source:** Explicit in SOW §6 Module 09.
- **In Scope:** F09-001 … F09-007.
- **Out of Scope:** Vakalat/Caveat and legal drafts (Legal SOW); publishing PDFs on a public home page as the reporting method.
- **Key Actors:** Officer, Competent Authority, Administrator, auditor.
- **Dependencies:** 01 Access; 02–08 data.
- **Notes:** Reports from structured records, not website PDFs.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Document handling & workflow | Embedded in claim processes (not a separate DMS/BPM) |
| Notifications (OTP, bank-officer email) | Embedded in Modules 01, 05; no standalone Notification Service |
| Audit logging | Module 01 F01-010 and Module 08 F08-005; NFR elsewhere |
| API / Integration Hub | Integrations listed in SOW §10; not a standalone module |
| FE Management dossier | Existing application; Module 02 import only |
| Legal Management | Separate SOW (`Projects/Fraud/LegalManagement`) |
| GIS field valuation | Separate SOW (`Projects/Fraud/Valuation`) |
| Market intelligence / investigation | Out of scope |
| Generative AI | Prohibited |
| Hardware / hosting AMC / scanning bureau | Out of scope unless separately ordered |

---

## Assumptions

1. Module `{NN}` and feature `F{NN}-{SEQ}` match `SoW_CLAIM_Detailed.md` and must not be renumbered at feature generation.
2. This Module 01 is the **shared user-management component** for Legal and Valuation.
3. Document management and workflow remain embedded.
4. Four depositor-match parameters remain Authority-confirmed.
5. No hours in this step.

---

## Risks

1. Existing FE application interface quality affects Module 02 and F05-007 lookups.
2. Valuation pack handoff (EVAL F07-007) must stay aligned with Module 03 recovered-fund figures.
3. OOK vs in-KA channel rules, if relaxed by the Authority, change Module 06 scope.
4. Unverified Aadhaar misuse would break F04-009 acceptance.
