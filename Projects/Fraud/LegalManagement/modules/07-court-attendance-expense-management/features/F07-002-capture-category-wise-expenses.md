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
1. Who creates: Advocate
2. How they create: User records Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage or Specified Other against the matter.
3. How they edit: Attaches voucher/document and saves.
4. How they send for approval: Lines are available to compile into an expense bill (F07-004). Select matter → category amounts → attach voucher → save.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Expense Capture form (listed categories)
- Voucher attach
- Save against the matter
- Not reimbursement gateway; not EVAL valuer billing; not payroll

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Expense Capture form (Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court, Clerkage, Other) | Complex |
| Voucher attach | Easy |
| Capture category-wise expenses history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Expense line operations | Complex |
| Update capture category-wise expenses | Medium |
| Search capture category-wise expenses | Medium |
| Read capture category-wise expenses history | Easy |

### Inputs
Matter; category; Task; Assigned By; amounts per category as used; voucher.

### Outputs
Expense lines; voucher attachments.

### Business Rules
- Category-wise as Annexure-I.
- Always linked to the matter (F07-005).
- Specified Other requires a description.

### Validations
- Matter required; category required; voucher as configured; amounts numeric ≥ 0.

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
- Currency and rate rules as SPLOCA finance directs; no payment gateway.

### Risks
Missing vouchers delay CA review.

### Non Functional Requirements
Lines retained for bill compile.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Expense Capture form (Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court, Clerkage, Other) | UI | Complex | 12 |
| Voucher attach | UI | Easy | 4 |
| Capture category-wise expenses history | UI | Medium | 6 |
| Expense line operations | API | Complex | 8 |
| Update capture category-wise expenses | API | Medium | 6 |
| Search capture category-wise expenses | API | Medium | 6 |
| Read capture category-wise expenses history | API | Easy | 4 |
| Capture category-wise expenses persistence | DB | Medium | 4 |
| Matter link | Integration | Simple | 4 |
| Capture category-wise expenses feature tests | Testing | Medium | 6 |
| Capture category-wise expenses implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
