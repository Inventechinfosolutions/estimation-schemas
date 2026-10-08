# ChatGPT Visualization Brief — Module 07: Notification Service

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 07 Notification Service
**Features:** 7 (F07-001 … F07-007)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 07 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Event → route → template → channel dispatch architecture
2. Notification job state machine + resend linkage
3. Multi-channel sequence (SMS/Email/In-App)
4. Admin delivery register + inbox UX flow
5. Notify ERD
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Notification Service
**Purpose:** Template and channel configuration; lifecycle event routing; multi-channel dispatch; delivery tracking; resend/recovery; candidate in-app notification inbox.

**Actors (union across features):**
- Candidate
- Candidate Registration module
- Certificate Management module
- Evaluation and Results module
- Examination Administrator
- Examination Scheduling and Allocation module
- Secure Examination Conduct module
- System Notification Service

**Feature list:**
- **F07-001** — Notification Template Catalog and Content Management
- **F07-002** — SMS Email and In-App Channel Provider Configuration
- **F07-003** — Examination Lifecycle Event Subscription and Template Routing
- **F07-004** — Multi-Channel Notification Dispatch Engine
- **F07-005** — Delivery Status Tracking and Notification Register
- **F07-006** — Resend Controls and Failed Delivery Recovery
- **F07-007** — Candidate Portal In-App Notification Inbox

### DATA MODEL (from EXAM DB design v2.1)

- `notification_template`
- `notification_channel_config`
- `notification_event_route`
- `notification_job`
- `notification_delivery_attempt`
- `in_app_notification`

### FEATURE CATALOGUE

#### F07-001 — Notification Template Catalog and Content Management

**One-liner / description:** Examination Administrators configure reusable notification templates for each examination lifecycle event and delivery channel (SMS, email, in-app/portal). Templates define subject lines, message bodies, supported…

**Business objective:** Centralise configurable message content for all examination lifecycle notifications so message wording can be updated without code changes and each event-channel combination has a governed, auditable template before any outbound send occurs.

**Actors:** Examination Administrator; System Notification Service

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Template name; Template description; Lifecycle event type selection; Channel selection (SMS, email, in-app/portal); Email subject line (email channel); Message body with placeholder tokens; Active flag; Sample placeholder values for preview

**Outputs:** Template register list rows; Template detail record; Rendered preview text per channel; Validation error messages for duplicate or invalid templates; Deactivation confirmation outcome; Template version audit entries

**Business rules:**
- Only one active template may exist per lifecycle event type and channel combination
- Deactivated templates cannot be selected for new event mappings but remain referenced by historical deliveries
- SMS templates must comply with configured maximum character length
- Email templates require non-empty subject and body
- In-app/portal templates store title and body suitable for inbox display
- Placeholder tokens must belong to the approved catalog for the selected event type
- Examination Administrator role is required for all template management actions

**Validations:**
- Template name required; maximum 120 characters
- Lifecycle event type required; must be from approved examination lifecycle catalog
- Channel required; must be SMS, email, or in-app/portal
- Email subject required when channel is email; maximum 200 characters
- Message body required; minimum 1 non-whitespace character
- SMS body must not exceed configured character limit (validated at save)
- Placeholder tokens must match pattern {{token_name}} and exist in event-type token catalog
- Duplicate active event-type plus channel combination rejected on create and on activate

**Workflow / states:** DRAFT (on create before first save) → ACTIVE (saved and enabled) → INACTIVE (deactivated by administrator). ACTIVE → ACTIVE on content edit (version incremented). INACTIVE templates cannot transition to dispatch use without reactivation through edit save.

**Dependencies:**
- F01 Platform Role and Permission Catalog — administrator authorization for template screens
- F01 Examination Administrator Account Lifecycle — authenticated administrator sessions
- F07-003 Examination Lifecycle Event Subscription and Template Routing — consumes templates via event mappings

**Risks:** Administrators may embed incorrect placeholders causing blank fields in live messages; Deactivating widely used templates without updating event mappings may suppress notifications

---

#### F07-002 — SMS Email and In-App Channel Provider Configuration

**One-liner / description:** Examination Administrators configure and maintain outbound channel providers for SMS, email, and in-app/portal notifications. Settings include gateway endpoints, sender identities, credential storage, TLS options,…

**Business objective:** Provide governed, secure configuration of multi-channel delivery infrastructure so examination lifecycle notifications can be sent reliably through department-approved SMS and email providers and surfaced in the candidate portal without embedding credentials in application code.

**Actors:** Examination Administrator; System Notification Service

**User journey (12 steps):**
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

**Functional capabilities:**
- Display channel configuration summary for SMS, email, and in-app channels
- Capture and update SMS gateway provider settings with credential masking on display
- Capture and update email SMTP settings including TLS and sender identity
- Capture and update in-app notification default retention and display settings
- Execute test send per channel with administrator-supplied test recipient
- Enable or disable each channel independently for outbound dispatch
- Validate host, port, email address, and mobile number formats before save or test
- Persist encrypted credentials separate from non-secret connection metadata
- Record last test send outcome and timestamp per channel

**Inputs:** SMS gateway URL; SMS sender ID; SMS API key or credentials; SMS request timeout; SMTP host and port; SMTP TLS mode; SMTP username and password; Email from name and from address

**Outputs:** Channel configuration summary; Per-channel configuration detail with masked secrets; Test send success or failure result with provider response code; Validation errors for invalid connection settings; Channel enabled/disabled status

**Business rules:**
- At least one channel should remain enabled for production go-live (warning only, not hard block)
- Disabled channels must not be used for new dispatch attempts
- Credentials never returned in clear text after initial save
- Test send uses current saved configuration even if changed fields not yet saved (prompt to save first)
- Only Examination Administrator may view or change provider credentials

**Validations:**
- SMS gateway URL required; must be valid HTTPS URL
- SMS sender ID required; alphanumeric length per gateway policy
- SMS API credential required on first save
- SMTP host required; valid hostname or IP
- SMTP port required; integer 1–65535
- From email address required; valid RFC email format
- Test mobile number required for SMS test; valid national mobile format
- Test email required for email test; valid RFC email format

**Workflow / states:** CONFIGURED (settings saved) ↔ ENABLED (channel active for dispatch) ↔ DISABLED (channel inactive). Test send does not change workflow state but updates last_test_status metadata.

**Dependencies:**
- F01 Platform Role and Permission Catalog — administrator authorization
- F01 Examination Administrator Account Lifecycle — authenticated sessions
- F07-004 Multi-Channel Notification Dispatch Engine — consumes channel settings for outbound send

**Risks:** Incorrect SMTP TLS settings may block all email notifications until corrected; Credential rotation requires administrator coordination to avoid dispatch outages

---

#### F07-003 — Examination Lifecycle Event Subscription and Template Routing

**One-liner / description:** The notification service subscribes to domain events emitted by registration, scheduling, conduct, results, and certificate modules, maps each event type to configured templates and channels, and enqueues dispatch…

**Business objective:** Automate examination lifecycle notifications by reacting to authoritative business events from upstream modules without duplicating their approval or business logic, ensuring the correct template reaches the correct candidate channels whenever a lifecycle milestone occurs.

**Actors:** Examination Administrator; System Notification Service; Candidate Registration module; Examination Scheduling and Allocation module; Secure Examination Conduct module; Evaluation and Results module; Certificate Management module

**User journey (16 steps):**
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

**Functional capabilities:**
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

**Inputs:** Domain event type code; Domain event idempotency key; Candidate identifier and contact channels (mobile, email); Registration number; Examination name and schedule details; Allocated centre name and address; Hall ticket reference; Examination credentials reference

**Outputs:** Event-to-template mapping register rows; Enqueued dispatch job records per channel; Idempotent duplicate suppression outcome; Unmapped event error log entries; Dispatch intake queue monitor rows

**Business rules:**
- Notification service does not decide whether registration, payment, or allocation is approved—it reacts only to emitted events
- Each domain event type may have at most one active routing mapping
- Dispatch enqueue skipped for channels that are globally disabled
- Missing candidate contact channel skips that channel but may still enqueue others
- Duplicate event idempotency key must not create duplicate dispatch jobs
- Events must carry sufficient placeholder data for template rendering or enqueue fails with explicit error

**Validations:**
- Event type required; must exist in lifecycle catalog
- Idempotency key required; non-empty string
- Mapping save requires at least one channel with linked active template
- Template channel must match mapping channel selection
- Registration events require registration number and candidate mobile
- Payment confirmation events require payment reference and amount placeholder source
- Hall ticket events require hall ticket download reference token
- Credentials events must not include plaintext password in payload—only notification-safe fields

**Workflow / states:** Event RECEIVED → MAPPING_RESOLVED → JOBS_ENQUEUED → HANDED_OFF_TO_DISPATCH. Event RECEIVED → UNMAPPED (no active mapping, terminal log). Event RECEIVED → DUPLICATE_SUPPRESSED (idempotency hit, terminal). Event RECEIVED → ENQUEUE_FAILED (validation or missing template, terminal with error detail).

**Dependencies:**
- F05 Candidate Registration — emits registration and payment confirmation events
- F06 Examination Scheduling and Allocation — emits schedule, allocation, and hall ticket events
- F09 Secure Examination Conduct — emits reminder and credentials events
- F10 Evaluation and Results — emits results published events
- F11 Certificate Management — emits certificate available events
- F07-001 Notification Template Catalog — templates referenced by mappings
- F07-002 Channel Provider Configuration — channel enablement governs enqueue
- F07-004 Multi-Channel Notification Dispatch Engine — processes enqueued jobs

**Risks:** Event schema drift between modules may break placeholder resolution; High-volume schedule bulk updates may spike intake queue requiring operational monitoring

---

#### F07-004 — Multi-Channel Notification Dispatch Engine

**One-liner / description:** Background dispatch processing dequeues notification jobs created by lifecycle event intake, renders template placeholders from event payload snapshots, sends SMS and email through configured providers, writes in-app…

**Business objective:** Reliably deliver examination lifecycle messages across SMS, email, and in-app channels with traceable attempt history and controlled retry so candidates receive timely registration, scheduling, conduct, results, and certificate notifications.

**Actors:** System Notification Service; Examination Administrator

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Dispatch job identifier; Template snapshot reference; Event payload snapshot; Recipient mobile number; Recipient email address; Candidate portal user identifier for in-app; Channel type; Retry attempt count

**Outputs:** Provider message identifier for SMS or email; In-app inbox record identifier; Per-attempt delivery log rows; Terminal dispatch job status; Administrator job detail with attempt timeline

**Business rules:**
- Jobs for disabled channels fail fast without provider call
- Rendered messages must not include fields marked sensitive in event contract
- Retry applies only to classified transient provider errors
- Permanent failures (invalid number, hard bounce) do not retry
- Successful in-app write is terminal for that channel attempt even if SMS/email sibling fails
- Job processing must be idempotent per attempt number

**Validations:**
- Recipient mobile required for SMS jobs; valid format or fail permanent
- Recipient email required for email jobs; valid RFC format or fail permanent
- Candidate identifier required for in-app jobs
- Template snapshot must exist and be readable at processing time
- Rendered SMS must not exceed configured length after substitution
- Missing mandatory placeholder when policy is FAIL aborts attempt with logged reason

**Workflow / states:** Job PENDING → PROCESSING → ATTEMPT_SENT (per channel success) → COMPLETED (all channels terminal success or acceptable partial success per policy). Job PENDING → PROCESSING → ATTEMPT_FAILED → RETRY_PENDING → PROCESSING (loop) → EXHAUSTED_FAILED when max retries exceeded. Job PENDING → FAILED_FAST when channel disabled or permanent validation failure.

**Dependencies:**
- F07-002 Channel Provider Configuration — provider settings and enable flags
- F07-001 Notification Template Catalog — template content snapshots
- F07-003 Examination Lifecycle Event Subscription — job enqueue source
- F07-005 Delivery Status Tracking — persists attempt outcomes
- F07-007 Candidate Portal In-App Notification Inbox — displays in-app records

**Risks:** Provider outage may delay large batches until retries exhaust; Template placeholder mismatch at dispatch time causes avoidable failures if event payload changes retroactively

---

#### F07-005 — Delivery Status Tracking and Notification Register

**One-liner / description:** Examination Administrators monitor all outbound notification deliveries across SMS, email, and in-app channels through a searchable register with status filters, drill-down to attempt history and provider responses,…

**Business objective:** Give examination administrators full visibility into whether lifecycle notifications reached candidates, support troubleshooting of failed deliveries, and maintain auditable evidence of communication for registration through certificate milestones.

**Actors:** Examination Administrator; System Notification Service

**User journey (9 steps):**
1. Examination Administrator opens Notification Delivery Register.
2. Administrator applies filters for date range, channel, delivery status, and lifecycle event type.
3. Administrator searches by candidate registration number or mobile number.
4. Register lists deliveries with sent time, channel, event type, status chip, and recipient masked appropriately.
5. Administrator selects a row to open delivery detail view.
6. Detail view shows rendered message snapshot reference, each attempt timestamp, provider response code, and linked source event identifier.
7. Administrator exports current filtered result set to spreadsheet for offline review.
8. If no deliveries match filters, empty state explains criteria.
9. If register API fails, error state offers retry.

**Functional capabilities:**
- List notification deliveries with pagination
- Filter deliveries by date range, channel, status, and event type
- Search deliveries by registration number or mobile number
- Display delivery detail with multi-attempt history
- Show provider response codes and correlation identifiers
- Link delivery row to source domain event and dispatch job
- Export filtered delivery register to spreadsheet format
- Mask recipient contact details partial display in list view

**Inputs:** Date range filter; Channel filter; Delivery status filter; Lifecycle event type filter; Registration number search text; Mobile number search text; Export column selection default set

**Outputs:** Delivery register paginated rows; Delivery detail with attempt timeline; Exported spreadsheet file; Empty and error state messages

**Business rules:**
- Delivery statuses include PENDING, SENT, DELIVERED (if provider confirms), FAILED, RETRY_PENDING, EXHAUSTED_FAILED for SMS/email; READ/UNREAD applies only to in-app channel display
- Historical deliveries remain visible after template deactivation
- Export limited to administrator authorized scope (department-wide for Examination Administrator)
- Provider response codes stored as received without alteration

**Validations:**
- Date range start must be before or equal to end
- Registration number search minimum 3 characters when provided
- Mobile search must be numeric format when provided
- Export row limit enforced with message when exceeded

**Workflow / states:** Delivery attempt statuses transition PENDING → SENT → DELIVERED or FAILED → RETRY_PENDING → SENT/FAILED loops → EXHAUSTED_FAILED terminal. In-app deliveries transition UNREAD → READ when candidate opens notification (tracked in inbox feature).

**Dependencies:**
- F07-004 Multi-Channel Notification Dispatch Engine — produces delivery attempts
- F01 Platform Role and Permission Catalog — administrator access control

**Risks:** Large export queries may impact performance during peak examination periods

---

#### F07-006 — Resend Controls and Failed Delivery Recovery

**One-liner / description:** Examination Administrators resend failed or exhausted lifecycle notifications individually or in bulk from the delivery register, with eligibility checks against active templates and enabled channels, mandatory…

**Business objective:** Allow controlled recovery when SMS, email, or in-app notifications fail so candidates still receive registration, scheduling, hall ticket, reminder, credentials, results, or certificate messages without duplicating successful sends or bypassing governance rules.

**Actors:** Examination Administrator; System Notification Service; Candidate

**User journey (12 steps):**
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

**Functional capabilities:**
- Filter delivery register to failed and exhausted deliveries eligible for review
- Resend single failed notification with mandatory reason capture
- Bulk resend selected failed notifications with rate limit guard
- Validate resend eligibility against active template and enabled channel
- Block resend with explicit reason when template inactive or channel disabled
- Create resend audit record linked to original delivery identifier
- Display resend history on delivery detail
- Cancel pending resend job before dispatch starts
- Prevent duplicate resend while identical resend job already pending

**Inputs:** Original delivery identifier; Bulk selected delivery identifiers; Resend reason text; Optional channel override when original channel permanently failed and alternate configured; Cancel pending resend job identifier

**Outputs:** New dispatch job identifier for resend; Resend audit entries; Bulk resend outcome summary counts; Blocked resend reason message; Resend history list on delivery detail; Cancel confirmation outcome

**Business rules:**
- Resend reason mandatory minimum 10 characters
- Cannot resend deliveries that already reached SENT or DELIVERED terminal success unless department override flag enabled for duplicate resend warning
- Bulk resend maximum batch size enforced (configurable, e.g., 100)
- Resend uses current template content version active at resend time
- Each resend retains correlation to original source lifecycle event
- Cancel allowed only while resend job status is PENDING

**Validations:**
- Original delivery must exist and be in FAILED or EXHAUSTED_FAILED status
- Reason text required; length 10–500 characters
- Bulk selection must not exceed configured maximum
- Template for event type and channel must be active
- Channel must be enabled
- Duplicate pending resend for same delivery rejected

**Workflow / states:** Failed delivery → RESEND_REQUESTED → RESEND_PENDING (job queued) → RESEND_DISPATCHING → RESEND_SENT or RESEND_FAILED. RESEND_PENDING → RESEND_CANCELLED (administrator cancel). Bulk operation tracks per-item subprocess through same states.

**Dependencies:**
- F07-005 Delivery Status Tracking — source failed delivery rows
- F07-004 Multi-Channel Notification Dispatch Engine — processes resend jobs
- F07-001 Notification Template Catalog — active template validation
- F07-002 Channel Provider Configuration — channel enable validation

**Risks:** Bulk resend during misconfiguration may amplify provider errors; Using updated template at resend time may confuse candidates if content differs materially

---

#### F07-007 — Candidate Portal In-App Notification Inbox

**One-liner / description:** Candidates view examination lifecycle notifications delivered to the portal in-app channel through a paginated inbox with unread badge, notification detail view, mark-read actions, empty and error states, and…

**Business objective:** Ensure candidates have a durable in-portal record of examination communications when SMS or email is missed, with clear read status and secure access limited to their own notifications.

**Actors:** Candidate; System Notification Service

**User journey (10 steps):**
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

**Functional capabilities:**
- List candidate in-app notifications with pagination
- Display unread count badge on portal header
- Show notification detail with title, body, and received timestamp
- Mark single notification as read on detail open
- Mark all notifications as read for logged-in candidate
- Hide notifications older than configured retention unless already opened
- Prevent candidate access to another candidate notification records
- Render mobile-responsive inbox list and detail layouts
- Show inbox empty state and load error state

**Inputs:** Authenticated candidate session identifier; Pagination page number and size; Notification identifier for detail and mark-read; Mark all as read action

**Outputs:** Paginated inbox list rows; Unread notification count; Notification detail content; Updated read status; Empty and error state views

**Business rules:**
- Candidates see only notifications addressed to their portal account
- Unread count includes notifications with read status UNREAD within retention window
- Mark all as read updates only notifications currently visible under retention policy
- In-app notifications created only by dispatch engine for mapped lifecycle events
- Deleted upstream registration does not delete historical notifications but may hide future relevance in UI footnote

**Validations:**
- Session required for all inbox operations
- Notification identifier must belong to authenticated candidate or return not found
- Pagination page size maximum 50
- Mark-read on already read notification is idempotent success

**Workflow / states:** Notification UNREAD → READ on detail view open or explicit mark-read. Mark all transitions all UNREAD in retention window to READ. Archived notifications beyond retention hidden from list (terminal visibility state).

**Dependencies:**
- F05 Candidate Registration — candidate portal authentication session
- F07-004 Multi-Channel Notification Dispatch Engine — creates inbox records
- F07-002 Channel Provider Configuration — in-app retention settings

**Risks:** Candidates may rely solely on inbox and miss time-sensitive SMS if unread; Long retention may clutter inbox unless titles are clear

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 07 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 07 Notification Service** (7 features).
> Features: F07-001 Notification Template Catalog and Content Management; F07-002 SMS Email and In-App Channel Provider Configuration; F07-003 Examination Lifecycle Event Subscription and Template Routing; F07-004 Multi-Channel Notification Dispatch Engine; F07-005 Delivery Status Tracking and Notification Register; F07-006 Resend Controls and Failed Delivery Recovery; F07-007 Candidate Portal In-App Notification Inbox.
> Purpose: Template and channel configuration; lifecycle event routing; multi-channel dispatch; delivery tracking; resend/recovery; candidate in-app notification inbox.
> Draw: Event → route → template → channel dispatch architecture; Notification job state machine + resend linkage; Multi-channel sequence (SMS/Email/In-App); Admin delivery register + inbox UX flow; ERD for `notification_template`, `notification_channel_config`, `notification_event_route`, `notification_job`, `notification_delivery_attempt`, `in_app_notification`.
