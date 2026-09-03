# F03-006 — Training and Capacity Building Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-006 |
| **Feature Name** | Training and Capacity Building Management |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
HR or a supervisor nominates a Person to a training programme; the nominee's supervising Post (or Training Officer) approves; attendance/completion is recorded.

### Business Objective
Track nominations, approvals and completion.

### Actors
Applicant: HR Training Officer or the staff member's supervisor creates a nomination. Staff member may self-nominate if policy allows. Approver: Training Officer Post or supervising Post per workflow template. Other: Nominee (sees own nominations). Auditor.

### User Journey
1. Who creates: HR Training Officer or the staff member's supervisor creates a nomination. Staff member may self-nominate if policy allows.
2. How they create: Applicant opens Training programmes (catalogue) → Nominate, selects Person, programme, dates, Save draft.
3. How they edit: Draft/Returned nominations can be edited. After approval, completion is recorded separately (not by editing the nomination).
4. How they send for approval: Submit to the configured approver.
5. How the approver sees pending items: Approver Training nomination inbox.
6. How the approver decides: Approve, reject or return. After the event, Training Officer records Completed / Not attended with dates.
7. How the applicant sees history: Nominator and nominee see nomination and completion history.
8. How the approver sees history: Approver sees decisions and completion status for programmes they own.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own training nomination history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My training nomination register | Medium |
| Training nomination form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver training nomination inbox | Complex |
| Training nomination decision panel (approve / reject / return) | Medium |
| My training nomination history | Medium |
| Team training nomination history (approver) | Medium |
| Training programme catalogue (read/admin) | Medium |
| Completion recording form | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft training nomination | Medium |
| Update draft training nomination | Medium |
| Submit training nomination for approval | Complex |
| Withdraw training nomination | Easy |
| Approver inbox query | Medium |
| Approve, reject or return training nomination | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record training completion | Easy |

### Inputs
Person, programme, dates, nomination remarks, completion status.

### Outputs
Persisted training nomination with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own training nomination.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Programme and Person mandatory.
- Dates within programme window.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional course material via knowledge centre.

### Reports
Nominations and completions by programme/office.

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
| My training nomination register | UI | Medium | 6 |
| Training nomination form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver training nomination inbox | UI | Complex | 12 |
| Training nomination decision panel (approve / reject / return) | UI | Medium | 6 |
| My training nomination history | UI | Medium | 6 |
| Team training nomination history (approver) | UI | Medium | 6 |
| Training programme catalogue (read/admin) | UI | Medium | 6 |
| Completion recording form | UI | Easy | 4 |
| Save draft training nomination | API | Medium | 6 |
| Update draft training nomination | API | Medium | 6 |
| Submit training nomination for approval | API | Complex | 8 |
| Withdraw training nomination | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return training nomination | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record training completion | API | Easy | 4 |
| Training nomination record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on training nomination status change | Integration | Simple | 4 |
| Training and Capacity Building Management feature tests | Testing | Complex | 8 |
| Training and Capacity Building Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **133** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
