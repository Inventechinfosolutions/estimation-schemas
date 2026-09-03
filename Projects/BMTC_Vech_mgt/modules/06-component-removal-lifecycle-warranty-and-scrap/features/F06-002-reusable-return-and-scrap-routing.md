# F06-002 — Reusable Return and Scrap Routing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Reusable Return and Scrap Routing |
| **Module** | 06 — Component Removal, Lifecycle, Warranty and Scrap |

### Description
On approved removal, Reusable items return to Depot Store serviceable stock; Scrap goes to Scrap Store with disposal/auction tracking.

### Business Objective
FR-M-16, FR-M-17, FR-X-04.

### Actors
Applicant: System proposes routing; Store Clerk confirms receipt into Depot Store or Scrap Store. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: System proposes routing; Store Clerk confirms receipt into Depot Store or Scrap Store.
2. How they create: From approved removal, routing screen shows destination store. Clerk confirms GR into that store.
3. How they edit: Cannot change condition after confirm; a new removal correction is required.
4. How they send for approval: Confirm receipt. Checker if scrap auction listing is raised.
5. How the approver sees pending items: Store Clerk inbound queue. Checker scrap-auction inbox if used.
6. How the approver decides: Confirm stock in; Checker may approve auction alert listing.
7. How the applicant sees history: Routing history on the item.
8. How the approver sees history: Confirmed receipts and auction alerts.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own stock routing history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My stock routing register | Medium |
| Stock routing form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver stock routing inbox | Complex |
| Stock routing decision panel (approve / reject / return) | Medium |
| My stock routing history | Medium |
| Team stock routing history (approver) | Medium |
| Routing confirmation | Medium |
| Scrap store register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft stock routing | Medium |
| Update draft stock routing | Medium |
| Submit stock routing for approval | Complex |
| Withdraw stock routing | Easy |
| Approver inbox query | Medium |
| Approve, reject or return stock routing | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Increase serviceable stock | Complex |
| Post to scrap store | Medium |

### Inputs
Destination store, qty, confirm datetime.

### Outputs
Persisted stock routing with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own stock routing.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Approved removal required.

### Calculations
Stock balances update.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Scrap register and auction alerts.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

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
| My stock routing register | UI | Medium | 6 |
| Stock routing form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver stock routing inbox | UI | Complex | 12 |
| Stock routing decision panel (approve / reject / return) | UI | Medium | 6 |
| My stock routing history | UI | Medium | 6 |
| Team stock routing history (approver) | UI | Medium | 6 |
| Routing confirmation | UI | Medium | 6 |
| Scrap store register | UI | Medium | 6 |
| Save draft stock routing | API | Medium | 6 |
| Update draft stock routing | API | Medium | 6 |
| Submit stock routing for approval | API | Complex | 8 |
| Withdraw stock routing | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return stock routing | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Increase serviceable stock | API | Complex | 8 |
| Post to scrap store | API | Medium | 6 |
| Stock routing record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on stock routing status change | Integration | Simple | 4 |
| Reusable Return and Scrap Routing feature tests | Testing | Complex | 8 |
| Reusable Return and Scrap Routing implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **145** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
