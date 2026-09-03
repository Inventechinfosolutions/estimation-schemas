# F15-003 — Learning Content and Catalogue

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-003 |
| **Feature Name** | Learning Content and Catalogue |
| **Module** | 15 — Knowledge Center & Learning |

### Description
Training officer adds a course/content item to the catalogue, submits for publish; staff browse catalogue.

### Business Objective
Catalogue of learning items.

### Actors
Applicant: Training Officer. Approver: Training supervisor / knowledge owner. Other: Staff. Auditor.

### User Journey
1. Who creates: Training Officer.
2. How they create: Catalogue → New item: title, type, duration, material, Save draft.
3. How they edit: Draft editable. After publish, update is a version.
4. How they send for approval: Submit to publish in catalogue.
5. How the approver sees pending items: Approver catalogue inbox.
6. How the approver decides: Publish or return.
7. How the applicant sees history: Item versions.
8. How the approver sees history: Published items.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own learning item history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My learning item register | Medium |
| Learning item form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver learning item inbox | Complex |
| Learning item decision panel (approve / reject / return) | Medium |
| My learning item history | Medium |
| Team learning item history (approver) | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft learning item | Medium |
| Update draft learning item | Medium |
| Submit learning item for approval | Complex |
| Withdraw learning item | Easy |
| Approver inbox query | Medium |
| Approve, reject or return learning item | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Title, type, duration, material.

### Outputs
Persisted learning item with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own learning item.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Title mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Learning material via DMS.

### Reports
Catalogue listing.

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
| My learning item register | UI | Medium | 6 |
| Learning item form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver learning item inbox | UI | Complex | 12 |
| Learning item decision panel (approve / reject / return) | UI | Medium | 6 |
| My learning item history | UI | Medium | 6 |
| Team learning item history (approver) | UI | Medium | 6 |
| Save draft learning item | API | Medium | 6 |
| Update draft learning item | API | Medium | 6 |
| Submit learning item for approval | API | Complex | 8 |
| Withdraw learning item | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return learning item | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Learning item record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on learning item status change | Integration | Simple | 4 |
| Learning Content and Catalogue feature tests | Testing | Complex | 8 |
| Learning Content and Catalogue implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **119** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
