# F01-010 — Forensic and login/security audit

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-010 |
| **Feature Name** | Forensic and login/security audit |
| **Module** | 01 — Access Control, Person–Post–Role & Forensic Audit |

### Description
An authorised Administrator or auditor opens the audit register, filters by Person, Post, claim, date or action type, and retrieves who did what, when, on which record, before/after values, and channel (staff web, OOK path). This covers verification, penny-drop, excess-payment, approval, payment, closure, mapping changes, login success/failure and 2FA events.

### Business Objective
Make privileged and security events retrievable for forensic review without granting the auditor the business action itself.

### Actors
Administrator; auditor; (events produced by Officers, CA, OOK claimants, and other modules).

### User Journey
1. Privileged actions and login/security events are written as they occur across modules.
2. Administrator or auditor opens the audit register.
3. They filter by Person, Post, claim, date or action type.
4. They retrieve who, what, when, record, before/after and channel (staff web or OOK path).
5. Payment-specific forensic drill-down on a batch also exists in F08-005 and contributes events here.

### Functional Capabilities
- Central forensic audit register with filters.
- Capture actor Person, Post, timestamp, action, record, before/after, channel.
- Cover verification, penny-drop, excess-payment, approval, payment, closure, mapping, login and 2FA.
- Read-only retrieval for authorised auditor Posts.

### Inputs
Filter criteria (Person, Post, claim, date, action type, channel).

### Outputs
Filtered audit rows; export for authorised auditors.

### Business Rules
- Audit rows are append-only; deactivation of a Person does not delete history.
- Viewing the audit register does not confer rights to perform the original business action.
- OOK channel events are in scope alongside staff web.

### Validations
- Only authorised Administrator/auditor Posts open the register.
- Filters cannot return another officer’s restricted business documents—only audit metadata and authorised fields.

### Calculations
None beyond filter/count of events.

### Workflow
Event ingest (background) → authorised query → retrieve/export. No correction workflow that rewrites history.

### Search Requirements
Person, Post, claim, date range, action type, channel, success/failure for login/2FA.

### Documents
None stored as claim packs; audit may reference document IDs viewed (F01-009).

### Reports
Audit register export. Role/Post mapping reports are F09-007.

### Notifications
None.

### Security
Auditor access is itself audited. Before/after values for credentials must not expose password secrets.

### Integrations
Internal event ingest from claim, identity, penny-drop, approval and payment features.

### Dependencies
All Module 01 features; event producers in Modules 04–08.

### Assumptions
- Payment forensic UI on a batch (F08-005) complements this register rather than replacing it.
- This module estimates the programme forensic store used also by Legal/Valuation identity events.

### Risks
- Incomplete event coverage would fail Key Aspect 3 forensic audit.
- Over-wide auditor export could still leak KYC if payload design is careless.

### Non Functional Requirements
This is the programme-wide identity product consumed by Legal Management and GIS field valuation; staff screens must remain usable during claim windows; privileged actions are attributable to a named Person acting in a Post; primary official hosting identity is an approved government domain, not .org. Privileged actions must be attributable and retrievable within agreed query times for official investigations.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Forensic audit register and filters | UI | Very High | 16 |
| Audit query operations | API | Very High | 16 |
| Audit store and indexes | DB | Very High | 10 |
| Internal event ingest | Integration | Simple | 4 |
| Forensic audit tests | Testing | Very High | 12 |
| Audit retrieval guide | Documentation | Complex | 4 |
| **Total** | | | **62** |

### Estimation Assumptions
- Uses Estimation Master values only.
- UI Very High is the audit register/dashboard, not a simple list.
- Payment-batch forensic screen is additionally estimated in F08-005.
