# F04-001 — Deputation Proposal Initiation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Deputation Proposal Initiation |
| **Module** | 04 — Deputation & Posting Management |

### Description
HR or the supervising officer raises a deputation proposal for a Person to a target office/Post.

### Business Objective
Capture a complete proposal before approval and tenure tracking.

### Actors
Applicant: HR Establishment Officer or the Person's current supervising Post. Approver: Competent deputation-approving Post per workflow template (often HO establishment). Other: The Person proposed (read of own case). Auditor.

### User Journey
1. Who creates: HR Establishment Officer or the Person's current supervising Post.
2. How they create: Applicant opens Deputation → New proposal, selects Person, current Post, target office/Post, proposed start, tenure months, justification, Save draft.
3. How they edit: Draft/Returned editable. After Submit, identity fields freeze; only Withdraw before first decision.
4. How they send for approval: Submit routes to the competent Post. Does not yet change F01-003 mappings.
5. How the approver sees pending items: Approver deputation inbox (pending proposals).
6. How the approver decides: This feature stops at submitting a valid proposal. Decision is F04-002. If a checker is configured at intake, they Confirm completeness or Return.
7. How the applicant sees history: Applicant sees proposal drafts and submitted status.
8. How the approver sees history: Intake checker sees completeness decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own deputation proposal history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My deputation proposal register | Medium |
| Deputation proposal form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver deputation proposal inbox | Complex |
| Deputation proposal decision panel (approve / reject / return) | Medium |
| My deputation proposal history | Medium |
| Team deputation proposal history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft deputation proposal | Medium |
| Update draft deputation proposal | Medium |
| Submit deputation proposal for approval | Complex |
| Withdraw deputation proposal | Easy |
| Approver inbox query | Medium |
| Approve, reject or return deputation proposal | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Person, current Post, target office/Post, start date, tenure, justification, attachments.

### Outputs
Persisted deputation proposal with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own deputation proposal.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Person must have a current mapping.
- Target Post mandatory.
- Start date mandatory.

### Calculations
Proposed end date = start + tenure months (editable).

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Consent/office correspondence attachments.

### Reports
Open proposals by office.

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
| My deputation proposal register | UI | Medium | 6 |
| Deputation proposal form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver deputation proposal inbox | UI | Complex | 12 |
| Deputation proposal decision panel (approve / reject / return) | UI | Medium | 6 |
| My deputation proposal history | UI | Medium | 6 |
| Team deputation proposal history (approver) | UI | Medium | 6 |
| Save draft deputation proposal | API | Medium | 6 |
| Update draft deputation proposal | API | Medium | 6 |
| Submit deputation proposal for approval | API | Complex | 8 |
| Withdraw deputation proposal | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return deputation proposal | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Deputation proposal record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on deputation proposal status change | Integration | Simple | 4 |
| Deputation Proposal Initiation feature tests | Testing | Complex | 8 |
| Deputation Proposal Initiation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
