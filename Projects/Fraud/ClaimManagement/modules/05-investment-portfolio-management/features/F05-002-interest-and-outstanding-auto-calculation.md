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
1. Who creates: Officer
2. How they create: Officer saves amounts and dates on the investment (F05-001).
3. How they edit: The system calculates interest received, promised versus paid interest, and outstanding balance, treating interest paid as principal repaid where the Authority’s rule applies.
4. How they send for approval: Officer views the calculated figures and can re-run after a correction. Save/correct inputs → calculate → view → store snapshot. Human remains responsible for using figures in verification.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. The calculation is stored for audit.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Calculate interest received, promised vs paid, outstanding.
- Apply interest-paid-as-principal-repaid where the approved rule requires it.
- Re-run after correction; store calculation for audit.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Calculated interest/outstanding panel | Medium |
| Recalculation trigger | Simple |
| Interest and outstanding auto-calculation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Interest and outstanding calculation engine | Very High |
| Update interest and outstanding auto-calculation | Medium |
| Search interest and outstanding auto-calculation | Medium |
| Read interest and outstanding auto-calculation history | Easy |

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
| Interest and outstanding auto-calculation history | UI | Medium | 6 |
| Interest and outstanding calculation engine | API | Very High | 16 |
| Update interest and outstanding auto-calculation | API | Medium | 6 |
| Search interest and outstanding auto-calculation | API | Medium | 6 |
| Read interest and outstanding auto-calculation history | API | Easy | 4 |
| Calculation snapshot persistence | DB | Medium | 4 |
| Interest and outstanding auto-calculation feature tests | Testing | Very High | 12 |
| Interest and outstanding auto-calculation implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **66** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
