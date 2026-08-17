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
1. User opens Court Proceedings / Alerts on the matter.
2. Records proceedings or directions, a stay alert, cause list, time-critical response or to-do.
3. Assigned members receive the alert and see it on the matter dashboard.

### Functional Capabilities
- Proceedings / Stay / Cause-List form
- Time-Critical To-Do panel
- Alerts to assigned members
- Dashboard visibility
- Cause list may link to attendance upload (F07-001) without duplicating attendance capture

### Inputs
Event type (proceedings/directions, stay, cause list, time-critical, to-do); text; assignees; optional cause-list file.

### Outputs
Matter event; alerts; dashboard items.

### Business Rules
- Events are matter-bound.
- Stay alerts are time-critical and must notify assigned members.
- Not Claim settlement notices.

### Validations
Matter required; type required; stay alert requires assignees.

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
Full attendance with entry/exit times is F07-001; this feature is proceedings/alerts/cause-list reporting.

### Risks
Stay alert not assigned to the advocate on record.

### Non Functional Requirements
Time-critical alerts prompt enough for court response windows.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Proceedings / Stay / Cause-List form | UI | Complex | 12 |
| Time-Critical To-Do panel | UI | Medium | 6 |
| Proceedings and alert operations | API | Complex | 8 |
| Proceedings event entities | Database | Medium | 4 |
| Matter dashboard and alerts | Integration | Easy | 8 |
| Court proceedings/alert tests | Testing | Medium | 6 |
| Court proceedings, stay and cause-list guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Attendance submit is F07-001.
