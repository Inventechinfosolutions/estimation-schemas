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
1. Who creates: Billing officer
2. How they create: Billing officer enters Valuer Code, selects the valuation report and opens the CA report.
3. How they edit: If the CA decision is not Accept, the billing window does not open and the user sees Reject / Revaluation / SCN.
4. How they send for approval: If Accept, F08-002 may proceed. Enter Valuer Code → select report → read CA decision → open or block.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Billing officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Billing officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Populate valuer basics by Valuer Code
- Open CA report in billing context
- Refuse billing window unless CA Accept

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My open billing only after ca acceptance list / queue | Medium |
| Billing gate and Valuer Code populate | Medium |
| Open billing only after ca acceptance history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Accept-only billing gate | Medium |
| Update open billing only after ca acceptance | Medium |
| Search open billing only after ca acceptance | Medium |
| Read open billing only after ca acceptance history | Easy |

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
|---|---|---|---|
| My open billing only after ca acceptance list / queue | UI | Medium | 6 |
| Billing gate and Valuer Code populate | UI | Medium | 6 |
| Open billing only after ca acceptance history | UI | Medium | 6 |
| Accept-only billing gate | API | Medium | 6 |
| Update open billing only after ca acceptance | API | Medium | 6 |
| Search open billing only after ca acceptance | API | Medium | 6 |
| Read open billing only after ca acceptance history | API | Easy | 4 |
| Open billing only after ca acceptance persistence | DB | Medium | 4 |
| CA decision consume | Integration | Simple | 4 |
| Open billing only after CA acceptance feature tests | Testing | Medium | 6 |
| Open billing only after CA acceptance implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
