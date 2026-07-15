# F02-006 — Deposit Rule Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-006 |
| **Feature Name** | Deposit Rule Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure effective-dated security deposit rules: multiples of rent, interest applicability, and forfeiture condition flags used during lease and deposit lifecycle.

### Business Objective
Standardize deposit expectations at allotment and support consistent refund/forfeiture policy application.

### Actors
- Super Administrator, Accounts Officer, Estate Officer

### User Journey
1. Admin creates deposit rule (e.g., 10 months’ rent, interest Y/N).
2. Sets forfeiture condition parameters/flags and effective dates.
3. Lease module suggests deposit amount from active rule.

### Functional Capabilities
- Multiples-of-rent (or fixed amount) configuration
- Interest applicability flags/parameters
- Forfeiture condition configuration (configurable checklist/flags—not legal engine)
- Effective dating, activate/deactivate, search, export

### Inputs
- Multiplier/amount, interest flags, forfeiture flags, applicability, dates, status

### Outputs
- Versioned deposit rules
- Suggested deposit amount preview

### Business Rules
- Active rule at lease approval date drives suggested deposit.
- Forfeiture execution remains in Module 04 with approvals; this feature only configures policy parameters.
- Rule changes do not silently alter collected deposits.

### Validations
- Multiplier/amount > 0 when required
- Date integrity

### Calculations
- Suggested deposit = f(monthly rent, multiplier/fixed)

### Workflow
Optional activation approval.

### Search Requirements
By code, status, lease type, date.

### Documents
None.

### Reports
Deposit Rule Catalogue.

### Notifications
Optional on activation.

### Security
RBAC + audit.

### Integrations
None.

### Dependencies
F02-003; Modules 04–05 consumers.

### Assumptions
- Interest calculation engine for deposits, if applicable, executed in Module 04 using these parameters.
- Forfeiture “conditions” are configurable flags/text, not an expert legal system.

### Risks
- Policy ambiguity on interest on deposits.

### Non Functional Requirements
- Preview accuracy for allotment officers

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Deposit rule list + form | UI | Complex | 8 |
| Deposit rule CRUD + dating | API | Complex | 8 |
| Deposit rule entities | Database | Medium | 4 |
| Deposit rule tests | Testing | Complex | 8 |
| Deposit rule guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Configuration complexity Complex; deposit transaction UX in Module 04.
