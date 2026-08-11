# F06-001 — Super Admin Basic KPIs

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-001 |
| Feature Name | Super Admin Basic KPIs |
| Module | 06 — Dashboards, KPIs & MIS |
| Description | Simple count KPIs for users/applications for Super Admin with date/geo filters and export. |
| Business Objective | Give Super Admin operational visibility of CDRMS volumes. |
| Actors | Super Admin |

### User Journey

- Super Admin opens dashboard → filters date/geo → views counts → optional Excel/CSV export.

### Functional Capabilities

- Active engineers count
- Applications by status/geo/period
- Filters
- Export

### Inputs

- Date range
- Geo filter

### Outputs

- KPI tiles/tables
- Export file

### Business Rules

- Counts from live data

### Validations

- None

### Calculations

- Aggregations by status/geo/period

### Workflow

- None

### Search Requirements

- By geo, status, period

### Documents

- None

### Reports

- KPI Excel/CSV

### Notifications

- None

### Security

- Super Admin

### Integrations

- None

### Dependencies

- F01-001
- F04-008

### Assumptions

- Online data current

### Risks

- Heavy periods slow aggregates

### Non Functional Requirements

- Dashboard usable on web

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Super Admin KPI dashboard | Very High | 16 |
| UI | KPI export | Easy | 4 |
| API | KPI aggregate queries + export | Complex | 8 |
| Database | Persistence / constraints for this feature | Medium | 4 |
| Testing | Feature test coverage | Complex | 8 |
| Documentation | Feature documentation | Medium | 3 |

**Feature Total: 43 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
