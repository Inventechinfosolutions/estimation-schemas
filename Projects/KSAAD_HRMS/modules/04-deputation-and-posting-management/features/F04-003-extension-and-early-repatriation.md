# F04-003 — Extension and Early Repatriation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Extension and Early Repatriation |
| **Module** | 04 — Deputation & Posting Management |

### Description
HR requests extension or early repatriation; competent Post decides; tenure and mappings update on approval.

### Business Objective
Change an approved deputation without editing history silently.

### Actors
Applicant: HR Establishment Officer on an Active deputation. Approver: Same class of competent Post as F04-002. Other: Person. Auditor.

### User Journey
1. Who creates: HR Establishment Officer on an Active deputation.
2. How they create: Officer opens the Active deputation → Request extension or Early repatriation, enters new end date or repatriation date and reason, Save draft.
3. How they edit: Draft/Returned editable. Cannot change the original approval; this is a new request linked to it.
4. How they send for approval: Submit to competent Post.
5. How the approver sees pending items: Approver change-request inbox.
6. How the approver decides: Approve (updates tenure end / triggers mapping revert) or Reject.
7. How the applicant sees history: Full chain: original approval + extensions + repatriation.
8. How the approver sees history: Decisions on change requests.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own deputation change request history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My deputation change request register | Medium |
| Deputation change request form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver deputation change request inbox | Complex |
| Deputation change request decision panel (approve / reject / return) | Medium |
| My deputation change request history | Medium |
| Team deputation change request history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft deputation change request | Medium |
| Update draft deputation change request | Medium |
| Submit deputation change request for approval | Complex |
| Withdraw deputation change request | Easy |
| Approver inbox query | Medium |
| Approve, reject or return deputation change request | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Linked deputation, change type, new date, reason.

### Outputs
Persisted deputation change request with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own deputation change request.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- New end date after current start.
- Repatriation date not in the future beyond policy.

### Calculations
None beyond new remaining tenure.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Change order.

### Reports
Extensions and early repatriations in a period.

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
| My deputation change request register | UI | Medium | 6 |
| Deputation change request form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver deputation change request inbox | UI | Complex | 12 |
| Deputation change request decision panel (approve / reject / return) | UI | Medium | 6 |
| My deputation change request history | UI | Medium | 6 |
| Team deputation change request history (approver) | UI | Medium | 6 |
| Save draft deputation change request | API | Medium | 6 |
| Update draft deputation change request | API | Medium | 6 |
| Submit deputation change request for approval | API | Complex | 8 |
| Withdraw deputation change request | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return deputation change request | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Deputation change request record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on deputation change request status change | Integration | Simple | 4 |
| Extension and Early Repatriation feature tests | Testing | Complex | 8 |
| Extension and Early Repatriation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
