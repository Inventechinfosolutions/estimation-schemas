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
1. Who creates: Officer
2. How they create: Officer records total recovered amount from Module 03 assets, total approved liability and available settlement fund.
3. How they edit: The system calculates eligible amount, previous returns, previous settlements and net payable.
4. How they send for approval: Officer reviews the figures, saves, and uses net payable for payment batches (F08-002). Load recovered/approved inputs → calculate → Officer review → save. Human confirms figures before batching.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. Recovered amount used here must match Module 03 recovered totals.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record total recovered amount, total approved liability, available settlement fund.
- Calculate eligible amount, previous returns, previous settlements, net payable.
- Require recovered total to match Module 03.
- Save figures for payment.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Settlement calculation workbench | Complex |
| Figures review panel | Medium |
| Settlement fund and net payable calculation history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Net payable calculation engine | Very High |
| Update settlement fund and net payable calculation | Medium |
| Search settlement fund and net payable calculation | Medium |
| Read settlement fund and net payable calculation history | Easy |

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
| Settlement fund and net payable calculation history | UI | Medium | 6 |
| Net payable calculation engine | API | Very High | 16 |
| Update settlement fund and net payable calculation | API | Medium | 6 |
| Search settlement fund and net payable calculation | API | Medium | 6 |
| Read settlement fund and net payable calculation history | API | Easy | 4 |
| Settlement figure persistence | DB | Complex | 6 |
| Settlement fund and net payable calculation feature tests | Testing | Very High | 12 |
| Settlement fund and net payable calculation implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **78** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
