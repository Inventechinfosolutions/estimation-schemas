# F14-006 — Procurement and Financial Reports

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F14-006 |
| **Feature Name** | Procurement and Financial Reports |
| **Module** | 14 — Reporting, Dashboards & Analytics |

### Description
Finance/purchase/stores run indent, PO, stock, expense, payment reports.

### Business Objective
Produce procurement/finance reports from live module data with office/Post scope.

### Actors
User: Finance, purchase, stores Posts. Auditor: read-only history.

### User Journey
1. Who creates: Finance, purchase, stores Posts.
2. How they create: User opens Reports → Procurement and Financial Reports, sets filters (office, period, status), Run. Optional Save snapshot.
3. How they edit: Filters edited and Run again. A released snapshot is not edited; new run = new snapshot.
4. How they send for approval: Running is not approval. If a snapshot is internally published, Submit snapshot to MIS Checker.
5. How the approver sees pending items: Checker snapshot inbox only if publish used. Otherwise none.
6. How the approver decides: Checker approves snapshot publish or user just exports.
7. How the user sees history: User sees recent runs/exports they launched.
8. How the supervisor / auditor sees history: Published snapshots if any. Data itself is live from source modules.

### Functional Capabilities
- Authorised user creates, edits and searches procurement/finance report records.
- Status/change history is visible to the user and to authorised supervisors.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Procurement/finance report register | Medium |
| Procurement/finance report form (create and edit) | Complex |
| Procurement/finance report history | Medium |
| Procurement and Financial Reports filter form | Medium |
| Results grid | Complex |
| Export dialog | Simple |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create procurement/finance report | Medium |
| Update procurement/finance report | Medium |
| Search procurement/finance report | Medium |
| Read procurement/finance report history | Easy |
| Run procurement/finance report | Complex |
| Export result | Easy |

### Inputs
Filters: office, period, status as relevant to the report.

### Outputs
Persisted procurement/finance report; searchable register; history.

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
| Procurement/finance report register | UI | Medium | 6 |
| Procurement/finance report form (create and edit) | UI | Complex | 12 |
| Procurement/finance report history | UI | Medium | 6 |
| Procurement and Financial Reports filter form | UI | Medium | 6 |
| Results grid | UI | Complex | 12 |
| Export dialog | UI | Simple | 2 |
| Create procurement/finance report | API | Medium | 6 |
| Update procurement/finance report | API | Medium | 6 |
| Search procurement/finance report | API | Medium | 6 |
| Read procurement/finance report history | API | Easy | 4 |
| Run procurement/finance report | API | Complex | 8 |
| Export result | API | Easy | 4 |
| Procurement/finance report record and history | DB | Medium | 4 |
| Internal identity/document hooks for procurement/finance report | Integration | Simple | 4 |
| Procurement and Financial Reports feature tests | Testing | Complex | 8 |
| Procurement and Financial Reports implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **97** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
