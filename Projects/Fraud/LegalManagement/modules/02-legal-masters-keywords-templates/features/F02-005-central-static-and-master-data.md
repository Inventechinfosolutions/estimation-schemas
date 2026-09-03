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
1. Who creates: Administrator
2. How they create: Administrator opens the Central Legal Master Register.
3. How they edit: Maintains values (courts, matter types, task statuses, attendance Effective/Ineffective, expense categories, space types, etc.).
4. How they send for approval: Maintain master → publish active values → consume on web and Android.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Central Legal Master Register
- Master Value Edit form
- Typed lists consumed by Modules 04–07 and 09
- Activate/deactivate values
- No second local master in matter/Android modules

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Central Legal Master Register | Medium |
| Master Value Edit form | Easy |
| Central static and master data change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Master CRUD and consume operations | Medium |
| Update central static and master data | Medium |
| Search central static and master data register | Medium |
| Read central static and master data change history | Easy |

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
- Unique code per type; in-use values cannot be deleted (deactivate only); Android/web see the same active set.

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
- SPLOCA confirms the initial court, status and category lists.

### Risks
Changing a code in use fragments historical reports unless deactivate-only is enforced.

### Non Functional Requirements
Consistent lists on web and Android; auditable master edits.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Central Legal Master Register | UI | Medium | 6 |
| Master Value Edit form | UI | Easy | 4 |
| Central static and master data change history | UI | Medium | 6 |
| Master CRUD and consume operations | API | Medium | 6 |
| Update central static and master data | API | Medium | 6 |
| Search central static and master data register | API | Medium | 6 |
| Read central static and master data change history | API | Easy | 4 |
| Central static and master data identity persistence | DB | Medium | 4 |
| Consume by matter, task, attendance and Android | Integration | Simple | 4 |
| Central static and master data feature tests | Testing | Easy | 4 |
| Central static and master data implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
