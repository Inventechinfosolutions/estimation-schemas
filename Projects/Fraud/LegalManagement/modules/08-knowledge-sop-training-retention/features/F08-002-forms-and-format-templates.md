# F08-002 — Forms and format templates

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Forms and format templates |
| **Module** | 08 — Knowledge, SOP, Training & Retention |

### Description
The user adds a form or format template to the knowledge base. A Legal Cell user opens it from the matter or knowledge menu and uses it for drafting (separate from statutory templates in Module 02 where those are court forms).

### Business Objective
Hold working forms/format templates in knowledge, distinct from court-approved statutory templates in Module 02.

### Actors
Knowledge owner; Legal Cell.

### User Journey
1. Who creates: Knowledge owner
2. How they create: User adds a form or format template to the knowledge base.
3. How they edit: Legal Cell opens it from the matter or knowledge menu and uses it for drafting.
4. How they send for approval: Statutory court forms remain Module 02. Add form → save → open from matter or knowledge.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Knowledge owner works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Knowledge owner opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Knowledge Forms Register
- Form/Template add
- Open from matter or knowledge menu
- Separate from F02-003 court-approved statutory templates
- No generative-AI form fill

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Knowledge Forms Register | Medium |
| Form/Template add | Easy |
| Forms and format templates history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Forms CRUD | Medium |
| Update forms and format templates | Medium |
| Search forms and format templates | Medium |
| Read forms and format templates history | Easy |

### Inputs
Form file; title; usage note; matter-open flag.

### Outputs
Knowledge form; open from matter/knowledge.

### Business Rules
- Separate from statutory templates in Module 02 where those are court forms.
- Human uses the form; no AI compose.

### Validations
- Title and file required; type not overlapping F02-003 court types unless SPLOCA marks it as knowledge-only.

### Calculations
None.

### Workflow
Add form → save → open from matter or knowledge.

### Search Requirements
Title, usage.

### Documents
Forms and format templates.

### Reports
Knowledge forms inventory.

### Notifications
None required.

### Security
Open follows Post rights.

### Integrations
Matter/knowledge menu consume (Simple).

### Dependencies
F04-002; F02-003 boundary; F08-001.

### Assumptions
- Working Word/Excel formats as supplied.

### Risks
Users confuse knowledge forms with court-approved 5(2)/7(1) templates.

### Non Functional Requirements
Available from matter menu when flagged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Knowledge Forms Register | UI | Medium | 6 |
| Form/Template add | UI | Easy | 4 |
| Forms and format templates history | UI | Medium | 6 |
| Forms CRUD | API | Medium | 6 |
| Update forms and format templates | API | Medium | 6 |
| Search forms and format templates | API | Medium | 6 |
| Read forms and format templates history | API | Easy | 4 |
| Forms and format templates persistence | DB | Medium | 4 |
| Matter/knowledge menu consume | Integration | Simple | 4 |
| Forms and format templates feature tests | Testing | Easy | 4 |
| Forms and format templates implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **52** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
