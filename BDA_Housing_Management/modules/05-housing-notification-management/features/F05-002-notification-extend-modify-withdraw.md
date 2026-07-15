# F05-002 — Notification Extend, Modify & Withdraw

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Notification Extend, Modify & Withdraw |
| **Module** | 05 — Housing Notification Management |

### Description
Control extension, modification, and withdrawal of published housing notifications before booking end.

### Business Objective
Keep public booking communications accurate, timely, and fully auditable.

### Actors
Housing/Engineering officers; configured Approvers; Citizens (view); Auditor.

### User Journey
Officer locates an active notification, proposes an extension, content modification, or withdrawal with reason, obtains configured approval, and the visibility/status updates.

### Functional Capabilities
Extension; material-content modification; withdrawal; reason capture; approval; visibility update; change history.

### Inputs
Notification, requested action, revised dates/content, withdrawal reason, supporting material, remarks.

### Outputs
Updated notification status/content, citizen visibility result, change history.

### Business Rules
Changes are permitted only before booking end as configured; withdrawal removes active citizen visibility; material changes follow approval where configured.

### Validations
Active notification required; end date rules; mandatory withdrawal reason; valid approval action.

### Calculations
None.

### Workflow
Propose change → review/approval → apply extension/modify/withdraw → refresh citizen visibility and audit.

### Search Requirements
Notification, project, action type, status, booking end date, requester, date range.

### Documents
Revised terms/policies remain embedded in the notification record.

### Reports
Notification Change and Withdrawal Register.

### Notifications
Configured alerts for change request, decision and withdrawal/extension outcome.

### Security
RBAC, SoD, approval and publication audit.

### Integrations
Internal workflow routing (Simple); notification service handoff (Simple).

### Dependencies
F05-001; F02-004; Module 06.

### Assumptions
Changes after booking end require separate BDA policy/change control.

### Risks
Late withdrawal/modification can create citizen disputes.

### Non Functional Requirements
Immediate visibility update; immutable change history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Notification change register | UI | Complex | 8 |
| Extend/modify/withdraw review screen | UI | Very High | 16 |
| Notification change operations | API | Very High | 16 |
| Notification change/history persistence | Database | Complex | 6 |
| Workflow routing handoff | Integration | Simple | 4 |
| Notification service handoff | Integration | Simple | 4 |
| Notification change tests | Testing | Very High | 12 |
| Notification change guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
