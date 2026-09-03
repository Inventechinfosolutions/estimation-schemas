# F07-005 — Link attendance and expense to matter

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-005 |
| **Feature Name** | Link attendance and expense to matter |
| **Module** | 07 — Court Attendance & Expense Management |

### Description
When saving attendance or expense, the user must select the court matter. Opening the matter shows those attendance and expense rows; they are not stored as unlinked personal notes.

### Business Objective
Enforce that attendance and authorised expenses always hang off the court matter — never as unlinked personal notes.

### Actors
Advocate; Legal Cell; system (constraint).

### User Journey
1. Who creates: Advocate
2. How they create: On save of attendance or expense, the user must select the court matter (Matter Mandatory picker).
3. How they edit: Opening the matter shows those attendance and expense rows on the Matter Attendance/Expense panel.
4. How they send for approval: Save without a matter is refused. Select matter → save attendance/expense → appear on matter.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Mandatory picker on save
- Matter Attendance/Expense panel
- Refuse unlinked personal notes
- Rows visible when the matter is opened

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Mandatory picker on save | Easy |
| Matter Attendance/Expense panel | Medium |
| Link attendance and expense to matter history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Mandatory link enforcement | Medium |
| Update link attendance and expense to matter | Medium |
| Search link attendance and expense to matter | Medium |
| Read link attendance and expense to matter history | Easy |

### Inputs
Attendance or expense draft; selected matter.

### Outputs
Linked rows; validation error if matter missing.

### Business Rules
- Attendance and authorised expenses shall link to the concerned court matter.
- Unlinked personal notes are not allowed.
- Opening the matter shows those rows.

### Validations
- Matter required and must exist and be visible; cannot detach after save except via authorised correction that re-links.

### Calculations
None.

### Workflow
Select matter → save attendance/expense → appear on matter.

### Search Requirements
Via matter dashboard and F07-003.

### Documents
None new.

### Reports
Unlinked-attempt audit if save was refused.

### Notifications
None.

### Security
Cannot park expenses on a matter the Person cannot open.

### Integrations
Matter dashboard (Simple).

### Dependencies
F07-001; F07-002; F04-001; F04-002.

### Assumptions
- F07-001/F07-002 screens include the picker; this feature is the enforcement and matter panel.

### Risks
Workaround via dummy matters — process control, not extra IAM.

### Non Functional Requirements
Constraint enforced server-side.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Mandatory picker on save | UI | Easy | 4 |
| Matter Attendance/Expense panel | UI | Medium | 6 |
| Link attendance and expense to matter history | UI | Medium | 6 |
| Mandatory link enforcement | API | Medium | 6 |
| Update link attendance and expense to matter | API | Medium | 6 |
| Search link attendance and expense to matter | API | Medium | 6 |
| Read link attendance and expense to matter history | API | Easy | 4 |
| Link attendance and expense to matter persistence | DB | Medium | 4 |
| Matter dashboard consume | Integration | Simple | 4 |
| Link attendance and expense to matter feature tests | Testing | Easy | 4 |
| Link attendance and expense to matter implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
