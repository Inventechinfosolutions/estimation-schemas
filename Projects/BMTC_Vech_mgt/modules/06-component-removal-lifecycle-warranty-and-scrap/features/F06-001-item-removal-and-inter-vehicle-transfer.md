# F06-001 — Item Removal and Inter-Vehicle Transfer

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Item Removal and Inter-Vehicle Transfer |
| **Module** | 06 — Component Removal, Lifecycle, Warranty and Scrap |

### Description
Mechanical Clerk records who removed an item, when, reason, condition, source vehicle and destination vehicle if refitted.

### Business Objective
FR-M-14, FR-M-15.

### Actors
Applicant: Mechanical Clerk. Approver: Tech. Supervisor. Other: Store Clerk (receives reusable). Auditor.

### User Journey
1. Who creates: Mechanical Clerk.
2. How they create: Vehicle or job card → Removal → New: item, source vehicle, reason, condition, destination vehicle if any, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to Tech. Supervisor.
5. How the approver sees pending items: Supervisor removal inbox.
6. How the approver decides: Approve (routes stock per F06-002/003) or Return.
7. How the applicant sees history: Removal history on item and vehicles.
8. How the approver sees history: Decided removals.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own removal record history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My removal record register | Medium |
| Removal record form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver removal record inbox | Complex |
| Removal record decision panel (approve / reject / return) | Medium |
| My removal record history | Medium |
| Team removal record history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft removal record | Medium |
| Update draft removal record | Medium |
| Submit removal record for approval | Complex |
| Withdraw removal record | Easy |
| Approver inbox query | Medium |
| Approve, reject or return removal record | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Item, vehicles, reason, condition, datetime, person.

### Outputs
Persisted removal record with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own removal record.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Source vehicle mandatory.
- Condition mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional photo of removed item.

### Reports
Removals by depot.

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
| My removal record register | UI | Medium | 6 |
| Removal record form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver removal record inbox | UI | Complex | 12 |
| Removal record decision panel (approve / reject / return) | UI | Medium | 6 |
| My removal record history | UI | Medium | 6 |
| Team removal record history (approver) | UI | Medium | 6 |
| Save draft removal record | API | Medium | 6 |
| Update draft removal record | API | Medium | 6 |
| Submit removal record for approval | API | Complex | 8 |
| Withdraw removal record | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return removal record | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Removal record record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on removal record status change | Integration | Simple | 4 |
| Item Removal and Inter-Vehicle Transfer feature tests | Testing | Complex | 8 |
| Item Removal and Inter-Vehicle Transfer implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
