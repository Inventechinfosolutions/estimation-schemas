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
1. Who creates: Officer
2. How they create: Officer or Competent Authority opens dashboards.
3. How they edit: User filters by imported FE, scheme, window or status.
4. How they send for approval: User views claim and settlement counts and exceptions. Open dashboard → filter → view. No approval workflow.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Another Post does not see restricted slices; menu access follows Module 01.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Decision dashboards with FE/scheme/window/status filters.
- Claim and settlement counts and exceptions.
- Visibility restricted by Post/Role.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My claim decision dashboards list / queue | Medium |
| Claim decision dashboard | Very High |
| Claim decision dashboards history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Dashboard query operations | Very High |
| Update claim decision dashboards | Medium |
| Search claim decision dashboards | Medium |
| Read claim decision dashboards history | Easy |

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
| My claim decision dashboards list / queue | UI | Medium | 6 |
| Claim decision dashboard | UI | Very High | 16 |
| Claim decision dashboards history | UI | Medium | 6 |
| Dashboard query operations | API | Very High | 16 |
| Update claim decision dashboards | API | Medium | 6 |
| Search claim decision dashboards | API | Medium | 6 |
| Read claim decision dashboards history | API | Easy | 4 |
| Dashboard aggregates | DB | Complex | 6 |
| Claim decision dashboards feature tests | Testing | Very High | 12 |
| Claim decision dashboards implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **81** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
