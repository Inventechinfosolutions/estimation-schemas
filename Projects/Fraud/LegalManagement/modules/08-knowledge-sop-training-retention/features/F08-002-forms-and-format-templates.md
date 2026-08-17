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
1. User adds a form or format template to the knowledge base.
2. Legal Cell opens it from the matter or knowledge menu and uses it for drafting.
3. Statutory court forms remain Module 02.

### Functional Capabilities
- Knowledge Forms Register
- Form/Template add
- Open from matter or knowledge menu
- Separate from F02-003 court-approved statutory templates
- No generative-AI form fill

### Inputs
Form file; title; usage note; matter-open flag.

### Outputs
Knowledge form; open from matter/knowledge.

### Business Rules
- Separate from statutory templates in Module 02 where those are court forms.
- Human uses the form; no AI compose.

### Validations
Title and file required; type not overlapping F02-003 court types unless SPLOCA marks it as knowledge-only.

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
Working Word/Excel formats as supplied.

### Risks
Users confuse knowledge forms with court-approved 5(2)/7(1) templates.

### Non Functional Requirements
Available from matter menu when flagged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Knowledge Forms Register | UI | Medium | 6 |
| Form/Template add | UI | Easy | 4 |
| Forms CRUD | API | Medium | 6 |
| Form entities | Database | Easy | 2 |
| Matter/knowledge menu consume | Integration | Simple | 4 |
| Knowledge forms tests | Testing | Easy | 4 |
| Forms and format templates guide | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- F02-003/F02-004 remain the court-approved statutory path.
