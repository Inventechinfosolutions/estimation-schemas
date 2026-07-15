# F10-001 — Voluntary Cancellation Request & Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-001 |
| **Feature Name** | Voluntary Cancellation Request & Approval |
| **Module** | 10 — Cancellation Refund Auto Cancellation |

### Description
Capture a citizen’s request to cancel an eligible booking, route it through configured approval, preserve reasons/documents, and create the approved cancellation outcome.

### Business Objective
Apply BDA cancellation policy consistently while retaining a complete record before inventory release and refund processing.

### Actors
Citizen; Housing/Estate Officer; Configured Approver; Accounts Officer; Auditor.

### User Journey
A citizen requests cancellation from an eligible personal booking, states the reason and attaches evidence if required; an officer reviews the request and routes it for approval; on approval the booking is cancelled and downstream release/refund actions are created.

### Functional Capabilities
- Citizen cancellation request, eligibility guidance, reason capture, and status tracking.
- Officer review/clarification and configured approval worklist.
- Cancellation outcome, audit history, and downstream inventory/refund handoff.

### Inputs
Active booking, citizen reason, supporting documents, officer remarks, approver action, and configured cancellation policy.

### Outputs
Cancellation request, approval history, cancelled-booking outcome, and release/refund work items.

### Business Rules
Cancellation is allowed only before sale deed execution and within configured policy; approval is required; cancelled booking retains history and does not erase prior payment/letter records; refund is calculated separately.

### Validations
Citizen ownership, eligible booking state, required reason/documents, approver authority, and mandatory remarks for reject/send-back/hold.

### Calculations
Cancellation request ageing and approval pendency; refund calculation is F10-002.

### Workflow
Citizen request → review/clarification → configured approval → approved cancellation/rejected → inventory release and refund initiation.

### Search Requirements
Cancellation reference, booking, citizen, project, unit, request date, reason, approval stage, and status.

### Documents
Cancellation request evidence, approval note, citizen communication, and cancellation outcome.

### Reports
Cancellation register, approval pendency, cancellation reasons, and pending-refund handoff report.

### Notifications
Request acknowledgement, clarification, approval/rejection, and cancellation outcome via Module 12.

### Security
Citizen ownership restriction, maker-checker approval, role-based internal views, and immutable cancellation history.

### Integrations
Workflow consumption (Medium), booking/inventory handoff (Medium), and notification handoff (Easy).

### Dependencies
Modules 02, 04, 07, 08, 12; F10-002 and F10-004.

### Assumptions
Legal dispute/court case management is out of scope; BDA defines eligible cancellation policy.

### Risks
Cancellation requests after an ineligible lifecycle stage may require manual policy escalation.

### Non Functional Requirements
Clear citizen status, reliable workflow transitions, and audited preservation of cancellation evidence.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Citizen request and officer review/approval UI | UI | Very High | 16 |
| Cancellation eligibility and workflow processing | API | Very High | 16 |
| Cancellation and approval-history persistence | Database | Complex | 6 |
| Workflow, booking/inventory, and notification handoffs | Integration | Medium | 16 |
| Cancellation approval tests | Testing | Very High | 12 |
| Cancellation process guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
Workflow configuration is Module 02; this feature estimates the runtime cancellation process, not refund computation or payment payout.
