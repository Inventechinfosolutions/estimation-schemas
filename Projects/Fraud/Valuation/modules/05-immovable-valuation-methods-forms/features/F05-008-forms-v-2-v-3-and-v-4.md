# F05-008 — Forms V-2, V-3 and V-4

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-008 |
| **Feature Name** | Forms V-2, V-3 and V-4 |
| **Module** | 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) |

### Description
For agricultural land the Valuer completes V-2 (survey, classification, crops, revenue, special features, comparables, unit value, declaration). For forests/plantations, V-3 (area, timber/density/transport, tree schedule). For mines/quarries, V-4 (output, reserves, seam, development, excluding plant/buildings). Each requires personal inspection and no-interest declaration and digital signature (F05-010). Form V-5 is not in the source and is not offered.

### Business Objective
Issue the applicable agricultural, forest/plantation or mine/quarry statutory form with digital declaration; never offer V-5.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Who creates: Approved Valuer
2. How they create: For agricultural land the Valuer completes V-2; for forests/plantations V-3; for mines/quarries V-4, with fields as in the FRS.
3. How they edit: Each requires personal inspection and no-interest declaration and digital signature (F05-010).
4. How they send for approval: Form V-5 is not offered. Select applicable form → complete → declare/sign → available to CA.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Approved Valuer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Approved Valuer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Form V-2 agricultural land
- Form V-3 forests and plantations
- Form V-4 mines and quarries (excluding plant/buildings as in FRS)
- Digital declaration via F05-010; Form V-5 not offered

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Form V-2 agricultural working | Complex |
| Form V-3 and V-4 working | Complex |
| Forms v-2, v-3 and v-4 history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| V-2/V-3/V-4 assemble and issue | Very High |
| Update forms v-2, v-3 and v-4 | Medium |
| Search forms v-2, v-3 and v-4 | Medium |
| Read forms v-2, v-3 and v-4 history | Easy |

### Inputs
Applicable form fields; declaration; digital signature.

### Outputs
Issued V-2 or V-3 or V-4 for CA.

### Business Rules
- V-5 absent and out of scope
- Plant/buildings excluded from V-4 as in FRS
- No generative drafting

### Validations
- Correct form for asset type
- Declaration and digital signature
- V-4 excludes plant/buildings

### Calculations
Unit value and FRS form calculations as entered/applied by the valuer.

### Workflow
Select applicable form → complete → declare/sign → available to CA.

### Search Requirements
Asset, form type V-2/V-3/V-4.

### Documents
Form V-2; Form V-3; Form V-4.

### Reports
The issued statutory form.

### Notifications
In-app if unsigned.

### Security
Assigned valuer; CA after issue.

### Integrations
F05-010 digital declaration consume.

### Dependencies
F05-001; F05-010; inspection Module 04.

### Assumptions
- FRS field lists for V-2–V-4 are supplied as templates.

### Risks
Offering V-5 by mistake; V-4 including plant/buildings contrary to FRS.

### Non Functional Requirements
Templates versioned; V-5 hidden.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Form V-2 agricultural working | UI | Complex | 12 |
| Form V-3 and V-4 working | UI | Complex | 12 |
| Forms v-2, v-3 and v-4 history | UI | Medium | 6 |
| V-2/V-3/V-4 assemble and issue | API | Very High | 16 |
| Update forms v-2, v-3 and v-4 | API | Medium | 6 |
| Search forms v-2, v-3 and v-4 | API | Medium | 6 |
| Read forms v-2, v-3 and v-4 history | API | Easy | 4 |
| Forms v-2, v-3 and v-4 persistence | DB | Medium | 4 |
| Digital-declaration consume | Integration | Simple | 4 |
| Forms V-2, V-3 and V-4 feature tests | Testing | Very High | 12 |
| Forms V-2, V-3 and V-4 implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **86** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
