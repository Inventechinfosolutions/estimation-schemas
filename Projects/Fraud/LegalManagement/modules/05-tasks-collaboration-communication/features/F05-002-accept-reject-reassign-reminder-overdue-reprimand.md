# F05-002 — Accept, reject, reassign, reminder, overdue, reprimand

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Accept, reject, reassign, reminder, overdue, reprimand |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
The assignee accepts or rejects the task. The assigner may reassign, send a reminder, view overdue items, or record a reprimand/warning. Each action is stored on the task with Person and timestamp.

### Business Objective
Complete the task action set required by Annexure-I: accept/reject, reassign, reminder, overdue view, reprimand/warning, all audited.

### Actors
Assignee; assigner; supervisor.

### User Journey
1. Who creates: Assignee
2. How they create: Assignee opens the task and accepts or rejects.
3. How they edit: Assigner may reassign, send a reminder, open the Overdue register, or record a reprimand/warning.
4. How they send for approval: Each action is stored on the task with Person and timestamp. Accept/reject → optional reassign/remind/reprimand → history.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Assignee works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Assignee opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Task Action panel (accept, reject, reassign, reminder)
- Overdue and Reprimand register
- Action history with Person and timestamp
- Embedded workflow — not a separate BPM product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Task Action panel (accept, reject, reassign, reminder) | Complex |
| Overdue and Reprimand register | Medium |
| Accept, reject, reassign, reminder, overdue, reprimand history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Lifecycle action operations | Complex |
| Update accept, reject, reassign, reminder, overdue, reprimand | Medium |
| Search accept, reject, reassign, reminder, overdue, reprimand | Medium |
| Read accept, reject, reassign, reminder, overdue, reprimand history | Easy |

### Inputs
Action type; optional new assignee; reminder text; reprimand/warning text.

### Outputs
Updated task status; action history; overdue list.

### Business Rules
- Every action stored with Person and timestamp (shared Person).
- Reject returns the task to the assigner path as configured.
- Reprimand/warning is recorded, not a payroll action.

### Validations
- Only assignee accepts/rejects; reassign target must be active; overdue is derived from due date and incomplete status.

### Calculations
Overdue flag when due date passed and not complete.

### Workflow
Accept/reject → optional reassign/remind/reprimand → history.

### Search Requirements
Overdue by assignee, matter, days overdue.

### Documents
Optional reprimand note.

### Reports
Overdue tasks; reprimand/warning log.

### Notifications
Reminder; reassignment alert; reject notice to assigner.

### Security
Reprimand visibility restricted to supervisor Posts as configured.

### Integrations
Alert to assignee/assigner (Simple).

### Dependencies
F05-001; F01-001.

### Assumptions
- Completion with report is F05-003.

### Risks
Reprimand content is sensitive; must not leak via Community spaces.

### Non Functional Requirements
Action history immutable once saved.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Task Action panel (accept, reject, reassign, reminder) | UI | Complex | 12 |
| Overdue and Reprimand register | UI | Medium | 6 |
| Accept, reject, reassign, reminder, overdue, reprimand history | UI | Medium | 6 |
| Lifecycle action operations | API | Complex | 8 |
| Update accept, reject, reassign, reminder, overdue, reprimand | API | Medium | 6 |
| Search accept, reject, reassign, reminder, overdue, reprimand | API | Medium | 6 |
| Read accept, reject, reassign, reminder, overdue, reprimand history | API | Easy | 4 |
| Accept, reject, reassign, reminder, overdue, reprimand persistence | DB | Medium | 4 |
| Alert to assignee/assigner | Integration | Simple | 4 |
| Accept, reject, reassign, reminder, overdue, reprimand feature tests | Testing | Complex | 8 |
| Accept, reject, reassign, reminder, overdue, reprimand implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **67** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
