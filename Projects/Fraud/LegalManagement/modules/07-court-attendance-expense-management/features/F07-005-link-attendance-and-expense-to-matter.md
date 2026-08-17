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
1. On save of attendance or expense, the user must select the court matter (Matter Mandatory picker).
2. Opening the matter shows those attendance and expense rows on the Matter Attendance/Expense panel.
3. Save without a matter is refused.

### Functional Capabilities
- Matter Mandatory picker on save
- Matter Attendance/Expense panel
- Refuse unlinked personal notes
- Rows visible when the matter is opened

### Inputs
Attendance or expense draft; selected matter.

### Outputs
Linked rows; validation error if matter missing.

### Business Rules
- Attendance and authorised expenses shall link to the concerned court matter.
- Unlinked personal notes are not allowed.
- Opening the matter shows those rows.

### Validations
Matter required and must exist and be visible; cannot detach after save except via authorised correction that re-links.

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
F07-001/F07-002 screens include the picker; this feature is the enforcement and matter panel.

### Risks
Workaround via dummy matters — process control, not extra IAM.

### Non Functional Requirements
Constraint enforced server-side.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Matter Mandatory picker on save | UI | Easy | 4 |
| Matter Attendance/Expense panel | UI | Medium | 6 |
| Mandatory link enforcement | API | Medium | 6 |
| Link constraints | Database | Easy | 2 |
| Matter dashboard consume | Integration | Simple | 4 |
| Matter-link tests | Testing | Easy | 4 |
| Attendance/expense matter-link guide | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Does not re-estimate full attendance/expense forms.
