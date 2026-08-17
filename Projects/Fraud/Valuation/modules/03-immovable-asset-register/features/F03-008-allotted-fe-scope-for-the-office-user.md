# F03-008 — Allotted-FE scope for the office user

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-008 |
| **Feature Name** | Allotted-FE scope for the office user |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An Administrator (on the shared component / valuation allotment) maps which FEs an Office user Person may work. That Officer’s Asset create and search list only those FEs. Attempting to save an asset against a non-allotted FE is refused. A CA or named admin override can open any FE.

### Business Objective
Restrict office create and search to FEs allotted to that Person/Post, with CA/admin override.

### Actors
Administrator; Office user; Competent Authority.

### User Journey
1. Administrator maps which FEs an Office user Person may work.
2. That Officer’s Asset create and search list only those FEs.
3. Save against a non-allotted FE is refused.
4. CA or named admin override can open any FE.

### Functional Capabilities
- Map FEs to Office user Person/Post
- Filter Asset create and search to allotted FEs
- Refuse save on non-allotted FE
- Allow CA/named admin override

### Inputs
Person; FE list; override flag for CA/admin.

### Outputs
Allotment map; filtered lists; refused save.

### Business Rules
- Office user creates and searches immovable assets only for allotted FEs unless override applies
- Refusal is server-side, not only hidden in the dropdown
- Login create/update/delete of Persons remains Claim Module 01

### Validations
- FE exists in programme reference
- Person is Office user Post unless override

### Calculations
None.

### Workflow
Map allotment → create/search filter → refuse out-of-scope save → override path for CA/admin.

### Search Requirements
Person, FE, allotment active, override used.

### Documents
None.

### Reports
FE allotment matrix.

### Notifications
In-app refusal on out-of-scope save.

### Security
Allotment is an access control, not a suggestion. Override is attributable.

### Integrations
Shared Person/Post plus FE reference (F02-005).

### Dependencies
F01-001; F01-002; F02-005; F03-001; F03-005.

### Assumptions
- SPLOCA supplies which Officers are allotted to which FEs.

### Risks
Missing allotment blocks legitimate create; over-broad override weakens need-to-know.

### Non Functional Requirements
Enforce on API; audit allotment changes and override opens.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| FE allotment mapping | UI | Medium | 6 |
| Allotted-FE filter and refuse | API | Complex | 8 |
| Person–FE allotment | Database | Medium | 4 |
| Shared Person and FE-reference consume | Integration | Easy | 8 |
| Allotted-FE scope tests | Testing | Complex | 8 |
| Allotted-FE scope guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- This is valuation allotment, not a second IAM directory.
