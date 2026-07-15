# F10-004 — Inventory Release & Notifications Handoff

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-004 |
| **Feature Name** | Inventory Release & Notifications Handoff |
| **Module** | 10 — Cancellation Refund Auto Cancellation |

### Description
Coordinate the post-cancellation release of a unit back to available inventory and issue the relevant citizen and internal notification events while preserving the cancelled booking history.

### Business Objective
Make cancelled inventory safely available again without losing cancellation/refund traceability or exposing inconsistent availability.

### Actors
System; Housing/Estate Officer; Citizen; Auditor.

### User Journey
After voluntary approval or auto-cancellation, the release process verifies the cancellation outcome, changes the unit from its active booked state to available, records the release event, updates portal availability through the inventory flow, and sends notices.

### Functional Capabilities
- Release-pending queue, release confirmation/status, and failed-handoff exception handling.
- Cancellation-to-inventory status transition evidence and portal-availability refresh event.
- Citizen/internal notice event generation with linked cancellation context.

### Inputs
Approved or auto-cancellation record, current booking/unit status, release eligibility, notification template/event context, and exception remarks.

### Outputs
Unit available status, inventory-release audit, portal visibility refresh event, and notification events.

### Business Rules
Only a completed approved or automatic cancellation can release a unit; release occurs once per cancelled booking; refund processing status does not block inventory release unless BDA configures otherwise; prior booking history remains linked to the unit.

### Validations
Eligible cancellation outcome, matching active unit/booking, no prior release event, permissible inventory transition, and notification recipient/event availability.

### Calculations
Time from cancellation to inventory release and failed-handoff ageing.

### Workflow
Cancellation completed → release eligibility verified → unit Available → portal inventory refreshed → citizen/internal notices → release complete or exception.

### Search Requirements
Cancellation, booking, unit, project, release date, release result, portal visibility, and handoff exception status.

### Documents
Cancellation outcome and release evidence; no separate unit document required.

### Reports
Inventory release register, release turnaround, returned-available inventory, and handoff exception report.

### Notifications
Cancellation completion, inventory release internal alert, and citizen-facing outcome notice through Module 12.

### Security
Only authorised/system transitions can release inventory; no exposure of prior citizen identity in public inventory; release events are immutable and audited.

### Integrations
Inventory/status handoff to Module 04 (Medium) and notification-service handoff to Module 12 (Easy).

### Dependencies
F10-001, F10-003, Modules 04, 05, 07, and 12.

### Assumptions
Module 04 remains authoritative for unit lifecycle status and Module 05 controls public notification visibility rules.

### Risks
A failed inventory handoff can leave a cancelled unit unavailable or expose it prematurely.

### Non Functional Requirements
Reliable at-most-once release, visible exception recovery, prompt citizen-portal availability refresh, and complete auditability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Release queue and handoff exception UI | UI | Complex | 8 |
| Release validation and transition processing | API | Complex | 8 |
| Release event and exception persistence | Database | Medium | 4 |
| Inventory and notification handoffs | Integration | Medium | 16 |
| Inventory release tests | Testing | Complex | 8 |
| Release handoff guide | Documentation | Medium | 3 |
| **Total** | | | **47** |

### Estimation Assumptions
This feature coordinates cancellation release; it does not implement independent inventory management or notification delivery.
