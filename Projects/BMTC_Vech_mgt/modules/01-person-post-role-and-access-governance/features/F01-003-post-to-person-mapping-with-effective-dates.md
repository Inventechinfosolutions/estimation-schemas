# F01-003 — Post-to-Person Mapping with Effective Dates

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-003 |
| **Feature Name** | Post-to-Person Mapping with Effective Dates |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Administrator maps a Person to a Post with effective dates; Checker approves before login under that Post.

### Business Objective
A Person acts only in currently mapped Posts.

### Actors
Applicant: Access Administrator. Approver: Access Checker. Other: The mapped Person. Auditor.

### User Journey
1. Who creates: Access Administrator.
2. How they create: Mapping register → New: Person, Post, effective from, optional to, reason, Save draft.
3. How they edit: Draft/Returned editable. Approved current mapping is ended by effective-to or a new mapping, not silent overwrite.
4. How they send for approval: Submit. Checker must approve before the Person can select that Post at login.
5. How the approver sees pending items: Checker mapping inbox by unit.
6. How the approver decides: Approve or reject.
7. How the applicant sees history: History by Person and by Post.
8. How the approver sees history: Same for checker/auditor.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own Post-to-Person mapping history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My Post-to-Person mapping register | Medium |
| Post-to-person mapping form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver Post-to-Person mapping inbox | Complex |
| Post-to-person mapping decision panel (approve / reject / return) | Medium |
| My Post-to-Person mapping history | Medium |
| Team Post-to-Person mapping history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft Post-to-Person mapping | Medium |
| Update draft Post-to-Person mapping | Medium |
| Submit Post-to-Person mapping for approval | Complex |
| Withdraw Post-to-Person mapping | Easy |
| Approver inbox query | Medium |
| Approve, reject or return Post-to-Person mapping | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Check mapping overlap | Medium |

### Inputs
Person, Post, effective from/to, reason.

### Outputs
Persisted Post-to-Person mapping with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own Post-to-Person mapping.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Person and Post mandatory.
- Overlap on the same Post refused.

### Calculations
None beyond effective-date overlap.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional office order.

### Reports
Current holders by unit.

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
| My Post-to-Person mapping register | UI | Medium | 6 |
| Post-to-person mapping form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver Post-to-Person mapping inbox | UI | Complex | 12 |
| Post-to-person mapping decision panel (approve / reject / return) | UI | Medium | 6 |
| My Post-to-Person mapping history | UI | Medium | 6 |
| Team Post-to-Person mapping history (approver) | UI | Medium | 6 |
| Save draft Post-to-Person mapping | API | Medium | 6 |
| Update draft Post-to-Person mapping | API | Medium | 6 |
| Submit Post-to-Person mapping for approval | API | Complex | 8 |
| Withdraw Post-to-Person mapping | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return Post-to-Person mapping | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Check mapping overlap | API | Medium | 6 |
| Post-to-person mapping record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on Post-to-Person mapping status change | Integration | Simple | 4 |
| Post-to-Person Mapping with Effective Dates feature tests | Testing | Complex | 8 |
| Post-to-Person Mapping with Effective Dates implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
