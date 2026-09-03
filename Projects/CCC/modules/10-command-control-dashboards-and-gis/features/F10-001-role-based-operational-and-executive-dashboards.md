# F10-001 — Role-based Operational and Executive Dashboards

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-001 |
| **Feature Name** | Role-based Operational and Executive Dashboards |
| **Module** | 10 — Command Control Dashboards and GIS |

### Description
Configurable dashboards for vehicle, CCTV, alert, incident, executive, SLA and system-health views with district drill-down.

### Business Objective
Unified operational supervision for State CCC and districts.

### Actors
Maker: MIS Administrator (definitions). User: CME-equivalent FCS Posts, District Officers, Executives. Checker: MIS Checker for definitions.

### User Journey
1. Who creates: MIS Administrator defines dashboard for a Role; users open My Dashboard.
2. How they create: Dashboard definition → widgets, audience Role, Save draft. User: open dashboard, filter, drill.
3. How they edit: Definition versions maker–checker. Users change filters only.
4. How they send for approval: Definition submit to MIS Checker.
5. How the approver sees pending items: Checker definition inbox.
6. How the approver decides: Approve definition go-live.
7. How the maker sees history: Definition versions.
8. How the checker/auditor sees history: Approved definitions; users see filter history optional.

### Functional Capabilities
- Role-based dashboards
- District drill-down
- Configurable widgets
- Auto-refresh live data

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Dashboard canvas | Very High |
| State dashboard | Very High |
| District dashboard | Complex |
| Executive dashboard | Complex |
| SLA / system health dashboard | Complex |
| Definition checker inbox | Medium |
| Definition approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query widget data | Very High |
| Save dashboard definition | Complex |
| Submit definition | Complex |
| Approve definition | Complex |

### Inputs
Widgets, audience Role, filters.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Data scope by Post unit.

### Validations
- Audience Role mandatory.

### Calculations
Widget KPIs from live modules.

### Workflow
Maker–checker on definitions.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
N/A.

### Notifications
None.

### Security
Role-scoped widgets.

### Integrations
Consumes Modules 05–09.

### Dependencies
Modules 05–09.

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
| Dashboard canvas | UI | Very High | 16 |
| State dashboard | UI | Very High | 16 |
| District dashboard | UI | Complex | 12 |
| Executive dashboard | UI | Complex | 12 |
| SLA / system health dashboard | UI | Complex | 12 |
| Definition checker inbox | UI | Medium | 6 |
| Definition approval | UI | Easy | 4 |
| Query widget data | API | Very High | 16 |
| Save dashboard definition | API | Complex | 8 |
| Submit definition | API | Complex | 8 |
| Approve definition | API | Complex | 8 |
| Dashboard definitions and prefs | DB | Complex | 6 |
| Role-based Operational and Executive Dashboards feature tests | Testing | Very High | 12 |
| Role-based Operational and Executive Dashboards implementation documentation | Documentation | Complex | 4 |

**Feature total: 140 hours**
