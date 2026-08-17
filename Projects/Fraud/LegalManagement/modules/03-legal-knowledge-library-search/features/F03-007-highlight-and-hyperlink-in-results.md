# F03-007 — Highlight and hyperlink in results

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-007 |
| **Feature Name** | Highlight and hyperlink in results |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
In the result list the user sees matched keywords highlighted and hyperlinked to the document address, then clicks through to the passage.

### Business Objective
Make search hits actionable: highlighted matched keywords with hyperlinks that open the document at the relevant address/passage.

### Actors
Legal Cell; Advocate.

### User Journey
1. User runs NL or Boolean search (F03-005 / F03-006).
2. In the result list, matched keywords are highlighted and hyperlinked to the document address.
3. User clicks through to the passage.
4. The stored original is not permanently marked up.

### Functional Capabilities
- Highlighted Result List
- Passage Jump Viewer
- Matched keywords highlighted in hits
- Hyperlink to document address / passage
- Originals unchanged

### Inputs
Hit identifiers; match offsets; document address from keyword links (F02-006).

### Outputs
Highlighted hit rows; passage view; click-through to document.

### Business Rules
- Keywords in results shall be highlighted and hyperlinked with document address.
- Highlights are presentation on results/viewer, not a new stored original.
- Click-through still enforces F01-003.

### Validations
Missing document address shows the hit without a dead link; offsets out of range open the document start.

### Calculations
None.

### Workflow
Search hits → highlight/hyperlink → click → passage.

### Search Requirements
N/A (presentation of other features’ hits).

### Documents
Same library documents.

### Reports
None.

### Notifications
None.

### Security
Snippets must not reveal content the Person cannot view.

### Integrations
Document address resolve (Simple).

### Dependencies
F03-005; F03-006; F02-006; F01-003.

### Assumptions
Passage offsets are stored or computed from the index used by F03-005/F03-006.

### Risks
Dead hyperlinks if F02-006 repair is skipped.

### Non Functional Requirements
Click-through lands near the matched passage.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Highlighted Result List | UI | Complex | 12 |
| Passage Jump Viewer | UI | Medium | 6 |
| Highlight and hyperlink resolve | API | Medium | 6 |
| Passage offset store | Database | Easy | 2 |
| Document address resolve | Integration | Simple | 4 |
| Highlight/hyperlink tests | Testing | Medium | 6 |
| Results highlight and hyperlink guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Does not re-estimate the search engines in F03-005/F03-006.
