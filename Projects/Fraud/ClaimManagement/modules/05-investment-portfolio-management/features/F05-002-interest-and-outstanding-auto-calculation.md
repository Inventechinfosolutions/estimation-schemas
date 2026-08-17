# F05-002 — Interest and outstanding auto-calculation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Interest and outstanding auto-calculation |
| **Module** | 05 — Investment Portfolio Management |

### Description
After the Officer saves amounts and dates, the system calculates interest received, promised versus paid interest, and outstanding balance (treating interest paid as principal repaid where the Authority’s rule applies). The Officer views the calculated figures, can re-run after a correction, and the calculation is stored for audit.

### Business Objective
Auto-calculate interest and outstanding on saved investments and keep the calculation for audit.

### Actors
Officer; auditor (read calculation trail).

### User Journey
1. Officer saves amounts and dates on the investment (F05-001).
2. The system calculates interest received, promised versus paid interest, and outstanding balance, treating interest paid as principal repaid where the Authority’s rule applies.
3. Officer views the calculated figures and can re-run after a correction.
4. The calculation is stored for audit.

### Functional Capabilities
- Calculate interest received, promised vs paid, outstanding.
- Apply interest-paid-as-principal-repaid where the approved rule requires it.
- Re-run after correction; store calculation for audit.

### Inputs
Deposit amount, dates, promised interest, amount received, Authority calculation rule.

### Outputs
Stored calculated figures and calculation snapshot for audit.

### Business Rules
- Interest-paid-as-principal-repaid applies only where the Authority’s approved business rule requires it.
- Officer may correct inputs and re-run; prior snapshots remain auditable.
- No generative “explain the interest” text; figures are rule-based.

### Validations
- Calculation refused if mandatory amount/date inputs are missing.

### Calculations
Interest received; promised versus paid; outstanding balance per Authority rule.

### Workflow
Save/correct inputs → calculate → view → store snapshot. Human remains responsible for using figures in verification.

### Search Requirements
Investments with outstanding, calculation run date.

### Documents
None.

### Reports
Outstanding extract used in verification and settlement.

### Notifications
None.

### Security
Calculation snapshots are attributable (who re-ran, when).

### Integrations
None (financial engine is internal).

### Dependencies
F05-001.

### Assumptions
- Authority confirms the interest/outstanding formula, including interest-paid-as-principal-repaid.

### Risks
- Wrong rule would mis-state net payable later in F08-001.

### Non Functional Requirements
Calculations are auditable and repeatable after correction.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Calculated interest/outstanding panel | UI | Medium | 6 |
| Recalculation trigger | UI | Simple | 2 |
| Interest and outstanding calculation engine | API | Very High | 16 |
| Calculation snapshot persistence | DB | Medium | 4 |
| Interest/outstanding calculation tests | Testing | Very High | 12 |
| Calculation rule note | Documentation | Complex | 4 |
| **Total** | | | **44** |

### Estimation Assumptions
- Uses Estimation Master values only.
- API Very High is the financial calculation engine, not standard CRUD.
