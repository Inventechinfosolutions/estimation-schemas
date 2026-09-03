# F13-003 — AVLS and BMTC IT Integration Hooks

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-003 |
| **Feature Name** | AVLS and BMTC IT Integration Hooks |
| **Module** | 13 — Barcode, QR, Notifications and External Integrations |

### Description
Fetch vehicle master/fuel/KM from AVLS (pre-bid: KM and fuel currently entered in AVLS). Share API/MIS with BMTC; integrate existing and future IT projects as required.

### Business Objective
RFP AVLS and API sharing.

### Actors
Applicant: Integration Administrator configures. Operator monitors runs. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Integration Administrator configures. Operator monitors runs.
2. How they create: Integrations → AVLS mapping: fields, schedule, Save draft. Test fetch.
3. How they edit: Draft mapping editable. Live change is a new version.
4. How they send for approval: Submit mapping to checker. Operator starts run on approved mapping.
5. How the approver sees pending items: Checker mapping inbox; failed-run inbox.
6. How the approver decides: Approve mapping; retry/abandon failed run.
7. How the applicant sees history: Run log.
8. How the approver sees history: Approved mappings.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own integration run history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My integration run register | Medium |
| Integration run form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver integration run inbox | Complex |
| Integration run decision panel (approve / reject / return) | Medium |
| My integration run history | Medium |
| Team integration run history (approver) | Medium |
| Mapping form | Complex |
| Run monitor | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft integration run | Medium |
| Update draft integration run | Medium |
| Submit integration run for approval | Complex |
| Withdraw integration run | Easy |
| Approver inbox query | Medium |
| Approve, reject or return integration run | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Fetch AVLS vehicle/fuel/KM | Very High |
| Expose agreed MIS/API to BMTC | Complex |

### Inputs
Source, schedule, field map, run status.

### Outputs
Persisted integration run with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own integration run.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Approved mapping required to run.

### Calculations
Read/error counts.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Interface note.

### Reports
Run success.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
AVLS and BMTC IT APIs

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
| My integration run register | UI | Medium | 6 |
| Integration run form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver integration run inbox | UI | Complex | 12 |
| Integration run decision panel (approve / reject / return) | UI | Medium | 6 |
| My integration run history | UI | Medium | 6 |
| Team integration run history (approver) | UI | Medium | 6 |
| Mapping form | UI | Complex | 12 |
| Run monitor | UI | Medium | 6 |
| Save draft integration run | API | Medium | 6 |
| Update draft integration run | API | Medium | 6 |
| Submit integration run for approval | API | Complex | 8 |
| Withdraw integration run | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return integration run | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Fetch AVLS vehicle/fuel/KM | API | Very High | 16 |
| Expose agreed MIS/API to BMTC | API | Complex | 8 |
| Integration run record, status history and attachments metadata | DB | Medium | 4 |
| AVLS and BMTC IT APIs | Integration | Complex | 24 |
| AVLS and BMTC IT Integration Hooks feature tests | Testing | Very High | 12 |
| AVLS and BMTC IT Integration Hooks implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **185** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
