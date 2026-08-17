# F06-005 — Form V-6 — equipment, furniture, machinery and plant

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-005 |
| **Feature Name** | Form V-6 — equipment, furniture, machinery and plant |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-6 (purpose, date, owners, description and purpose of plant, line-wise code, description, make, model/year, original and present market price, depreciation, market value) and declares personal inspection and no interest with digital signature (F05-010).

### Business Objective
Issue Form V-6 from tabulated movables with digital declaration.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Valuer completes V-6 from tabulated equipment/furniture/machinery/plant rows (codes, make, model/year, original and present market price, depreciation, market value).
2. Declares personal inspection and no interest with digital signature (F05-010).

### Functional Capabilities
- Complete Form V-6 from eValueM tabulation
- Digital declaration via F05-010
- No generative drafting

### Inputs
V-6 fields; tabulated rows; digital signature.

### Outputs
Issued Form V-6.

### Business Rules
- Reads F06-001/F06-002 rather than re-keying codes/condition
- Unsigned cannot go to CA

### Validations
- Line-wise codes from tree
- Digital declaration present

### Calculations
Depreciation and present market value as entered/applied by the valuer on V-6.

### Workflow
Complete V-6 → sign (F05-010) → CA available.

### Search Requirements
Asset/seizure, Form V-6.

### Documents
Form V-6.

### Reports
Form V-6.

### Notifications
In-app if unsigned.

### Security
Assigned valuer.

### Integrations
F05-010 digital signature consume.

### Dependencies
F06-001; F06-002; F05-010; F07-001.

### Assumptions
- V-6 template from Annexure-01.

### Risks
Plant included on V-4 mines form instead of V-6.

### Non Functional Requirements
Issued snapshot.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Form V-6 working | UI | Complex | 12 |
| V-6 assemble | API | Complex | 8 |
| V-6 store | Database | Medium | 4 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-6 tests | Testing | Complex | 8 |
| Form V-6 guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- PKI hours sit in F05-010.
