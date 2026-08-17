# F07-004 — Accept, reject, revaluation or SCN

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Accept, reject, revaluation or SCN |
| **Module** | 07 — CA Assessment, MIS Reports & Auction-Display Photos |

### Description
The CA chooses Accept, Reject, Order Revaluation, or Issue SCN to penalise the valuer, with remarks. Accept unlocks billing (Module 08) and makes the pack eligible for Claim release (F07-007). Revaluation returns the asset to assignment (F04-001) with the CA remarks visible to the valuer and resets stage (F04-008). SCN is stored on the valuer master and the report.

### Business Objective
Record the CA gate decision that controls billing, Claim release, revaluation loop and SCN.

### Actors
Competent Authority; Approved Valuer (on revaluation); Billing officer (after Accept).

### User Journey
1. CA chooses Accept, Reject, Order Revaluation, or Issue SCN to penalise the valuer, with remarks.
2. Accept unlocks billing (Module 08) and Claim-release eligibility (F07-007).
3. Revaluation returns the asset to assignment with CA remarks visible and resets stage (F04-008).
4. SCN is stored on the valuer master (F02-001) and the report.

### Functional Capabilities
- Record Accept / Reject / Order Revaluation / Issue SCN with remarks
- Unlock billing and release only on Accept
- Revaluation loop to assignment + stage reset
- Store SCN on valuer master and report

### Inputs
Decision; remarks.

### Outputs
Decision on the valuation; billing/release eligibility; revaluation assignment state; SCN record.

### Business Rules
- Billing window does not open unless Accepted (F08-001)
- Non-Accepted pack cannot be released (F07-007)
- Revaluation shows CA remarks to the valuer

### Validations
- CA assessment exists (F07-002)
- Remarks present on Reject / Revaluation / SCN as Authority requires

### Calculations
None.

### Workflow
Choose decision → apply gates → if revaluation reset stage and return to assignment → if SCN write valuer master.

### Search Requirements
Decision, valuer, asset, SCN.

### Documents
SCN (stored).

### Reports
CA decision register.

### Notifications
In-app to valuer on revaluation/SCN; no standalone notification module.

### Security
CA Person attributable; SCN on professional master is not a login disable (that remains shared IAM).

### Integrations
Internal assignment/stage and billing gate.

### Dependencies
F07-002; F04-001; F04-008; F08-001; F07-007; F02-001.

### Assumptions
- SCN penalise process beyond storage is Authority operational practice.

### Risks
Accept without complete assessment parameters.

### Non Functional Requirements
Decision immutable except by authorised correction with history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| CA decision (Accept/Reject/Revalue/SCN) | UI | Medium | 6 |
| CA decision workflow | API | Very High | 16 |
| Decision and SCN store | Database | Medium | 4 |
| Assignment/stage/billing gate consume | Integration | Simple | 4 |
| CA decision tests | Testing | Complex | 8 |
| CA decision guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- API Very High 16 for decision workflow.
