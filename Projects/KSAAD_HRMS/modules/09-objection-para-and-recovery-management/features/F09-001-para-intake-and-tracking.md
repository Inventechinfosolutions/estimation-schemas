# F09-001 — Para Intake and Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Para Intake and Tracking |
| **Module** | 09 — Objection, Para & Recovery Management |

### Description
Officer registers a para from the issued report (or supplementary); in-charge/supervisor confirms classification; history on the para.

### Business Objective
Every para is a tracked record.

### Actors
Applicant: Audit officer / in-charge creates paras from accepted observations or after issue. Approver: Supervising Post confirms classification/amount if checker required. Other: Institution (replies in F16-003). Auditor.

### User Journey
1. Who creates: Audit officer / in-charge creates paras from accepted observations or after issue.
2. How they create: Opens assignment/report → Paras → New: number, title, amount, type, Save draft.
3. How they edit: Draft/Returned editable. After confirm, amount changes are a checked amendment.
4. How they send for approval: Submit for classification confirm.
5. How the approver sees pending items: Supervisor para inbox.
6. How the approver decides: Confirm or return.
7. How the applicant sees history: Para timeline.
8. How the approver sees history: Confirmed paras.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit para history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit para register | Medium |
| Audit para form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver audit para inbox | Complex |
| Audit para decision panel (approve / reject / return) | Medium |
| My audit para history | Medium |
| Team audit para history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit para | Medium |
| Update draft audit para | Medium |
| Submit audit para for approval | Complex |
| Withdraw audit para | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit para | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Para number, title, amount, type, linked observation.

### Outputs
Persisted audit para with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit para.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Title mandatory.
- Linked issued report when policy requires.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Extract from report.

### Reports
Para register.

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
| My audit para register | UI | Medium | 6 |
| Audit para form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit para inbox | UI | Complex | 12 |
| Audit para decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit para history | UI | Medium | 6 |
| Team audit para history (approver) | UI | Medium | 6 |
| Save draft audit para | API | Medium | 6 |
| Update draft audit para | API | Medium | 6 |
| Submit audit para for approval | API | Complex | 8 |
| Withdraw audit para | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit para | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Audit para record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit para status change | Integration | Simple | 4 |
| Para Intake and Tracking feature tests | Testing | Complex | 8 |
| Para Intake and Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
