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
1. Who creates: Officer
2. How they create: Officer records a penny-drop request against the depositor’s refund account.
3. How they edit: Result from the contracted bank is recorded: success/fail, match indicators, timestamp.
4. How they send for approval: Auditor later opens the same depositor or payment trail and sees that penny-drop event. Request → bank result → record. Not a bank-core product.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record penny-drop request and result against the refund account.
- Store success/fail, match indicators and timestamp.
- Surface the event on depositor and payment forensic trails (F01-010 / F08-005).

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My penny-drop verification recording list / queue | Medium |
| Penny-drop recording screen | Medium |
| Penny-drop verification recording history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Penny-drop event operations | Complex |
| Update penny-drop verification recording | Medium |
| Search penny-drop verification recording | Medium |
| Read penny-drop verification recording history | Easy |

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
| My penny-drop verification recording list / queue | UI | Medium | 6 |
| Penny-drop recording screen | UI | Medium | 6 |
| Penny-drop verification recording history | UI | Medium | 6 |
| Penny-drop event operations | API | Complex | 8 |
| Update penny-drop verification recording | API | Medium | 6 |
| Search penny-drop verification recording | API | Medium | 6 |
| Read penny-drop verification recording history | API | Easy | 4 |
| Penny-drop event persistence | DB | Easy | 2 |
| Contracted-bank penny-drop process | Integration | Complex | 24 |
| Penny-drop verification recording feature tests | Testing | Complex | 8 |
| Penny-drop verification recording implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
