# F01-006 — Access Audit Log and Recertification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Access Audit Log and Recertification |
| **Module** | 01 — Person, Post, Role & Access Governance |

### Description
Auditor searches who did what, when, from which Post, MAC/IP. Administrator runs periodic recertification of mappings.

### Business Objective
Tamper-evident access evidence as required by the RFP audit trail.

### Actors
Applicant: Auditor searches logs. Access Administrator raises recertification packs. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Auditor searches logs. Access Administrator raises recertification packs.
2. How they create: Opens Access log search by Person, Post, unit, period, action. Recertification: select unit, generate mapping pack.
3. How they edit: Logs are not edited. Recertification remarks are added.
4. How they send for approval: Recertification pack submitted to Access Checker if mappings must be confirmed or ended.
5. How the approver sees pending items: Checker recertification inbox. Logs have no inbox.
6. How the approver decides: Checker confirms mapping still valid or instructs JML.
7. How the applicant sees history: Recertification history. Log search history for auditor.
8. How the approver sees history: Confirmed recertifications.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own access recertification history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My access recertification register | Medium |
| Access recertification form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver access recertification inbox | Complex |
| Access recertification decision panel (approve / reject / return) | Medium |
| My access recertification history | Medium |
| Team access recertification history (approver) | Medium |
| Access log search | Complex |
| Recertification pack | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft access recertification | Medium |
| Update draft access recertification | Medium |
| Submit access recertification for approval | Complex |
| Withdraw access recertification | Easy |
| Approver inbox query | Medium |
| Approve, reject or return access recertification | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Search access log | Complex |
| Submit recertification | Medium |

### Inputs
Filters; recertification decision.

### Outputs
Persisted access recertification with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own access recertification.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Period required for log export.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional export file.

### Reports
Access log export retained per RFP (minimum one year transaction log; five years application data).

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
| My access recertification register | UI | Medium | 6 |
| Access recertification form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver access recertification inbox | UI | Complex | 12 |
| Access recertification decision panel (approve / reject / return) | UI | Medium | 6 |
| My access recertification history | UI | Medium | 6 |
| Team access recertification history (approver) | UI | Medium | 6 |
| Access log search | UI | Complex | 12 |
| Recertification pack | UI | Medium | 6 |
| Save draft access recertification | API | Medium | 6 |
| Update draft access recertification | API | Medium | 6 |
| Submit access recertification for approval | API | Complex | 8 |
| Withdraw access recertification | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return access recertification | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Search access log | API | Complex | 8 |
| Submit recertification | API | Medium | 6 |
| Access recertification record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on access recertification status change | Integration | Simple | 4 |
| Access Audit Log and Recertification feature tests | Testing | Complex | 8 |
| Access Audit Log and Recertification implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
