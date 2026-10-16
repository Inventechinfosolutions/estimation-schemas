# F05-002 — Attempt-Based Fee Calculation & Online Payment

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-002 |
| Feature Name | Attempt-Based Fee Calculation & Online Payment |
| Module | 05 — Online Test Booking, Fees & Hall Ticket |
| Module Type | Business |
| Release | Go-live |

### Description
Fee resolution using category and attempt history, zero-fee path for first employee attempt, payment initiation through the gateway, status handling (success, failure, pending), retries, double-payment prevention and booking confirmation on success.

### Business Objective
Collect correct fees with reliable payment status.

### Actors
- Candidate
- Finance Officer

### User Journey
1. **Who creates:** The candidate initiates payment from booking.
2. **How they create:** The fee is shown with breakup; the candidate chooses a payment mode and pays at the gateway.
3. **How they edit:** Failed payments can be retried within the seat hold.
4. **How they send for approval:** No approval; booking confirms on gateway success.
5. **How the approver sees pending items:** The Finance Officer sees payments by status.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** The candidate sees payment history.
8. **How the approver / auditor sees history:** Auditors see the gateway request and response log.

### Functional Capabilities
- Fee breakup display
- Zero-fee bypass
- Payment modes UPI / UPI-QR, net banking, cards
- Gateway callback and status inquiry
- Pending payment resolution
- Duplicate payment prevention
- Booking confirmation on success

### UI Screens
- Fee breakup and payment mode
- Payment status page
- Payment history

### Logical API Operations
- Resolve fee
- Create payment order
- Handle gateway callback
- Status inquiry for pending
- Prevent double payment
- Confirm booking on payment

### Inputs
- Booking
- Payment mode

### Outputs
- Payment record
- Confirmed booking

### Business Rules
- Booking confirmed only on verified success
- Amount verified against order

### Validations
- Signature verification of callback

### Calculations
- Fee = F02-004 matrix

### Workflow
Initiated → Success / Failed / Pending → Success / Failed

### Search Requirements
- Payments by status

### Documents
- None

### Reports
- Payment statistics

### Notifications
- Payment success / failure

### Security
- Callback signature check
- No card data stored

### Integrations
- Payment gateway via F15-004

### Dependencies
- F02-004
- F15-004
- F05-001

### Assumptions
- KEONICS gateway account

### Risks
- Gateway downtime

### Non Functional Requirements
- Callback processed within 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Fee breakup and payment mode | Medium | 6 |
| UI | Payment status page | Medium | 6 |
| UI | Payment history | Easy | 4 |
| API | Resolve fee | Medium | 6 |
| API | Create payment order | Medium | 6 |
| API | Handle gateway callback | Complex | 8 |
| API | Status inquiry for pending | Medium | 6 |
| API | Prevent double payment | Medium | 6 |
| API | Confirm booking on payment | Medium | 6 |
| Database | Payment transactions | Medium | 4 |
| Testing | Payment flow tests including failures and pending | Complex | 8 |
| Documentation | Payment guide | Easy | 2 |

**Feature Total: 68 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 38 | 4 | 0 | 8 | 2 | **68** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Gateway connector in F15-004
- No external integration channel in this feature; Integration row omitted.
