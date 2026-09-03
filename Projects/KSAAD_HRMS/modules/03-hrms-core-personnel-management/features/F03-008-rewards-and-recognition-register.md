# F03-008 — Rewards and Recognition Register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-008 |
| **Feature Name** | Rewards and Recognition Register |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
A supervisor proposes a reward for a Person; competent Post approves; the register and history are visible to HR and the Person.

### Business Objective
Record rewards with approval, not informal notes.

### Actors
Applicant: Supervising Post (or HR) raises the proposal against a Person. Approver: Competent authority Post per workflow template. Other: Nominee Person (sees approved rewards). Auditor.

### User Journey
1. Who creates: Supervising Post (or HR) raises the proposal against a Person.
2. How they create: Applicant opens Rewards → New, selects Person, reward type, citation, date, Save draft.
3. How they edit: Draft/Returned editable. Approved entries are not rewritten; cancellations are a new action with reason.
4. How they send for approval: Submit to competent Post.
5. How the approver sees pending items: Approver rewards inbox.
6. How the approver decides: Approve or reject with remarks.
7. How the applicant sees history: Proposer sees proposal history. Person sees own approved rewards.
8. How the approver sees history: Approver sees decided proposals.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own reward proposal history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My reward proposal register | Medium |
| Reward proposal form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver reward proposal inbox | Complex |
| Reward proposal decision panel (approve / reject / return) | Medium |
| My reward proposal history | Medium |
| Team reward proposal history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft reward proposal | Medium |
| Update draft reward proposal | Medium |
| Submit reward proposal for approval | Complex |
| Withdraw reward proposal | Easy |
| Approver inbox query | Medium |
| Approve, reject or return reward proposal | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Person, reward type, citation, proposed date, remarks.

### Outputs
Persisted reward proposal with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own reward proposal.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Person and reward type mandatory.
- Citation mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional citation attachment.

### Reports
Rewards by office and year.

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
| My reward proposal register | UI | Medium | 6 |
| Reward proposal form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver reward proposal inbox | UI | Complex | 12 |
| Reward proposal decision panel (approve / reject / return) | UI | Medium | 6 |
| My reward proposal history | UI | Medium | 6 |
| Team reward proposal history (approver) | UI | Medium | 6 |
| Save draft reward proposal | API | Medium | 6 |
| Update draft reward proposal | API | Medium | 6 |
| Submit reward proposal for approval | API | Complex | 8 |
| Withdraw reward proposal | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return reward proposal | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Reward proposal record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on reward proposal status change | Integration | Simple | 4 |
| Rewards and Recognition Register feature tests | Testing | Complex | 8 |
| Rewards and Recognition Register implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
