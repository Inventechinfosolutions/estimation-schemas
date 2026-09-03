# F08-005 — Audit Report Issuance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-005 |
| **Feature Name** | Audit Report Issuance |
| **Module** | 08 — Field Audit Execution & Reporting |

### Description
After approval, designated officer issues the report to the institution and internal copies; issue event is history.

### Business Objective
Traceable issuance.

### Actors
Applicant: Officer with Issue Role (often after CA approve). Approver: If dual control on issue, a checker confirms dispatch; else Issue is the action. Other: Institution users (see issued copy in Module 16). Auditor.

### User Journey
1. Who creates: Officer with Issue Role (often after CA approve).
2. How they create: Opens issuance-ready reports → Issue: date, addressees, dispatch mode, Save/Submit.
3. How they edit: Cannot edit an issued report body here. Corrigendum is a new linked issuance.
4. How they send for approval: Issue (or Submit to issue-checker then Issue).
5. How the approver sees pending items: Issue-checker inbox if configured. Institution sees issued reports in F16-004.
6. How the approver decides: Confirm issue. Records issue number and timestamp.
7. How the applicant sees history: Issuance log on the assignment.
8. How the approver sees history: All issuances by office.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit report issuance history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit report issuance register | Medium |
| Audit report issuance form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver audit report issuance inbox | Complex |
| Audit report issuance decision panel (approve / reject / return) | Medium |
| My audit report issuance history | Medium |
| Team audit report issuance history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit report issuance | Medium |
| Update draft audit report issuance | Medium |
| Submit audit report issuance for approval | Complex |
| Withdraw audit report issuance | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit report issuance | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Allocate issue number | Easy |

### Inputs
Issue date, addressees, mode, issue number (system).

### Outputs
Persisted audit report issuance with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit report issuance.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Report must be approval-complete.
- At least one addressee.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Issued PDF snapshot.

### Reports
Issued vs approved not issued.

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
| My audit report issuance register | UI | Medium | 6 |
| Audit report issuance form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit report issuance inbox | UI | Complex | 12 |
| Audit report issuance decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit report issuance history | UI | Medium | 6 |
| Team audit report issuance history (approver) | UI | Medium | 6 |
| Save draft audit report issuance | API | Medium | 6 |
| Update draft audit report issuance | API | Medium | 6 |
| Submit audit report issuance for approval | API | Complex | 8 |
| Withdraw audit report issuance | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit report issuance | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Allocate issue number | API | Easy | 4 |
| Audit report issuance record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit report issuance status change | Integration | Simple | 4 |
| Audit Report Issuance feature tests | Testing | Complex | 8 |
| Audit Report Issuance implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
