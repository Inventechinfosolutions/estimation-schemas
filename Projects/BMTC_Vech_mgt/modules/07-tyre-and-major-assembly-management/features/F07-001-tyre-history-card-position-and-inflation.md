# F07-001 — Tyre History Card, Position and Inflation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Tyre History Card, Position and Inflation |
| **Module** | 07 — Tyre and Major Assembly Management |

### Description
Tyre Clerk records fitment/removal per tyre with wheel position and cumulative KM across vehicles and retreads; records inflation readings.

### Business Objective
FR-M-24, FR-M-25.

### Actors
Applicant: Tyre section clerk / mechanic. Tech. Supervisor reviews. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Tyre section clerk / mechanic. Tech. Supervisor reviews.
2. How they create: Tyre register → New tyre ID or open card → Fitment: vehicle, position (FL/FR/RLI/RLO/RRI/RRO/Spare), KM, Save. Inflation: pressure, date, location, Save.
3. How they edit: Draft events editable. Posted events reversed with a new event.
4. How they send for approval: Fitment/removal may require supervisor confirm. Inflation save can be direct.
5. How the approver sees pending items: Supervisor tyre inbox for fitment/removal.
6. How the approver decides: Confirm fitment/removal or return.
7. How the applicant sees history: Tyre history card.
8. How the approver sees history: Confirmed events.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own tyre event history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tyre event register | Medium |
| Tyre event form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver tyre event inbox | Complex |
| Tyre event decision panel (approve / reject / return) | Medium |
| My tyre event history | Medium |
| Team tyre event history (approver) | Medium |
| Tyre history card | Complex |
| Position diagram / selector | Medium |
| Inflation entry | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft tyre event | Medium |
| Update draft tyre event | Medium |
| Submit tyre event for approval | Complex |
| Withdraw tyre event | Easy |
| Approver inbox query | Medium |
| Approve, reject or return tyre event | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record tyre fitment/removal | Complex |
| Record inflation | Easy |

### Inputs
Tyre ID, vehicle, position, KM, pressure, location, dates.

### Outputs
Persisted tyre event with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own tyre event.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Position from the RFP list.
- Tyre ID unique.

### Calculations
Cumulative KM across vehicles and retread cycles.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Tyre Fitment & History Report.

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
| My tyre event register | UI | Medium | 6 |
| Tyre event form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver tyre event inbox | UI | Complex | 12 |
| Tyre event decision panel (approve / reject / return) | UI | Medium | 6 |
| My tyre event history | UI | Medium | 6 |
| Team tyre event history (approver) | UI | Medium | 6 |
| Tyre history card | UI | Complex | 12 |
| Position diagram / selector | UI | Medium | 6 |
| Inflation entry | UI | Easy | 4 |
| Save draft tyre event | API | Medium | 6 |
| Update draft tyre event | API | Medium | 6 |
| Submit tyre event for approval | API | Complex | 8 |
| Withdraw tyre event | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return tyre event | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record tyre fitment/removal | API | Complex | 8 |
| Record inflation | API | Easy | 4 |
| Tyre event record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on tyre event status change | Integration | Simple | 4 |
| Tyre History Card, Position and Inflation feature tests | Testing | Complex | 8 |
| Tyre History Card, Position and Inflation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **153** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
