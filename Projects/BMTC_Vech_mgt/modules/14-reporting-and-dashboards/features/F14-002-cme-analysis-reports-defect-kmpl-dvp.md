# F14-002 — CME Analysis Reports (Defect, KMPL, DVP)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-002 |
| **Feature Name** | CME Analysis Reports (Defect, KMPL, DVP) |
| **Module** | 14 — Reporting and Dashboards |

### Description
Most defective bus; low performing driver and vehicle KMPL with flags; DVP analysis (schedules, vehicles, off-road, spare %).

### Business Objective
FR-R-03 to 06.

### Actors
User: CME/DC/DME and Mechanical Section. Auditor: read-only history.

### User Journey
1. Who creates: CME/DC/DME and Mechanical Section.
2. How they create: Reports → analysis report, filters depot/zone/date/make, Run.
3. How they edit: KMPL thresholds are Module 08. Report is a run.
4. How they send for approval: Not approval unless snapshot publish.
5. How the approver sees pending items: None for run.
6. How the approver decides: Not applicable.
7. How the user sees history: Recent runs.
8. How the supervisor / auditor sees history: Auditor runs.

### Functional Capabilities
- Authorised user creates, edits and searches CME analysis report records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Cme analysis report register | Medium |
| Cme analysis report form (create and edit) | Complex |
| Cme analysis report history | Medium |
| Most defective bus | Complex |
| Driver/vehicle KMPL ranking | Complex |
| DVP analysis | Complex |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create CME analysis report | Medium |
| Update CME analysis report | Medium |
| Search CME analysis report | Medium |
| Read CME analysis report history | Easy |
| Run defective bus ranking | Complex |
| Run KMPL ranking | Complex |
| Run DVP | Complex |

### Inputs
Period, depot/zone, make/model.

### Outputs
Persisted CME analysis report; searchable register; history.

### Business Rules
- Reports and dashboards have English and Kannada versions (pre-bid). Predictive analysis report/database changes continue during maintenance.

### Validations
- Period required.

### Calculations
Rankings; KMPL 10% below standard for 3+ days → Watch/Warning/Counselling; DVP spare %.

### Workflow
Not approval unless snapshot publish.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Export.

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
| Cme analysis report register | UI | Medium | 6 |
| Cme analysis report form (create and edit) | UI | Complex | 12 |
| Cme analysis report history | UI | Medium | 6 |
| Most defective bus | UI | Complex | 12 |
| Driver/vehicle KMPL ranking | UI | Complex | 12 |
| DVP analysis | UI | Complex | 12 |
| Create CME analysis report | API | Medium | 6 |
| Update CME analysis report | API | Medium | 6 |
| Search CME analysis report | API | Medium | 6 |
| Read CME analysis report history | API | Easy | 4 |
| Run defective bus ranking | API | Complex | 8 |
| Run KMPL ranking | API | Complex | 8 |
| Run DVP | API | Complex | 8 |
| Cme analysis report record and history | DB | Medium | 4 |
| Internal identity/document hooks for CME analysis report | Integration | Simple | 4 |
| CME Analysis Reports (Defect, KMPL, DVP) feature tests | Testing | Complex | 8 |
| CME Analysis Reports (Defect, KMPL, DVP) implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **125** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
