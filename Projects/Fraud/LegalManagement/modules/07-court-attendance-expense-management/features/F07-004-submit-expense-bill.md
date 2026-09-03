# F07-004 — Submit expense bill

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Submit expense bill |
| **Module** | 07 — Court Attendance & Expense Management |

### Description
The user compiles authorised expenses for the period, submits the expense bill, and the bill remains linked to the matter for CA or supervisor review.

### Business Objective
Compile authorised expense lines into a bill still linked to the matter for CA/supervisor review — not a reimbursement gateway.

### Actors
Advocate; Legal Cell; Competent Authority / supervisor (review).

### User Journey
1. Who creates: Advocate
2. How they create: User compiles authorised expenses for the period on the Bill Compile screen.
3. How they edit: Submits the expense bill.
4. How they send for approval: The bill remains linked to the matter for CA or supervisor review. Compile lines → submit → CA/supervisor review → status on matter.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Bill Compile screen
- Supervisor/CA Review
- Submit bill linked to the matter
- Vouchers visible on the bill
- No payment/reimbursement gateway; no payroll

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Bill Compile screen | Complex |
| Supervisor/CA Review | Medium |
| Submit expense bill history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Bill submit and review operations | Complex |
| Update submit expense bill | Medium |
| Search submit expense bill | Medium |
| Read submit expense bill history | Easy |

### Inputs
Period; selected expense lines; matter; submitter Person.

### Outputs
Expense bill; review status; still linked to matter.

### Business Rules
- An expense bill is linked to the matter and shows vouchers.
- Only authorised (saved) lines can be compiled.
- EVAL valuer billing is out of scope.

### Validations
- At least one line; all lines same matter (or policy-stated set); period required; review Post required to approve if configured.

### Calculations
Bill total = sum of included lines.

### Workflow
Compile lines → submit → CA/supervisor review → status on matter.

### Search Requirements
Bills by matter, period, submitter, status.

### Documents
Bill plus vouchers.

### Reports
Expense bills for review.

### Notifications
Submit notice to CA/supervisor.

### Security
Review restricted; amounts not editable after submit without recorded revision.

### Integrations
Matter linkage (Simple).

### Dependencies
F07-002; F07-005; F01-001; F04-002.

### Assumptions
- Payment of the bill is outside this application (no gateway).

### Risks
Lines from another matter compiled in error — F07-005 must block.

### Non Functional Requirements
Review queue for supervisor.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Bill Compile screen | UI | Complex | 12 |
| Supervisor/CA Review | UI | Medium | 6 |
| Submit expense bill history | UI | Medium | 6 |
| Bill submit and review operations | API | Complex | 8 |
| Update submit expense bill | API | Medium | 6 |
| Search submit expense bill | API | Medium | 6 |
| Read submit expense bill history | API | Easy | 4 |
| Submit expense bill persistence | DB | Medium | 4 |
| Matter linkage | Integration | Simple | 4 |
| Submit expense bill feature tests | Testing | Medium | 6 |
| Submit expense bill implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
