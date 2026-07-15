# F12-002 — SMS Dispatch Service

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F12-002 |
| **Feature Name** | SMS Dispatch Service |
| **Module** | 12 — Notification Service |

### Description
Dispatch BDA-approved SMS messages for OTP, booking, payment, cancellation, refund, NOC, and other configured BHMS events.
### Business Objective
Provide timely mobile alerts for time-sensitive citizen and officer actions.
### Actors
- System; Citizen; BDA officers; Super Administrator
### User Journey
1. A source process raises a configured event. 2. BHMS renders an SMS template and sends it through the approved provider. 3. Delivery outcome is logged.
### Functional Capabilities
- Template rendering, recipient resolution, queued dispatch, delivery outcome capture, and provider-failure handling.
### Inputs
- Template, mobile number, event reference, merge values, and priority.
### Outputs
- SMS dispatch result, provider reference, and exception status.
### Business Rules
- Only approved templates and opted-in/legally permitted recipients are used.
### Validations
- Mobile format, template completeness, recipient eligibility, and provider response.
### Calculations
- Source-defined notification counts and delivery statuses only.
### Workflow
- Queued → sent → delivered/failed.
### Search Requirements
- By mobile, source reference, template, date, and delivery status.
### Documents
- No standalone document; source-linked artefacts remain in business modules.
### Reports
- SMS dispatch and failure summary.
### Notifications
- SMS is the notification channel implemented by this feature.
### Security
- RBAC, protected recipient contact details, citizen ownership isolation, and auditable operational access.
### Integrations
- One BDA-approved SMS provider.
### Dependencies
- Modules 02–11; F12-005/F12-006; provider credentials.
### Assumptions
- One provider and approved sender/template registration at go-live.
### Risks
- Provider regulatory approval or delivery latency can affect launch communications.
### Non Functional Requirements
- Asynchronous dispatch, retry-safe correlation, and protected contact data.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| SMS dispatch configuration and status view | UI | Easy | 4 |
| SMS composition and dispatch operations | API | Complex | 8 |
| SMS delivery state | Database | Medium | 4 |
| SMS provider integration | Integration | Medium | 16 |
| SMS dispatch tests | Testing | Complex | 8 |
| SMS dispatch guide | Documentation | Medium | 3 |
| **Total** | | | **43** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. One provider and approved sender/template registration at go-live.
