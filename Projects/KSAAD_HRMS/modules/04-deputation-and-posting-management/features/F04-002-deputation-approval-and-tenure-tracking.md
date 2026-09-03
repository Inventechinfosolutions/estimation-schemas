# F04-002 — Deputation Approval and Tenure Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Deputation Approval and Tenure Tracking |
| **Module** | 04 — Deputation & Posting Management |

### Description
Competent Post approves or rejects the proposal; on approve, tenure is stored and mapping/vacancy updates are triggered.

### Business Objective
Governed approval with a tracked tenure.

### Actors
Applicant: The officer who submitted the proposal (F04-001) — they do not re-create it; they wait. HR may resubmit after Return. Approver: Competent deputation Post. Other: Person on deputation. Auditor.

### User Journey
1. Who creates: The officer who submitted the proposal (F04-001) — they do not re-create it; they wait. HR may resubmit after Return.
2. How they create: Approver does not create the proposal. They open it from the inbox (created in F04-001).
3. How they edit: Approver cannot silently change target Post; they Return for correction if wrong.
4. How they send for approval: Already submitted in F04-001. Approver acts on Submitted items.
5. How the approver sees pending items: Approver inbox: Submitted deputation proposals with Person, from/to Post, dates.
6. How the approver decides: Approve (records tenure start/end, notifies HR to apply mapping via F04-004) or Reject/Return with remarks.
7. How the applicant sees history: HR and Person see approval timeline and tenure clock.
8. How the approver sees history: Approver sees decided cases and active tenures they approved.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own deputation approval history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My deputation approval register | Medium |
| Deputation approval form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver deputation approval inbox | Complex |
| Deputation approval decision panel (approve / reject / return) | Medium |
| My deputation approval history | Medium |
| Team deputation approval history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft deputation approval | Medium |
| Update draft deputation approval | Medium |
| Submit deputation approval for approval | Complex |
| Withdraw deputation approval | Easy |
| Approver inbox query | Medium |
| Approve, reject or return deputation approval | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record tenure on approval | Medium |

### Inputs
Proposal reference, decision, tenure start/end, remarks.

### Outputs
Persisted deputation approval with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own deputation approval.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Cannot approve if target Post is missing.
- Cannot approve overlapping deputation for same Person.

### Calculations
Remaining tenure days = end date − today for Active deputations.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Approval order generated/attached.

### Reports
Active deputations and tenure ageing.

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
| My deputation approval register | UI | Medium | 6 |
| Deputation approval form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver deputation approval inbox | UI | Complex | 12 |
| Deputation approval decision panel (approve / reject / return) | UI | Medium | 6 |
| My deputation approval history | UI | Medium | 6 |
| Team deputation approval history (approver) | UI | Medium | 6 |
| Save draft deputation approval | API | Medium | 6 |
| Update draft deputation approval | API | Medium | 6 |
| Submit deputation approval for approval | API | Complex | 8 |
| Withdraw deputation approval | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return deputation approval | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record tenure on approval | API | Medium | 6 |
| Deputation approval record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on deputation approval status change | Integration | Simple | 4 |
| Deputation Approval and Tenure Tracking feature tests | Testing | Complex | 8 |
| Deputation Approval and Tenure Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
