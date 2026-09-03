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
1. Who creates: Legal Cell
2. How they create: User runs NL or Boolean search (F03-005 / F03-006).
3. How they edit: In the result list, matched keywords are highlighted and hyperlinked to the document address.
4. How they send for approval: User clicks through to the passage. Search hits → highlight/hyperlink → click → passage.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. The stored original is not permanently marked up.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Highlighted Result List
- Passage Jump Viewer
- Matched keywords highlighted in hits
- Hyperlink to document address / passage
- Originals unchanged

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Highlighted Result List | Complex |
| Passage Jump Viewer | Medium |
| Highlight and hyperlink in results history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Highlight and hyperlink resolve | Medium |
| Update highlight and hyperlink in results | Medium |
| Search highlight and hyperlink in results | Medium |
| Read highlight and hyperlink in results history | Easy |

### Inputs
Hit identifiers; match offsets; document address from keyword links (F02-006).

### Outputs
Highlighted hit rows; passage view; click-through to document.

### Business Rules
- Keywords in results shall be highlighted and hyperlinked with document address.
- Highlights are presentation on results/viewer, not a new stored original.
- Click-through still enforces F01-003.

### Validations
- Missing document address shows the hit without a dead link; offsets out of range open the document start.

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
- Passage offsets are stored or computed from the index used by F03-005/F03-006.

### Risks
Dead hyperlinks if F02-006 repair is skipped.

### Non Functional Requirements
Click-through lands near the matched passage.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Highlighted Result List | UI | Complex | 12 |
| Passage Jump Viewer | UI | Medium | 6 |
| Highlight and hyperlink in results history | UI | Medium | 6 |
| Highlight and hyperlink resolve | API | Medium | 6 |
| Update highlight and hyperlink in results | API | Medium | 6 |
| Search highlight and hyperlink in results | API | Medium | 6 |
| Read highlight and hyperlink in results history | API | Easy | 4 |
| Highlight and hyperlink in results persistence | DB | Medium | 4 |
| Document address resolve | Integration | Simple | 4 |
| Highlight and hyperlink in results feature tests | Testing | Medium | 6 |
| Highlight and hyperlink in results implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
