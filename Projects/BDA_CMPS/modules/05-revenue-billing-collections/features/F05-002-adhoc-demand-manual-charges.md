# F05-002 — Ad-hoc Demand & Manual Charges

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-002 |
| **Feature Name** | Ad-hoc Demand & Manual Charges |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Create manual/ad-hoc demands for miscellaneous or one-off charges with configurable approval before posting to tenant/lease ledgers.

### Business Objective
Handle charges outside the regular bill cycle without bypassing financial controls.

### Actors
- Accounts Officer, Revenue Officer, Approvers

### User Journey
1. Officer creates ad-hoc demand against lease/tenant.
2. Selects charge type, amount, GST applicability, due date, remarks.
3. Submits for approval if configured; on approve, demand posts.

### Functional Capabilities
- Ad-hoc demand entry with charge lines
- Approval workflow (F02-009)
- Link to property/lease/tenant
- Appears in outstanding and portal dues

### Inputs
- Lease/tenant, charge type, amounts, GST flags, due date, reason

### Outputs
- Posted or rejected ad-hoc demand

### Business Rules
- Manual ad-hoc demand requires approval where configured.
- Same ledger and allocation rules as scheduled demands once posted.
- Cannot post against inactive lease without controlled exception.

### Validations
- Amount > 0; mandatory reason; charge type active

### Calculations
- GST on line if taxable per config

### Workflow
Draft → Approve → Post.

### Search Requirements
Ad-hoc demands by status, date, officer.

### Documents
Supporting sanction notes (Module 08).

### Reports
Ad-hoc Demand Register.

### Notifications
Approval tasks; tenant optional notice.

### Security
RBAC; maker-checker; audit.

### Integrations
None.

### Dependencies
F05-001 ledger model; F02-007/009; Module 04

### Assumptions
- Uses shared demand schema from F05-001.

### Risks
- Overuse of ad-hoc bypasses policy — reporting & approval thresholds required.

### Non Functional Requirements
- Same receipt/outstanding behaviour as regular demands

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Ad-hoc demand form | UI | Complex | 8 |
| Ad-hoc demand create/approve ops | API | Complex | 8 |
| Ad-hoc demand entities | Database | Easy | 2 |
| Ad-hoc demand tests | Testing | Complex | 8 |
| Ad-hoc demand guide | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Relies on demand model delivered in F05-001.
