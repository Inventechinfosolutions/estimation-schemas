# F07-003 — Auditor Resource Allocation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | Auditor Resource Allocation |
| **Module** | 07 — Audit Planning & Resource Allocation |

### Description
Planning officer assigns Persons (auditors) to a planned audit; supervising Post approves the allocation.

### Business Objective
Named team on a planned unit before field execution.

### Actors
Applicant: Audit Planning Officer / Audit Superintendent. Approver: Supervising Post / competent allocation Post. Other: Assigned auditors (see My allocations). Auditor of system.

### User Journey
1. Who creates: Audit Planning Officer / Audit Superintendent.
2. How they create: Opens an approved plan row → Allocate, picks Persons and role on the team (in-charge/member), dates, Save draft.
3. How they edit: Draft/Returned editable. After approve, change of member is a revision allocation.
4. How they send for approval: Submit allocation.
5. How the approver sees pending items: Approver allocation inbox.
6. How the approver decides: Approve or return. On approve, field execution (Module 08) can start for that assignment.
7. How the applicant sees history: Allocation history per institution/year.
8. How the approver sees history: Decided allocations.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own auditor allocation history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My auditor allocation register | Medium |
| Auditor allocation form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver auditor allocation inbox | Complex |
| Auditor allocation decision panel (approve / reject / return) | Medium |
| My auditor allocation history | Medium |
| Team auditor allocation history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft auditor allocation | Medium |
| Update draft auditor allocation | Medium |
| Submit auditor allocation for approval | Complex |
| Withdraw auditor allocation | Easy |
| Approver inbox query | Medium |
| Approve, reject or return auditor allocation | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Check Person already allocated overlapping dates | Medium |

### Inputs
Plan row, Persons, team role, assignment dates.

### Outputs
Persisted auditor allocation with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own auditor allocation.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- At least one in-charge.
- Persons must have current Post mapping.
- Dates within plan year.

### Calculations
None beyond overlap detection.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Auditor loading.

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
| My auditor allocation register | UI | Medium | 6 |
| Auditor allocation form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver auditor allocation inbox | UI | Complex | 12 |
| Auditor allocation decision panel (approve / reject / return) | UI | Medium | 6 |
| My auditor allocation history | UI | Medium | 6 |
| Team auditor allocation history (approver) | UI | Medium | 6 |
| Save draft auditor allocation | API | Medium | 6 |
| Update draft auditor allocation | API | Medium | 6 |
| Submit auditor allocation for approval | API | Complex | 8 |
| Withdraw auditor allocation | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return auditor allocation | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Check Person already allocated overlapping dates | API | Medium | 6 |
| Auditor allocation record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on auditor allocation status change | Integration | Simple | 4 |
| Auditor Resource Allocation feature tests | Testing | Complex | 8 |
| Auditor Resource Allocation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
