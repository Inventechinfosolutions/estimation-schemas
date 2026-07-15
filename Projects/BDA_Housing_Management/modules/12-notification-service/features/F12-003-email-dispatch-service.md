# F12-003 — Email Dispatch Service

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F12-003 |
| **Feature Name** | Email Dispatch Service |
| **Module** | 12 — Notification Service |

### Description
Dispatch email acknowledgements and notices for BHMS process events using configured BDA templates.
### Business Objective
Provide an alternative durable communication channel for citizens and officers.
### Actors
- System; Citizen; BDA officers; Super Administrator
### User Journey
1. A configured process event triggers email preparation. 2. BHMS renders the template and submits it to the mail service. 3. Status is logged for operational review.
### Functional Capabilities
- Template rendering, recipient resolution, attachment/link handling, asynchronous dispatch, and failure visibility.
### Inputs
- Template, recipient email, event reference, merge values, and permitted attachment/source link.
### Outputs
- Email dispatch result, provider reference, and exception status.
### Business Rules
- Sensitive documents are shared only through authorized links or approved attachments.
### Validations
- Email address, template completeness, attachment eligibility, and provider response.
### Calculations
- Source-defined notification counts and delivery statuses only.
### Workflow
- Queued → sent → delivered/failed.
### Search Requirements
- By recipient, source reference, template, date, and delivery status.
### Documents
- Approved source-linked notices or download links.
### Reports
- Email dispatch and failure summary.
### Notifications
- Email dispatch outcome; process alerts may additionally use in-app/SMS.
### Security
- RBAC, protected recipient contact details, citizen ownership isolation, and auditable operational access.
### Integrations
- One BDA-approved email service.
### Dependencies
- Modules 02–11; F12-005/F12-006; mail-service credentials.
### Assumptions
- One approved outbound service and verified BDA sender domain.
### Risks
- Sender-domain or provider limits can delay delivery.
### Non Functional Requirements
- Asynchronous delivery, protection from unauthorized document disclosure, and traceable status.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Email dispatch configuration and status view | UI | Easy | 4 |
| Email composition and dispatch operations | API | Complex | 8 |
| Email delivery state | Database | Medium | 4 |
| Email service integration | Integration | Medium | 16 |
| Email dispatch tests | Testing | Complex | 8 |
| Email dispatch guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. One approved outbound service and verified BDA sender domain.
