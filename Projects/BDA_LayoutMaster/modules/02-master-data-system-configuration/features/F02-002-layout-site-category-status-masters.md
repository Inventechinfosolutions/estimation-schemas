# F02-002 — Layout, Site, Category & Status Masters
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Layout, Site, Category & Status Masters |
| **Module** | 02 — Master Data & System Configuration |
### Description
Maintain configurable layout/site statuses, categories, reservations, facing indicators, and structure codes.
### Business Objective
Provide controlled classification and lifecycle reference data for layouts and sites.
### Actors
Super Administrator; section administrator; operational users (lookup).
### User Journey
Administrator maintains master sets and their active status; users consume active values while maintaining layouts/sites.
### Functional Capabilities
Maintain layout/site status, categories, reservation, road facing, corner/intermediate, and block/sector/phase/stage/section codes; audit and export.
### Inputs
Master type, code, name, status, display/order attributes as configured.
### Outputs
Active reference values and master export.
### Business Rules
Historical references are retained after deactivation; process-driving categories are subject to approval in Module 04.
### Validations
Unique code per master type; active values only for new selections.
### Calculations
None.
### Workflow
Direct administration with audit.
### Search Requirements
Master type, code, name, status.
### Documents
None.
### Reports
Master configuration export.
### Notifications
Optional critical-master change notification.
### Security
RBAC and critical-change audit.
### Integrations
Internal master-data consumption (Simple).
### Dependencies
Module 01 and Modules 03–04 consumers.
### Assumptions
BDA supplies final category/status values and permitted combinations.
### Risks
Uncontrolled category changes could affect downstream eligibility.
### Non Functional Requirements
Responsive UI; consistent lookups; auditability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Master register and filters | UI | Complex | 8 |
| Configurable master editor | UI | Complex | 8 |
| Master lifecycle and lookup operations | API | Complex | 8 |
| Master reference persistence | Database | Complex | 6 |
| Internal master-data consumption | Integration | Simple | 4 |
| Master and eligibility impact tests | Testing | Very High | 12 |
| Master configuration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Transactional classification is estimated in Module 04.
