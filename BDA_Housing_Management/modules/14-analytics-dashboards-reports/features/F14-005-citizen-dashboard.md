# F14-005 — Citizen Dashboard

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-005 |
| **Feature Name** | Citizen Dashboard |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Present each citizen’s own applications, booking/payment status, balance, issued artefacts, notifications, and permitted downloads.
### Business Objective
Give citizens a single self-service status view without exposing other parties’ data.
### Actors
- Citizen
### User Journey
1. Citizen selects the permitted dashboard. 2. BHMS applies authorized filters and presents reconciled KPIs. 3. The user drills to an authorized register where required.
### Functional Capabilities
- Role-based navigation, KPI cards, filters, trends/distributions, and permitted source-register drill-through.
### Inputs
- Authenticated citizen identity and own linked transaction records.
### Outputs
- Personal dashboard, status timeline, balances, alerts, and permitted artefact links.
### Business Rules
- A citizen can view only their own records; documents appear only after their owning process authorizes them.
### Validations
- Authenticated citizen ownership and source-record access.
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
- Modules 06–11, F12-001, and F14-001.
### Assumptions
- Citizen portal authentication and ownership controls are available.
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
