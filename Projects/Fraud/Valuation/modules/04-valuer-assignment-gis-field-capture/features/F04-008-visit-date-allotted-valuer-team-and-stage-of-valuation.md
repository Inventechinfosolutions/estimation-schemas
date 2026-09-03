# F04-008 — Visit date, allotted valuer team and stage of valuation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-008 |
| **Feature Name** | Visit date, allotted valuer team and stage of valuation |
| **Module** | 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) |

### Description
The assigned Valuer (or Office user) records Date of Visit, Valuer Names Allotted with mobile numbers (team on this assignment, not a second login directory), and Stage of Valuation (for example assigned / visited / inspection complete / analytical in progress / submitted to CA / revaluation). Changing stage appends history (who, when, previous, new). CA Time Taken (F07-006) uses visit date and later submit time from this record.

### Business Objective
Record visit date, field team and valuation stage as the assignment lifecycle, feeding computed Time Taken.

### Actors
Approved Valuer; Office user.

### User Journey
1. Who creates: Approved Valuer
2. How they create: Assigned Valuer or Office user records Date of Visit, Valuer Names Allotted with mobile numbers, and Stage of Valuation (assigned / visited / inspection complete / analytical in progress / submitted to CA / revaluation, as used).
3. How they edit: Changing stage appends history (who, when, previous, new).
4. How they send for approval: F07-006 uses visit date and later submit time from this record. Enter visit/team → set stage → history; CA/revaluation updates stage.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record Date of Visit
- Record allotted valuer names and mobiles as team on this assignment (not logins)
- Record Stage of Valuation with append-only history
- Supply visit date to Time Taken (F07-006)

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My visit date, allotted valuer team and stage of valuation list / queue | Medium |
| Visit, team and stage panel | Medium |
| Visit date, allotted valuer team and stage of valuation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Stage-of-valuation workflow | Very High |
| Update visit date, allotted valuer team and stage of valuation | Medium |
| Search visit date, allotted valuer team and stage of valuation | Medium |
| Read visit date, allotted valuer team and stage of valuation history | Easy |

### Inputs
Date of Visit; team names and mobiles; new stage.

### Outputs
Visit/team/stage record; stage history.

### Business Rules
- Team names are not a second login directory
- Stage change is history-logged
- Revaluation from F07-004 resets stage with CA remarks visible

### Validations
- Date of Visit present before inspection-complete where required
- Stage is a known stage

### Calculations
None here (elapsed Time Taken is F07-006).

### Workflow
Enter visit/team → set stage → history; CA/revaluation updates stage.

### Search Requirements
Assignment, stage, visit date, allotted names.

### Documents
None.

### Reports
Stage history extract.

### Notifications
In-app stage change confirmation.

### Security
Assigned valuer or Office user; stage history attributable.

### Integrations
Internal consume by F07-006 and F07-004.

### Dependencies
F04-001; F07-004; F07-006; F09-005 submit timestamp.

### Assumptions
- Authority confirms the stage list (examples in the SOW).

### Risks
Missing visit date flags Time Taken (F07-006) and can stall CA assessment quality.

### Non Functional Requirements
Stage history immutable; team mobiles stored with the assignment.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My visit date, allotted valuer team and stage of valuation list / queue | UI | Medium | 6 |
| Visit, team and stage panel | UI | Medium | 6 |
| Visit date, allotted valuer team and stage of valuation history | UI | Medium | 6 |
| Stage-of-valuation workflow | API | Very High | 16 |
| Update visit date, allotted valuer team and stage of valuation | API | Medium | 6 |
| Search visit date, allotted valuer team and stage of valuation | API | Medium | 6 |
| Read visit date, allotted valuer team and stage of valuation history | API | Easy | 4 |
| Visit date, allotted valuer team and stage of valuation persistence | DB | Medium | 4 |
| Time-Taken and CA-stage consume | Integration | Simple | 4 |
| Visit date, allotted valuer team and stage of valuation feature tests | Testing | Complex | 8 |
| Visit date, allotted valuer team and stage of valuation implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **69** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
