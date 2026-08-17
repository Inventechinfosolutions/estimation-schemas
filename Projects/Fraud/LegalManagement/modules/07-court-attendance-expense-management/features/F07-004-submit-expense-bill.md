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
1. User compiles authorised expenses for the period on the Bill Compile screen.
2. Submits the expense bill.
3. The bill remains linked to the matter for CA or supervisor review.

### Functional Capabilities
- Bill Compile screen
- Supervisor/CA Review
- Submit bill linked to the matter
- Vouchers visible on the bill
- No payment/reimbursement gateway; no payroll

### Inputs
Period; selected expense lines; matter; submitter Person.

### Outputs
Expense bill; review status; still linked to matter.

### Business Rules
- An expense bill is linked to the matter and shows vouchers.
- Only authorised (saved) lines can be compiled.
- EVAL valuer billing is out of scope.

### Validations
At least one line; all lines same matter (or policy-stated set); period required; review Post required to approve if configured.

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
Payment of the bill is outside this application (no gateway).

### Risks
Lines from another matter compiled in error — F07-005 must block.

### Non Functional Requirements
Review queue for supervisor.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Bill Compile screen | UI | Complex | 12 |
| Supervisor/CA Review | UI | Medium | 6 |
| Bill submit and review operations | API | Complex | 8 |
| Bill entities | Database | Medium | 4 |
| Matter linkage | Integration | Simple | 4 |
| Expense bill tests | Testing | Medium | 6 |
| Expense bill guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- No payment-gateway Integration Very High hours.
