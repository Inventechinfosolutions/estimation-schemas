# F07-001 — Submit court attendance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Submit court attendance |
| **Module** | 07 — Court Attendance & Expense Management |

### Description
An Advocate or Legal Cell user opens Attendance, selects the matter, enters name/code, date, court, location, entry/exit time, judge, brief on proceedings, Effective/Ineffective, uploads the cause list, and submits. The row appears on the matter dashboard.

### Business Objective
Record court attendance with cause list against the matter for Legal Cell and advocates.

### Actors
Advocate; Legal Cell.

### User Journey
1. User opens Attendance, selects the matter.
2. Enters name/code, date, court, location, entry/exit time, judge, brief on proceedings, Effective/Ineffective.
3. Uploads the cause list and submits.
4. The row appears on the matter dashboard.

### Functional Capabilities
- Court Attendance form (name/code, date, court, location, times, judge, brief, Effective/Ineffective)
- Cause List upload
- Submit against the matter
- Dashboard row
- Not payroll; not unlinked personal notes

### Inputs
Matter; name/code; date; court; location; entry time; exit time; Presiding Judge; brief; Effective/Ineffective; cause-list file.

### Outputs
Attendance row; cause-list attachment; dashboard item.

### Business Rules
- Attendance shall link to the concerned court matter (enforced with F07-005).
- Cause list upload is part of submit.
- Effective/Ineffective from central masters.
- Not valuer billing (EVAL).

### Validations
Matter required; date and court required; exit not before entry; cause list required as specified; judge from catalogue or text as configured.

### Calculations
Duration from entry/exit if shown.

### Workflow
Select matter → fill attendance → upload cause list → submit → dashboard.

### Search Requirements
By date, court, matter, person (F07-003).

### Documents
Cause list upload.

### Reports
Attendance register (also via F07-003).

### Notifications
Optional notice to supervisor on submit.

### Security
Attributed to shared Person; matter visibility.

### Integrations
Matter dashboard handoff (Simple).

### Dependencies
F04-001; F04-002; F02-001 judge; F02-005; F07-005; F09-006 Android.

### Assumptions
Name/code may default from the logged-in Person but remain editable if an authorised clerk files for an advocate as policy allows.

### Risks
Attendance without cause list or matter link.

### Non Functional Requirements
Usable on court day after return from court; Android capture is F09-006.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Court Attendance form (name/code, date, court, location, times, judge, brief, Effective/Ineffective) | UI | Complex | 12 |
| Cause List upload | UI | Medium | 6 |
| Attendance submit operations | API | Complex | 8 |
| Attendance entities | Database | Medium | 4 |
| Matter dashboard handoff | Integration | Simple | 4 |
| Attendance tests | Testing | Medium | 6 |
| Court attendance guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Mandatory matter link rules are also F07-005.
- Android UI is F09-006.
