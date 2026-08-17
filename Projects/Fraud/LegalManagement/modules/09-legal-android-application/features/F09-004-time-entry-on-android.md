# F09-004 — Time entry on Android

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Time entry on Android |
| **Module** | 09 — Legal Android Application (Advocates & Legal Cell) |

### Description
The user records a time entry against the matter (date, duration, activity) and saves. The matter dashboard shows the entry.

### Business Objective
Capture advocate/Legal Cell time against the matter from Android so the matter dashboard shows the entry.

### Actors
Advocate; Legal Cell.

### User Journey
1. User records a time entry against the matter (date, duration, activity) and saves.
2. The matter dashboard (web and device) shows the entry.

### Functional Capabilities
- Android Time-Entry form
- Time list on the matter
- Date, duration, activity against the matter
- Not payroll; not EVAL billing

### Inputs
Matter; date; duration; activity.

### Outputs
Time entry on matter dashboard.

### Business Rules
- Time is matter-bound.
- Not a reimbursement or salary engine.

### Validations
Matter required; duration > 0; date required.

### Calculations
Duration as entered; optional daily total on the matter.

### Workflow
Enter time → save → dashboard.

### Search Requirements
Time entries on the matter by date.

### Documents
None.

### Reports
Consumed on dashboard; formal reports remain web where specified.

### Notifications
None required.

### Security
Attributed to shared Person.

### Integrations
Matter dashboard consume (Easy).

### Dependencies
F04-002; F01-004.

### Assumptions
Activity list from F02-005.

### Risks
Double entry from web and Android without duplicate warning.

### Non Functional Requirements
Quick capture after hearing.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Android Time-Entry form | UI | Complex | 12 |
| Time list on the matter | UI | Easy | 4 |
| Time save operations | API | Medium | 6 |
| Time entities | Database | Easy | 2 |
| Matter dashboard consume | Integration | Easy | 8 |
| Android time-entry tests | Testing | Easy | 4 |
| Android time entry guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Dashboard aggregation remains F04-002 / F09-005.
