# F14-002 — Objection, Para and Recovery Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-002 |
| **Feature Name** | Objection, Para and Recovery Reports |
| **Module** | 14 — Reporting, Dashboards & Analytics |

### Description
Officers run para and recovery position reports; snapshots may be submitted for internal publish.

### Business Objective
Produce para/recovery reports from live module data with office/Post scope.

### Actors
User: Audit/recovery Posts. Auditor: read-only history.

### User Journey
1. Who creates: Audit/recovery Posts.
2. How they create: User opens Reports → Objection, Para and Recovery Reports, sets filters (office, period, status), Run. Optional Save snapshot.
3. How they edit: Filters edited and Run again. A released snapshot is not edited; new run = new snapshot.
4. How they send for approval: Running is not approval. If a snapshot is internally published, Submit snapshot to MIS Checker.
5. How the approver sees pending items: Checker snapshot inbox only if publish used. Otherwise none.
6. How the approver decides: Checker approves snapshot publish or user just exports.
7. How the user sees history: User sees recent runs/exports they launched.
8. How the supervisor / auditor sees history: Published snapshots if any. Data itself is live from source modules.

### Functional Capabilities
- Authorised user creates, edits and searches para/recovery report records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Para/recovery report register | Medium |
| Para/recovery report form (create and edit) | Complex |
| Para/recovery report history | Medium |
| Objection, Para and Recovery Reports filter form | Medium |
| Results grid | Complex |
| Export dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create para/recovery report | Medium |
| Update para/recovery report | Medium |
| Search para/recovery report | Medium |
| Read para/recovery report history | Easy |
| Run para/recovery report | Complex |
| Export result | Easy |

### Inputs
Filters: office, period, status as relevant to the report.

### Outputs
Persisted para/recovery report; searchable register; history.

### Business Rules
- Only authorised Posts may create or edit.
- History is append-only.

### Validations
- Period required where the report is periodic.

### Calculations
Aggregations from source modules (counts, sums, ageing).

### Workflow
Running is not approval. If a snapshot is internally published, Submit snapshot to MIS Checker.

### Search Requirements
Search by identifier, person, office, period and status.

### Documents
Exported file.

### Reports
This feature is the report.

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
| Para/recovery report register | UI | Medium | 6 |
| Para/recovery report form (create and edit) | UI | Complex | 12 |
| Para/recovery report history | UI | Medium | 6 |
| Objection, Para and Recovery Reports filter form | UI | Medium | 6 |
| Results grid | UI | Complex | 12 |
| Export dialog | UI | Simple | 2 |
| Create para/recovery report | API | Medium | 6 |
| Update para/recovery report | API | Medium | 6 |
| Search para/recovery report | API | Medium | 6 |
| Read para/recovery report history | API | Easy | 4 |
| Run para/recovery report | API | Complex | 8 |
| Export result | API | Easy | 4 |
| Para/recovery report record and history | DB | Medium | 4 |
| Internal identity/document hooks for para/recovery report | Integration | Simple | 4 |
| Objection, Para and Recovery Reports feature tests | Testing | Complex | 8 |
| Objection, Para and Recovery Reports implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **97** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
