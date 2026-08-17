# F08-001 — Manuals, guidelines and SOP

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Manuals, guidelines and SOP |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
An authorised user uploads a manual, guideline or SOP, applies keywords, and saves. Another user searches by keyword or title and opens the document.

### Business Objective
Provide a searchable SOP/manuals/guidelines library with keywords for Legal Cell daily use.

### Actors
Authorised knowledge owner; Legal Cell; Advocate (read).

### User Journey
1. Authorised user uploads a manual, guideline or SOP, applies keywords, and saves.
2. Another user searches by keyword or title and opens the document.

### Functional Capabilities
- SOP Library Register
- Upload and Keyword form
- Search by keyword or title
- Open document
- Not an LMS vendor product

### Inputs
File; title; keywords; type (manual/guideline/SOP).

### Outputs
Knowledge document; search hits.

### Business Rules
- Keywords hyperlinked as for other knowledge items.
- Classroom/instructor-led training is out of scope unless separately ordered.
- No generative-AI SOP authoring.

### Validations
Title and file required; keywords from catalogues when applied.

### Calculations
None.

### Workflow
Upload → keyword → save → search/open.

### Search Requirements
Keyword, title.

### Documents
Manuals, guidelines, SOP.

### Reports
SOP inventory.

### Notifications
Optional publish notice.

### Security
View per Post; some SOP may be Limited.

### Integrations
Keyword consume (Simple).

### Dependencies
F02-001; F01-003; F08-006 retention.

### Assumptions
SPLOCA supplies SOP files.

### Risks
Out-of-date SOP without version note.

### Non Functional Requirements
Search by title or keyword as acceptance criterion.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| SOP Library Register | UI | Medium | 6 |
| Upload and Keyword form | UI | Complex | 12 |
| SOP CRUD | API | Medium | 6 |
| SOP entities | Database | Medium | 4 |
| Keyword consume | Integration | Simple | 4 |
| SOP tests | Testing | Easy | 4 |
| Manuals, guidelines and SOP guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Court statutory templates remain F02-003.
