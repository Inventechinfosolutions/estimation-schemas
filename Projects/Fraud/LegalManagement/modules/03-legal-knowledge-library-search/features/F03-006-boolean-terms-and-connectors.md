# F03-006 — Boolean terms and connectors

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-006 |
| **Feature Name** | Boolean terms and connectors |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
The user enters AND, OR, NOT, /p, /s, /pg, /d, a quoted phrase, /#, ! root expander or parentheses, runs search, and opens a hit. The system applies those connectors as specified in Annexure-I.

### Business Objective
Provide Annexure-I Boolean and proximity search so Legal Cell can run precise library queries (including AND/OR/NOT, /p /s /pg /d, quoted phrases, /#, ! and parentheses).

### Actors
Legal Cell; Advocate.

### User Journey
1. User opens Advanced / Boolean Library Search.
2. Enters a query using AND, OR, NOT, /p, /s, /pg, /d, a quoted phrase, /# , ! root expander and/or parentheses.
3. Runs search; the engine applies those connectors as specified in Annexure-I.
4. User opens a hit; highlights follow F03-007.

### Functional Capabilities
- Boolean Query Builder / Advanced Search screen
- Connector help / query syntax panel
- AND, OR, NOT
- Proximity: /p (paragraph), /s (sentence), /pg (page), /d (document window as specified)
- Quoted phrase; /# ; ! root expander; parentheses for grouping
- Open hit from Boolean result list
- No generative-AI query rewrite that changes the user’s connectors

### Inputs
Boolean/proximity query string; optional document-type scope; current corpus.

### Outputs
Hit list honouring connectors; parse errors with syntax guidance; document links.

### Business Rules
- Connectors are those specified in Annexure-I: AND, OR, NOT, /p, /s, /pg, /d, quoted phrase, /#, !, parentheses.
- Quoted phrase matches the phrase as entered.
- Parentheses control evaluation order.
- ! expands the root as specified for this library (not an AI synonym generator).
- /# behaves as specified in Annexure-I (numeric/count connector as used by the Authority’s search facility).
- Public website search is out of scope.

### Validations
Unbalanced parentheses rejected with a clear message; unknown operators rejected; empty query rejected; rights-filter applied to hits.

### Calculations
Proximity windows for /p /s /pg /d as specified; no other business calculations.

### Workflow
Enter Boolean query → parse → search corpus → hit list → open document.

### Search Requirements
This feature is Boolean/proximity search; may combine with type filters (Act, opinion, order, petition).

### Documents
Library corpus.

### Reports
Boolean query audit (optional, Person/timestamp/query).

### Notifications
None.

### Security
Same view rights as NL search; no bypass of F01-003 via a hit snippet.

### Integrations
Search index / corpus (Complex — specialised Boolean/proximity against the legal library, not a generic lookup).

### Dependencies
F03-001–F03-005; F03-007; F02-001.

### Assumptions
Annexure-I connector semantics are implemented as specified; SPLOCA confirms /# and /d window if the annexure is terse. This is not a market search product.

### Risks
Incorrect proximity semantics produce false comfort in research; syntax errors must not run a degraded NL search silently.

### Non Functional Requirements
Parse and search suitable for daily Legal Cell work; explicit syntax errors; index supports proximity.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Boolean Query Builder / Advanced Search screen | UI | Very High | 16 |
| Connector help / query syntax panel | UI | Medium | 6 |
| Boolean parser (AND OR NOT /p /s /pg /d quoted /# ! parentheses) | API | Very High | 16 |
| Proximity and Boolean index support | Database | Very High | 10 |
| Legal library corpus / search index | Integration | Complex | 24 |
| Boolean connector tests | Testing | Very High | 12 |
| Boolean terms and connectors guide | Documentation | Complex | 4 |
| **Total** | | | **88** |

### Estimation Assumptions
- Hours cover Annexure-I connectors only — not a general web search engine.
- NL search is F03-005; highlight/hyperlink is F03-007.
- No generative-AI query expansion hours.
