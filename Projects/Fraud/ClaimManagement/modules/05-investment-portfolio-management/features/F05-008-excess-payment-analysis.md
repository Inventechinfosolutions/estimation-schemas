# F05-008 — Excess payment analysis

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-008 |
| **Feature Name** | Excess payment analysis |
| **Module** | 05 — Investment Portfolio Management |

### Description
The Officer opens bank and cash transactions for a depositor or FE, runs excess-payment analysis, and reviews flagged excesses. The Officer records the outcome; the system keeps an audit trail of the analysis and the Officer’s decision.

### Business Objective
Flag excess payments on bank and cash transactions and keep analysis plus Officer decision for forensic audit.

### Actors
Officer; auditor.

### User Journey
1. Who creates: Officer
2. How they create: Officer opens bank and cash transactions for a depositor or FE.
3. How they edit: Officer runs excess-payment analysis and reviews flagged excesses.
4. How they send for approval: Officer records the outcome. Open transactions → run analysis → review flags → record outcome.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. The system keeps an audit trail of the analysis and the Officer’s decision (F01-010).
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Run excess-payment analysis on bank and cash transactions.
- Present flagged excesses.
- Record Officer outcome with audit trail.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My excess payment analysis list / queue | Medium |
| Excess-payment analysis screen | Complex |
| Excess payment analysis history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Excess-payment analysis operations | Very High |
| Update excess payment analysis | Medium |
| Search excess payment analysis | Medium |
| Read excess payment analysis history | Easy |

### Inputs
Bank and cash transactions, portfolio/claim payments, Officer decision.

### Outputs
Flagged excesses; recorded outcome; audit trail.

### Business Rules
- Excess-payment events participate in forensic audit.
- Officer decision is required; analysis does not auto-recover money.
- No generative narrative of excess.

### Validations
- Outcome save requires the analysis run identifier.

### Calculations
Excess versus expected returns/settlements per Authority rule.

### Workflow
Open transactions → run analysis → review flags → record outcome.

### Search Requirements
Depositor, FE, excess flag, decision.

### Documents
None required.

### Reports
Excess-payment flag list.

### Notifications
None.

### Security
Analysis and decision are privileged audit events.

### Integrations
None.

### Dependencies
F05-001, F05-002; Module 08 previous settlements when present.

### Assumptions
- Authority defines the excess-payment rule relative to returns and settlements.

### Risks
- Ignoring flags before payment would over-pay claimants.

### Non Functional Requirements
Forensic trail of analysis and decision is retrievable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My excess payment analysis list / queue | UI | Medium | 6 |
| Excess-payment analysis screen | UI | Complex | 12 |
| Excess payment analysis history | UI | Medium | 6 |
| Excess-payment analysis operations | API | Very High | 16 |
| Update excess payment analysis | API | Medium | 6 |
| Search excess payment analysis | API | Medium | 6 |
| Read excess payment analysis history | API | Easy | 4 |
| Analysis and decision audit persistence | DB | Medium | 4 |
| Excess payment analysis feature tests | Testing | Complex | 8 |
| Excess payment analysis implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **71** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
