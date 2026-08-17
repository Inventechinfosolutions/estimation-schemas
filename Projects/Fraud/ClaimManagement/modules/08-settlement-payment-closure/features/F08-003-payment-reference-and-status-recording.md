# F08-003 — Payment reference and status recording

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Payment reference and status recording |
| **Module** | 08 — Settlement, Payment & Closure |

### Description
After transfer, the Officer (or returning bank status) records payment reference, transaction number and status (pending, success, failed, reversed) against each claim in the batch. The Officer can reopen a claim and see the latest payment status.

### Business Objective
Store payment reference, transaction number and status for every payment so claims show the latest bank outcome.

### Actors
Officer; bank status return (external).

### User Journey
1. After transfer, Officer or returning bank status records payment reference, transaction number and status against each claim in the batch.
2. Status values are pending, success, failed or reversed as applicable.
3. Officer reopens a claim and sees the latest payment status.

### Functional Capabilities
- Record payment reference and transaction number.
- Record status pending / success / failed / reversed.
- Show latest status on the claim.

### Inputs
Batch, claim, payment reference, transaction number, status.

### Outputs
Updated payment status per claim; history append in F08-004/F08-005.

### Business Rules
- Every payment stores reference, transaction number and status.
- Failed or reversed status must not close the claim (F08-004).

### Validations
- Status from the closed set.
- Reference/transaction recorded as policy requires for the mode.

### Calculations
None.

### Workflow
Transfer → record/return status → visible on claim. Bank core product not built here.

### Search Requirements
Batch ID, claim, payment reference, transaction number, status.

### Documents
Bank return artefacts if supplied.

### Reports
Payment status register.

### Notifications
On-screen status; forensic trail in F08-005.

### Security
Status changes are privileged and audited.

### Integrations
Payment rails — NEFT/RTGS status recording through Authority-approved banking arrangements (not a payment-gateway product).

### Dependencies
F08-002.

### Assumptions
- Bank status may be manual record or file/return as arrangements allow.

### Risks
- Missing transaction numbers would fail payment forensic audit.

### Non Functional Requirements
Latest status retrievable on the claim. Audit who recorded bank references.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Payment status register | UI | Complex | 12 |
| Per-claim payment status | UI | Medium | 6 |
| Payment status recording operations | API | Complex | 8 |
| Payment status persistence | DB | Medium | 4 |
| Bank status return (NEFT/RTGS arrangements) | Integration | Medium | 16 |
| Payment status tests | Testing | Complex | 8 |
| Payment status note | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Integration Medium is bank status mapping/retry, not Very High 40 payment gateway.
