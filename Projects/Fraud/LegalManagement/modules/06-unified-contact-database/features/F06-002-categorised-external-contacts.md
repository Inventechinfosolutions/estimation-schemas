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
1. Who creates: Legal Cell
2. How they create: User adds Advocate, Accused, Petitioner, Visitor, External Expert, Tahsildar, AC or Sub Registrar, or a custom category.
3. How they edit: Fills details and saves.
4. How they send for approval: Contact is available to matters and search. Select category → fill → save.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- External Contact form with standard categories
- Custom Category admin
- Save into the unified directory
- No payment-contact or marketing lists

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| External Contact form (Advocate, Accused, Petitioner, Visitor, Expert, Tahsildar, AC, Sub Registrar) | Complex |
| Custom Category admin | Easy |
| Categorised external contacts history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| External contact CRUD | Medium |
| Update categorised external contacts | Medium |
| Search categorised external contacts | Medium |
| Read categorised external contacts history | Easy |

### Inputs
Category; name; phones; email; address; custom category label where used.

### Outputs
External contact record.

### Business Rules
- Standard categories as Annexure-I: Advocates, Accused, Petitioners, Visitors, External Experts, Tahsildar, AC, Sub Registrar.
- Custom categories allowed.
- Accused/petitioner contacts are directory entries, not a criminal-case CMS rebuild.

### Validations
- Category required; custom category unique name; details as configured mandatory.

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
- Custom categories are Legal-only labels, not a second IAM.

### Risks
Over-broad custom categories become a junk drawer.

### Non Functional Requirements
Same store as office contacts.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| External Contact form (Advocate, Accused, Petitioner, Visitor, Expert, Tahsildar, AC, Sub Registrar) | UI | Complex | 12 |
| Custom Category admin | UI | Easy | 4 |
| Categorised external contacts history | UI | Medium | 6 |
| External contact CRUD | API | Medium | 6 |
| Update categorised external contacts | API | Medium | 6 |
| Search categorised external contacts | API | Medium | 6 |
| Read categorised external contacts history | API | Easy | 4 |
| Categorised external contacts persistence | DB | Medium | 4 |
| Internal directory handoff | Integration | Simple | 4 |
| Categorised external contacts feature tests | Testing | Easy | 4 |
| Categorised external contacts implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **58** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
