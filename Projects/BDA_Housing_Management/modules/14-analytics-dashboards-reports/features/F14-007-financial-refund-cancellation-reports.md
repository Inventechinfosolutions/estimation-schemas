# F14-007 — Financial, Refund & Cancellation Reports

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-007 |
| **Feature Name** | Financial, Refund & Cancellation Reports |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Provide specialized financial reports for revenue, collections, outstanding balances, refunds, voluntary cancellations, auto-cancellations, and related exceptions.
### Business Objective
Support Accounts, management, and audit review of financial exposure and housing lifecycle reversals.
### Actors
- Accounts Section; senior authority; Auditor
### User Journey
1. Authorized user selects a financial/refund/cancellation report. 2. BHMS applies project/date/status filters. 3. Results reconcile to payment and cancellation/refund source records.
### Functional Capabilities
- Revenue and collection reporting, outstanding analysis, refund status, cancellation/auto-cancellation registers, and exception views.
### Inputs
- Project/date/payment-head/status filters and payment/refund/cancellation records.
### Outputs
- Financial and lifecycle report results with aggregate totals and details.
### Business Rules
- Financial reports use verified payment/refund statuses; no general-ledger replacement is included.
### Validations
- Role, project/date filters, valid source statuses, and authorized sensitive-data access.
### Calculations
- Paid, pending, refunded, cancelled, outstanding, and period totals from source records.
### Workflow
- Select report → filter → retrieve → reconcile/export.
### Search Requirements
- By project, payment head, date, refund status, cancellation type, and outstanding age.
### Documents
- Source receipts/refund/cancellation evidence when authorized.
### Reports
- Financial/refund/cancellation report pack.
### Notifications
- No independent notifications.
### Security
- Restricted Accounts/Auditor access, protected financial data, and export audit trail.
### Integrations
- Internal BHMS financial source data.
### Dependencies
- Modules 08, 10, F13-001, F14-001, and F14-008.
### Assumptions
- Gateway and refund statuses have been reconciled in their owning processes.
### Risks
- Unmatched gateway or incomplete refund records can affect report acceptance.
### Non Functional Requirements
- Accurate period filtering, export consistency, and reconciliation to source registers.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Filterable report workspace | UI | Very High | 16 |
| Report retrieval and aggregation operations | API | Complex | 8 |
| Report query and aggregation support | Database | Medium | 4 |
| Report tests | Testing | Complex | 8 |
| Report guide | Documentation | Complex | 4 |
| **Total** | | | **40** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Report UI is Very High (16); accounting ledger replacement is excluded.
