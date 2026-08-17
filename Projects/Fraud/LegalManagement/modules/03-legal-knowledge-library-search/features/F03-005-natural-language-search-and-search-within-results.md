# F03-005 — Natural-language search and search-within-results

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Natural-language search and search-within-results |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
The user types a plain-language query (for example an elements-style question) in the search box, reviews hits, then enters further keywords to Search Within Results. Hits show highlighted terms and a link to the document.

### Business Objective
Let Legal Cell retrieve library material with plain-language queries and then narrow the current hit list without starting over.

### Actors
Legal Cell; Advocate.

### User Journey
1. User opens Library Search and types a plain-language query (for example an elements-style question).
2. Reviews the hit list with highlighted terms and a link to each document.
3. Enters further keywords and chooses Search Within Results.
4. The hit list narrows to the current set; originals remain unchanged.

### Functional Capabilities
- Library Search Box and Hit List
- Search Within Results panel
- Plain-language (elements-style) queries against the coded library
- Hits with highlighted terms and document link
- Not a public website search; not a standalone search product
- No generative-AI answer synthesis — hits are documents, not composed advice

### Inputs
Natural-language query; optional within-results keywords; active hit-set identifier.

### Outputs
Ranked/listed hits; narrowed hit set; highlight spans; document links.

### Business Rules
- Search Within Results operates on the current hit list only.
- Results highlight and hyperlink (detail in F03-007); Boolean connectors are F03-006.
- Does not return Claim settlement or eValueI records.
- Does not generate legal advice text.

### Validations
Empty query rejected; within-results requires an existing hit set; rights filter hits the user cannot open.

### Calculations
Hit ranking/order as configured; no financial calculations.

### Workflow
Enter NL query → hit list → Search Within Results → open document.

### Search Requirements
This feature is the NL search; filters by document type (Act, opinion, order, petition/SOB/argument).

### Documents
Library documents already filed.

### Reports
Optional search audit (query, Person, timestamp) for internal use.

### Notifications
None.

### Security
Hits suppressed if F01-003 would refuse view; queries attributable to shared Person.

### Integrations
Library corpus indexing (Medium — mapping + retry of index updates).

### Dependencies
F03-001–F03-004; F03-007; F02-001; F01-003.

### Assumptions
NL search is query-against-corpus, not a large-language-model chat. Boolean syntax is a separate feature (F03-006).

### Risks
Over-broad NL hits slow court-day use; Search Within Results must not silently search the whole corpus again.

### Non Functional Requirements
Interactive search suitable for daily Legal Cell work; index refresh after new filings.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Library Search Box and Hit List | UI | Very High | 16 |
| Search Within Results panel | UI | Complex | 12 |
| Natural-language query and refine engine | API | Very High | 16 |
| Search index | Database | Complex | 6 |
| Library corpus indexing | Integration | Medium | 16 |
| NL search and within-results tests | Testing | Very High | 12 |
| Natural-language library search guide | Documentation | Complex | 4 |
| **Total** | | | **82** |

### Estimation Assumptions
- Not a generative-AI copilot; no answer-composition hours.
- Boolean AND/OR/NOT and proximity connectors are estimated in F03-006.
