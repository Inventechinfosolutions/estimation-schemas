# F04-005 — Post-Publish Unit Change Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Post-Publish Unit Change Approval |
| **Module** | 04 — Flats & Villas Inventory & Status |

### Description
Route configured material changes to published unit details, financials, or media through approval before release.

### Business Objective
Protect citizen-facing inventory information after publication.

### Actors
Engineering Section; Accounts Section; configured Approvers; Auditor.

### User Journey
Officer proposes a material change on a published unit, submits it with reason, approvers act, and the approved change is released with a complete history.

### Functional Capabilities
Change request capture; before/after review; configurable approval; approve/reject/send back; controlled release; change history.

### Inputs
Unit, proposed changes, reason, supporting documents, approver remarks.

### Outputs
Change decision, updated published unit data, history.

### Business Rules
Only configured material changes require approval; rejected changes do not alter published data; approved changes preserve prior history.

### Validations
Published unit required; reason mandatory; valid proposed values; required approver decision.

### Calculations
None.

### Workflow
Propose change → configured review → approved release or rejection/send-back → citizen-facing data refreshed by owning publication view.

### Search Requirements
Project, unit, change type, requester, approval status, date range.

### Documents
Supporting files may be attached through the unit record.

### Reports
Post-Publish Unit Change Register.

### Notifications
Configured alerts for submission, pending review and outcome.

### Security
RBAC, SoD, change/approval audit.

### Integrations
Internal workflow routing (Simple); notification service handoff (Simple).

### Dependencies
F02-004; F04-001/002/003; F01-007.

### Assumptions
The feature applies only where BDA configures post-publish approval.

### Risks
Delays in review may leave public details outdated.

### Non Functional Requirements
Auditable before/after values; no unapproved public release.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Post-publish change register | UI | Complex | 8 |
| Change proposal and approval review screen | UI | Very High | 16 |
| Change approval/release operations | API | Very High | 16 |
| Change request/history persistence | Database | Complex | 6 |
| Workflow routing handoff | Integration | Simple | 4 |
| Notification handoff | Integration | Simple | 4 |
| Post-publish change tests | Testing | Very High | 12 |
| Change approval guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
