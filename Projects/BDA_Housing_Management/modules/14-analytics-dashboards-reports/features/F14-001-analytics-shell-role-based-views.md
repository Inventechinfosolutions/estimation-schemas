# F14-001 — Analytics Shell & Role-Based Views

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-001 |
| **Feature Name** | Analytics Shell & Role-Based Views |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Provide the analytics landing area with role-based navigation, authorized dashboard selection, common filters, and drill-through controls.
### Business Objective
Establish a secure, consistent entry point for all BHMS analytics.
### Actors
- Commissioner/senior authority; section officers; Accounts; Auditor; Citizen
### User Journey
1. Commissioner/senior authority selects the permitted dashboard. 2. BHMS applies authorized filters and presents reconciled KPIs. 3. The user drills to an authorized register where required.
### Functional Capabilities
- Role-based navigation, KPI cards, filters, trends/distributions, and permitted source-register drill-through.
### Inputs
- Authorized role, selected view, date/project filters.
### Outputs
- Authorized dashboard navigation, saved context, and unavailable-view handling.
### Business Rules
- Only dashboard views permitted to the current role are available.
### Validations
- Role access, valid filter combinations, and ownership isolation for citizen views.
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
- F14-002–F14-008 and Modules 01, 03–11.
### Assumptions
- Role mapping is maintained in Module 01.
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
