# F05-004 — Court proceedings, stay alerts and cause lists

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-004 |
| **Feature Name** | Court proceedings, stay alerts and cause lists |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
An Advocate or Legal Cell user records court proceedings or directions, a stay alert, cause list, time-critical response or to-do against the matter. Assigned members receive the alert and see it on the matter dashboard.

### Business Objective
Capture court proceedings/directions, stay alerts, cause lists, time-critical responses and to-dos on the matter with alerts.

### Actors
Advocate; Legal Cell; assigned members.

### User Journey
1. Who creates: Advocate
2. How they create: User opens Court Proceedings / Alerts on the matter.
3. How they edit: Records proceedings or directions, a stay alert, cause list, time-critical response or to-do.
4. How they send for approval: Assigned members receive the alert and see it on the matter dashboard. Record event → alert assignees → show on dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Proceedings / Stay / Cause-List form
- Time-Critical To-Do panel
- Alerts to assigned members
- Dashboard visibility
- Cause list may link to attendance upload (F07-001) without duplicating attendance capture

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Proceedings / Stay / Cause-List form | Complex |
| Time-Critical To-Do panel | Medium |
| Court proceedings, stay alerts and cause lists history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Proceedings and alert operations | Complex |
| Update court proceedings, stay alerts and cause lists | Medium |
| Search court proceedings, stay alerts and cause lists | Medium |
| Read court proceedings, stay alerts and cause lists history | Easy |

### Inputs
Event type (proceedings/directions, stay, cause list, time-critical, to-do); text; assignees; optional cause-list file.

### Outputs
Matter event; alerts; dashboard items.

### Business Rules
- Events are matter-bound.
- Stay alerts are time-critical and must notify assigned members.
- Not Claim settlement notices.

### Validations
- Matter required; type required; stay alert requires assignees.

### Calculations
None.

### Workflow
Record event → alert assignees → show on dashboard.

### Search Requirements
Event type, date, matter, stay vs ordinary.

### Documents
Cause list file; directions notes.

### Reports
Stay alert register.

### Notifications
Alert to assigned members.

### Security
Need-to-know on stay-sensitive notes.

### Integrations
Matter dashboard and alerts (Easy).

### Dependencies
F04-002; F04-006; F07-001; F01-001.

### Assumptions
- Full attendance with entry/exit times is F07-001; this feature is proceedings/alerts/cause-list reporting.

### Risks
Stay alert not assigned to the advocate on record.

### Non Functional Requirements
Time-critical alerts prompt enough for court response windows.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Proceedings / Stay / Cause-List form | UI | Complex | 12 |
| Time-Critical To-Do panel | UI | Medium | 6 |
| Court proceedings, stay alerts and cause lists history | UI | Medium | 6 |
| Proceedings and alert operations | API | Complex | 8 |
| Update court proceedings, stay alerts and cause lists | API | Medium | 6 |
| Search court proceedings, stay alerts and cause lists | API | Medium | 6 |
| Read court proceedings, stay alerts and cause lists history | API | Easy | 4 |
| Court proceedings, stay alerts and cause lists persistence | DB | Medium | 4 |
| Matter dashboard and alerts | Integration | Easy | 8 |
| Court proceedings, stay alerts and cause lists feature tests | Testing | Medium | 6 |
| Court proceedings, stay alerts and cause lists implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
