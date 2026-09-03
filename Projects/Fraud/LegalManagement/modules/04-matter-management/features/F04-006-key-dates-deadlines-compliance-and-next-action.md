# F04-006 — Key dates, deadlines, compliance and next action

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | Key dates, deadlines, compliance and next action |
| **Module** | 04 — Matter Management |

### Description
The user records a key date or deadline, sets an alert, and updates compliance status and next action. Assigned users receive the alert; overdue dates show on the dashboard.

### Business Objective
Track key dates, deadlines, alerts, compliance status and next action so court timelines are visible on the matter.

### Actors
Legal Cell; Advocate; assigned team members.

### User Journey
1. Who creates: Legal Cell
2. How they create: User opens Key Dates on the matter.
3. How they edit: Records a key date or deadline, sets an alert, and assigns users.
4. How they send for approval: Updates compliance status and next action. Record date → set alert → notify assignees → update compliance/next action → overdue on dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Assigned users receive the alert; overdue dates show on the matter dashboard.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Key Dates Register
- Deadline and Alert form
- Compliance status and next action
- Alerts to assigned users
- Overdue indication on dashboard

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Key Dates Register | Complex |
| Deadline and Alert form | Medium |
| Key dates, deadlines, compliance and next action history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dates, compliance and alert operations | Complex |
| Update key dates, deadlines, compliance and next action | Medium |
| Search key dates, deadlines, compliance and next action | Medium |
| Read key dates, deadlines, compliance and next action history | Easy |

### Inputs
Date/deadline; alert offset; assigned Persons; compliance status; next action text.

### Outputs
Key date records; alerts; overdue flags; dashboard indicators.

### Business Rules
- Proceedings item 6 coverage: hearings, orders, compliance, next action — as recorded here and on F05-004.
- Overdue dates must show on the dashboard (F04-002).
- Alerts are attributable and stored.

### Validations
- Date required; assignee must be active shared Person; compliance status from central masters.

### Calculations
Overdue = current date past deadline and not complied.

### Workflow
Record date → set alert → notify assignees → update compliance/next action → overdue on dashboard.

### Search Requirements
Key date type, date range, compliance status, assignee, matter.

### Documents
Optional supporting order/notice.

### Reports
Key-date-wise report consumed also by F04-007.

### Notifications
Alert to assigned users; overdue reminder.

### Security
Matter visibility still applies.

### Integrations
Alert to assigned users (Easy).

### Dependencies
F04-002; F01-001; F02-005; F05-004 related court alerts.

### Assumptions
- Alert channel is in-app plus email if F05-008 is in scope for the user.

### Risks
Missed limitation/hearing dates if alerts are not assigned.

### Non Functional Requirements
Alerts timely for court-day; dashboard overdue visible.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Key Dates Register | UI | Complex | 12 |
| Deadline and Alert form | UI | Medium | 6 |
| Key dates, deadlines, compliance and next action history | UI | Medium | 6 |
| Dates, compliance and alert operations | API | Complex | 8 |
| Update key dates, deadlines, compliance and next action | API | Medium | 6 |
| Search key dates, deadlines, compliance and next action | API | Medium | 6 |
| Read key dates, deadlines, compliance and next action history | API | Easy | 4 |
| Key dates, deadlines, compliance and next action persistence | DB | Medium | 4 |
| Alert to assigned users | Integration | Easy | 8 |
| Key dates, deadlines, compliance and next action feature tests | Testing | Medium | 6 |
| Key dates, deadlines, compliance and next action implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
