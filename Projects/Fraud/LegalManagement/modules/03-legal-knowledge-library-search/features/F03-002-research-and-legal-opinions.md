# F03-002 — Research and legal opinions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Research and legal opinions |
| **Module** | 03 — Legal Knowledge Library & Search |

### Description
The user files an opinion against FE, CA, date, case/petition (Petitioner and OP), and codes Case Number, FE, CA, filing/order dates, Act and section. Another user retrieves it by those fields or keywords.

### Business Objective
File research and legal opinions with the Annexure-I referencing scheme so they can be retrieved by FE, case and Act/section.

### Actors
Legal Cell; Advocate.

### User Journey
1. User opens the Opinion Register and files an opinion.
2. Records FE, CA, date, case/petition (Petitioner and OP).
3. Codes Case Number, FE, CA, filing/order dates, Act and section.
4. Another user retrieves the opinion by those fields or keywords.

### Functional Capabilities
- Opinion Register
- Opinion Filing form (FE, CA, Petitioner/OP, dates, Act/section)
- Retrieve by coded fields and keywords
- Original opinion file unchanged on view
- No generative-AI opinion drafting

### Inputs
Opinion file; FE; CA; date; case/petition (Petitioner & OP); Case Number; filing/order dates; Act & section keywords.

### Outputs
Filed opinion; coded metadata; retrieval hits.

### Business Rules
- Opinions are referenced to FE, CA, Date and Cases/Petitions (Petitioner & OP).
- Coding/hyperlink uses Case Number, FE, CA, Date of Filing, Date of Order, Act & Section.
- FE/CA are programme references, not a new FE dossier or Claim settlement file.
- Human-authored opinions only.

### Validations
Referencing fields required as applicable; keywords from catalogues; rights on open per F01-003.

### Calculations
None.

### Workflow
File → code → save → retrieve by field or keyword.

### Search Requirements
FE, CA, Case Number, Petitioner, OP, Act/section, date.

### Documents
Opinion originals.

### Reports
Opinion filing register.

### Notifications
None required.

### Security
Classification and Post rights on view/download; access log F01-003.

### Integrations
Keyword/FE–CA lookup (Simple).

### Dependencies
F02-001; F03-001 pattern; F04 matter may link the same opinion.

### Assumptions
Opinions are Legal Cell/advocate work product, not Claim settlement determinations.

### Risks
Incomplete Petitioner/OP coding blocks later retrieval.

### Non Functional Requirements
Retrieval by coded fields; originals unchanged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Opinion Register | UI | Medium | 6 |
| Opinion Filing form (FE, CA, petition, dates, Act/section) | UI | Complex | 12 |
| Opinion CRUD and coded retrieve | API | Complex | 8 |
| Opinion entities | Database | Medium | 4 |
| Keyword and FE/CA lookup | Integration | Simple | 4 |
| Opinion filing tests | Testing | Medium | 6 |
| Research and legal opinions guide | Documentation | Easy | 2 |
| **Total** | | | **42** |

### Estimation Assumptions
- Boolean engine is F03-006.
- No AI drafting hours.
