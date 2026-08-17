# F05-001 — Assign task with due date and status

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Assign task with due date and status |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
An authorised user opens a matter (or the task inbox), assigns a task to a Person/Post, sets due date and initial status, and saves. The assignee sees it in the task inbox with an alert.

### Business Objective
Start the legal/official task lifecycle by assigning a Person/Post, due date and status against a matter (or the inbox).

### Actors
Legal Cell; Advocate; authorised assigner.

### User Journey
1. User opens a matter or the Task Inbox.
2. Assigns a task to a Person/Post, sets due date and initial status, and saves.
3. Assignee sees the task in the Task Inbox with an alert.

### Functional Capabilities
- Task Assignment form
- Task Inbox list
- Assign to shared Person/Post with due date and initial status
- Alert to assignee
- Matter-linked or inbox-originated official tasks

### Inputs
Matter (where applicable); assignee Person/Post; due date; initial status; task description.

### Outputs
Task record; inbox row; assignee alert.

### Business Rules
- Assignee is a shared-identity Person/Post — no local user list.
- Status values come from central masters (F02-005).
- Not a public collaboration portal.

### Validations
Assignee active; due date required; matter required when the task is matter-bound; status from master.

### Calculations
None at assign (overdue is F05-002).

### Workflow
Open matter/inbox → assign → save → inbox + alert.

### Search Requirements
Task inbox by assignee, matter, due date, status.

### Documents
Optional assignment attachment.

### Reports
Open assignments list.

### Notifications
Alert to assignee.

### Security
Assigner Post must be allowed; assignee sees only assigned/visible tasks.

### Integrations
Person/Post lookup (Simple).

### Dependencies
F01-001; F04-001; F02-005; F05-002.

### Assumptions
Android inbox (F09-002) consumes the same task.

### Risks
Assigning to a deactivated Person if shared IAM is stale.

### Non Functional Requirements
Inbox refresh suitable for court-day.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Task Assignment form | UI | Complex | 12 |
| Task Inbox list | UI | Medium | 6 |
| Assign and alert operations | API | Complex | 8 |
| Task entities | Database | Medium | 4 |
| Person/Post lookup | Integration | Simple | 4 |
| Task assignment tests | Testing | Medium | 6 |
| Task assignment guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Accept/reject/reassign/reprimand is F05-002.
