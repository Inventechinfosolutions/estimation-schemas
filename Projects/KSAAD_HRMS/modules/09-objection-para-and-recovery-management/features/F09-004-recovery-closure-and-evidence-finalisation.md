# F09-004 — Recovery Closure and Evidence Finalisation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Recovery Closure and Evidence Finalisation |
| **Module** | 09 — Objection, Para & Recovery Management |

### Description
Officer proposes closure when outstanding is zero (or write-off path); competent Post approves; evidence pack frozen.

### Business Objective
Closed with evidence, not informal.

### Actors
Applicant: Recovery officer. Approver: Competent Post. Other: Auditor.

### User Journey
1. Who creates: Recovery officer.
2. How they create: On recovery action with outstanding 0 (or write-off request) → Propose closure, attach evidence list, Save.
3. How they edit: Draft proposal editable. After approve, reopen is a new case.
4. How they send for approval: Submit closure.
5. How the approver sees pending items: Approver closure inbox.
6. How the approver decides: Approve closure or reject (case stays open).
7. How the applicant sees history: Closure decision on the action.
8. How the approver sees history: Closed recoveries.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own recovery closure history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My recovery closure register | Medium |
| Recovery closure form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver recovery closure inbox | Complex |
| Recovery closure decision panel (approve / reject / return) | Medium |
| My recovery closure history | Medium |
| Team recovery closure history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft recovery closure | Medium |
| Update draft recovery closure | Medium |
| Submit recovery closure for approval | Complex |
| Withdraw recovery closure | Easy |
| Approver inbox query | Medium |
| Approve, reject or return recovery closure | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Recovery action, closure type, evidence list, remarks.

### Outputs
Persisted recovery closure with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own recovery closure.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Outstanding must be 0 unless write-off type and reason present.

### Calculations
Outstanding must match ledger.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Closure evidence pack via DMS.

### Reports
Closed vs open recovery.

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
| My recovery closure register | UI | Medium | 6 |
| Recovery closure form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver recovery closure inbox | UI | Complex | 12 |
| Recovery closure decision panel (approve / reject / return) | UI | Medium | 6 |
| My recovery closure history | UI | Medium | 6 |
| Team recovery closure history (approver) | UI | Medium | 6 |
| Save draft recovery closure | API | Medium | 6 |
| Update draft recovery closure | API | Medium | 6 |
| Submit recovery closure for approval | API | Complex | 8 |
| Withdraw recovery closure | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return recovery closure | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Recovery closure record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on recovery closure status change | Integration | Simple | 4 |
| Recovery Closure and Evidence Finalisation feature tests | Testing | Complex | 8 |
| Recovery Closure and Evidence Finalisation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
