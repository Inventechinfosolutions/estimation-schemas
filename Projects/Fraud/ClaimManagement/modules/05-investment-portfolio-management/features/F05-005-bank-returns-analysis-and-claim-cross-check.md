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
1. Officer uploads or opens scanned bank-return data after transfer.
2. Officer runs analysis and compares it with claim and investment records.
3. Officer sees matches and exceptions and records the cross-check outcome on the claim or investment.

### Functional Capabilities
- Upload/open scanned bank-return data.
- Run analysis against claim and investment records.
- Show matches and exceptions.
- Record cross-check outcome on the claim or investment.

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
| Bank-return analysis operations | API | Very High | 16 |
| Cross-check persistence | DB | Complex | 6 |
| Bank-return analysis tests | Testing | Very High | 12 |
| Bank-return analysis guide | Documentation | Complex | 4 |
| **Total** | | | **66** |

### Estimation Assumptions
- Uses Estimation Master values only.
- OCR engine hours remain in F04-001; this feature estimates analysis and cross-check.
