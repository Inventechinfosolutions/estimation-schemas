# F09-003 — Candidate and Staff Notifications

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Candidate and Staff Notifications |
| **Module** | 09 — Dashboards, Reports, Notifications and Audit |

### Description
Configure and dispatch lifecycle notifications across SMS, email and portal channels for registration, payment, status, schedule, allocation, hall ticket, reminders, examination credentials, result and certificate events, with templates, channel settings, dispatch console, candidate portal inbox and delivery status tracking.

### Business Objective
Keep candidates and staff informed at each critical examination lifecycle stage through Department-approved channels.

### Actors
- Examination Administrator (templates, channels, manual/ops dispatch)
- System (event-driven queueing from Modules 02–08)
- Candidate (receives SMS/email/portal messages)
- Staff recipients where configured (e.g. credential/ops alerts)
- Auditor (delivery and template change history)

### User Journey
1. Who creates: Administrators create/maintain notification templates and channel configuration; lifecycle events in other modules create notification queue items; administrators may also create ad-hoc operational dispatches where approved.
2. How they create: Template register → edit template for an event/channel → enable SMS/email/portal → events enqueue messages → gateway/portal delivery → candidate sees portal inbox and external messages; failures appear on delivery status register for retry.
3. How they edit: Templates and channel flags are editable by administrators with version/history. Sent messages are not rewritten; retries create new delivery attempts.
4. How they send for approval: Template publish may be a simple admin save in current SOW (no multi-level approval inbox). Message dispatch itself is not an approval workflow.
5. How the approver sees pending items: No Department approver inbox. Delivery failure register is the operational queue.
6. How the approver decides: No approval decision on individual candidate messages.
7. How the applicant / maker sees history: Candidates see portal notification inbox history; administrators see dispatch and delivery status history.
8. How the approver / auditor sees history: Auditors view template changes, dispatch batches, channel, status (sent/failed), timestamps and target reference (registration/staff id) without exposing OTP bodies in logs beyond policy.

### Functional Capabilities
- Notification template register and editor for lifecycle events
- Channel configuration for SMS, email and portal as finally approved
- Event coverage: registration, payment, status, schedule, allocation, hall ticket, reminders, credentials, result, certificate
- Queue and dispatch lifecycle notifications
- Candidate portal notification inbox
- Delivery status and failure register with retry
- Staff notification targets where configured
- Suppress duplicate spam for the same event instance per approved rules
- Honour candidate contact details from registration/portal profile

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Notification template register | Complex |
| Notification template editor | Complex |
| Channel configuration (SMS email portal) | Medium |
| Notification dispatch console | Medium |
| Candidate portal notification inbox | Medium |
| Delivery status and failure register | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Maintain notification templates | Medium |
| Configure channels and event bindings | Medium |
| Queue lifecycle notification | Complex |
| Dispatch SMS notification | Complex |
| Dispatch email notification | Complex |
| Deliver portal notification | Medium |
| Search delivery status | Medium |
| Retry failed notification | Medium |

### Inputs
Event type and business reference, template id, channel flags, recipient mobile/email/user id, template variables, retry request.

### Outputs
Queued messages, gateway dispatch results, portal inbox items, delivery status records.

### Business Rules
- Channels used only as configured/approved for each event.
- OTP and credential messages follow security wording rules (no excess sensitive data in SMS where prohibited).
- Failed gateway sends are visible and retryable under rate limits.
- Portal notifications remain available after SMS/email for candidates who log in.
- Unsubscribed/invalid contacts handled with failure reason, not silent success.

### Validations
- Template required fields and variable placeholders
- Channel enabled before dispatch on that channel
- Recipient address present for selected channel
- Retry only for failed/pending terminal states allowed

### Calculations
None beyond delivery counts on status register.

### Workflow
Event → queue → dispatch per channel → record status → optional retry. No approval.

### Search Requirements
Delivery status by event, registration, channel, date, status; templates by event name.

### Documents
None; email body/SMS text are message content, not document management.

### Reports
Delivery volumes may appear in operational reports; this feature owns delivery register.

### Notifications
This feature is the notifications capability.

### Security
Template admin restricted; message content access limited; OTP/credential payloads masked in admin logs as approved; portal inbox ownership enforced.

### Integrations
SMS gateway and email gateway (estimated as Integration rows). Portal channel is internal.

### Dependencies
Modules 02–08 event producers; contact data from registration/portal.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- SMS Integration = Complex (auth, templates mapping, DLT/sender constraints as applicable, retry).
- Email Integration = Medium (SMTP/API auth, mapping, retry).
- Final channel matrix confirmed with Department; unused channels can be disabled without removing the feature.

### Risks
SMS DLT/template registration delays in India deployments.
Gateway outages during hall-ticket/result bursts — mitigate with queue and retry.

### Non Functional Requirements
Queue absorbs burst publishes; delivery workers idempotent; PII in payloads minimised and protected.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Notification template register | UI | Complex | 12 |
| Notification template editor | UI | Complex | 12 |
| Channel configuration (SMS email portal) | UI | Medium | 6 |
| Notification dispatch console | UI | Medium | 6 |
| Candidate portal notification inbox | UI | Medium | 6 |
| Delivery status and failure register | UI | Medium | 6 |
| Maintain notification templates | API | Medium | 6 |
| Configure channels and event bindings | API | Medium | 6 |
| Queue lifecycle notification | API | Complex | 8 |
| Dispatch SMS notification | API | Complex | 8 |
| Dispatch email notification | API | Complex | 8 |
| Deliver portal notification | API | Medium | 6 |
| Search delivery status | API | Medium | 6 |
| Retry failed notification | API | Medium | 6 |
| SMS gateway integration | Integration | Complex | 24 |
| Email gateway integration | Integration | Medium | 16 |
| Notification and delivery entities | DB | Medium | 4 |
| Candidate and staff notifications tests | Testing | Complex | 8 |
| Candidate and staff notifications implementation documentation | Documentation | Complex | 4 |

**Feature total: 158 hours**
