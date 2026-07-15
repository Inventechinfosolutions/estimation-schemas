# F04-007 — Advanced Layout & Site Search
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F04-007 |
| **Feature Name** | Advanced Layout & Site Search |
| **Module** | 04 — Site Management & Classification |
### Description
Provide multi-parameter layout/site search and retrieval for permitted officer users.
### Business Objective
Enable reliable operational discovery across master and process status data.
### Actors
All authorised officer roles; Auditor.
### User Journey
User combines supported filters, reviews result details, and exports permitted results.
### Functional Capabilities
Search/filter/export by layout, site, location, structure, category, process/approval/GIS/property statuses.
### Inputs
Listed SOW filter parameters and user scope.
### Outputs
Scoped result set, detail navigation, export.
### Business Rules
Results obey role, department, and zone scope; citizen search is Module 10.
### Validations
Valid filters and allowed export range.
### Calculations
Result count and permitted aggregate indicators.
### Workflow
Read-only retrieval.
### Search Requirements
All SOW parameters: layout/site/survey/location/structure/category/process/approval/GIS/property status.
### Documents
Attachment indicators only; retrieval stays embedded with record.
### Reports
Search export.
### Notifications
None.
### Security
RBAC, data scope, export audit.
### Integrations
Internal layout/site/process search consumption (Simple).
### Dependencies
Modules 01–05 data sources; F01-003.
### Assumptions
GIS availability is consumed as a status, not GIS map implementation.
### Risks
Large data volumes may affect filter response.
### Non Functional Requirements
Agreed response time; secure export.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Advanced filter/search UI | UI | Very High | 16 |
| Result/detail/export UI | UI | Complex | 8 |
| Multi-parameter search operations | API | Very High | 16 |
| Search optimisation persistence | Database | Complex | 6 |
| Internal record search consumption | Integration | Simple | 4 |
| Search/security tests | Testing | Very High | 12 |
| Search guide | Documentation | Medium | 3 |
| **Total** | | | **65** |
### Estimation Assumptions
Dashboard/report packs are Module 13 scope.
