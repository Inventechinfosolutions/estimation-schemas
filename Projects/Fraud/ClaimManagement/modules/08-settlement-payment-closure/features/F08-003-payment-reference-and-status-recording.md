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
1. Who creates: Officer
2. How they create: After transfer, Officer or returning bank status records payment reference, transaction number and status against each claim in the batch.
3. How they edit: Status values are pending, success, failed or reversed as applicable.
4. How they send for approval: Officer reopens a claim and sees the latest payment status. Transfer → record/return status → visible on claim. Bank core product not built here.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Record payment reference and transaction number.
- Record status pending / success / failed / reversed.
- Show latest status on the claim.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Payment status register | Complex |
| Per-claim payment status | Medium |
| Payment reference and status recording history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Payment status recording operations | Complex |
| Update payment reference and status recording | Medium |
| Search payment reference and status recording | Medium |
| Read payment reference and status recording history | Easy |

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
| Payment reference and status recording history | UI | Medium | 6 |
| Payment status recording operations | API | Complex | 8 |
| Update payment reference and status recording | API | Medium | 6 |
| Search payment reference and status recording | API | Medium | 6 |
| Read payment reference and status recording history | API | Easy | 4 |
| Payment status persistence | DB | Medium | 4 |
| Bank status return (NEFT/RTGS arrangements) | Integration | Medium | 16 |
| Payment reference and status recording feature tests | Testing | Complex | 8 |
| Payment reference and status recording implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
