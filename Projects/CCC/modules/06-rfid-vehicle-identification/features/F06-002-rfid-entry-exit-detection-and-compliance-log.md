# F06-002 — RFID Entry Exit Detection and Compliance Log

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | RFID Entry Exit Detection and Compliance Log |
| **Module** | 06 — RFID Vehicle Identification |

### Description
System logs vehicle entry/exit via RFID, flags unauthorized vehicles, and supports cross-verification with ANPR.

### Business Objective
RFID-based compliance at warehouse gates.

### Actors
User: Godown Operator / CCC Operator. System posts events. Supervisor reviews exceptions.

### User Journey
1. Who creates: System on RFID read; Operator may raise exception note.
2. How they create: Events appear on RFID transaction monitor; Operator opens event, adds remark if needed.
3. How they edit: Remarks only; raw reads not silently deleted.
4. How they send for approval: Unauthorized event may escalate to Supervisor (Module 09 incident).
5. How the approver sees pending items: Supervisor exception inbox / incident queue.
6. How the approver decides: Confirm authorized exception or raise incident.
7. How the user sees history: RFID transaction log for own godown.
8. How the approver sees history: District/state RFID compliance log.

### Functional Capabilities
- Entry/exit detection
- Unauthorized detection
- Transaction log
- ANPR cross-check hook

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| RFID transaction monitor | Complex |
| Unauthorized vehicle alert panel | Complex |
| RFID compliance log | Medium |
| Exception remark form | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Ingest RFID read | Very High |
| Match tag to vehicle | Complex |
| Flag unauthorized | Complex |
| Query RFID log | Medium |
| Request ANPR cross-check | Complex |

### Inputs
Tag, vehicle, site, timestamp, match status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Cross-verification with ANPR when both present.

### Validations
- Reader must be registered.

### Calculations
None.

### Workflow
Auto log; exceptions to Module 09.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
RFID compliance reports (Module 11).

### Notifications
Unauthorized → Module 09.

### Security
Site-scoped.

### Integrations
ANPR Module 07.

### Dependencies
F06-001, Module 07.

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
| RFID transaction monitor | UI | Complex | 12 |
| Unauthorized vehicle alert panel | UI | Complex | 12 |
| RFID compliance log | UI | Medium | 6 |
| Exception remark form | UI | Easy | 4 |
| Ingest RFID read | API | Very High | 16 |
| Match tag to vehicle | API | Complex | 8 |
| Flag unauthorized | API | Complex | 8 |
| Query RFID log | API | Medium | 6 |
| Request ANPR cross-check | API | Complex | 8 |
| RFID transaction log | DB | Complex | 6 |
| RFID Entry Exit Detection and Compliance Log feature tests | Testing | Very High | 12 |
| RFID Entry Exit Detection and Compliance Log implementation documentation | Documentation | Medium | 3 |

**Feature total: 101 hours**
