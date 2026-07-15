# F14-002 — Management Dashboard

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-002 |
| **Feature Name** | Management Dashboard |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Present executive KPIs for projects, unit availability/sales, cancellations, registrations, possessions, collections, pending revenue, refunds, auto-cancellations, and project/area trends.
### Business Objective
Give senior BDA authority a reconciled portfolio view for decisions.
### Actors
- Commissioner/senior authority; Auditor
### User Journey
1. Commissioner/senior authority selects the permitted dashboard. 2. BHMS applies authorized filters and presents reconciled KPIs. 3. The user drills to an authorized register where required.
### Functional Capabilities
- Role-based navigation, KPI cards, filters, trends/distributions, and permitted source-register drill-through.
### Inputs
- Date/project/area filters and aggregated lifecycle data.
### Outputs
- Executive KPI cards, trend/distribution views, and authorized drill-through.
### Business Rules
- KPIs reconcile to underlying BHMS registers; management views do not change source records.
### Validations
- KPI definitions, filter dates, and authorized drill-through.
### Calculations
- KPI totals, balances, counts, and trends are calculated only from source records.
### Workflow
- Open view → apply filters → review KPIs → drill through.
### Search Requirements
- By authorized project, area, date, lifecycle status, and KPI dimension.
### Documents
- No standalone documents; links are controlled by source processes.
### Reports
- Dashboard KPI and filtered operational visibility.
### Notifications
- No independent notifications; source alerts remain in Module 12.
### Security
- RBAC, least-privilege access, protected sensitive values, and auditable activity.
### Integrations
- Internal BHMS data services.
### Dependencies
- Modules 03–10 and F14-001.
### Assumptions
- BDA confirms KPI definitions and presentation priorities.
### Risks
- Incomplete or inconsistent source statuses can affect KPI acceptance.
### Non Functional Requirements
- Near-real-time refresh, expected-volume performance, and KPI-to-register reconciliation.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Role-based dashboard workspace | UI | Very High | 16 |
| KPI retrieval and authorized drill-through operations | API | Complex | 8 |
| Dashboard aggregation support | Database | Medium | 4 |
| Dashboard tests | Testing | Complex | 8 |
| Dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Dashboard UI is Very High (16).
