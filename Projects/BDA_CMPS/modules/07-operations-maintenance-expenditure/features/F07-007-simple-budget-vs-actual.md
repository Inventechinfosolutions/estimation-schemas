# F07-007 — Simple Budget vs Actual

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-007 |
| **Feature Name** | Simple Budget vs Actual |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Optional simple annual budget by category and/or property with budget vs actual views against posted expenditures.

### Business Objective
Give managers early visibility of spend against plan without a full budgeting suite.

### Actors
- Accounts Officer, Chief Engineer, Property Manager, Auditor

### User Journey
1. Officer sets annual budget amounts by property and/or category.
2. System compares to posted expenses in period.
3. Views show variance; export for review.

### Functional Capabilities
- Annual budget entry by property and/or expense category
- Budget vs actual dashboard-style view (module-local)
- Variance amount/% 
- Excel export
- Optional soft warning when posting expense near/over budget (no hard block unless configured)

### Inputs
- FY, property/category, budget amount

### Outputs
- Budget records; variance views

### Business Rules
- Simple budgets only—not multi-year forecasting/commitment accounting.
- Actuals = posted expenditures (F07-006) in FY.
- Optional feature—can be Phase 2 but estimated for SOW completeness.

### Validations
- Amount ≥ 0; unique FY+dimensions

### Calculations
- actual, variance = budget − actual, variance %

### Workflow
N/A.

### Search Requirements
By FY, property, category.

### Documents
None.

### Reports
Budget vs Actual export.

### Notifications
Optional over-budget alerts.

### Security
RBAC; audit budget changes.

### Integrations
None.

### Dependencies
F07-006; F02-011 FY params

### Assumptions
- Not a full public financial management budget module.
- Complex UI for pivots/views within module (not Module 11 full MIS).

### Risks
- Users expect encumbrance accounting—confirm out of scope.

### Non Functional Requirements
- Fast aggregation for typical property counts

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Budget setup & budget-vs-actual views | UI | Complex | 8 |
| Budget maintain & compare ops | API | Medium | 6 |
| Budget entities | Database | Easy | 2 |
| Budget vs actual tests | Testing | Medium | 6 |
| Budget guide | Documentation | Easy | 2 |
| **Total** | | | **24** |

### Estimation Assumptions
- Marked optional/simple per SOW; included for estimation completeness.
