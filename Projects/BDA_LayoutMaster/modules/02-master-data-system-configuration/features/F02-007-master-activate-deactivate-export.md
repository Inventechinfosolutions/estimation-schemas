# F02-007 — Master Activate, Deactivate & Export
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F02-007 |
| **Feature Name** | Master Activate, Deactivate & Export |
| **Module** | 02 — Master Data & System Configuration |
### Description
Provide consistent lifecycle controls, reference-impact checks, search, and export across configured masters.
### Business Objective
Protect historical records while enabling controlled master-data maintenance.
### Actors
Super Administrator; section administrator; Auditor.
### User Journey
Administrator searches a master, reviews its reference impact, activates/deactivates it with reason, and exports the filtered register.
### Functional Capabilities
Cross-master search/filter, activation/deactivation with impact warning, critical-change audit, and export.
### Inputs
Master type, target value, requested status, reason, filters.
### Outputs
Lifecycle outcome, impact warning, export, audit entry.
### Business Rules
Referenced masters are never deleted; deactivated values remain historical but cannot be newly selected.
### Validations
Authorised administrator; valid target; mandatory reason for controlled deactivation.
### Calculations
Reference impact/count display where available.
### Workflow
Direct controlled maintenance with audit.
### Search Requirements
Master type, code/name, status, date, modifier.
### Documents
None.
### Reports
Master status and change export.
### Notifications
Optional critical-change alert.
### Security
RBAC, audit, and restricted activation authority.
### Integrations
Internal master-data consumption (Simple).
### Dependencies
F02-001 through F02-006 and all consuming modules.
### Assumptions
Individual master form maintenance is estimated in its owning feature.
### Risks
Deactivation of a widely used value may disrupt operational selection.
### Non Functional Requirements
Responsive searches/exports; historical integrity.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Cross-master search and export | UI | Complex | 8 |
| Lifecycle confirmation and impact view | UI | Medium | 6 |
| Lifecycle and export operations | API | Complex | 8 |
| Lifecycle audit persistence | Database | Medium | 4 |
| Internal master-data consumption | Integration | Simple | 4 |
| Lifecycle integrity tests | Testing | Complex | 8 |
| Master lifecycle guide | Documentation | Medium | 3 |
| **Total** | | | **41** |
### Estimation Assumptions
No generic reporting platform is included.
