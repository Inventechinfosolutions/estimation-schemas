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
1. Assignee opens the task and accepts or rejects.
2. Assigner may reassign, send a reminder, open the Overdue register, or record a reprimand/warning.
3. Each action is stored on the task with Person and timestamp.

### Functional Capabilities
- Task Action panel (accept, reject, reassign, reminder)
- Overdue and Reprimand register
- Action history with Person and timestamp
- Embedded workflow — not a separate BPM product

### Inputs
Action type; optional new assignee; reminder text; reprimand/warning text.

### Outputs
Updated task status; action history; overdue list.

### Business Rules
- Every action stored with Person and timestamp (shared Person).
- Reject returns the task to the assigner path as configured.
- Reprimand/warning is recorded, not a payroll action.

### Validations
Only assignee accepts/rejects; reassign target must be active; overdue is derived from due date and incomplete status.

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
Completion with report is F05-003.

### Risks
Reprimand content is sensitive; must not leak via Community spaces.

### Non Functional Requirements
Action history immutable once saved.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Task Action panel (accept, reject, reassign, reminder) | UI | Complex | 12 |
| Overdue and Reprimand register | UI | Medium | 6 |
| Lifecycle action operations | API | Complex | 8 |
| Action history entities | Database | Medium | 4 |
| Alert to assignee/assigner | Integration | Simple | 4 |
| Task lifecycle tests | Testing | Complex | 8 |
| Task accept/reject/reassign/reprimand guide | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- Completion report and team schedule are F05-003.
