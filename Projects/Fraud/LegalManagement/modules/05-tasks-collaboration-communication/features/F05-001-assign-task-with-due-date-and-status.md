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
1. Who creates: Legal Cell
2. How they create: User opens a matter or the Task Inbox.
3. How they edit: Assigns a task to a Person/Post, sets due date and initial status, and saves. Draft or returned records can be edited; decided records are not silently overwritten.
4. How they send for approval: Assignee sees the task in the Task Inbox with an alert. Open matter/inbox → assign → save → inbox + alert.
5. How the approver sees pending items: Advocate opens the pending inbox for this feature and opens a row.
6. How the approver decides: Advocate approves, rejects or returns with remarks.
7. How the applicant sees history: Legal Cell opens history on the record (actor Person, Post, time, status, remarks).
8. How the approver / auditor sees history: Advocate and auditor open the same history for items in their scope.

### Functional Capabilities
- Task Assignment form
- Task Inbox list
- Assign to shared Person/Post with due date and initial status
- Alert to assignee
- Matter-linked or inbox-originated official tasks

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My assign task with due date and status register | Medium |
| Task Assignment form | Complex |
| Submit confirmation | Simple |
| Approver assign task with due date and status inbox | Complex |
| Assign task with due date and status decision panel (approve / reject / return) | Medium |
| My assign task with due date and status history | Medium |
| Team assign task with due date and status history (approver) | Medium |
| Task Inbox list | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft assign task with due date and status | Medium |
| Update draft assign task with due date and status | Medium |
| Assign and alert operations | Complex |
| Withdraw assign task with due date and status | Easy |
| Approver inbox query | Medium |
| Approve, reject or return assign task with due date and status | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Matter (where applicable); assignee Person/Post; due date; initial status; task description.

### Outputs
Task record; inbox row; assignee alert.

### Business Rules
- Assignee is a shared-identity Person/Post — no local user list.
- Status values come from central masters (F02-005).
- Not a public collaboration portal.

### Validations
- Assignee active; due date required; matter required when the task is matter-bound; status from master.

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
- Android inbox (F09-002) consumes the same task.

### Risks
Assigning to a deactivated Person if shared IAM is stale.

### Non Functional Requirements
Inbox refresh suitable for court-day.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My assign task with due date and status register | UI | Medium | 6 |
| Task Assignment form | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver assign task with due date and status inbox | UI | Complex | 12 |
| Assign task with due date and status decision panel (approve / reject / return) | UI | Medium | 6 |
| My assign task with due date and status history | UI | Medium | 6 |
| Team assign task with due date and status history (approver) | UI | Medium | 6 |
| Task Inbox list | UI | Medium | 6 |
| Save draft assign task with due date and status | API | Medium | 6 |
| Update draft assign task with due date and status | API | Medium | 6 |
| Assign and alert operations | API | Complex | 8 |
| Withdraw assign task with due date and status | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return assign task with due date and status | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Assign task with due date and status record and status history | DB | Medium | 4 |
| Person/Post lookup | Integration | Simple | 4 |
| Assign task with due date and status feature tests | Testing | Medium | 6 |
| Assign task with due date and status implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **122** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
