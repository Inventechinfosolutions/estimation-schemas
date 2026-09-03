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
1. Who creates: Legal Cell
2. How they create: User opens Petitions / SOB / Written Arguments Register.
3. How they edit: Selects type, applies the same referencing scheme as orders, scans or uploads, and saves.
4. How they send for approval: Team members with rights open the current version from the library or the linked matter. Scan/upload → code → save version → open current from library or matter.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Previous versions remain available; originals are not silently replaced.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Petitions / SOB / Written Arguments Register
- Scan/Upload and Referencing form
- Current version open from library or matter
- Prior versions retrievable
- No generative-AI drafting of SOB or arguments

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Petitions / SOB / Written Arguments Register | Medium |
| Scan/Upload and Referencing form | Complex |
| Petitions, sobs and written arguments history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Filing and version retrieve operations | Complex |
| Update petitions, sobs and written arguments | Medium |
| Search petitions, sobs and written arguments | Medium |
| Read petitions, sobs and written arguments history | Easy |

### Inputs
Document type (Petition/SOB/Written arguments); scan/upload; referencing fields as for orders; matter link where used.

### Outputs
Filed document; current version pointer; version history.

### Business Rules
- All Petitions, SOBs and Written Arguments use the same referencing and coding scheme as orders.
- Team members open only with F01-003 rights and space membership.
- Template-generated drafts (F02-004) may be filed here after human verify; AI compose is forbidden.

### Validations
- Type required; file required; referencing as applicable; version number monotonic.

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
- Scanning bureau is out of scope unless separately ordered; user uploads/scans at desk.

### Risks
Filing a new scan as overwrite without versioning loses the court-filed copy.

### Non Functional Requirements
Version retrieve; originals retained.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Petitions / SOB / Written Arguments Register | UI | Medium | 6 |
| Scan/Upload and Referencing form | UI | Complex | 12 |
| Petitions, sobs and written arguments history | UI | Medium | 6 |
| Filing and version retrieve operations | API | Complex | 8 |
| Update petitions, sobs and written arguments | API | Medium | 6 |
| Search petitions, sobs and written arguments | API | Medium | 6 |
| Read petitions, sobs and written arguments history | API | Easy | 4 |
| Petitions, sobs and written arguments persistence | DB | Medium | 4 |
| Matter/library share handoff | Integration | Simple | 4 |
| Petitions, SOBs and written arguments feature tests | Testing | Medium | 6 |
| Petitions, SOBs and written arguments implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
