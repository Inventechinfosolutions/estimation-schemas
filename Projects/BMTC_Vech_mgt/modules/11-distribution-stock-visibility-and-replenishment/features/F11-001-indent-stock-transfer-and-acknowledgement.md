# F11-001 — Indent, Stock Transfer and Acknowledgement

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-001 |
| **Feature Name** | Indent, Stock Transfer and Acknowledgement |
| **Module** | 11 — Distribution, Stock Visibility and Replenishment |

### Description
Receiving location raises indent; Central Stores dispatches Stock Transfer; receiver acknowledges to complete the cycle and move stock.

### Business Objective
FR-S-10 to 13.

### Actors
Applicant: Depot/CWS Store Clerk raises indent. Central Stores clerk creates dispatch. Approver: Stores Officer approves indent/dispatch as configured. Receiving clerk acknowledges. Other: Auditor.

### User Journey
1. Who creates: Depot/CWS Store Clerk raises indent. Central Stores clerk creates dispatch.
2. How they create: Indent → New: destination, items, qty, Save draft. On approve, Central Stores → Dispatch: source, destination, qty, date, Save.
3. How they edit: Draft indent/dispatch editable. After acknowledge, reverse is a new return transfer.
4. How they send for approval: Indent submit to Stores Officer. Dispatch submit. Receiver Acknowledge.
5. How the approver sees pending items: Indent approval inbox; dispatch pending ack inbox at destination.
6. How the approver decides: Approve indent; Acknowledge receipt (or short-land with remarks).
7. How the applicant sees history: Indent and transfer timeline.
8. How the approver sees history: Approved/acked transfers.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own stock transfer history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My stock transfer register | Medium |
| Stock transfer form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver stock transfer inbox | Complex |
| Stock transfer decision panel (approve / reject / return) | Medium |
| My stock transfer history | Medium |
| Team stock transfer history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft stock transfer | Medium |
| Update draft stock transfer | Medium |
| Submit stock transfer for approval | Complex |
| Withdraw stock transfer | Easy |
| Approver inbox query | Medium |
| Approve, reject or return stock transfer | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Reduce source stock | Complex |
| Increase destination stock on ack | Complex |

### Inputs
Source, destination, item, qty, dates.

### Outputs
Persisted stock transfer with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own stock transfer.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Qty ≤ source stock.
- Source ≠ destination.

### Calculations
Stock moves only on acknowledgement.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Transfer note.

### Reports
In-transit stock.

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
| My stock transfer register | UI | Medium | 6 |
| Stock transfer form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver stock transfer inbox | UI | Complex | 12 |
| Stock transfer decision panel (approve / reject / return) | UI | Medium | 6 |
| My stock transfer history | UI | Medium | 6 |
| Team stock transfer history (approver) | UI | Medium | 6 |
| Save draft stock transfer | API | Medium | 6 |
| Update draft stock transfer | API | Medium | 6 |
| Submit stock transfer for approval | API | Complex | 8 |
| Withdraw stock transfer | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return stock transfer | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Reduce source stock | API | Complex | 8 |
| Increase destination stock on ack | API | Complex | 8 |
| Stock transfer record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on stock transfer status change | Integration | Simple | 4 |
| Indent, Stock Transfer and Acknowledgement feature tests | Testing | Complex | 8 |
| Indent, Stock Transfer and Acknowledgement implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **135** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
