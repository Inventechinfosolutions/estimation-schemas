# F08-002 — Online Payment Checkout & Status

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Online Payment Checkout & Status |
| **Module** | 08 — Online Payment Management |

### Description
Allow citizens to select an eligible outstanding payment and proceed through the online checkout handoff, then present the final, pending, failed, or exception status returned through the integration hub.

### Business Objective
Collect online payments safely while ensuring only successful settled statuses affect BHMS financial and booking outcomes.

### Actors
Citizen; Accounts Officer; Housing Officer; Auditor.

### User Journey
A citizen opens an eligible due, reviews the amount and payment head, starts checkout, returns to BHMS, and sees a clear pending/success/failure outcome; Accounts can view unresolved exceptions.

### Functional Capabilities
- Pay-now selection, payable summary, checkout handoff/return status, and retry guidance.
- Payment attempt history and pending/failed exception view.
- Controlled linkage from successful payment to the dues ledger and booking confirmation trigger.

### Inputs
Citizen-owned booking, eligible due/payment head, payable amount, payment attempt reference, and status supplied by Module 13.

### Outputs
Payment attempt, checkout status, settled-payment posting request, and citizen status message.

### Business Rules
Only eligible own outstanding dues are payable; BHMS must not mark payment successful until the hub returns a successful status; pending/failed statuses do not confirm a booking; payment amount cannot exceed the permitted payable amount without approved rule support.

### Validations
Citizen ownership, active booking/charge, valid outstanding amount, payment-head eligibility, unique attempt/reference, and status transition validity.

### Calculations
Payable amount, remaining balance after settlement, and attempt ageing.

### Workflow
Due selected → checkout initiated → pending → success/failed/expired → ledger update; booking confirmation consumes successful booking payment only.

### Search Requirements
Payment reference, booking, citizen, payment head, initiation date, status, and exception age.

### Documents
Payment attempt acknowledgement and settled receipt linkage once issued.

### Reports
Online payment status register, pending/failed attempt report, and payment exception queue.

### Notifications
Payment success/failure/pending status notice through Module 12.

### Security
Citizen ownership checks, tamper-resistant amount/reference context, no storage of card credentials, and payment-event audit.

### Integrations
Payment hub checkout/status consumption from Module 13 (Medium); ledger/booking event handoffs (Medium).

### Dependencies
F08-001, F08-003, F07-004, Modules 12–13.

### Assumptions
Supported payment instruments are enabled by the selected gateway; the gateway connector itself is Module 13.

### Risks
Callback delay or ambiguous final status can require Accounts exception handling.

### Non Functional Requirements
Clear return-state handling, idempotent status processing, and peak-load resilience during public booking windows.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Pay-now, checkout return, and payment history UI | UI | Very High | 16 |
| Payment initiation and state processing | API | Very High | 16 |
| Payment attempt/status persistence | Database | Complex | 6 |
| Payment hub and ledger/booking handoffs | Integration | Medium | 16 |
| Checkout and status tests | Testing | Very High | 12 |
| Citizen payment guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
Module 08 estimates Easy/Medium integration-hub consumption only; Very High payment gateway connector work belongs exclusively to Module 13.
