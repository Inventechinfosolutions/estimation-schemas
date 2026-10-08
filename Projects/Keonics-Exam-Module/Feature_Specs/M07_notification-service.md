# Module 07: Notification Service

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 7 (F07-001 … F07-007)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 07 Notification Service

931.35 hours · 154 tasks · Platform

Configurable multi-channel notifications for registration, scheduling, conduct, results, and certificate lifecycle events.

### F07-001 Notification Template Catalog and Content Management

127.1 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure reusable notification templates for each examination lifecycle event and delivery channel (SMS, email, in-app/portal). Templates define subject lines, message bodies, supported placeholder tokens, active status, and channel-specific variants so downstream dispatch can render consistent messages for registration confirmation, payment confirmation, schedule and allocation updates, hall ticket availability, examination reminders, credentials issuance, results publication, and certificate availability.

##### Business objective

Centralise configurable message content for all examination lifecycle notifications so message wording can be updated without code changes and each event-channel combination has a governed, auditable template before any outbound send occurs.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Notification Templates from examination administration settings.
2. Administrator views the template register filtered by lifecycle event type, channel, and active status.
3. Administrator selects Create Template.
4. Administrator chooses lifecycle event type (registration confirmation, payment confirmation, schedule update, allocation update, hall ticket available, examination reminder, credentials issued, results published, certificate available).
5. Administrator selects target channel (SMS, email, in-app/portal).
6. Administrator enters template name, optional description, email subject (email channel only), and message body with placeholder tokens from the reference panel.
7. Administrator saves; system validates uniqueness of event-type plus channel combination and placeholder syntax.
8. Administrator opens Preview, supplies sample candidate and examination values, and reviews rendered output per channel rules.
9. Administrator returns to register, edits an existing template to revise wording, and saves a new version while prior send history remains linked to earlier content snapshots.
10. Administrator deactivates an obsolete template after confirming no active event mapping depends on it (dependency check surfaced in confirmation dialog).
11. If register load fails, administrator sees error state with retry; if no templates exist, empty state prompts first template creation.

##### Functional capabilities

- Display paginated notification template register with event type, channel, name, active status, and last modified metadata
- Filter template register by lifecycle event type, channel, and active/inactive status
- Create notification template bound to one lifecycle event type and one channel
- Edit notification template content and metadata without deleting historical send references
- Deactivate notification template while retaining audit and delivery history
- Show placeholder token reference panel listing permitted tokens for selected event type
- Preview rendered template output using administrator-supplied sample placeholder values
- Validate unique active template per event-type and channel combination
- Validate mandatory subject line for email channel templates
- Validate message body length limits per channel policy
- Reject unknown or malformed placeholder tokens at save time
- Expose template register empty state and load-failure error state

##### Inputs

- Template name
- Template description
- Lifecycle event type selection
- Channel selection (SMS, email, in-app/portal)
- Email subject line (email channel)
- Message body with placeholder tokens
- Active flag
- Sample placeholder values for preview

##### Outputs

- Template register list rows
- Template detail record
- Rendered preview text per channel
- Validation error messages for duplicate or invalid templates
- Deactivation confirmation outcome
- Template version audit entries

##### Business rules

- Only one active template may exist per lifecycle event type and channel combination
- Deactivated templates cannot be selected for new event mappings but remain referenced by historical deliveries
- SMS templates must comply with configured maximum character length
- Email templates require non-empty subject and body
- In-app/portal templates store title and body suitable for inbox display
- Placeholder tokens must belong to the approved catalog for the selected event type
- Examination Administrator role is required for all template management actions

##### Validations

- Template name required; maximum 120 characters
- Lifecycle event type required; must be from approved examination lifecycle catalog
- Channel required; must be SMS, email, or in-app/portal
- Email subject required when channel is email; maximum 200 characters
- Message body required; minimum 1 non-whitespace character
- SMS body must not exceed configured character limit (validated at save)
- Placeholder tokens must match pattern {{token_name}} and exist in event-type token catalog
- Duplicate active event-type plus channel combination rejected on create and on activate
- Deactivation blocked when template is the sole active mapping for a subscribed event unless force-deactivate with warning

##### Calculations

- Preview rendering substitutes each {{token}} with supplied sample value or empty string when sample omitted
- SMS preview displays character count against configured limit

##### Workflow

DRAFT (on create before first save) → ACTIVE (saved and enabled) → INACTIVE (deactivated by administrator). ACTIVE → ACTIVE on content edit (version incremented). INACTIVE templates cannot transition to dispatch use without reactivation through edit save.

##### Search requirements

- Search templates by template name partial match
- Filter by lifecycle event type
- Filter by channel
- Filter by active or inactive status
- Sort by last modified date descending default

##### Security

- Restrict template management to Examination Administrator permissions from User and Role Management
- Audit log every create, update, deactivate, and preview action with administrator identity and timestamp
- Do not expose provider credentials on template screens

##### Dependencies

- F01 Platform Role and Permission Catalog — administrator authorization for template screens
- F01 Examination Administrator Account Lifecycle — authenticated administrator sessions
- F07-003 Examination Lifecycle Event Subscription and Template Routing — consumes templates via event mappings

##### Assumptions

- Final placeholder token catalog per event type will be confirmed during requirements workshops
- Channel-specific length limits for SMS will be supplied by selected SMS gateway constraints
- Template content localisation to multiple languages is out of scope unless added later

##### Risks

- Administrators may embed incorrect placeholders causing blank fields in live messages
- Deactivating widely used templates without updating event mappings may suppress notifications

##### Non-functional requirements

- Template register loads within 2 seconds for up to 500 templates
- Preview rendering completes within 1 second for standard templates
- All template changes must be auditable for compliance review

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Notification template register list with event type, channel, and active status filters | Easy | 14 |
| UI | Template register empty state when no templates exist | Simple | 5 |
| UI | Create notification template form with channel selector and subject/body fields | Medium | 16 |
| UI | Edit notification template form with last-modified metadata | Medium | 16 |
| UI | Placeholder token reference panel on template create and edit forms | Easy | 14 |
| UI | Deactivate template confirmation dialog with active mapping warning | Simple | 5 |
| UI | Template preview dialog with sample candidate and examination values | Medium | 16 |
| UI | Template register load failure error state with retry action | Simple | 5 |
| API | List and search notification templates with event, channel, and status filters | Medium | 6 |
| API | Get notification template detail by identifier | Easy | 4 |
| API | Create notification template with unique event-channel validation | Medium | 6 |
| API | Update notification template content and metadata with version increment | Medium | 6 |
| API | Deactivate notification template without deleting delivery history references | Easy | 4 |
| API | Preview rendered template with supplied placeholder sample values | Medium | 6 |
| API | List supported placeholder tokens for selected lifecycle event type | Simple | 2 |
| Database | Notification template core entity persistence | Simple | 0.1 |
| Database | Per-channel template content variant persistence | Easy | 0.25 |
| Database | Template change audit history persistence | Medium | 0.3 |
| Testing | Happy-path template create, edit, preview, and deactivate flows | Medium | 0.3 |
| Testing | Duplicate event-type plus channel active template rejection | Medium | 0.3 |
| Testing | Invalid placeholder syntax and missing email subject validation cases | Medium | 0.3 |
| Documentation | Examination Administrator notification template management runbook | Medium | 0.3 |
| Documentation | Technical placeholder token catalog and rendering rules | Easy | 0.25 |

### F07-002 SMS Email and In-App Channel Provider Configuration

152.4 hours · Go-live · 23 tasks

##### Description

Examination Administrators configure and maintain outbound channel providers for SMS, email, and in-app/portal notifications. Settings include gateway endpoints, sender identities, credential storage, TLS options, default retention for in-app messages, channel enablement flags, and test-send capability so each channel can be validated before lifecycle notifications are dispatched.

##### Business objective

Provide governed, secure configuration of multi-channel delivery infrastructure so examination lifecycle notifications can be sent reliably through department-approved SMS and email providers and surfaced in the candidate portal without embedding credentials in application code.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Channel Configuration under notification administration.
2. Administrator views read-only summary showing SMS, email, and in-app channel status (enabled/disabled, last test result).
3. Administrator selects Configure SMS.
4. Administrator enters gateway URL, sender ID, API credentials, and timeout settings; masked fields hide existing secrets.
5. Administrator saves SMS configuration; system validates mandatory fields and connectivity parameters format.
6. Administrator opens Test Send dialog, enters test mobile number, sends test SMS, and views success or failure message with provider response snippet.
7. Administrator selects Configure Email.
8. Administrator enters SMTP host, port, TLS mode, username, password, from-name, and from-address.
9. Administrator saves and runs email test send to a supplied test mailbox.
10. Administrator selects Configure In-App Channel and sets default inbox retention days and display title prefix.
11. Administrator disables a channel via confirmation dialog when maintenance is required; enabled channels resume after re-enable without data loss.
12. On validation failure, inline field errors and banner explain missing or invalid settings.

##### Functional capabilities

- Display channel configuration summary for SMS, email, and in-app channels
- Capture and update SMS gateway provider settings with credential masking on display
- Capture and update email SMTP settings including TLS and sender identity
- Capture and update in-app notification default retention and display settings
- Execute test send per channel with administrator-supplied test recipient
- Enable or disable each channel independently for outbound dispatch
- Validate host, port, email address, and mobile number formats before save or test
- Persist encrypted credentials separate from non-secret connection metadata
- Record last test send outcome and timestamp per channel

##### Inputs

- SMS gateway URL
- SMS sender ID
- SMS API key or credentials
- SMS request timeout
- SMTP host and port
- SMTP TLS mode
- SMTP username and password
- Email from name and from address
- In-app default retention days
- In-app display title prefix
- Test recipient mobile number
- Test recipient email address
- Channel enable/disable flag

##### Outputs

- Channel configuration summary
- Per-channel configuration detail with masked secrets
- Test send success or failure result with provider response code
- Validation errors for invalid connection settings
- Channel enabled/disabled status

##### Business rules

- At least one channel should remain enabled for production go-live (warning only, not hard block)
- Disabled channels must not be used for new dispatch attempts
- Credentials never returned in clear text after initial save
- Test send uses current saved configuration even if changed fields not yet saved (prompt to save first)
- Only Examination Administrator may view or change provider credentials

##### Validations

- SMS gateway URL required; must be valid HTTPS URL
- SMS sender ID required; alphanumeric length per gateway policy
- SMS API credential required on first save
- SMTP host required; valid hostname or IP
- SMTP port required; integer 1–65535
- From email address required; valid RFC email format
- Test mobile number required for SMS test; valid national mobile format
- Test email required for email test; valid RFC email format
- In-app retention days required; integer minimum 1 maximum 365

##### Workflow

CONFIGURED (settings saved) ↔ ENABLED (channel active for dispatch) ↔ DISABLED (channel inactive). Test send does not change workflow state but updates last_test_status metadata.

##### Security

- Encrypt provider credentials at rest
- Mask credential fields in UI and API responses
- Audit all configuration changes and test send actions
- Restrict access to Examination Administrator role

##### Integrations

- SMS gateway provider for connectivity test and live send
- SMTP mail server for connectivity test and live send

##### Dependencies

- F01 Platform Role and Permission Catalog — administrator authorization
- F01 Examination Administrator Account Lifecycle — authenticated sessions
- F07-004 Multi-Channel Notification Dispatch Engine — consumes channel settings for outbound send

##### Assumptions

- Department will nominate single primary SMS gateway and SMTP service for initial go-live
- Exact SMS gateway API shape will be finalised during integration confirmation
- Failover across multiple SMS providers is out of scope

##### Risks

- Incorrect SMTP TLS settings may block all email notifications until corrected
- Credential rotation requires administrator coordination to avoid dispatch outages

##### Non-functional requirements

- Configuration save completes within 2 seconds
- Test send returns result within 30 seconds or times out with clear error
- Credential encryption meets department security baseline

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Channel configuration summary overview for SMS, email, and in-app status | Easy | 14 |
| UI | SMS gateway provider configuration form with masked credential fields | Medium | 16 |
| UI | Email SMTP and sender identity configuration form | Medium | 16 |
| UI | In-app portal notification channel settings form | Easy | 14 |
| UI | Per-channel test send dialog with recipient input | Easy | 14 |
| UI | Channel enable disable confirmation dialog | Simple | 5 |
| UI | Channel configuration validation error banner and field errors | Simple | 5 |
| API | List channel configuration records | Easy | 4 |
| API | Get channel configuration detail by channel type with secret masking | Easy | 4 |
| API | Update SMS provider settings with encrypted credential storage | Medium | 6 |
| API | Update email channel settings with TLS and sender validation | Medium | 6 |
| API | Update in-app channel retention and display settings | Easy | 4 |
| API | Execute test send for selected channel | Medium | 6 |
| API | Enable or disable outbound channel without deleting configuration | Easy | 4 |
| Database | Channel provider configuration persistence | Easy | 0.25 |
| Database | Encrypted credential and connection parameter constraints | Complex | 0.5 |
| Integration | SMS gateway connectivity handshake for test send | Medium | 16 |
| Integration | SMTP server authentication handshake for test send | Medium | 16 |
| Testing | Happy-path save configuration and successful test send per channel | Complex | 0.5 |
| Testing | Invalid host, port, credential, and sender address rejection cases | Medium | 0.3 |
| Testing | Disabled channel blocks new dispatch enqueue for that channel | Medium | 0.3 |
| Documentation | Administrator channel provider setup runbook | Medium | 0.3 |
| Documentation | Technical credential storage and rotation notes | Easy | 0.25 |

### F07-003 Examination Lifecycle Event Subscription and Template Routing

255.95 hours · Go-live · 32 tasks

##### Description

The notification service subscribes to domain events emitted by registration, scheduling, conduct, results, and certificate modules, maps each event type to configured templates and channels, and enqueues dispatch jobs. Supported events include registration confirmation, payment confirmation, schedule updates, centre allocation updates, hall ticket availability, examination reminders, examination credentials issuance, results publication, and certificate availability. Administrators maintain event-to-template routing rules and monitor the inbound dispatch intake queue.

##### Business objective

Automate examination lifecycle notifications by reacting to authoritative business events from upstream modules without duplicating their approval or business logic, ensuring the correct template reaches the correct candidate channels whenever a lifecycle milestone occurs.

##### Actors

- Examination Administrator
- System Notification Service
- Candidate Registration module
- Examination Scheduling and Allocation module
- Secure Examination Conduct module
- Evaluation and Results module
- Certificate Management module

##### User journey

1. Examination Administrator opens Event Notification Mappings.
2. Administrator views mapping register filtered by lifecycle domain (registration, scheduling, conduct, results, certificate) and active status.
3. Administrator selects Create Mapping.
4. Administrator picks domain event type (e.g., payment confirmation, hall ticket available).
5. Administrator selects one or more channels and linked active templates with priority order when multiple channels apply.
6. Administrator saves mapping; system validates template availability and channel enablement.
7. When Candidate Registration completes registration, upstream module emits registration confirmation event with candidate contact details and registration number.
8. Notification service receives event, verifies idempotency key, resolves mapping, and enqueues per-channel dispatch jobs.
9. When payment succeeds, payment confirmation event triggers mapped templates similarly.
10. Scheduling module emits schedule update or allocation update events after administrator actions; service enqueues notifications without re-evaluating allocation logic.
11. Hall ticket generation emits hall ticket available event; service notifies candidate via configured channels.
12. Conduct module emits examination reminder and credentials issued events prior to session.
13. Results module emits results published event after publication.
14. Certificate module emits certificate available event after generation.
15. Administrator monitors dispatch intake queue for received events, mapping resolution status, and enqueue failures.
16. Unmapped or malformed events appear in queue with error status for investigation.

##### Functional capabilities

- Maintain catalog of examination lifecycle domain event types
- Create event-to-template routing mapping with multi-channel selection
- Edit and deactivate event routing mappings
- Receive registration confirmation domain event and enqueue notifications
- Receive payment confirmation domain event and enqueue notifications
- Receive schedule update domain event and enqueue notifications
- Receive centre allocation update domain event and enqueue notifications
- Receive hall ticket available domain event and enqueue notifications
- Receive examination reminder domain event and enqueue notifications
- Receive examination credentials issued domain event and enqueue notifications
- Receive results published domain event and enqueue notifications
- Receive certificate available domain event and enqueue notifications
- Enforce idempotent processing using upstream event identifier
- Log unmapped event types without dispatch
- Display dispatch intake queue monitor with event type and status filters

##### Inputs

- Domain event type code
- Domain event idempotency key
- Candidate identifier and contact channels (mobile, email)
- Registration number
- Examination name and schedule details
- Allocated centre name and address
- Hall ticket reference
- Examination credentials reference
- Result summary fields permitted for notification
- Certificate reference
- Event occurrence timestamp
- Selected template identifiers per channel
- Channel priority order

##### Outputs

- Event-to-template mapping register rows
- Enqueued dispatch job records per channel
- Idempotent duplicate suppression outcome
- Unmapped event error log entries
- Dispatch intake queue monitor rows

##### Business rules

- Notification service does not decide whether registration, payment, or allocation is approved—it reacts only to emitted events
- Each domain event type may have at most one active routing mapping
- Dispatch enqueue skipped for channels that are globally disabled
- Missing candidate contact channel skips that channel but may still enqueue others
- Duplicate event idempotency key must not create duplicate dispatch jobs
- Events must carry sufficient placeholder data for template rendering or enqueue fails with explicit error

##### Validations

- Event type required; must exist in lifecycle catalog
- Idempotency key required; non-empty string
- Mapping save requires at least one channel with linked active template
- Template channel must match mapping channel selection
- Registration events require registration number and candidate mobile
- Payment confirmation events require payment reference and amount placeholder source
- Hall ticket events require hall ticket download reference token
- Credentials events must not include plaintext password in payload—only notification-safe fields
- Malformed JSON payload rejected with logged error

##### Workflow

Event RECEIVED → MAPPING_RESOLVED → JOBS_ENQUEUED → HANDED_OFF_TO_DISPATCH. Event RECEIVED → UNMAPPED (no active mapping, terminal log). Event RECEIVED → DUPLICATE_SUPPRESSED (idempotency hit, terminal). Event RECEIVED → ENQUEUE_FAILED (validation or missing template, terminal with error detail).

##### Search requirements

- Filter event mappings by lifecycle domain
- Filter event mappings by event type
- Filter dispatch intake queue by event type, status, and received date range
- Search intake queue by registration number

##### Notifications

- Registration confirmation trigger
- Payment confirmation trigger
- Schedule update trigger
- Centre allocation update trigger
- Hall ticket availability trigger
- Examination reminder trigger
- Examination credentials availability trigger
- Results publication trigger
- Certificate availability trigger

##### Security

- Accept domain events only from authenticated internal module publishers
- Do not persist full payment instrument details from payment events
- Credentials events must exclude secrets from stored payload snapshots
- Administrator queue monitor requires Examination Administrator permission

##### Integrations

- Candidate Registration module event publication
- Examination Scheduling and Allocation module event publication
- Secure Examination Conduct module event publication
- Evaluation and Results module event publication
- Certificate Management module event publication

##### Dependencies

- F05 Candidate Registration — emits registration and payment confirmation events
- F06 Examination Scheduling and Allocation — emits schedule, allocation, and hall ticket events
- F09 Secure Examination Conduct — emits reminder and credentials events
- F10 Evaluation and Results — emits results published events
- F11 Certificate Management — emits certificate available events
- F07-001 Notification Template Catalog — templates referenced by mappings
- F07-002 Channel Provider Configuration — channel enablement governs enqueue
- F07-004 Multi-Channel Notification Dispatch Engine — processes enqueued jobs

##### Assumptions

- Upstream modules emit events after their business transactions commit successfully
- Exact event payload fields will be agreed in cross-module technical workshops
- OTP generation for candidate login remains in Candidate Registration module

##### Risks

- Event schema drift between modules may break placeholder resolution
- High-volume schedule bulk updates may spike intake queue requiring operational monitoring

##### Non-functional requirements

- Event intake and enqueue within 3 seconds under normal load
- Idempotency store retained minimum 90 days
- Intake queue monitor supports pagination for 10,000+ rows

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Event-to-template mapping register with lifecycle domain filters | Medium | 16 |
| UI | Create event mapping form with event type, template, and channel priority | Medium | 16 |
| UI | Edit event mapping form | Medium | 16 |
| UI | Event mapping detail read-only view with linked templates | Easy | 14 |
| UI | Deactivate event mapping confirmation dialog | Simple | 5 |
| UI | Dispatch intake queue monitor list with status and event type filters | Complex | 18 |
| API | List examination lifecycle event types catalog | Simple | 2 |
| API | List event-to-template mappings with search filters | Medium | 6 |
| API | Create event-to-template mapping with duplicate prevention | Medium | 6 |
| API | Update event-to-template mapping channels and priority | Medium | 6 |
| API | Deactivate event-to-template mapping | Easy | 4 |
| API | Intake registration confirmation event and enqueue notifications | Complex | 8 |
| API | Intake payment confirmation event and enqueue notifications | Complex | 8 |
| API | Intake schedule and allocation update event and enqueue notifications | Complex | 8 |
| API | Intake hall ticket availability event and enqueue notifications | Complex | 8 |
| API | Intake examination reminder event and enqueue notifications | Complex | 8 |
| API | Intake examination credentials issued event and enqueue notifications | Complex | 8 |
| API | Intake results publication event and enqueue notifications | Complex | 8 |
| API | Intake certificate availability event and enqueue notifications | Complex | 8 |
| Database | Event type reference catalog persistence | Simple | 0.1 |
| Database | Event-to-template routing mapping persistence | Easy | 0.25 |
| Database | Inbound domain event idempotency and dispatch job enqueue persistence | Complex | 0.5 |
| Integration | Subscribe to Candidate Registration module domain events | Medium | 16 |
| Integration | Subscribe to Examination Scheduling and Allocation module domain events | Medium | 16 |
| Integration | Subscribe to Secure Examination Conduct module domain events | Medium | 16 |
| Integration | Subscribe to Evaluation and Results module domain events | Medium | 16 |
| Integration | Subscribe to Certificate Management module domain events | Medium | 16 |
| Testing | Happy-path each lifecycle event type routes to configured templates | Complex | 0.5 |
| Testing | Unmapped event type logging and invalid payload rejection | Medium | 0.3 |
| Testing | Duplicate domain event idempotency suppresses duplicate dispatch jobs | Complex | 0.5 |
| Documentation | Administrator event mapping configuration guide | Medium | 0.3 |
| Documentation | Technical domain event payload contract per lifecycle event | Complex | 0.5 |

### F07-004 Multi-Channel Notification Dispatch Engine

117.45 hours · Go-live · 21 tasks

##### Description

Background dispatch processing dequeues notification jobs created by lifecycle event intake, renders template placeholders from event payload snapshots, sends SMS and email through configured providers, writes in-app notifications to candidate inboxes, records per-channel attempt outcomes, and applies retry with backoff for transient provider failures until terminal success or exhaustion.

##### Business objective

Reliably deliver examination lifecycle messages across SMS, email, and in-app channels with traceable attempt history and controlled retry so candidates receive timely registration, scheduling, conduct, results, and certificate notifications.

##### Actors

- System Notification Service
- Examination Administrator

##### User journey

1. Dispatch worker polls queued jobs in priority and received-time order.
2. Worker loads job, linked template snapshot, channel configuration, and recipient contact details.
3. Worker renders message body and subject by substituting placeholders from event payload.
4. For SMS jobs, worker calls SMS gateway with rendered text and records provider message ID or error.
5. For email jobs, worker sends SMTP message with rendered subject and HTML or plain body.
6. For in-app jobs, worker inserts inbox record for candidate with title and body.
7. Worker writes delivery attempt row with status SENT, FAILED, or RETRY_PENDING.
8. On transient failure, worker schedules retry according to backoff policy until max attempts.
9. After terminal outcome, worker marks dispatch job COMPLETED or EXhausted_FAILED.
10. Examination Administrator opens dispatch job detail from monitor to view channel attempt timeline and provider responses.
11. When queue has no pending jobs, monitor shows empty state.

##### Functional capabilities

- Dequeue pending dispatch jobs for worker processing
- Render template placeholders from stored event payload snapshot
- Send SMS through configured gateway with provider response capture
- Send email through configured SMTP with message ID capture
- Create candidate in-app inbox notification record
- Record each delivery attempt with timestamp, channel, status, and provider code
- Retry transient failures with configurable backoff and max attempts
- Mark dispatch job terminal success or exhausted failure
- Expose dispatch job detail with attempt timeline for administrators
- Handle missing placeholder values with configurable fail-or-blank policy

##### Inputs

- Dispatch job identifier
- Template snapshot reference
- Event payload snapshot
- Recipient mobile number
- Recipient email address
- Candidate portal user identifier for in-app
- Channel type
- Retry attempt count
- Provider credentials from channel configuration

##### Outputs

- Provider message identifier for SMS or email
- In-app inbox record identifier
- Per-attempt delivery log rows
- Terminal dispatch job status
- Administrator job detail with attempt timeline

##### Business rules

- Jobs for disabled channels fail fast without provider call
- Rendered messages must not include fields marked sensitive in event contract
- Retry applies only to classified transient provider errors
- Permanent failures (invalid number, hard bounce) do not retry
- Successful in-app write is terminal for that channel attempt even if SMS/email sibling fails
- Job processing must be idempotent per attempt number

##### Validations

- Recipient mobile required for SMS jobs; valid format or fail permanent
- Recipient email required for email jobs; valid RFC format or fail permanent
- Candidate identifier required for in-app jobs
- Template snapshot must exist and be readable at processing time
- Rendered SMS must not exceed configured length after substitution
- Missing mandatory placeholder when policy is FAIL aborts attempt with logged reason

##### Calculations

- Next retry time equals previous attempt time plus backoff interval for attempt number
- SMS rendered length counted after placeholder substitution

##### Workflow

Job PENDING → PROCESSING → ATTEMPT_SENT (per channel success) → COMPLETED (all channels terminal success or acceptable partial success per policy). Job PENDING → PROCESSING → ATTEMPT_FAILED → RETRY_PENDING → PROCESSING (loop) → EXHAUSTED_FAILED when max retries exceeded. Job PENDING → FAILED_FAST when channel disabled or permanent validation failure.

##### Search requirements

- Administrator job detail retrieved by dispatch job identifier
- Dispatch monitor filters jobs by status and received date

##### Security

- Worker credentials loaded from encrypted configuration only at runtime
- Do not log full message bodies containing credentials in application logs
- Restrict administrator job detail to Examination Administrator role

##### Integrations

- SMS gateway send API
- SMTP mail send
- Internal candidate inbox persistence

##### Dependencies

- F07-002 Channel Provider Configuration — provider settings and enable flags
- F07-001 Notification Template Catalog — template content snapshots
- F07-003 Examination Lifecycle Event Subscription — job enqueue source
- F07-005 Delivery Status Tracking — persists attempt outcomes
- F07-007 Candidate Portal In-App Notification Inbox — displays in-app records

##### Assumptions

- Single dispatch worker pool sufficient for initial examination volumes
- Provider transient error classification table supplied during gateway integration
- Partial success policy (e.g., in-app succeeds, SMS fails) acceptable unless department mandates all-channel success

##### Risks

- Provider outage may delay large batches until retries exhaust
- Template placeholder mismatch at dispatch time causes avoidable failures if event payload changes retroactively

##### Non-functional requirements

- Process standard job within 10 seconds excluding provider latency
- Support at least 500 concurrent queued jobs
- Retry backoff configurable without code deployment

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Dispatch job detail read-only view with channel attempt timeline | Medium | 16 |
| UI | Dispatch queue monitor empty state when no pending jobs | Simple | 5 |
| API | Dequeue pending dispatch job for worker processing | Medium | 6 |
| API | Render message body by resolving template placeholders from event payload | Complex | 8 |
| API | Dispatch SMS outbound message via configured gateway | Medium | 6 |
| API | Dispatch email outbound message via configured SMTP | Medium | 6 |
| API | Persist in-app portal notification record for candidate | Medium | 6 |
| API | Record per-channel dispatch attempt outcome on delivery log | Medium | 6 |
| API | Retry transient failure with configured backoff policy | Complex | 8 |
| API | Mark dispatch job terminal success or exhausted failure | Medium | 6 |
| API | Get dispatch job detail with channel attempt history | Medium | 6 |
| Database | Outbound dispatch worker job state persistence | Medium | 0.3 |
| Database | Per-recipient rendered message snapshot persistence | Easy | 0.25 |
| Integration | SMS gateway send message call with provider response mapping | Medium | 16 |
| Integration | SMTP send mail call with provider correlation identifier capture | Medium | 16 |
| Integration | Internal portal notification fan-out to candidate inbox store | Simple | 4 |
| Testing | Happy-path successful SMS, email, and in-app dispatch for single job | Complex | 0.5 |
| Testing | Provider timeout and invalid recipient permanent failure recording | Medium | 0.3 |
| Testing | Retry policy stops after max attempts with complete audit trail | Complex | 0.5 |
| Testing | Missing mandatory placeholder fail policy aborts dispatch safely | Medium | 0.3 |
| Documentation | Technical dispatch worker operations and retry policy notes | Medium | 0.3 |

### F07-005 Delivery Status Tracking and Notification Register

82.05 hours · Go-live · 17 tasks

##### Description

Examination Administrators monitor all outbound notification deliveries across SMS, email, and in-app channels through a searchable register with status filters, drill-down to attempt history and provider responses, correlation to source lifecycle events and registration numbers, and export for operational review.

##### Business objective

Give examination administrators full visibility into whether lifecycle notifications reached candidates, support troubleshooting of failed deliveries, and maintain auditable evidence of communication for registration through certificate milestones.

##### Actors

- Examination Administrator
- System Notification Service

##### User journey

1. Examination Administrator opens Notification Delivery Register.
2. Administrator applies filters for date range, channel, delivery status, and lifecycle event type.
3. Administrator searches by candidate registration number or mobile number.
4. Register lists deliveries with sent time, channel, event type, status chip, and recipient masked appropriately.
5. Administrator selects a row to open delivery detail view.
6. Detail view shows rendered message snapshot reference, each attempt timestamp, provider response code, and linked source event identifier.
7. Administrator exports current filtered result set to spreadsheet for offline review.
8. If no deliveries match filters, empty state explains criteria.
9. If register API fails, error state offers retry.

##### Functional capabilities

- List notification deliveries with pagination
- Filter deliveries by date range, channel, status, and event type
- Search deliveries by registration number or mobile number
- Display delivery detail with multi-attempt history
- Show provider response codes and correlation identifiers
- Link delivery row to source domain event and dispatch job
- Export filtered delivery register to spreadsheet format
- Mask recipient contact details partial display in list view

##### Inputs

- Date range filter
- Channel filter
- Delivery status filter
- Lifecycle event type filter
- Registration number search text
- Mobile number search text
- Export column selection default set

##### Outputs

- Delivery register paginated rows
- Delivery detail with attempt timeline
- Exported spreadsheet file
- Empty and error state messages

##### Business rules

- Delivery statuses include PENDING, SENT, DELIVERED (if provider confirms), FAILED, RETRY_PENDING, EXHAUSTED_FAILED for SMS/email; READ/UNREAD applies only to in-app channel display
- Historical deliveries remain visible after template deactivation
- Export limited to administrator authorized scope (department-wide for Examination Administrator)
- Provider response codes stored as received without alteration

##### Validations

- Date range start must be before or equal to end
- Registration number search minimum 3 characters when provided
- Mobile search must be numeric format when provided
- Export row limit enforced with message when exceeded

##### Workflow

Delivery attempt statuses transition PENDING → SENT → DELIVERED or FAILED → RETRY_PENDING → SENT/FAILED loops → EXHAUSTED_FAILED terminal. In-app deliveries transition UNREAD → READ when candidate opens notification (tracked in inbox feature).

##### Search requirements

- Filter by sent date range
- Filter by channel SMS, email, in-app
- Filter by status PENDING, SENT, FAILED, EXHAUSTED_FAILED
- Filter by lifecycle event type
- Search by registration number exact or partial
- Search by mobile number
- Default sort by sent timestamp descending

##### Security

- Examination Administrator role required
- Mask mobile and email in list view showing last four digits or local-part obscured
- Audit export actions with administrator identity and filter snapshot

##### Dependencies

- F07-004 Multi-Channel Notification Dispatch Engine — produces delivery attempts
- F01 Platform Role and Permission Catalog — administrator access control

##### Assumptions

- SMS delivery confirmation depends on gateway delivery receipt support; otherwise status remains SENT
- Export format is CSV or XLSX per department standard

##### Risks

- Large export queries may impact performance during peak examination periods

##### Non-functional requirements

- Register search returns within 3 seconds for 100,000 delivery rows indexed
- Export up to 10,000 rows per request

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Notification delivery register list with date, channel, status, and event type filters | Medium | 16 |
| UI | Delivery register empty state when no deliveries match filters | Simple | 5 |
| UI | Delivery detail read-only view with provider response codes | Medium | 16 |
| UI | Export delivery register to spreadsheet action | Easy | 14 |
| UI | Delivery register load failure error state | Simple | 5 |
| API | List notification deliveries with search and filter parameters | Medium | 6 |
| API | Get delivery detail including attempt history and message snapshot reference | Medium | 6 |
| API | Search deliveries by registration number or mobile number | Medium | 6 |
| API | Export filtered delivery register dataset | Medium | 6 |
| Database | Per-channel delivery attempt log persistence | Medium | 0.3 |
| Database | Delivery status indexing for register query performance | Easy | 0.25 |
| Database | Delivery to source domain event correlation persistence | Medium | 0.3 |
| Testing | Happy-path register list, detail drill-down, and filtered search | Medium | 0.3 |
| Testing | Export respects active filters and row limit enforcement | Easy | 0.25 |
| Testing | Unauthorized user denied access to delivery register | Medium | 0.3 |
| Documentation | Administrator delivery monitoring runbook | Easy | 0.25 |
| Documentation | Technical delivery status lifecycle definitions | Simple | 0.1 |

### F07-006 Resend Controls and Failed Delivery Recovery

108.45 hours · Go-live · 19 tasks

##### Description

Examination Administrators resend failed or exhausted lifecycle notifications individually or in bulk from the delivery register, with eligibility checks against active templates and enabled channels, mandatory reason capture, audit linkage to original deliveries, partial bulk outcome reporting, and ability to cancel pending resends before dispatch starts.

##### Business objective

Allow controlled recovery when SMS, email, or in-app notifications fail so candidates still receive registration, scheduling, hall ticket, reminder, credentials, results, or certificate messages without duplicating successful sends or bypassing governance rules.

##### Actors

- Examination Administrator
- System Notification Service
- Candidate

##### User journey

1. Examination Administrator opens Delivery Register and applies Failed or Exhausted status filter.
2. Administrator reviews failed delivery rows and opens detail to inspect last provider error.
3. Administrator selects Resend on a single delivery.
4. Resend dialog shows channel, recipient, linked event type, and requires reason text.
5. System validates template still active and channel enabled; if not, blocked reason dialog explains constraint.
6. Administrator confirms; system creates new dispatch job linked to original delivery and writes resend audit record.
7. Administrator selects multiple failed rows and chooses Bulk Resend.
8. Bulk confirmation shows count and requires reason; system processes each with eligibility check.
9. Results summary shows succeeded, skipped, and failed counts without duplicating already-resubmitted items.
10. Administrator views Resend History tab on original delivery detail showing each resend attempt linkage.
11. If resend still queued, administrator may cancel pending resend before worker picks up job.
12. Candidate receives message when resend dispatch succeeds through normal engine flow.

##### Functional capabilities

- Filter delivery register to failed and exhausted deliveries eligible for review
- Resend single failed notification with mandatory reason capture
- Bulk resend selected failed notifications with rate limit guard
- Validate resend eligibility against active template and enabled channel
- Block resend with explicit reason when template inactive or channel disabled
- Create resend audit record linked to original delivery identifier
- Display resend history on delivery detail
- Cancel pending resend job before dispatch starts
- Prevent duplicate resend while identical resend job already pending

##### Inputs

- Original delivery identifier
- Bulk selected delivery identifiers
- Resend reason text
- Optional channel override when original channel permanently failed and alternate configured
- Cancel pending resend job identifier

##### Outputs

- New dispatch job identifier for resend
- Resend audit entries
- Bulk resend outcome summary counts
- Blocked resend reason message
- Resend history list on delivery detail
- Cancel confirmation outcome

##### Business rules

- Resend reason mandatory minimum 10 characters
- Cannot resend deliveries that already reached SENT or DELIVERED terminal success unless department override flag enabled for duplicate resend warning
- Bulk resend maximum batch size enforced (configurable, e.g., 100)
- Resend uses current template content version active at resend time
- Each resend retains correlation to original source lifecycle event
- Cancel allowed only while resend job status is PENDING

##### Validations

- Original delivery must exist and be in FAILED or EXHAUSTED_FAILED status
- Reason text required; length 10–500 characters
- Bulk selection must not exceed configured maximum
- Template for event type and channel must be active
- Channel must be enabled
- Duplicate pending resend for same delivery rejected

##### Calculations

- Bulk resend summary counts succeeded, skipped_ineligible, and failed_enqueue per item

##### Workflow

Failed delivery → RESEND_REQUESTED → RESEND_PENDING (job queued) → RESEND_DISPATCHING → RESEND_SENT or RESEND_FAILED. RESEND_PENDING → RESEND_CANCELLED (administrator cancel). Bulk operation tracks per-item subprocess through same states.

##### Search requirements

- Filter failed deliveries eligible for resend
- Resend history listed by original delivery identifier

##### Security

- Examination Administrator permission required for resend and cancel
- Audit every resend and cancel with administrator, reason, and timestamp
- Bulk resend rate limit prevents abuse

##### Dependencies

- F07-005 Delivery Status Tracking — source failed delivery rows
- F07-004 Multi-Channel Notification Dispatch Engine — processes resend jobs
- F07-001 Notification Template Catalog — active template validation
- F07-002 Channel Provider Configuration — channel enable validation

##### Assumptions

- Administrators resend only after correcting recipient data upstream when failure was invalid contact
- Candidate-initiated resend is out of scope except via administrator action

##### Risks

- Bulk resend during misconfiguration may amplify provider errors
- Using updated template at resend time may confuse candidates if content differs materially

##### Non-functional requirements

- Single resend enqueue within 2 seconds
- Bulk resend of 100 items completes enqueue within 60 seconds

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Failed delivery subset filter view on delivery register | Easy | 14 |
| UI | Resend single delivery confirmation dialog with mandatory reason | Medium | 16 |
| UI | Bulk resend selected failed deliveries confirmation dialog | Medium | 16 |
| UI | Resend blocked reason dialog when template inactive or channel disabled | Simple | 5 |
| UI | Resend history tab on delivery detail view | Easy | 14 |
| UI | Cancel pending resend confirmation dialog | Simple | 5 |
| API | List failed deliveries eligible for resend | Medium | 6 |
| API | Resend single notification delivery with audit reason capture | Complex | 8 |
| API | Bulk resend failed deliveries with rate limit guard | Complex | 8 |
| API | Validate resend eligibility against template and channel availability | Medium | 6 |
| API | List resend history for original delivery identifier | Easy | 4 |
| API | Cancel pending resend queue entry before dispatch starts | Easy | 4 |
| Database | Resend audit record linked to original delivery persistence | Medium | 0.3 |
| Testing | Happy-path single and bulk resend creates new dispatch attempt | Complex | 0.5 |
| Testing | Resend rejected when template deactivated or channel disabled | Medium | 0.3 |
| Testing | Bulk resend partial failure reporting without duplicate pending resends | Complex | 0.5 |
| Testing | Resend reason mandatory validation and cancel pending resend flow | Medium | 0.3 |
| Documentation | Administrator resend policy and failure recovery runbook | Medium | 0.3 |
| Documentation | Technical resend idempotency and audit linkage notes | Easy | 0.25 |

### F07-007 Candidate Portal In-App Notification Inbox

87.95 hours · Go-live · 19 tasks

##### Description

Candidates view examination lifecycle notifications delivered to the portal in-app channel through a paginated inbox with unread badge, notification detail view, mark-read actions, empty and error states, and mobile-responsive layout. Covers registration confirmation, payment confirmation, schedule and allocation updates, hall ticket availability, examination reminders, credentials notices, results publication, and certificate availability messages.

##### Business objective

Ensure candidates have a durable in-portal record of examination communications when SMS or email is missed, with clear read status and secure access limited to their own notifications.

##### Actors

- Candidate
- System Notification Service

##### User journey

1. Candidate logs into examination portal (OTP login handled by Candidate Registration module).
2. Header shows unread in-app notification count badge when count greater than zero.
3. Candidate opens Notifications inbox from portal menu.
4. Inbox lists notifications with title, received date, and unread indicator sorted newest first.
5. Candidate taps a row to open notification detail showing full message body and related examination context fields.
6. Opening detail marks notification as read and decrements unread badge.
7. Candidate uses Mark all as read control to clear unread indicators.
8. If no notifications exist, empty state explains notifications will appear for registration and examination milestones.
9. If inbox load fails, error state with retry is shown.
10. On mobile viewport, list layout adapts for touch navigation without loss of content.

##### Functional capabilities

- List candidate in-app notifications with pagination
- Display unread count badge on portal header
- Show notification detail with title, body, and received timestamp
- Mark single notification as read on detail open
- Mark all notifications as read for logged-in candidate
- Hide notifications older than configured retention unless already opened
- Prevent candidate access to another candidate notification records
- Render mobile-responsive inbox list and detail layouts
- Show inbox empty state and load error state

##### Inputs

- Authenticated candidate session identifier
- Pagination page number and size
- Notification identifier for detail and mark-read
- Mark all as read action

##### Outputs

- Paginated inbox list rows
- Unread notification count
- Notification detail content
- Updated read status
- Empty and error state views

##### Business rules

- Candidates see only notifications addressed to their portal account
- Unread count includes notifications with read status UNREAD within retention window
- Mark all as read updates only notifications currently visible under retention policy
- In-app notifications created only by dispatch engine for mapped lifecycle events
- Deleted upstream registration does not delete historical notifications but may hide future relevance in UI footnote

##### Validations

- Session required for all inbox operations
- Notification identifier must belong to authenticated candidate or return not found
- Pagination page size maximum 50
- Mark-read on already read notification is idempotent success

##### Calculations

- Unread count equals count of inbox rows with read status UNREAD within retention days from channel configuration

##### Workflow

Notification UNREAD → READ on detail view open or explicit mark-read. Mark all transitions all UNREAD in retention window to READ. Archived notifications beyond retention hidden from list (terminal visibility state).

##### Search requirements

- Inbox sorted by received timestamp descending
- Optional future filter by unread only not in initial scope unless configured—default shows all within retention

##### Notifications

- In-app display of registration confirmation message
- In-app display of payment confirmation message
- In-app display of schedule and allocation update message
- In-app display of hall ticket availability message
- In-app display of examination reminder message
- In-app display of credentials notice message
- In-app display of results publication message
- In-app display of certificate availability message

##### Security

- Candidate session scoped data access only
- No exposure of other candidates notification identifiers through sequential ID guessing
- HTTPS required for inbox access

##### Dependencies

- F05 Candidate Registration — candidate portal authentication session
- F07-004 Multi-Channel Notification Dispatch Engine — creates inbox records
- F07-002 Channel Provider Configuration — in-app retention settings

##### Assumptions

- Candidate portal shell and navigation exist from registration module
- Push browser notifications are out of scope; inbox is pull-based only

##### Risks

- Candidates may rely solely on inbox and miss time-sensitive SMS if unread
- Long retention may clutter inbox unless titles are clear

##### Non-functional requirements

- Inbox first page loads within 2 seconds on mobile network
- Unread count API responds within 500 milliseconds
- Responsive layout supports minimum viewport 320px width

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal notification inbox list with unread indicators | Medium | 16 |
| UI | Candidate notification detail read-only view | Easy | 14 |
| UI | Mark single notification as read control on detail view | Simple | 5 |
| UI | Mark all notifications as read action on inbox | Simple | 5 |
| UI | Candidate inbox empty state when no notifications exist | Simple | 5 |
| UI | Candidate inbox load error state with retry | Simple | 5 |
| UI | Mobile-responsive notification list and detail layout | Medium | 16 |
| API | List candidate in-app notifications with pagination | Medium | 6 |
| API | Get candidate notification detail by identifier | Easy | 4 |
| API | Mark single notification as read | Easy | 4 |
| API | Mark all notifications as read for authenticated candidate | Easy | 4 |
| API | Count unread in-app notifications for portal header badge | Simple | 2 |
| Database | Candidate in-app notification inbox persistence | Easy | 0.25 |
| Database | Read status and received timestamp indexing for inbox queries | Easy | 0.25 |
| Testing | Happy-path inbox list, detail, mark read, and unread count badge | Medium | 0.3 |
| Testing | Candidate cannot access another candidate notification record | Complex | 0.5 |
| Testing | Expired notifications hidden per retention policy | Medium | 0.3 |
| Documentation | Candidate portal notification inbox user guide | Easy | 0.25 |
| Documentation | Technical in-app notification retention policy notes | Simple | 0.1 |
