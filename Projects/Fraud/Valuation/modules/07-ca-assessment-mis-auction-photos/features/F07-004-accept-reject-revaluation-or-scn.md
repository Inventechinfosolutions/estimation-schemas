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
1. Who creates: Competent Authority
2. How they create: CA chooses Accept, Reject, Order Revaluation, or Issue SCN to penalise the valuer, with remarks.
3. How they edit: Accept unlocks billing (Module 08) and Claim-release eligibility (F07-007).
4. How they send for approval: Revaluation returns the asset to assignment with CA remarks visible and resets stage (F04-008). Choose decision → apply gates → if revaluation reset stage and return to assignment → if SCN write valuer master.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Competent Authority works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Competent Authority opens history on the record. SCN is stored on the valuer master (F02-001) and the report.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record Accept / Reject / Order Revaluation / Issue SCN with remarks
- Unlock billing and release only on Accept
- Revaluation loop to assignment + stage reset
- Store SCN on valuer master and report

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My accept, reject, revaluation or scn list / queue | Medium |
| CA decision (Accept/Reject/Revalue/SCN) | Medium |
| Accept, reject, revaluation or scn history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| CA decision workflow | Very High |
| Update accept, reject, revaluation or scn | Medium |
| Search accept, reject, revaluation or scn | Medium |
| Read accept, reject, revaluation or scn history | Easy |

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
|---|---|---|---|
| My accept, reject, revaluation or scn list / queue | UI | Medium | 6 |
| CA decision (Accept/Reject/Revalue/SCN) | UI | Medium | 6 |
| Accept, reject, revaluation or scn history | UI | Medium | 6 |
| CA decision workflow | API | Very High | 16 |
| Update accept, reject, revaluation or scn | API | Medium | 6 |
| Search accept, reject, revaluation or scn | API | Medium | 6 |
| Read accept, reject, revaluation or scn history | API | Easy | 4 |
| Accept, reject, revaluation or scn persistence | DB | Medium | 4 |
| Assignment/stage/billing gate consume | Integration | Simple | 4 |
| Accept, reject, revaluation or SCN feature tests | Testing | Complex | 8 |
| Accept, reject, revaluation or SCN implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
