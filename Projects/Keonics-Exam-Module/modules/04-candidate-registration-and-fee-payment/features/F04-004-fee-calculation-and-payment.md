# F04-004 — Fee Calculation and Payment

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Fee Calculation and Payment |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
Calculate the applicable examination fee from Module 03 fee rules and attempt history, initiate online payment where payable, track success and failure, store transaction/reference data, issue a receipt, and gate registration completion so that registration completes only after successful payment where payment is mandatory. Government first attempt may be free; subsequent government attempts and other-organisation registrations follow configured payable rules.

### Business Objective
Collect the correct fee reliably, prevent half-registered candidates after failed payments, and produce auditable payment evidence before registration confirmation.

### Actors
Maker: Candidate initiating payment. Approver: none for payment success (gateway callback confirmation). Auditor: Examination Administrator (payment and receipt trail). Payment Gateway: external channel.

### User Journey
1. Who creates: The candidate with identity draft, examination and preferences saved, when fee rules require payment (or when a zero-fee path must still be calculated and acknowledged).
2. How they create: Open fee summary → system calculates amount from category/attempt rules → if payable, initiate payment → complete gateway journey → return to success or failure screen → on success, receipt available and payment gate opens confirmation (F04-005); on failure, retry from failure screen.
3. How they edit: Candidate does not edit calculated fee amounts; may retry failed payments; cannot mark paid manually. Admin fee overrides, if ever allowed by Department, are outside normal candidate path and must be audited if later configured.
4. How they send for approval: Does not apply — payment is confirmed by gateway success, not by a staff approver inbox.
5. How the approver sees pending items: No payment approver inbox; administrators monitor failed/pending transactions via payment transaction history and Module 09 reports.
6. How the approver decides: No staff approve/reject of a payment in this feature; gateway success/failure is authoritative for the payment gate.
7. How the applicant / maker sees history: Candidate sees fee amount, payment status, reference, receipt and retry history on the registration journey and status view.
8. How the approver / auditor sees history: Administrator views transaction references, statuses, amounts, timestamps and receipt linkage on the registration and payment registers.

### Functional Capabilities
- Calculate fee using Module 03 rules (government first free; subsequent government payable; other-organisation mandatory; configurable amounts).
- Use attempt history basis for first vs subsequent government registration.
- Present fee summary before payment initiation.
- Initiate payment with gateway for payable amounts.
- Handle payment return success path and persist success status.
- Handle payment failure/cancel path with retry.
- Store gateway transaction/reference identifiers.
- Issue payment receipt after success.
- Gate registration completion: where payment is mandatory, block F04-005 completion until success.
- Support zero-fee path with explicit fee-calculated acknowledgement without gateway call.
- Query payment status for pending/unknown returns.
- Prevent double-charge on retry after unknown status via idempotent initiation rules.
- Audit all calculation, initiation, callback and receipt events.
- Surface candidate-safe error messages without exposing gateway secrets.

### UI Screens
| Screen | Purpose |
|---|---|
| Fee calculation summary screen | Show category, attempt basis, amount due |
| Payment initiation screen | Confirm and start gateway payment |
| Payment gateway return handling screen | Process return/cancel from gateway UX |
| Payment success and receipt screen | Confirm success and show receipt access |
| Payment failure and retry screen | Explain failure and allow retry |
| Payment receipt view screen | View/download receipt details |
| Payment transaction history screen | Candidate/admin trail of attempts |

### Logical API operations
| Operation | Purpose |
|---|---|
| Calculate applicable examination fee | Apply fee rules and attempt history |
| Initiate payment transaction | Create payable transaction and gateway session |
| Confirm payment callback outcome | Persist success/failure from gateway result |
| Query payment transaction status | Reconcile pending/unknown payments |
| Issue payment receipt | Generate receipt for successful payment |
| Mark registration payment gate complete | Open completion path when rules satisfied |
| Search payment transactions | Locate transactions by reference/status/registration |

### Inputs
Registration draft; candidate category; attempt history; fee rule configuration; gateway response/reference; candidate session.

### Outputs
Calculated fee amount; payment transaction records; success/failure status; receipt; payment-gate flag for registration completion.

### Business Rules
- Fee amounts come from Module 03 configuration — not hard-coded in this feature.
- Other-organisation registration cannot complete without mandatory successful payment.
- Government first attempt may be zero fee; subsequent attempts payable per rules.
- Registration completion (F04-005) requires successful payment where mandatory.
- Failed payments must not leave the candidate marked as fee-paid.
- Receipt issued only after confirmed success.

### Validations
- Draft must have examination selected before fee calculation.
- Payable amount must be non-negative; zero-fee path skips gateway.
- Callback/reference must match initiated transaction.
- Candidate may act only on own transactions.

### Calculations
Fee amount from category + attempt history + configured rule amounts; remaining payable after partial states if Department later defines (baseline: single full amount).

### Workflow
Preferences saved → calculate fee → zero-fee acknowledge OR initiate payment → gateway success/failure → on success issue receipt and open payment gate → proceed to F04-005; on failure allow retry. No staff approval of payment.

### Search Requirements
Admin search by registration number, gateway reference, status, date and examination.

### Documents
Payment receipt (generated). Competent-authority document remains F04-002.

### Reports
Fee collection and failure registers feed Module 09.

### Notifications
Payment success/failure notifications via Module 09 channels as configured; in-portal status always shown.

### Security
Gateway credentials server-side only; integrity of callback verification; PII-minimised receipt; audited payment events; no client-side fee override.

### Integrations
**Payment gateway** — initiation, status, success/failure, reference and receipt support. Estimated as Integration **Very High (40)**.

### Dependencies
Module 03 fee rules and attempt history basis; F04-001/F04-002/F04-003; unlocks F04-005; Module 09 for notification/reporting consumption.

### Assumptions
- Payment gateway product itself is not rebuilt; connector work is Integration Very High on this feature.
- Exact gateway vendor finalised at confirmation; estimate covers enterprise payment integration complexity.
- Hours use Estimation Master; each screen and API independently estimated.

### Risks
Dropped callbacks leave pending payments; weak idempotency risks double charge; fee rule misconfiguration causes under/over collection.

### Non Functional Requirements
Idempotent payment initiation; secure callback handling; clear retry UX; durable transaction audit; production logging without storing card data.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Fee calculation summary screen | UI | Complex | 12 |
| Payment initiation screen | UI | Medium | 6 |
| Payment gateway return handling screen | UI | Medium | 6 |
| Payment success and receipt screen | UI | Easy | 4 |
| Payment failure and retry screen | UI | Medium | 6 |
| Payment receipt view screen | UI | Easy | 4 |
| Payment transaction history screen | UI | Medium | 6 |
| Calculate applicable examination fee | API | Complex | 8 |
| Initiate payment transaction | API | Very High | 16 |
| Confirm payment callback outcome | API | Complex | 8 |
| Query payment transaction status | API | Medium | 6 |
| Issue payment receipt | API | Medium | 6 |
| Mark registration payment gate complete | API | Complex | 8 |
| Search payment transactions | API | Medium | 6 |
| Fee and payment transaction persistence | Database | Complex | 6 |
| Payment gateway fee collection channel | Integration | Very High | 40 |
| Fee calculation and payment tests | Testing | Very High | 12 |
| Fee calculation and payment implementation documentation | Documentation | Complex | 4 |

**Feature total: 164 hours**

### Estimation Assumptions
- Payment Gateway Integration billed at Estimation Master **Very High (40)**.
- Initiate payment API billed **Very High (16)** for transaction orchestration beyond standard CRUD.
- KGID and document upload remain on F04-001 / F04-002.
