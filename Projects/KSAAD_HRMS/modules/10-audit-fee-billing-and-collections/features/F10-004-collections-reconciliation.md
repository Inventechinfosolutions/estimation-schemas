# F10-004 — Collections Reconciliation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-004 |
| **Feature Name** | Collections Reconciliation |
| **Module** | 10 — Audit Fee, Billing and Collections |

### Description
Accounts records receipts against bills, reconciles, submits mismatch for checker; institution sees paid/outstanding.

### Business Objective
Outstanding fee is a calculated fact.

### Actors
Applicant: Accounts officer records receipt. Approver: Accounts checker on unmatched or excess receipts. Other: Institution. Auditor.

### User Journey
1. Who creates: Accounts officer records receipt.
2. How they create: Opens bill → Record receipt: amount, date, instrument, Save.
3. How they edit: Wrong receipt is reversed by a reversing entry, not overwritten.
4. How they send for approval: Matched full payment auto-closes outstanding. Excess/short goes to checker inbox.
5. How the approver sees pending items: Checker unmatched receipts inbox.
6. How the approver decides: Allocate to bill, return to officer, or hold.
7. How the applicant sees history: Receipts and outstanding on the bill.
8. How the approver sees history: Reconciliation decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own fee collection receipt history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My fee collection receipt register | Medium |
| Fee collection receipt form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver fee collection receipt inbox | Complex |
| Fee collection receipt decision panel (approve / reject / return) | Medium |
| My fee collection receipt history | Medium |
| Team fee collection receipt history (approver) | Medium |
| Receipt form | Medium |
| Unmatched inbox | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft fee collection receipt | Medium |
| Update draft fee collection receipt | Medium |
| Submit fee collection receipt for approval | Complex |
| Withdraw fee collection receipt | Easy |
| Approver inbox query | Medium |
| Approve, reject or return fee collection receipt | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Allocate receipt to bill | Complex |

### Inputs
Bill, amount, date, instrument.

### Outputs
Persisted fee collection receipt with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own fee collection receipt.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount > 0.
- Bill must be dispatched unless advance policy.

### Calculations
Outstanding = billed − allocated receipts + reversals.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Challan scan.

### Reports
Outstanding fee.

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
| My fee collection receipt register | UI | Medium | 6 |
| Fee collection receipt form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver fee collection receipt inbox | UI | Complex | 12 |
| Fee collection receipt decision panel (approve / reject / return) | UI | Medium | 6 |
| My fee collection receipt history | UI | Medium | 6 |
| Team fee collection receipt history (approver) | UI | Medium | 6 |
| Receipt form | UI | Medium | 6 |
| Unmatched inbox | UI | Medium | 6 |
| Save draft fee collection receipt | API | Medium | 6 |
| Update draft fee collection receipt | API | Medium | 6 |
| Submit fee collection receipt for approval | API | Complex | 8 |
| Withdraw fee collection receipt | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return fee collection receipt | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Allocate receipt to bill | API | Complex | 8 |
| Fee collection receipt record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on fee collection receipt status change | Integration | Simple | 4 |
| Collections Reconciliation feature tests | Testing | Complex | 8 |
| Collections Reconciliation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **139** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
