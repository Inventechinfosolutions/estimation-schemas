# F14-001 — Job Card and Maintenance Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-001 |
| **Feature Name** | Job Card and Maintenance Reports |
| **Module** | 14 — Reporting and Dashboards |

### Description
Pending job cards with ageing bands and pending reason; job card register; vehicle maintenance history; repeated complaint and most items consuming vehicle.

### Business Objective
FR-R-01 and report list 1–4, 9, 11–12.

### Actors
User: Tech. Supervisor, Depot Manager, CME/DC/DME Posts with report Role. Auditor: read-only history.

### User Journey
1. Who creates: Tech. Supervisor, Depot Manager, CME/DC/DME Posts with report Role.
2. How they create: Reports → select report, filters (depot/zone/workshop/CO, date, ageing, section), Run, Export Excel/PDF.
3. How they edit: Filters edited and re-run. Snapshots optional Save.
4. How they send for approval: Running is not approval. Snapshot publish to MIS Checker if used.
5. How the approver sees pending items: Checker snapshot inbox only if publish used.
6. How the approver decides: Approve snapshot or user just exports.
7. How the user sees history: Recent runs.
8. How the supervisor / auditor sees history: Published snapshots.

### Functional Capabilities
- Authorised user creates, edits and searches maintenance report records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Maintenance report register | Medium |
| Maintenance report form (create and edit) | Complex |
| Maintenance report history | Medium |
| Pending job cards report | Complex |
| Export dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create maintenance report | Medium |
| Update maintenance report | Medium |
| Search maintenance report | Medium |
| Read maintenance report history | Easy |
| Run pending job cards | Complex |
| Export Excel/PDF | Easy |

### Inputs
Filters per FR-R-01 and list reports.

### Outputs
Persisted maintenance report; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Date range required.

### Calculations
Ageing 0–1 / 2–3 / 4–7 / 7+ days.

### Workflow
Running is not approval. Snapshot publish to MIS Checker if used.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Exported file.

### Reports
This feature.

### Notifications
On-screen confirmation. Optional notice to the user on save failure.

### Security
Need-to-know by Post. Actions attributed to Person acting in a Post.

### Integrations
Module 01 identity. Document store if attachments are used.

### Dependencies
Module 01 Person–Post–Role. Document store where attachments are required.

### Assumptions
- Hours use Estimation Master values only, at capability grain (not one billed row per screen).

### Risks
Unscoped access would expose records outside the user's office.

### Non Functional Requirements
Register and history remain searchable during office hours.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Maintenance report register | UI | Medium | 6 |
| Maintenance report form (create and edit) | UI | Complex | 12 |
| Maintenance report history | UI | Medium | 6 |
| Pending job cards report | UI | Complex | 12 |
| Export dialog | UI | Simple | 2 |
| Create maintenance report | API | Medium | 6 |
| Update maintenance report | API | Medium | 6 |
| Search maintenance report | API | Medium | 6 |
| Read maintenance report history | API | Easy | 4 |
| Run pending job cards | API | Complex | 8 |
| Export Excel/PDF | API | Easy | 4 |
| Maintenance report record and history | DB | Medium | 4 |
| Internal identity/document hooks for maintenance report | Integration | Simple | 4 |
| Job Card and Maintenance Reports feature tests | Testing | Complex | 8 |
| Job Card and Maintenance Reports implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **91** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
