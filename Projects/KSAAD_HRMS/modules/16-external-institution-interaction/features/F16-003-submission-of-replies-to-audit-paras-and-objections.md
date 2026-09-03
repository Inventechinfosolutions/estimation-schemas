# F16-003 — Submission of Replies to Audit Paras and Objections

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-003 |
| **Feature Name** | Submission of Replies to Audit Paras and Objections |
| **Module** | 16 — External / Institution Interaction |

### Description
Institution user selects a para on an issued report, writes reply, attaches evidence, submits; audit officer receives it in F09-002.

### Business Objective
Formal institution reply.

### Actors
Applicant: Institution user with Reply function. Approver: Not approved by institution. KSAAD officer processes in F09-002. Institution may Withdraw before officer starts processing. Other: Institution Administrator. Auditor.

### User Journey
1. Who creates: Institution user with Reply function.
2. How they create: Portal → Paras → select para → Reply, text + attachments, Save draft.
3. How they edit: Draft/Returned (by KSAAD) editable. After Submit, freeze until KSAAD Return.
4. How they send for approval: Submit reply. Staff F09-002 inbox gets the item.
5. How the approver sees pending items: Institution sees Returned replies. Staff see new replies in F09-002.
6. How the approver decides: Institution does not approve. KSAAD Return/accept-for-processing is F09-002.
7. How the applicant sees history: All replies on each para.
8. How the approver sees history: Staff history in F09-002.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own institution para reply history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My institution para reply register | Medium |
| Institution para reply form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver institution para reply inbox | Complex |
| Institution para reply decision panel (approve / reject / return) | Medium |
| My institution para reply history | Medium |
| Team institution para reply history (approver) | Medium |
| Institution para list | Medium |
| Reply form | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft institution para reply | Medium |
| Update draft institution para reply | Medium |
| Submit institution para reply for approval | Complex |
| Withdraw institution para reply | Easy |
| Approver inbox query | Medium |
| Approve, reject or return institution para reply | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Para, reply text, attachments.

### Outputs
Persisted institution para reply with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own institution para reply.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Para must be issued to this institution.
- Text or attachment required.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Reply evidence.

### Reports
Paras without reply (staff).

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
| My institution para reply register | UI | Medium | 6 |
| Institution para reply form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver institution para reply inbox | UI | Complex | 12 |
| Institution para reply decision panel (approve / reject / return) | UI | Medium | 6 |
| My institution para reply history | UI | Medium | 6 |
| Team institution para reply history (approver) | UI | Medium | 6 |
| Institution para list | UI | Medium | 6 |
| Reply form | UI | Complex | 12 |
| Save draft institution para reply | API | Medium | 6 |
| Update draft institution para reply | API | Medium | 6 |
| Submit institution para reply for approval | API | Complex | 8 |
| Withdraw institution para reply | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return institution para reply | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Institution para reply record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on institution para reply status change | Integration | Simple | 4 |
| Submission of Replies to Audit Paras and Objections feature tests | Testing | Complex | 8 |
| Submission of Replies to Audit Paras and Objections implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
