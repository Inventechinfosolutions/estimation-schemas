# F06-001 — Office and agency contacts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Office and agency contacts |
| **Module** | 06 — Unified Contact Database |

### Description
An authorised user adds or updates a contact for SPLOCA, RC Office, CA, RD, DFPC, IO or Legal Team, sets category, and saves. Another user searches and opens that contact.

### Business Objective
Maintain office and agency contacts (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team) in the unified directory.

### Actors
Legal Cell; Advocate; Administrator.

### User Journey
1. User opens Office and Agency Contacts.
2. Adds or updates SPLOCA, RC Office, CA, RD, DFPC, IO or Legal Team, sets category, and saves.
3. Another user searches and opens that contact.

### Functional Capabilities
- Office/Agency Contact Register
- Office Contact Create/Edit form (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team)
- Category on save
- Open from search
- Not a marketing CRM; not payment contacts

### Inputs
Office/agency type; name; phones; email; category; notes.

### Outputs
Contact record; searchable directory row.

### Business Rules
- These are official office/agency contacts for legal work.
- Not Claim settlement payee masters.
- Unify/merge of duplicates is F06-003.

### Validations
Type/category required; at least one name; phone/email format where entered.

### Calculations
None.

### Workflow
Add/update → save → search/open.

### Search Requirements
Name, office, category (full free-text is F06-004).

### Documents
None required.

### Reports
Office/agency contact extract.

### Notifications
None required.

### Security
Maintain restricted; view by Legal Posts.

### Integrations
Internal directory (Simple).

### Dependencies
F01-001; F02-005 categories; F06-004 search.

### Assumptions
CA here is Competent Authority office contact, not a Claim CA workflow.

### Risks
Duplicate office entries until F06-003 merge.

### Non Functional Requirements
Directory available to web and Android consume.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Office/Agency Contact Register | UI | Medium | 6 |
| Office Contact Create/Edit form (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team) | UI | Complex | 12 |
| Office contact CRUD | API | Medium | 6 |
| Contact entities | Database | Medium | 4 |
| Internal directory handoff | Integration | Simple | 4 |
| Office contact tests | Testing | Easy | 4 |
| Office and agency contacts guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- External categories are F06-002.
- Free-text search UI is F06-004.
