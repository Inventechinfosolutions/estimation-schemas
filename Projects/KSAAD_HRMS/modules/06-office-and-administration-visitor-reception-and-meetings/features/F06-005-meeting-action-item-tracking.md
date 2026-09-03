# F06-005 — Meeting Action Item Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Meeting Action Item Tracking |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
From confirmed MoM, recorder assigns actions to a Person/Post with due date; assignee updates; assigner/chair closes; history on each item.

### Business Objective
Accountable follow-up from meetings.

### Actors
Applicant: Recorder creates items. Assignee updates progress. Approver: Chair or assigner closes/accepts completion. Other: Auditor.

### User Journey
1. Who creates: Recorder creates items. Assignee updates progress.
2. How they create: On confirmed MoM → Add action: description, assignee Post/Person, due date, Save.
3. How they edit: Creator edits draft items. After assign, assignee cannot change due date; they update status/notes. Due date change is Return-to-creator or chair edit with history.
4. How they send for approval: Assign (submit) notifies assignee. Assignee Submit completion. Chair Confirms close.
5. How the approver sees pending items: Assignee My Actions inbox. Chair overdue actions inbox.
6. How the approver decides: Chair Accept completion or Return to assignee.
7. How the applicant sees history: Item timeline: created, assigned, progress, closed.
8. How the approver sees history: Chair sees all items for meetings they chaired.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own meeting action item history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My meeting action item register | Medium |
| Meeting action item form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver meeting action item inbox | Complex |
| Meeting action item decision panel (approve / reject / return) | Medium |
| My meeting action item history | Medium |
| Team meeting action item history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft meeting action item | Medium |
| Update draft meeting action item | Medium |
| Submit meeting action item for approval | Complex |
| Withdraw meeting action item | Easy |
| Approver inbox query | Medium |
| Approve, reject or return meeting action item | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Meeting, description, assignee, due date, status, notes.

### Outputs
Persisted meeting action item with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own meeting action item.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Assignee and due date mandatory.

### Calculations
Overdue = not closed and today > due date.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional completion evidence.

### Reports
Open/overdue actions by office.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

### Dependencies
Module 01 Person–Post–Role mapping (current Post and supervising Post). Notifications use the mapped Person of the supervising Post.

### Assumptions
- Supervising Post is maintained on the Post master (Module 01).
- Hours use Estimation Master values only, at capability grain (primary and secondary UI, one logical API, persistence, tests, documentation).

### Risks
Wrong supervising Post mapping would send the request to the wrong approver.

### Non Functional Requirements
Inbox and history screens remain usable under concurrent office load. Status history is immutable after write.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My meeting action item register | UI | Medium | 6 |
| Meeting action item form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver meeting action item inbox | UI | Complex | 12 |
| Meeting action item decision panel (approve / reject / return) | UI | Medium | 6 |
| My meeting action item history | UI | Medium | 6 |
| Team meeting action item history (approver) | UI | Medium | 6 |
| Save draft meeting action item | API | Medium | 6 |
| Update draft meeting action item | API | Medium | 6 |
| Submit meeting action item for approval | API | Complex | 8 |
| Withdraw meeting action item | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return meeting action item | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Meeting action item record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on meeting action item status change | Integration | Simple | 4 |
| Meeting Action Item Tracking feature tests | Testing | Complex | 8 |
| Meeting Action Item Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
