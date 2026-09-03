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
1. Who creates: Legal Cell
2. How they create: User types a name, office, category or fragment in Contact Search.
3. How they edit: System shows matches.
4. How they send for approval: User opens the contact. Type → matches → open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Contact Search box and results
- Contact Card
- Match on name, office, category, fragment
- Open contact

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Contact Search box and results | Medium |
| Contact Card | Easy |
| Free-text contact search history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Free-text search operations | Medium |
| Update free-text contact search | Medium |
| Search free-text contact search | Medium |
| Read free-text contact search history | Easy |

### Inputs
Free-text query.

### Outputs
Match list; opened contact.

### Business Rules
- A contact can be found by free text and opened with category and details.
- Need-to-know may hide sensitive accused contacts from Posts not allowed.
- Not library Boolean search (F03-006).

### Validations
- Empty query rejected or shows recents as configured; results respect rights.

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
- Fragment match is substring/token, not Boolean proximity.

### Risks
Over-broad fragment returns too many accused names on a shared screen.

### Non Functional Requirements
Interactive as the user types or on submit as designed.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Contact Search box and results | UI | Medium | 6 |
| Contact Card | UI | Easy | 4 |
| Free-text contact search history | UI | Medium | 6 |
| Free-text search operations | API | Medium | 6 |
| Update free-text contact search | API | Medium | 6 |
| Search free-text contact search | API | Medium | 6 |
| Read free-text contact search history | API | Easy | 4 |
| Free-text contact search persistence | DB | Medium | 4 |
| Internal directory index | Integration | Simple | 4 |
| Free-text contact search feature tests | Testing | Medium | 6 |
| Free-text contact search implementation documentation | Documentation | Simple | 1 |
| **Total** | | | **53** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
