# F11-003 — Revenue Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-003 |
| **Feature Name** | Revenue Dashboard |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Revenue dashboard for rent demand, collected, pending, collection %, security deposit position, and utility & tax collections where applicable, with drill-down and ledger reconciliation for closed periods (M8-AC1).

### Business Objective
Executive visibility of revenue realization and arrears pressure.

### Actors
- Accounts, Revenue, Commissioner, Auditor

### User Journey
1. Select period.
2. View demand vs collection KPIs and deposit position.
3. Drill to demand/payment/outstanding registers (Module 05/04).

### Functional Capabilities
- Demand, collected, pending, collection %
- Security deposit position
- Utility & tax collection tiles (from Module 06 postings/recoveries as available)
- Trend sparklines optional baseline charts
- Drill-down

### Inputs
- Period filters

### Outputs
- Revenue KPIs

### Business Rules
- KPIs reconcile to transactional data for closed test period (M8-AC1).
- Credits/cancellations net correctly.

### Validations
Period closed flag for reconciliation pack.

### Calculations
- collection % = collected / demand (define inclusion rules with Accounts)

### Workflow
N/A.

### Search Requirements
Drill-down.

### Documents
None.

### Reports
Links to financial/Outstanding reports.

### Notifications
None.

### Security
Financial roles; scoped.

### Integrations
None.

### Dependencies
F11-001; Modules 04–06

### Assumptions
- Testing Very High for reconciliation scenarios.

### Risks
- Definition debates on demand base — freeze with BDA Accounts.

### Non Functional Requirements
- Accurate to ledgers; performant aggregations

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Revenue dashboard UI | UI | Very High | 16 |
| Revenue KPI query ops | API | Complex | 8 |
| Revenue KPI support | Database | Medium | 4 |
| Revenue dashboard tests | Testing | Very High | 12 |
| Revenue dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Utility/tax tiles depend on Module 06 data quality.
