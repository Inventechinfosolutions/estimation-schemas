# F02-005 — Penalty Rule Configuration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F02-005 |
| **Feature Name** | Penalty Rule Configuration |
| **Module** | 02 — Master Data & System Configuration |

### Description
Configure effective-dated penalty rules including grace period and daily/monthly interest or flat penalty models used for overdue rent and related dues.

### Business Objective
Automate consistent arrears penalty policy for billing (M1-AC2) with auditable rule versions.

### Actors
- Super Administrator, Accounts Officer, Revenue Officer

### User Journey
1. Admin defines penalty method, grace days, rate/amount.
2. Sets effective dates and applicability.
3. Activates rule for use by demand generation.

### Functional Capabilities
- Grace period configuration
- Daily/monthly interest or flat penalty
- Effective dating / versioning
- Activate/deactivate, search, export
- Simple preview calculator

### Inputs
- Rule attributes, grace days, rate/amount, basis (outstanding principal etc.), dates, status

### Outputs
- Versioned penalty rules
- Preview penalty amount

### Business Rules
- Penalty not applied within grace period.
- Rule in force determined by due/calculation date policy (document in billing).
- Historical posted penalties not auto-recomputed on rule change.

### Validations
- Non-negative rates/amounts; grace ≥ 0
- Effective date integrity

### Calculations
- Preview: penalty from sample outstanding, days overdue, rule

### Workflow
Optional activation approval.

### Search Requirements
By code, method, status, date.

### Documents
None.

### Reports
Penalty Rule Catalogue.

### Notifications
Optional on activation.

### Security
RBAC + audit.

### Integrations
None.

### Dependencies
F02-003; Module 05 consumer.

### Assumptions
- Interest compounding method confirmed during design (simple vs compound).
- Runtime application hours primarily in Module 05; configuration here.

### Risks
- Legal/policy disputes on interest method; needs BDA written policy.

### Non Functional Requirements
- Clear display of active vs historic versions

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Penalty rule list + form | UI | Complex | 8 |
| Penalty rule CRUD + dating | API | Complex | 8 |
| Penalty rule entities | Database | Medium | 4 |
| Penalty rule tests | Testing | Complex | 8 |
| Penalty rule guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Complex UI for parameter combinations; not full financial engine (that sits in billing).
