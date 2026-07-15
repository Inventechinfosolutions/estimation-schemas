# F07-005 — Vendor Work Assignment & Completion

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-005 |
| **Feature Name** | Vendor Work Assignment & Completion |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Support vendor work assignment, cost estimates, completion certificates, and payment processing linkage to expenditure/work orders (M6-AC4).

### Business Objective
Connect field execution to payable outcomes with documentary evidence.

### Actors
- Maintenance Officer, Accounts Officer, Vendor (data subject)

### User Journey
1. From work order, assign vendor and capture cost estimate.
2. On completion, upload/generate completion certificate.
3. Link to expenditure/payment request (F07-006); approvals by threshold.

### Functional Capabilities
- Vendor assignment on WO
- Cost estimate capture/revisions with audit
- Completion certificate upload/generate
- Payment processing linkage to expense
- Status of payment linkage

### Inputs
- Vendor, estimate amounts, certificate, payment/expense refs

### Outputs
- Assignment record; certificate artefact; expense link

### Business Rules
- Vendor payments linkable to work orders/invoices and require configured approvals (M6-AC4)—approvals executed with F07-006 thresholds.
- Estimate changes after approval require re-approval when configured.

### Validations
- Vendor not blacklisted; amounts ≥ 0
- Certificate required before payment link when configured

### Calculations
- Variance estimate vs actual expense (display)

### Workflow
Assign → Estimate → Execute (F07-002) → Certificate → Payment link.

### Search Requirements
By vendor, WO, certificate status, payment link status.

### Documents
Estimates, certificates, invoices (Module 08).

### Reports
Vendor Work Register; pending certificates.

### Notifications
Pending certificate/payment actions.

### Security
RBAC; audit financial estimates.

### Integrations
Internal expense module ops.

### Dependencies
F07-002/004/006; Module 08

### Assumptions
- Banking payout rails not built here; payment status tracking + expense link.

### Risks
- Paying without certificate — enforce config gate.

### Non Functional Requirements
- Clear trace WO ↔ expense

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Work assignment & estimate UI (vendor context) | UI | Complex | 8 |
| Completion certificate & payment-link UI | UI | Complex | 8 |
| Assignment/certificate/payment-link ops | API | Complex | 8 |
| Assignment certificate entities | Database | Medium | 4 |
| Vendor work lifecycle tests | Testing | Complex | 8 |
| Vendor work assignment guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Deep AP banking integrations via Module 10 only if later required.
