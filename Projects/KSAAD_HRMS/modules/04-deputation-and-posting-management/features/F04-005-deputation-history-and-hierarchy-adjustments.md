# F04-005 — Deputation History and Hierarchy Adjustments

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Deputation History and Hierarchy Adjustments |
| **Module** | 04 — Deputation & Posting Management |

### Description
While on deputation, reporting hierarchy may temporarily follow the host Post. HR records that adjustment; checker approves; history is kept with the deputation.

### Business Objective
Approvals during deputation go to the right supervising Post.

### Actors
Applicant: HR Establishment Officer. Approver: HR Checker / Access Checker if it changes supervising Post used by Module 01. Other: Person. Auditor.

### User Journey
1. Who creates: HR Establishment Officer.
2. How they create: Officer opens deputation case → Hierarchy adjustment, selects temporary supervising Post at host office, effective period within tenure, Save draft.
3. How they edit: Draft/Returned editable. After approval, end-date on repatriation is automatic.
4. How they send for approval: Submit to checker. On approve, leave/diary/TA approvals use the temporary supervising Post.
5. How the approver sees pending items: Checker inbox of hierarchy adjustments.
6. How the approver decides: Approve or reject. Cannot overlap two temporary supervising Posts.
7. How the applicant sees history: Deputation case shows original vs temporary reporting, with dates.
8. How the approver sees history: Checker/auditor see all hierarchy adjustments.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own temporary reporting change history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My temporary reporting change register | Medium |
| Temporary reporting change form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver temporary reporting change inbox | Complex |
| Temporary reporting change decision panel (approve / reject / return) | Medium |
| My temporary reporting change history | Medium |
| Team temporary reporting change history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft temporary reporting change | Medium |
| Update draft temporary reporting change | Medium |
| Submit temporary reporting change for approval | Complex |
| Withdraw temporary reporting change | Easy |
| Approver inbox query | Medium |
| Approve, reject or return temporary reporting change | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Deputation, temporary supervising Post, effective from/to.

### Outputs
Persisted temporary reporting change with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own temporary reporting change.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Period inside tenure.
- Temporary Post exists.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Host office order optional.

### Reports
Persons with temporary reporting.

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
| My temporary reporting change register | UI | Medium | 6 |
| Temporary reporting change form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver temporary reporting change inbox | UI | Complex | 12 |
| Temporary reporting change decision panel (approve / reject / return) | UI | Medium | 6 |
| My temporary reporting change history | UI | Medium | 6 |
| Team temporary reporting change history (approver) | UI | Medium | 6 |
| Save draft temporary reporting change | API | Medium | 6 |
| Update draft temporary reporting change | API | Medium | 6 |
| Submit temporary reporting change for approval | API | Complex | 8 |
| Withdraw temporary reporting change | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return temporary reporting change | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Temporary reporting change record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on temporary reporting change status change | Integration | Simple | 4 |
| Deputation History and Hierarchy Adjustments feature tests | Testing | Complex | 8 |
| Deputation History and Hierarchy Adjustments implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
