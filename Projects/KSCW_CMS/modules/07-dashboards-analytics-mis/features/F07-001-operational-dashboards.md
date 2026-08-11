# F07-001 — Operational Dashboards

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-001 |
| Feature Name | Operational Dashboards |
| Module | 07 — Dashboards, Analytics, Real-time Monitoring & MIS |
| Description | Provide role-based operational dashboards for day-to-day CMS management. |
| Business Objective | Give each role an at-a-glance view of operational load. |
| Actors | Admin; Supervisor; Operator (limited) |

### User Journey

- User logs in → lands on role dashboard → views KPIs/cards → drills to lists where linked.

### Functional Capabilities

- Role-specific dashboard layouts
- KPI cards (intake, pending, closed, etc. per design)
- Date/location filters as approved

### Inputs

- Role context
- Filter parameters

### Outputs

- Dashboard widgets/KPI values

### Business Rules

- Data scoped by role

### Validations

- Valid filter ranges

### Calculations

- Counts and simple rates per Dashboard Design

### Workflow

- N/A (read/monitor)

### Search Requirements

- Filters on dashboard

### Documents

- None

### Reports

- Links to MIS where designed

### Notifications

- None

### Security

- RBAC on widgets

### Integrations

- None

### Dependencies

- Modules 03–05

### Assumptions

- Approved Dashboard Design document

### Risks

- Design churn after estimation

### Non Functional Requirements

- Acceptable load time for KPI queries

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Role-based operational dashboard shells and KPI cards | Very High | 16 |
| API | Operational KPI aggregation endpoints | Complex | 8 |
| Database | Read models/indexes for dashboard counts | Medium | 4 |
| Testing | Role-scoped dashboard scenarios | Complex | 8 |
| Documentation | Operational dashboard notes | Medium | 3 |

**Feature Total: 39 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
