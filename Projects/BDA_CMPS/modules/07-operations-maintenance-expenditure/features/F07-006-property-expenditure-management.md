# F07-006 — Property Expenditure Management

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F07-006 |
| **Feature Name** | Property Expenditure Management |
| **Module** | 07 — Operations, Maintenance & Expenditure |

### Description
Post and track property-linked expenditures across configurable categories with vendor, invoice, GST, payment status, documents, and amount-threshold approvals; support property-wise expense reporting (M6-AC5).

### Business Objective
Control and visibility of maintenance and statutory-linked spend per property.

### Actors
- Accounts Officer, Maintenance Officer, Approvers, Auditor

### User Journey
1. Officer creates expense against property/unit with category, vendor, invoice, GST, amount.
2. Attaches documents; links WO/tax payment where applicable.
3. If above threshold, routes approval (F02-009).
4. Updates payment status; reports reconcile to postings (M6-AC5).

### Functional Capabilities
- Categories: Civil, Painting, Plumbing, Electrical, Lift, Housekeeping, Security, Generator, Landscaping, Pest Control, Water, Electricity, Property Tax, Insurance, Miscellaneous (configurable via Module 02)
- Expense CRUD with property/unit linkage
- Vendor, invoice no./date, amount, GST, payment status, documents
- Threshold approval workflow
- Link to WO (F07-005) and tax payments (F06-006)
- Search/export; property-wise expense views

### Inputs
- Category, property, vendor, invoice fields, amounts, GST, docs, links

### Outputs
- Posted expenses; approval tasks; payment status updates

### Business Rules
- Property-wise expense reports match posted expenditure transactions (M6-AC5).
- Approval by amount threshold.
- Full procurement/e-tender out of scope.
- ERP GL push optional Module 10.

### Validations
- Mandatory invoice attrs when category requires
- Duplicate invoice warning per vendor

### Calculations
- GST break-up if entered; totals

### Workflow
Draft → (Approve if threshold) → Posted → Paid/Closed.

### Search Requirements
By property, category, vendor, date, status, amount.

### Documents
Invoices, approvals (Module 08).

### Reports
Expense Register; Property-wise Expense (Module 11).

### Notifications
Approval tasks; payment due internal notes.

### Security
RBAC; SoD maker/checker; audit.

### Integrations
Internal DMS (Simple).

### Dependencies
F02-008/009; F07-004/005; F06-006; Modules 03, 08, 09

### Assumptions
- Testing Very High for finance controls + categories matrix.
- Budget feature separate (F07-007).

### Risks
- Category overlap with utility/tax modules — use links not duplicate amounts blindly.

### Non Functional Requirements
- Excel export; reconcile-able for UAT period

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Expenditure register & filters | UI | Complex | 8 |
| Expense entry form (invoice/GST/docs) | UI | Complex | 8 |
| Approval inbox for threshold expenses | UI | Medium | 6 |
| Expenditure post & approve ops | API | Complex | 8 |
| Expenditure entities | Database | Medium | 4 |
| DMS invoice handoff | Integration | Simple | 4 |
| Expenditure tests | Testing | Very High | 12 |
| Expenditure management guide | Documentation | Medium | 3 |
| **Total** | | | **53** |

### Estimation Assumptions
- Three UI surfaces: register, form, approval inbox.
