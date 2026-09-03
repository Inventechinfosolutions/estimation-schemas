# F04-002 — Daily KM Entry and AVLS KM

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Daily KM Entry and AVLS KM |
| **Module** | 04 — Vehicle Master, KM and Fleet History |

### Description
Statistical clerk enters starting progressive KM; later KM is added from AVLS. Manual entry remains for exceptions. Used for PM due KM.

### Business Objective
KM that drives docking/10-day schedules.

### Actors
Applicant: Statistical clerk at the depot. System applies AVLS increments when the feed is available. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Statistical clerk at the depot. System applies AVLS increments when the feed is available.
2. How they create: KM register for a date/depot → enter starting progressive KM per bus, or run AVLS fetch, Save.
3. How they edit: Corrections before freeze. Frozen days require a checked amendment.
4. How they send for approval: Day freeze may go to Depot Manager checker if configured.
5. How the approver sees pending items: Checker freeze inbox. AVLS fetch has no inbox.
6. How the approver decides: Approve freeze or return.
7. How the applicant sees history: KM history per vehicle.
8. How the approver sees history: Freeze decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own KM reading history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My KM reading register | Medium |
| Km reading form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver KM reading inbox | Complex |
| Km reading decision panel (approve / reject / return) | Medium |
| My KM reading history | Medium |
| Team KM reading history (approver) | Medium |
| Daily KM grid | Complex |
| AVLS fetch confirmation | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft KM reading | Medium |
| Update draft KM reading | Medium |
| Submit KM reading for approval | Complex |
| Withdraw KM reading | Easy |
| Approver inbox query | Medium |
| Approve, reject or return KM reading | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Save daily KM | Medium |
| Fetch AVLS KM | Very High |

### Inputs
Vehicle, date, KM, source (manual/AVLS).

### Outputs
Persisted KM reading with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own KM reading.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- KM not less than last accepted progressive KM without reason.

### Calculations
Progressive KM = last + AVLS delta or entered value.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
KM register by depot.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
AVLS KM feed

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
| My KM reading register | UI | Medium | 6 |
| Km reading form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver KM reading inbox | UI | Complex | 12 |
| Km reading decision panel (approve / reject / return) | UI | Medium | 6 |
| My KM reading history | UI | Medium | 6 |
| Team KM reading history (approver) | UI | Medium | 6 |
| Daily KM grid | UI | Complex | 12 |
| AVLS fetch confirmation | UI | Easy | 4 |
| Save draft KM reading | API | Medium | 6 |
| Update draft KM reading | API | Medium | 6 |
| Submit KM reading for approval | API | Complex | 8 |
| Withdraw KM reading | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return KM reading | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Save daily KM | API | Medium | 6 |
| Fetch AVLS KM | API | Very High | 16 |
| Km reading record, status history and attachments metadata | DB | Medium | 4 |
| AVLS KM feed | Integration | Medium | 16 |
| Daily KM Entry and AVLS KM feature tests | Testing | Complex | 8 |
| Daily KM Entry and AVLS KM implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **169** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
