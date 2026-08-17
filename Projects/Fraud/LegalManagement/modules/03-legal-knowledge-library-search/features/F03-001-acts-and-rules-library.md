# F03-001 — Acts and Rules library

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Acts and Rules library |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
A Legal Cell user uploads or records an Act/Rule, applies coded keywords, and saves. Another user searches or follows a hyperlink and opens that Act/Rule without altering the stored original.

### Business Objective
Hold coded Acts and Rules as library originals that remain unchanged when users search or follow hyperlinks.

### Actors
Legal Cell; Advocate (read/search).

### User Journey
1. Legal Cell opens the Acts and Rules Library Register.
2. Uploads or records an Act/Rule, applies coded keywords (F02-001/F02-002), and saves.
3. Another user searches or follows a hyperlink and opens the Act/Rule.
4. The stored original is not altered by viewing, highlighting or hyperlink follow.

### Functional Capabilities
- Acts and Rules Library Register
- Act/Rule Upload and Keyword Coding form
- Open original without write-back
- Hyperlink landing from coded sections
- No public-website search; no generative-AI digest of the Act

### Inputs
Act/Rule file or record, title, coded keywords, Act & section codes.

### Outputs
Library Act/Rule record; unchanged original; keyword links.

### Business Rules
- Originals remain unchanged; highlights/hyperlinks are in results, not burned into the stored file.
- Keywords come from the legal catalogues, not free-text-only coding.
- Not a standalone search product (search is F03-005/F03-006).

### Validations
Title required; file or recorded text required; keywords must exist in catalogues when applied.

### Calculations
None.

### Workflow
Upload/record → apply codes → save original → retrieve via search or hyperlink.

### Search Requirements
Title, Act, section, keyword (full NL/Boolean in F03-005/F03-006).

### Documents
Act/Rule originals.

### Reports
Acts/Rules inventory.

### Notifications
None required.

### Security
View/download per F01-003; originals not overwritten by viewers.

### Integrations
Keyword catalogue consume (Simple).

### Dependencies
F02-001; F02-002; F01-003; F03-005–F03-007.

### Assumptions
Authority supplies Act/Rule texts for load; migration of existing files is a data load, not scanning bureau.

### Risks
Overwrite of originals if viewer save is allowed — must be prevented.

### Non Functional Requirements
Original byte-stable; HTTPS retrieval.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Acts and Rules Library Register | UI | Medium | 6 |
| Act/Rule Upload and Keyword Coding form | UI | Complex | 12 |
| Library Act/Rule CRUD operations | API | Medium | 6 |
| Act/Rule document entities | Database | Medium | 4 |
| Keyword catalogue consume | Integration | Simple | 4 |
| Acts/Rules library tests | Testing | Medium | 6 |
| Acts and Rules library guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- NL and Boolean search hours are F03-005 and F03-006.
