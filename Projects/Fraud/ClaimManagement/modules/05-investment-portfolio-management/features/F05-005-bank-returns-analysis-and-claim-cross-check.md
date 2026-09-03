# F05-005 — Bank returns analysis and claim cross-check

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-005 |
| **Feature Name** | Bank returns analysis and claim cross-check |
| **Module** | 05 — Investment Portfolio Management |

### Description
The Officer uploads or opens scanned bank-return data after transfer, runs analysis, and compares it with claim and investment records. The Officer sees matches and exceptions and records the cross-check outcome on the claim or investment.

### Business Objective
Cross-check bank-return data with claims and investments and record matches and exceptions.

### Actors
Officer.

### User Journey
1. Who creates: Officer
2. How they create: Officer uploads or opens scanned bank-return data after transfer.
3. How they edit: Officer runs analysis and compares it with claim and investment records.
4. How they send for approval: Officer sees matches and exceptions and records the cross-check outcome on the claim or investment. Upload/open → analyse → review matches/exceptions → record outcome.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload/open scanned bank-return data.
- Run analysis against claim and investment records.
- Show matches and exceptions.
- Record cross-check outcome on the claim or investment.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Bank-return upload and analysis workbench | Very High |
| Match and exception results | Complex |
| Bank returns analysis and claim cross-check history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Bank-return analysis operations | Very High |
| Update bank returns analysis and claim cross-check | Medium |
| Search bank returns analysis and claim cross-check | Medium |
| Read bank returns analysis and claim cross-check history | Easy |

### Inputs
Bank-return scans or structured return data, claim/investment records.

### Outputs
Match/exception results; recorded outcome on claim or investment.

### Business Rules
- Analysis is rule-based; no generative interpretation of bank scans.
- OCR of scans may reuse F04-001 working copies; originals stay unaltered.

### Validations
- Outcome cannot be saved without viewing the result set.

### Calculations
Match/exception identification against portfolio and claims.

### Workflow
Upload/open → analyse → review matches/exceptions → record outcome.

### Search Requirements
FE, depositor, claim, exception flag, return date.

### Documents
Bank-return scans (originals retained).

### Reports
Exception list from bank-return cross-check.

### Notifications
None.

### Security
Bank-return data is need-to-know. Outcomes audited.

### Integrations
None beyond optional reuse of OCR working copies.

### Dependencies
F05-001; Module 06 claims when present; F04-001 if scans need OCR.

### Assumptions
- Authority supplies bank returns for modules built in this application.

### Risks
- Unrecorded exceptions would weaken verification and excess-payment analysis.

### Non Functional Requirements
Analysis results are structured records, not a homepage PDF.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Bank-return upload and analysis workbench | UI | Very High | 16 |
| Match and exception results | UI | Complex | 12 |
| Bank returns analysis and claim cross-check history | UI | Medium | 6 |
| Bank-return analysis operations | API | Very High | 16 |
| Update bank returns analysis and claim cross-check | API | Medium | 6 |
| Search bank returns analysis and claim cross-check | API | Medium | 6 |
| Read bank returns analysis and claim cross-check history | API | Easy | 4 |
| Cross-check persistence | DB | Complex | 6 |
| Bank returns analysis and claim cross-check feature tests | Testing | Very High | 12 |
| Bank returns analysis and claim cross-check implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
