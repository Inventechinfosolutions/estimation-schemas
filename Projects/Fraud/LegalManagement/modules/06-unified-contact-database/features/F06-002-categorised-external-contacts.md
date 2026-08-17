# F06-002 — Categorised external contacts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Categorised external contacts |
| **Module** | 06 — Unified Contact Database |

### Description
The user adds an Advocate, Accused, Petitioner, Visitor, External Expert, Tahsildar, AC or Sub Registrar (or a custom category), fills details, and saves.

### Business Objective
Hold categorised external contacts used in legal work, including custom categories the Authority adds.

### Actors
Legal Cell; Advocate; Administrator (custom category).

### User Journey
1. User adds Advocate, Accused, Petitioner, Visitor, External Expert, Tahsildar, AC or Sub Registrar, or a custom category.
2. Fills details and saves.
3. Contact is available to matters and search.

### Functional Capabilities
- External Contact form with standard categories
- Custom Category admin
- Save into the unified directory
- No payment-contact or marketing lists

### Inputs
Category; name; phones; email; address; custom category label where used.

### Outputs
External contact record.

### Business Rules
- Standard categories as Annexure-I: Advocates, Accused, Petitioners, Visitors, External Experts, Tahsildar, AC, Sub Registrar.
- Custom categories allowed.
- Accused/petitioner contacts are directory entries, not a criminal-case CMS rebuild.

### Validations
Category required; custom category unique name; details as configured mandatory.

### Calculations
None.

### Workflow
Select category → fill → save.

### Search Requirements
By category and name (F06-004).

### Documents
None required.

### Reports
Contacts by category.

### Notifications
None required.

### Security
Sensitive accused contacts follow need-to-know.

### Integrations
Internal (Simple).

### Dependencies
F06-001 same directory; F02-005; F01-002.

### Assumptions
Custom categories are Legal-only labels, not a second IAM.

### Risks
Over-broad custom categories become a junk drawer.

### Non Functional Requirements
Same store as office contacts.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| External Contact form (Advocate, Accused, Petitioner, Visitor, Expert, Tahsildar, AC, Sub Registrar) | UI | Complex | 12 |
| Custom Category admin | UI | Easy | 4 |
| External contact CRUD | API | Medium | 6 |
| Category entities | Database | Medium | 4 |
| Internal directory handoff | Integration | Simple | 4 |
| External contact tests | Testing | Easy | 4 |
| Categorised external contacts guide | Documentation | Easy | 2 |
| **Total** | | | **36** |

### Estimation Assumptions
- Office/agency types are F06-001.
