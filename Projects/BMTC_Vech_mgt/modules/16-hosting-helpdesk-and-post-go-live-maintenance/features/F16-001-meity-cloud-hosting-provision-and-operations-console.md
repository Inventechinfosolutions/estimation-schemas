# F16-001 — MeitY Cloud Hosting Provision and Operations Console

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F16-001 |
| **Feature Name** | MeitY Cloud Hosting Provision and Operations Console |
| **Module** | 16 — Hosting, Helpdesk and Post Go-Live Maintenance |

### Description
Successful bidder provides MeitY-empaneled cloud hosting in India with required compute, storage, bandwidth, DR/backup and SLA instrumentation. Pre-bid: hosting infrastructure is by the successful bidder. This feature is provision, environment promotion and the operations console — not the cloud vendor invoice.

### Business Objective
RFP hosting + pre-bid query 13.

### Actors
Applicant: Hosting Administrator / SPOC. BMTC CSM views SLA and backup status. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Hosting Administrator / SPOC. BMTC CSM views SLA and backup status.
2. How they create: Ops console → New environment (dev/test/prod): sizing, region India, backup policy, Save draft.
3. How they edit: Draft sizing editable. Production change is a new version submitted to checker.
4. How they send for approval: Submit environment change for Hosting Checker / BMTC CSM acknowledge.
5. How the approver sees pending items: Checker inbox for production changes. Backup/SLA alerts list.
6. How the approver decides: Approve production change or return.
7. How the applicant sees history: Environment and backup history.
8. How the approver sees history: Approved changes; auditor SLA pack.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own hosting environment history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My hosting environment register | Medium |
| Hosting environment form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver hosting environment inbox | Complex |
| Hosting environment decision panel (approve / reject / return) | Medium |
| My hosting environment history | Medium |
| Team hosting environment history (approver) | Medium |
| Environment register | Complex |
| Backup and DR status | Complex |
| SLA uptime dashboard | Very High |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft hosting environment | Medium |
| Update draft hosting environment | Medium |
| Submit hosting environment for approval | Complex |
| Withdraw hosting environment | Easy |
| Approver inbox query | Medium |
| Approve, reject or return hosting environment | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Provision/update environment | Very High |
| Record backup completion | Medium |
| Compute monthly uptime | Complex |

### Inputs
Environment, sizing, backup policy, DR flag, India residency confirmation.

### Outputs
Persisted hosting environment with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own hosting environment.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Cloud consumption (INR) is quoted inside the per-user-per-month rate; hours here are provision and ops software, not the vendor bill.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- India residency mandatory.
- Prod change requires checker.

### Calculations
Monthly uptime % against 99.5% RFP baseline.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Hosting runbook.

### Reports
Monthly SLA pack for payment.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
MeitY-empaneled cloud platform (India region)

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
| My hosting environment register | UI | Medium | 6 |
| Hosting environment form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver hosting environment inbox | UI | Complex | 12 |
| Hosting environment decision panel (approve / reject / return) | UI | Medium | 6 |
| My hosting environment history | UI | Medium | 6 |
| Team hosting environment history (approver) | UI | Medium | 6 |
| Environment register | UI | Complex | 12 |
| Backup and DR status | UI | Complex | 12 |
| SLA uptime dashboard | UI | Very High | 16 |
| Save draft hosting environment | API | Medium | 6 |
| Update draft hosting environment | API | Medium | 6 |
| Submit hosting environment for approval | API | Complex | 8 |
| Withdraw hosting environment | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return hosting environment | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Provision/update environment | API | Very High | 16 |
| Record backup completion | API | Medium | 6 |
| Compute monthly uptime | API | Complex | 8 |
| Hosting environment record, status history and attachments metadata | DB | Medium | 4 |
| MeitY-empaneled cloud platform (India region) | Integration | Very High | 40 |
| MeitY Cloud Hosting Provision and Operations Console feature tests | Testing | Very High | 12 |
| MeitY Cloud Hosting Provision and Operations Console implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **229** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
