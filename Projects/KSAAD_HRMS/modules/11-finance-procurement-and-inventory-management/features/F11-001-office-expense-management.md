# F11-001 — Office Expense Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-001 |
| **Feature Name** | Office Expense Management |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Office clerk/officer records an expense, submits to supervising/accounts Post; history of decisions and amounts.

### Business Objective
Approved expenses, not informal books.

### Actors
Applicant: Office staff with expense Role. Approver: Supervising Post and/or accounts Post per template/threshold. Other: Auditor.

### User Journey
1. Who creates: Office staff with expense Role.
2. How they create: Opens Expenses → New: head, amount, date, office, grant tag optional, bills, Save draft.
3. How they edit: Draft/Returned editable. After Submit freeze.
4. How they send for approval: Submit for approval.
5. How the approver sees pending items: Approver expense inbox.
6. How the approver decides: Approve, reject, return.
7. How the applicant sees history: My expenses timeline.
8. How the approver sees history: Decided expenses.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own office expense history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My office expense register | Medium |
| Office expense form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver office expense inbox | Complex |
| Office expense decision panel (approve / reject / return) | Medium |
| My office expense history | Medium |
| Team office expense history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft office expense | Medium |
| Update draft office expense | Medium |
| Submit office expense for approval | Complex |
| Withdraw office expense | Easy |
| Approver inbox query | Medium |
| Approve, reject or return office expense | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Head, amount, date, office, attachments.

### Outputs
Persisted office expense with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own office expense.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount > 0.
- Head from catalogue.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Bills via DMS.

### Reports
Expenses by head/office.

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
| My office expense register | UI | Medium | 6 |
| Office expense form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver office expense inbox | UI | Complex | 12 |
| Office expense decision panel (approve / reject / return) | UI | Medium | 6 |
| My office expense history | UI | Medium | 6 |
| Team office expense history (approver) | UI | Medium | 6 |
| Save draft office expense | API | Medium | 6 |
| Update draft office expense | API | Medium | 6 |
| Submit office expense for approval | API | Complex | 8 |
| Withdraw office expense | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return office expense | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Office expense record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on office expense status change | Integration | Simple | 4 |
| Office Expense Management feature tests | Testing | Complex | 8 |
| Office Expense Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
