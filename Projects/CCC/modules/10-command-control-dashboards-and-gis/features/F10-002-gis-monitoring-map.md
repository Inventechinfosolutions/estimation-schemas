# F10-002 — GIS Monitoring Map

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | GIS Monitoring Map |
| **Module** | 10 — Command Control Dashboards and GIS |

### Description
GIS map shows live vehicles, routes, godowns, district/taluk boundaries, incidents, alerts and geo-fenced areas with drill-down.

### Business Objective
Map-based operational awareness.

### Actors
User: CCC Operator / District Officer. Auditor: read.

### User Journey
1. Who creates: Operator opens GIS map.
2. How they create: Selects layers (vehicles, routes, godowns, incidents), filters district, drills into feature.
3. How they edit: Layer/filter only.
4. How they send for approval: Not applicable.
5. How the approver sees pending items: No inbox.
6. How the approver decides: Not applicable.
7. How the user sees history: Optional last layer set.
8. How the auditor sees history: Map access log if enabled.

### Functional Capabilities
- Live GIS layers
- Boundaries
- Incident/alert pins
- Drill-down

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| GIS monitoring map | Very High |
| Layer control panel | Complex |
| Feature drill-down panel | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query GIS layer data | Very High |
| Resolve feature details | Complex |

### Inputs
Layers, district filter, selected feature.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Uses Module 02 locations and Module 04 geo-fences.

### Validations
- Scope enforced.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Map snapshot optional.

### Notifications
None.

### Security
Unit-scoped layers.

### Integrations
GIS basemap.

### Dependencies
Modules 02, 04, 05, 09.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| GIS monitoring map | UI | Very High | 16 |
| Layer control panel | UI | Complex | 12 |
| Feature drill-down panel | UI | Medium | 6 |
| Query GIS layer data | API | Very High | 16 |
| Resolve feature details | API | Complex | 8 |
| GIS layer cache metadata | DB | Medium | 4 |
| Base map / GIS platform service | Integration | Complex | 24 |
| GIS Monitoring Map feature tests | Testing | Very High | 12 |
| GIS Monitoring Map implementation documentation | Documentation | Complex | 4 |

**Feature total: 102 hours**
