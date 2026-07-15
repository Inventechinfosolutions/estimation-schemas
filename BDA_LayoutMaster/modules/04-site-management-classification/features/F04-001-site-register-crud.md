# F04-001 — Site Register CRUD
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Site Register CRUD |
| **Module** | 04 — Site Management & Classification |
### Description
Create, update, and view uniquely identified sites under valid layouts.
### Business Objective
Maintain the authoritative BDA site register.
### Actors
Town Planning, Engineering, Zonal Officer, Data Entry Operator.
### User Journey
Officer selects a valid layout, enters site identity and core fields, saves, and views audited details.
### Functional Capabilities
Site CRUD, numbering, layout linkage, status, change history, and scoped retrieval.
### Inputs
Layout, site number, status, core site attributes.
### Outputs
Site record and history.
### Business Rules
Each site belongs to exactly one valid layout and must be uniquely identifiable.
### Validations
Active parent layout; unique site number within layout; required master values.
### Calculations
None.
### Workflow
Create/update follows configured controls; cancellation is F04-006.
### Search Requirements
Layout, site number, status, zone.
### Documents
Embedded documents are F04-003.
### Reports
Site register via Module 13.
### Notifications
Configured workflow alerts where applicable.
### Security
RBAC, scope, audit.
### Integrations
Internal layout/master consumption (Simple).
### Dependencies
Modules 01–03; F04-003–006.
### Assumptions
GIS synchronization is Module 09 scope.
### Risks
Duplicate legacy numbering requires BDA resolution.
### Non Functional Requirements
Responsive forms, auditability, standard performance.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Site register/search | UI | Complex | 8 |
| Site create/edit/detail | UI | Very High | 16 |
| Site lifecycle operations | API | Complex | 8 |
| Site persistence | Database | Complex | 6 |
| Internal layout/master consumption | Integration | Simple | 4 |
| Site register tests | Testing | Very High | 12 |
| Site register guide | Documentation | Medium | 3 |
| **Total** | | | **57** |
### Estimation Assumptions
Classification and documents are separately estimated.
