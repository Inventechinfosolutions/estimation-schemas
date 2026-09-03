# F02-007 — Certified structure-classification master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-007 |
| **Feature Name** | Certified structure-classification master |
| **Module** | 02 — Valuation Masters, Property Coding & References |

### Description
An Administrator maintains the certified classification of structures: specification class, expected economic life, and residual/scrap (typically 10% unless the Authority records otherwise). When a Valuer runs cost-of-construction or land-and-building depreciation (F05-002, F05-005), the valuer selects a class from this master; they do not type a one-off life unless an override with reason is recorded.

### Business Objective
Drive depreciation from a certified structure class, not one-off typed lives.

### Actors
Administrator; Approved Valuer.

### User Journey
1. Who creates: Administrator
2. How they create: Administrator maintains specification class, expected economic life, and residual/scrap (typically 10% unless the Authority records otherwise).
3. How they edit: Valuer on F05-002 or F05-005 selects a class from this master.
4. How they send for approval: Maintain class → valuer selects on method working → engine uses life/residual.
5. How the approver sees pending items: No approval inbox unless maker–checker is later required. Auditor opens the register.
6. How the approver decides: No decision on this master beyond save; auditor reads history.
7. How the maker sees history: Administrator opens change history on the record (who changed what, when).
8. How the checker / auditor sees history: Auditor (and checker if used) open the same history.

### Functional Capabilities
- Maintain certified structure classes (specification, economic life, residual/scrap)
- Require class selection on accounts and land-and-building depreciation
- Record override reason if life/residual is replaced

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Structure-classification register | Medium |
| Certified structure-classification master create/edit form | Medium |
| Certified structure-classification master change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Class CRUD and valuation consume | Medium |
| Update certified structure-classification master | Medium |
| Search certified structure-classification master register | Medium |
| Read certified structure-classification master change history | Easy |

### Inputs
Class name/specification; expected economic life; residual/scrap percent; override reason on valuation working.

### Outputs
Selectable class; life and residual consumed by F05-002 / F05-005.

### Business Rules
- Valuer does not type a one-off life unless override with reason is recorded
- Default residual/scrap is typically 10% unless the Authority records otherwise on the class

### Validations
- Life > 0
- Residual within Authority-allowed band
- Override reason mandatory if class values replaced

### Calculations
None here; depreciation formulae run in F05-002 / F05-005 using these values.

### Workflow
Maintain class → valuer selects on method working → engine uses life/residual.

### Search Requirements
Class, life, residual, active.

### Documents
Optional certified-classification circular stored on the master.

### Reports
Structure-classification list.

### Notifications
None.

### Security
Administrator maintains classes; valuers select.

### Integrations
Internal consume by method engines F05-002 and F05-005.

### Dependencies
F05-002; F05-005 (consumers).

### Assumptions
- Authority supplies the certified table; 10% residual is default unless recorded otherwise.

### Risks
Wrong class selection systematically skews depreciation.

### Non Functional Requirements
Class values at calculation time are stored on the working so later master edits do not silently rewrite submitted forms.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Structure-classification register | UI | Medium | 6 |
| Certified structure-classification master create/edit form | UI | Medium | 6 |
| Certified structure-classification master change history | UI | Medium | 6 |
| Class CRUD and valuation consume | API | Medium | 6 |
| Update certified structure-classification master | API | Medium | 6 |
| Search certified structure-classification master register | API | Medium | 6 |
| Read certified structure-classification master change history | API | Easy | 4 |
| Certified structure-classification master identity persistence | DB | Medium | 4 |
| Internal consume by method engines | Integration | Simple | 4 |
| Certified structure-classification master feature tests | Testing | Medium | 6 |
| Certified structure-classification master implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
