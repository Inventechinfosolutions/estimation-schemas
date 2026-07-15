# F11-005 — Financial Dashboard

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-005 |
| **Feature Name** | Financial Dashboard |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Financial dashboard presenting Revenue → Expenses → Net Income → Outstanding → Receivables → Cash flow with period filters and reconciliation to ledgers.

### Business Objective
Single executive view of commercial portfolio financial health.

### Actors
- Commissioner, Accounts, Auditor

### User Journey
1. Select period.
2. Follow financial cascade KPIs.
3. Drill to income/expense/outstanding reports.

### Functional Capabilities
- Cascade KPI flow as SOW
- Period comparison (optional MoM)
- Drill-down to reports/registers
- Closed-period reconciliation mode

### Inputs
- Period filters

### Outputs
- Financial KPIs

### Business Rules
- Not a statutory company accounting P&L—portfolio operating view from CPMS ledgers.
- Must reconcile for UAT closed period (M8-AC1).

### Validations
Period rules.

### Calculations
- Net income = revenue − expenses (defined components)
- Cash flow approximation from collections − expense payments (document formula)

### Workflow
N/A.

### Search Requirements
Drill-down.

### Documents
None.

### Reports
P&L Summary / Cash Collection links.

### Notifications
None.

### Security
Finance-sensitive RBAC.

### Integrations
None (ERP optional elsewhere).

### Dependencies
F11-001/003/004; Modules 05/07

### Assumptions
- Formula freeze workshop with Accounts included in docs/testing intensity.

### Risks
- Cash flow definition ambiguity.

### Non Functional Requirements
- Accurate aggregates; explainability tooltips for formulas

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Financial dashboard UI | UI | Very High | 16 |
| Financial KPI cascade ops | API | Complex | 8 |
| Financial KPI support | Database | Medium | 4 |
| Financial dashboard tests | Testing | Very High | 12 |
| Financial dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Testing Very High for formula reconciliation.
