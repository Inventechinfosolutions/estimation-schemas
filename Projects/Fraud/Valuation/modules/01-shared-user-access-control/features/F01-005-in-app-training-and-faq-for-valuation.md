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
1. Who creates: Office user
2. How they create: User opens Help / FAQ on valuation web or Android while in a module (assignment, GIS capture, Form V-1, billing, or other).
3. How they edit: The topic for that module and Post is shown.
4. How they send for approval: Administrator adds or updates topics. Open Help → resolve module + Post → show topic; Administrator save → next open sees update.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record. Classroom scheduling is not offered unless separately ordered.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Context Help/FAQ per valuation module on web and Android
- Administrator maintains topics
- No classroom timetable and no second identity product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| In-app Help/FAQ reader | Medium |
| FAQ topic maintenance | Easy |
| In-app training and faq for valuation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Context FAQ retrieve and save | Medium |
| Update in-app training and faq for valuation | Medium |
| Search in-app training and faq for valuation | Medium |
| Read in-app training and faq for valuation history | Easy |

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
|---|---|---|---|
| In-app Help/FAQ reader | UI | Medium | 6 |
| FAQ topic maintenance | UI | Easy | 4 |
| In-app training and faq for valuation history | UI | Medium | 6 |
| Context FAQ retrieve and save | API | Medium | 6 |
| Update in-app training and faq for valuation | API | Medium | 6 |
| Search in-app training and faq for valuation | API | Medium | 6 |
| Read in-app training and faq for valuation history | API | Easy | 4 |
| In-app training and faq for valuation persistence | DB | Medium | 4 |
| Help embed on web and Android shells | Integration | Simple | 4 |
| In-app training and FAQ for valuation feature tests | Testing | Easy | 4 |
| In-app training and FAQ for valuation implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
