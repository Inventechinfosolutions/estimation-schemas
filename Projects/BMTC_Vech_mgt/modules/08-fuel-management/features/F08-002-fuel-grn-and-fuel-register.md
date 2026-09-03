# F08-002 — Fuel GRN and Fuel Register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Fuel GRN and Fuel Register |
| **Module** | 08 — Fuel Management |

### Description
Fuel clerk records supplier GRN; the fuel register shows cumulative receipts, issues and closing balance.

### Business Objective
FR-M-32, FR-M-34.

### Actors
Applicant: Fuel Clerk. Approver: Depot Manager / Stores Officer as configured. Other: Auditor. Accounts (read of register).

### User Journey
1. Who creates: Fuel Clerk.
2. How they create: Fuel GRN → New: supplier, HSD qty, date, UGT, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to approver. On approve, register receipt increases.
5. How the approver sees pending items: Approver fuel-GRN inbox.
6. How the approver decides: Approve or reject.
7. How the applicant sees history: GRN history and register movements.
8. How the approver sees history: Decided GRNs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own fuel GRN history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My fuel GRN register | Medium |
| Fuel grn form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver fuel GRN inbox | Complex |
| Fuel grn decision panel (approve / reject / return) | Medium |
| My fuel GRN history | Medium |
| Team fuel GRN history (approver) | Medium |
| Fuel register | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft fuel GRN | Medium |
| Update draft fuel GRN | Medium |
| Submit fuel GRN for approval | Complex |
| Withdraw fuel GRN | Easy |
| Approver inbox query | Medium |
| Approve, reject or return fuel GRN | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Post receipt to fuel register | Complex |

### Inputs
Supplier, qty, UGT, date.

### Outputs
Persisted fuel GRN with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own fuel GRN.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Qty > 0.
- UGT mandatory.

### Calculations
Closing balance = opening + receipts − issues.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Supplier invoice optional.

### Reports
Fuel register.

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
| My fuel GRN register | UI | Medium | 6 |
| Fuel grn form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver fuel GRN inbox | UI | Complex | 12 |
| Fuel grn decision panel (approve / reject / return) | UI | Medium | 6 |
| My fuel GRN history | UI | Medium | 6 |
| Team fuel GRN history (approver) | UI | Medium | 6 |
| Fuel register | UI | Complex | 12 |
| Save draft fuel GRN | API | Medium | 6 |
| Update draft fuel GRN | API | Medium | 6 |
| Submit fuel GRN for approval | API | Complex | 8 |
| Withdraw fuel GRN | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return fuel GRN | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Post receipt to fuel register | API | Complex | 8 |
| Fuel grn record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on fuel GRN status change | Integration | Simple | 4 |
| Fuel GRN and Fuel Register feature tests | Testing | Complex | 8 |
| Fuel GRN and Fuel Register implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **139** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
