# F05-001 — Live Vehicle Tracking Dashboard

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Live Vehicle Tracking Dashboard |
| **Module** | 05 — GPS Live Monitoring and Trip Lifecycle |

### Description
Operators view state-wide live vehicle locations, movement/ignition status, district and contractor filters, and load-carrying details from VLTS feed.

### Business Objective
Real-time visibility of food-grain transportation vehicles.

### Actors
User: CCC Operator / District Officer. Auditor: read-only.

### User Journey
1. Who creates: System displays live feed; Operator opens dashboard.
2. How they create: Opens Live Tracking, filters district/contractor/status, selects vehicle for detail.
3. How they edit: Filters only; location data is not manually edited.
4. How they send for approval: Not applicable.
5. How the approver sees pending items: No approver inbox.
6. How the approver decides: Not applicable.
7. How the user sees history: Recent viewed vehicles; trip history via F05-002.
8. How the supervisor/auditor sees history: Same scoped live view and audit of filter exports.

### Functional Capabilities
- Live map/list
- District/contractor filters
- Ignition/movement status
- Load details display

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| State-wide live tracking dashboard | Very High |
| Vehicle detail side panel | Complex |
| District-wise monitoring view | Complex |
| Contractor-wise monitoring view | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Query live vehicle positions | Very High |
| Query vehicle status | Complex |
| Filter by district/contractor | Medium |

### Inputs
Filters, vehicle id, status, location, load details.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Scope enforced by Post unit.
- GPS hardware out of scope.

### Validations
- Scope enforced.

### Calculations
None on UI beyond status badges.

### Workflow
No approval.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Snapshot export optional.

### Notifications
Alerts in Module 09.

### Security
Role-scoped live view.

### Integrations
Module 12 VLTS.

### Dependencies
F03-002, Module 12.

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
| State-wide live tracking dashboard | UI | Very High | 16 |
| Vehicle detail side panel | UI | Complex | 12 |
| District-wise monitoring view | UI | Complex | 12 |
| Contractor-wise monitoring view | UI | Medium | 6 |
| Query live vehicle positions | API | Very High | 16 |
| Query vehicle status | API | Complex | 8 |
| Filter by district/contractor | API | Medium | 6 |
| Latest position cache and filter prefs | DB | Complex | 6 |
| Consume VLTS live position feed | Integration | Very High | 40 |
| Live Vehicle Tracking Dashboard feature tests | Testing | Very High | 12 |
| Live Vehicle Tracking Dashboard implementation documentation | Documentation | Complex | 4 |

**Feature total: 138 hours**
