# F02-003 — Notification Templates & System Parameters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Notification Templates & System Parameters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain reusable notification wording and configurable housing policy parameters.

### Business Objective
Allow approved business wording and timelines to change without code modification.

### Actors
Super Administrator; authorised section administrator; Auditor.

### User Journey
Administrator selects a template or parameter, edits approved content/value, validates it, activates it, and reviews history.

### Functional Capabilities
SMS/email/portal template maintenance; parameters for 90-day balance period, 130-day auto-cancel and 10% refund deduction; version/status history.

### Inputs
Template channel, event, subject/body; parameter name, value, effective status.

### Outputs
Active template/parameter configuration and audit history.

### Business Rules
Only active approved values are consumed; changes apply prospectively unless owning process rules state otherwise; parameter names are controlled.

### Validations
Mandatory placeholders/content; numeric/range checks for policy values; unique active template per event/channel.

### Calculations
None.

### Workflow
Maintain draft → validate/approve as configured → activate → downstream process consumes value.

### Search Requirements
Channel, event, parameter, status, effective date.

### Documents
None.

### Reports
Template and Parameter Configuration exports.

### Notifications
Optional notice to administrators when a policy parameter changes.

### Security
Restricted editors; sensitive policy changes auditable.

### Integrations
Internal notification service handoff (Simple).

### Dependencies
Module 01; Module 12 for dispatch.

### Assumptions
Template dispatch mechanics are not included here.

### Risks
Unapproved wording or parameter changes may affect citizen commitments.

### Non Functional Requirements
Version traceability; safe rendering of template content.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Template and parameter register | UI | Complex | 8 |
| Template editor and parameter administration | UI | Very High | 16 |
| Template/parameter operations | API | Complex | 8 |
| Configuration/version persistence | Database | Complex | 6 |
| Notification configuration handoff | Integration | Simple | 4 |
| Template and parameter tests | Testing | Very High | 12 |
| Template/parameter guide | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
