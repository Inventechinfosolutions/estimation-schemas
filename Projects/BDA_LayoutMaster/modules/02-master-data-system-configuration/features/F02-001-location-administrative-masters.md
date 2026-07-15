# F02-001 — Location & Administrative Masters
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Location & Administrative Masters |
| **Module** | 02 — Master Data & System Configuration |
### Description
Maintain location hierarchy and BDA organisation masters used by operational records and routing.
### Business Objective
Standardise location and administrative reference data across LMS.
### Actors
Super Administrator; section administrator; operational users (lookup).
### User Journey
Administrator maintains hierarchy values and status; users select active values in business transactions.
### Functional Capabilities
CRUD for country, state, district, taluk, village, hobli, zone, section, division, and department; hierarchical lookup; activation control; audit.
### Inputs
Master name, code, parent, status.
### Outputs
Active reference values and master export.
### Business Rules
Deactivated values remain visible on historical records but cannot be selected for new transactions.
### Validations
Unique code/name within parent; valid active parent; no deletion of referenced values.
### Calculations
None.
### Workflow
Direct administration with audit.
### Search Requirements
Name, code, parent, type, status.
### Documents
None.
### Reports
Location and organisation master export.
### Notifications
Optional change notification.
### Security
Administrator-only maintenance; read access for authorised users.
### Integrations
Internal master-data consumption (Simple).
### Dependencies
Module 01 access control.
### Assumptions
Hierarchy values and codes are supplied/approved by BDA.
### Risks
Changes to parent hierarchy can affect operational filtering.
### Non Functional Requirements
Fast dependent lookup; audit trail; responsive UI.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Hierarchical master register | UI | Complex | 8 |
| Master create/edit with dependent parent selection | UI | Complex | 8 |
| Master lifecycle and lookup operations | API | Complex | 8 |
| Hierarchical reference persistence | Database | Complex | 6 |
| Internal master-data consumption | Integration | Simple | 4 |
| Hierarchy and reference tests | Testing | Very High | 12 |
| Master administration guide | Documentation | Medium | 3 |
| **Total** | | | **49** |
### Estimation Assumptions
Bulk legacy migration is Module 14 scope.
