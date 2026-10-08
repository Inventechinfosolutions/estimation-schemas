# F06-001 — Operations Dashboard

| Field | Value |
|-------|-------|
| Feature ID | F06-001 |
| Feature Name | Operations Dashboard |
| Module | 06 — Administration, Monitoring & Reports |
| Type | Business |
| Notes | Go-live |

## Feature Specification

### Description
Administrative dashboard showing bookings, occupancy, and payments summaries.

### Business Objective
Give administrators at-a-glance operational awareness across sites.

### Actors
- Platform Administrator
- Site Administrator

### User Journey
1. Administrator opens dashboard (no 'create' entity).
2. Selects site/date filters; views KPI cards and charts/lists.
3. Refines filters; no approval.
4. Approval does not apply.
5. No approver inbox.
6. No approver decision.
7. Dashboard is live/operational — history is in underlying registers.
8. Auditor may use read-only dashboard if role granted.

### Functional Capabilities
- Show booking counts
- Show occupancy snapshot
- Show payment success/failure summaries
- Filter by site/date

### UI Screens
- Operations dashboard
- Dashboard filter bar

### Logical API Operations
- Get dashboard booking metrics
- Get dashboard occupancy metrics
- Get dashboard payment metrics

### Inputs
- Actor inputs and selections as described in the user journey and validations
- System timestamps and configuration policy values

### Outputs
- Persisted domain records for this feature
- Screen payloads and status messages
- Audit entries for material actions

### Business Rules
- Site Administrator sees only scoped sites
- Metrics from authoritative modules

### Validations
- Date range valid

### Calculations
- Occupancy %
- Payment success rate

### Workflow
ViewOnly

### Search Requirements
Filters on dashboard

### Documents
None

### Reports
Dashboard complements formal reports

### Notifications
None

### Security
- Role and site scope

### Integrations
None

### Dependencies
- F03-002
- F04-002
- F05-003

### Assumptions
- Near-real-time aggregates acceptable

### Risks
- Heavy queries without summary tables

### Non Functional Requirements
- Dashboard load within acceptable admin wait

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Operations dashboard | Very High | 16 |
| UI | Dashboard filter bar | Easy | 4 |
| API | Get dashboard booking metrics | Complex | 8 |
| API | Get dashboard occupancy metrics | Complex | 8 |
| API | Get dashboard payment metrics | Complex | 8 |
| Database | Persistence for feature entities/constraints | Easy | 2 |
| Testing | Feature test coverage | Medium | 6 |
| Documentation | Feature documentation | Easy | 2 |

**Feature Total: 54 hours**

### Estimation Assumptions
- Hours use the Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- Major complexity drivers: Near-real-time aggregates acceptable / Heavy queries without summary tables.
