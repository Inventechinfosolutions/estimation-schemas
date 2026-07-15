# F01-006 — Login History & Access Audit

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F01-006 |
| **Feature Name** | Login History & Access Audit |
| **Module** | 01 — User & Role Management |

### Description
Provide searchable, non-editable records of login/logout and privileged access activity, including the **Post** and **Role** used for the session.

### Business Objective
Support security monitoring and accountability under the Person–Post–Role model.

### Actors
Super Administrator; Auditor; authorised security officer.

### User Journey
Reviewer filters by period, Person, Post, Role, or outcome; inspects events; exports for review.

### Functional Capabilities
- Record login/logout, failed authentication, timeout, post-switch, privileged access  
- Searchable register with Person / Post / Role context  
- Event detail and export  

### Inputs
Event type, Person, Post, Role, timestamp, source context, outcome.

### Outputs
Access Audit Register and filtered export.

### Business Rules
Audit records are non-editable; exports limited to authorised Roles; retention follows BDA policy.

### Validations
Date range required for broad exports; permitted viewers only.

### Calculations
None.

### Workflow
System records event (with Post context) → reviewer searches/exports → access to audit itself is logged.

### Search Requirements
Person, Post, Role, event type, outcome, date range.

### Documents
None.

### Reports
Login History and Access Audit exports.

### Notifications
Optional alert for repeated failed logins (policy-based).

### Security
Read-only audit access; tamper-resistant records; export audit.

### Integrations
None.

### Dependencies
F01-004; F01-001; F01-003.

### Assumptions
Business transaction audit remains embedded in owning business features.

### Risks
Broad audit access can expose sensitive activity patterns.

### Non Functional Requirements
Scalable filtering; consistent timestamps; export performance.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Login history register + Person/Post filters | UI | Complex | 8 |
| Access-event detail and export controls | UI | Medium | 6 |
| Audit retrieval and export operations | API | Complex | 8 |
| Audit event persistence (incl. Post/Role) | Database | Complex | 6 |
| Audit trail tests | Testing | Very High | 12 |
| Audit review guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Uses Estimation Master values only.  
