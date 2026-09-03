# F07-003 — New and RC Major Assembly Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | New and RC Major Assembly Tracking |
| **Module** | 07 — Tyre and Major Assembly Management |

### Description
Workshop tracks new major assemblies and reconditioned (RC) assemblies with related reports (engine, gearbox, axles, alternator, starter).

### Business Objective
FR-M-28, FR-M-29, FR-M-21.

### Actors
Applicant: CWS / section clerk. Supervisor confirms. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: CWS / section clerk. Supervisor confirms.
2. How they create: Assembly register → New: type, serial, new or RC, linked vehicle if fitted, Save draft.
3. How they edit: Draft/Returned editable. Fitment history append-only.
4. How they send for approval: Submit to section supervisor.
5. How the approver sees pending items: Supervisor assembly inbox.
6. How the approver decides: Confirm master/fitment.
7. How the applicant sees history: Assembly history.
8. How the approver sees history: Confirmed records.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own assembly record history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My assembly record register | Medium |
| Assembly record form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver assembly record inbox | Complex |
| Assembly record decision panel (approve / reject / return) | Medium |
| My assembly record history | Medium |
| Team assembly record history (approver) | Medium |
| Assembly register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft assembly record | Medium |
| Update draft assembly record | Medium |
| Submit assembly record for approval | Complex |
| Withdraw assembly record | Easy |
| Approver inbox query | Medium |
| Approve, reject or return assembly record | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Record assembly fitment | Medium |

### Inputs
Assembly type, serial, new/RC, vehicle, dates.

### Outputs
Persisted assembly record with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own assembly record.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Type and serial mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Assembly-level history report.

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
| My assembly record register | UI | Medium | 6 |
| Assembly record form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver assembly record inbox | UI | Complex | 12 |
| Assembly record decision panel (approve / reject / return) | UI | Medium | 6 |
| My assembly record history | UI | Medium | 6 |
| Team assembly record history (approver) | UI | Medium | 6 |
| Assembly register | UI | Medium | 6 |
| Save draft assembly record | API | Medium | 6 |
| Update draft assembly record | API | Medium | 6 |
| Submit assembly record for approval | API | Complex | 8 |
| Withdraw assembly record | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return assembly record | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Record assembly fitment | API | Medium | 6 |
| Assembly record record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on assembly record status change | Integration | Simple | 4 |
| New and RC Major Assembly Tracking feature tests | Testing | Complex | 8 |
| New and RC Major Assembly Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **131** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
