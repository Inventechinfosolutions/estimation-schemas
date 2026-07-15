# F07-004 — CA Renewal, Cancellation & Breach
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | CA Renewal, Cancellation & Breach |
| **Module** | 07 — CA Site Management |
### Description
Manage renewal requests, cancellation decisions, breach notices, and closure of a CA allotment/lease/assignment.
### Business Objective
Maintain a controlled CA lifecycle and prevent expired or breached cases from remaining incorrectly occupied.
### Actors
CA Officer; inspector/section user; approvers; institutional representative; Auditor.
### User Journey
Officer identifies an expiring or non-compliant agreement, creates a renewal/cancellation/breach case, records notice and evidence, obtains approval, then updates the agreement and site occupancy outcome.
### Functional Capabilities
Lifecycle worklist, renewal request form, breach-notice tracker, approval timeline, closure/availability outcome.
### Inputs
Current agreement, event type, compliance evidence, notice date, proposed renewal terms, reason, and approval remarks.
### Outputs
Renewed term, approved cancellation/breach outcome, notices, and revised CA status.
### Business Rules
Only current CA agreements can renew or close; no extension without approval; cancellation/breach retains historic agreement and notices.
### Validations
Valid lifecycle event, required evidence/reason, no overlapping open lifecycle case, and approved effective date.
### Calculations
Days to expiry, notice aging, and revised expiry date.
### Workflow
Active → renewal/cancellation/breach initiated → review/approval → renewed, closed, or released.
### Search Requirements
CA site, institution, agreement, expiry range, event type, breach status.
### Documents
Renewal request, compliance certificate, breach notice, cancellation order.
### Reports
Expiring agreements, breach pendency, and closed CA cases.
### Notifications
Expiry reminders and case outcomes through Module 11.
### Security
High-impact CA role restriction and full history.
### Integrations
Internal CA/site status update (Simple).
### Dependencies
F07-003, F07-005, Modules 02 and 11.
### Assumptions
BDA defines renewal windows and breach decision criteria.
### Risks
Delayed decisions may cause unauthorized continued occupancy.
### Non Functional Requirements
Reliable date alerts, auditability, secure evidence access.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Expiry/breach worklist | UI | Complex | 8 |
| Lifecycle case and notice screens | UI | Very High | 16 |
| Renewal/closure approval processing | API | Very High | 16 |
| Lifecycle event persistence | Database | Complex | 6 |
| Site-status update | Integration | Simple | 4 |
| Renewal and breach tests | Testing | Very High | 12 |
| Lifecycle guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
