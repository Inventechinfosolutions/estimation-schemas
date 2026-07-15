# F10-003 — Auto-Cancellation for Non-Payment

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-003 |
| **Feature Name** | Auto-Cancellation for Non-Payment |
| **Module** | 10 — Cancellation Refund Auto Cancellation |

### Description
Evaluate active bookings against the configurable non-payment threshold and automatically cancel eligible unpaid bookings without a manual decision step.

### Business Objective
Enforce BDA payment timelines consistently and return non-compliant bookings to the cancellation/release process.

### Actors
System; Housing Officer; Accounts Officer; Citizen; Auditor.

### User Journey
The scheduled process identifies bookings that remain unpaid beyond the configured threshold, verifies that no valid exception or completion condition applies, records the auto-cancellation reason, updates the booking state, starts inventory release, and notifies the citizen.

### Functional Capabilities
- Scheduled eligibility evaluation, candidate preview, auto-cancellation execution, and exception/suppression view.
- Reason code “Auto Cancellation – Non-payment”, history, and downstream inventory-release handoff.
- Operational register for processed, skipped, and failed cases.

### Inputs
Active booking, payment ledger, configured auto-cancellation days, due status, permitted hold/exception indicator, and processing time.

### Outputs
Auto-cancellation record, cancelled booking, inventory-release event, notification event, and processing audit.

### Business Rules
Default threshold is 130 days from booking but is configurable; auto-cancel runs only when the configured non-payment condition is met; valid full payment, approved hold, or excluded lifecycle state prevents cancellation; no manual approval is required for the configured automated rule.

### Validations
Active booking state, authoritative payment balance, valid parameter, eligibility date, no approved exemption, and idempotent run processing.

### Calculations
Eligibility date = booking date plus configured auto-cancellation days; days overdue and unpaid balance at evaluation.

### Workflow
Active unpaid booking → threshold reached → eligibility validated → auto-cancelled → unit release initiated → citizen notified → refund policy outcome where applicable.

### Search Requirements
Booking, citizen, project, unit, threshold date, unpaid balance, auto-cancel run date, result, and exception reason.

### Documents
Auto-cancellation notice and processing evidence; no separate primary attachment required.

### Reports
Auto-cancellation register, candidate ageing, skipped/exempt cases, and run exception report.

### Notifications
Auto-cancellation notice and internal processing alert through Module 12.

### Security
Scheduler actions are system-audited; exception/suppression management is restricted; citizens cannot alter auto-cancellation records.

### Integrations
Dues/ledger consumption (Medium), inventory-release handoff (Medium), and notification handoff (Easy).

### Dependencies
Module 02 parameters; F08-001, F08-004, F10-004; Modules 04, 07, 08, and 12.

### Assumptions
Approved exceptions/holds are captured by BDA policy; scheduler infrastructure is part of application delivery.

### Risks
Incorrect parameters or delayed payment-status updates could cancel an eligible booking incorrectly.

### Non Functional Requirements
Reliable scheduled execution, idempotency, controlled recovery, and audit-grade run history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Auto-cancellation register and exception UI | UI | Complex | 8 |
| Scheduled eligibility and cancellation processing | API | Very High | 16 |
| Run, exception, and cancellation persistence | Database | Complex | 6 |
| Ledger, inventory, and notification handoffs | Integration | Medium | 16 |
| Auto-cancellation rule tests | Testing | Very High | 12 |
| Auto-cancellation operations guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
The automatic rule is estimated within this module; payment gateway connector and notification transport remain in Modules 13 and 12.
