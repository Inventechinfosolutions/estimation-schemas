# F15-004 — Training Completion and Acknowledgement Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-004 |
| **Feature Name** | Training Completion and Acknowledgement Tracking |
| **Module** | 15 — Knowledge Center & Learning |

### Description
Staff mark acknowledgement/completion of a learning item (or Training Officer records it); supervisor may confirm; history per Person.

### Business Objective
Know who completed what.

### Actors
Applicant: Staff member records own completion, or Training Officer records for a Person. Approver: Supervisor confirms if the item requires confirmation. Other: HR. Auditor.

### User Journey
1. Who creates: Staff member records own completion, or Training Officer records for a Person.
2. How they create: My Learning → select item → Record completion/acknowledgement, date, Save. Officer may bulk-record with reason.
3. How they edit: Draft editable. After confirm, corrections via Return.
4. How they send for approval: Submit if confirmation required; else Save = completed.
5. How the approver sees pending items: Supervisor completion inbox.
6. How the approver decides: Confirm or reject (then staff must redo).
7. How the applicant sees history: My completions.
8. How the approver sees history: Team completions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own learning completion history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My learning completion register | Medium |
| Learning completion form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver learning completion inbox | Complex |
| Learning completion decision panel (approve / reject / return) | Medium |
| My learning completion history | Medium |
| Team learning completion history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft learning completion | Medium |
| Update draft learning completion | Medium |
| Submit learning completion for approval | Complex |
| Withdraw learning completion | Easy |
| Approver inbox query | Medium |
| Approve, reject or return learning completion | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Bulk record completion | Medium |

### Inputs
Person, learning item, date, acknowledgement flag.

### Outputs
Persisted learning completion with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own learning completion.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Item and date mandatory.

### Calculations
Completion % by office = completed / assigned.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional certificate.

### Reports
Pending completions.

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
| My learning completion register | UI | Medium | 6 |
| Learning completion form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver learning completion inbox | UI | Complex | 12 |
| Learning completion decision panel (approve / reject / return) | UI | Medium | 6 |
| My learning completion history | UI | Medium | 6 |
| Team learning completion history (approver) | UI | Medium | 6 |
| Save draft learning completion | API | Medium | 6 |
| Update draft learning completion | API | Medium | 6 |
| Submit learning completion for approval | API | Complex | 8 |
| Withdraw learning completion | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return learning completion | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Bulk record completion | API | Medium | 6 |
| Learning completion record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on learning completion status change | Integration | Simple | 4 |
| Training Completion and Acknowledgement Tracking feature tests | Testing | Complex | 8 |
| Training Completion and Acknowledgement Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
