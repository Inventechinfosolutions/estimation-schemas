# F02-008 — Financial & Payment Lookup Masters

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-008 |
| **Feature Name** | Financial & Payment Lookup Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain Expense Category, Income Category, Utility Types, Tax Types, Payment Modes, and Bank Masters used across billing, collections, utilities, tax, and expenditure.

### Business Objective
Provide controlled financial reference data so operational modules classify and process transactions consistently.

### Actors
- Super Administrator, Accounts Officer, Utility/Tax officers (limited)

### User Journey
1. Admin opens Financial Masters.
2. Maintains category/type/mode/bank lists.
3. Deactivates obsolete codes; exports registers.

### Functional Capabilities
- CRUD for Expense Category, Income Category, Utility Types, Tax Types, Payment Modes
- Bank Master (bank name, branch, IFSC, account references as required for BDA receipts/payments)
- Activate/deactivate, search, filter, Excel export
- Optional grouping/parent categories

### Inputs
- Codes, names, attributes (IFSC, account no. masked), status

### Outputs
- Lookup lists for Modules 05–07
- Exports

### Business Rules
- Deactivated codes blocked for new transactions; retained historically.
- Payment modes can be enabled/disabled for online vs offline channels.
- Bank master changes do not alter posted receipts; affect future allocation references only.

### Validations
- Unique codes; IFSC format where provided
- Mandatory fields by type

### Calculations
None.

### Workflow
N/A baseline.

### Search Requirements
By code, name, type, status; bank by IFSC/branch.

### Documents
None.

### Reports
Financial Master Registers.

### Notifications
None.

### Security
RBAC; mask sensitive bank account display by role.

### Integrations
None.

### Dependencies
Module 01; consumed by Modules 05–07.

### Assumptions
- Grouped multi-type masters share common admin patterns.
- Offline instrument banks vs BDA collection accounts distinguished in attributes during design.

### Risks
- Payment mode list vs gateway capabilities misalignment (Module 10).

### Non Functional Requirements
- Fast lookups; Excel export; PII/account masking

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Financial lookup master lists/forms (multi-type) | UI | Complex | 8 |
| Bank master form (with account attrs) | UI | Medium | 6 |
| Financial lookup CRUD + search | API | Medium | 6 |
| Lookup & bank master schema | Database | Medium | 4 |
| Financial master tests | Testing | Complex | 8 |
| Financial masters guide | Documentation | Medium | 3 |
| **Total** | | | **35** |

### Estimation Assumptions
- Six lookup types estimated as one Complex UI package + shared Medium API, plus dedicated Bank form Medium.
