# F05-007 — Receipts, History & Outstanding Statements

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F05-007 |
| **Feature Name** | Receipts, History & Outstanding Statements |
| **Module** | 05 — Revenue Billing & Collections |

### Description
Auto-generate digital receipts, maintain payment history, and produce outstanding statements per tenant/lease/property, with PDF archive and exports reconciling to ledgers (M4-AC5).

### Business Objective
Provide financial artefacts for tenants, counters, and audit with statement visibility of dues.

### Actors
- Accounts/Revenue officers, Auditor, Tenant (portal downloads via F05-009)

### User Journey
1. On successful payment, system issues digital receipt (number series).
2. Officer/tenant views payment history.
3. Officer generates outstanding statement for a tenant/lease/property as of date.
4. PDFs archived in Module 08.

### Functional Capabilities
- Auto receipt PDF generation
- Receipt series from F02-011
- Payment history register
- Outstanding statement by tenant/lease/property
- Re-print/download with watermark controls
- Excel export of history/outstanding

### Inputs
- Payment id / party / as-of date filters

### Outputs
- Receipt PDF; statement PDF/Excel; history lists

### Business Rules
- Outstanding, collection %, and ageing reports reconcile to transaction ledgers (M4-AC5) — statements must match demand−credit−allocation math.
- Receipt immutable after issue; cancellations via linked credit/reversal docs.

### Validations
- Valid payment reference for receipt
- Scope checks on party access

### Calculations
- Statement lines: opening, demands, credits, payments, closing balance

### Workflow
N/A (document generation).

### Search Requirements
Receipts by number, tenant, date, mode; statements generation filters.

### Documents
Receipts & statements in Module 08.

### Reports
Payment History; Outstanding Statement; feeds Module 11 collection %.

### Notifications
Email receipt optional (Module 09).

### Security
RBAC; tenant only own docs; audit reprints.

### Integrations
Internal DMS (Simple).

### Dependencies
F05-004–006; F02-011; Module 08/09; F05-009

### Assumptions
- Collection % dashboards are Module 11; this provides source statements/registers.

### Risks
- Rounding differences vs GST lines — freeze rounding policy.

### Non Functional Requirements
- Fast PDF generation; printable counter copy

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Receipt view/print & payment history | UI | Complex | 8 |
| Outstanding statement screens | UI | Complex | 8 |
| Receipt & statement generate ops | API | Complex | 8 |
| Receipt series entities | Database | Easy | 2 |
| DMS receipt archive handoff | Integration | Simple | 4 |
| Receipts/statements tests | Testing | Complex | 8 |
| Receipts & statements guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- Two Complex UIs: history/receipts and statements.
