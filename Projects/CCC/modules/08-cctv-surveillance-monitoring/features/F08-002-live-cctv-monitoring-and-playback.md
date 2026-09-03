# F08-002 — Live CCTV Monitoring and Playback

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Live CCTV Monitoring and Playback |
| **Module** | 08 — CCTV Surveillance Monitoring |

### Description
Operators view live feeds, entry/exit and loading/unloading monitoring, incident-linked playback. Video wall hardware is out of software hours.

### Business Objective
Centralized live video monitoring of warehouse operations.

### Actors
User: CCC Operator / Vigilance Officer. Auditor: playback audit.

### User Journey
1. Who creates: Operator opens live wall layout in software.
2. How they create: Selects godown/cameras, starts live view; opens playback by time/incident.
3. How they edit: Layout/filters only.
4. How they send for approval: Not applicable for view; incident raise goes to Module 09.
5. How the approver sees pending items: No view inbox.
6. How the approver decides: Not applicable.
7. How the user sees history: Recent layouts and playback requests.
8. How the auditor sees history: Playback access log.

### Functional Capabilities
- Live multi-camera view
- Playback
- Incident-linked view
- Event monitoring

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Live CCTV monitoring workspace | Very High |
| Playback viewer | Very High |
| CCTV event monitor | Complex |
| Playback access log | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Start live stream session | Very High |
| Request playback | Very High |
| List camera events | Complex |
| Link view to incident | Medium |

### Inputs
Godown, camera set, time range, incident link.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Video wall controllers/hardware excluded from hours.

### Validations
- Approved cameras only.

### Calculations
None.

### Workflow
No approval for view.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
CCTV activity logs (Module 11).

### Notifications
Via Module 09.

### Security
Need-to-know; playback audited.

### Integrations
Uses F08-001 streams.

### Dependencies
F08-001.

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
| Live CCTV monitoring workspace | UI | Very High | 16 |
| Playback viewer | UI | Very High | 16 |
| CCTV event monitor | UI | Complex | 12 |
| Playback access log | UI | Medium | 6 |
| Start live stream session | API | Very High | 16 |
| Request playback | API | Very High | 16 |
| List camera events | API | Complex | 8 |
| Link view to incident | API | Medium | 6 |
| View session and playback access log | DB | Medium | 4 |
| Live CCTV Monitoring and Playback feature tests | Testing | Very High | 12 |
| Live CCTV Monitoring and Playback implementation documentation | Documentation | Complex | 4 |

**Feature total: 116 hours**
