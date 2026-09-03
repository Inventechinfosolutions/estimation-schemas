# F08-004 — OM, GO and guard-file database

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-004 |
| **Feature Name** | OM, GO and guard-file database |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
The user files an OM, GO or guard-file item with docket title, date and author. Another user locates it by title or word search.

### Business Objective
File OM, GO and guard-file items with docket title, date and author, locatable by title or word search.

### Actors
Knowledge owner; Legal Cell.

### User Journey
1. Who creates: Knowledge owner
2. How they create: User files an OM, GO or guard-file item with docket title, date and author.
3. How they edit: Another user locates it by title or word search.
4. How they send for approval: Another user locates it by title or word search. File docket → save → title/word search → open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Knowledge owner works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Knowledge owner opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- OM/GO/Guard-File Register
- Docket Filing form
- Title and word search
- Open item

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| OM/GO/Guard-File Register | Medium |
| Docket Filing form | Medium |
| Om, go and guard-file database history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Docket CRUD and word search | Medium |
| Update om, go and guard-file database | Medium |
| Search om, go and guard-file database | Medium |
| Read om, go and guard-file database history | Easy |

### Inputs
Type (OM/GO/guard file); docket title; date; author; file.

### Outputs
Docket record; search hits.

### Business Rules
- OM, GO and Guard File database as Annexure-I.
- SOP/OM/GO can be found by title or keyword (programme acceptance).
- Not Claim settlement GOs unless filed here as knowledge.

### Validations
- Type, title, date, author required as specified; file required.

### Calculations
None.

### Workflow
File docket → save → title/word search → open.

### Search Requirements
Title, word, author, date, type.

### Documents
OM, GO, guard-file items.

### Reports
OM/GO inventory.

### Notifications
None required.

### Security
Guard file may be more restricted than ordinary OM.

### Integrations
Internal (Simple).

### Dependencies
F08-001; F01-003.

### Assumptions
- Word search is knowledge-base text search, not F03-006 Boolean unless the same engine is reused internally.

### Risks
Guard-file over-exposure.

### Non Functional Requirements
Title or word locate.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| OM/GO/Guard-File Register | UI | Medium | 6 |
| Docket Filing form | UI | Medium | 6 |
| Om, go and guard-file database history | UI | Medium | 6 |
| Docket CRUD and word search | API | Medium | 6 |
| Update om, go and guard-file database | API | Medium | 6 |
| Search om, go and guard-file database | API | Medium | 6 |
| Read om, go and guard-file database history | API | Easy | 4 |
| Om, go and guard-file database persistence | DB | Medium | 4 |
| Internal knowledge retrieve | Integration | Simple | 4 |
| OM, GO and guard-file database feature tests | Testing | Easy | 4 |
| OM, GO and guard-file database implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **54** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
