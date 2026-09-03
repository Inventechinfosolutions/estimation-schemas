# F03-002 — Post and Vacancy Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Post and Vacancy Management |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
HR Establishment Officer maintains sanctioned strength vs occupied Posts (from Module 01 mappings) and vacancy.

### Business Objective
Show vacancy without duplicating the Post master.

### Actors
Applicant: HR Establishment Officer updates sanctioned numbers. Occupied count is derived from approved Post-to-Person mappings. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: HR Establishment Officer updates sanctioned numbers. Occupied count is derived from approved Post-to-Person mappings.
2. How they create: Officer opens Vacancy register by office/designation, enters sanctioned strength for that Post/designation, Save.
3. How they edit: Sanctioned strength changes are edited on the same register (checked if policy requires). Occupied is not typed; it comes from current mappings.
4. How they send for approval: If maker–checker is on, sanctioned-strength change is submitted to HR Checker. Occupied/vacant figures are calculated, not submitted.
5. How the approver sees pending items: HR Checker sees pending sanctioned-strength changes. There is no inbox for occupied counts.
6. How the approver decides: Checker approves sanctioned-strength change.
7. How the applicant sees history: Officer sees history of sanctioned-strength changes.
8. How the approver sees history: Checker/auditor see the same plus derived occupied snapshots in the vacancy report.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own vacancy position history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My vacancy position register | Medium |
| Vacancy position form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver vacancy position inbox | Complex |
| Vacancy position decision panel (approve / reject / return) | Medium |
| My vacancy position history | Medium |
| Team vacancy position history (approver) | Medium |
| Vacancy register (sanctioned vs occupied) | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft vacancy position | Medium |
| Update draft vacancy position | Medium |
| Submit vacancy position for approval | Complex |
| Withdraw vacancy position | Easy |
| Approver inbox query | Medium |
| Approve, reject or return vacancy position | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Derive occupied count from mappings | Medium |

### Inputs
Office, designation/Post, sanctioned strength, effective date.

### Outputs
Persisted vacancy position with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own vacancy position.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Occupied = count of current approved mappings to that Post.
- Vacant = sanctioned − occupied (not below zero without a warning).

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Sanctioned strength integer ≥ 0.

### Calculations
Occupied from F01-003; Vacant = sanctioned − occupied.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional sanction order.

### Reports
Vacancy statement by office.

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
| My vacancy position register | UI | Medium | 6 |
| Vacancy position form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver vacancy position inbox | UI | Complex | 12 |
| Vacancy position decision panel (approve / reject / return) | UI | Medium | 6 |
| My vacancy position history | UI | Medium | 6 |
| Team vacancy position history (approver) | UI | Medium | 6 |
| Vacancy register (sanctioned vs occupied) | UI | Complex | 12 |
| Save draft vacancy position | API | Medium | 6 |
| Update draft vacancy position | API | Medium | 6 |
| Submit vacancy position for approval | API | Complex | 8 |
| Withdraw vacancy position | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return vacancy position | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Derive occupied count from mappings | API | Medium | 6 |
| Vacancy position record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on vacancy position status change | Integration | Simple | 4 |
| Post and Vacancy Management feature tests | Testing | Complex | 8 |
| Post and Vacancy Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
