# F04-005 — Lease Amendments & Version History

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-005 |
| **Feature Name** | Lease Amendments & Version History |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Support lease amendments for rent, area, party, and related terms with approvals and full previous version history (M3-AC5).

### Business Objective
Allow controlled contractual changes without losing auditability of prior lease terms.

### Actors
- Estate Officer, Accounts Officer, Approvers, Auditor

### User Journey
1. Officer initiates amendment on active lease.
2. Edits proposed fields; system shows before/after.
3. Approval workflow runs.
4. On approve, new version becomes current; prior version retained.

### Functional Capabilities
- Amendment types: rent change, area change, party change, other conditions
- Before/after comparison
- Approval (F02-009)
- Immutable version history & audit trail
- Propagate rent changes as effective-dated signal to Module 05 (future demands)

### Inputs
- Amendment type, new values, effective date, reason, documents

### Outputs
- New lease version; history timeline

### Business Rules
- All amendments retain previous version history and audit trail (M3-AC5).
- Posted historical demands not silently rewritten; future billing uses new rent from effective date.
- Party change may require refreshed KYC.

### Validations
- Effective date rules; mandatory reason
- Party must exist and pass KYC if replaced

### Calculations
None beyond display deltas.

### Workflow
Draft amendment → Approve → Publish version.

### Search Requirements
Amendments by lease, type, date, status.

### Documents
Amendment agreements (Module 08).

### Reports
Amendment Register.

### Notifications
Approval tasks; tenant notification of change.

### Security
RBAC; audit; SoD on financial rent changes.

### Integrations
None.

### Dependencies
F04-003; F02-009; Module 05 effective rent; Module 08/09

### Assumptions
- Versioning at lease-header level; not full clause CLM.

### Risks
- Mid-cycle rent change policies need BDA clarity.

### Non Functional Requirements
- History always reconstructable for audit

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Amendment request & history UI | UI | Complex | 8 |
| Amendment compare / approve views | UI | Medium | 6 |
| Amendment + versioning operations | API | Complex | 8 |
| Lease version entities | Database | Medium | 4 |
| Amendment tests | Testing | Complex | 8 |
| Amendment guide | Documentation | Medium | 3 |
| **Total** | | | **37** |

### Estimation Assumptions
- Complex API for versioning + effective dating handoff.
