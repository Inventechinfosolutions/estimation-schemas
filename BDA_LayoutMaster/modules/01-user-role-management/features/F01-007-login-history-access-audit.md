# F01-007 — Login History & Access Audit
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F01-007 |
| **Feature Name** | Login History & Access Audit |
| **Module** | 01 — User & Role Management |
### Description
Record and retrieve login and access-related activity for officer and citizen accounts.
### Business Objective
Support accountability, security review, and audit evidence.
### Actors
Super Administrator; Auditor; authorised security reviewer.
### User Journey
Reviewer filters access history, opens an event, and exports permitted evidence for review.
### Functional Capabilities
Capture login success/failure, logout, lockout, and privileged access events; search, filter, retain, and export history.
### Inputs
Authentication and access events from LMS functions.
### Outputs
Immutable access audit entries and export.
### Business Rules
Audit entries are retained and cannot be edited by operational users.
### Validations
Valid event source, timestamp, user identity, and permitted query range.
### Calculations
None.
### Workflow
System captures events automatically; reviewers access read-only evidence.
### Search Requirements
User, date range, event type, outcome, role, and source channel.
### Documents
None.
### Reports
Login and access activity report.
### Notifications
Optional alert for repeated failed access attempts.
### Security
Read-only audit access, RBAC, PII minimisation, and protected retention.
### Integrations
Internal authentication service (Simple).
### Dependencies
F01-004 through F01-006; system-wide privileged actions.
### Assumptions
This is application-level logging, not a full SIEM product.
### Risks
Retention requirements may increase storage needs.
### Non Functional Requirements
Tamper-resistant audit trail; searchable within agreed response times.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Audit register and filters | UI | Complex | 8 |
| Event detail view | UI | Medium | 6 |
| Audit capture and retrieval operations | API | Complex | 8 |
| Audit event persistence | Database | Medium | 4 |
| Internal authentication event handoff | Integration | Simple | 4 |
| Audit trail tests | Testing | Complex | 8 |
| Audit review guide | Documentation | Medium | 3 |
| **Total** | | | **41** |
### Estimation Assumptions
Domain approval history remains embedded in its business module.
