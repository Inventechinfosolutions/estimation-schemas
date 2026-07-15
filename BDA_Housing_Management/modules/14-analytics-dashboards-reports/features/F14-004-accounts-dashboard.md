# F14-004 — Accounts Dashboard

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-004 |
| **Feature Name** | Accounts Dashboard |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Present booking and balance collections, pending payments, refunds pending/completed, daily/monthly collections, revenue summary, and payment exceptions.
### Business Objective
Give Accounts reconciled visibility of housing cashflow and outstanding actions.
### Actors
- Accounts Section; senior authority; Auditor
### User Journey
1. Accounts Section selects the permitted dashboard. 2. BHMS applies authorized filters and presents reconciled KPIs. 3. The user drills to an authorized register where required.
### Functional Capabilities
- Role-based navigation, KPI cards, filters, trends/distributions, and permitted source-register drill-through.
### Inputs
- Date/project/payment-head filters and payment/refund records.
### Outputs
- Accounts KPI views, pending lists, and permitted reconciliation drill-through.
### Business Rules
- Dashboard values reflect verified source payment/refund statuses and do not replace accounting processes.
### Validations
- Authorized Accounts role, date range, and source-status consistency.
### Calculations
- KPI totals, balances, counts, and trends are calculated only from source records.
### Workflow
- Open view → apply filters → review KPIs → drill through.
### Search Requirements
- By authorized project, area, date, lifecycle status, and KPI dimension.
### Documents
- No standalone documents; links are controlled by source processes.
### Reports
- Dashboard KPI and filtered operational visibility.
### Notifications
- No independent notifications; source alerts remain in Module 12.
### Security
- RBAC, least-privilege access, protected sensitive values, and auditable activity.
### Integrations
- Internal BHMS data services.
### Dependencies
- Modules 08 and 10, F13-001, and F14-001.
### Assumptions
- Gateway reconciliation outcomes are available from the payment process.
### Risks
- Incomplete or inconsistent source statuses can affect KPI acceptance.
### Non Functional Requirements
- Near-real-time refresh, expected-volume performance, and KPI-to-register reconciliation.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Role-based dashboard workspace | UI | Very High | 16 |
| KPI retrieval and authorized drill-through operations | API | Complex | 8 |
| Dashboard aggregation support | Database | Medium | 4 |
| Dashboard tests | Testing | Complex | 8 |
| Dashboard guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Dashboard UI is Very High (16).
