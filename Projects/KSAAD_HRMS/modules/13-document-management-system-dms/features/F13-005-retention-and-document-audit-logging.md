# F13-005 — Retention and Document Audit Logging

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-005 |
| **Feature Name** | Retention and Document Audit Logging |
| **Module** | 13 — Document Management System (DMS) |

### Description
DMS admin sets retention on document types; legal hold stops purge; every view/download is logged; purge runs are history.

### Business Objective
Retention and access forensic log.

### Actors
Applicant: DMS Administrator configures. Checker approves retention policy. System logs views. Purge is a checked run. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: DMS Administrator configures. Checker approves retention policy. System logs views. Purge is a checked run.
2. How they create: Retention policies → New: document type, years, Save draft. Legal hold → select documents, reason, Save.
3. How they edit: Policy versions. Holds revoked with reason.
4. How they send for approval: Submit policy/hold/purge list to checker.
5. How the approver sees pending items: Checker retention inbox. Purge preview list.
6. How the approver decides: Approve policy, hold, or purge run.
7. How the applicant sees history: Policy versions, holds, purge runs.
8. How the approver sees history: Same plus access log (who viewed/downloaded which document when).

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own retention hold history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My retention hold register | Medium |
| Retention hold form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver retention hold inbox | Complex |
| Retention hold decision panel (approve / reject / return) | Medium |
| My retention hold history | Medium |
| Team retention hold history (approver) | Medium |
| Retention policy form | Medium |
| Access log search | Complex |
| Purge preview | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft retention hold | Medium |
| Update draft retention hold | Medium |
| Submit retention hold for approval | Complex |
| Withdraw retention hold | Easy |
| Approver inbox query | Medium |
| Approve, reject or return retention hold | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Write access log | Medium |
| Apply hold | Medium |
| Purge run | Complex |

### Inputs
Type, years, hold reason, purge candidate list.

### Outputs
Persisted retention hold with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own retention hold.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Purge skipped if hold or parent still open.

### Calculations
Eligible purge date = created + years unless hold.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
N/A.

### Reports
Access log export.

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
| My retention hold register | UI | Medium | 6 |
| Retention hold form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver retention hold inbox | UI | Complex | 12 |
| Retention hold decision panel (approve / reject / return) | UI | Medium | 6 |
| My retention hold history | UI | Medium | 6 |
| Team retention hold history (approver) | UI | Medium | 6 |
| Retention policy form | UI | Medium | 6 |
| Access log search | UI | Complex | 12 |
| Purge preview | UI | Medium | 6 |
| Save draft retention hold | API | Medium | 6 |
| Update draft retention hold | API | Medium | 6 |
| Submit retention hold for approval | API | Complex | 8 |
| Withdraw retention hold | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return retention hold | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Write access log | API | Medium | 6 |
| Apply hold | API | Medium | 6 |
| Purge run | API | Complex | 8 |
| Retention hold record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on retention hold status change | Integration | Simple | 4 |
| Retention and Document Audit Logging feature tests | Testing | Complex | 8 |
| Retention and Document Audit Logging implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **163** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
