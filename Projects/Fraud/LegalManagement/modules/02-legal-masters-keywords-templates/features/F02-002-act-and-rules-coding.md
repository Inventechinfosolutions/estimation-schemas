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
1. Who creates: Administrator
2. How they create: User opens the Act/Rules Coding Workspace and selects or adds an Act or Rule.
3. How they edit: Codes sections (and sub-sections as used) and saves.
4. How they send for approval: Select Act/Rule → code sections → preview hyperlink targets → publish for library use.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Act/Rules Coding Workspace
- Section Tree / Hyperlink Preview
- Map section codes used in library documents
- Follow-from-library to the coded section without altering the stored original Act text
- No generative-AI section summarisation

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Act/Rules Coding Workspace | Complex |
| Section Tree / Hyperlink Preview | Medium |
| Act and rules coding change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Act/section coding operations | Complex |
| Update act and rules coding | Medium |
| Search act and rules coding register | Medium |
| Read act and rules coding change history | Easy |

### Inputs
Act/Rule title, citation, section/sub-section codes, status.

### Outputs
Coded Act/Rule; section tree; hyperlink targets for the library.

### Business Rules
- Original Act/Rule text in the library is not rewritten by coding.
- Hyperlinks use current catalogue codes; broken links are repaired in F02-006.
- Coding is human-maintained; no unsupervised AI extraction of sections.

### Validations
- Act/Rule required; section codes unique within the instrument; empty section trees cannot be published for hyperlink.

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
- SPLOCA supplies the Act/Rule texts to load; this feature is coding, not legislative drafting.

### Risks
Incorrect section codes send users to the wrong passage.

### Non Functional Requirements
Hyperlink resolve must land on the coded section; originals unchanged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Act/Rules Coding Workspace | UI | Complex | 12 |
| Section Tree / Hyperlink Preview | UI | Medium | 6 |
| Act and rules coding change history | UI | Medium | 6 |
| Act/section coding operations | API | Complex | 8 |
| Update act and rules coding | API | Medium | 6 |
| Search act and rules coding register | API | Medium | 6 |
| Read act and rules coding change history | API | Easy | 4 |
| Act and rules coding identity persistence | DB | Medium | 4 |
| Library hyperlink consume | Integration | Simple | 4 |
| Act and Rules coding feature tests | Testing | Medium | 6 |
| Act and Rules coding implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
