# F13-001 — Payment Gateway Connector

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F13-001 |
| **Feature Name** | Payment Gateway Connector |
| **Module** | 13 — API / Integration Hub |

### Description
Connect one BDA-approved payment gateway for booking amount, balance, and applicable housing-charge payments, including verified outcomes and reconciliation support.
### Business Objective
Enable secure online payment outcomes for BHMS without placing connector complexity in payment-business screens.
### Actors
- Citizen; Accounts officer; Super Administrator; System
### User Journey
1. Module 08 requests a payment initiation. 2. The gateway returns the supported payment journey. 3. BHMS verifies callback/status and hands the outcome to the owning payment process.
### Functional Capabilities
- Payment initiation, supported payment methods, callback authenticity, status inquiry, idempotent outcome handoff, sandbox/production controls, and reconciliation hooks.
### Inputs
- Amount, payment head, booking reference, citizen context, return context, and gateway metadata.
### Outputs
- Gateway reference, verified payment status, failure reason, and reconciliation correlation.
### Business Rules
- Module 08 owns dues, receipts, and business posting; a successful gateway result is processed once only.
### Validations
- Amount/currency, authorized source request, callback authenticity, unique correlation, and permitted status transition.
### Calculations
- No independent fee calculation; gateway-provided fees are informational where returned.
### Workflow
- Initiate → citizen pays → verified callback/status inquiry → outcome handoff → reconciliation review.
### Search Requirements
- By gateway reference, booking, payment head, date, status, and exception state.
### Documents
- Provider onboarding evidence and source payment receipt remain in their owning contexts.
### Reports
- Gateway success/failure and unmatched-status extracts for Accounts.
### Notifications
- Operational failure alerts through Module 12.
### Security
- RBAC, least-privilege access, protected sensitive values, and auditable activity.
### Integrations
- Payment Gateway — **Very High (40)** per Estimation Master.
### Dependencies
- Modules 01, 08, 12; F13-002.
### Assumptions
- One primary BDA-approved gateway at go-live; refund payout rails are outside baseline except for outcome hooks.
### Risks
- Provider certification and partial callback failures can delay readiness.
### Non Functional Requirements
- Idempotent settlement, protected credentials, PCI data minimization, low callback latency, and full correlation audit.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Payment configuration and reconciliation hooks | UI | Complex | 8 |
| Payment initiation and verified outcome operations | API | Complex | 8 |
| Payment intent and callback state | Database | Medium | 4 |
| Payment Gateway integration | Integration | Very High | 40 |
| Payment connector tests | Testing | Very High | 12 |
| Payment connector guide | Documentation | Complex | 4 |
| **Total** | | | **76** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. One primary BDA-approved gateway at go-live; refund payout rails are outside baseline except for outcome hooks.
