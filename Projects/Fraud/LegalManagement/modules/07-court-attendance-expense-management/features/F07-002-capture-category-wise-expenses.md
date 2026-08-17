# F07-002 — Capture category-wise expenses

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Capture category-wise expenses |
| **Module** | 07 — Court Attendance & Expense Management |

### Description
The user records Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage or Specified Other against the matter, attaches voucher/document, and saves.

### Business Objective
Capture authorised category-wise expenses against the matter with voucher, not as personal unlinked notes.

### Actors
Advocate; Legal Cell.

### User Journey
1. User records Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage or Specified Other against the matter.
2. Attaches voucher/document and saves.
3. Lines are available to compile into an expense bill (F07-004).

### Functional Capabilities
- Expense Capture form (listed categories)
- Voucher attach
- Save against the matter
- Not reimbursement gateway; not EVAL valuer billing; not payroll

### Inputs
Matter; category; Task; Assigned By; amounts per category as used; voucher.

### Outputs
Expense lines; voucher attachments.

### Business Rules
- Category-wise as Annexure-I.
- Always linked to the matter (F07-005).
- Specified Other requires a description.

### Validations
Matter required; category required; voucher as configured; amounts numeric ≥ 0.

### Calculations
Line amounts; bill totals in F07-004.

### Workflow
Select matter → category amounts → attach voucher → save.

### Search Requirements
F07-003.

### Documents
Vouchers.

### Reports
Expense lines by category/matter.

### Notifications
None required on each line.

### Security
Vouchers follow document rights; amounts attributable.

### Integrations
Matter link (Simple).

### Dependencies
F07-001 matter; F07-004; F07-005; F02-005.

### Assumptions
Currency and rate rules as SPLOCA finance directs; no payment gateway.

### Risks
Missing vouchers delay CA review.

### Non Functional Requirements
Lines retained for bill compile.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Expense Capture form (Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court, Clerkage, Other) | UI | Complex | 12 |
| Voucher attach | UI | Easy | 4 |
| Expense line operations | API | Complex | 8 |
| Expense entities | Database | Medium | 4 |
| Matter link | Integration | Simple | 4 |
| Expense capture tests | Testing | Medium | 6 |
| Category-wise expense guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- Bill submit/review is F07-004.
