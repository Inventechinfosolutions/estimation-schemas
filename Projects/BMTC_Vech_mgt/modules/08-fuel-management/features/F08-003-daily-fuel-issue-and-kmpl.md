# F08-003 — Daily Fuel Issue and KMPL

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Daily Fuel Issue and KMPL |
| **Module** | 08 — Fuel Management |

### Description
Fuel clerk records daily HSD issue per bus with driver; system calculates KMPL and flags underperforming vehicles vs norms; averages by vehicle, driver, depot, model.

### Business Objective
FR-M-30, FR-M-31, FR-M-35.

### Actors
Applicant: Fuel Clerk. Statistical clerk may confirm KM. Mechanical Section configures KMPL thresholds. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Fuel Clerk. Statistical clerk may confirm KM. Mechanical Section configures KMPL thresholds.
2. How they create: Daily issue grid: bus, driver, HSD qty, Save. KM from F04-002.
3. How they edit: Same-day draft editable. After freeze, amendment request.
4. How they send for approval: Day freeze to Depot Manager if configured.
5. How the approver sees pending items: Checker freeze inbox. Threshold config has maker–checker.
6. How the approver decides: Approve freeze. Mechanical Section approves threshold changes.
7. How the applicant sees history: Issue history and KMPL by bus/driver.
8. How the approver sees history: Freeze and threshold history.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own fuel issue history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My fuel issue register | Medium |
| Fuel issue form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver fuel issue inbox | Complex |
| Fuel issue decision panel (approve / reject / return) | Medium |
| My fuel issue history | Medium |
| Team fuel issue history (approver) | Medium |
| Daily fuel issue grid | Complex |
| KMPL dashboard | Complex |
| Threshold configuration | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft fuel issue | Medium |
| Update draft fuel issue | Medium |
| Submit fuel issue for approval | Complex |
| Withdraw fuel issue | Easy |
| Approver inbox query | Medium |
| Approve, reject or return fuel issue | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Save fuel issue | Medium |
| Calculate KMPL | Complex |
| Flag underperforming KMPL | Medium |

### Inputs
Bus, driver, HSD qty, date.

### Outputs
Persisted fuel issue with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own fuel issue.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- AVLS KM is used when available; otherwise statistical clerk KM.
- Pre-bid: integrate with existing HPCL fuel software and remain able to add future PSU/vendor feeds.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Bus and qty mandatory.
- Driver mandatory.

### Calculations
KMPL = KM / HSD for the period. Flag if below standard. Averages by vehicle, driver, depot, model.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
KMPL reports (also Module 14).

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
HPCL fuel software and future PSU/vendor feeds

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
| My fuel issue register | UI | Medium | 6 |
| Fuel issue form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver fuel issue inbox | UI | Complex | 12 |
| Fuel issue decision panel (approve / reject / return) | UI | Medium | 6 |
| My fuel issue history | UI | Medium | 6 |
| Team fuel issue history (approver) | UI | Medium | 6 |
| Daily fuel issue grid | UI | Complex | 12 |
| KMPL dashboard | UI | Complex | 12 |
| Threshold configuration | UI | Medium | 6 |
| Save draft fuel issue | API | Medium | 6 |
| Update draft fuel issue | API | Medium | 6 |
| Submit fuel issue for approval | API | Complex | 8 |
| Withdraw fuel issue | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return fuel issue | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Save fuel issue | API | Medium | 6 |
| Calculate KMPL | API | Complex | 8 |
| Flag underperforming KMPL | API | Medium | 6 |
| Fuel issue record, status history and attachments metadata | DB | Medium | 4 |
| HPCL fuel software and future PSU/vendor feeds | Integration | Complex | 24 |
| Daily Fuel Issue and KMPL feature tests | Testing | Complex | 8 |
| Daily Fuel Issue and KMPL implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **189** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
