# F04-009 — Tenant Portal Lease Summary

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-009 |
| **Feature Name** | Tenant Portal Lease Summary |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Provide tenant self-service portal view of own lease summary: parties, units, term, rent, key dates, deposit summary, and downloadable agreement/notices metadata.

### Business Objective
Improve transparency and reduce estate desk queries; fulfill SOW tenant portal lease visibility.

### Actors
- Tenant (Portal)
- System (scope enforcement)

### User Journey
1. Tenant logs in (Module 01).
2. Opens My Lease(s).
3. Views summary, units, important dates, deposit status snapshot.
4. Downloads agreement/notice PDFs allowed by ACL.

### Functional Capabilities
- List/view leases linked to tenant account
- Summary of term, rent, escalation next date, expiry
- Units/parking linked
- Deposit balance snapshot (from F04-007)
- Links to dues/payments (Module 05 portal) and complaints (Module 07) as navigation only
- Download permitted documents

### Inputs
- Authenticated tenant context

### Outputs
- Read-only lease summary UX

### Business Rules
- Tenant sees only own leases/data.
- No amend/terminate actions in portal baseline (request via office).
- Mask officer-only remarks.

### Validations
- Strict tenant scope on every API

### Calculations
- Days to expiry display

### Workflow
N/A.

### Search Requirements
If multiple leases, simple list filter.

### Documents
Agreement/notices download via Module 08 ACL.

### Reports
None.

### Notifications
In-app list of lease notices (read).

### Security
Tenant role only; server-side scope; no IDOR.

### Integrations
None beyond internal read models.

### Dependencies
F01-001/008; F04-003/007; Module 08

### Assumptions
- Portal dues/pay estimated in Module 05; complaints in Module 07.
- Complex UI for polished tenant-facing summary, not admin grids.

### Risks
- Data leakage across tenants — mandatory security tests.

### Non Functional Requirements
- Mobile-first responsive; < 3s load typical

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Tenant portal lease summary pages | UI | Complex | 8 |
| Portal lease read APIs (scoped) | API | Medium | 6 |
| Portal lease view tests | Testing | Medium | 6 |
| Tenant lease portal help | Documentation | Easy | 2 |
| **Total** | | | **22** |

### Estimation Assumptions
- Credentials issuance not re-estimated (F01-008).
