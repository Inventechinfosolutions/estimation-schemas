# F05-009 — Tenant Portal Dues & Payments

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-009 |
| **Feature Name** | Tenant Portal Dues & Payments |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Tenant self-service to view current dues and history, pay selected outstanding demands online, and download receipts/statements.

### Business Objective
Improve collection convenience and reduce counter load per SOW tenant portal scope.

### Actors
- Tenant (Portal)

### User Journey
1. Tenant opens My Dues.
2. Reviews open demands and history.
3. Selects items → Pay Online (F05-005/Module 10).
4. Downloads receipt and outstanding/payment statements.

### Functional Capabilities
- View current dues and payment/demand history
- Multi-select pay online
- Download receipts and statements
- Clear success/failure messaging
- Navigation to lease summary (F04-009)

### Inputs
- Selected demand IDs; payment confirmation return

### Outputs
- Settled dues view; downloadable PDFs

### Business Rules
- Strict tenant data scope (own leases only).
- Allocation auto-applied (no manual override in portal).
- Show only payable open demands.

### Validations
- IDOR prevention; amount server-calculated

### Calculations
- Payable total for selection

### Workflow
View → Select → Pay → Receipt.

### Search Requirements
Simple filters on open vs history.

### Documents
Receipts/statements via Module 08 ACL.

### Reports
None (tenant-facing).

### Notifications
Payment result notifications.

### Security
Tenant role; server-side scope; secure return URL handling.

### Integrations
Uses F05-005 online payment flow.

### Dependencies
F01-001/008; F05-001/005–007; Module 08/09/10

### Assumptions
- Payment gateway connector not re-estimated at Very High here.
- Testing Very High due to security + payment paths.

### Risks
- Session/payment return race conditions — robust order status page required.

### Non Functional Requirements
- Mobile-first; accessible payment journey

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Portal dues list & detail | UI | Complex | 8 |
| Portal pay selected dues + result pages | UI | Complex | 8 |
| Portal receipts/statements download UI | UI | Medium | 6 |
| Portal billing read/pay APIs (scoped) | API | Complex | 8 |
| Tenant portal billing tests | Testing | Very High | 12 |
| Tenant payment portal help | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- Three UI surfaces estimated independently (dues, pay, downloads).
