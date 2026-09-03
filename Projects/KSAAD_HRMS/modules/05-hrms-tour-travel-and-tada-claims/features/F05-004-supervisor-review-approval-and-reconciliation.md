# F05-004 — Supervisor Review, Approval and Reconciliation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-004 |
| **Feature Name** | Supervisor Review, Approval and Reconciliation |
| **Module** | 05 — HRMS Tour, Travel & TA/DA Claims |

### Description
Supervisor sees submitted claims, reviews lines and evidence, approves/rejects/returns, and reconciles against advances.

### Business Objective
Decision and reconciliation with full history.

### Actors
Applicant: Traveller who submitted (cannot approve). Approver: Supervising Post (or accounts Post if template splits financial concurrence). Other: Accounts officer (payment staging). Auditor.

### User Journey
1. Who creates: Traveller who submitted (cannot approve).
2. How they create: Approver does not create the claim. Opens Approver TA/DA inbox.
3. How they edit: Approver cannot edit lines; Return for correction if amounts are wrong.
4. How they send for approval: Already submitted. Approver decides.
5. How the approver sees pending items: Inbox of Submitted claims: Person, tour, total, submitted on.
6. How the approver decides: Approve (optionally adjust payable by recorded recovery of advance — not by silent line edit), Reject, or Return. Remarks mandatory on Reject/Return.
7. How the applicant sees history: Claim timeline including payment-ready flag after approve.
8. How the approver sees history: Decided claims and reconciliation notes.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own TA/DA approval history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My TA/DA approval register | Medium |
| Ta/da approval form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver TA/DA approval inbox | Complex |
| Ta/da approval decision panel (approve / reject / return) | Medium |
| My TA/DA approval history | Medium |
| Team TA/DA approval history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft TA/DA approval | Medium |
| Update draft TA/DA approval | Medium |
| Submit TA/DA approval for approval | Complex |
| Withdraw TA/DA approval | Easy |
| Approver inbox query | Medium |
| Approve, reject or return TA/DA approval | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Set approved payable | Complex |

### Inputs
Decision, approved payable, advance recovery, remarks.

### Outputs
Persisted TA/DA approval with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own TA/DA approval.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Cannot approve above claimed total without a recorded exception reason.

### Calculations
Payable = claimed total − advance recovery − rejected lines (if return-not-used and lines marked not payable).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Evidence pack from F05-003 (read-only).

### Reports
Approved TA/DA by office; pending ageing.

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
| My TA/DA approval register | UI | Medium | 6 |
| Ta/da approval form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver TA/DA approval inbox | UI | Complex | 12 |
| Ta/da approval decision panel (approve / reject / return) | UI | Medium | 6 |
| My TA/DA approval history | UI | Medium | 6 |
| Team TA/DA approval history (approver) | UI | Medium | 6 |
| Save draft TA/DA approval | API | Medium | 6 |
| Update draft TA/DA approval | API | Medium | 6 |
| Submit TA/DA approval for approval | API | Complex | 8 |
| Withdraw TA/DA approval | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return TA/DA approval | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Set approved payable | API | Complex | 8 |
| Ta/da approval record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on TA/DA approval status change | Integration | Simple | 4 |
| Supervisor Review, Approval and Reconciliation feature tests | Testing | Complex | 8 |
| Supervisor Review, Approval and Reconciliation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **127** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
