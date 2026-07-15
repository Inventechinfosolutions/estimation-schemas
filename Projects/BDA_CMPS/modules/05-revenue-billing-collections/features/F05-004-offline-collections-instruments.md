# F05-004 — Offline Collections & Instruments

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-004 |
| **Feature Name** | Offline Collections & Instruments |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Record offline collections via cash, cheque, DD, bank transfer, NEFT/RTGS (as enabled), including cheque/DD realization dates and bounce handling with reopening of dues.

### Business Objective
Support BDA counter and bank-instrument collections alongside online channels.

### Actors
- Accounts Officer, Revenue Officer, Cashier (if role exists)

### User Journey
1. Officer selects tenant/lease outstanding.
2. Records payment mode and instrument details.
3. Allocates to demands (F05-006).
4. For cheque/DD: mark realized or bounced later; bounce reverses allocation and logs reason.

### Functional Capabilities
- Payment modes: Cash, Cheque, DD, Bank Transfer, NEFT/RTGS (configurable enablement)
- Instrument metadata (number, bank, date, amount)
- Realization workflow for deferred instruments
- Bounce handling with reason and dual-entry audit
- Reconciliation helpers (uninrealized instruments list)

### Inputs
- Mode, amount, instrument fields, target dues, realization/bounce action

### Outputs
- Payment transaction; updated instrument status; allocation effects

### Business Rules
- Partial payments allowed subject to F05-006 priority rules (M4-AC4).
- Bounce restores outstanding and voids provisional clearance.
- Cash collections may require same-day till reconciliation (light process).

### Validations
- Instrument uniqueness warnings; amount > 0; mode enabled
- Bounce only if not permanently realized

### Calculations
- Allocated vs unallocated payment amount

### Workflow
Collect → (Pending realization) → Realized / Bounced.

### Search Requirements
Payments by mode, instrument no., status, date, tenant.

### Documents
Scanned cheque images optional (Module 08).

### Reports
Collection Register; Unrealized Instruments; Bounce Register.

### Notifications
Optional bounce notice to tenant.

### Security
RBAC; till segregation; audit; SoD with credit notes.

### Integrations
None mandatory (bank files optional later).

### Dependencies
F05-001; F05-006; F02-008 payment modes/banks; Module 08/09

### Assumptions
- No automated bank statement AI reconciliation in baseline.
- Receipt generation in F05-007.

### Risks
- Cheque float mismanagement — strong unrealized queue required.

### Non Functional Requirements
- Counter-friendly UI; same-day print receipt path

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Offline collection entry screens | UI | Complex | 8 |
| Cheque/DD realization & bounce UI | UI | Complex | 8 |
| Offline collection & instrument ops | API | Complex | 8 |
| Instrument lifecycle entities | Database | Medium | 4 |
| Offline collection tests | Testing | Complex | 8 |
| Offline collections guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Two Complex UIs: collection entry + realization/bounce.
