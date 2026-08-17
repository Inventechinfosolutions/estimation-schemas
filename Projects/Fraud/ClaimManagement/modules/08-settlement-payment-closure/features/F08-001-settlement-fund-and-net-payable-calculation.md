# F08-001 — Settlement fund and net payable calculation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Settlement fund and net payable calculation |
| **Module** | 08 — Settlement, Payment & Closure |

### Description
An Officer records total recovered amount (from assets), total approved liability and available settlement fund. The system calculates eligible amount, previous returns, previous settlements and net payable. The Officer reviews the figures, saves, and uses net payable for payment.

### Business Objective
Calculate net payable that reconciles to recovered funds, approved liability, previous returns and previous settlements.

### Actors
Officer; Competent Authority (oversee as authorised).

### User Journey
1. Officer records total recovered amount from Module 03 assets, total approved liability and available settlement fund.
2. The system calculates eligible amount, previous returns, previous settlements and net payable.
3. Officer reviews the figures, saves, and uses net payable for payment batches (F08-002).
4. Recovered amount used here must match Module 03 recovered totals.

### Functional Capabilities
- Record total recovered amount, total approved liability, available settlement fund.
- Calculate eligible amount, previous returns, previous settlements, net payable.
- Require recovered total to match Module 03.
- Save figures for payment.

### Inputs
Module 03 recovered total, approved claims, previous returns, previous settlements, available fund.

### Outputs
Saved settlement figures including net payable per claim/batch scope.

### Business Rules
- Recovered amount must match Module 03 totals.
- Settlement calculations reconcile to recovered funds and prior returns/settlements.
- No generative explanation of the arithmetic.

### Validations
- Mismatch between entered recovered amount and Module 03 total is refused or flagged as blocking per policy.
- Net payable cannot be negative unless policy explicitly allows a recorded zero-pay.

### Calculations
Eligible amount; previous returns received; previous settlements; net payable; available settlement fund.

### Workflow
Load recovered/approved inputs → calculate → Officer review → save. Human confirms figures before batching.

### Search Requirements
FE, settlement run, net payable, mismatch-to-Module-03 flag.

### Documents
None required beyond structured figures.

### Reports
Settlement calculation sheet used in F09-001/F09-002 inputs.

### Notifications
On-screen mismatch if recovered totals do not match Module 03.

### Security
Settlement figures are privileged. Changes audited.

### Integrations
None (Module 03 is internal).

### Dependencies
F03-004 recovered funds; F07-005 approved claims; F05 previous returns.

### Assumptions
- Interest-paid-as-principal-repaid already reflected in portfolio figures where applicable.

### Risks
- Paying from a recovered figure that does not match Module 03 would break court-facing outputs.

### Non Functional Requirements
Figures used in court outputs must reconcile to recovered funds and approved claims.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Settlement calculation workbench | UI | Complex | 12 |
| Figures review panel | UI | Medium | 6 |
| Net payable calculation engine | API | Very High | 16 |
| Settlement figure persistence | DB | Complex | 6 |
| Settlement calculation tests | Testing | Very High | 12 |
| Settlement calculation guide | Documentation | Complex | 4 |
| **Total** | | | **56** |

### Estimation Assumptions
- Uses Estimation Master values only.
- API Very High is the financial settlement engine. Payment gateway product is out of scope.
