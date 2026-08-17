# F05-007 — Team messages saved and searchable per matter

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-007 |
| **Feature Name** | Team messages saved and searchable per matter |
| **Module** | 05 — Tasks, Collaboration & Communication |

### Description
The user sends a sidebar or matter message. The system saves it against the matter. Another user searches communications by Person, Date, Case or Key Word and opens the brief.

### Business Objective
Keep team sidebar/matter messages as a searchable record per matter (Person, Date, Case, Key Word).

### Actors
Legal Cell; Advocate; authorised team members.

### User Journey
1. User sends a sidebar or matter message.
2. System saves it against the matter.
3. Another user searches communications by Person, Date, Case or Key Word and opens the brief.

### Functional Capabilities
- Matter Sidebar Messages
- Communication Search (Person, Date, Case, Key Word)
- Save every message against the matter
- Open the brief from search
- Not a consumer chat product

### Inputs
Message text; matter; optional keyword; sender Person.

### Outputs
Saved message; search hits; brief view.

### Business Rules
- Communication on a matter is searchable by person, date, case and keyword.
- Messages are official records, not ephemeral.
- Need-to-know still applies.

### Validations
Matter required; empty message rejected; search scoped to matters the user can open.

### Calculations
None.

### Workflow
Send → save on matter → search → open brief.

### Search Requirements
Person, Date, Case, Key Word.

### Documents
Optional file attached to a message (also F05-008 for broader file share).

### Reports
Communication extract per matter (authorised).

### Notifications
Optional in-app new-message notice.

### Security
No leak of Limited messages into Community search.

### Integrations
Matter linkage (Simple).

### Dependencies
F04-001; F01-002; F05-008 for email sync.

### Assumptions
Email bodies synced in F05-008 are also searchable once stored against the matter.

### Risks
Sidebar used for sensitive advice without Limited space.

### Non Functional Requirements
Search over typical matter message volume.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Matter Sidebar Messages | UI | Complex | 12 |
| Communication Search (Person, Date, Case, Key Word) | UI | Complex | 12 |
| Message save and search operations | API | Complex | 8 |
| Message store | Database | Medium | 4 |
| Matter linkage | Integration | Simple | 4 |
| Matter message tests | Testing | Medium | 6 |
| Matter messages search guide | Documentation | Easy | 2 |
| **Total** | | | **48** |

### Estimation Assumptions
- Email mailbox sync is F05-008.
