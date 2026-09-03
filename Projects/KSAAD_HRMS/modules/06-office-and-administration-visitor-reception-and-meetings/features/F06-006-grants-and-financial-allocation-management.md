# F06-006 — Grants and Financial Allocation Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-006 |
| **Feature Name** | Grants and Financial Allocation Management |
| **Module** | 06 — Office & Administration (Visitor, Reception and Meetings) |

### Description
Finance/admin officer records a grant or internal allocation, submits for competent approval, tracks utilisation against later expenses.

### Business Objective
Approved allocation before spending.

### Actors
Applicant: Finance or office administration officer. Approver: Competent financial Post per template. Other: Utilising office. Auditor.

### User Journey
1. Who creates: Finance or office administration officer.
2. How they create: Opens Grants → New: source, amount, period, receiving office, purpose, Save draft.
3. How they edit: Draft/Returned editable. After Approve, amount increase is a new allocation; decrease is a revision request.
4. How they send for approval: Submit to competent Post.
5. How the approver sees pending items: Approver grant inbox.
6. How the approver decides: Approve or reject. Utilisation is updated from tagged office expenses (F11-001) read-only here.
7. How the applicant sees history: Allocation and revision history plus utilisation to date.
8. How the approver sees history: Approved allocations.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own grant allocation history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My grant allocation register | Medium |
| Grant allocation form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver grant allocation inbox | Complex |
| Grant allocation decision panel (approve / reject / return) | Medium |
| My grant allocation history | Medium |
| Team grant allocation history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft grant allocation | Medium |
| Update draft grant allocation | Medium |
| Submit grant allocation for approval | Complex |
| Withdraw grant allocation | Easy |
| Approver inbox query | Medium |
| Approve, reject or return grant allocation | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Read utilisation from expenses | Medium |

### Inputs
Source, amount, period, office, purpose.

### Outputs
Persisted grant allocation with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own grant allocation.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount > 0.
- Office mandatory.

### Calculations
Remaining = approved amount − utilised (from tagged expenses).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Grant order.

### Reports
Allocation vs utilisation.

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
| My grant allocation register | UI | Medium | 6 |
| Grant allocation form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver grant allocation inbox | UI | Complex | 12 |
| Grant allocation decision panel (approve / reject / return) | UI | Medium | 6 |
| My grant allocation history | UI | Medium | 6 |
| Team grant allocation history (approver) | UI | Medium | 6 |
| Save draft grant allocation | API | Medium | 6 |
| Update draft grant allocation | API | Medium | 6 |
| Submit grant allocation for approval | API | Complex | 8 |
| Withdraw grant allocation | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return grant allocation | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Read utilisation from expenses | API | Medium | 6 |
| Grant allocation record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on grant allocation status change | Integration | Simple | 4 |
| Grants and Financial Allocation Management feature tests | Testing | Complex | 8 |
| Grants and Financial Allocation Management implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
