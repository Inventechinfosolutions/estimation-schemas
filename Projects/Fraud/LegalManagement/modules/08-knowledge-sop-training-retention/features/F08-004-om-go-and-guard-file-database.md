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
1. User files an OM, GO or guard-file item with docket title, date and author.
2. Another user locates it by title or word search.

### Functional Capabilities
- OM/GO/Guard-File Register
- Docket Filing form
- Title and word search
- Open item

### Inputs
Type (OM/GO/guard file); docket title; date; author; file.

### Outputs
Docket record; search hits.

### Business Rules
- OM, GO and Guard File database as Annexure-I.
- SOP/OM/GO can be found by title or keyword (programme acceptance).
- Not Claim settlement GOs unless filed here as knowledge.

### Validations
Type, title, date, author required as specified; file required.

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
Word search is knowledge-base text search, not F03-006 Boolean unless the same engine is reused internally.

### Risks
Guard-file over-exposure.

### Non Functional Requirements
Title or word locate.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| OM/GO/Guard-File Register | UI | Medium | 6 |
| Docket Filing form | UI | Medium | 6 |
| Docket CRUD and word search | API | Medium | 6 |
| Docket entities | Database | Medium | 4 |
| Internal knowledge retrieve | Integration | Simple | 4 |
| OM/GO tests | Testing | Easy | 4 |
| OM, GO and guard-file guide | Documentation | Easy | 2 |
| **Total** | | | **32** |

### Estimation Assumptions
- Library Boolean engine hours stay in F03-006.
