# F05-005 — Online Payment Collection

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-005 |
| **Feature Name** | Online Payment Collection |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Enable online collection (UPI/gateway) for selected dues, update demand status, and generate receipts without manual intervention on successful callback, with officer reconciliation for pending/failed states (M4-AC3).

### Business Objective
Increase on-time collection through digital payments for officers/portal (portal UX in F05-009).

### Actors
- Tenant (via portal F05-009), Accounts/Revenue (reconciliation)
- System (callbacks)

### User Journey
1. Payer selects outstanding demands and pays online.
2. Redirect/UPI intent via payment gateway (Module 10 connector).
3. On success callback: allocate, mark paid/partial, issue receipt automatically (M4-AC3).
4. Officer reconciles pending/failed/orphan callbacks in console.

### Functional Capabilities
- Create payment order for selected dues
- Consume Module 10 payment gateway APIs
- Idempotent callback handling
- Auto receipt trigger (F05-007)
- Reconciliation console for mismatches
- Support UPI and other gateway methods as enabled

### Inputs
- Selected demand IDs, amount, payer channel

### Outputs
- Payment order/status; settled payment; receipt

### Business Rules
- Online payment updates demand status and generates receipt without manual intervention (M4-AC3).
- Partial settlements follow F05-006.
- Duplicate callbacks must not double-post.

### Validations
- Amount matches selected dues rules; order expiry

### Calculations
- Payable total after selection

### Workflow
Create order → User pays → Callback → Settle → Receipt.

### Search Requirements
Orders by status, gateway ref, tenant, date.

### Documents
Receipt PDF (F05-007/Module 08).

### Reports
Online Collection Register; Pending Orders.

### Notifications
Payment success/failure (Module 09).

### Security
Checksum/signature verify on callback; no trust of client amount alone.

### Integrations
Payment Gateway via Module 10 — Easy REST consumption here; **Very High gateway connector estimated in Module 10** (avoid double-counting 40h).

### Dependencies
Module 10; F05-006/007; F05-009; Module 09

### Assumptions
- Gateway provider hours primarily Module 10.
- This feature estimates business orchestration + reconcile UX + Easy integration consumption.

### Risks
- Orphan successes without callback — reconciliation tools critical.
- Double-count with Module 10 if both book full gateway — flagged for roll-up.

### Non Functional Requirements
- Near-real-time settlement UX; secure callback endpoint

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Online pay initiation & status UX (officer+support) | UI | Medium | 6 |
| Payment callback reconciliation console | UI | Complex | 8 |
| Online payment order & confirm ops | API | Complex | 8 |
| Payment order entities | Database | Medium | 4 |
| Gateway consumption (via Integration Hub) | Integration | Easy | 8 |
| Online payment tests | Testing | Very High | 12 |
| Online payments guide | Documentation | Medium | 3 |
| **Total** | | | **49** |

### Estimation Assumptions
- Integration Easy (8h) for hub consumption; Module 10 holds Payment Gateway Very High.
