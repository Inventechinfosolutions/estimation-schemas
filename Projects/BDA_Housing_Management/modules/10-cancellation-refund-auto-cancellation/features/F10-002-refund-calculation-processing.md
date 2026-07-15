# F10-002 — Refund Calculation & Processing

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | Refund Calculation & Processing |
| **Module** | 10 — Cancellation Refund Auto Cancellation |

### Description
Calculate the refund eligible after an approved cancellation using BDA’s configurable deduction policy, create a refund case, and track authorised processing and completion status.

### Business Objective
Provide transparent and auditable refund amounts while keeping payout-rail implementation outside the baseline.

### Actors
Accounts Officer; Finance Supervisor; Citizen; Auditor.

### User Journey
After cancellation approval, Accounts opens the refund case, reviews paid amounts and configured deduction, confirms or records authorised adjustment evidence, marks the case through processing/completed states, and the citizen tracks the outcome.

### Functional Capabilities
- Refund worklist, calculation preview, approval/processing status, and citizen-facing status.
- Configured deduction consumption, adjustment reason capture, and refund register.
- Payment/refund reference recording without implementing bank settlement rails.

### Inputs
Approved cancellation, booking payment ledger, configured deduction percentage, authorised adjustment/reason, refund reference, processing dates, and status.

### Outputs
Refund calculation, refund case, amount breakdown, status history, and citizen update.

### Business Rules
Default deduction is 10% of booking amount but is configurable; refund eligible amount is based on recorded paid amounts less approved deductions; no refund payout is treated as complete without recorded authorised completion status; bank settlement rails are outside baseline.

### Validations
Approved cancellation, valid payment ledger, active deduction parameter, non-negative eligible amount, authorised adjustment, required reference/date for completion.

### Calculations
Deduction = applicable booking amount × configured deduction percentage; eligible refund = eligible paid amount − deduction − approved adjustments, subject to configured policy.

### Workflow
Cancellation approved → refund case created → calculation reviewed → processing → completed/on hold/rejected → citizen status updated.

### Search Requirements
Refund reference, cancellation/booking, citizen, project, unit, amount, status, processing date, and ageing.

### Documents
Refund calculation statement, approval/adjustment evidence, payment reference support, and citizen communication.

### Reports
Refund register, pending-refund ageing, deduction analysis, and completed/refund-on-hold report.

### Notifications
Refund initiated, on-hold, and completion notices through Module 12.

### Security
Accounts-only processing, approval controls for adjustments as configured, citizen access to own status, and full financial audit.

### Integrations
Payment-ledger consumption (Medium) and notification handoff (Easy); payout connector is excluded.

### Dependencies
F10-001; Module 02 parameters; Modules 07–08 and 12.

### Assumptions
BDA defines refund policy exceptions and completes external bank settlement outside this baseline feature.

### Risks
Policy changes or incomplete payment history can change eligible amounts and delay processing.

### Non Functional Requirements
Precise currency treatment, clear amount breakdown, auditable adjustments, and controlled financial access.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Refund worklist, calculation, and status UI | UI | Very High | 16 |
| Refund calculation and processing workflow | API | Very High | 16 |
| Refund case and adjustment persistence | Database | Complex | 6 |
| Payment ledger and notification handoffs | Integration | Medium | 16 |
| Refund calculation tests | Testing | Very High | 12 |
| Refund processing guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
This feature records and tracks refund processing; external payment-payout connectivity is not estimated.
