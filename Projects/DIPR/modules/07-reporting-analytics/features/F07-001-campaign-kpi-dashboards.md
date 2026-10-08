# F07-001 — Campaign KPI dashboards

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-001 |
| Feature Name | Campaign KPI dashboards |
| Module | 07 — Reporting & Analytics |
| Description | Role-based dashboards for campaign progress, PoD completion, and status KPIs |
| Business Objective | Give managers at-a-glance campaign health and PoD completion against plan. |
| Actors | DIPR Admin; Campaign Manager; Verifier; Viewer (read-only) |

### User Journey

- User logs in → lands on role dashboard → views KPI cards (active campaigns, PoD completion %, pending verification) → applies date/campaign filters → drills to lists where linked.

### Functional Capabilities

- Role-specific dashboard layouts
- KPI cards for campaign progress, PoD completion, verification backlog
- Filters by date range, media channel, campaign, and org scope
- Drill-through links to campaign and PoD registers

### Inputs

Role context; filter parameters

### Outputs

Dashboard widgets and KPI values

### Business Rules

Data scoped by role and organisational unit
KPI definitions finalized with DIPR during design

### Validations

- N/A

### Calculations

Completion rates and counts derived from campaign and PoD source data

### Workflow

- N/A

### Search Requirements

- N/A

### Documents

- None

### Reports

- None

### Notifications

- None

### Security

- RBAC and platform security controls apply

### Integrations

- None

### Dependencies

Modules 03, 05; F07-006 for entitlements

### Assumptions

Approved KPI definition catalogue from DIPR workshops

### Risks

KPI definition changes after baseline estimation

### Non Functional Requirements

- Production-grade performance and reliability for government deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Executive KPI dashboard shell with date/campaign filters | Very High | 16 |
| UI | Campaign status KPI card strip | Medium | 6 |
| UI | PoD verification progress KPI cards | Medium | 6 |
| UI | Field completion funnel chart panel | Complex | 12 |
| UI | Drill-down to campaign list from KPI click | Easy | 4 |
| UI | Role-scoped dashboard empty state | Simple | 2 |
| API | Campaign count aggregates by status | Medium | 6 |
| API | PoD submitted/verified/rejected KPI aggregates | Complex | 8 |
| API | Field task completion rate aggregate | Medium | 6 |
| API | Dashboard filter metadata (campaigns, regions) | Easy | 4 |
| Database | KPI aggregate materialized summary support | Medium | 4 |
| Database | Dashboard query indexes on campaign dates | Easy | 2 |
| Testing | Role-scoped KPI visibility | Complex | 8 |
| Testing | Filter combination accuracy | Medium | 6 |
| Testing | KPI numbers vs source module sample | Complex | 8 |
| Documentation | KPI definition dictionary | Medium | 3 |
| Documentation | Dashboard user interpretation guide | Easy | 2 |

**Feature Total: 103 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, hosting certification, warranty operations) are excluded from feature hours.
