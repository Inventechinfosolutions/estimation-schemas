# F09-004 — Claim decision dashboards

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-004 |
| **Feature Name** | Claim decision dashboards |
| **Module** | 09 — Operational Reports, Lists & Special Court Outputs |

### Description
The Officer or Competent Authority opens dashboards, filters by imported FE, scheme, window or status, and views claim and settlement counts and exceptions. Menu access follows Module 01; another Post does not see restricted slices.

### Business Objective
Give authorised users queryable dashboards of claim and settlement counts and exceptions under need-to-know.

### Actors
Officer; Competent Authority; other authorised Posts.

### User Journey
1. Officer or Competent Authority opens dashboards.
2. User filters by imported FE, scheme, window or status.
3. User views claim and settlement counts and exceptions.
4. Another Post does not see restricted slices; menu access follows Module 01.

### Functional Capabilities
- Decision dashboards with FE/scheme/window/status filters.
- Claim and settlement counts and exceptions.
- Visibility restricted by Post/Role.

### Inputs
Filters: imported FE, scheme, window, status.

### Outputs
Dashboard views; authorised data extracts as allowed.

### Business Rules
- Dashboard/query outputs are restricted by Module 01 visibility rules.
- Raw data extract is authorised-Post only.
- No generative narrative of the dashboard.

### Validations
- Filters limited to imported FE/scheme references.

### Calculations
Counts and exception tallies.

### Workflow
Open dashboard → filter → view. No approval workflow.

### Search Requirements
Dashboard filters are the query.

### Documents
None.

### Reports
Dashboard / decision reports (structured).

### Notifications
None.

### Security
Restricted slices hidden. Access to dashboards is itself permissioned.

### Integrations
None.

### Dependencies
Modules 02–08 data; F01-003.

### Assumptions
- Exact widgets follow Authority operational questions; this feature covers claim/settlement counts and exceptions.

### Risks
- Unfiltered dashboards would leak KYC-adjacent volumes across Posts.

### Non Functional Requirements
Usable filters. Availability during claim-window operations.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Claim decision dashboard | UI | Very High | 16 |
| Dashboard query operations | API | Very High | 16 |
| Dashboard aggregates | DB | Complex | 6 |
| Dashboard tests | Testing | Very High | 12 |
| Dashboard note | Documentation | Medium | 3 |
| **Total** | | | **53** |

### Estimation Assumptions
- Uses Estimation Master values only.
- UI Very High is the dashboard (Estimation Master dashboard class), not UI Complex 8.
