# F16-006 — Controlled External Integration Touchpoints

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-006 |
| **Feature Name** | Controlled External Integration Touchpoints |
| **Module** | 16 — External / Institution Interaction |

### Description
If an approved external system sends AFS/reply metadata, operator maps it to an institution submission; checker confirms; staff then process as if portal-submitted.

### Business Objective
No silent back-door into paras/AFS.

### Actors
Applicant: Integration operator plus audit officer. Checker confirms linking. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Integration operator plus audit officer. Checker confirms linking.
2. How they create: Inbound event appears in Institution exchange inbox. Operator selects institution and target (AFS/reply), Save draft link.
3. How they edit: Draft link editable. After confirm, processed as F16-002/003 record.
4. How they send for approval: Submit link for checker.
5. How the approver sees pending items: Operator unmatched events; checker link inbox.
6. How the approver decides: Confirm link or reject event (quarantine).
7. How the applicant sees history: Event to submission mapping history.
8. How the approver sees history: Confirmed links.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own institution exchange event history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My institution exchange event register | Medium |
| Institution exchange event form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver institution exchange event inbox | Complex |
| Institution exchange event decision panel (approve / reject / return) | Medium |
| My institution exchange event history | Medium |
| Team institution exchange event history (approver) | Medium |
| Unmatched event inbox | Complex |
| Link form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft institution exchange event | Medium |
| Update draft institution exchange event | Medium |
| Submit institution exchange event for approval | Complex |
| Withdraw institution exchange event | Easy |
| Approver inbox query | Medium |
| Approve, reject or return institution exchange event | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Ingest event | Complex |
| Link to submission | Complex |

### Inputs
Inbound event, institution, target type, target record.

### Outputs
Persisted institution exchange event with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own institution exchange event.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Institution mandatory before confirm.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Payload stored as attachment.

### Reports
Unmatched events ageing.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

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
| My institution exchange event register | UI | Medium | 6 |
| Institution exchange event form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver institution exchange event inbox | UI | Complex | 12 |
| Institution exchange event decision panel (approve / reject / return) | UI | Medium | 6 |
| My institution exchange event history | UI | Medium | 6 |
| Team institution exchange event history (approver) | UI | Medium | 6 |
| Unmatched event inbox | UI | Complex | 12 |
| Link form | UI | Medium | 6 |
| Save draft institution exchange event | API | Medium | 6 |
| Update draft institution exchange event | API | Medium | 6 |
| Submit institution exchange event for approval | API | Complex | 8 |
| Withdraw institution exchange event | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return institution exchange event | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Ingest event | API | Complex | 8 |
| Link to submission | API | Complex | 8 |
| Institution exchange event record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on institution exchange event status change | Integration | Simple | 4 |
| Controlled External Integration Touchpoints feature tests | Testing | Complex | 8 |
| Controlled External Integration Touchpoints implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **153** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
