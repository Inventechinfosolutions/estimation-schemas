# F10-002 — Payment Gateway Connector

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-002 |
| **Feature Name** | Payment Gateway Connector |
| **Module** | 10 — API / Integration Hub |

### Description
Implement government-approved payment gateway connector (Razorpay/SBI/other) including order create, callback verification, status inquiry, refund hooks (as needed), and reconciliation support for Module 05 online collections.

### Business Objective
Enable secure online rent and dues payments with trustworthy settlement callbacks.

### Actors
- Technical admin, Accounts (reconcile via Module 05 UX), System

### User Journey
1. Module 05 requests payment order via hub.
2. Hub calls gateway; returns redirect/UPI payload.
3. Gateway callback verified; hub notifies Module 05 settlement.
4. Ops handles disputed statuses via status APIs.

### Functional Capabilities
- Create order / payment link / UPI intent as provider supports
- Signature verification & idempotent callbacks
- Status inquire API
- Refund initiation hooks (if BDA process needs)
- Sandbox/prod config
- Error mapping to domain codes

### Inputs
- Amount, consumer refs, return URLs, metadata

### Outputs
- Gateway order ids; payment status events

### Business Rules
- Business allocation/receipts remain Module 05 (F05-005/007).
- **Reconcile double-count:** F05-005 already estimated Easy (8h) consumption—keep that as thin client; this feature owns Very High gateway integration.

### Validations
- Amount/currency; callback authenticity

### Calculations
None beyond provider fee fields if returned (informational).

### Workflow
Create → Pay → Callback → Confirm/Fail.

### Search Requirements
Gateway transactions by order id/date/status (ops).

### Documents
Provider setup worksheets.

### Reports
Gateway success/failure extracts for Accounts.

### Notifications
Failure spikes via Module 09.

### Security
Webhook hardening; secret rotation; PCI scope minimize (no card data storage).

### Integrations
Payment Gateway — **Very High (40)** per Estimation Master.

### Dependencies
F10-001; Module 05 consumers

### Assumptions
- One primary gateway at go-live; second provider = change request.
- Refund rails included at hook level; complex bank refund ops with Accounts SOP.

### Risks
- Provider certification timelines outside engineering hours.
- Partial webhook failures — status poll mandatory.

### Non Functional Requirements
- Idempotent settlement; low callback processing latency

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Payment gateway config & reconcile hooks UI | UI | Complex | 8 |
| Payment gateway facade APIs | API | Complex | 8 |
| Payment intent/callback entities | Database | Medium | 4 |
| Payment Gateway integration | Integration | Very High | 40 |
| Payment gateway connector tests | Testing | Very High | 12 |
| Payment gateway integration guide | Documentation | Complex | 4 |
| **Total** | | | **76** |

### Estimation Assumptions
- Integration Very High 40 applied once here (not again in Module 05).
