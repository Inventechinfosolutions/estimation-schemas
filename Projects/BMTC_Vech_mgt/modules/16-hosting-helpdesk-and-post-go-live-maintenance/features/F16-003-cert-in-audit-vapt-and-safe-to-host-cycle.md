# F16-003 — CERT-IN Audit, VAPT and Safe-to-Host Cycle

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-003 |
| **Feature Name** | CERT-IN Audit, VAPT and Safe-to-Host Cycle |
| **Module** | 16 — Hosting, Helpdesk and Post Go-Live Maintenance |

### Description
Arrange CERT-IN empanelled security audit and safe-to-host before Go-Live, and VAPT after major changes, with reports shared with BMTC. Costs borne by bidder as per RFP.

### Business Objective
RFP security audit and VAPT.

### Actors
Applicant: Security lead raises pack. Checker / BMTC CSM accepts report. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Security lead raises pack. Checker / BMTC CSM accepts report.
2. How they create: Audit register → New: type (CERT-IN / VAPT / annual), scope, vendor, planned date, Save draft. Attach report when received.
3. How they edit: Draft editable. After submit, only remarks and attachments.
4. How they send for approval: Submit pack with report for BMTC accept.
5. How the approver sees pending items: CSM/checker audit inbox.
6. How the approver decides: Accept (safe to host / VAPT closed) or Return.
7. How the applicant sees history: Audit history.
8. How the approver sees history: Accepted packs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own security audit pack history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My security audit pack register | Medium |
| Security audit pack form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver security audit pack inbox | Complex |
| Security audit pack decision panel (approve / reject / return) | Medium |
| My security audit pack history | Medium |
| Team security audit pack history (approver) | Medium |
| Audit register | Medium |
| Finding tracker | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft security audit pack | Medium |
| Update draft security audit pack | Medium |
| Submit security audit pack for approval | Complex |
| Withdraw security audit pack | Easy |
| Approver inbox query | Medium |
| Approve, reject or return security audit pack | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record audit pack | Medium |
| Track finding closure | Complex |

### Inputs
Type, vendor, dates, findings count, status.

### Outputs
Persisted security audit pack with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own security audit pack.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Report attachment required to submit.

### Calculations
Open findings count.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Audit report PDF.

### Reports
Audit calendar.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
CERT-IN empanelled auditor coordination

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
| My security audit pack register | UI | Medium | 6 |
| Security audit pack form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver security audit pack inbox | UI | Complex | 12 |
| Security audit pack decision panel (approve / reject / return) | UI | Medium | 6 |
| My security audit pack history | UI | Medium | 6 |
| Team security audit pack history (approver) | UI | Medium | 6 |
| Audit register | UI | Medium | 6 |
| Finding tracker | UI | Complex | 12 |
| Save draft security audit pack | API | Medium | 6 |
| Update draft security audit pack | API | Medium | 6 |
| Submit security audit pack for approval | API | Complex | 8 |
| Withdraw security audit pack | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return security audit pack | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record audit pack | API | Medium | 6 |
| Track finding closure | API | Complex | 8 |
| Security audit pack record, status history and attachments metadata | DB | Medium | 4 |
| CERT-IN empanelled auditor coordination | Integration | Medium | 16 |
| CERT-IN Audit, VAPT and Safe-to-Host Cycle feature tests | Testing | Complex | 8 |
| CERT-IN Audit, VAPT and Safe-to-Host Cycle implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **163** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
