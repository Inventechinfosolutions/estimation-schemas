# F08-001 — Open billing only after CA acceptance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Open billing only after CA acceptance |
| **Module** | 08 — Valuer Billing |

### Description
A Billing officer (or Office user so authorised) enters Valuer Code, selects the valuation report and opens the CA report. If the CA decision is not Accept, the billing window does not open and the user sees the current decision (Reject / Revaluation / SCN).

### Business Objective
Keep the valuer bill closed until the CA has Accepted the report.

### Actors
Billing officer; Office user (authorised).

### User Journey
1. Billing officer enters Valuer Code, selects the valuation report and opens the CA report.
2. If the CA decision is not Accept, the billing window does not open and the user sees Reject / Revaluation / SCN.
3. If Accept, F08-002 may proceed.

### Functional Capabilities
- Populate valuer basics by Valuer Code
- Open CA report in billing context
- Refuse billing window unless CA Accept

### Inputs
Valuer Code; selected valuation report.

### Outputs
Open billing window or blocked with current CA decision.

### Business Rules
- Billing window opens only if CA has accepted
- Server-side gate, not only hidden menu

### Validations
- Valuer Code exists (F02-001)
- Report belongs to that valuer
- Decision is Accept to open

### Calculations
None.

### Workflow
Enter Valuer Code → select report → read CA decision → open or block.

### Search Requirements
Valuer Code, report, decision.

### Documents
CA report (view).

### Reports
Blocked billing attempts (optional extract).

### Notifications
In-app current decision when blocked.

### Security
Billing officer / authorised Office; cannot bypass Accept.

### Integrations
Internal CA decision consume (F07-004).

### Dependencies
F07-004; F02-001; F07-002.

### Assumptions
- Payment execution remains out of scope.

### Risks
Opening bill on Revaluation if gate fails.

### Non Functional Requirements
Gate enforced on API.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Billing gate and Valuer Code populate | UI | Medium | 6 |
| Accept-only billing gate | API | Medium | 6 |
| Billing-open attempt log | Database | Simple | 1 |
| CA decision consume | Integration | Simple | 4 |
| Billing-gate tests | Testing | Medium | 6 |
| Billing gate note | Documentation | Easy | 2 |
| **Total** | | | **25** |

### Estimation Assumptions
- Bill/voucher content is F08-002.
