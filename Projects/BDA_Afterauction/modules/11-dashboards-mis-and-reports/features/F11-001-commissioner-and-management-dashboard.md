# F11-001 — Commissioner & Management Dashboard

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-001 |
| Feature Name | Commissioner & Management Dashboard |
| Module | 11 — Dashboards, MIS & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Organisation-wide dashboard with sites awarded, value, premium, payments due and collected, pendency by stage and DS office, overdue and defaults, completion rate and trends, with drill-down to lists and export.

### Business Objective
Give management real-time visibility of the post-auction pipeline and revenue.

### Actors
- Commissioner / Read-only Viewer
- Auction Admin

### User Journey
1. **Who creates:** Data is aggregated by the system.
2. **How they create:** Users open the dashboard and apply filters (auction, layout, period).
3. **How they edit:** Not editable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Users drill down to lists.
8. **How the approver / auditor sees history:** Auditors see dashboard access.

### Functional Capabilities
- KPI tiles
- Stage funnel
- Revenue trend
- DS-wise pendency
- Drill-down and export

### UI Screens
- Management dashboard
- Drill-down list

### Logical API Operations
- Dashboard KPI aggregation
- Trend data
- Drill-down list
- Export

### Inputs
- Filters

### Outputs
- KPIs and charts

### Business Rules
- Figures reconcile with ledger

### Validations
- Filter ranges

### Calculations
- KPIs

### Workflow
Not applicable

### Search Requirements
- Filters

### Documents
- None

### Reports
- Dashboard export

### Notifications
- None

### Security
- Read-only

### Integrations
- None

### Dependencies
- Modules 03–09

### Assumptions
- None

### Risks
- Performance; aggregates refreshed every 15 minutes

### Non Functional Requirements
- Loads within 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Management dashboard | Complex | 12 |
| UI | Drill-down list | Medium | 6 |
| API | Dashboard KPI aggregation | Complex | 8 |
| API | Trend data | Medium | 6 |
| API | Drill-down list | Medium | 6 |
| API | Export | Easy | 4 |
| Database | Reporting views / aggregates | Medium | 4 |
| Testing | KPI accuracy tests | Medium | 6 |
| Documentation | Dashboard KPI definitions | Easy | 2 |

**Feature Total: 54 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 24 | 4 | 0 | 6 | 2 | **54** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Aggregation rated Complex
- No external integration channel in this feature; Integration row omitted.
