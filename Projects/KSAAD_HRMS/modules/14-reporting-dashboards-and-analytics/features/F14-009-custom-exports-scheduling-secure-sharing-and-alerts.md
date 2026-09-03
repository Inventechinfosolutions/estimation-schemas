# F14-009 — Custom Exports, Scheduling, Secure Sharing and Alerts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-009 |
| **Feature Name** | Custom Exports, Scheduling, Secure Sharing and Alerts |
| **Module** | 14 — Reporting, Dashboards & Analytics |

### Description
User saves a report filter, schedules export, shares to Posts; checker approves schedules that leave the organisation; alerts fire on thresholds.

### Business Objective
Controlled distribution.

### Actors
Applicant: Report user creates schedule/share. Approver: MIS Checker for external/email schedules. Internal Post share may auto-grant. Other: Recipients. Auditor.

### User Journey
1. Who creates: Report user creates schedule/share.
2. How they create: From a report → Schedule: frequency, format, recipients Posts, optional threshold alert, Save draft.
3. How they edit: Draft editable. After approve, pause/resume with history.
4. How they send for approval: Submit schedule if leaving staff app (email). Internal share Save.
5. How the approver sees pending items: Checker schedule inbox. Recipients see Shared reports.
6. How the approver decides: Approve/reject schedule. Threshold alerts notify without a decision.
7. How the applicant sees history: Schedule runs (success/fail).
8. How the approver sees history: Approved schedules.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own scheduled export history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My scheduled export register | Medium |
| Scheduled export form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver scheduled export inbox | Complex |
| Scheduled export decision panel (approve / reject / return) | Medium |
| My scheduled export history | Medium |
| Team scheduled export history (approver) | Medium |
| Schedule form | Complex |
| Alert rule form | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft scheduled export | Medium |
| Update draft scheduled export | Medium |
| Submit scheduled export for approval | Complex |
| Withdraw scheduled export | Easy |
| Approver inbox query | Medium |
| Approve, reject or return scheduled export | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Run scheduled export | Complex |
| Send to recipients | Medium |

### Inputs
Filter, frequency, format, recipients, threshold.

### Outputs
Persisted scheduled export with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own scheduled export.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Recipient not empty.
- Frequency mandatory.

### Calculations
Alert if metric compared to threshold.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Exported files.

### Reports
Schedule run log.

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
| My scheduled export register | UI | Medium | 6 |
| Scheduled export form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver scheduled export inbox | UI | Complex | 12 |
| Scheduled export decision panel (approve / reject / return) | UI | Medium | 6 |
| My scheduled export history | UI | Medium | 6 |
| Team scheduled export history (approver) | UI | Medium | 6 |
| Schedule form | UI | Complex | 12 |
| Alert rule form | UI | Medium | 6 |
| Save draft scheduled export | API | Medium | 6 |
| Update draft scheduled export | API | Medium | 6 |
| Submit scheduled export for approval | API | Complex | 8 |
| Withdraw scheduled export | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return scheduled export | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Run scheduled export | API | Complex | 8 |
| Send to recipients | API | Medium | 6 |
| Scheduled export record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on scheduled export status change | Integration | Simple | 4 |
| Custom Exports, Scheduling, Secure Sharing and Alerts feature tests | Testing | Complex | 8 |
| Custom Exports, Scheduling, Secure Sharing and Alerts implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **151** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
