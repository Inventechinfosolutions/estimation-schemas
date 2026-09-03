# F15-001 — Knowledge Repository and Articles

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-001 |
| **Feature Name** | Knowledge Repository and Articles |
| **Module** | 15 — Knowledge Center & Learning |

### Description
Author drafts an article, submits to knowledge owner Post; after publish, staff search and read; versions kept.

### Business Objective
Reviewed operational knowledge.

### Actors
Applicant: Author with Knowledge Role. Approver: Knowledge owner Post. Other: Staff readers. Auditor.

### User Journey
1. Who creates: Author with Knowledge Role.
2. How they create: Knowledge → New article: title, body, tags, Save draft.
3. How they edit: Draft/Returned editable. After publish, edit = new version submitted again.
4. How they send for approval: Submit for publish.
5. How the approver sees pending items: Owner article inbox.
6. How the approver decides: Publish or return. Unpublish with reason.
7. How the applicant sees history: Article versions.
8. How the approver sees history: Publish decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own knowledge article history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My knowledge article register | Medium |
| Knowledge article form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver knowledge article inbox | Complex |
| Knowledge article decision panel (approve / reject / return) | Medium |
| My knowledge article history | Medium |
| Team knowledge article history (approver) | Medium |
| Article editor | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft knowledge article | Medium |
| Update draft knowledge article | Medium |
| Submit knowledge article for approval | Complex |
| Withdraw knowledge article | Easy |
| Approver inbox query | Medium |
| Approve, reject or return knowledge article | Complex |
| Applicant history query | Medium |
| Team history query | Medium |

### Inputs
Title, body, tags, audience optional.

### Outputs
Persisted knowledge article with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own knowledge article.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Title and body mandatory.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Optional attachments.

### Reports
Published articles by tag.

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
| My knowledge article register | UI | Medium | 6 |
| Knowledge article form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver knowledge article inbox | UI | Complex | 12 |
| Knowledge article decision panel (approve / reject / return) | UI | Medium | 6 |
| My knowledge article history | UI | Medium | 6 |
| Team knowledge article history (approver) | UI | Medium | 6 |
| Article editor | UI | Complex | 12 |
| Save draft knowledge article | API | Medium | 6 |
| Update draft knowledge article | API | Medium | 6 |
| Submit knowledge article for approval | API | Complex | 8 |
| Withdraw knowledge article | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return knowledge article | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Knowledge article record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on knowledge article status change | Integration | Simple | 4 |
| Knowledge Repository and Articles feature tests | Testing | Complex | 8 |
| Knowledge Repository and Articles implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **131** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
