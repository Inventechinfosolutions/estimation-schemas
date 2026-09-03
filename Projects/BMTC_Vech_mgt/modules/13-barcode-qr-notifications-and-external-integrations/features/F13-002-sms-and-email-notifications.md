# F13-002 — SMS and Email Notifications

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-002 |
| **Feature Name** | SMS and Email Notifications |
| **Module** | 13 — Barcode, QR, Notifications and External Integrations |

### Description
SMS gateway and email for PM alerts, reorder, job-card pending, PO overdue. SMS charges borne by BMTC.

### Business Objective
RFP SMS/email integration.

### Actors
Applicant: System sends. Administrator configures templates and which Posts receive which event. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: System sends. Administrator configures templates and which Posts receive which event.
2. How they create: Template register → New event type, SMS/email body, audience Posts, Save draft.
3. How they edit: Draft/Returned editable. After approve, new version for wording changes.
4. How they send for approval: Template submit to Access/Admin Checker.
5. How the approver sees pending items: Checker template inbox. Recipients see in-app plus SMS/email.
6. How the approver decides: Approve template go-live.
7. How the applicant sees history: Template versions and send log.
8. How the approver sees history: Approved templates.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own notification event history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My notification event register | Medium |
| Notification event form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver notification event inbox | Complex |
| Notification event decision panel (approve / reject / return) | Medium |
| My notification event history | Medium |
| Team notification event history (approver) | Medium |
| Template form | Medium |
| Send log | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft notification event | Medium |
| Update draft notification event | Medium |
| Submit notification event for approval | Complex |
| Withdraw notification event | Easy |
| Approver inbox query | Medium |
| Approve, reject or return notification event | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Send SMS | Medium |
| Send email | Medium |

### Inputs
Event, channel, audience, body.

### Outputs
Persisted notification event with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own notification event.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Audience not empty.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Failed sends.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
SMS gateway and SMTP/email

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

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
| My notification event register | UI | Medium | 6 |
| Notification event form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver notification event inbox | UI | Complex | 12 |
| Notification event decision panel (approve / reject / return) | UI | Medium | 6 |
| My notification event history | UI | Medium | 6 |
| Team notification event history (approver) | UI | Medium | 6 |
| Template form | UI | Medium | 6 |
| Send log | UI | Medium | 6 |
| Save draft notification event | API | Medium | 6 |
| Update draft notification event | API | Medium | 6 |
| Submit notification event for approval | API | Complex | 8 |
| Withdraw notification event | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return notification event | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Send SMS | API | Medium | 6 |
| Send email | API | Medium | 6 |
| Notification event record, status history and attachments metadata | DB | Medium | 4 |
| SMS gateway and SMTP/email | Integration | Medium | 16 |
| SMS and Email Notifications feature tests | Testing | Complex | 8 |
| SMS and Email Notifications implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **155** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
