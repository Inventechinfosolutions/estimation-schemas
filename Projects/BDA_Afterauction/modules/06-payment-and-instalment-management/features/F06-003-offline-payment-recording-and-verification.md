# F06-003 — Offline Payment Recording & Verification

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-003 |
| Feature Name | Offline Payment Recording & Verification |
| Module | 06 — Payment & Instalment Management |
| Module Type | Business |
| Release | Go-live |

### Description
Recording of payments made offline by Demand Draft, NEFT or RTGS (outside the gateway), by the bidder (self-report with proof) or by BDA staff, and verification by the Payment Reconciler against bank statements before credit is applied and a receipt is issued.

### Business Objective
Accept all permitted payment channels while ensuring no credit is recorded without verification.

### Actors
- Successful Bidder
- Payment Reconciler
- Finance Officer

### User Journey
1. **Who creates:** The bidder or a Payment Reconciler creates an offline payment entry.
2. **How they create:** The bidder selects the instalment, enters mode, instrument / UTR number, date, amount and bank, and uploads proof; staff can enter the same for counter receipts.
3. **How they edit:** The entry can be edited until verification starts.
4. **How they send for approval:** The entry goes to the Payment Reconciler's verification queue.
5. **How the approver sees pending items:** The Payment Reconciler sees pending entries with proof and matching bank lines.
6. **How the approver decides:** The Payment Reconciler verifies (credit applied, receipt issued) or rejects with reason; large amounts can need Finance Officer confirmation.
7. **How the applicant / maker sees history:** The bidder sees status and receipt.
8. **How the approver / auditor sees history:** Auditors see entry, proof, verifier and decision.

### Functional Capabilities
- Offline payment entry by bidder or staff
- Proof upload (DD copy, UTR advice)
- Verification queue with suggested bank statement matches
- Two-level verification above a configured amount
- Receipt generation on verification
- DD realisation status tracking

### UI Screens
- Offline payment entry (bidder)
- Offline payment entry (staff)
- Verification queue
- Verification decision with proof and matches
- DD realisation tracking

### Logical API Operations
- Create offline payment entry
- Upload proof
- Suggest bank matches
- Verify / reject entry
- Second-level confirmation
- Issue receipt and update status
- Update DD realisation

### Inputs
- Mode, reference, date, amount, bank
- Proof file
- Decision

### Outputs
- Verified credit
- Receipt

### Business Rules
- UTR / DD number unique
- Credit only after verification and, for DD, realisation
- Rejected entries notify the bidder with reason

### Validations
- Amount ≤ outstanding unless excess allowed
- Date not in future
- File type PDF / JPG ≤ 5 MB

### Calculations
- Outstanding after credit

### Workflow
Entered → Under Verification → Verified (receipt) | Rejected

### Search Requirements
- By UTR / DD number, site, bidder, status

### Documents
- Payment proofs

### Reports
- Offline payments pending verification

### Notifications
- Verification outcome to bidder

### Security
- Reconciler cannot verify their own entries

### Integrations
- None (uses bank data from F06-004)

### Dependencies
- F06-004
- F06-001

### Assumptions
- Bank statements available daily

### Risks
- Fake proofs; verification against bank data mitigates

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Offline payment entry (bidder) | Medium | 6 |
| UI | Offline payment entry (staff) | Easy | 4 |
| UI | Verification queue | Medium | 6 |
| UI | Verification decision with proof and matches | Medium | 6 |
| UI | DD realisation tracking | Easy | 4 |
| API | Create offline payment entry | Medium | 6 |
| API | Upload proof | Easy | 4 |
| API | Suggest bank matches | Medium | 6 |
| API | Verify / reject entry | Medium | 6 |
| API | Second-level confirmation | Easy | 4 |
| API | Issue receipt and update status | Medium | 6 |
| API | Update DD realisation | Easy | 4 |
| Database | Offline payment entry store | Easy | 2 |
| Testing | Offline entry and verification tests | Medium | 6 |
| Testing | Two-level and DD realisation tests | Easy | 4 |
| Documentation | Offline payment verification guide | Easy | 2 |

**Feature Total: 76 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 36 | 2 | 0 | 10 | 2 | **76** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- No external integration
- No external integration channel in this feature; Integration row omitted.
