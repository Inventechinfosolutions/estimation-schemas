# F05-009 — Operational unit and Legal Cell coordination

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-009 |
| **Feature Name** | Operational unit and Legal Cell coordination |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
An authorised operational-unit user and a Legal Cell user join an authorised group meeting or share documents / audio-visual as permitted. Unauthorised users cannot join. Need-to-know still applies.

### Business Objective
Enable authorised real-time coordination between operational units and Legal Cell (group meetings, document and AV share) without opening a public room.

### Actors
Authorised operational-unit user; Legal Cell; Advocate where permitted.

### User Journey
1. Authorised operational-unit user and Legal Cell user join an authorised group meeting or share documents / AV as permitted.
2. Unauthorised users cannot join.
3. Need-to-know still applies to AV and documents.

### Functional Capabilities
- Authorised Group Meeting room
- AV / Document Share controls
- Join only if authorised
- Need-to-know on AV and files
- Not a public collaboration portal; not investigation war-rooms

### Inputs
Meeting identity; authorised participant Posts; document/AV share flags.

### Outputs
Meeting session record; share log; join refusals.

### Business Rules
- Unauthorised users cannot join.
- Need-to-know still applies to AV/group meetings.
- Operational-unit users are shared-identity Persons with permitted Posts — not a second directory.
- Market intelligence / investigation process remains out of scope.

### Validations
Both sides must hold authorised Posts; Limited space documents cannot be AV-broadcast to Community.

### Calculations
None.

### Workflow
Create authorised meeting → admit permitted Posts → share docs/AV → record session.

### Search Requirements
Meetings by matter, date, participating unit, Legal Cell Person.

### Documents
Shared during meeting as permitted.

### Reports
Cross-unit meeting log.

### Notifications
Meeting invite to authorised Posts only.

### Security
Join token bound to shared Person; recording policy as SPLOCA sets; no anonymous links.

### Integrations
Need-to-know plus operational-unit identity from shared IAM (Medium).

### Dependencies
F01-001; F01-002; F04-004; F05-006.

### Assumptions
AV tooling is an approved interface, not a consumer Zoom tenant for the public. Policy may tighten Limited/Community rules.

### Risks
AV leak of Limited documents; unauthorised operational staff joining.

### Non Functional Requirements
Join checks on every participant; session audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Authorised Group Meeting room | UI | Complex | 12 |
| AV / Document Share controls | UI | Complex | 12 |
| Meeting join and share operations | API | Complex | 8 |
| Meeting session records | Database | Medium | 4 |
| Need-to-know and operational-unit identity | Integration | Medium | 16 |
| Cross-unit coordination tests | Testing | Complex | 8 |
| Operational unit and Legal Cell coordination guide | Documentation | Medium | 3 |
| **Total** | | | **63** |

### Estimation Assumptions
- Does not include building a full commercial AV platform from scratch; hours cover Legal controls, join rules and integration.
