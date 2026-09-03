# F07-004 — Gram Panchayat Adhoc and Non-Adhoc Committee Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Gram Panchayat Adhoc and Non-Adhoc Committee Tracking |
| **Module** | 07 — Audit Planning & Resource Allocation |

### Description
Officer records GP adhoc/non-adhoc committee composition and status updates; supervisor confirms; history per GP.

### Business Objective
Track GP committee updates required by the source.

### Actors
Applicant: LAC/audit officer captures updates. Supervising Post confirms if configured. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: LAC/audit officer captures updates. Supervising Post confirms if configured.
2. How they create: Opens GP committee register → select GP/institution → New update: committee type, members, date, status, Save.
3. How they edit: Draft editable. Confirmed updates are superseded by a new update, not overwritten.
4. How they send for approval: Submit for supervisor confirm when required.
5. How the approver sees pending items: Supervisor GP-update inbox.
6. How the approver decides: Confirm or return.
7. How the applicant sees history: Timeline of committee updates per GP.
8. How the approver sees history: Confirmed updates.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own GP committee update history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My GP committee update register | Medium |
| Gp committee update form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver GP committee update inbox | Complex |
| Gp committee update decision panel (approve / reject / return) | Medium |
| My GP committee update history | Medium |
| Team GP committee update history (approver) | Medium |
| GP committee register | Complex |
| Update form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft GP committee update | Medium |
| Update draft GP committee update | Medium |
| Submit GP committee update for approval | Complex |
| Withdraw GP committee update | Easy |
| Approver inbox query | Medium |
| Approve, reject or return GP committee update | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
GP/institution, committee type, members, status, date.

### Outputs
Persisted GP committee update with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own GP committee update.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- GP and type mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Committee notification attachment.

### Reports
GPs without current committee data.

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
| My GP committee update register | UI | Medium | 6 |
| Gp committee update form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver GP committee update inbox | UI | Complex | 12 |
| Gp committee update decision panel (approve / reject / return) | UI | Medium | 6 |
| My GP committee update history | UI | Medium | 6 |
| Team GP committee update history (approver) | UI | Medium | 6 |
| GP committee register | UI | Complex | 12 |
| Update form | UI | Medium | 6 |
| Save draft GP committee update | API | Medium | 6 |
| Update draft GP committee update | API | Medium | 6 |
| Submit GP committee update for approval | API | Complex | 8 |
| Withdraw GP committee update | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return GP committee update | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Gp committee update record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on GP committee update status change | Integration | Simple | 4 |
| Gram Panchayat Adhoc and Non-Adhoc Committee Tracking feature tests | Testing | Complex | 8 |
| Gram Panchayat Adhoc and Non-Adhoc Committee Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
