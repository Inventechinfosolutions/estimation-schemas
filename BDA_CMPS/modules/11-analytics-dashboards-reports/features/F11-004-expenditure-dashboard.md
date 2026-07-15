# F11-004 — Expenditure Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-004 |
| **Feature Name** | Expenditure Dashboard |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Expenditure dashboard for total expenses by category, maintenance, repairs, tax, and vendor payments with drill-down to Module 07.

### Business Objective
Control visibility of property spend and vendor outflows.

### Actors
- Accounts, Chief Engineer, Maintenance leadership, Auditor

### User Journey
1. Select period/scope.
2. Review category breakdown and vendor payment totals.
3. Drill into expense register.

### Functional Capabilities
- Total expenses; category breakdown
- Maintenance/repairs tiles
- Tax and vendor payment aggregates
- Drill-down

### Inputs
- Period filters

### Outputs
- Spend KPIs/charts

### Business Rules
- Align to posted expenditures (M6-AC5 lineage).
- Scoped properties only.

### Validations
N/A.

### Calculations
- Sums by category; period comparisons optional

### Workflow
N/A.

### Search Requirements
Drill-down.

### Documents
None.

### Reports
Links to expense reports.

### Notifications
None.

### Security
Scoped RBAC.

### Integrations
None.

### Dependencies
F11-001; Module 07; Module 06 tax links if shown

### Assumptions
- Budget vs actual remains F07-007; may deep-link.

### Risks
- Double counting tax if also in revenue tiles—label BDA-paid tax spend clearly.

### Non Functional Requirements
- Fast category rollups

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Expenditure dashboard UI | UI | Very High | 16 |
| Expenditure KPI query ops | API | Complex | 8 |
| Expenditure KPI support | Database | Easy | 2 |
| Expenditure dashboard tests | Testing | Complex | 8 |
| Expenditure dashboard guide | Documentation | Easy | 2 |
| **Total** | | | **36** |

### Estimation Assumptions
- Very High dashboard UI.
