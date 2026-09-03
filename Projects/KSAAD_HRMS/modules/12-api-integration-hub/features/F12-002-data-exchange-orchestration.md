# F12-002 — Data Exchange Orchestration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-002 |
| **Feature Name** | Data Exchange Orchestration |
| **Module** | 12 — API Integration Hub |

### Description
Administrator configures a run (source, mapping, schedule); checker approves config; operator starts/monitors runs; failed runs retry with history.

### Business Objective
Repeatable, traced exchanges.

### Actors
Applicant: Integration Administrator designs. Operator starts/retries. Checker approves mapping versions. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Integration Administrator designs. Operator starts/retries. Checker approves mapping versions.
2. How they create: Opens Exchanges → New: source, target, mapping, schedule, Save draft config.
3. How they edit: Config versions: edit draft, submit, approve. In-flight run cannot change mapping mid-run.
4. How they send for approval: Submit mapping version. Operator Start run on approved config.
5. How the approver sees pending items: Checker mapping inbox. Operator failed-run inbox.
6. How the approver decides: Checker approve mapping. Operator Retry or Abandon failed run with reason.
7. How the applicant sees history: Run log: start, counts, errors.
8. How the approver sees history: Approved mappings; abandoned runs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own exchange run history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My exchange run register | Medium |
| Exchange run form (create and edit) | Very High |
| Submit confirmation | Simple |
| Approver exchange run inbox | Complex |
| Exchange run decision panel (approve / reject / return) | Medium |
| My exchange run history | Medium |
| Team exchange run history (approver) | Medium |
| Mapping designer | Very High |
| Run monitor | Complex |
| Retry dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft exchange run | Medium |
| Update draft exchange run | Medium |
| Submit exchange run for approval | Complex |
| Withdraw exchange run | Easy |
| Approver inbox query | Medium |
| Approve, reject or return exchange run | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Start run | Very High |
| Retry run | Complex |
| Record run result | Complex |

### Inputs
Source, target, mapping, schedule, run status.

### Outputs
Persisted exchange run with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own exchange run.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Approved mapping required to start.

### Calculations
Read/inserted/skipped/error counts.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Mapping documentation.

### Reports
Run success rate.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Source/target exchange channel with retry

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
| My exchange run register | UI | Medium | 6 |
| Exchange run form (create and edit) | UI | Very High | 16 |
| Submit confirmation | UI | Simple | 2 |
| Approver exchange run inbox | UI | Complex | 12 |
| Exchange run decision panel (approve / reject / return) | UI | Medium | 6 |
| My exchange run history | UI | Medium | 6 |
| Team exchange run history (approver) | UI | Medium | 6 |
| Mapping designer | UI | Very High | 16 |
| Run monitor | UI | Complex | 12 |
| Retry dialog | UI | Simple | 2 |
| Save draft exchange run | API | Medium | 6 |
| Update draft exchange run | API | Medium | 6 |
| Submit exchange run for approval | API | Complex | 8 |
| Withdraw exchange run | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return exchange run | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Start run | API | Very High | 16 |
| Retry run | API | Complex | 8 |
| Record run result | API | Complex | 8 |
| Exchange run record, status history and attachments metadata | DB | Medium | 4 |
| Source/target exchange channel with retry | Integration | Medium | 16 |
| Data Exchange Orchestration feature tests | Testing | Very High | 12 |
| Data Exchange Orchestration implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **201** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
