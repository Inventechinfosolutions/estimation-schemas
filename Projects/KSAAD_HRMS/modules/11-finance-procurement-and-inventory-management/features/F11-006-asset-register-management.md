# F11-006 — Asset Register Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-006 |
| **Feature Name** | Asset Register Management |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Officer creates an asset from purchase/capitalisation, submits to checker; later transfers/disposal are requests with history.

### Business Objective
Asset register with lifecycle events.

### Actors
Applicant: Stores/accounts officer. Approver: Asset checker / competent Post on capitalise, transfer, dispose. Other: Custodian office. Auditor.

### User Journey
1. Who creates: Stores/accounts officer.
2. How they create: Assets → New: description, category, value, location/custodian, linked PO, Save draft.
3. How they edit: Draft editable. Location change is a transfer request, not a silent edit of history.
4. How they send for approval: Submit capitalisation, transfer or disposal.
5. How the approver sees pending items: Checker asset-event inbox.
6. How the approver decides: Approve or reject event.
7. How the applicant sees history: Asset event timeline.
8. How the approver sees history: Approved events.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own asset record history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My asset record register | Medium |
| Asset record form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver asset record inbox | Complex |
| Asset record decision panel (approve / reject / return) | Medium |
| My asset record history | Medium |
| Team asset record history (approver) | Medium |
| Asset form | Complex |
| Transfer/disposal form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft asset record | Medium |
| Update draft asset record | Medium |
| Submit asset record for approval | Complex |
| Withdraw asset record | Easy |
| Approver inbox query | Medium |
| Approve, reject or return asset record | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Description, category, value, location, event type.

### Outputs
Persisted asset record with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own asset record.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Description and category mandatory.
- Disposal requires reason.

### Calculations
None beyond counts.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Invoice/capitalisation note.

### Reports
Asset register by location.

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
| My asset record register | UI | Medium | 6 |
| Asset record form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver asset record inbox | UI | Complex | 12 |
| Asset record decision panel (approve / reject / return) | UI | Medium | 6 |
| My asset record history | UI | Medium | 6 |
| Team asset record history (approver) | UI | Medium | 6 |
| Asset form | UI | Complex | 12 |
| Transfer/disposal form | UI | Medium | 6 |
| Save draft asset record | API | Medium | 6 |
| Update draft asset record | API | Medium | 6 |
| Submit asset record for approval | API | Complex | 8 |
| Withdraw asset record | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return asset record | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Asset record record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on asset record status change | Integration | Simple | 4 |
| Asset Register Management feature tests | Testing | Complex | 8 |
| Asset Register Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **137** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
