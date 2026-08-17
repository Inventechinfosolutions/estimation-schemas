# F06-007 — Form V-8 — art and handicrafts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-007 |
| **Feature Name** | Form V-8 — art and handicrafts |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
The Valuer completes V-8 (description, material, dimensions and weight, base value, additions for hand-crafted, antiquity and rarity, total) and declares personal inspection and no interest with digital signature (F05-010).

### Business Objective
Issue Form V-8 with craft/antiquity/rarity additions and digital declaration.

### Actors
Approved Valuer; Expert Valuer if appointed.

### User Journey
1. Valuer completes V-8 description, material, dimensions and weight, base value, and additions for hand-crafted, antiquity and rarity.
2. Declares personal inspection and no interest with digital signature (F05-010).

### Functional Capabilities
- Form V-8 with base value and listed additions
- Digital declaration F05-010
- No generative appraisal narrative

### Inputs
V-8 fields; additions; digital signature.

### Outputs
Issued Form V-8.

### Business Rules
- Additions are valuer-entered
- Unsigned cannot go to CA

### Validations
- Total consistent with base + additions as stored
- Digital declaration

### Calculations
Total = base value + hand-crafted + antiquity + rarity additions as entered.

### Workflow
Complete V-8 → sign → CA available.

### Search Requirements
Seizure, Form V-8.

### Documents
Form V-8.

### Reports
Form V-8.

### Notifications
In-app if unsigned.

### Security
Assigned valuer.

### Integrations
F05-010 consume.

### Dependencies
F06-001; F06-002; F05-010.

### Assumptions
- V-8 template from Annexure-01.

### Risks
Unjustified rarity additions without stored reason if the Authority later requires reason — record remarks on the form.

### Non Functional Requirements
Issued snapshot.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Form V-8 working | UI | Complex | 12 |
| V-8 assemble with additions | API | Complex | 8 |
| V-8 store | Database | Medium | 4 |
| Digital-declaration consume | Integration | Easy | 8 |
| Form V-8 tests | Testing | Complex | 8 |
| Form V-8 guide | Documentation | Complex | 4 |
| **Total** | | | **44** |

### Estimation Assumptions
- Documentation Complex 4 for craft/antiquity/rarity additions.
