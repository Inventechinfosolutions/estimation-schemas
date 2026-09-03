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
1. Who creates: Office user
2. How they create: Office user or assigned Valuer selects the seized lot, picks the eValueM code from F02-004, and records location, model, likely purchase date, likely price, and bank/account details where required.
3. How they edit: Save creates the movable row under the parent seizure/FE.
4. How they send for approval: Office IT inventory is not offered. Select parent → pick code → enter extras → save row.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Classify from eValueM tree (category/sub/object/detail)
- Record location, model, likely purchase date/price, bank/account where required
- Create movable row under parent seizure/FE
- Exclude office IT inventory / maintenance tickets

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My classify and register a movable list / queue | Medium |
| Movable register and classify | Complex |
| Classify and register a movable history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Movable create with code pick | Medium |
| Update classify and register a movable | Medium |
| Search classify and register a movable | Medium |
| Read classify and register a movable history | Easy |

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
|---|---|---|---|
| My classify and register a movable list / queue | UI | Medium | 6 |
| Movable register and classify | UI | Complex | 12 |
| Classify and register a movable history | UI | Medium | 6 |
| Movable create with code pick | API | Medium | 6 |
| Update classify and register a movable | API | Medium | 6 |
| Search classify and register a movable | API | Medium | 6 |
| Read classify and register a movable history | API | Easy | 4 |
| Classify and register a movable persistence | DB | Medium | 4 |
| eValueM tree consume | Integration | Simple | 4 |
| Classify and register a movable feature tests | Testing | Medium | 6 |
| Classify and register a movable implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **62** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
