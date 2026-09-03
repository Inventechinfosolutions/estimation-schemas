# F09-002 — Objection and Representation Reply Workflow

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Objection and Representation Reply Workflow |
| **Module** | 09 — Objection, Para & Recovery Management |

### Description
Institution reply (from Module 16) or internal representation is linked to a para; audit officer proposes disposal; competent Post decides.

### Business Objective
Controlled reply and disposal.

### Actors
Applicant: Audit officer processes the incoming reply. Institution creates the reply in F16-003. Approver: Competent disposal Post. Other: Institution (status). Auditor.

### User Journey
1. Who creates: Audit officer processes the incoming reply. Institution creates the reply in F16-003.
2. How they create: Officer opens para → Incoming replies, or New internal note, Save draft disposal proposal.
3. How they edit: Draft proposal editable. After Submit, freeze until Return.
4. How they send for approval: Submit proposed disposal (drop/sustain/recover) to competent Post.
5. How the approver sees pending items: Approver disposal inbox. Officer has inbox of new institution replies.
6. How the approver decides: Approve disposal, return, or modify by Return only.
7. How the applicant sees history: Reply and disposal timeline on the para.
8. How the approver sees history: Disposals decided.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own objection / representation history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My objection / representation register | Medium |
| Objection / representation form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver objection / representation inbox | Complex |
| Objection / representation decision panel (approve / reject / return) | Medium |
| My objection / representation history | Medium |
| Team objection / representation history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft objection / representation | Medium |
| Update draft objection / representation | Medium |
| Submit objection / representation for approval | Complex |
| Withdraw objection / representation | Easy |
| Approver inbox query | Medium |
| Approve, reject or return objection / representation | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Para, reply reference, proposed disposal, remarks.

### Outputs
Persisted objection / representation with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own objection / representation.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Para mandatory.
- Disposal type mandatory on submit.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Reply attachments from institution.

### Reports
Pending replies ageing.

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
| My objection / representation register | UI | Medium | 6 |
| Objection / representation form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver objection / representation inbox | UI | Complex | 12 |
| Objection / representation decision panel (approve / reject / return) | UI | Medium | 6 |
| My objection / representation history | UI | Medium | 6 |
| Team objection / representation history (approver) | UI | Medium | 6 |
| Save draft objection / representation | API | Medium | 6 |
| Update draft objection / representation | API | Medium | 6 |
| Submit objection / representation for approval | API | Complex | 8 |
| Withdraw objection / representation | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return objection / representation | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Objection / representation record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on objection / representation status change | Integration | Simple | 4 |
| Objection and Representation Reply Workflow feature tests | Testing | Complex | 8 |
| Objection and Representation Reply Workflow implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
