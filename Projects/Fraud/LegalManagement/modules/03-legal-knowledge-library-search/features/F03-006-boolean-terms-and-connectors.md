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
1. Who creates: Legal Cell
2. How they create: User opens Advanced / Boolean Library Search.
3. How they edit: Enters a query using AND, OR, NOT, /p, /s, /pg, /d, a quoted phrase, /# , ! root expander and/or parentheses.
4. How they send for approval: Runs search; the engine applies those connectors as specified in Annexure-I. Enter Boolean query → parse → search corpus → hit list → open document.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. User opens a hit; highlights follow F03-007.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Boolean Query Builder / Advanced Search screen
- Connector help / query syntax panel
- AND, OR, NOT
- Proximity: /p (paragraph), /s (sentence), /pg (page), /d (document window as specified)
- Quoted phrase; /# ; ! root expander; parentheses for grouping
- Open hit from Boolean result list
- No generative-AI query rewrite that changes the user’s connectors

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Boolean Query Builder / Advanced Search screen | Very High |
| Connector help / query syntax panel | Medium |
| Boolean terms and connectors history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Boolean parser (AND OR NOT /p /s /pg /d quoted /# ! parentheses) | Very High |
| Update boolean terms and connectors | Medium |
| Search boolean terms and connectors | Medium |
| Read boolean terms and connectors history | Easy |

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
- Unbalanced parentheses rejected with a clear message; unknown operators rejected; empty query rejected; rights-filter applied to hits.

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
- Annexure-I connector semantics are implemented as specified; SPLOCA confirms /# and /d window if the annexure is terse. This is not a market search product.

### Risks
Incorrect proximity semantics produce false comfort in research; syntax errors must not run a degraded NL search silently.

### Non Functional Requirements
Parse and search suitable for daily Legal Cell work; explicit syntax errors; index supports proximity.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Boolean Query Builder / Advanced Search screen | UI | Very High | 16 |
| Connector help / query syntax panel | UI | Medium | 6 |
| Boolean terms and connectors history | UI | Medium | 6 |
| Boolean parser (AND OR NOT /p /s /pg /d quoted /# ! parentheses) | API | Very High | 16 |
| Update boolean terms and connectors | API | Medium | 6 |
| Search boolean terms and connectors | API | Medium | 6 |
| Read boolean terms and connectors history | API | Easy | 4 |
| Boolean terms and connectors persistence | DB | Medium | 4 |
| Legal library corpus / search index | Integration | Complex | 24 |
| Boolean terms and connectors feature tests | Testing | Very High | 12 |
| Boolean terms and connectors implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **104** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
