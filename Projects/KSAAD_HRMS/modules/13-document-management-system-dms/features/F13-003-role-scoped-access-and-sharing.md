# F13-003 — Role-Scoped Access and Sharing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-003 |
| **Feature Name** | Role-Scoped Access and Sharing |
| **Module** | 13 — Document Management System (DMS) |

### Description
Owner Post shares a document to another Post/Person with view or download; checker may be required for download of sensitive types; revoke is history.

### Business Objective
Need-to-know on evidence.

### Actors
Applicant: Person whose Post owns the parent (or DMS admin). Approver: Information owner / checker if document type is restricted. Other: Share target. Auditor.

### User Journey
1. Who creates: Person whose Post owns the parent (or DMS admin).
2. How they create: On document → Share: select Post/Person, right (view/download), expiry optional, Save draft.
3. How they edit: Draft share editable. After grant, change rights is a new share/revoke.
4. How they send for approval: Submit if restricted type; else Save grants immediately.
5. How the approver sees pending items: Checker share inbox for restricted types. Target sees Shared with me.
6. How the approver decides: Approve share or reject. Revoke is immediate by owner with reason.
7. How the applicant sees history: Share and revoke log on the document.
8. How the approver sees history: Approved shares.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own document share history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My document share register | Medium |
| Document share form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver document share inbox | Complex |
| Document share decision panel (approve / reject / return) | Medium |
| My document share history | Medium |
| Team document share history (approver) | Medium |
| Share dialog | Medium |
| Shared with me | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft document share | Medium |
| Update draft document share | Medium |
| Submit document share for approval | Complex |
| Withdraw document share | Easy |
| Approver inbox query | Medium |
| Approve, reject or return document share | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Grant access | Complex |
| Revoke access | Easy |
| Authorise download | Complex |

### Inputs
Document, target, right, expiry.

### Outputs
Persisted document share with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own document share.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Target mandatory.
- Cannot share wider than owner's own right.

### Calculations
None.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
N/A.

### Reports
Download/view audit (also F13-005).

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
| My document share register | UI | Medium | 6 |
| Document share form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver document share inbox | UI | Complex | 12 |
| Document share decision panel (approve / reject / return) | UI | Medium | 6 |
| My document share history | UI | Medium | 6 |
| Team document share history (approver) | UI | Medium | 6 |
| Share dialog | UI | Medium | 6 |
| Shared with me | UI | Easy | 4 |
| Save draft document share | API | Medium | 6 |
| Update draft document share | API | Medium | 6 |
| Submit document share for approval | API | Complex | 8 |
| Withdraw document share | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return document share | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Grant access | API | Complex | 8 |
| Revoke access | API | Easy | 4 |
| Authorise download | API | Complex | 8 |
| Document share record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on document share status change | Integration | Simple | 4 |
| Role-Scoped Access and Sharing feature tests | Testing | Complex | 8 |
| Role-Scoped Access and Sharing implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **149** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
