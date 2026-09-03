# F05-003 — Evidence Upload and Claim Validation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Evidence Upload and Claim Validation |
| **Module** | 05 — HRMS Tour, Travel & TA/DA Claims |

### Description
Applicant attaches bills/tickets to the draft claim, system validates completeness, then applicant submits for approval.

### Business Objective
No submit without required evidence.

### Actors
Applicant: Same Person as the claim. Approver: Supervising Post receives the claim only after this Submit. Other: Auditor.

### User Journey
1. Who creates: Same Person as the claim.
2. How they create: Applicant opens the draft claim → Evidence, uploads tickets/bills, maps each to a claim line, Save.
3. How they edit: Can replace/delete attachments while Draft/Returned. After Submit, pack is frozen.
4. How they send for approval: Submit Claim runs validations (mandatory docs per head, amounts vs bills). On pass, status Submitted → F05-004 inbox.
5. How the approver sees pending items: Not the approver yet beyond seeing Submitted in F05-004. Validation failures stay with the applicant as an on-screen list.
6. How the approver decides: System pass/fail on Submit; no human approve here.
7. How the applicant sees history: Evidence versions and submit attempts.
8. How the approver sees history: Approver in F05-004 sees the frozen pack.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own TA/DA evidence pack history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My TA/DA evidence pack register | Medium |
| Ta/da evidence pack form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver TA/DA evidence pack inbox | Complex |
| Ta/da evidence pack decision panel (approve / reject / return) | Medium |
| My TA/DA evidence pack history | Medium |
| Team TA/DA evidence pack history (approver) | Medium |
| Evidence mapping grid | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft TA/DA evidence pack | Medium |
| Update draft TA/DA evidence pack | Medium |
| Submit TA/DA evidence pack for approval | Complex |
| Withdraw TA/DA evidence pack | Easy |
| Approver inbox query | Medium |
| Approve, reject or return TA/DA evidence pack | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Validate claim completeness | Complex |

### Inputs
Claim, attachments, line mapping.

### Outputs
Persisted TA/DA evidence pack with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own TA/DA evidence pack.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Required document types per head.
- Submit blocked if any debit line has no evidence when policy requires it.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Tickets, boarding passes, bills via DMS.

### Reports
Claims blocked for missing evidence.

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
| My TA/DA evidence pack register | UI | Medium | 6 |
| Ta/da evidence pack form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver TA/DA evidence pack inbox | UI | Complex | 12 |
| Ta/da evidence pack decision panel (approve / reject / return) | UI | Medium | 6 |
| My TA/DA evidence pack history | UI | Medium | 6 |
| Team TA/DA evidence pack history (approver) | UI | Medium | 6 |
| Evidence mapping grid | UI | Complex | 12 |
| Save draft TA/DA evidence pack | API | Medium | 6 |
| Update draft TA/DA evidence pack | API | Medium | 6 |
| Submit TA/DA evidence pack for approval | API | Complex | 8 |
| Withdraw TA/DA evidence pack | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return TA/DA evidence pack | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Validate claim completeness | API | Complex | 8 |
| Ta/da evidence pack record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on TA/DA evidence pack status change | Integration | Simple | 4 |
| Evidence Upload and Claim Validation feature tests | Testing | Complex | 8 |
| Evidence Upload and Claim Validation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **139** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
