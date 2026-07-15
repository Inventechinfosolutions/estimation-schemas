# F04-001 — Flat & Villa Unit Register

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Flat & Villa Unit Register |
| **Module** | 04 — Flats & Villas Inventory & Status |

### Description
Maintain uniquely identified Flat and Villa inventory under housing projects with physical and construction attributes.

### Business Objective
Provide reliable, searchable housing stock for controlled booking and lifecycle management.

### Actors
Engineering Section; Housing officers; Approvers; Auditor.

### User Journey
Officer selects a project, creates or edits a unit, captures flat/villa attributes and readiness, and views it in the Unit Register.

### Functional Capabilities
Unit create/edit/view; flat/villa type; tower/block/floor; BHK/facing; areas; parking; description; construction status; unique unit register.

### Inputs
Project, unit number, property type, location hierarchy, areas, parking, facing, construction status.

### Outputs
Unit record and Unit Register.

### Business Rules
Every unit is unique within its project; only valid project/master combinations can be used; booking processing is excluded.

### Validations
Required project/unit number; uniqueness under project; non-negative areas; valid hierarchy selections.

### Calculations
None.

### Workflow
Draft unit maintenance → submit/approve where configured → availability governed by F04-004.

### Search Requirements
Project, unit number, property type, tower/block/floor, BHK, facing, construction status, status.

### Documents
Unit media/documents are embedded in F04-003.

### Reports
Unit Register export.

### Notifications
Optional internal alert on unit readiness change.

### Security
RBAC by section; change audit.

### Integrations
None.

### Dependencies
Modules 01–03; F04-004.

### Assumptions
Bulk migration/import is handled in Module 15.

### Risks
Duplicate or inaccurate unit identifiers compromise inventory integrity.

### Non Functional Requirements
Responsive officer entry; high-volume search; audit trail.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Unit Register + advanced filters | UI | Complex | 8 |
| Flat/Villa create-edit form | UI | Very High | 16 |
| Unit register operations | API | Complex | 8 |
| Unit and attribute persistence | Database | Complex | 6 |
| Unit register tests | Testing | Very High | 12 |
| Unit register guide | Documentation | Medium | 3 |
| **Total** | | | **53** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
