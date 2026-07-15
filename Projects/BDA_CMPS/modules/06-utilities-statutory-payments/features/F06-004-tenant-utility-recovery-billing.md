# F06-004 — Tenant Utility Recovery Billing

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F06-004 |
| **Feature Name** | Tenant Utility Recovery Billing |
| **Module** | 06 — Utilities & Statutory Payments |

### Description
When recovery is enabled, post utility dues to the tenant lease account as demand charge lines in Module 05 (M5-AC2).

### Business Objective
Recover BDA-paid or lease-agreed utility charges from tenants through the standard dues/collection process.

### Actors
- Utility Officer, Accounts Officer, Revenue Officer

### User Journey
1. Officer opens recoverable utility bills for occupied units/leases.
2. Reviews amount (full/share rule as configured).
3. Posts recovery → creates Module 05 demand/ad-hoc charge linked to utility bill.
4. Tenant pays via Module 05 channels; status syncs back as recovered.

### Functional Capabilities
- Mark bills recoverable and link to lease
- Allocate amount to lease (100% or configured share for CAM etc.)
- Post to Module 05 dues (M5-AC2)
- Prevent double posting
- View recovery status

### Inputs
- Utility bill, lease, recoverable amount, GST flags if applicable

### Outputs
- Module 05 demand/charge reference; recovery status

### Business Rules
- Only when recovery enabled for type/lease terms.
- Cannot post if no active lease on unit (exception path).
- Collections remain Module 05; this feature creates recoverable demand.

### Validations
- Lease active; amount ≤ bill outstanding recoverable balance
- Idempotent post key (bill+lease)

### Calculations
- Share % for common charges if configured

### Workflow
Select → Review → Post → Recovered (on payment event).

### Search Requirements
Recoverable pending; posted recoveries by lease/bill.

### Documents
None mandatory beyond bill.

### Reports
Utility Recovery Register.

### Notifications
Optional tenant charge notice (Module 09 / F05-008 patterns).

### Security
RBAC; SoD from bill create if configured; audit posts.

### Integrations
Internal billing demand API (Module 05) — treated as internal service within Complex API (not separate Integration Very High).

### Dependencies
F06-003; Module 04 lease; Module 05 demands; Module 09

### Assumptions
- Does not reinvent payment UX.
- Complex CAM apportionment across many tenants = future enhancement if multi-tenant split complex; baseline supports single-lease or simple share.

### Risks
- Wrong lease linkage — require unit→lease resolution validation.

### Non Functional Requirements
- Clear traceability bill ↔ demand

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Recovery selection & post-to-dues UI | UI | Complex | 8 |
| Recovery posting operations | API | Complex | 8 |
| Recovery link entities | Database | Easy | 2 |
| Recovery posting tests | Testing | Complex | 8 |
| Tenant recovery guide | Documentation | Medium | 3 |
| **Total** | | | **29** |

### Estimation Assumptions
- Internal Module 05 posting included in API complexity.
