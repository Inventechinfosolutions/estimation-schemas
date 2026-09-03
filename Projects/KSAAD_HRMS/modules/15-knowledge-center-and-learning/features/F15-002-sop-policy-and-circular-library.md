# F15-002 — SOP, Policy and Circular Library

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-002 |
| **Feature Name** | SOP, Policy and Circular Library |
| **Module** | 15 — Knowledge Center & Learning |

### Description
Admin links SOPs/policies (often also circulars from F03-009) into a searchable library with version; owner approves listing.

### Business Objective
One place to retrieve official SOP/policy.

### Actors
Applicant: Knowledge/establishment admin lists documents. Owner Post approves listing. Staff search/read. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Knowledge/establishment admin lists documents. Owner Post approves listing. Staff search/read.
2. How they create: Library → New: title, type (SOP/policy/circular), upload or link existing circular, effective date, Save draft.
3. How they edit: Draft editable. New version replaces current listing after approve.
4. How they send for approval: Submit listing.
5. How the approver sees pending items: Owner library inbox.
6. How the approver decides: Approve listing or reject.
7. How the applicant sees history: Listing versions.
8. How the approver sees history: Approved listings.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own policy library item history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My policy library item register | Medium |
| Policy library item form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver policy library item inbox | Complex |
| Policy library item decision panel (approve / reject / return) | Medium |
| My policy library item history | Medium |
| Team policy library item history (approver) | Medium |
| Library search | Complex |
| Listing form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft policy library item | Medium |
| Update draft policy library item | Medium |
| Submit policy library item for approval | Complex |
| Withdraw policy library item | Easy |
| Approver inbox query | Medium |
| Approve, reject or return policy library item | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Publish listing | Medium |

### Inputs
Title, type, file/link, effective date.

### Outputs
Persisted policy library item with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own policy library item.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Type and title mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
SOP/policy file via DMS.

### Reports
Library inventory.

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
| My policy library item register | UI | Medium | 6 |
| Policy library item form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver policy library item inbox | UI | Complex | 12 |
| Policy library item decision panel (approve / reject / return) | UI | Medium | 6 |
| My policy library item history | UI | Medium | 6 |
| Team policy library item history (approver) | UI | Medium | 6 |
| Library search | UI | Complex | 12 |
| Listing form | UI | Medium | 6 |
| Save draft policy library item | API | Medium | 6 |
| Update draft policy library item | API | Medium | 6 |
| Submit policy library item for approval | API | Complex | 8 |
| Withdraw policy library item | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return policy library item | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Publish listing | API | Medium | 6 |
| Policy library item record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on policy library item status change | Integration | Simple | 4 |
| SOP, Policy and Circular Library feature tests | Testing | Complex | 8 |
| SOP, Policy and Circular Library implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **143** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
