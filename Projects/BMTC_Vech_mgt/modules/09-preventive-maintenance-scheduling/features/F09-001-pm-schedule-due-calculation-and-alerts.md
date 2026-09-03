# F09-001 — PM Schedule, Due Calculation and Alerts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | PM Schedule, Due Calculation and Alerts |
| **Module** | 09 — Preventive Maintenance Scheduling |

### Description
System tracks EOC/Docking and 10-Day schedules with auto due date and due KM from last completed maintenance; statuses Upcoming / Due Today / Overdue / Completed; alerts to Tech. Supervisor and Depot Manager.

### Business Objective
FR-M-36 to 38.

### Actors
Applicant: System calculates dues. Tech. Supervisor confirms completion via job card type Preventive. Mechanical Section configures intervals. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: System calculates dues. Tech. Supervisor confirms completion via job card type Preventive. Mechanical Section configures intervals.
2. How they create: PM register shows all vehicles. Completion is posted when a Preventive job card is Completed (F05-003). Admin sets interval KM/days.
3. How they edit: Interval configuration is maker–checker. Due values are calculated, not typed.
4. How they send for approval: Interval change submitted to Mechanical Checker. Alerts fire automatically.
5. How the approver sees pending items: Supervisor/DM receive alert list (approaching due). Checker interval inbox.
6. How the approver decides: Checker approves interval change. Completion is the job-card sign-off.
7. How the applicant sees history: PM status history per vehicle.
8. How the approver sees history: Interval versions and alert log.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own PM schedule history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My PM schedule register | Medium |
| Pm schedule form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver PM schedule inbox | Complex |
| Pm schedule decision panel (approve / reject / return) | Medium |
| My PM schedule history | Medium |
| Team PM schedule history (approver) | Medium |
| PM schedule register | Complex |
| Interval configuration | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft PM schedule | Medium |
| Update draft PM schedule | Medium |
| Submit PM schedule for approval | Complex |
| Withdraw PM schedule | Easy |
| Approver inbox query | Medium |
| Approve, reject or return PM schedule | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Calculate due KM/date | Complex |
| Send PM approaching alerts | Medium |

### Inputs
Vehicle, last PM, interval KM/days, due KM/date, status.

### Outputs
Persisted PM schedule with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own PM schedule.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Pre-bid: auto-alerts to DM, DME and DC; frequency agreed with BMTC after award. Schedule usually Time and KM.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Interval > 0.

### Calculations
Due KM = last completed KM + interval KM. Due date = last date + interval days. Status from today vs due.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Preventive Maintenance Schedule Register.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Notify DM, DME, DC, Tech. Supervisor (SMS/email)

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
| My PM schedule register | UI | Medium | 6 |
| Pm schedule form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver PM schedule inbox | UI | Complex | 12 |
| Pm schedule decision panel (approve / reject / return) | UI | Medium | 6 |
| My PM schedule history | UI | Medium | 6 |
| Team PM schedule history (approver) | UI | Medium | 6 |
| PM schedule register | UI | Complex | 12 |
| Interval configuration | UI | Medium | 6 |
| Save draft PM schedule | API | Medium | 6 |
| Update draft PM schedule | API | Medium | 6 |
| Submit PM schedule for approval | API | Complex | 8 |
| Withdraw PM schedule | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return PM schedule | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Calculate due KM/date | API | Complex | 8 |
| Send PM approaching alerts | API | Medium | 6 |
| Pm schedule record, status history and attachments metadata | DB | Medium | 4 |
| Notify DM, DME, DC, Tech. Supervisor (SMS/email) | Integration | Easy | 8 |
| PM Schedule, Due Calculation and Alerts feature tests | Testing | Complex | 8 |
| PM Schedule, Due Calculation and Alerts implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **155** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
