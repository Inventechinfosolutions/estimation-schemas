# F06-002 — CAO Basic KPIs

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F06-002 |
| Feature Name | CAO Basic KPIs |
| Module | 06 — Dashboards, KPIs & MIS |
| Description | Pending and outcome count KPIs for CAO with filters. |
| Business Objective | Help CAO track verification backlog and outcomes. |
| Actors | CAO |

### User Journey

- CAO opens KPI view → sees pending/verified/returned/rejected counts → filters as needed.

### Functional Capabilities

- Pending count
- Verified/Returned/Rejected counts
- Filters

### Inputs

- Date range
- Geo filter

### Outputs

- CAO KPI view

### Business Rules

- CAO organization-wide counts

### Validations

- None

### Calculations

- Status counts

### Workflow

- None

### Search Requirements

- By status/period/geo

### Documents

- None

### Reports

- Optional export

### Notifications

- None

### Security

- CAO

### Integrations

- None

### Dependencies

- F05-001

### Assumptions

- Statuses consistent

### Risks

- Backlog spikes

### Non Functional Requirements

- Web responsive

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | CAO KPI dashboard | Complex | 8 |
| API | CAO KPI aggregates | Medium | 6 |
| Database | Persistence / constraints for this feature | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 24 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
