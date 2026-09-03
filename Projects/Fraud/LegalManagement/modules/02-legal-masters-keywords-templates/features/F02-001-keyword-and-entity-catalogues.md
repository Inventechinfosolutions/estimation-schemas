# F02-001 — Keyword and entity catalogues

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Keyword and entity catalogues |
| **Module** | 02 — Legal Masters, Keywords & Templates |

### Description
An Administrator or authorised Legal Cell user opens the keyword catalogue, adds or updates FE, CA, Accused, Advocate, Presiding Judge, Act/Rules/section or doctrine entries, and saves. Library and matter screens then offer those values for coding and search.

### Business Objective
Provide a single coded keyword catalogue so library documents and matters use consistent FE, CA, party, judge, Act and doctrine values.

### Actors
Administrator; authorised Legal Cell.

### User Journey
1. Who creates: Administrator
2. How they create: User opens the Keyword Catalogue Register.
3. How they edit: Adds or updates an FE, CA, Accused, Advocate, Presiding Judge, Act/Rules/section or legal-doctrine entry.
4. How they send for approval: Open catalogue → create/update → save → consume on library/matter.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Keyword Catalogue Register with type filters (FE, CA, Accused, Advocate, Presiding Judge, Act/Rules/section, doctrine)
- Keyword Create/Edit form
- Activate/deactivate catalogue entries without deleting history
- Lookup for library and matter coding screens
- No generative-AI keyword suggestion

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Keyword Catalogue Register | Complex |
| Keyword Create/Edit form (FE, CA, Accused, Advocate, Judge, Act, doctrine) | Complex |
| Keyword and entity catalogues change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Catalogue CRUD and lookup operations | Medium |
| Update keyword and entity catalogues | Medium |
| Search keyword and entity catalogues register | Medium |
| Read keyword and entity catalogues change history | Easy |

### Inputs
Keyword type, display name, code, status, optional FE/CA reference as used by the programme (not a new FE dossier).

### Outputs
Catalogue entry; lookup lists for library/matter; change history.

### Business Rules
- FE/CA names are programme references, not a rebuilt FE dossier or Claim settlement record.
- Library and matter screens consume these values; they do not keep a second local catalogue.
- Deactivated keywords remain on existing documents but are not offered for new coding.
- Intellectual property of the catalogue application remains with SPLOCA.

### Validations
- Type required; unique code within type; FE/CA reference format as agreed with Claim/FE programme; no empty names.

### Calculations
None.

### Workflow
Open catalogue → create/update → save → consume on library/matter.

### Search Requirements
Keyword name, type, code, status.

### Documents
None.

### Reports
Keyword catalogue export (Excel).

### Notifications
None required.

### Security
Catalogue maintenance restricted to Administrator / authorised Legal Cell Posts.

### Integrations
Internal lookup handoff to Modules 03–04 (Simple). FE identity imported as reference only.

### Dependencies
F01-001; F02-002 extends Act/section coding; F02-006 maintains document links.

### Assumptions
- FE dossiers remain in the existing FE application; only coded names/ids are stored here.

### Risks
Duplicate FE/CA spellings fragment search; catalogue change can break links until F02-006 repair.

### Non Functional Requirements
Lookup response suitable for coding screens; auditable catalogue edits.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Keyword Catalogue Register | UI | Complex | 12 |
| Keyword Create/Edit form (FE, CA, Accused, Advocate, Judge, Act, doctrine) | UI | Complex | 12 |
| Keyword and entity catalogues change history | UI | Medium | 6 |
| Catalogue CRUD and lookup operations | API | Medium | 6 |
| Update keyword and entity catalogues | API | Medium | 6 |
| Search keyword and entity catalogues register | API | Medium | 6 |
| Read keyword and entity catalogues change history | API | Easy | 4 |
| Keyword and entity catalogues identity persistence | DB | Medium | 4 |
| Internal library/matter lookup handoff | Integration | Simple | 4 |
| Keyword and entity catalogues feature tests | Testing | Medium | 6 |
| Keyword and entity catalogues implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **68** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
