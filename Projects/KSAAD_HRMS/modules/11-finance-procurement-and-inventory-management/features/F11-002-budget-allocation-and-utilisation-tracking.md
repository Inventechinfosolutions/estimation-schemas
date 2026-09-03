# F11-002 — Budget Allocation and Utilisation Tracking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-002 |
| **Feature Name** | Budget Allocation and Utilisation Tracking |
| **Module** | 11 — Finance, Procurement & Inventory Management |

### Description
Finance officer enters budget for office/head/year; checker approves; utilisation is derived from approved expenses/POs.

### Business Objective
See remaining budget before spend.

### Actors
Applicant: Finance officer. Approver: Finance checker / competent Post. Other: Spending offices (read remaining). Auditor.

### User Journey
1. Who creates: Finance officer.
2. How they create: Opens Budget → New: year, office, head, amount, Save draft.
3. How they edit: Draft editable. After approve, increase/decrease is a revision request.
4. How they send for approval: Submit allocation/revision.
5. How the approver sees pending items: Checker budget inbox.
6. How the approver decides: Approve or reject. Utilisation is read-only from tagged approved spend.
7. How the applicant sees history: Allocation versions and utilisation.
8. How the approver sees history: Approved budgets.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own budget allocation history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My budget allocation register | Medium |
| Budget allocation form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver budget allocation inbox | Complex |
| Budget allocation decision panel (approve / reject / return) | Medium |
| My budget allocation history | Medium |
| Team budget allocation history (approver) | Medium |
| Utilisation panel | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft budget allocation | Medium |
| Update draft budget allocation | Medium |
| Submit budget allocation for approval | Complex |
| Withdraw budget allocation | Easy |
| Approver inbox query | Medium |
| Approve, reject or return budget allocation | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Compute utilisation | Complex |

### Inputs
Year, office, head, amount.

### Outputs
Persisted budget allocation with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own budget allocation.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Amount ≥ 0.
- Year and head mandatory.

### Calculations
Remaining = approved budget − utilisation from approved expenses/POs tagged to the head.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Budget order.

### Reports
Budget vs actual.

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
| My budget allocation register | UI | Medium | 6 |
| Budget allocation form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver budget allocation inbox | UI | Complex | 12 |
| Budget allocation decision panel (approve / reject / return) | UI | Medium | 6 |
| My budget allocation history | UI | Medium | 6 |
| Team budget allocation history (approver) | UI | Medium | 6 |
| Utilisation panel | UI | Medium | 6 |
| Save draft budget allocation | API | Medium | 6 |
| Update draft budget allocation | API | Medium | 6 |
| Submit budget allocation for approval | API | Complex | 8 |
| Withdraw budget allocation | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return budget allocation | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Compute utilisation | API | Complex | 8 |
| Budget allocation record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on budget allocation status change | Integration | Simple | 4 |
| Budget Allocation and Utilisation Tracking feature tests | Testing | Complex | 8 |
| Budget Allocation and Utilisation Tracking implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **133** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
