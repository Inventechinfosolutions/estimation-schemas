# F04-007 — Penny-drop verification recording

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-007 |
| **Feature Name** | Penny-drop verification recording |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer records a penny-drop request/result from the contracted bank against the refund account (success/fail, match indicators, timestamp). An auditor later opens the same depositor or payment trail and sees that penny-drop event.

### Business Objective
Record contracted-bank penny-drop against the refund account so payment audit can see it.

### Actors
Officer; auditor; contracted bank (external result).

### User Journey
1. Officer records a penny-drop request against the depositor’s refund account.
2. Result from the contracted bank is recorded: success/fail, match indicators, timestamp.
3. Auditor later opens the same depositor or payment trail and sees that penny-drop event.

### Functional Capabilities
- Record penny-drop request and result against the refund account.
- Store success/fail, match indicators and timestamp.
- Surface the event on depositor and payment forensic trails (F01-010 / F08-005).

### Inputs
Refund account, request reference, bank result, match indicators, timestamp.

### Outputs
Penny-drop event on the depositor and on the payment trail.

### Business Rules
- Penny-drop is against the refund account used for settlement.
- Events participate in the forensic audit trail.

### Validations
- Refund account must exist on KYC (F04-003).
- Result values limited to the agreed success/fail/match set.

### Calculations
None beyond match indicators as supplied by the bank process.

### Workflow
Request → bank result → record. Not a bank-core product.

### Search Requirements
Depositor, refund account, penny-drop status, date.

### Documents
Bank result artefacts if supplied.

### Reports
Penny-drop exception list.

### Notifications
None to claimants required; staff see on-screen result.

### Security
Penny-drop is a privileged recorded event (who, when). Bank account data is need-to-know.

### Integrations
Bank penny-drop process (record verification results).

### Dependencies
F04-003 refund account; F01-010 audit; Module 08 payment trail.

### Assumptions
- Banking arrangements for penny-drop exist; this application records and consumes results rather than operating a payment gateway product.

### Risks
- Paying without a recorded penny-drop where policy requires it would fail payment audit.

### Non Functional Requirements
Penny-drop events are retrievable in forensic audit.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Penny-drop recording screen | UI | Medium | 6 |
| Penny-drop event operations | API | Complex | 8 |
| Penny-drop event persistence | DB | Easy | 2 |
| Contracted-bank penny-drop process | Integration | Complex | 24 |
| Penny-drop recording tests | Testing | Complex | 8 |
| Penny-drop recording guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Complex is the contracted bank penny-drop process, not a Very High payment gateway product (out of scope).
