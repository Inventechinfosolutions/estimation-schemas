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
1. Who creates: Legal Cell
2. How they create: User opens the Opinion Register and files an opinion.
3. How they edit: Records FE, CA, date, case/petition (Petitioner and OP).
4. How they send for approval: Codes Case Number, FE, CA, filing/order dates, Act and section. File → code → save → retrieve by field or keyword.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Legal Cell works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Legal Cell opens history on the record. Another user retrieves the opinion by those fields or keywords.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Opinion Register
- Opinion Filing form (FE, CA, Petitioner/OP, dates, Act/section)
- Retrieve by coded fields and keywords
- Original opinion file unchanged on view
- No generative-AI opinion drafting

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Opinion Register | Medium |
| Opinion Filing form (FE, CA, petition, dates, Act/section) | Complex |
| Research and legal opinions history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Opinion CRUD and coded retrieve | Complex |
| Update research and legal opinions | Medium |
| Search research and legal opinions | Medium |
| Read research and legal opinions history | Easy |

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
- Referencing fields required as applicable; keywords from catalogues; rights on open per F01-003.

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
- Opinions are Legal Cell/advocate work product, not Claim settlement determinations.

### Risks
Incomplete Petitioner/OP coding blocks later retrieval.

### Non Functional Requirements
Retrieval by coded fields; originals unchanged.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Opinion Register | UI | Medium | 6 |
| Opinion Filing form (FE, CA, petition, dates, Act/section) | UI | Complex | 12 |
| Research and legal opinions history | UI | Medium | 6 |
| Opinion CRUD and coded retrieve | API | Complex | 8 |
| Update research and legal opinions | API | Medium | 6 |
| Search research and legal opinions | API | Medium | 6 |
| Read research and legal opinions history | API | Easy | 4 |
| Research and legal opinions persistence | DB | Medium | 4 |
| Keyword and FE/CA lookup | Integration | Simple | 4 |
| Research and legal opinions feature tests | Testing | Medium | 6 |
| Research and legal opinions implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **64** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
