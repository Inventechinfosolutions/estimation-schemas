# F08-001 — Payment Dues Ledger & Heads

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Payment Dues Ledger & Heads |
| **Module** | 08 — Online Payment Management |

### Description
Maintain the payable heads, due schedule, paid/balance position, and ledger view for each booking across booking amount, balance, GST, registration charges, maintenance, and other applicable charges.

### Business Objective
Provide one transparent financial position used by citizens, Accounts, reminders, and downstream lifecycle controls.

### Actors
Citizen; Accounts Officer; Housing Officer; Auditor.

### User Journey
After a booking is confirmed, authorised staff review the applicable payment heads and due schedule; the citizen sees payable amounts; settled payments update the ledger and balance position.

### Functional Capabilities
- Booking financial summary, payment-head schedule, due/balance ledger, and accounts review view.
- Configured applicable charges and due-date presentation.
- Controlled adjustments/status explanation through linked business events.

### Inputs
Booking, unit financial components, configured charges, due-period parameters, and settled payment statuses.

### Outputs
Payment-head ledger, total/paid/balance values, due dates, and account position.

### Business Rules
Baseline payment mode is online-only; payment heads reflect applicable configured unit/booking charges; due dates use configured rules; ledger events are traceable and cannot be silently overwritten.

### Validations
Valid booking, active payment head, applicable charge rule, non-negative amounts, and authorised adjustment context.

### Calculations
Total payable, paid amount, outstanding balance, due amount by head, and due-date ageing.

### Workflow
Booking confirmed → heads/schedule established → payment pending/partial/settled → balance due/fully paid.

### Search Requirements
Booking, citizen, project, unit, payment head, due date, outstanding amount, and payment status.

### Documents
Linked receipts and applicable charge support documents.

### Reports
Payment dues ledger, outstanding by head, and booking financial-position register.

### Notifications
This feature supplies due events to Module 12; reminder dispatch is F08-004.

### Security
Citizen sees own ledger only; Accounts adjustments are role-controlled and audited; financial values are protected from unauthorised edit.

### Integrations
Booking/unit financial consumption (Medium) and payment-status hub consumption (Medium).

### Dependencies
Modules 02, 04, 07, and 13; F08-002.

### Assumptions
Charge configuration exists in Module 02; accounting ERP/general ledger replacement is excluded.

### Risks
Unclear charge applicability or rounding policy can produce ledger disputes.

### Non Functional Requirements
Accurate monetary display, traceable changes, and timely ledger refresh after settled payment.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Booking dues ledger and payment-head UI | UI | Complex | 8 |
| Dues and ledger calculation processing | API | Very High | 16 |
| Payment-head and ledger persistence | Database | Complex | 6 |
| Booking financial and payment hub consumption | Integration | Medium | 16 |
| Ledger and due tests | Testing | Very High | 12 |
| Dues ledger guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
Payment gateway connector hours are not included; this feature consumes payment status through the integration hub.
