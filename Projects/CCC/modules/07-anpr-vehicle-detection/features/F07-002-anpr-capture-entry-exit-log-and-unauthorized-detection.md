# F07-002 — ANPR Capture, Entry Exit Log and Unauthorized Detection

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | ANPR Capture, Entry Exit Log and Unauthorized Detection |
| **Module** | 07 — ANPR Vehicle Detection |

### Description
System captures plates, logs entry/exit with timestamps, detects unauthorized vehicles, and integrates with RFID validation.

### Business Objective
Automated vehicle detection at gates.

### Actors
User: Godown/CCC Operator. System posts captures. Supervisor handles unauthorized.

### User Journey
1. Who creates: System on plate capture.
2. How they create: Events on ANPR monitor; Operator reviews mismatch.
3. How they edit: Remarks only.
4. How they send for approval: Unauthorized → escalate (Module 09).
5. How the approver sees pending items: Exception/incident inbox.
6. How the approver decides: Confirm or raise incident.
7. How the user sees history: ANPR transaction log.
8. How the approver sees history: District/state ANPR log.

### Functional Capabilities
- Plate capture
- Entry/exit log
- Unauthorized detection
- RFID cross-check

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| ANPR transaction monitor | Complex |
| ANPR unauthorized panel | Complex |
| ANPR analytics view | Complex |
| ANPR log search | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Ingest ANPR capture | Very High |
| Match plate to vehicle master | Complex |
| Flag unauthorized | Complex |
| Query ANPR log | Medium |
| Cross-check RFID | Complex |

### Inputs
Plate, site, timestamp, match status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Integrate with RFID when both present.

### Validations
- Camera must be approved.

### Calculations
Movement analytics counts.

### Workflow
Auto; exceptions to Module 09.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Optional plate image (embedded).

### Reports
ANPR reports (Module 11).

### Notifications
Unauthorized → Module 09.

### Security
Site-scoped.

### Integrations
RFID Module 06.

### Dependencies
F07-001, F03-001.

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
| ANPR transaction monitor | UI | Complex | 12 |
| ANPR unauthorized panel | UI | Complex | 12 |
| ANPR analytics view | UI | Complex | 12 |
| ANPR log search | UI | Medium | 6 |
| Ingest ANPR capture | API | Very High | 16 |
| Match plate to vehicle master | API | Complex | 8 |
| Flag unauthorized | API | Complex | 8 |
| Query ANPR log | API | Medium | 6 |
| Cross-check RFID | API | Complex | 8 |
| ANPR transaction log | DB | Complex | 6 |
| ANPR Capture, Entry Exit Log and Unauthorized Detection feature tests | Testing | Very High | 12 |
| ANPR Capture, Entry Exit Log and Unauthorized Detection implementation documentation | Documentation | Medium | 3 |

**Feature total: 109 hours**
