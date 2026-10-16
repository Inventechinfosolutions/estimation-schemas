# F06-002 — Online Instalment Payment & Receipt

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-002 |
| Feature Name | Online Instalment Payment & Receipt |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Online payment of instalments by the bidder through BDA's e-payment gateway (net banking, UPI, debit / credit card, NEFT / RTGS challan), including partial payment rules where allowed, payment status callbacks, double verification with the gateway, automatic bilingual receipt with QR code, and handling of pending and failed transactions.

### Business Objective
Allow bidders to pay securely from anywhere and update payment status immediately on confirmed credit.

### Actors
- Successful Bidder
- System
- Finance Officer (monitoring)

### User Journey
1. **Who creates:** The bidder initiates payment against a demand.
2. **How they create:** The bidder opens Payments, selects the due instalment, confirms the amount, chooses a mode and is redirected to the gateway; on success the receipt is generated.
3. **How they edit:** A pending transaction cannot be edited; the bidder can retry after failure or wait for status reconciliation.
4. **How they send for approval:** No approval; credit is confirmed by gateway callback and verification API.
5. **How the approver sees pending items:** The Finance Officer sees pending and failed transactions in a monitoring view.
6. **How the approver decides:** The Finance Officer does not approve online payments; mismatches go to reconciliation (F06-004) or disputes (F06-009).
7. **How the applicant / maker sees history:** The bidder sees payment history and receipts.
8. **How the approver / auditor sees history:** Auditors see each transaction with gateway reference, callback data hash and receipt.

### Functional Capabilities
- Payment initiation against a demand with amount lock
- Gateway redirect with signed request; callback and server-to-server verification
- NEFT / RTGS challan generation with virtual account / reference where supported
- Status handling: success, failure, pending, timed-out; scheduled status re-query
- Automatic receipt (bilingual PDF, QR) and e-mail / SMS
- Payment status update: 25% / 75% / 100% Payment Completed only on confirmed credit
- Duplicate payment detection and refund flagging
- Convenience charges display where applicable

### UI Screens
- Bidder dues and pay screen
- Payment confirmation and mode selection
- Payment result page
- NEFT / RTGS challan page
- Receipt view and download
- Transaction monitoring (Finance)

### Logical API Operations
- Initiate payment
- Gateway callback handler
- Verify transaction with gateway
- Pending transaction re-query job
- Generate challan
- Generate receipt
- Update instalment and stage status
- Detect duplicate payment
- List transactions

### Inputs
- Demand selection
- Payment mode
- Gateway response

### Outputs
- Transaction record
- Receipt
- Updated payment status

### Business Rules
- Status changes only on verified credit
- Amount cannot be changed by the client (server-side amount)
- Partial payments allowed only if rule permits
- Duplicate payments are flagged for refund, never auto-applied to another site

### Validations
- Callback signature valid
- Amount and order ID match

### Calculations
- Outstanding = demand − confirmed payments

### Workflow
Initiated → Pending → Success (receipt) | Failed | Timed-out → Re-queried

### Search Requirements
- Transactions by site, bidder, date, status, gateway reference

### Documents
- Receipts
- Challans

### Reports
- Daily collection report

### Notifications
- Receipt e-mail / SMS
- Failure notice

### Security
- Checksum / signature validation
- No card data stored
- TLS

### Integrations
- BDA e-payment gateway

### Dependencies
- F06-001
- F13-001
- F12-002

### Assumptions
- BDA's existing gateway supports callbacks and verification API

### Risks
- Gateway downtime and delayed callbacks

### Non Functional Requirements
- Receipt within 1 minute of confirmed credit

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Bidder dues and pay screen | Medium | 6 |
| UI | Payment confirmation and mode selection | Medium | 6 |
| UI | Payment result page | Easy | 4 |
| UI | NEFT / RTGS challan page | Medium | 6 |
| UI | Receipt view and download | Easy | 4 |
| UI | Transaction monitoring (Finance) | Medium | 6 |
| API | Initiate payment | Complex | 8 |
| API | Gateway callback handler | Complex | 8 |
| API | Verify transaction with gateway | Medium | 6 |
| API | Pending transaction re-query job | Medium | 6 |
| API | Generate challan | Medium | 6 |
| API | Generate receipt | Medium | 6 |
| API | Update instalment and stage status | Complex | 8 |
| API | Detect duplicate payment | Medium | 6 |
| API | List transactions | Easy | 4 |
| Database | Payment transaction store | Medium | 4 |
| Database | Receipt register | Easy | 2 |
| Integration | E-payment gateway connector (initiate, callback, verify) | Complex | 24 |
| Testing | Gateway integration tests (success, failure, pending, tampering) | Complex | 8 |
| Testing | Status update and receipt tests | Medium | 6 |
| Testing | Duplicate and concurrency tests | Medium | 6 |
| Documentation | Payment gateway interface note | Medium | 3 |
| Documentation | Bidder payment help (bilingual) | Easy | 2 |

**Feature Total: 145 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 58 | 6 | 24 | 20 | 5 | **145** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- One Complex integration row for the gateway
