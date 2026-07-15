# F03-003 — Project Publish Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Project Publish Approval |
| **Module** | 03 — Housing Project Management |

### Description
Route project creation and major changes through configured approval before publication.

### Business Objective
Ensure only authorised, complete projects become visible to citizens.

### Actors
Engineering Section; configured Approvers; Citizen (published view consumer); Auditor.

### User Journey
Officer submits a project for approval; approvers review, act with remarks, and on approval an authorised officer publishes or unpublishes it.

### Functional Capabilities
Submit/review approval queue; approve/reject/send back/hold/clarification as configured; publish/unpublish control; status history; citizen-visibility flag.

### Inputs
Project reference, approval remarks, decision, publish action, effective status.

### Outputs
Approval outcome, published project status, history.

### Business Rules
Publication requires successful configured approval; unpublished/rejected projects remain hidden from citizens; major changes follow configured approval.

### Validations
Complete mandatory project details; required documents where configured; valid approver action/remarks.

### Calculations
None.

### Workflow
Draft → submit → configured multi-level review → approved → publish; rejection/send-back returns to officer.

### Search Requirements
Project, approval status, approver, published status, date range.

### Documents
Relevant project documents from F03-002 are available during review.

### Reports
Project Approval and Publication Register.

### Notifications
Configured alerts for submission, pending approval, decision and publication.

### Security
RBAC, SoD, approval audit, publish authority restriction.

### Integrations
Internal workflow routing (Simple); notification service handoff (Simple).

### Dependencies
F02-004; F01-003; F01-007; F03-001/002.

### Assumptions
Citizen portal display is owned by Module 06; this feature controls eligibility only.

### Risks
Incomplete approver mapping can hold publication.

### Non Functional Requirements
Auditable state transitions; timely queue visibility.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Project approval queue | UI | Complex | 8 |
| Project review and publish control screen | UI | Very High | 16 |
| Project approval/publish operations | API | Very High | 16 |
| Approval and publication persistence | Database | Complex | 6 |
| Workflow routing handoff | Integration | Simple | 4 |
| Notification handoff | Integration | Simple | 4 |
| Project approval tests | Testing | Very High | 12 |
| Project publish guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
