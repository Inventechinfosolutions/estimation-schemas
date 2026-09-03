# F09-003 — Recovery Action Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Recovery Action Tracking |
| **Module** | 09 — Objection, Para & Recovery Management |

### Description
When disposal is recover, officer opens a recovery action, records demand and receipts, submits status to supervisor.

### Business Objective
Follow money after para disposal.

### Actors
Applicant: Audit/recovery officer. Approver: Supervising Post on status changes / closure proposal. Other: Accounts. Institution (fee-like visibility if configured). Auditor.

### User Journey
1. Who creates: Audit/recovery officer.
2. How they create: From para disposal Recover → New recovery action: demand amount, due date, Save.
3. How they edit: Record receipts as child events (not editing demand silently). Demand change is a checked amendment.
4. How they send for approval: Submit demand amendment or periodic status to supervisor.
5. How the approver sees pending items: Supervisor recovery inbox.
6. How the approver decides: Confirm demand/receipt or return.
7. How the applicant sees history: Demand, receipts, outstanding timeline.
8. How the approver sees history: Confirmed recovery events.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own recovery action history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My recovery action register | Medium |
| Recovery action form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver recovery action inbox | Complex |
| Recovery action decision panel (approve / reject / return) | Medium |
| My recovery action history | Medium |
| Team recovery action history (approver) | Medium |
| Receipt entry | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft recovery action | Medium |
| Update draft recovery action | Medium |
| Submit recovery action for approval | Complex |
| Withdraw recovery action | Easy |
| Approver inbox query | Medium |
| Approve, reject or return recovery action | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record recovery receipt | Medium |

### Inputs
Para, demand, receipt amount/date, outstanding.

### Outputs
Persisted recovery action with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own recovery action.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Demand > 0.
- Receipt ≤ outstanding.

### Calculations
Outstanding = demand − sum(receipts).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Challan/receipt scan.

### Reports
Outstanding recovery.

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
| My recovery action register | UI | Medium | 6 |
| Recovery action form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver recovery action inbox | UI | Complex | 12 |
| Recovery action decision panel (approve / reject / return) | UI | Medium | 6 |
| My recovery action history | UI | Medium | 6 |
| Team recovery action history (approver) | UI | Medium | 6 |
| Receipt entry | UI | Easy | 4 |
| Save draft recovery action | API | Medium | 6 |
| Update draft recovery action | API | Medium | 6 |
| Submit recovery action for approval | API | Complex | 8 |
| Withdraw recovery action | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return recovery action | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record recovery receipt | API | Medium | 6 |
| Recovery action record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on recovery action status change | Integration | Simple | 4 |
| Recovery Action Tracking feature tests | Testing | Complex | 8 |
| Recovery Action Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **129** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
