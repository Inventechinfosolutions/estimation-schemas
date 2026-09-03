# F10-003 — Invoice Dispatch and Status Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-003 |
| **Feature Name** | Invoice Dispatch and Status Tracking |
| **Module** | 10 — Audit Fee, Billing and Collections |

### Description
Officer dispatches an approved bill, records mode and date; status history is visible internally and to the institution.

### Business Objective
Know whether the bill was issued.

### Actors
Applicant: Accounts/despatch officer. Approver: Optional despatch checker. Other: Institution. Auditor.

### User Journey
1. Who creates: Accounts/despatch officer.
2. How they create: Opens approved bill → Dispatch: date, mode, addressee, Save.
3. How they edit: Correct dispatch only via checked amendment.
4. How they send for approval: Submit dispatch if checker required; else Save = dispatched.
5. How the approver sees pending items: Checker dispatch inbox if used.
6. How the approver decides: Confirm dispatch.
7. How the applicant sees history: Dispatch events on the bill.
8. How the approver sees history: Dispatch register.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own bill dispatch history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My bill dispatch register | Medium |
| Bill dispatch form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver bill dispatch inbox | Complex |
| Bill dispatch decision panel (approve / reject / return) | Medium |
| My bill dispatch history | Medium |
| Team bill dispatch history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft bill dispatch | Medium |
| Update draft bill dispatch | Medium |
| Submit bill dispatch for approval | Complex |
| Withdraw bill dispatch | Easy |
| Approver inbox query | Medium |
| Approve, reject or return bill dispatch | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Bill, dispatch date, mode, addressee.

### Outputs
Persisted bill dispatch with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own bill dispatch.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Bill approved.
- Dispatch date mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Despatch proof optional.

### Reports
Dispatched vs pending.

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
| My bill dispatch register | UI | Medium | 6 |
| Bill dispatch form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver bill dispatch inbox | UI | Complex | 12 |
| Bill dispatch decision panel (approve / reject / return) | UI | Medium | 6 |
| My bill dispatch history | UI | Medium | 6 |
| Team bill dispatch history (approver) | UI | Medium | 6 |
| Save draft bill dispatch | API | Medium | 6 |
| Update draft bill dispatch | API | Medium | 6 |
| Submit bill dispatch for approval | API | Complex | 8 |
| Withdraw bill dispatch | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return bill dispatch | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Bill dispatch record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on bill dispatch status change | Integration | Simple | 4 |
| Invoice Dispatch and Status Tracking feature tests | Testing | Complex | 8 |
| Invoice Dispatch and Status Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
