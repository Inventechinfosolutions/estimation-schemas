# F11-005 — Inventory Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-005 |
| **Feature Name** | Inventory Management |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Stores receives against PO, issues to office, adjusts stock with checker on write-off; stock and movement history.

### Business Objective
Stock from receipts and issues.

### Actors
Applicant: Stores clerk records GRN/issue. Write-off submitted to checker. Approver: Stores supervisor on write-off / adjustment. Other: Indenting office. Auditor.

### User Journey
1. Who creates: Stores clerk records GRN/issue. Write-off submitted to checker.
2. How they create: Receive: select PO → GRN qty, Save. Issue: select item/office → qty, Save. Adjustment: New write-off with reason.
3. How they edit: Same-day draft GRN editable. Posted movements reversed by contra entry.
4. How they send for approval: Write-off Submit to supervisor. Normal GRN/issue Save may be checker-free.
5. How the approver sees pending items: Supervisor adjustment inbox.
6. How the approver decides: Approve write-off or reject.
7. How the applicant sees history: Item ledger (receipts, issues, adjustments).
8. How the approver sees history: Approved write-offs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own inventory movement history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My inventory movement register | Medium |
| Inventory movement form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver inventory movement inbox | Complex |
| Inventory movement decision panel (approve / reject / return) | Medium |
| My inventory movement history | Medium |
| Team inventory movement history (approver) | Medium |
| GRN form | Medium |
| Issue form | Medium |
| Stock ledger | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft inventory movement | Medium |
| Update draft inventory movement | Medium |
| Submit inventory movement for approval | Complex |
| Withdraw inventory movement | Easy |
| Approver inbox query | Medium |
| Approve, reject or return inventory movement | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Post stock movement | Complex |

### Inputs
Item, qty, PO/indent, office, reason.

### Outputs
Persisted inventory movement with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own inventory movement.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Issue qty ≤ on-hand.
- GRN qty ≤ remaining PO qty.

### Calculations
On-hand = receipts − issues − write-offs.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
GRN/delivery note.

### Reports
Stock position.

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
| My inventory movement register | UI | Medium | 6 |
| Inventory movement form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver inventory movement inbox | UI | Complex | 12 |
| Inventory movement decision panel (approve / reject / return) | UI | Medium | 6 |
| My inventory movement history | UI | Medium | 6 |
| Team inventory movement history (approver) | UI | Medium | 6 |
| GRN form | UI | Medium | 6 |
| Issue form | UI | Medium | 6 |
| Stock ledger | UI | Complex | 12 |
| Save draft inventory movement | API | Medium | 6 |
| Update draft inventory movement | API | Medium | 6 |
| Submit inventory movement for approval | API | Complex | 8 |
| Withdraw inventory movement | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return inventory movement | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Post stock movement | API | Complex | 8 |
| Inventory movement record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on inventory movement status change | Integration | Simple | 4 |
| Inventory Management feature tests | Testing | Complex | 8 |
| Inventory Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
