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
1. Who creates: Advocate
2. How they create: User opens Attendance, selects the matter.
3. How they edit: Enters name/code, date, court, location, entry/exit time, judge, brief on proceedings, Effective/Ineffective.
4. How they send for approval: Uploads the cause list and submits. Select matter → fill attendance → upload cause list → submit → dashboard.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Advocate works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Advocate opens history on the record. The row appears on the matter dashboard.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Court Attendance form (name/code, date, court, location, times, judge, brief, Effective/Ineffective)
- Cause List upload
- Submit against the matter
- Dashboard row
- Not payroll; not unlinked personal notes

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Court Attendance form (name/code, date, court, location, times, judge, brief, Effective/Ineffective) | Complex |
| Cause List upload | Medium |
| Submit court attendance history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Attendance submit operations | Complex |
| Update submit court attendance | Medium |
| Search submit court attendance | Medium |
| Read submit court attendance history | Easy |

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
- Matter required; date and court required; exit not before entry; cause list required as specified; judge from catalogue or text as configured.

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
- Name/code may default from the logged-in Person but remain editable if an authorised clerk files for an advocate as policy allows.

### Risks
Attendance without cause list or matter link.

### Non Functional Requirements
Usable on court day after return from court; Android capture is F09-006.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Court Attendance form (name/code, date, court, location, times, judge, brief, Effective/Ineffective) | UI | Complex | 12 |
| Cause List upload | UI | Medium | 6 |
| Submit court attendance history | UI | Medium | 6 |
| Attendance submit operations | API | Complex | 8 |
| Update submit court attendance | API | Medium | 6 |
| Search submit court attendance | API | Medium | 6 |
| Read submit court attendance history | API | Easy | 4 |
| Submit court attendance persistence | DB | Medium | 4 |
| Matter dashboard handoff | Integration | Simple | 4 |
| Submit court attendance feature tests | Testing | Medium | 6 |
| Submit court attendance implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **65** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
