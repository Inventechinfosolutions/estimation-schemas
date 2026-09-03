# F12-002 — Auto Purchase Request and Manual PR

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-002 |
| **Feature Name** | Auto Purchase Request and Manual PR |
| **Module** | 12 — Purchase and Supplier Management |

### Description
System raises auto PR as advance alert from reorder/forecast; officer may raise manual PR for Store and Mechanical officers.

### Business Objective
FR-S-21.

### Actors
Applicant: Store/Mechanical Officer (manual) or system (auto). Approver: COSP / Purchase approving Post. Other: Auditor.

### User Journey
1. Who creates: Store/Mechanical Officer (manual) or system (auto).
2. How they create: Auto: from reorder/forecast → Create PR draft. Manual: PR → New: items, qty, justification, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to purchase approver.
5. How the approver sees pending items: PR approval inbox.
6. How the approver decides: Approve (eligible for PO) or Return/Reject.
7. How the applicant sees history: PR timeline.
8. How the approver sees history: Decided PRs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own purchase request history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My purchase request register | Medium |
| Purchase request form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver purchase request inbox | Complex |
| Purchase request decision panel (approve / reject / return) | Medium |
| My purchase request history | Medium |
| Team purchase request history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft purchase request | Medium |
| Update draft purchase request | Medium |
| Submit purchase request for approval | Complex |
| Withdraw purchase request | Easy |
| Approver inbox query | Medium |
| Approve, reject or return purchase request | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Generate auto PR from reorder | Complex |

### Inputs
Items, qty, source (auto/manual), justification.

### Outputs
Persisted purchase request with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own purchase request.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Qty > 0.
- Item mandatory.

### Calculations
Suggested qty from reorder/forecast (editable).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
Open PRs.

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
| My purchase request register | UI | Medium | 6 |
| Purchase request form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver purchase request inbox | UI | Complex | 12 |
| Purchase request decision panel (approve / reject / return) | UI | Medium | 6 |
| My purchase request history | UI | Medium | 6 |
| Team purchase request history (approver) | UI | Medium | 6 |
| Save draft purchase request | API | Medium | 6 |
| Update draft purchase request | API | Medium | 6 |
| Submit purchase request for approval | API | Complex | 8 |
| Withdraw purchase request | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return purchase request | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Generate auto PR from reorder | API | Complex | 8 |
| Purchase request record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on purchase request status change | Integration | Simple | 4 |
| Auto Purchase Request and Manual PR feature tests | Testing | Complex | 8 |
| Auto Purchase Request and Manual PR implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **127** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
