# F03-004 — Work Diary Submission

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Work Diary Submission |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
The staff member records work done for a date or week and submits it to the supervising Post for acknowledgement.

### Business Objective
Supervisors see field/office work without paper diaries.

### Actors
Applicant: Person mapped to a Post (typically field auditor or office staff required to file a diary). Approver: Person mapped to the supervising Post. Other: Auditor (read-only).

### User Journey
1. Who creates: Person mapped to a Post (typically field auditor or office staff required to file a diary).
2. How they create: Applicant opens My Work Diaries → New, selects period (date or week), enters work description, place of work, optional link to tour/audit assignment, Save draft.
3. How they edit: Draft or Returned diaries can be edited. Submitted/Acknowledged cannot be edited.
4. How they send for approval: Submit sends to supervising Post. Duplicate diary for the same Person and date is refused.
5. How the approver sees pending items: Supervisor opens Work Diary inbox (pending acknowledgement).
6. How the approver decides: Supervisor Acknowledge, Return for correction, or Record exception (with remarks). Acknowledge is not a financial approval.
7. How the applicant sees history: My Work Diary history with statuses and supervisor remarks.
8. How the approver sees history: Team diary history for supervised Posts.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own work diary history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My work diary register | Medium |
| Work diary form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver work diary inbox | Complex |
| Work diary decision panel (approve / reject / return) | Medium |
| My work diary history | Medium |
| Team work diary history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft work diary | Medium |
| Update draft work diary | Medium |
| Submit work diary for approval | Complex |
| Withdraw work diary | Easy |
| Approver inbox query | Medium |
| Approve, reject or return work diary | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Period, work description, place, linked assignment (optional), remarks.

### Outputs
Persisted work diary with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own work diary.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Period mandatory.
- Description mandatory.
- One diary per Person per date.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional supporting note.

### Reports
Diary compliance (submitted vs expected days).

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
| My work diary register | UI | Medium | 6 |
| Work diary form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver work diary inbox | UI | Complex | 12 |
| Work diary decision panel (approve / reject / return) | UI | Medium | 6 |
| My work diary history | UI | Medium | 6 |
| Team work diary history (approver) | UI | Medium | 6 |
| Save draft work diary | API | Medium | 6 |
| Update draft work diary | API | Medium | 6 |
| Submit work diary for approval | API | Complex | 8 |
| Withdraw work diary | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return work diary | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Work diary record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on work diary status change | Integration | Simple | 4 |
| Work Diary Submission feature tests | Testing | Complex | 8 |
| Work Diary Submission implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
