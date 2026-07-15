# F08-005 — Accounts Reconciliation Views

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-005 |
| **Feature Name** | Accounts Reconciliation Views |
| **Module** | 08 — Online Payment Management |

### Description
Give Accounts a searchable view to compare BHMS payment attempts, settlement outcomes, receipts, and ledger postings, with controlled exception tracking.

### Business Objective
Allow Accounts to identify and resolve mismatches without duplicating the payment gateway connector or a general ledger system.

### Actors
Accounts Officer; Finance Supervisor; Auditor.

### User Journey
An Accounts user filters a settlement period, reviews matched and exception payment records, opens a discrepancy, records resolution remarks or follow-up status, and exports the reconciliation view for review.

### Functional Capabilities
- Settlement-period summary, matched/unmatched/duplicate/pending exception lists, and drill-down.
- Controlled exception notes, status, owner, and ageing view.
- Exportable reconciliation register aligned to payment/receipt/ledger records.

### Inputs
Payment status feed already consumed through the hub, BHMS payment attempt, settled payment, ledger/receipt references, period filters, and resolution remarks.

### Outputs
Reconciliation status, exception register, matching evidence, and period export.

### Business Rules
The view does not change gateway settlement data; exceptions require recorded resolution action; only authorised Accounts users can update exception disposition; booking confirmation remains governed by successful business payment status.

### Validations
Valid reconciliation period, authorised user, existing payment reference, permitted exception transition, and required resolution remarks on closure.

### Calculations
Matched/unmatched counts and amounts, variance amounts, settlement ageing, and exception ageing.

### Workflow
Payment status available → reconcile view → matched or exception → investigate/remark → resolved/monitoring.

### Search Requirements
Payment reference, gateway reference, booking, citizen, payment head, date, amount, match status, exception owner, and age.

### Documents
Settlement support file references where BDA supplies them, receipt, and exception evidence.

### Reports
Daily/monthly reconciliation register, unmatched payment report, and exception ageing report.

### Notifications
Optional internal exception assignment notice through Module 12.

### Security
Accounts-only financial access, maker-checker policy for high-impact exception closure where configured, and full audit of dispositions/exports.

### Integrations
Payment hub status feed consumption (Medium) and ledger/receipt consumption (Medium).

### Dependencies
F08-001–003; Module 13; Module 12.

### Assumptions
Gateway settlement files/feeds are available through the hub as agreed; ERP posting is not part of baseline.

### Risks
Delayed or incomplete settlement feed can keep valid payments in an exception state.

### Non Functional Requirements
Period views must handle high transaction volumes, preserve export consistency, and retain auditable resolutions.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Reconciliation summary, exceptions, and drill-down UI | UI | Very High | 16 |
| Matching and exception-disposition processing | API | Very High | 16 |
| Reconciliation and exception persistence | Database | Complex | 6 |
| Payment hub and ledger/receipt consumption | Integration | Medium | 16 |
| Reconciliation tests | Testing | Very High | 12 |
| Accounts reconciliation guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
This feature consumes the integration hub output. Payment gateway connectivity and callback handling are estimated only in Module 13.
