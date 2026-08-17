# F02-005 — Central static and master data

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-005 |
| **Feature Name** | Central static and master data |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
An Administrator maintains static/master values used by matters, tasks, attendance and collaboration in one place. Matter and Android screens consume those values; a second local master is not created in those modules.

### Business Objective
Single legal master/static set so matter, task, attendance, collaboration and Android do not fork local lists.

### Actors
Administrator; Legal Cell (consume); Advocate on Android (consume).

### User Journey
1. Administrator opens the Central Legal Master Register.
2. Maintains values (courts, matter types, task statuses, attendance Effective/Ineffective, expense categories, space types, etc.).
3. Saves; matter, task, attendance and Android screens load the same lists.
4. A module screen does not offer a private duplicate master.

### Functional Capabilities
- Central Legal Master Register
- Master Value Edit form
- Typed lists consumed by Modules 04–07 and 09
- Activate/deactivate values
- No second local master in matter/Android modules

### Inputs
Master type, code, display value, sort order, status.

### Outputs
Central master values; consume APIs for other modules.

### Business Rules
- Matter, task, attendance/expense and collaboration consume this register.
- Android consumes the same values; it does not keep a conflicting local master.
- Keyword/entity catalogues remain F02-001; this feature is static/reference lists, not FE/Accused catalogues.
- Claim and valuation masters are not duplicated here.

### Validations
Unique code per type; in-use values cannot be deleted (deactivate only); Android/web see the same active set.

### Calculations
None.

### Workflow
Maintain master → publish active values → consume on web and Android.

### Search Requirements
Master type, code, value, status.

### Documents
None.

### Reports
Central master extract (Excel).

### Notifications
None required.

### Security
Administrator-only maintain; consume is read for authorised Legal Posts.

### Integrations
Consume by matter/task/attendance/Android (Simple).

### Dependencies
F01-001; consumed by F04–F07 and F09.

### Assumptions
SPLOCA confirms the initial court, status and category lists.

### Risks
Changing a code in use fragments historical reports unless deactivate-only is enforced.

### Non Functional Requirements
Consistent lists on web and Android; auditable master edits.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Central Legal Master Register | UI | Medium | 6 |
| Master Value Edit form | UI | Easy | 4 |
| Master CRUD and consume operations | API | Medium | 6 |
| Master entities | Database | Medium | 4 |
| Consume by matter, task, attendance and Android | Integration | Simple | 4 |
| Central master tests | Testing | Easy | 4 |
| Central static/master data guide | Documentation | Easy | 2 |
| **Total** | | | **30** |

### Estimation Assumptions
- Keyword catalogues are F02-001.
- No duplicate masters estimated in Modules 04–09.
