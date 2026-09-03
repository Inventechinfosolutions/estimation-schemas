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
1. Who creates: Legal Cell
2. How they create: User sends a sidebar or matter message.
3. How they edit: System saves it against the matter.
4. How they send for approval: Another user searches communications by Person, Date, Case or Key Word and opens the brief. Send → save on matter → search → open brief.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Matter Sidebar Messages
- Communication Search (Person, Date, Case, Key Word)
- Save every message against the matter
- Open the brief from search
- Not a consumer chat product

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Matter Sidebar Messages | Complex |
| Communication Search (Person, Date, Case, Key Word) | Complex |
| Team messages saved and searchable per matter history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Message save and search operations | Complex |
| Update team messages saved and searchable per matter | Medium |
| Search team messages saved and searchable per matter | Medium |
| Read team messages saved and searchable per matter history | Easy |

### Inputs
Message text; matter; optional keyword; sender Person.

### Outputs
Saved message; search hits; brief view.

### Business Rules
- Communication on a matter is searchable by person, date, case and keyword.
- Messages are official records, not ephemeral.
- Need-to-know still applies.

### Validations
- Matter required; empty message rejected; search scoped to matters the user can open.

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
- Email bodies synced in F05-008 are also searchable once stored against the matter.

### Risks
Sidebar used for sensitive advice without Limited space.

### Non Functional Requirements
Search over typical matter message volume.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Matter Sidebar Messages | UI | Complex | 12 |
| Communication Search (Person, Date, Case, Key Word) | UI | Complex | 12 |
| Team messages saved and searchable per matter history | UI | Medium | 6 |
| Message save and search operations | API | Complex | 8 |
| Update team messages saved and searchable per matter | API | Medium | 6 |
| Search team messages saved and searchable per matter | API | Medium | 6 |
| Read team messages saved and searchable per matter history | API | Easy | 4 |
| Team messages saved and searchable per matter persistence | DB | Medium | 4 |
| Matter linkage | Integration | Simple | 4 |
| Team messages saved and searchable per matter feature tests | Testing | Medium | 6 |
| Team messages saved and searchable per matter implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **70** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
