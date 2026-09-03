# F14-008 — Advanced Analytics, MIS and Compliance Reporting

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-008 |
| **Feature Name** | Advanced Analytics, MIS and Compliance Reporting |
| **Module** | 14 — Reporting, Dashboards & Analytics |

### Description
MIS officer builds a compliance/MIS pack (period, office), submits for internal release if required; history of released packs.

### Business Objective
Repeatable MIS/compliance outputs.

### Actors
Applicant: MIS officer. Checker if internal release required. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: MIS officer. Checker if internal release required.
2. How they create: MIS → New pack: period, offices, included reports, Save draft, Generate.
3. How they edit: Regenerate while draft. Released packs are frozen; new period = new pack.
4. How they send for approval: Submit for release if configured.
5. How the approver sees pending items: Checker MIS-pack inbox.
6. How the approver decides: Approve release or return.
7. How the applicant sees history: Packs and generate logs.
8. How the approver sees history: Released packs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own MIS/compliance pack history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My MIS/compliance pack register | Medium |
| Mis/compliance pack form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver MIS/compliance pack inbox | Complex |
| Mis/compliance pack decision panel (approve / reject / return) | Medium |
| My MIS/compliance pack history | Medium |
| Team MIS/compliance pack history (approver) | Medium |
| Pack builder | Complex |
| Generate progress | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft MIS/compliance pack | Medium |
| Update draft MIS/compliance pack | Medium |
| Submit MIS/compliance pack for approval | Complex |
| Withdraw MIS/compliance pack | Easy |
| Approver inbox query | Medium |
| Approve, reject or return MIS/compliance pack | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Generate pack | Very High |

### Inputs
Period, office scope, report list.

### Outputs
Persisted MIS/compliance pack with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own MIS/compliance pack.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Period mandatory.

### Calculations
As per included reports.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Exported pack files.

### Reports
This feature produces them.

### Notifications
Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.

### Security
Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.

### Integrations
Internal identity (Module 01) and notification service. Document store when attachments are required.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

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
| My MIS/compliance pack register | UI | Medium | 6 |
| Mis/compliance pack form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver MIS/compliance pack inbox | UI | Complex | 12 |
| Mis/compliance pack decision panel (approve / reject / return) | UI | Medium | 6 |
| My MIS/compliance pack history | UI | Medium | 6 |
| Team MIS/compliance pack history (approver) | UI | Medium | 6 |
| Pack builder | UI | Complex | 12 |
| Generate progress | UI | Easy | 4 |
| Save draft MIS/compliance pack | API | Medium | 6 |
| Update draft MIS/compliance pack | API | Medium | 6 |
| Submit MIS/compliance pack for approval | API | Complex | 8 |
| Withdraw MIS/compliance pack | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return MIS/compliance pack | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Generate pack | API | Very High | 16 |
| Mis/compliance pack record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on MIS/compliance pack status change | Integration | Simple | 4 |
| Advanced Analytics, MIS and Compliance Reporting feature tests | Testing | Complex | 8 |
| Advanced Analytics, MIS and Compliance Reporting implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
