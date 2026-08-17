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
1. For agricultural land the Valuer completes V-2; for forests/plantations V-3; for mines/quarries V-4, with fields as in the FRS.
2. Each requires personal inspection and no-interest declaration and digital signature (F05-010).
3. Form V-5 is not offered.

### Functional Capabilities
- Form V-2 agricultural land
- Form V-3 forests and plantations
- Form V-4 mines and quarries (excluding plant/buildings as in FRS)
- Digital declaration via F05-010; Form V-5 not offered

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
|---|---|---|---:|
| Form V-2 agricultural working | UI | Complex | 12 |
| Form V-3 and V-4 working | UI | Complex | 12 |
| V-2/V-3/V-4 assemble and issue | API | Very High | 16 |
| V-2/V-3/V-4 form store | Database | Complex | 6 |
| Digital-declaration consume | Integration | Simple | 4 |
| V-2/V-3/V-4 tests | Testing | Very High | 12 |
| Forms V-2–V-4 guide | Documentation | Complex | 4 |
| **Total** | | | **66** |

### Estimation Assumptions
- Two Complex UI artefacts (V-2 vs V-3/V-4). Digital sign hours in F05-010. V-5 excluded.
