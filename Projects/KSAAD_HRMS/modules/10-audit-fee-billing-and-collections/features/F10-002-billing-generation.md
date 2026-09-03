# F10-002 — Billing Generation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | Billing Generation |
| **Module** | 10 — Audit Fee, Billing and Collections |

### Description
Officer generates a bill from an approved assessment; checker approves the bill before dispatch.

### Business Objective
Bill tied to assessment.

### Actors
Applicant: Accounts officer. Approver: Accounts checker. Other: Institution. Auditor.

### User Journey
1. Who creates: Accounts officer.
2. How they create: Select approved assessment(s) → Generate bill, review lines, Save draft.
3. How they edit: Draft editable (period/narrative). Amounts come from assessment; changing amount requires assessment revision.
4. How they send for approval: Submit bill for checker.
5. How the approver sees pending items: Checker bill inbox.
6. How the approver decides: Approve or return.
7. How the applicant sees history: Bills and versions.
8. How the approver sees history: Approved bills.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own audit fee bill history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My audit fee bill register | Medium |
| Audit fee bill form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver audit fee bill inbox | Complex |
| Audit fee bill decision panel (approve / reject / return) | Medium |
| My audit fee bill history | Medium |
| Team audit fee bill history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft audit fee bill | Medium |
| Update draft audit fee bill | Medium |
| Submit audit fee bill for approval | Complex |
| Withdraw audit fee bill | Easy |
| Approver inbox query | Medium |
| Approve, reject or return audit fee bill | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Generate bill number | Easy |

### Inputs
Assessment, bill lines, bill date.

### Outputs
Persisted audit fee bill with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own audit fee bill.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Assessment must be approved.
- Cannot bill twice for same assessment version without a supplementary type.

### Calculations
Bill total = sum(lines).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Bill PDF.

### Reports
Bills generated.

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
| My audit fee bill register | UI | Medium | 6 |
| Audit fee bill form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver audit fee bill inbox | UI | Complex | 12 |
| Audit fee bill decision panel (approve / reject / return) | UI | Medium | 6 |
| My audit fee bill history | UI | Medium | 6 |
| Team audit fee bill history (approver) | UI | Medium | 6 |
| Save draft audit fee bill | API | Medium | 6 |
| Update draft audit fee bill | API | Medium | 6 |
| Submit audit fee bill for approval | API | Complex | 8 |
| Withdraw audit fee bill | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return audit fee bill | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Generate bill number | API | Easy | 4 |
| Audit fee bill record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on audit fee bill status change | Integration | Simple | 4 |
| Billing Generation feature tests | Testing | Complex | 8 |
| Billing Generation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **123** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
