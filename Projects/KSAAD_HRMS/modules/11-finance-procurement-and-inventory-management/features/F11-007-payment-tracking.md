# F11-007 — Payment Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-007 |
| **Feature Name** | Payment Tracking |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Accounts prepares payment for approved expense/PO/TA/DA, submits to checker, records bank status; payee and auditor see history.

### Business Objective
Payment status is recorded, not informal.

### Actors
Applicant: Accounts officer. Approver: Accounts checker / DDO Post. Other: Payee staff (own TA/DA). Auditor.

### User Journey
1. Who creates: Accounts officer.
2. How they create: Select approved payable (expense/PO/TA) → New payment: amount, mode, beneficiary, Save draft.
3. How they edit: Draft editable. After Submit, status updates (sent/success/fail) are events, not edits of amount.
4. How they send for approval: Submit payment instruction.
5. How the approver sees pending items: Checker payment inbox.
6. How the approver decides: Approve to send. Officer later records bank reference / success / fail.
7. How the applicant sees history: Payment events on the source document.
8. How the approver sees history: Approved instructions and failures.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own payment instruction history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My payment instruction register | Medium |
| Payment instruction form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver payment instruction inbox | Complex |
| Payment instruction decision panel (approve / reject / return) | Medium |
| My payment instruction history | Medium |
| Team payment instruction history (approver) | Medium |
| Payment form | Medium |
| Bank status update | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft payment instruction | Medium |
| Update draft payment instruction | Medium |
| Submit payment instruction for approval | Complex |
| Withdraw payment instruction | Easy |
| Approver inbox query | Medium |
| Approve, reject or return payment instruction | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record bank status | Medium |

### Inputs
Source document, amount, mode, beneficiary, bank reference, status.

### Outputs
Persisted payment instruction with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own payment instruction.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount ≤ approved payable outstanding.
- Beneficiary mandatory.

### Calculations
Outstanding payable = approved − successful payments.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Payment advice.

### Reports
Payments pending/failed.

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
| My payment instruction register | UI | Medium | 6 |
| Payment instruction form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver payment instruction inbox | UI | Complex | 12 |
| Payment instruction decision panel (approve / reject / return) | UI | Medium | 6 |
| My payment instruction history | UI | Medium | 6 |
| Team payment instruction history (approver) | UI | Medium | 6 |
| Payment form | UI | Medium | 6 |
| Bank status update | UI | Easy | 4 |
| Save draft payment instruction | API | Medium | 6 |
| Update draft payment instruction | API | Medium | 6 |
| Submit payment instruction for approval | API | Complex | 8 |
| Withdraw payment instruction | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return payment instruction | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record bank status | API | Medium | 6 |
| Payment instruction record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on payment instruction status change | Integration | Simple | 4 |
| Payment Tracking feature tests | Testing | Complex | 8 |
| Payment Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **135** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
