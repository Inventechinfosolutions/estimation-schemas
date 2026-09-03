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
1. Who creates: Approved Valuer (Registered Valuer)
2. How they create: Valuer completes Form V-1 sections (general, land, building, rents, sales, cost of construction, Part II approach, Part III declaration, sub-annexure technical details), consuming inspection amenities and method workings.
3. How they edit: Registered Valuer (and Expert if appointed) declares true information, no interest, personal inspection date, and digitally signs (F05-010).
4. How they send for approval: Form becomes available to the CA. Form V-5 is not offered. Complete V-1 → declare/sign (F05-010) → available to CA (Module 07).
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer (Registered Valuer) works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer (Registered Valuer) opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Complete Form V-1 from inspection + method workings
- Require Registered Valuer digital declaration before CA
- Include Expert declaration when appointed
- Do not offer Form V-5

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My form v-1 immovable report and declaration list / queue | Medium |
| Form V-1 working | Very High |
| Form v-1 immovable report and declaration history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| V-1 assemble and issue | Very High |
| Update form v-1 immovable report and declaration | Medium |
| Search form v-1 immovable report and declaration | Medium |
| Read form v-1 immovable report and declaration history | Easy |

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
|---|---|---|---|
| My form v-1 immovable report and declaration list / queue | UI | Medium | 6 |
| Form V-1 working | UI | Very High | 16 |
| Form v-1 immovable report and declaration history | UI | Medium | 6 |
| V-1 assemble and issue | API | Very High | 16 |
| Update form v-1 immovable report and declaration | API | Medium | 6 |
| Search form v-1 immovable report and declaration | API | Medium | 6 |
| Read form v-1 immovable report and declaration history | API | Easy | 4 |
| Form v-1 immovable report and declaration persistence | DB | Medium | 4 |
| Inspection and method-working consume | Integration | Simple | 4 |
| Form V-1 immovable report and declaration feature tests | Testing | Very High | 12 |
| Form V-1 immovable report and declaration implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **84** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
