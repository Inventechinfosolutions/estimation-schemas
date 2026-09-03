# F04-003 — Vehicle Lifecycle, Transfer and History

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Vehicle Lifecycle, Transfer and History |
| **Module** | 04 — Vehicle Master, KM and Fleet History |

### Description
Fleet Administrator records induction, inter-depot transfer and scrap with auction alert; the vehicle history shows spares, services, transfers, warranty parts and accidents.

### Business Objective
Complete vehicle history (FR-M-21 to 23).

### Actors
Applicant: Fleet Administrator raises events. Depot Manager acknowledges incoming transfer. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Fleet Administrator raises events. Depot Manager acknowledges incoming transfer.
2. How they create: Vehicle → Lifecycle → New event: Transfer or Scrap, dates, destination depot or scrap reason, Save draft.
3. How they edit: Draft/Returned editable. History rows are not overwritten.
4. How they send for approval: Transfer/scrap submitted to Fleet Checker / Depot Manager of receiving depot.
5. How the approver sees pending items: Receiving Depot Manager inbox; Checker inbox for scrap.
6. How the approver decides: Acknowledge transfer or approve scrap (auction alert).
7. How the applicant sees history: Lifecycle timeline on the vehicle.
8. How the approver sees history: Decided events.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own vehicle lifecycle event history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My vehicle lifecycle event register | Medium |
| Vehicle lifecycle event form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver vehicle lifecycle event inbox | Complex |
| Vehicle lifecycle event decision panel (approve / reject / return) | Medium |
| My vehicle lifecycle event history | Medium |
| Team vehicle lifecycle event history (approver) | Medium |
| Vehicle history timeline | Complex |
| Assembly history panel | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft vehicle lifecycle event | Medium |
| Update draft vehicle lifecycle event | Medium |
| Submit vehicle lifecycle event for approval | Complex |
| Withdraw vehicle lifecycle event | Easy |
| Approver inbox query | Medium |
| Approve, reject or return vehicle lifecycle event | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record transfer | Complex |
| Record scrap with auction alert | Medium |

### Inputs
Event type, dates, from/to depot, remarks.

### Outputs
Persisted vehicle lifecycle event with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own vehicle lifecycle event.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Transfer requires destination depot.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Transfer/scrap order optional.

### Reports
Fleet allocation and scrap list.

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
| My vehicle lifecycle event register | UI | Medium | 6 |
| Vehicle lifecycle event form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver vehicle lifecycle event inbox | UI | Complex | 12 |
| Vehicle lifecycle event decision panel (approve / reject / return) | UI | Medium | 6 |
| My vehicle lifecycle event history | UI | Medium | 6 |
| Team vehicle lifecycle event history (approver) | UI | Medium | 6 |
| Vehicle history timeline | UI | Complex | 12 |
| Assembly history panel | UI | Medium | 6 |
| Save draft vehicle lifecycle event | API | Medium | 6 |
| Update draft vehicle lifecycle event | API | Medium | 6 |
| Submit vehicle lifecycle event for approval | API | Complex | 8 |
| Withdraw vehicle lifecycle event | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return vehicle lifecycle event | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record transfer | API | Complex | 8 |
| Record scrap with auction alert | API | Medium | 6 |
| Vehicle lifecycle event record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on vehicle lifecycle event status change | Integration | Simple | 4 |
| Vehicle Lifecycle, Transfer and History feature tests | Testing | Complex | 8 |
| Vehicle Lifecycle, Transfer and History implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
