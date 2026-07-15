# F11-009 — Standard Financial Reports

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-009 |
| **Feature Name** | Standard Financial Reports |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Financial report pack: Income, Expense, P&L Summary, Cash Collection, Tax, Utility Expense—with filters and PDF/Excel export; reconcile to ledgers.

### Business Objective
Provide Accounts/audit with standard financial MIS from CPMS operational ledgers.

### Actors
- Accounts, Auditor, executives

### User Journey
Select financial report → filter period → preview → export.

### Functional Capabilities
- Six named reports
- Period compulsory
- PDF/Excel export
- Reconciliation notes for UAT

### Inputs
- Report type, period, scope filters

### Outputs
- Preview/exports

### Business Rules
- Portfolio financials not full ERP trial balance.
- Must reconcile for closed periods with Modules 05–07.

### Validations
Period required.

### Calculations
- P&L composition; cash collection totals; tax/utility expense totals

### Workflow
N/A.

### Search Requirements
Preview.

### Documents
Exports.

### Reports
This feature.

### Notifications
None.

### Security
Finance RBAC; audit export downloads.

### Integrations
None.

### Dependencies
F11-001; Modules 05–07

### Assumptions
- Documentation Complex for formula definitions sign-off.
- Testing Very High.

### Risks
- Naming “P&L” confuses statutory accounts—subtitle as “Portfolio Operating Summary”.

### Non Functional Requirements
- Deterministic totals; export performance

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Financial report runner UI | UI | Complex | 8 |
| Financial report query ops (6 reports) | API | Very High | 16 |
| Financial report support | Database | Medium | 4 |
| PDF/Excel export ops | API | Medium | 6 |
| Financial reports tests | Testing | Very High | 12 |
| Financial reports guide | Documentation | Complex | 4 |
| **Total** | | | **50** |

### Estimation Assumptions
- Six reports as one pack.
