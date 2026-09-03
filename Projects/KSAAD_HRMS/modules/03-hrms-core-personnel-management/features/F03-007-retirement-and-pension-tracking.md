# F03-007 — Retirement and Pension Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-007 |
| **Feature Name** | Retirement and Pension Tracking |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
HR opens a retirement case from the Person's service dates; the case is submitted through establishment approvals; pension checklist progress is recorded.

### Business Objective
Track retirement milestones without running a full pension disbursement engine unless later ordered.

### Actors
Applicant: HR Establishment Officer creates the case when the Person is within the configured notice window of superannuation (or on voluntary retirement request). Approver: Establishment supervisor / competent Post per template. Other: The retiring Person (read of their case status). Auditor.

### User Journey
1. Who creates: HR Establishment Officer creates the case when the Person is within the configured notice window of superannuation (or on voluntary retirement request).
2. How they create: Officer opens Retirement register → New, selects Person; system fills likely retirement date from service data; officer confirms type (superannuation / VRS), Save draft.
3. How they edit: Draft/Returned cases editable. After Submit, checklist items are updated without changing identity fields.
4. How they send for approval: Submit for establishment approval of the case opening. Later checklist completions may be maker–checker per item.
5. How the approver sees pending items: Approver retirement-case inbox.
6. How the approver decides: Approve case opening or reject. Officer then ticks checklist (pension papers, NOC) with dates; checker may confirm completed items.
7. How the applicant sees history: Officer and Person see case timeline and checklist history.
8. How the approver sees history: Approver sees cases decided and pending checklist ageing.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own retirement case history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My retirement case register | Medium |
| Retirement case form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver retirement case inbox | Complex |
| Retirement case decision panel (approve / reject / return) | Medium |
| My retirement case history | Medium |
| Team retirement case history (approver) | Medium |
| Retirement checklist panel | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft retirement case | Medium |
| Update draft retirement case | Medium |
| Submit retirement case for approval | Complex |
| Withdraw retirement case | Easy |
| Approver inbox query | Medium |
| Approve, reject or return retirement case | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Update checklist item | Medium |

### Inputs
Person, retirement type, retirement date, checklist items, remarks.

### Outputs
Persisted retirement case with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own retirement case.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Does not itself calculate pension amounts unless a later ordered interface exists.
- Person is not auto-deactivated; leaver is F01-007 on the retirement date.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Person mandatory.
- Retirement date mandatory.

### Calculations
Notice window = retirement date − configured months; case can be opened when today is inside the window.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Pension papers checklist attachments.

### Reports
Upcoming retirements; pending checklist.

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
| My retirement case register | UI | Medium | 6 |
| Retirement case form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver retirement case inbox | UI | Complex | 12 |
| Retirement case decision panel (approve / reject / return) | UI | Medium | 6 |
| My retirement case history | UI | Medium | 6 |
| Team retirement case history (approver) | UI | Medium | 6 |
| Retirement checklist panel | UI | Complex | 12 |
| Save draft retirement case | API | Medium | 6 |
| Update draft retirement case | API | Medium | 6 |
| Submit retirement case for approval | API | Complex | 8 |
| Withdraw retirement case | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return retirement case | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Update checklist item | API | Medium | 6 |
| Retirement case record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on retirement case status change | Integration | Simple | 4 |
| Retirement and Pension Tracking feature tests | Testing | Complex | 8 |
| Retirement and Pension Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
