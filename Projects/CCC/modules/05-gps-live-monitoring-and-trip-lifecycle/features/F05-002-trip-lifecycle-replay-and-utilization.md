# F05-002 — Trip Lifecycle, Replay and Utilization

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Trip Lifecycle, Replay and Utilization |
| **Module** | 05 — GPS Live Monitoring and Trip Lifecycle |

### Description
System manages trip initiation/closure (including geo-fence automation), halt/idle, route deviation monitoring, historical trip replay and utilization.

### Business Objective
Complete trip lifecycle and historical playback.

### Actors
Applicant: Operations Officer (manual trip open/close when needed). Approver: Supervisor if manual override. System automates geo-fence start/end.

### User Journey
1. Who creates: System on geo-fence entry/exit, or Officer for manual trip.
2. How they create: Trip register → New/auto: vehicle, route, start time, Save. Closure on destination geo-fence or manual close.
3. How they edit: Manual corrections only on Draft/Returned override requests.
4. How they send for approval: Manual override submit to Supervisor.
5. How the approver sees pending items: Supervisor trip-override inbox.
6. How the approver decides: Approve override or return.
7. How the applicant sees history: Trip history and replay for own unit.
8. How the approver sees history: Team trips and replay.

### Functional Capabilities
- Trip start/end
- Geo-fence automation
- Halt/idle
- Trip replay
- Utilization

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Trip register | Complex |
| Trip form / override | Complex |
| Trip replay player | Very High |
| Utilization dashboard | Complex |
| Trip override inbox | Medium |
| Trip decision panel | Easy |
| Trip history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Open trip | Complex |
| Close trip | Complex |
| Record halt/idle | Medium |
| Detect route deviation | Very High |
| Replay trip track | Very High |
| Submit override | Complex |
| Approve override | Complex |

### Inputs
Vehicle, route, start/end, halt events, deviation flags.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Auto start/end preferred; manual override audited.

### Validations
- Vehicle must have active device and route assignment.

### Calculations
Utilization from trip times; ETA vs actual.

### Workflow
Auto trips; manual override Draft → Approved.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Trip and utilization reports (Module 11).

### Notifications
Deviation/delay → Module 09.

### Security
Unit-scoped.

### Integrations
Uses live feed from F05-001.

### Dependencies
F04-002, F05-001.

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
| Trip register | UI | Complex | 12 |
| Trip form / override | UI | Complex | 12 |
| Trip replay player | UI | Very High | 16 |
| Utilization dashboard | UI | Complex | 12 |
| Trip override inbox | UI | Medium | 6 |
| Trip decision panel | UI | Easy | 4 |
| Trip history | UI | Medium | 6 |
| Open trip | API | Complex | 8 |
| Close trip | API | Complex | 8 |
| Record halt/idle | API | Medium | 6 |
| Detect route deviation | API | Very High | 16 |
| Replay trip track | API | Very High | 16 |
| Submit override | API | Complex | 8 |
| Approve override | API | Complex | 8 |
| Trip, events and track points metadata | DB | Very High | 10 |
| Trip Lifecycle, Replay and Utilization feature tests | Testing | Very High | 12 |
| Trip Lifecycle, Replay and Utilization implementation documentation | Documentation | Complex | 4 |

**Feature total: 164 hours**
