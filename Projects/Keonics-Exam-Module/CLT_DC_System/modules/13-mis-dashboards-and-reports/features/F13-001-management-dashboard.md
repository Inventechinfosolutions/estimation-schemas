# F13-001 — Management Dashboard

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-001 |
| Feature Name | Management Dashboard |
| Module | 13 — MIS, Dashboards & Reports |
| Module Type | Business |
| Release | Go-live |

### Description
Management dashboard with KPIs: registrations by category and district, bookings and utilisation, tests conducted, attendance, pass percentage, average scores by topic, fee collections, malpractice cases, helpdesk tickets, SLA status, with trends and drill-down.

### Business Objective
Give management a single view of the programme.

### Actors
- KEONICS
- Center for E-Governance
- DPAR

### User Journey
1. **Who creates:** Dashboard populated from transactions.
2. **How they create:** Users select filters.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Users see KPIs.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see access logs.

### Functional Capabilities
- KPI tiles
- Trends
- District and period filters
- Drill-down
- Export

### UI Screens
- Management dashboard
- KPI drill-down

### Logical API Operations
- KPI aggregation
- Drill-down queries

### Inputs
- Transactions

### Outputs
- KPIs

### Business Rules
- Scope by role

### Validations
- None

### Calculations
- Rates, averages

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
- All business modules

### Assumptions
- None

### Risks
- None

### Non Functional Requirements
- Under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Management dashboard | Complex | 12 |
| UI | KPI drill-down | Medium | 6 |
| API | KPI aggregation | Complex | 8 |
| API | Drill-down queries | Medium | 6 |
| Database | Reporting aggregates | Medium | 4 |
| Testing | KPI reconciliation tests | Medium | 6 |
| Documentation | KPI definitions | Easy | 2 |

**Feature Total: 44 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 14 | 4 | 0 | 6 | 2 | **44** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
