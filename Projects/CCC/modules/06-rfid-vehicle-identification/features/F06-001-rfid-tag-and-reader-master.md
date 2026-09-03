# F06-001 — RFID Tag and Reader Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | RFID Tag and Reader Master |
| **Module** | 06 — RFID Vehicle Identification |

### Description
Administrator manages RFID tags, maps tags to vehicles, and registers readers at warehouse entry/exit.

### Business Objective
Tamper-resistant vehicle identification at godowns.

### Actors
Maker: Warehouse/RFID Administrator. Checker: Warehouse Checker.

### User Journey
1. Who creates: RFID Administrator.
2. How they create: Tag/Reader register → New: tag ID or reader ID, site (godown), vehicle map for tags, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker RFID inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Tag/reader history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- Tag management
- Reader registration
- Tag–vehicle mapping

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| RFID register | Medium |
| Tag/reader form | Complex |
| RFID history | Medium |
| RFID checker inbox | Medium |
| RFID approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create tag/reader | Medium |
| Map tag to vehicle | Complex |
| Search RFID | Medium |
| Submit RFID | Complex |
| Approve RFID | Complex |

### Inputs
Tag ID, reader ID, godown, vehicle, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Reader hardware supply may be SI infra; software mapping is this feature.

### Validations
- Tag ID unique.
- Godown mandatory.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
RFID master export.

### Notifications
Checker/maker.

### Security
Warehouse Posts.

### Integrations
Reader events.

### Dependencies
F02-002, F03-001.

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
| RFID register | UI | Medium | 6 |
| Tag/reader form | UI | Complex | 12 |
| RFID history | UI | Medium | 6 |
| RFID checker inbox | UI | Medium | 6 |
| RFID approval | UI | Easy | 4 |
| Create tag/reader | API | Medium | 6 |
| Map tag to vehicle | API | Complex | 8 |
| Search RFID | API | Medium | 6 |
| Submit RFID | API | Complex | 8 |
| Approve RFID | API | Complex | 8 |
| RFID tag/reader and mapping | DB | Complex | 6 |
| RFID reader event channel | Integration | Complex | 24 |
| RFID Tag and Reader Master feature tests | Testing | Very High | 12 |
| RFID Tag and Reader Master implementation documentation | Documentation | Medium | 3 |

**Feature total: 115 hours**
