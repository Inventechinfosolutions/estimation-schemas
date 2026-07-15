# F04-002 — Unit Pricing & Charges

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Unit Pricing & Charges |
| **Module** | 04 — Flats & Villas Inventory & Status |

### Description
Maintain per-unit base price, booking amount, GST, registration, maintenance, and other applicable charges with total cost.

### Business Objective
Present controlled, traceable unit financials for notifications, booking, and payment.

### Actors
Engineering Section; Accounts Section; Approvers; Auditor.

### User Journey
Authorised officer opens a unit financials view, enters or updates applicable amounts, reviews total cost, and submits changes according to status controls.

### Functional Capabilities
Per-unit price and charge entry; configurable charge selection; total display; financial history; pricing export.

### Inputs
Unit reference, base price, booking amount, GST, registration, maintenance, other charges.

### Outputs
Unit financial summary, total cost, Unit Pricing Register.

### Business Rules
Total cost is the sum of applicable configured components; changes after publish follow F04-005 where configured; payment posting remains Module 08.

### Validations
Required base/booking amounts where applicable; non-negative values; active charge selections only.

### Calculations
Total cost is calculated as base price plus all applicable unit charges.

### Workflow
Maintain financials → validate/calculation → save or route post-publish change for approval.

### Search Requirements
Project, unit, price range, booking amount, charge type, status.

### Documents
None.

### Reports
Unit Pricing and Charges Register.

### Notifications
Optional alerts for approved post-publish financial change.

### Security
Accounts/Engineering permission separation; financial change audit.

### Integrations
None.

### Dependencies
F02-002; F04-001; F04-005.

### Assumptions
Tax rules are entered/configured values; no external tax engine is included.

### Risks
Incorrect price or charges affect citizen commitment and payment values.

### Non Functional Requirements
Accurate calculations; monetary display consistency; auditability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Unit pricing register + filters | UI | Complex | 8 |
| Unit financials and charge editor | UI | Complex | 8 |
| Pricing and charge operations | API | Complex | 8 |
| Unit financial persistence | Database | Complex | 6 |
| Unit pricing tests | Testing | Very High | 12 |
| Unit pricing guide | Documentation | Medium | 3 |
| **Total** | | | **45** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
