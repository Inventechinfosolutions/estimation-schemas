# F08-003 — Land Loser Correction & Cancellation
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F08-003 |
| **Feature Name** | Land Loser Correction & Cancellation |
| **Module** | 08 — Land Loser Management |
### Description
Submit and approve controlled corrections or cancellation of a proposed or effective Land Loser marking.
### Business Objective
Correct inaccurate reference/beneficiary information without deleting the original decision trail.
### Actors
Land Acquisition Officer; Legal User; approvers; Auditor.
### User Journey
Officer opens the existing record, chooses correction or cancellation, states the reason, attaches replacement evidence, sends it through approval, and views the resulting amended or withdrawn site status.
### Functional Capabilities
Change-case register, correction form, evidence comparison, approval history, and status outcome.
### Inputs
Existing Land Loser case, change type, reason, corrected references, replacement evidence, approval remarks.
### Outputs
Approved correction/cancellation, superseded history, and revised effective status.
### Business Rules
No record is deleted; effective status changes only after approval; one open correction case per Land Loser record.
### Validations
Existing case, mandatory reason/evidence, valid corrected reference format, no parallel open change request.
### Calculations
Change-case aging and corrected/cancelled counts.
### Workflow
Draft → submitted → verification/approval → corrected effective or cancelled/withdrawn.
### Search Requirements
Site, original case, change type, status, effective date, proposer.
### Documents
Correction justification, replacement acquisition evidence, cancellation order.
### Reports
Correction/cancellation register and audit history.
### Notifications
Approval/outcome notifications via Module 11.
### Security
High-impact action restriction, maker-checker, before/after audit.
### Integrations
Internal site-master status update (Simple).
### Dependencies
F08-002, Modules 02, 04, 11.
### Assumptions
BDA supplies change authority and evidence requirements.
### Risks
Premature cancellation can remove a legitimate downstream eligibility marker.
### Non Functional Requirements
Immutable lineage, protected documents, traceable status update.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Change-case register | UI | Complex | 8 |
| Correction/cancellation and comparison screens | UI | Very High | 16 |
| Controlled change/approval processing | API | Very High | 16 |
| Change lineage persistence | Database | Complex | 6 |
| Site status update | Integration | Simple | 4 |
| Change-control tests | Testing | Very High | 12 |
| Correction guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
