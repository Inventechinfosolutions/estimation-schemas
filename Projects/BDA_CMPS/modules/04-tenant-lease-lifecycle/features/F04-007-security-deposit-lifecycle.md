# F04-007 — Security Deposit Lifecycle

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-007 |
| **Feature Name** | Security Deposit Lifecycle |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Manage security deposit collection, adjustment against dues, refund, forfeiture, optional interest, and refund workflow with approvals updating tenant ledger (M3-AC4).

### Business Objective
Safeguard deposits from allotment through vacate with full financial control and audit.

### Actors
- Accounts Officer, Estate Officer, Approvers, Auditor
- Tenant (portal view of deposit status — read)

### User Journey
1. Collect deposit against lease (instruments online/offline — collection posting may use Module 05 payment patterns).
2. Track deposit balance/ledger.
3. Adjust against dues when approved.
4. Refund or forfeit via approval workflow; update ledger.

### Functional Capabilities
- Deposit demand/collection recording
- Ledger: collected, adjusted, refunded, forfeited, balance
- Interest calculation if configured (F02-006 parameters)
- Refund workflow with payment processing status
- Forfeiture with reason codes
- Waiver of deposit for activation (approved exception) per M3-AC1
- Deposit-related notice triggers (with F04-008)

### Inputs
- Amounts, instruments/refs, adjustment dues refs, refund beneficiary, reasons

### Outputs
- Deposit ledger movements
- Approval tasks
- Updated activation gate / vacate clearance

### Business Rules
- Refund/forfeiture follows approval workflow and updates tenant ledger (M3-AC4).
- Suggested deposit from Module 02 deposit rules.
- Adjustments link to Module 05 outstanding where applicable.
- Payment gateway settlement for refunds may use Module 10/05 — record status here.

### Validations
- Amounts ≤ available balance for refund/forfeit/adjust
- Beneficiary bank details for refund

### Calculations
- Optional interest on deposit per rule
- Net refundable = balance − dues hold ± interest

### Workflow
Collect → (Adjust) → Refund/Forfeit request → Approve → Paid/Closed.

### Search Requirements
By lease, tenant, status, ageing of pending refunds.

### Documents
Deposit receipts, refund sanctions (Module 08).

### Reports
Security Deposit Report; pending refunds.

### Notifications
Deposit due, refund processed, forfeiture notices.

### Security
SoD collection vs refund approve; full audit.

### Integrations
May call Module 05 payment posting / Module 10 refund payout patterns (internal).

### Dependencies
F02-006; F04-003; Module 05; Module 08/09/10 as applicable

### Assumptions
- Very High API: financial deposit engine + workflows.
- Online collection UX primarily Module 05; this owns deposit business ledger.

### Risks
- Dual posting between deposit ledger and receipts — clear accounting design needed.

### Non Functional Requirements
- Ledger reconcile-able to receipts for UAT period

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Deposit ledger & transactions UI | UI | Complex | 8 |
| Refund / forfeiture / adjustment forms | UI | Complex | 8 |
| Deposit lifecycle operations | API | Very High | 16 |
| Deposit ledger schema | Database | Medium | 4 |
| Deposit lifecycle tests | Testing | Very High | 12 |
| Deposit management guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Payment gateway connector hours remain Module 10; deposit business logic here.
