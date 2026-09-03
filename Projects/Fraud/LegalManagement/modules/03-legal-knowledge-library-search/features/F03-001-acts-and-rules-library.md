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
1. Who creates: Legal Cell
2. How they create: Legal Cell opens the Acts and Rules Library Register.
3. How they edit: Uploads or records an Act/Rule, applies coded keywords (F02-001/F02-002), and saves.
4. How they send for approval: Another user searches or follows a hyperlink and opens the Act/Rule. Upload/record → apply codes → save original → retrieve via search or hyperlink.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. The stored original is not altered by viewing, highlighting or hyperlink follow.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Acts and Rules Library Register
- Act/Rule Upload and Keyword Coding form
- Open original without write-back
- Hyperlink landing from coded sections
- No public-website search; no generative-AI digest of the Act

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Acts and Rules Library Register | Medium |
| Act/Rule Upload and Keyword Coding form | Complex |
| Acts and rules library history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Library Act/Rule CRUD operations | Medium |
| Update acts and rules library | Medium |
| Search acts and rules library | Medium |
| Read acts and rules library history | Easy |

### Inputs
Act/Rule file or record, title, coded keywords, Act & section codes.

### Outputs
Library Act/Rule record; unchanged original; keyword links.

### Business Rules
- Originals remain unchanged; highlights/hyperlinks are in results, not burned into the stored file.
- Keywords come from the legal catalogues, not free-text-only coding.
- Not a standalone search product (search is F03-005/F03-006).

### Validations
- Title required; file or recorded text required; keywords must exist in catalogues when applied.

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
- Authority supplies Act/Rule texts for load; migration of existing files is a data load, not scanning bureau.

### Risks
Overwrite of originals if viewer save is allowed — must be prevented.

### Non Functional Requirements
Original byte-stable; HTTPS retrieval.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Acts and Rules Library Register | UI | Medium | 6 |
| Act/Rule Upload and Keyword Coding form | UI | Complex | 12 |
| Acts and rules library history | UI | Medium | 6 |
| Library Act/Rule CRUD operations | API | Medium | 6 |
| Update acts and rules library | API | Medium | 6 |
| Search acts and rules library | API | Medium | 6 |
| Read acts and rules library history | API | Easy | 4 |
| Acts and rules library persistence | DB | Medium | 4 |
| Keyword catalogue consume | Integration | Simple | 4 |
| Acts and Rules library feature tests | Testing | Medium | 6 |
| Acts and Rules library implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
