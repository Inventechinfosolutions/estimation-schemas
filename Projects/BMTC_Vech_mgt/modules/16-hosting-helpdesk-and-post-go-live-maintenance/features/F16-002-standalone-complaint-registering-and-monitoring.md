# F16-002 — Standalone Complaint Registering and Monitoring

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-002 |
| **Feature Name** | Standalone Complaint Registering and Monitoring |
| **Module** | 16 — Hosting, Helpdesk and Post Go-Live Maintenance |

### Description
24x7 helpdesk as a standalone module (pre-bid: not integrated with an existing BMTC helpdesk). BMTC staff register application faults; SPOC updates rectification.

### Business Objective
RFP Complaint Registering & Monitoring; pre-bid standalone module.

### Actors
Applicant: Any authorised BMTC Person from a current Post. Approver: On-site SPOC / L2 resolver Post. Other: CSM. Auditor.

### User Journey
1. Who creates: Any authorised BMTC Person from a current Post.
2. How they create: Helpdesk → New ticket: module, severity, description, optional screenshot, Save draft, Submit.
3. How they edit: Draft/Returned editable. Open tickets take remarks and status updates, not silent field overwrite of the original complaint.
4. How they send for approval: Submit opens the ticket. SPOC assigns and resolves.
5. How the approver sees pending items: SPOC/L2 inbox by severity and ageing. 24x7 intake remains open.
6. How the approver decides: Resolve with rectification notes, Return to requester for more detail, or Escalate.
7. How the applicant sees history: My tickets.
8. How the approver sees history: All tickets by depot/module.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own support ticket history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My support ticket register | Medium |
| Support ticket form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver support ticket inbox | Complex |
| Support ticket decision panel (approve / reject / return) | Medium |
| My support ticket history | Medium |
| Team support ticket history (approver) | Medium |
| 24x7 ticket intake | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft support ticket | Medium |
| Update draft support ticket | Medium |
| Submit support ticket for approval | Complex |
| Withdraw support ticket | Easy |
| Approver inbox query | Medium |
| Approve, reject or return support ticket | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Start SLA clock | Medium |
| Close ticket within critical/normal RFP windows | Complex |

### Inputs
Module, severity, description, status, SLA clock.

### Outputs
Persisted support ticket with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own support ticket.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Severity mandatory.
- Resolved requires rectification text.

### Calculations
Ageing vs critical <8 hrs and normal <48 hrs (RFP SLA table).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional screenshot.

### Reports
Open tickets; SLA breach list.

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
| My support ticket register | UI | Medium | 6 |
| Support ticket form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver support ticket inbox | UI | Complex | 12 |
| Support ticket decision panel (approve / reject / return) | UI | Medium | 6 |
| My support ticket history | UI | Medium | 6 |
| Team support ticket history (approver) | UI | Medium | 6 |
| 24x7 ticket intake | UI | Complex | 12 |
| Save draft support ticket | API | Medium | 6 |
| Update draft support ticket | API | Medium | 6 |
| Submit support ticket for approval | API | Complex | 8 |
| Withdraw support ticket | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return support ticket | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Start SLA clock | API | Medium | 6 |
| Close ticket within critical/normal RFP windows | API | Complex | 8 |
| Support ticket record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on support ticket status change | Integration | Simple | 4 |
| Standalone Complaint Registering and Monitoring feature tests | Testing | Very High | 12 |
| Standalone Complaint Registering and Monitoring implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **149** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
