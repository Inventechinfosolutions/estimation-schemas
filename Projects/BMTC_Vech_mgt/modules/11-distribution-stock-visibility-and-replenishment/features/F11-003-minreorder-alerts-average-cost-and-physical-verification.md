# F11-003 — Min/Reorder Alerts, Average Cost and Physical Verification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-003 |
| **Feature Name** | Min/Reorder Alerts, Average Cost and Physical Verification |
| **Module** | 11 — Distribution, Stock Visibility and Replenishment |

### Description
Alerts at min and reorder; monthly average cost valuation; physical count vs system with discrepancy reconciliation. Forecasting of material requirement from consumption (FR-X-05, FR-X-06).

### Business Objective
FR-S-16 to 19 and forecasting.

### Actors
Applicant: Store Officer receives alerts. Clerk posts PV. Checker approves PV discrepancy. Approver: Person currently mapped to the supervising Post, unless stated otherwise. Other: Auditor (read-only history).

### User Journey
1. Who creates: Store Officer receives alerts. Clerk posts PV. Checker approves PV discrepancy.
2. How they create: Alerts appear on dashboard. PV: select location, count qty vs system, Save draft discrepancy.
3. How they edit: PV draft editable. Cost method is configuration (maker–checker).
4. How they send for approval: PV discrepancy submit to Stores Checker. Forecast run is on demand.
5. How the approver sees pending items: Checker PV inbox. Alert list for Store Officer.
6. How the approver decides: Approve stock adjustment or return.
7. How the applicant sees history: PV and adjustment history.
8. How the approver sees history: Approved adjustments; forecast runs.

### Functional Capabilities
- Applicant creates, edits draft, submits, withdraws and views own stock control action history.
- Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.
- Status timeline is visible to both applicant and approver on the same record.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My stock control action register | Medium |
| Stock control action form (create and edit) | Complex |
| Submit confirmation | Simple |
| Approver stock control action inbox | Complex |
| Stock control action decision panel (approve / reject / return) | Medium |
| My stock control action history | Medium |
| Team stock control action history (approver) | Medium |
| Alert list | Medium |
| Physical verification sheet | Complex |
| Forecast run | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Save draft stock control action | Medium |
| Update draft stock control action | Medium |
| Submit stock control action for approval | Complex |
| Withdraw stock control action | Easy |
| Approver inbox query | Medium |
| Approve, reject or return stock control action | Complex |
| Applicant history query | Medium |
| Team history query | Medium |
| Evaluate min/reorder | Medium |
| Value stock at monthly average cost | Complex |
| Post PV adjustment | Complex |
| Generate consumption forecast | Very High |

### Inputs
Min, reorder, count qty, period for forecast.

### Outputs
Persisted stock control action with status; inbox item for the approver; notifications; searchable history for applicant and approver.

### Business Rules
- The applicant cannot approve their own stock control action.
- Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.
- Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.
- Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.

### Validations
- Mandatory fields must be complete before Submit.
- Submit is blocked if the applicant has no current Post mapping.
- Submit is blocked if no supervising Post / approver can be resolved.
- Approver can act only on items in their inbox (Posts they currently supervise).
- PV requires location and date.

### Calculations
Monthly average cost; forecast from consumption, failures, maintenance frequency by item, location, vehicle type. Flag high-failure items.

### Workflow
Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.

### Search Requirements
Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.

### Documents
PV sheet.

### Reports
Reorder list; PV discrepancy; forecast.

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
| My stock control action register | UI | Medium | 6 |
| Stock control action form (create and edit) | UI | Complex | 12 |
| Submit confirmation | UI | Simple | 2 |
| Approver stock control action inbox | UI | Complex | 12 |
| Stock control action decision panel (approve / reject / return) | UI | Medium | 6 |
| My stock control action history | UI | Medium | 6 |
| Team stock control action history (approver) | UI | Medium | 6 |
| Alert list | UI | Medium | 6 |
| Physical verification sheet | UI | Complex | 12 |
| Forecast run | UI | Complex | 12 |
| Save draft stock control action | API | Medium | 6 |
| Update draft stock control action | API | Medium | 6 |
| Submit stock control action for approval | API | Complex | 8 |
| Withdraw stock control action | API | Easy | 4 |
| Approver inbox query | API | Medium | 6 |
| Approve, reject or return stock control action | API | Complex | 8 |
| Applicant history query | API | Medium | 6 |
| Team history query | API | Medium | 6 |
| Evaluate min/reorder | API | Medium | 6 |
| Value stock at monthly average cost | API | Complex | 8 |
| Post PV adjustment | API | Complex | 8 |
| Generate consumption forecast | API | Very High | 16 |
| Stock control action record, status history and attachments metadata | DB | Medium | 4 |
| Notify applicant and approver on stock control action status change | Integration | Simple | 4 |
| Min/Reorder Alerts, Average Cost and Physical Verification feature tests | Testing | Complex | 8 |
| Min/Reorder Alerts, Average Cost and Physical Verification implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **187** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
