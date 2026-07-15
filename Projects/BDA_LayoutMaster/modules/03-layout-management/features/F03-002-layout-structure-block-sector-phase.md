# F03-002 — Layout Structure: Block, Sector & Phase
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Layout Structure: Block, Sector & Phase |
| **Module** | 03 — Layout Management |
### Description
Maintain applicable block, sector, phase, stage, and section structure within a layout.
### Business Objective
Provide a controlled hierarchy for site addressing and search.
### Actors
Town Planning Officer; Engineering Section; Data Entry Operator.
### User Journey
Officer opens a layout, adds or updates applicable structural segments, validates unique codes, and saves them for site assignment.
### Functional Capabilities
Maintain layout-specific structures, status, ordering, search, and change history.
### Inputs
Parent layout, structure type, code, name, status.
### Outputs
Layout structure hierarchy and selectable site-addressing values.
### Business Rules
Structures belong to one valid layout; inactive values remain historical but cannot be newly selected.
### Validations
Valid layout; unique structure code within layout/type; active master type.
### Calculations
None.
### Workflow
Maintained with layout change controls; major amendment may use F03-004.
### Search Requirements
Layout, structure type, code, name, status.
### Documents
Supporting sketches, if required, remain embedded in F03-003.
### Reports
Layout structure export.
### Notifications
Optional approval notifications for major amendments.
### Security
RBAC, scope controls, audit.
### Integrations
Internal layout/site consumption (Simple).
### Dependencies
F03-001; F02-002 structure-code masters; Module 04 site register.
### Assumptions
Only structures applicable to each layout are maintained.
### Risks
Changing structures after site creation requires controlled impact review.
### Non Functional Requirements
Fast dependent lookup and auditability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Structure register | UI | Complex | 8 |
| Structure hierarchy editor | UI | Complex | 8 |
| Structure operations | API | Complex | 8 |
| Structure persistence | Database | Complex | 6 |
| Internal site consumption | Integration | Simple | 4 |
| Structure integrity tests | Testing | Complex | 8 |
| Structure guide | Documentation | Medium | 3 |
| **Total** | | | **45** |
### Estimation Assumptions
Spatial geometry remains outside this feature.
