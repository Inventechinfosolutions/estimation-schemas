# F14-003 — Role-based Dashboards and Accounts Views

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-003 |
| **Feature Name** | Role-based Dashboards and Accounts Views |
| **Module** | 14 — Reporting and Dashboards |

### Description
Role-based dashboards: fleet status, stock alerts, open job cards, procurement, fuel efficiency (FR-X-07). Accounts section reports and login (FR-X-09). Auto-refresh live data.

### Business Objective
Operational and accounts oversight.

### Actors
Applicant: CME, COSP, Depot Managers, senior management, Accounts Posts. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: CME, COSP, Depot Managers, senior management, Accounts Posts.
2. How they create: Admin: dashboard definition for a Role, Save draft. User: open My Dashboard, filter, drill to register.
3. How they edit: Definition versions maker–checker. Users only change filters.
4. How they send for approval: Definition submit to MIS Checker.
5. How the approver sees pending items: Checker definition inbox.
6. How the approver decides: Approve definition go-live.
7. How the applicant sees history: Definition versions.
8. How the approver sees history: Approved definitions.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own dashboard view history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My dashboard view register | Medium |
| Dashboard view form (create and edit) | Very High |
| Submit confirmation | Simple |
| Approver dashboard view inbox | Complex |
| Dashboard view decision panel (approve / reject / return) | Medium |
| My dashboard view history | Medium |
| Team dashboard view history (approver) | Medium |
| Dashboard canvas | Very High |
| Accounts audit reports | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft dashboard view | Medium |
| Update draft dashboard view | Medium |
| Submit dashboard view for approval | Complex |
| Withdraw dashboard view | Easy |
| Approver inbox query | Medium |
| Approve, reject or return dashboard view | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Query widget data | Very High |
| Run accounts audit reports | Complex |

### Inputs
Widgets, audience Role, filters.

### Outputs
Persisted dashboard view with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own dashboard view.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- Audience Role mandatory.

### Calculations
Widget metrics from live modules.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
None.

### Reports
N/A.

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
| My dashboard view register | UI | Medium | 6 |
| Dashboard view form (create and edit) | UI | Very High | 16 |
| Submit confirmation | UI | Simple | 2 |
| Approver dashboard view inbox | UI | Complex | 12 |
| Dashboard view decision panel (approve / reject / return) | UI | Medium | 6 |
| My dashboard view history | UI | Medium | 6 |
| Team dashboard view history (approver) | UI | Medium | 6 |
| Dashboard canvas | UI | Very High | 16 |
| Accounts audit reports | UI | Complex | 12 |
| Save draft dashboard view | API | Medium | 6 |
| Update draft dashboard view | API | Medium | 6 |
| Submit dashboard view for approval | API | Complex | 8 |
| Withdraw dashboard view | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return dashboard view | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Query widget data | API | Very High | 16 |
| Run accounts audit reports | API | Complex | 8 |
| Dashboard view record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on dashboard view status change | Integration | Simple | 4 |
| Role-based Dashboards and Accounts Views feature tests | Testing | Very High | 12 |
| Role-based Dashboards and Accounts Views implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **179** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
