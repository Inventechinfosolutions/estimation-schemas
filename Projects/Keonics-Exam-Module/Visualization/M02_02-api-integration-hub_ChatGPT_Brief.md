# ChatGPT Visualization Brief — Module 02: API Integration Hub

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 02 API Integration Hub
**Features:** 4 (F02-001 … F02-004)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 02 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Hub context map (Mod 05 + external KGID + Payment)
2. KGID lookup sequence (found / not-found / unavailable)
3. Payment initiate → callback → reconcile sequence
4. Transient vs permanent retry flowchart
5. Admin config swimlane + Hub ERD
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** API Integration Hub
**Purpose:** Integrate external KGID employee lookup and payment gateway; administer endpoints/credentials; shared retry and call-log observability for registration fee and identity flows.

**Actors (union across features):**
- Candidate Registration module consumer
- Examination Administrator
- External payment gateway
- System Integration Service

**Feature list:**
- **F02-001** — KGID Government Employee Lookup Integration
- **F02-002** — Payment Gateway Fee Transaction Integration
- **F02-003** — Integration Endpoint and Credential Administration
- **F02-004** — Integration Retry Logging and Error Observability

### DATA MODEL (from EXAM DB design v2.1)

- `integration_endpoint`
- `integration_credential`
- `integration_call_log`
- `kgid_lookup_cache`

### FEATURE CATALOGUE

#### F02-001 — KGID Government Employee Lookup Integration

**One-liner / description:** Implements the technical integration layer that accepts a government employee KGID number, validates it, calls the external KGID system, maps returned employee attributes into a canonical employee-detail payload,…

**Business objective:** Automate retrieval of government department employee information during Type 1 registration without manual data entry, while preserving audit evidence and controlled failure behavior when the KGID service is unavailable.

**Actors:** Examination Administrator; System Integration Service; Candidate Registration module consumer

**User journey (12 steps):**
1. Candidate Registration module receives a KGID number entered by a government department employee candidate during registration (presentation handled outside this feature).
2. System Integration Service validates KGID number format and normalizes input before any external call.
3. Service resolves active KGID integration configuration (endpoint, credentials, timeout, retry policy) from Integration Configuration administration.
4. Service authenticates to the external KGID API using configured credentials.
5. Service submits KGID lookup request with a generated correlation identifier.
6. On successful response, service maps available fields (employee name, KGID number, employee details) into the canonical employee-detail structure.
7. Service persists request metadata, response snapshot, outcome status, and correlation identifier for audit.
8. Service returns mapped employee details to the registration consumer for candidate confirmation (confirmation UI is outside this feature).
9. If KGID record is not found, service returns a structured not-found outcome without partial employee data.
10. If KGID API returns transient errors, service applies configured retry policy via the integration retry framework and either succeeds or returns service-unavailable after retry exhaustion.
11. If KGID API returns permanent errors (invalid credentials, authorization denied), service logs classified error, skips further retry, and returns a controlled failure outcome.
12. Examination Administrator may later review KGID lookup logs through Integration Observability when investigating registration failures.

**Functional capabilities:**
- Accept KGID lookup requests from authorized internal registration consumers
- Validate KGID number format prior to external invocation
- Authenticate against configured KGID external API credentials
- Invoke external KGID lookup by KGID number
- Map external KGID response fields into canonical employee name, KGID number, and employee details structure
- Return structured found outcome with mapped employee attributes when data is available
- Return structured not-found outcome when KGID has no matching employee record
- Return structured service-unavailable outcome when external API is down or retry is exhausted
- Persist auditable KGID lookup request and response snapshot with correlation identifier
- Emit integration call records to shared logging and retry framework
- Apply KGID-specific timeout and retry binding using shared retry policy engine

**Inputs:** KGID number; Registration correlation or session reference from consuming module; Active KGID integration configuration profile; Encrypted KGID API credentials; Retry and timeout policy parameters

**Outputs:** Canonical employee detail payload (employee name, KGID number, employee details when available); Structured not-found outcome; Structured service-unavailable outcome; Structured permanent integration failure outcome; KGID lookup audit record with correlation identifier; Integration call log entry with timing and classified error

**Business rules:**
- KGID lookup is mandatory input path for government department employee registration flows; this feature does not determine registration eligibility
- Only fields returned by the external KGID API and mapped by configuration shall be included; missing fields are omitted rather than invented
- Retrieved information availability is subject to external API and data availability as stated in the source document
- Lookup outcomes must be auditable and traceable by correlation identifier
- External KGID credentials must never be returned to registration consumers or written unredacted to operational logs
- Not-found and unavailable outcomes must be distinguishable for downstream registration handling

**Validations:**
- KGID number must be present and non-blank
- KGID number must match approved format pattern before external call
- KGID number length must fall within configured minimum and maximum bounds
- KGID number must not contain disallowed characters after normalization
- Integration configuration for KGID type must be active before lookup is attempted
- External response must contain minimum identifiable employee reference before mapped as found
- Mapped employee name must not be empty when found outcome is returned
- Duplicate concurrent lookup for same KGID within same correlation context must reuse or reject per idempotency rule without duplicate external calls

**Workflow / states:** States: LOOKUP_REQUESTED → FORMAT_VALIDATED → CONFIG_RESOLVED → EXTERNAL_CALL_IN_PROGRESS → (MAPPING_COMPLETED | NOT_FOUND | TRANSIENT_ERROR | PERMANENT_ERROR | SERVICE_UNAVAILABLE). Transitions: LOOKUP_REQUESTED to FORMAT_VALIDATED on successful field validation; FORMAT_VALIDATED to CONFIG_RESOLVED when active KGID profile loaded; CONFIG_RESOLVED to EXTERNAL_CALL_IN_PROGRESS on authenticated outbound call; EXTERNAL_CALL_IN_PROGRESS to MAPPING_COMPLETED when employee record returned and mapped; EXTERNAL_CALL_IN_PROGRESS to NOT_FOUND when external system reports no record; EXTERNAL_CALL_IN_PROGRESS to TRANSIENT_ERROR on timeout or retryable HTTP or gateway fault; TRANSIENT_ERROR to EXTERNAL_CALL_IN_PROGRESS on retry attempt; TRANSIENT_ERROR to SERVICE_UNAVAILABLE when retry maximum exceeded; EXTERNAL_CALL_IN_PROGRESS to PERMANENT_ERROR on authentication or authorization failure; MAPPING_COMPLETED, NOT_FOUND, PERMANENT_ERROR, and SERVICE_UNAVAILABLE to AUDIT_PERSISTED on log write completion.

**Dependencies:**
- F01 Platform Role and Permission Catalog for Examination Administrator access to related configuration and logs
- F01 Staff Authentication Session and Credential Policy for administrator sessions
- F02-003 Integration Endpoint and Credential Administration for KGID endpoint and credential profiles
- F02-004 Integration Retry Logging and Error Observability for retry execution and call logging
- Module 05 Candidate Registration consumes lookup outcomes; registration confirmation UI is out of scope for this feature

**Risks:** KGID API downtime blocks automated employee verification for government department candidates; External schema changes may require mapping updates; Incomplete external data may limit auto-population despite successful lookup

**Notes:** Provides backend KGID connectivity consumed by Candidate Registration; does not include registration UI or fee logic.

---

#### F02-002 — Payment Gateway Fee Transaction Integration

**One-liner / description:** Implements payment gateway connectivity for online examination fee processing including payment session initiation, capture of gateway transaction references, asynchronous success and failure callback processing with…

**Business objective:** Enable secure, traceable online examination fee collection through an external payment gateway with reliable status synchronization so registration can complete only after confirmed successful payment where applicable.

**Actors:** Examination Administrator; System Integration Service; Candidate Registration module consumer; External payment gateway

**User journey (15 steps):**
1. Candidate Registration module determines that payment is mandatory and supplies payable amount and registration payment reference to this integration (fee rules are outside this feature).
2. System Integration Service validates payment initiation input including positive amount and registration reference presence.
3. Service loads active payment gateway configuration and decrypts credentials.
4. Service authenticates with payment gateway and creates payment initiation request.
5. Service receives gateway session or redirect payload including gateway transaction reference.
6. Service persists payment transaction record in initiated state with internal reference and gateway transaction reference.
7. Candidate completes payment on gateway channel (gateway-hosted flow; presentation outside this feature).
8. Payment gateway posts asynchronous status callback to integration callback endpoint.
9. Service verifies callback authenticity using gateway signature or shared secret rules.
10. Service classifies callback as success or failure and locates matching initiated transaction by gateway reference.
11. On success callback, service transitions transaction to successful state, captures final gateway transaction reference and timestamp, and notifies registration consumer.
12. On failure callback, service transitions transaction to failed state with failure reason code and notifies registration consumer.
13. If callback is delayed, registration consumer may request current payment status by internal reference; service queries gateway status endpoint when supported and reconciles local state.
14. Duplicate success callbacks for the same gateway reference are processed idempotently without duplicate financial completion signals.
15. Examination Administrator reviews payment integration logs and transaction audit via observability and configuration features when resolving reconciliation issues.

**Functional capabilities:**
- Initiate examination fee payment session with external payment gateway
- Persist internal payment transaction with initiated status and registration reference
- Capture gateway transaction reference at initiation
- Receive asynchronous payment gateway status callbacks
- Verify payment callback authenticity signature or checksum
- Transition payment transaction to successful state on verified success callback
- Transition payment transaction to failed state on verified failure callback
- Retrieve payment transaction status by internal registration payment reference
- Query payment gateway for current status when callback is delayed
- Enforce idempotent processing for duplicate callbacks sharing the same gateway transaction reference
- Persist callback event history for each payment transaction
- Return structured outcomes for initiation failure, callback rejection, and unknown transaction reference

**Inputs:** Registration payment reference from Candidate Registration module; Payable fee amount; Candidate redirect return URLs supplied by registration consumer; Active payment gateway integration configuration; Encrypted payment gateway credentials; Gateway callback payload with transaction reference and status; Gateway callback signature or authentication headers

**Outputs:** Payment initiation payload for candidate redirect or gateway session; Internal payment transaction identifier; Gateway transaction reference; Payment status outcome (initiated, successful, failed, unknown); Callback event audit entries; Structured reconciliation detail for registration confirmation storage

**Business rules:**
- Registration completion after payment is enforced by Candidate Registration; this feature supplies authoritative payment status only
- Payment transaction reference and gateway transaction reference must be captured for successful payments
- Failed payment must not mark transaction as successful
- Duplicate success callbacks must not create duplicate successful financial completion events
- Payment amount at initiation must match amount supplied by registration consumer; this feature does not calculate applicable fee
- All callback processing must occur only after signature or authenticity verification passes
- Transaction state transitions must be monotonic: initiated to successful or initiated to failed; successful cannot revert to failed without manual administrative intervention outside automated callback flow

**Validations:**
- Registration payment reference must be present
- Payable amount must be greater than zero for chargeable registrations
- Payable amount must not exceed configured maximum single-transaction limit
- Payment gateway configuration must be active before initiation
- Callback payload must include gateway transaction reference
- Callback signature must match gateway verification rules
- Callback referencing unknown gateway transaction reference must be rejected and logged
- Callback amount must match persisted initiated transaction amount when amount is present in callback

**Workflow / states:** States: PAYMENT_INITIATED → (PAYMENT_SUCCESSFUL | PAYMENT_FAILED | PAYMENT_UNKNOWN). Transitions: PAYMENT_INITIATED created on successful gateway session creation; PAYMENT_INITIATED to PAYMENT_SUCCESSFUL on verified success callback or reconciled success status query; PAYMENT_INITIATED to PAYMENT_FAILED on verified failure callback or reconciled failure status query; PAYMENT_INITIATED remains PAYMENT_UNKNOWN when callback not yet received and status query inconclusive; duplicate success callback while already PAYMENT_SUCCESSFUL transitions to IDEMPOTENT_NOOP with audit entry only.

**Dependencies:**
- F01 Platform Role and Permission Catalog for administrator access to related logs and configuration
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for payment gateway profiles
- F02-004 Integration Retry Logging and Error Observability for initiation and status query logging
- Module 05 Candidate Registration supplies payable amount and consumes payment outcomes; fee rule determination and attempt history are out of scope

**Risks:** Delayed or lost callbacks may leave transactions in unknown state until status query reconciliation; Gateway schema or signature rule changes require urgent mapping updates; Duplicate or out-of-order callbacks may cause reconciliation complexity without strict idempotency

**Notes:** Covers fee payment initiation, asynchronous status callback, and transaction reference capture; fee amount determination remains in Candidate Registration.

---

#### F02-003 — Integration Endpoint and Credential Administration

**One-liner / description:** Provides Examination Administrator capabilities to configure, update, and test KGID and payment gateway integration profiles including endpoint URLs, timeout and retry parameters, active status, and encrypted…

**Business objective:** Allow authorized administrators to manage external integration connectivity settings securely without code deployments, enabling environment-specific endpoints and credential lifecycle control for KGID lookup and fee payment flows.

**Actors:** Examination Administrator

**User journey (13 steps):**
1. Examination Administrator signs in through staff authentication governed by User and Role Management.
2. Administrator opens Integration Configuration register listing KGID and payment gateway profiles with active or inactive status.
3. If no profiles exist, administrator sees empty state guidance to create first integration profile.
4. Administrator selects KGID profile to create or edit endpoint URL, timeout seconds, retry attempt limit, and active flag.
5. Administrator enters or rotates KGID API credentials in masked credential form and confirms rotation in confirmation dialog.
6. Administrator saves KGID configuration; system validates URL format and numeric timeout bounds and persists encrypted credentials.
7. Administrator runs KGID connection test; system displays success or structured failure message in connection test result dialog.
8. Administrator selects payment gateway profile to create or edit initiation URL, callback path identifier, status query URL if applicable, timeout, and active flag.
9. Administrator enters or rotates payment gateway merchant credentials and callback signing secret in masked form.
10. Administrator saves payment gateway configuration with field-level validation errors shown inline on failure.
11. Administrator runs payment gateway connection test; system displays test outcome dialog.
12. Each save or credential rotation writes configuration change audit entry with administrator identity and timestamp.
13. Administrator returns to register to verify updated status chips and last-tested timestamp if displayed.

**Functional capabilities:**
- List integration configuration profiles by integration type and active status
- Display empty state when no integration profiles are configured
- Create KGID integration endpoint configuration profile
- Update KGID integration endpoint configuration profile
- Create payment gateway integration endpoint configuration profile
- Update payment gateway integration endpoint configuration profile
- Store integration credentials encrypted at rest
- Rotate integration credentials without exposing prior secret values in UI
- Execute live connectivity test against KGID endpoint using stored credentials
- Execute live connectivity test against payment gateway endpoint using stored credentials
- Record configuration change audit trail for create, update, and credential rotation events
- Restrict configuration management to authorized Examination Administrator roles

**Inputs:** KGID endpoint URL; KGID API key or client credentials; KGID timeout seconds; KGID retry attempt limit; Payment gateway initiation endpoint URL; Payment gateway status query endpoint URL; Payment gateway merchant identifier and secret; Payment gateway callback signing secret

**Outputs:** Saved integration configuration profiles; Masked credential metadata showing rotation timestamp without secret exposure; Connection test success or failure result messages; Configuration change audit records; Validation error messages for invalid URLs and out-of-range timeout values

**Business rules:**
- Only one active KGID profile and one active payment gateway profile may be designated per environment unless explicitly configured otherwise
- Credential values must never be returned in full after initial save; UI shows masked placeholders only
- Deactivating a profile prevents new lookup or payment initiation calls from using that profile
- Configuration changes must be auditable with administrator identity
- Connection test must not mutate production financial state for payment gateway beyond provider-permitted ping or token exchange

**Validations:**
- Endpoint URL must be valid HTTPS URL format
- Timeout seconds must be positive integer within configured maximum
- Retry attempt limit must be non-negative integer within configured maximum
- KGID credentials must be provided on create and on rotation
- Payment gateway merchant identifier must be non-blank
- Payment gateway secret must be provided on create and on rotation
- Callback signing secret must meet minimum length requirement
- Active flag must be boolean

**Workflow / states:** Configuration states: DRAFT → ACTIVE → INACTIVE. Transitions: DRAFT to ACTIVE when administrator activates saved valid profile; ACTIVE to INACTIVE when administrator deactivates profile; INACTIVE to ACTIVE on reactivation after validation; credential rotation while ACTIVE creates new credential version then retires prior version on successful save.

**Dependencies:**
- F01 Platform Role and Permission Catalog defining Examination Administrator integration configuration permissions
- F01 Examination Administrator Account Lifecycle for administrator identities
- F01 Staff Authentication Session and Credential Policy
- F01 Downstream Module Authorization Integration Hooks for permission enforcement on configuration APIs
- F02-001 KGID Government Employee Lookup Integration consumes KGID profiles
- F02-002 Payment Gateway Fee Transaction Integration consumes payment gateway profiles

**Risks:** Misconfigured endpoints or expired credentials cause registration KGID lookup or payment outages; Credential rotation errors may invalidate in-flight payment sessions if coordinated downtime is not observed

**Notes:** Administrator-facing configuration for KGID and payment gateway connectivity; excludes registration business parameters.

---

#### F02-004 — Integration Retry Logging and Error Observability

**One-liner / description:** Delivers shared integration observability and resilience capabilities including structured call logging with correlation identifiers, transient versus permanent error classification, configurable retry execution for…

**Business objective:** Ensure KGID and payment integrations operate reliably under failure conditions with auditable evidence and administrator visibility into errors, retries, and outcomes without exposing secrets.

**Actors:** Examination Administrator; System Integration Service

**User journey (11 steps):**
1. System Integration Service initiates any KGID lookup or payment gateway call and assigns correlation identifier propagated from registration context where supplied.
2. Service records call attempt with integration type, endpoint, start time, and requesting service identity.
3. On transient failure such as timeout or gateway error, service classifies error as transient and schedules retry according to active profile retry limit.
4. Each retry attempt appends retry history linked to parent call with attempt number and outcome.
5. On permanent failure such as authentication rejection, service classifies error as permanent, skips further retry, and marks call failed.
6. On success, service records completion timing and outcome status with redacted request and response payload excerpts.
7. Examination Administrator opens Integration Call Log register filtered by date range, integration type, outcome status, and correlation identifier fragment.
8. Administrator selects a log row to open read-only detail view showing attempt timeline, error classification, and redacted payload excerpts.
9. If no logs match filters, administrator sees empty state message.
10. Administrator exports filtered log result set to file for incident analysis or audit request.
11. Administrator uses log evidence to coordinate credential rotation or endpoint correction in Integration Configuration administration.

**Functional capabilities:**
- Record integration call attempt with correlation identifier and integration type
- Append retry attempt history records linked to parent integration call
- Classify integration errors as transient or permanent
- Execute retry policy for transient errors until success or retry limit exceeded
- Skip retry for permanent errors
- Redact credentials and secrets from persisted log payloads
- List integration call logs with date, type, status, and correlation filters
- Retrieve integration call log detail with attempt timeline
- Export filtered integration call logs for administrator download
- Restrict log register and export to authorized Examination Administrator roles

**Inputs:** Integration type (KGID lookup or payment gateway operation); Correlation identifier from consuming flow; Request metadata and redacted payload excerpts; HTTP or gateway status codes and error messages; Retry policy parameters from integration configuration profile; Administrator filter criteria for log register

**Outputs:** Integration call log entries with outcome status; Retry attempt history records; Error classification label per failed attempt; Administrator log register rows; Exported log file for filtered result set; Structured permanent versus transient failure signals to calling integration features

**Business rules:**
- Every external KGID and payment gateway call must produce a log record regardless of outcome
- Retry attempts must not exceed configured maximum for the active integration profile
- Permanent errors must never trigger automatic retry
- Secrets, API keys, and card-related data must be redacted before persistence
- Log export must respect same authorization scope as log register viewing
- Correlation identifier must be preserved across retry attempts for a single logical operation

**Validations:**
- Correlation identifier must be non-blank when supplied by consumer
- Integration type must be one of supported values (KGID, payment gateway)
- Retry attempt number must increment monotonically per parent call
- Log list date-from must be before or equal to date-to
- Export row limit must not exceed configured maximum export size
- Administrator must hold integration observability permission to access log detail and export

**Workflow / states:** Call lifecycle states: CALL_STARTED → (CALL_SUCCEEDED | RETRY_SCHEDULED | CALL_FAILED_PERMANENT | CALL_FAILED_EXHAUSTED). Transitions: CALL_STARTED to CALL_SUCCEEDED on successful external response; CALL_STARTED to RETRY_SCHEDULED on transient error when retries remain; RETRY_SCHEDULED to CALL_STARTED on next attempt execution; RETRY_SCHEDULED to CALL_FAILED_EXHAUSTED when retry limit reached; CALL_STARTED to CALL_FAILED_PERMANENT on permanent error classification without entering RETRY_SCHEDULED.

**Dependencies:**
- F01 Platform Role and Permission Catalog for observability permission
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for retry limit and timeout parameters
- F02-001 KGID Government Employee Lookup Integration emits and consumes logging and retry behavior
- F02-002 Payment Gateway Fee Transaction Integration emits and consumes logging and retry behavior

**Risks:** High registration volume may produce large log volume requiring archival strategy outside this feature; Incorrect transient classification may cause unnecessary load on failing external systems; Insufficient redaction rules may expose secrets if gateway payloads change format

**Notes:** Shared cross-cutting capability supporting KGID lookup and payment gateway flows with administrator log review.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 02 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 02 API Integration Hub** (4 features).
> Features: F02-001 KGID Government Employee Lookup Integration; F02-002 Payment Gateway Fee Transaction Integration; F02-003 Integration Endpoint and Credential Administration; F02-004 Integration Retry Logging and Error Observability.
> Purpose: Integrate external KGID employee lookup and payment gateway; administer endpoints/credentials; shared retry and call-log observability for registration fee and identity flows.
> Draw: Hub context map (Mod 05 + external KGID + Payment); KGID lookup sequence (found / not-found / unavailable); Payment initiate → callback → reconcile sequence; Transient vs permanent retry flowchart; ERD for `integration_endpoint`, `integration_credential`, `integration_call_log`, `kgid_lookup_cache`.
