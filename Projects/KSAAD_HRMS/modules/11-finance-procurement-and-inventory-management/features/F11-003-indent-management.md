# F11-003 — Indent Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-003 |
| **Feature Name** | Indent Management |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Indenting officer creates indent, submits to supervisor then purchase cell; history of quantities and decisions.

### Business Objective
Approved indent before PO.

### Actors
Applicant: Indenting officer. Approver: Supervising Post then purchase Post as configured. Other: Stores. Auditor.

### User Journey
1. Who creates: Indenting officer.
2. How they create: Opens Indents → New: items, qty, specification, needed-by, Save draft.
3. How they edit: Draft/Returned editable. After Submit freeze.
4. How they send for approval: Submit to first approver.
5. How the approver sees pending items: Each level indent inbox.
6. How the approver decides: Approve, reject, return. Approve makes indent available to F11-004.
7. How the applicant sees history: Indent timeline.
8. How the approver sees history: Decided indents.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own indent history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My indent register | Medium |
| Indent form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver indent inbox | Complex |
| Indent decision panel (approve / reject / return) | Medium |
| My indent history | Medium |
| Team indent history (approver) | Medium |
| Indent item grid | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft indent | Medium |
| Update draft indent | Medium |
| Submit indent for approval | Complex |
| Withdraw indent | Easy |
| Approver inbox query | Medium |
| Approve, reject or return indent | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Items, qty, spec, date needed.

### Outputs
Persisted indent with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own indent.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- At least one item.
- Qty > 0.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Specification attachment.

### Reports
Pending indents.

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
| My indent register | UI | Medium | 6 |
| Indent form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver indent inbox | UI | Complex | 12 |
| Indent decision panel (approve / reject / return) | UI | Medium | 6 |
| My indent history | UI | Medium | 6 |
| Team indent history (approver) | UI | Medium | 6 |
| Indent item grid | UI | Complex | 12 |
| Save draft indent | API | Medium | 6 |
| Update draft indent | API | Medium | 6 |
| Submit indent for approval | API | Complex | 8 |
| Withdraw indent | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return indent | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Indent record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on indent status change | Integration | Simple | 4 |
| Indent Management feature tests | Testing | Complex | 8 |
| Indent Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **131** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
