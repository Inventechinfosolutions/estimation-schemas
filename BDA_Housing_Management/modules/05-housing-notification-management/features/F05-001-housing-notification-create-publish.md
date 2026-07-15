# F05-001 — Housing Notification Create & Publish

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Housing Notification Create & Publish |
| **Module** | 05 — Housing Notification Management |

### Description
Create, approve, and publish public booking notifications for approved housing projects.

### Business Objective
Present complete, approved booking information to citizens during the booking window.

### Actors
Housing/Engineering officers; configured Approvers; Citizens (view); Auditor.

### User Journey
Officer selects an approved project, composes notification content with available-unit summary and policies, attaches/references required material, submits for approval, and publishes after approval.

### Functional Capabilities
Notification draft; project/unit summary; prices/booking amount; required documents; booking window; payment schedule; cancellation/refund policy; terms; approval and publish control.

### Inputs
Project, unit summary, prices, booking amount, required documents, dates, payment schedule, policies, T&Cs.

### Outputs
Published housing notification and citizen-visible booking information.

### Business Rules
Only approved/published projects and eligible inventory may be notified; publication requires configured approval; active window controls visibility.

### Validations
Project eligibility; start/end date sequence; mandatory content/policies; active inventory summary.

### Calculations
None.

### Workflow
Draft → submit → configured approval → publish → active citizen visibility within booking window.

### Search Requirements
Project, notification reference, status, booking dates, publisher, active status.

### Documents
Notification-specific terms and citizen-required-document information embedded in the notification.

### Reports
Housing Notification Register and Published Notification export.

### Notifications
Configured alerts for submission, pending approval, approval and publication.

### Security
RBAC, SoD, audit, citizen read-only access to published content.

### Integrations
Internal workflow routing (Simple); notification service handoff (Simple).

### Dependencies
Modules 03–04; F02-004; Module 06 portal visibility.

### Assumptions
SMS/email campaign dispatch is not included; this feature owns booking-notification content.

### Risks
Incomplete content or stale inventory may mislead citizens.

### Non Functional Requirements
Responsive citizen-readable display; accurate window enforcement; auditability.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Housing notification register + filters | UI | Complex | 8 |
| Notification authoring and publish review screen | UI | Very High | 16 |
| Notification create/publish operations | API | Very High | 16 |
| Notification content/status persistence | Database | Complex | 6 |
| Workflow routing handoff | Integration | Simple | 4 |
| Notification service handoff | Integration | Simple | 4 |
| Notification publication tests | Testing | Very High | 12 |
| Notification publication guide | Documentation | Complex | 4 |
| **Total** | | | **70** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
