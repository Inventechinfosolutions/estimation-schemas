# F06-006 — Form V-7 — gemstones, precious metals and jewellery

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-006 |
| **Feature Name** | Form V-7 — gemstones, precious metals and jewellery |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-7 (item description, unit, gross/net weight, stone and metal values, special enhancement, explanation of rates, purity-testing methods actually adopted from the FRS list: digital weighing, XRF/touchstone, diamond loupe/CVD, gemstone loupe) and Sub-Annexures I and II. Declaration of personal inspection and no interest with digital signature (F05-010) is required.

### Business Objective
Issue Form V-7 with recorded purity-testing methods and sub-annexures, digitally declared.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Valuer completes V-7 including weights, stone and metal values, special enhancement, explanation of rates, and purity-testing methods actually adopted (digital weighing, XRF/touchstone, diamond loupe/CVD, gemstone loupe).
2. Completes Sub-Annexures I and II.
3. Declares personal inspection and no interest with digital signature (F05-010).

### Functional Capabilities
- Form V-7 with stone/metal values and rate explanation
- Record purity-testing methods actually adopted from the FRS list
- Sub-Annexures I and II
- Digital declaration F05-010

### Inputs
V-7 fields; methods adopted; sub-annexures; digital signature.

### Outputs
Issued Form V-7 with sub-annexures.

### Business Rules
- Methods are those actually adopted, not a generated list
- No generative AI

### Validations
- At least one purity-testing method recorded
- Sub-annexures complete as FRS requires
- Digital declaration

### Calculations
Stone/metal values and totals as entered/applied by the valuer.

### Workflow
Complete V-7 + sub-annexures → sign → CA available.

### Search Requirements
Seizure, Form V-7.

### Documents
Form V-7; Sub-Annexures I and II.

### Reports
Form V-7.

### Notifications
In-app if methods or signature missing.

### Security
Assigned valuer; jewellery values need-to-know.

### Integrations
F05-010 consume.

### Dependencies
F06-001; F06-002; F05-010.

### Assumptions
- FRS purity-testing list is the allowed set.

### Risks
Claiming methods not actually used.

### Non Functional Requirements
Methods stored on the issued form.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Form V-7 working | UI | Very High | 16 |
| V-7 and sub-annexure assemble | API | Very High | 16 |
| V-7 and sub-annexure store | Database | Complex | 6 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-7 tests | Testing | Very High | 12 |
| Form V-7 guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
- UI/API Very High justified by purity methods and sub-annexures.
