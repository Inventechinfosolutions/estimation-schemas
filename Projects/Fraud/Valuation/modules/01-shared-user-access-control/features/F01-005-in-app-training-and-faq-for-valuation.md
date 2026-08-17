# F01-005 — In-app training and FAQ for valuation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-005 |
| **Feature Name** | In-app training and FAQ for valuation |
| **Module** | 01 — Shared User & Access Control (consumed) |

### Description
An Office user, Approved Valuer or CA opens Help / FAQ on the valuation web or Android and reads the topic for the module they are in (for example assignment, GIS capture, Form V-1, billing). The Administrator maintains those topics. This is not a second identity product and not classroom scheduling unless separately ordered.

### Business Objective
Give each valuation module in-application training and FAQ for the Posts that use it (Proceedings item 23).

### Actors
Office user; Approved Valuer; Competent Authority; Administrator.

### User Journey
1. User opens Help / FAQ on valuation web or Android while in a module (assignment, GIS capture, Form V-1, billing, or other).
2. The topic for that module and Post is shown.
3. Administrator adds or updates topics.
4. Classroom scheduling is not offered unless separately ordered.

### Functional Capabilities
- Context Help/FAQ per valuation module on web and Android
- Administrator maintains topics
- No classroom timetable and no second identity product

### Inputs
Current module context; Post; topic text; Administrator save.

### Outputs
Displayed topic; maintained topic list.

### Business Rules
- Topics are scoped to the module the user is in
- This is not IAM and not a training LMS unless later ordered

### Validations
- Module context is a known valuation module
- Topic has a title and body

### Calculations
None.

### Workflow
Open Help → resolve module + Post → show topic; Administrator save → next open sees update.

### Search Requirements
Module, topic title, last update.

### Documents
Optional attached job-aid files on a topic (not a DMS).

### Reports
FAQ topic list by module.

### Notifications
None.

### Security
Only Administrator maintains topics; readers see topics for modules their Post may use.

### Integrations
Embed Help on valuation web and Android shells (internal).

### Dependencies
F01-002 (Post); F01-004 (channels).

### Assumptions
- Authority supplies initial FAQ copy per module.

### Risks
Stale topics after form or GIS rule changes.

### Non Functional Requirements
Help available offline on Android for already-downloaded topics where the device has cached them; web requires connectivity.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| In-app Help/FAQ reader | UI | Medium | 6 |
| FAQ topic maintenance | UI | Easy | 4 |
| Context FAQ retrieve and save | API | Medium | 6 |
| FAQ topics store | Database | Easy | 2 |
| Help embed on web and Android shells | Integration | Simple | 4 |
| Help/FAQ tests | Testing | Easy | 4 |
| In-app FAQ note | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Classroom / LMS is out of scope unless separately ordered.
