# F05-003 — Job Card Closure and Labour Hours

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-003 |
| **Feature Name** | Job Card Closure and Labour Hours |
| **Module** | 05 — Digital Job Card and Fitment |

### Description
Supervisor closes the job card only after work is complete, with digital sign-off. Labour hours are calculated from start/end. Closed cards remain on vehicle history.

### Business Objective
FR-M-09 to 12.

### Actors
Applicant: Tech. Supervisor requests closure (or clerk requests; supervisor decides). Approver: Tech. Supervisor / Depot Manager digital sign-off Post. Other: Mechanic. Auditor.

### User Journey
1. Who creates: Tech. Supervisor requests closure (or clerk requests; supervisor decides).
2. How they create: On the job card, enter labour start/end, vehicle ready date/time, next maintenance KM/date, Submit for closure.
3. How they edit: Cannot edit a Completed card. Return reopens to In Progress.
4. How they send for approval: Submit closure. Blocked if required spares/fitment incomplete unless waived with reason.
5. How the approver sees pending items: Supervisor closure inbox.
6. How the approver decides: Digital sign-off Completes the card, or Return.
7. How the applicant sees history: Closure timeline on the card; card remains in vehicle maintenance history.
8. How the approver sees history: Sign-off history.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own job card closure history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My job card closure register | Medium |
| Job card closure form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver job card closure inbox | Complex |
| Job card closure decision panel (approve / reject / return) | Medium |
| My job card closure history | Medium |
| Team job card closure history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft job card closure | Medium |
| Update draft job card closure | Medium |
| Submit job card closure for approval | Complex |
| Withdraw job card closure | Easy |
| Approver inbox query | Medium |
| Approve, reject or return job card closure | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Calculate labour hours | Easy |

### Inputs
Labour times, ready time, next PM KM/date, sign-off.

### Outputs
Persisted job card closure with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own job card closure.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Start before end.
- Supervisor Post required to complete.

### Calculations
Total labour hours = end − start.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Digital sign-off record.

### Reports
Completed job cards; pending ageing (FR-R-01 uses status).

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
| My job card closure register | UI | Medium | 6 |
| Job card closure form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver job card closure inbox | UI | Complex | 12 |
| Job card closure decision panel (approve / reject / return) | UI | Medium | 6 |
| My job card closure history | UI | Medium | 6 |
| Team job card closure history (approver) | UI | Medium | 6 |
| Save draft job card closure | API | Medium | 6 |
| Update draft job card closure | API | Medium | 6 |
| Submit job card closure for approval | API | Complex | 8 |
| Withdraw job card closure | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return job card closure | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Calculate labour hours | API | Easy | 4 |
| Job card closure record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on job card closure status change | Integration | Simple | 4 |
| Job Card Closure and Labour Hours feature tests | Testing | Complex | 8 |
| Job Card Closure and Labour Hours implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
