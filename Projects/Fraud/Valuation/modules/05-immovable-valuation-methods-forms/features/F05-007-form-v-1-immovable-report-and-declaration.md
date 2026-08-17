# F05-007 — Form V-1 immovable report and declaration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-007 |
| **Feature Name** | Form V-1 immovable report and declaration |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
The Valuer completes Form V-1 (purpose, date, owners, location, amenities, land, roads, tenure, restrictions, building, FSI, rents, disputes, sales, construction, Part II calculations, sub-annexure technical details). The Registered Valuer (and Expert Valuer if appointed — F05-010) declares information true, no direct/indirect interest, and personal inspection date, and digitally signs. The form is then available to the CA.

### Business Objective
Issue Form V-1 for immovable property other than agri/plantations/forests/mines, with declaration and digital signature.

### Actors
Approved Valuer (Registered Valuer); Expert Valuer if appointed.

### User Journey
1. Valuer completes Form V-1 sections (general, land, building, rents, sales, cost of construction, Part II approach, Part III declaration, sub-annexure technical details), consuming inspection amenities and method workings.
2. Registered Valuer (and Expert if appointed) declares true information, no interest, personal inspection date, and digitally signs (F05-010).
3. Form becomes available to the CA. Form V-5 is not offered.

### Functional Capabilities
- Complete Form V-1 from inspection + method workings
- Require Registered Valuer digital declaration before CA
- Include Expert declaration when appointed
- Do not offer Form V-5

### Inputs
V-1 fields; declaration; digital signature (F05-010); method workings; amenity pack.

### Outputs
Issued Form V-1 available to CA.

### Business Rules
- Digital declaration required before CA review
- Form V-5 out of scope
- No generative report drafting

### Validations
- Mandatory V-1 blocks
- Registered Valuer digital declaration present
- Personal inspection date present

### Calculations
Part II calculations as carried from method engines (not re-invented by AI).

### Workflow
Complete V-1 → declare/sign (F05-010) → available to CA (Module 07).

### Search Requirements
Asset, form V-1, issued date.

### Documents
Form V-1.

### Reports
Form V-1 (the statutory report).

### Notifications
In-app when unsigned (cannot submit to CA).

### Security
Assigned Registered Valuer; Expert if appointed; CA reads after issue.

### Integrations
Internal consume of F04-005 amenities and F05-002/003/005 workings; digital sign in F05-010.

### Dependencies
F04-004–F04-008; F05-002–F05-006; F05-010; F07-001.

### Assumptions
- V-1 template matches Annexure-01.

### Risks
Incomplete Part II if method working not saved.

### Non Functional Requirements
Issued form snapshot; later master edits do not silently rewrite issued V-1.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Form V-1 working | UI | Very High | 16 |
| V-1 assemble and issue | API | Very High | 16 |
| V-1 form store | Database | Complex | 6 |
| Inspection and method-working consume | Integration | Simple | 4 |
| Form V-1 tests | Testing | Very High | 12 |
| Form V-1 guide | Documentation | Complex | 4 |
| **Total** | | | **58** |

### Estimation Assumptions
- Digital signature product hours are F05-010. Form V-5 not estimated.
