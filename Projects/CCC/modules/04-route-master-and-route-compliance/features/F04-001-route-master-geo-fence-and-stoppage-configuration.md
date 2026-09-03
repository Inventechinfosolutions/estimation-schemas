# F04-001 — Route Master, Geo-fence and Stoppage Configuration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Route Master, Geo-fence and Stoppage Configuration |
| **Module** | 04 — Route Master and Route Compliance |

### Description
Route Administrator defines source–destination routes, geo-fences for warehouses/FPS, deviation limits, authorized stoppages and expected travel time.

### Business Objective
Authorized transportation routes as directed by the Department.

### Actors
Maker: Route Administrator. Checker: Route Checker / District Officer.

### User Journey
1. Who creates: Route Administrator.
2. How they create: Route register → New: source, destination, waypoints, geo-fence polygons, deviation limit, stoppages, ETA, Save draft.
3. How they edit: Draft/Returned editable. Approved route change is a new version.
4. How they send for approval: Submit to Route Checker.
5. How the approver sees pending items: Checker route inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Route version history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- Route master
- Geo-fence
- Stoppage and ETA config
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Route register | Medium |
| Route and geo-fence designer | Very High |
| Stoppage/ETA panel | Complex |
| Route history | Medium |
| Route checker inbox | Medium |
| Route approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create route | Complex |
| Update geo-fence | Very High |
| Search routes | Medium |
| Submit route | Complex |
| Approve route | Complex |
| Read route history | Easy |

### Inputs
Source, destination, geo-fence, deviation limit, stoppages, expected time.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Geo-fence uses approved locations from Module 02.

### Validations
- Source and destination mandatory.
- Deviation limit > 0.

### Calculations
Expected travel time may be configured.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Route catalogue.

### Notifications
Checker/maker.

### Security
Route admin Posts.

### Integrations
None.

### Dependencies
F02-002.

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
| Route register | UI | Medium | 6 |
| Route and geo-fence designer | UI | Very High | 16 |
| Stoppage/ETA panel | UI | Complex | 12 |
| Route history | UI | Medium | 6 |
| Route checker inbox | UI | Medium | 6 |
| Route approval | UI | Easy | 4 |
| Create route | API | Complex | 8 |
| Update geo-fence | API | Very High | 16 |
| Search routes | API | Medium | 6 |
| Submit route | API | Complex | 8 |
| Approve route | API | Complex | 8 |
| Read route history | API | Easy | 4 |
| Route, geo-fence and version history | DB | Very High | 10 |
| Route Master, Geo-fence and Stoppage Configuration feature tests | Testing | Very High | 12 |
| Route Master, Geo-fence and Stoppage Configuration implementation documentation | Documentation | Complex | 4 |

**Feature total: 126 hours**
