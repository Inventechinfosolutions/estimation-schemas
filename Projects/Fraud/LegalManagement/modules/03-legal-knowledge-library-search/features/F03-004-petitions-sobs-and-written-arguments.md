# F03-004 — Petitions, SOBs and written arguments

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-004 |
| **Feature Name** | Petitions, SOBs and written arguments |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
The user files a petition, SOB or written argument with the same referencing scheme as orders, scans/uploads the document, and saves. Team members with rights open the current version from the library or the matter.

### Business Objective
Keep petitions, SOBs and written arguments in the coded library with the same referencing scheme as orders, version-aware for the team.

### Actors
Legal Cell; Advocate; team members with rights.

### User Journey
1. User opens Petitions / SOB / Written Arguments Register.
2. Selects type, applies the same referencing scheme as orders, scans or uploads, and saves.
3. Team members with rights open the current version from the library or the linked matter.
4. Previous versions remain available; originals are not silently replaced.

### Functional Capabilities
- Petitions / SOB / Written Arguments Register
- Scan/Upload and Referencing form
- Current version open from library or matter
- Prior versions retrievable
- No generative-AI drafting of SOB or arguments

### Inputs
Document type (Petition/SOB/Written arguments); scan/upload; referencing fields as for orders; matter link where used.

### Outputs
Filed document; current version pointer; version history.

### Business Rules
- All Petitions, SOBs and Written Arguments use the same referencing and coding scheme as orders.
- Team members open only with F01-003 rights and space membership.
- Template-generated drafts (F02-004) may be filed here after human verify; AI compose is forbidden.

### Validations
Type required; file required; referencing as applicable; version number monotonic.

### Calculations
None.

### Workflow
Scan/upload → code → save version → open current from library or matter.

### Search Requirements
Type, case number, FE, CA, matter, version, date.

### Documents
Petition, SOB, written argument files.

### Reports
Petition/SOB/argument filing register.

### Notifications
Optional notice to matter team when a new version is saved.

### Security
Controlled share; download per rights matrix.

### Integrations
Matter/library share (Simple).

### Dependencies
F03-003 scheme; F04-004; F01-003; F02-004 optional source.

### Assumptions
Scanning bureau is out of scope unless separately ordered; user uploads/scans at desk.

### Risks
Filing a new scan as overwrite without versioning loses the court-filed copy.

### Non Functional Requirements
Version retrieve; originals retained.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Petitions / SOB / Written Arguments Register | UI | Medium | 6 |
| Scan/Upload and Referencing form | UI | Complex | 12 |
| Filing and version retrieve operations | API | Complex | 8 |
| Petition/SOB/argument document entities | Database | Medium | 4 |
| Matter/library share handoff | Integration | Simple | 4 |
| Petition/SOB filing tests | Testing | Medium | 6 |
| Petitions, SOB and written arguments guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Matter-controlled share UI is primarily F04-004.
