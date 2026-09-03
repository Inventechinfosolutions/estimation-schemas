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
1. Who creates: Legal Cell
2. How they create: User files a key judgement with title, date, author/court and keywords.
3. How they edit: Another user searches and opens it.
4. How they send for approval: Another user searches and opens it. File → keyword → search/open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Judgement Register
- Judgement Filing form
- Search and open
- Not a substitute for the orders library (F03-003) — key judgements as knowledge
- No AI case summaries

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Judgement Register | Medium |
| Judgement Filing form | Complex |
| Key judgement database history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Judgement CRUD and search | Medium |
| Update key judgement database | Medium |
| Search key judgement database | Medium |
| Read key judgement database history | Easy |

### Inputs
Judgement file; title; date; author/court; keywords.

### Outputs
Judgement record; search hits.

### Business Rules
- Key judgement database as Annexure-I §7.
- Originals unchanged on view.
- Distinct from live matter orders in F03-003 though a judgement may also be linked.

### Validations
- Title and date required; file required; keywords optional but recommended.

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
- SPLOCA designates which judgements are ‘key’.

### Risks
Duplication with F03-003 orders without a link.

### Non Functional Requirements
Search and open.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Judgement Register | UI | Medium | 6 |
| Judgement Filing form | UI | Complex | 12 |
| Key judgement database history | UI | Medium | 6 |
| Judgement CRUD and search | API | Medium | 6 |
| Update key judgement database | API | Medium | 6 |
| Search key judgement database | API | Medium | 6 |
| Read key judgement database history | API | Easy | 4 |
| Key judgement database persistence | DB | Medium | 4 |
| Keyword consume | Integration | Simple | 4 |
| Key judgement database feature tests | Testing | Easy | 4 |
| Key judgement database implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
