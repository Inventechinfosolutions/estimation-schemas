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
1. Officer opens bank and cash transactions for a depositor or FE.
2. Officer runs excess-payment analysis and reviews flagged excesses.
3. Officer records the outcome.
4. The system keeps an audit trail of the analysis and the Officer’s decision (F01-010).

### Functional Capabilities
- Run excess-payment analysis on bank and cash transactions.
- Present flagged excesses.
- Record Officer outcome with audit trail.

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
| Excess-payment analysis screen | UI | Complex | 12 |
| Excess-payment analysis operations | API | Very High | 16 |
| Analysis and decision audit persistence | DB | Medium | 4 |
| Excess-payment analysis tests | Testing | Complex | 8 |
| Excess-payment analysis note | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Payment forensic UI is additionally estimated in F08-005.
