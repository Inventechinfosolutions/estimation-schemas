# F08-003 — Key judgement database

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Key judgement database |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
The user files a key judgement with title, date, author/court and keywords. Another user searches and opens it.

### Business Objective
Maintain a key judgement database searchable by title, date, court/author and keywords for Legal Cell research.

### Actors
Legal Cell; knowledge owner; Advocate (read).

### User Journey
1. User files a key judgement with title, date, author/court and keywords.
2. Another user searches and opens it.

### Functional Capabilities
- Judgement Register
- Judgement Filing form
- Search and open
- Not a substitute for the orders library (F03-003) — key judgements as knowledge
- No AI case summaries

### Inputs
Judgement file; title; date; author/court; keywords.

### Outputs
Judgement record; search hits.

### Business Rules
- Key judgement database as Annexure-I §7.
- Originals unchanged on view.
- Distinct from live matter orders in F03-003 though a judgement may also be linked.

### Validations
Title and date required; file required; keywords optional but recommended.

### Calculations
None.

### Workflow
File → keyword → search/open.

### Search Requirements
Title, date, court/author, keyword.

### Documents
Key judgements.

### Reports
Judgement inventory.

### Notifications
None required.

### Security
F01-003 on download.

### Integrations
Keyword consume (Simple).

### Dependencies
F02-001; F03-003 related; F01-003.

### Assumptions
SPLOCA designates which judgements are ‘key’.

### Risks
Duplication with F03-003 orders without a link.

### Non Functional Requirements
Search and open.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Judgement Register | UI | Medium | 6 |
| Judgement Filing form | UI | Complex | 12 |
| Judgement CRUD and search | API | Medium | 6 |
| Judgement entities | Database | Medium | 4 |
| Keyword consume | Integration | Simple | 4 |
| Judgement tests | Testing | Easy | 4 |
| Key judgement database guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Special/High Court order filing for matters remains F03-003.
