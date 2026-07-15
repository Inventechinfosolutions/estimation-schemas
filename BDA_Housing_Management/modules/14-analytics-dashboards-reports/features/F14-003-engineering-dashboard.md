# F14-003 — Engineering Dashboard

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-003 |
| **Feature Name** | Engineering Dashboard |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Present project development, approval, inventory-readiness, construction-status, and available-unit indicators for Engineering.
### Business Objective
Give Engineering a current view of project and inventory readiness.
### Actors
- Engineering Section; approvers; senior authority
### User Journey
1. Engineering Section selects the permitted dashboard. 2. BHMS applies authorized filters and presents reconciled KPIs. 3. The user drills to an authorized register where required.
### Functional Capabilities
- Role-based navigation, KPI cards, filters, trends/distributions, and permitted source-register drill-through.
### Inputs
- Project/area/status filters and project/inventory records.
### Outputs
- Engineering KPI views and permitted drill-through to project/unit records.
### Business Rules
- Only captured construction/progress indicators are reported; no GIS platform is included.
### Validations
- Authorized engineering role and valid project/status filters.
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
- Modules 03–05 and F14-001.
### Assumptions
- Construction progress is maintained in the source project/unit processes.
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
