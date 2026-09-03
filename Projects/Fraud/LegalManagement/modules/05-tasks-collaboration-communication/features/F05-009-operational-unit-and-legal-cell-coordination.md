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
1. Who creates: Authorised operational-unit user
2. How they create: Authorised operational-unit user and Legal Cell user join an authorised group meeting or share documents / AV as permitted.
3. How they edit: Unauthorised users cannot join.
4. How they send for approval: Need-to-know still applies to AV and documents. Create authorised meeting → admit permitted Posts → share docs/AV → record session.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Authorised operational-unit user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Authorised operational-unit user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Authorised Group Meeting room
- AV / Document Share controls
- Join only if authorised
- Need-to-know on AV and files
- Not a public collaboration portal; not investigation war-rooms

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Authorised Group Meeting room | Complex |
| AV / Document Share controls | Complex |
| Operational unit and legal cell coordination history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Meeting join and share operations | Complex |
| Update operational unit and legal cell coordination | Medium |
| Search operational unit and legal cell coordination | Medium |
| Read operational unit and legal cell coordination history | Easy |

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
- Both sides must hold authorised Posts; Limited space documents cannot be AV-broadcast to Community.

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
- AV tooling is an approved interface, not a consumer Zoom tenant for the public. Policy may tighten Limited/Community rules.

### Risks
AV leak of Limited documents; unauthorised operational staff joining.

### Non Functional Requirements
Join checks on every participant; session audit.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Authorised Group Meeting room | UI | Complex | 12 |
| AV / Document Share controls | UI | Complex | 12 |
| Operational unit and legal cell coordination history | UI | Medium | 6 |
| Meeting join and share operations | API | Complex | 8 |
| Update operational unit and legal cell coordination | API | Medium | 6 |
| Search operational unit and legal cell coordination | API | Medium | 6 |
| Read operational unit and legal cell coordination history | API | Easy | 4 |
| Operational unit and legal cell coordination persistence | DB | Medium | 4 |
| Need-to-know and operational-unit identity | Integration | Medium | 16 |
| Operational unit and Legal Cell coordination feature tests | Testing | Complex | 8 |
| Operational unit and Legal Cell coordination implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **85** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
