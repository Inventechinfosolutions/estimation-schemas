# F08-002 — Land Loser Verification, Approval & Publish
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F08-002 |
| **Feature Name** | Land Loser Verification, Approval & Publish |
| **Module** | 08 — Land Loser Management |
### Description
Verify proposal references and documents, route the case through configured multi-level approval, and publish effective Land Loser status to the site master.
### Business Objective
Ensure only verified, authorised Land Loser records become visible for downstream BDA use.
### Actors
Land Acquisition Verifier; Legal User; configured approvers; Auditor.
### User Journey
Verifier reviews the proposal and evidence, records findings or returns it for correction; approvers decide with remarks; final approval publishes the effective status and complete history to the site record.
### Functional Capabilities
Verification worklist, evidence-review screen, approval timeline, publish confirmation, and effective register.
### Inputs
Proposal, verifier findings, document evidence, approver decisions, and publication date.
### Outputs
Approved/rejected/returned case, effective site status, and approval history.
### Business Rules
Only approved cases become effective; returned/rejected cases cannot be consumed downstream; publishing keeps acquisition evidence linked to the site.
### Validations
Verification decision and mandatory findings; required approval levels; valid current site; no conflicting effective marking.
### Calculations
Verification/approval pendency and effective Land Loser counts.
### Workflow
Submitted → verified/returned → multi-level approval → published effective or rejected.
### Search Requirements
Site, proposal, acquisition reference, verification status, approver, publication date.
### Documents
Verified acquisition evidence, legal remarks, approval documents.
### Reports
Effective Land Loser register and approval-pendency report.
### Notifications
Return, approval task, and effective-status notifications via Module 11.
### Security
Verifier/approver segregation, sensitive beneficiary evidence restrictions, full audit.
### Integrations
Internal site-master status publication (Simple).
### Dependencies
F08-001, Modules 02, 04, 11.
### Assumptions
Approval routing is configured in Module 02.
### Risks
Incorrect publish action can affect downstream eligibility and reporting.
### Non Functional Requirements
Complete history, idempotent publish, secure evidence access.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Verification worklist and evidence view | UI | Complex | 8 |
| Approval timeline and publish confirmation | UI | Very High | 16 |
| Verification, approval and publication processing | API | Very High | 16 |
| Verification/approval history persistence | Database | Complex | 6 |
| Site-master publication | Integration | Simple | 4 |
| Approval/publish tests | Testing | Very High | 12 |
| Verification guide | Documentation | Complex | 4 |
| **Total** | | | **66** |
