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
1. Assigned Valuer or Office user records Date of Visit, Valuer Names Allotted with mobile numbers, and Stage of Valuation (assigned / visited / inspection complete / analytical in progress / submitted to CA / revaluation, as used).
2. Changing stage appends history (who, when, previous, new).
3. F07-006 uses visit date and later submit time from this record.

### Functional Capabilities
- Record Date of Visit
- Record allotted valuer names and mobiles as team on this assignment (not logins)
- Record Stage of Valuation with append-only history
- Supply visit date to Time Taken (F07-006)

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
|---|---|---|---:|
| Visit, team and stage panel | UI | Medium | 6 |
| Stage-of-valuation workflow | API | Very High | 16 |
| Visit/team/stage history | Database | Medium | 4 |
| Time-Taken and CA-stage consume | Integration | Simple | 4 |
| Visit/stage tests | Testing | Complex | 8 |
| Visit and stage guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- API Very High 16 for stage workflow. Time Taken computation hours are F07-006.
