# F08-004 — Payment Due Reminders

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-004 |
| **Feature Name** | Payment Due Reminders |
| **Module** | 08 — Online Payment Management |

### Description
Identify upcoming and overdue booking dues from the payment ledger and trigger configured reminder events for delivery through the notification service.

### Business Objective
Encourage timely balance payment before escalation to the non-payment auto-cancellation process.

### Actors
System; Citizen; Accounts Officer; Housing Officer; Auditor.

### User Journey
The scheduled reminder process reviews open dues against configured reminder windows, creates eligible reminder events, sends them through Module 12, and exposes delivery/outcome history to authorised officers.

### Functional Capabilities
- Upcoming/overdue due queue, reminder eligibility view, and suppressed/failed-event review.
- Configurable reminder schedule consumption and duplicate-send prevention.
- Citizen-facing due context in reminder links.

### Inputs
Open dues, due dates, booking/citizen contact context, configured reminder windows, and delivery outcome.

### Outputs
Reminder events, delivery history, due-ageing view, and unresolved delivery exception.

### Business Rules
Reminders are sent only for active unpaid/part-paid eligible dues; a given reminder stage is not duplicated for the same due unless re-trigger policy permits; reminders do not alter payment or booking status.

### Validations
Active booking, valid due amount/date, configured reminder stage, available citizen contact, and no prior equivalent reminder.

### Calculations
Days to due, days overdue, reminder-stage eligibility, and reminder delivery counts.

### Workflow
Open due → reminder window reached → reminder event queued → delivered/failed/suppressed → next eligible stage or payment closure.

### Search Requirements
Booking, citizen, project, due date, payment head, reminder stage, delivery status, and overdue age.

### Documents
No primary document; delivery logs and due notices are retained as process evidence.

### Reports
Due reminder register, overdue ageing, and failed-delivery exception report.

### Notifications
SMS/email/portal reminder delivery is performed by Module 12.

### Security
Citizen contact details are protected; reminder queues are restricted to authorised operations/Accounts roles; no sensitive financial data beyond approved notice content.

### Integrations
Ledger due consumption (Medium) and notification-service handoff (Easy).

### Dependencies
F08-001; Module 02 parameters; Module 12; F10-003.

### Assumptions
Reminder lead times and templates are maintained by BDA configuration; escalation/cancellation decision remains Module 10.

### Risks
Incorrect contact details or excessive reminders can reduce citizen trust.

### Non Functional Requirements
Reliable scheduled execution, duplicate prevention, delivery traceability, and scalable batch handling.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Reminder queue and ageing/exceptions UI | UI | Complex | 8 |
| Due eligibility and reminder scheduling processing | API | Very High | 16 |
| Reminder event and suppression persistence | Database | Complex | 6 |
| Ledger and notification-service handoffs | Integration | Medium | 16 |
| Reminder schedule tests | Testing | Very High | 12 |
| Reminder operations guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
Notification transport is owned by Module 12; this feature estimates due qualification and event handoff only.
