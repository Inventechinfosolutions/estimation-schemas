# F03-005 — Layout Search & Site Summary
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Layout Search & Site Summary |
| **Module** | 03 — Layout Management |
### Description
Search layouts and show linked site counts by status and category.
### Business Objective
Enable officers to locate layouts and assess their operational inventory.
### Actors
Town Planning Officer; Zonal Officer; Auditor.
### User Journey
User applies filters, opens a layout result, and reviews permitted linked-site counts and summary.
### Functional Capabilities
Multi-parameter search, results/detail view, linked-site status/category summary, export.
### Inputs
Name, code, zone, district, taluk, village, status, filters.
### Outputs
Filtered layouts, site summary, export.
### Business Rules
Results and counts follow data scope and permitted layout/site visibility.
### Validations
Valid filters and authorised scope.
### Calculations
Aggregate linked sites by status and category.
### Workflow
Read-only retrieval.
### Search Requirements
Name, code, zone, district, taluk, village, status.
### Documents
Document indicators/linkage only; retrieval is F03-003.
### Reports
Layout search export.
### Notifications
None.
### Security
RBAC and zone/department data scope.
### Integrations
Internal site-register aggregation (Simple).
### Dependencies
F03-001; Module 04 site register; F01-003.
### Assumptions
Enterprise dashboards remain Module 13.
### Risks
Large volumes require agreed indexing/performance approach.
### Non Functional Requirements
Agreed filter response time; export security.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Search/filter results | UI | Complex | 8 |
| Layout summary view | UI | Complex | 8 |
| Search and aggregation operations | API | Complex | 8 |
| Search optimisation persistence | Database | Complex | 6 |
| Internal site aggregation | Integration | Simple | 4 |
| Search and count tests | Testing | Complex | 8 |
| Search guide | Documentation | Easy | 2 |
| **Total** | | | **44** |
### Estimation Assumptions
GIS map display is Module 09 scope.
