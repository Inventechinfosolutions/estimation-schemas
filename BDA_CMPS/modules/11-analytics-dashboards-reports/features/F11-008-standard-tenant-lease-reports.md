# F11-008 — Standard Tenant & Lease Reports

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F11-008 |
| **Feature Name** | Standard Tenant & Lease Reports |
| **Module** | 11 — Analytics, Dashboards & Reports |

### Description
Tenant/Lease report pack: Tenant Register, Lease Expiry, Rent Collection, Outstanding, Security Deposit—with filters and PDF/Excel export.

### Business Objective
Support estate follow-up, renewal planning, and arrears recovery reporting.

### Actors
- Estate, Revenue, Accounts, Auditor

### User Journey
Same pattern as F11-007 for tenant/lease report set.

### Functional Capabilities
- Five named reports
- Filters, scope, PDF/Excel export
- Ageing/expiry windows where relevant

### Inputs
- Report type, filters

### Outputs
- Preview/exports

### Business Rules
- M8-AC2 compliance for this group.
- Outstanding/collection figures align to Module 05 ledgers.

### Validations
Filter rules.

### Calculations
- Totals; ageing buckets where applicable

### Workflow
N/A.

### Search Requirements
Preview search.

### Documents
Exports.

### Reports
This feature.

### Notifications
None.

### Security
PII masking rules for exports by role where required.

### Integrations
None.

### Dependencies
F11-001; Modules 04–05

### Assumptions
- Pack-level Very High API.

### Risks
- PII in Excel exports — watermark/ACL.

### Non Functional Requirements
- Large export async

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Tenant/lease report runner UI | UI | Complex | 8 |
| Tenant/lease report query ops (5 reports) | API | Very High | 16 |
| Report support tables | Database | Easy | 2 |
| PDF/Excel export ops | API | Medium | 6 |
| Tenant/lease reports tests | Testing | Very High | 12 |
| Tenant/lease reports guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
- Five reports as one pack.
