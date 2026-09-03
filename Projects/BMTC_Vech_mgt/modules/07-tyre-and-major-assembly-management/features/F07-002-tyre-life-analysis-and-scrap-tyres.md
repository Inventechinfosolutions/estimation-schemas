# F07-002 — Tyre Life Analysis and Scrap Tyres

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Tyre Life Analysis and Scrap Tyres |
| **Module** | 07 — Tyre and Major Assembly Management |

### Description
System analyses KM run and premature wear; scrap tyres get condition and disposal records.

### Business Objective
FR-M-26, FR-M-27.

### Actors
Applicant: Tyre Supervisor runs analysis. Clerk records scrap assessment. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Tyre Supervisor runs analysis. Clerk records scrap assessment.
2. How they create: Tyre analysis → Run for depot/period. Scrap: select tyre, condition, disposal, Save draft.
3. How they edit: Analysis is a run, not an edited record. Scrap draft editable.
4. How they send for approval: Scrap submitted to Stores/auction path if required.
5. How the approver sees pending items: Checker scrap-tyre inbox.
6. How the approver decides: Approve scrap record.
7. How the applicant sees history: Analysis runs and scrap history.
8. How the approver sees history: Approved scraps.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own tyre analysis history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My tyre analysis register | Medium |
| Tyre analysis form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver tyre analysis inbox | Complex |
| Tyre analysis decision panel (approve / reject / return) | Medium |
| My tyre analysis history | Medium |
| Team tyre analysis history (approver) | Medium |
| Tyre life analysis | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft tyre analysis | Medium |
| Update draft tyre analysis | Medium |
| Submit tyre analysis for approval | Complex |
| Withdraw tyre analysis | Easy |
| Approver inbox query | Medium |
| Approve, reject or return tyre analysis | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Compute tyre life metrics | Complex |

### Inputs
Period, premature-wear flags, scrap condition.

### Outputs
Persisted tyre analysis with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own tyre analysis.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Scrap requires condition.

### Calculations
KM run; flag premature wear vs configured norm.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Tyre life and scrap.

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
| My tyre analysis register | UI | Medium | 6 |
| Tyre analysis form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver tyre analysis inbox | UI | Complex | 12 |
| Tyre analysis decision panel (approve / reject / return) | UI | Medium | 6 |
| My tyre analysis history | UI | Medium | 6 |
| Team tyre analysis history (approver) | UI | Medium | 6 |
| Tyre life analysis | UI | Complex | 12 |
| Save draft tyre analysis | API | Medium | 6 |
| Update draft tyre analysis | API | Medium | 6 |
| Submit tyre analysis for approval | API | Complex | 8 |
| Withdraw tyre analysis | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return tyre analysis | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Compute tyre life metrics | API | Complex | 8 |
| Tyre analysis record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on tyre analysis status change | Integration | Simple | 4 |
| Tyre Life Analysis and Scrap Tyres feature tests | Testing | Complex | 8 |
| Tyre Life Analysis and Scrap Tyres implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **139** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
