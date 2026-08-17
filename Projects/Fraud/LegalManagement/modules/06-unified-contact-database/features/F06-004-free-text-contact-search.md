# F06-004 — Free-text contact search

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-004 |
| **Feature Name** | Free-text contact search |
| **Module** | 06 — Unified Contact Database |

### Description
The user types a name, office, category or fragment; the system shows matches; the user opens the contact.

### Business Objective
Find a contact by free text (name, office, category or fragment) and open the record.

### Actors
Legal Cell; Advocate.

### User Journey
1. User types a name, office, category or fragment in Contact Search.
2. System shows matches.
3. User opens the contact.

### Functional Capabilities
- Contact Search box and results
- Contact Card
- Match on name, office, category, fragment
- Open contact

### Inputs
Free-text query.

### Outputs
Match list; opened contact.

### Business Rules
- A contact can be found by free text and opened with category and details.
- Need-to-know may hide sensitive accused contacts from Posts not allowed.
- Not library Boolean search (F03-006).

### Validations
Empty query rejected or shows recents as configured; results respect rights.

### Calculations
None.

### Workflow
Type → matches → open.

### Search Requirements
This feature is the search.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Filtered by Post where contacts are classified sensitive.

### Integrations
Internal index (Simple).

### Dependencies
F06-001; F06-002; F01-003 where classification applies.

### Assumptions
Fragment match is substring/token, not Boolean proximity.

### Risks
Over-broad fragment returns too many accused names on a shared screen.

### Non Functional Requirements
Interactive as the user types or on submit as designed.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Contact Search box and results | UI | Medium | 6 |
| Contact Card | UI | Easy | 4 |
| Free-text search operations | API | Medium | 6 |
| Contact search indexes | Database | Easy | 2 |
| Internal directory index | Integration | Simple | 4 |
| Contact search tests | Testing | Medium | 6 |
| Free-text contact search guide | Documentation | Simple | 1 |
| **Total** | | | **29** |

### Estimation Assumptions
- Boolean library search is F03-006, not this feature.
