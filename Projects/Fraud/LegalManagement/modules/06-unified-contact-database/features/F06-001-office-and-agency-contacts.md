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
1. Who creates: Legal Cell
2. How they create: User opens Office and Agency Contacts.
3. How they edit: Adds or updates SPLOCA, RC Office, CA, RD, DFPC, IO or Legal Team, sets category, and saves.
4. How they send for approval: Another user searches and opens that contact. Add/update → save → search/open.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Office/Agency Contact Register
- Office Contact Create/Edit form (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team)
- Category on save
- Open from search
- Not a marketing CRM; not payment contacts

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Office/Agency Contact Register | Medium |
| Office Contact Create/Edit form (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team) | Complex |
| Office and agency contacts history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Office contact CRUD | Medium |
| Update office and agency contacts | Medium |
| Search office and agency contacts | Medium |
| Read office and agency contacts history | Easy |

### Inputs
Office/agency type; name; phones; email; category; notes.

### Outputs
Contact record; searchable directory row.

### Business Rules
- These are official office/agency contacts for legal work.
- Not Claim settlement payee masters.
- Unify/merge of duplicates is F06-003.

### Validations
- Type/category required; at least one name; phone/email format where entered.

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
- CA here is Competent Authority office contact, not a Claim CA workflow.

### Risks
Duplicate office entries until F06-003 merge.

### Non Functional Requirements
Directory available to web and Android consume.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Office/Agency Contact Register | UI | Medium | 6 |
| Office Contact Create/Edit form (SPLOCA, RC, CA, RD, DFPC, IO, Legal Team) | UI | Complex | 12 |
| Office and agency contacts history | UI | Medium | 6 |
| Office contact CRUD | API | Medium | 6 |
| Update office and agency contacts | API | Medium | 6 |
| Search office and agency contacts | API | Medium | 6 |
| Read office and agency contacts history | API | Easy | 4 |
| Office and agency contacts persistence | DB | Medium | 4 |
| Internal directory handoff | Integration | Simple | 4 |
| Office and agency contacts feature tests | Testing | Easy | 4 |
| Office and agency contacts implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **60** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
