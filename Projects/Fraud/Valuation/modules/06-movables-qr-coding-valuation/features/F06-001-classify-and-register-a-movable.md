# F06-001 — Classify and register a movable

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Classify and register a movable |
| **Module** | 06 — Movables QR Coding & Valuation (eValueM) |

### Description
An Office user or assigned Valuer selects the seized lot, picks the eValueM code (category / sub-code / object / detail), and records location, model, likely purchase date, likely price, and bank/account details where the proceedings require them. Saving creates the movable row under the parent seizure/FE. Office IT inventory / maintenance tickets are out of scope.

### Business Objective
Register each movable under the parent seizure with a consistent eValueM code and proceedings extras.

### Actors
Office user; Approved Valuer.

### User Journey
1. Office user or assigned Valuer selects the seized lot, picks the eValueM code from F02-004, and records location, model, likely purchase date, likely price, and bank/account details where required.
2. Save creates the movable row under the parent seizure/FE.
3. Office IT inventory is not offered.

### Functional Capabilities
- Classify from eValueM tree (category/sub/object/detail)
- Record location, model, likely purchase date/price, bank/account where required
- Create movable row under parent seizure/FE
- Exclude office IT inventory / maintenance tickets

### Inputs
Parent seizure/FE; eValueM code; location; model; likely purchase date; likely price; bank/account as applicable.

### Outputs
Movable row.

### Business Rules
- Code must come from F02-004
- Not an office IT CMDB
- Valuer cannot invent a parent seizure

### Validations
- Code from tree
- Parent seizure exists
- Allotted-FE/assignment scope as applicable

### Calculations
None.

### Workflow
Select parent → pick code → enter extras → save row.

### Search Requirements
FE, eValueM code, location, model.

### Documents
None.

### Reports
Movable register by seizure.

### Notifications
None.

### Security
Office or assigned valuer; FE/assignment scope.

### Integrations
eValueM tree consume (F02-004).

### Dependencies
F02-004; F01-001; parent seizure/asset.

### Assumptions
- Parent lot/seizure exists from office capture.

### Risks
Coding outside the tree fragments QR later.

### Non Functional Requirements
Row attributable to the Person who saved.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Movable register and classify | UI | Complex | 12 |
| Movable create with code pick | API | Medium | 6 |
| Movable row | Database | Medium | 4 |
| eValueM tree consume | Integration | Simple | 4 |
| Movable register tests | Testing | Medium | 6 |
| Movable register note | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Office IT inventory explicitly out of scope.
