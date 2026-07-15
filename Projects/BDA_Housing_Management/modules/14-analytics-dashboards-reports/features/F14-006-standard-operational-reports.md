# F14-006 — Standard Operational Reports

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-006 |
| **Feature Name** | Standard Operational Reports |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Provide filterable project, inventory, booking, payment, registration/possession, citizen application, administrative activity, workflow-pendency, and audit reports.
### Business Objective
Give authorized BDA users reproducible operational registers and process evidence.
### Actors
- Section officers; approvers; Auditor; senior authority
### User Journey
1. User chooses a permitted report and filters it. 2. BHMS retrieves the reconciled result. 3. User reviews or exports the report through F14-008.
### Functional Capabilities
- Packaged operational reports, filters, totals, sorting, detail views, and report access history.
### Inputs
- Authorized report, filter criteria, source registers, and date range.
### Outputs
- Filterable report result with source-register totals.
### Business Rules
- Reports reflect source-module records and enforce the report viewer’s role permissions.
### Validations
- Report permission, valid filters, date range, and source-record availability.
### Calculations
- Totals and counts from source registers only.
### Workflow
- Select report → filter → retrieve → review/export.
### Search Requirements
- By project, unit, application, booking, payment, registration, possession, actor, date, and status.
### Documents
- Source-linked documents only where the viewer is authorized.
### Reports
- The packaged operational reports are the output of this feature.
### Notifications
- No independent notifications.
### Security
- RBAC, citizen ownership isolation, export audit, and protected sensitive fields.
### Integrations
- Internal BHMS reporting services.
### Dependencies
- Modules 01 and 03–11; F14-001 and F14-008.
### Assumptions
- Packaged reports cover the SOW list; ad-hoc BI warehouse reporting is excluded.
### Risks
- State-history quality can affect pendency/audit report acceptance.
### Non Functional Requirements
- Reproducible filters, expected-volume performance, and register reconciliation.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Filterable report workspace | UI | Very High | 16 |
| Report retrieval and aggregation operations | API | Complex | 8 |
| Report query and aggregation support | Database | Medium | 4 |
| Report tests | Testing | Complex | 8 |
| Report guide | Documentation | Complex | 4 |
| **Total** | | | **40** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Report UI is Very High (16); source workflows remain owned by business modules.
