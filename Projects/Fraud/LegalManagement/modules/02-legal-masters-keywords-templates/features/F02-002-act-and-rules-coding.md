# F02-002 — Act and Rules coding

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Act and Rules coding |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
The user codes an Act or Rule and sections so that a library document can hyperlink those codes. Another user opens the Act in the library and follows the keyword to the coded section.

### Business Objective
Make Acts and Rules navigable by coded section so library hyperlinks resolve to the intended passage.

### Actors
Administrator; Legal Cell; Advocate (follow hyperlink).

### User Journey
1. User opens the Act/Rules Coding Workspace and selects or adds an Act or Rule.
2. Codes sections (and sub-sections as used) and saves.
3. A library document is hyperlinked to those codes (F02-006 / Module 03).
4. Another user opens the Act in the library and follows the keyword to the coded section.

### Functional Capabilities
- Act/Rules Coding Workspace
- Section Tree / Hyperlink Preview
- Map section codes used in library documents
- Follow-from-library to the coded section without altering the stored original Act text
- No generative-AI section summarisation

### Inputs
Act/Rule title, citation, section/sub-section codes, status.

### Outputs
Coded Act/Rule; section tree; hyperlink targets for the library.

### Business Rules
- Original Act/Rule text in the library is not rewritten by coding.
- Hyperlinks use current catalogue codes; broken links are repaired in F02-006.
- Coding is human-maintained; no unsupervised AI extraction of sections.

### Validations
Act/Rule required; section codes unique within the instrument; empty section trees cannot be published for hyperlink.

### Calculations
None.

### Workflow
Select Act/Rule → code sections → preview hyperlink targets → publish for library use.

### Search Requirements
Act/Rule title, citation, section code.

### Documents
Acts and Rules stored in the library (F03-001).

### Reports
Act/section coding register.

### Notifications
None required.

### Security
Coding changes restricted to authorised Posts; library originals remain read-intact.

### Integrations
Library hyperlink consume (Simple).

### Dependencies
F02-001; F03-001; F02-006; F03-007.

### Assumptions
SPLOCA supplies the Act/Rule texts to load; this feature is coding, not legislative drafting.

### Risks
Incorrect section codes send users to the wrong passage.

### Non Functional Requirements
Hyperlink resolve must land on the coded section; originals unchanged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Act/Rules Coding Workspace | UI | Complex | 12 |
| Section Tree / Hyperlink Preview | UI | Medium | 6 |
| Act/section coding operations | API | Complex | 8 |
| Act and section entities | Database | Medium | 4 |
| Library hyperlink consume | Integration | Simple | 4 |
| Act/Rules coding tests | Testing | Medium | 6 |
| Act and Rules coding guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Library upload of Act PDFs/text is F03-001.
- Boolean search is F03-006.
