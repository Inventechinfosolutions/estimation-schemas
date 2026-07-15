# F04-006 — Lease Renewal & Termination

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-006 |
| **Feature Name** | Lease Renewal & Termination |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Manage lease renewal and termination/vacating including end-of-term processing, unit return to Vacant, and coordination with deposit settlement and billing stop.

### Business Objective
Close or extend lease lifecycle cleanly so inventory, deposits, and revenue stay consistent.

### Actors
- Estate Officer, Property Manager, Accounts Officer, Approvers

### User Journey
**Renewal:** Expiry alert → initiate renewal → update term/rent → approve → new period active.  
**Termination:** Initiate vacate → clearance checks (dues/deposit) → approve → handover-back → units Vacant → billing stop.

### Functional Capabilities
- Renewal offer/capture with new dates/rent
- Termination/vacating workflow with reason codes
- Pre-clearance: outstanding dues warning (Module 05), deposit path (F04-007)
- Unit status to Vacant; vacancy pipeline fields triggered (Module 03)
- Stop billing commencement / end date for Module 05

### Inputs
- Renewal terms or termination reason, dates, clearances, approvals

### Outputs
- Renewed lease term or closed lease
- Inventory/billing side effects

### Business Rules
- Renewal/expiry alerts lead time configured (paired with F04-008).
- Cannot complete vacate with blocking dues unless approved exception.
- Eviction legal process offline; system supports status/docs/notices only.

### Validations
- Renewal end > new start; termination date rules
- Clearance checklist

### Calculations
Optional prorated rent suggestion (display; billing posts in Module 05).

### Workflow
Renewal and Termination each with approval gates as configured.

### Search Requirements
Expiring leases; pending renewals; terminations in progress.

### Documents
Renewal letters, vacating reports (Module 08).

### Reports
Expiry pipeline; termination register.

### Notifications
Renewal/termination status (Module 09).

### Security
RBAC; audit; approvals.

### Integrations
Events to Modules 03 and 05.

### Dependencies
F04-003–005, F04-007–008; Modules 03, 05, 08, 09

### Assumptions
- Proration posting is Module 05; this feature orchestrates dates/flags.

### Risks
- Vacate without deposit settlement leaves financial open items — enforce checklist.

### Non Functional Requirements
- Expiry queues performant for portfolio size

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Renewal workspace UI | UI | Complex | 8 |
| Termination / vacating wizard | UI | Complex | 8 |
| Renewal & termination operations | API | Complex | 8 |
| Renewal/termination entities | Database | Medium | 4 |
| Renewal/termination tests | Testing | Complex | 8 |
| Renewal & vacating guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Two Complex UIs (renewal + termination) estimated independently.
