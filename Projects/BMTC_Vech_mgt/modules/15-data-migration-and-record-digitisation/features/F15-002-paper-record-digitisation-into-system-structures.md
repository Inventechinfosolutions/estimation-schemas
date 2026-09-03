# F15-002 — Paper Record Digitisation into System Structures

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-002 |
| **Feature Name** | Paper Record Digitisation into System Structures |
| **Module** | 15 — Data Migration and Record Digitisation |

### Description
Existing BMTC paper categories listed in the RFP are captured into the same structures as live transactions (job cards, history cards, registers), mirroring paper information.

### Business Objective
RFP document digitisation requirements.

### Actors
Applicant: Data entry clerk at depot/stores. Supervisor samples. Checker batch sign-off. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Data entry clerk at depot/stores. Supervisor samples. Checker batch sign-off.
2. How they create: Digitisation → New batch: record type, location, enter/upload records matching paper fields, Save draft.
3. How they edit: Draft batch editable. After sign-off, corrections are amendment records.
4. How they send for approval: Submit batch for supervisor sample then Checker sign-off.
5. How the approver sees pending items: Supervisor sample inbox; Checker batch inbox.
6. How the approver decides: Accept batch or Return.
7. How the applicant sees history: Batch and record history.
8. How the approver sees history: Signed batches.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own digitisation batch history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My digitisation batch register | Medium |
| Digitisation batch form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver digitisation batch inbox | Complex |
| Digitisation batch decision panel (approve / reject / return) | Medium |
| My digitisation batch history | Medium |
| Team digitisation batch history (approver) | Medium |
| Digitisation entry form | Complex |
| Batch register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft digitisation batch | Medium |
| Update draft digitisation batch | Medium |
| Submit digitisation batch for approval | Complex |
| Withdraw digitisation batch | Easy |
| Approver inbox query | Medium |
| Approve, reject or return digitisation batch | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Save digitised record | Medium |
| Sign off batch | Complex |

### Inputs
Record type, paper fields mapped to system fields, count.

### Outputs
Persisted digitisation batch with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own digitisation batch.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Scanning bureau hardware/staffing is out of application hours unless BMTC later orders it. Hours here are screens and load into live structures.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Record type from catalogue.
- Mandatory paper fields mapped.

### Calculations
Batch completeness %.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Scan optional; structured fields are the system of record.

### Reports
Digitisation progress.

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
| My digitisation batch register | UI | Medium | 6 |
| Digitisation batch form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver digitisation batch inbox | UI | Complex | 12 |
| Digitisation batch decision panel (approve / reject / return) | UI | Medium | 6 |
| My digitisation batch history | UI | Medium | 6 |
| Team digitisation batch history (approver) | UI | Medium | 6 |
| Digitisation entry form | UI | Complex | 12 |
| Batch register | UI | Medium | 6 |
| Save draft digitisation batch | API | Medium | 6 |
| Update draft digitisation batch | API | Medium | 6 |
| Submit digitisation batch for approval | API | Complex | 8 |
| Withdraw digitisation batch | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return digitisation batch | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Save digitised record | API | Medium | 6 |
| Sign off batch | API | Complex | 8 |
| Digitisation batch record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on digitisation batch status change | Integration | Simple | 4 |
| Paper Record Digitisation into System Structures feature tests | Testing | Complex | 8 |
| Paper Record Digitisation into System Structures implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
