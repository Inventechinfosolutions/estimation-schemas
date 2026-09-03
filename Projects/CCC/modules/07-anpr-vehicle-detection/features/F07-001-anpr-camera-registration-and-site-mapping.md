# F07-001 — ANPR Camera Registration and Site Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | ANPR Camera Registration and Site Mapping |
| **Module** | 07 — ANPR Vehicle Detection |

### Description
Administrator registers ANPR cameras at warehouse entry/exit and maps them to godown sites.

### Business Objective
Automated number-plate detection points.

### Actors
Maker: Surveillance Administrator. Checker: Warehouse Checker.

### User Journey
1. Who creates: Surveillance Administrator.
2. How they create: ANPR register → New: camera ID, site, lane (entry/exit), Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker ANPR inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Camera history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- Camera registration
- Site/lane mapping
- Maker–checker

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| ANPR camera register | Medium |
| ANPR camera form | Complex |
| ANPR history | Medium |
| ANPR checker inbox | Medium |
| ANPR approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Register ANPR camera | Medium |
| Update camera | Medium |
| Search cameras | Medium |
| Submit camera | Complex |
| Approve camera | Complex |

### Inputs
Camera ID, godown, lane, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Camera hardware supply may be separate; software registration here.

### Validations
- Camera ID unique.
- Site mandatory.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Camera list.

### Notifications
Checker/maker.

### Security
Surveillance Posts.

### Integrations
ANPR vendors.

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
| ANPR camera register | UI | Medium | 6 |
| ANPR camera form | UI | Complex | 12 |
| ANPR history | UI | Medium | 6 |
| ANPR checker inbox | UI | Medium | 6 |
| ANPR approval | UI | Easy | 4 |
| Register ANPR camera | API | Medium | 6 |
| Update camera | API | Medium | 6 |
| Search cameras | API | Medium | 6 |
| Submit camera | API | Complex | 8 |
| Approve camera | API | Complex | 8 |
| ANPR camera master | DB | Medium | 4 |
| ANPR camera/vendor interface | Integration | Complex | 24 |
| ANPR Camera Registration and Site Mapping feature tests | Testing | Very High | 12 |
| ANPR Camera Registration and Site Mapping implementation documentation | Documentation | Medium | 3 |

**Feature total: 111 hours**
