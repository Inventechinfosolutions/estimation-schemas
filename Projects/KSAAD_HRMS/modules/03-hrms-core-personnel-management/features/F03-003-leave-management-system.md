# F03-003 — Leave Management System

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Leave Management System |
| **Module** | 03 — HRMS Core Personnel Management |

### Description
The staff member applies for leave against their current Post. The reporting officer (Person mapped to the supervising Post) sees an inbox and approves, rejects or returns. Both see history.

### Business Objective
Replace informal leave with a Post-routed application, decision and history.

### Actors
Applicant: The staff member — the Person currently mapped to a Post — applies for their own leave. HR Establishment Officer may raise an application on behalf of a Person only with a recorded reason (e.g. person on medical emergency). Approver: The Person currently mapped to the supervising Post of the applicant's Post (Module 01). If that Person is on leave, the workflow template may route to the next supervising Post. Other: HR Establishment Officer (balances, on-behalf apply). Auditor (read-only).

### User Journey
1. Who creates: The staff member — the Person currently mapped to a Post — applies for their own leave. HR Establishment Officer may raise an application on behalf of a Person only with a recorded reason (e.g. person on medical emergency).
2. How they create: Applicant opens My Leave Applications → New. System shows Person name, current Post and leave balances. Applicant selects leave type, from date, to date (or first/second session), reason, optional attachment (medical certificate). Applicant clicks Save draft. The application is not visible in the approver inbox yet.
3. How they edit: Applicant opens a Draft or Returned application from My Leave Applications, changes dates/type/reason/attachment, Save. Submitted, Approved and Rejected applications cannot be edited. Applicant may Withdraw a Submitted application before the approver decides; Withdrawn applications are not decided.
4. How they send for approval: On the form, applicant clicks Submit. System checks: balance sufficient (or 'without balance' type allowed), no overlapping approved/pending leave, supervising Post resolved. On success, status becomes Submitted and the reporting officer receives an inbox item and notification. Applicant cannot submit if they are also the only mapped Person on the supervising Post (self-approval blocked); HR must route to the next Post.
5. How the approver sees pending items: Approver opens Approver Leave Inbox. Default filter: Pending, for Posts they currently supervise. Columns: applicant Person, Post, leave type, period, days, submitted on. Approver may filter by office, type and period. Approver clicks a row to open the read-only application plus balances and overlapping leave.
6. How the approver decides: On the decision panel the approver selects Approve, Reject or Return for correction. Reject and Return require remarks. Approve deducts balance (unless type does not debit). Return sets status Returned; applicant edits and resubmits. Approver cannot edit the applicant's dates; they decide or return.
7. How the applicant sees history: Applicant opens My Leave History (or the History tab on an application). Timeline shows Draft saved, Submitted, Returned, resubmitted, Approved/Rejected/Withdrawn — each with Person, Post, date-time and remarks. Applicant also sees year-wise balance (opening, credited, taken, closing).
8. How the approver sees history: Approver opens Team Leave History: applications they decided, and current pending for their Posts. They do not see leave of Persons outside their supervised Posts. Auditor with the access-log Role can see all leave decisions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own leave application history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My leave application register | Medium |
| Leave application form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver leave application inbox | Complex |
| Leave application decision panel (approve / reject / return) | Medium |
| My leave application history | Medium |
| Team leave application history (approver) | Medium |
| Leave balance panel on the form | Medium |
| Overlap warning dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft leave application | Medium |
| Update draft leave application | Medium |
| Submit leave application for approval | Complex |
| Withdraw leave application | Easy |
| Approver inbox query | Medium |
| Approve, reject or return leave application | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Get leave balance for Person | Medium |
| Check overlapping leave | Medium |
| Debit or restore leave balance | Complex |

### Inputs
Leave type, from date, to date, session, reason, attachment, on-behalf flag and reason (if HR applies), applicant Person and Post (system), current balance (system).

### Outputs
Persisted leave application with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own leave application.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.
- Balance is computed from credited leave and approved applications; pending applications reserve balance until decided.
- Overlapping periods with another pending or approved leave of the same Person are refused.
- Cancelled after approval is a separate action (if policy allows) and restores balance; it is not a silent edit.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- From date ≤ to date.
- Leave type mandatory and from the leave-type catalogue.
- Medical certificate mandatory when leave type requires it.
- Submit blocked when reserved+requested days exceed balance for debiting types.

### Calculations
Days = inclusive calendar days minus configured weekly offs/holidays when the leave type says so. On Submit, requested days are reserved. On Approve, reserved becomes taken. On Reject/Withdraw/Return, reserved is released. On Approve of a debiting type, closing balance decreases.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
Medical certificate or other proof when the leave type requires it, stored via DMS and linked to the application.

### Reports
Leave register by Person/office/type; pending inbox ageing; balance statement.

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
| My leave application register | UI | Medium | 6 |
| Leave application form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver leave application inbox | UI | Complex | 12 |
| Leave application decision panel (approve / reject / return) | UI | Medium | 6 |
| My leave application history | UI | Medium | 6 |
| Team leave application history (approver) | UI | Medium | 6 |
| Leave balance panel on the form | UI | Medium | 6 |
| Overlap warning dialog | UI | Simple | 2 |
| Save draft leave application | API | Medium | 6 |
| Update draft leave application | API | Medium | 6 |
| Submit leave application for approval | API | Complex | 8 |
| Withdraw leave application | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return leave application | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Get leave balance for Person | API | Medium | 6 |
| Check overlapping leave | API | Medium | 6 |
| Debit or restore leave balance | API | Complex | 8 |
| Leave application, status history, balance ledger and attachment links | DB | Complex | 6 |
| Notify applicant and approver on leave application status change | Integration | Simple | 4 |
| Leave Management System feature tests | Testing | Very High | 12 |
| Leave Management System implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **154** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
