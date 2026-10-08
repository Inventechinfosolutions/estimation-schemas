# Module 02: API Integration Hub

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 4 (F02-001 … F02-004)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 02 API Integration Hub

451.8 hours · 87 tasks · Platform

External system connectivity for KGID employee lookup and online examination fee payment processing.

### F02-001 KGID Government Employee Lookup Integration

66.7 hours · Go-live · 17 tasks

##### Description

Implements the technical integration layer that accepts a government employee KGID number, validates it, calls the external KGID system, maps returned employee attributes into a canonical employee-detail payload, persists an auditable lookup record, and exposes lookup outcomes (found, not found, unavailable) to downstream registration flows. Subject to API and data availability as stated in the source document.

##### Business objective

Automate retrieval of government department employee information during Type 1 registration without manual data entry, while preserving audit evidence and controlled failure behavior when the KGID service is unavailable.

##### Actors

- Examination Administrator
- System Integration Service
- Candidate Registration module consumer

##### User journey

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

##### Functional capabilities

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

##### Inputs

- KGID number
- Registration correlation or session reference from consuming module
- Active KGID integration configuration profile
- Encrypted KGID API credentials
- Retry and timeout policy parameters

##### Outputs

- Canonical employee detail payload (employee name, KGID number, employee details when available)
- Structured not-found outcome
- Structured service-unavailable outcome
- Structured permanent integration failure outcome
- KGID lookup audit record with correlation identifier
- Integration call log entry with timing and classified error

##### Business rules

- KGID lookup is mandatory input path for government department employee registration flows; this feature does not determine registration eligibility
- Only fields returned by the external KGID API and mapped by configuration shall be included; missing fields are omitted rather than invented
- Retrieved information availability is subject to external API and data availability as stated in the source document
- Lookup outcomes must be auditable and traceable by correlation identifier
- External KGID credentials must never be returned to registration consumers or written unredacted to operational logs
- Not-found and unavailable outcomes must be distinguishable for downstream registration handling

##### Validations

- KGID number must be present and non-blank
- KGID number must match approved format pattern before external call
- KGID number length must fall within configured minimum and maximum bounds
- KGID number must not contain disallowed characters after normalization
- Integration configuration for KGID type must be active before lookup is attempted
- External response must contain minimum identifiable employee reference before mapped as found
- Mapped employee name must not be empty when found outcome is returned
- Duplicate concurrent lookup for same KGID within same correlation context must reuse or reject per idempotency rule without duplicate external calls

##### Calculations

- None; this feature performs retrieval and mapping only and does not compute registration fees or attempt history

##### Workflow

States: LOOKUP_REQUESTED → FORMAT_VALIDATED → CONFIG_RESOLVED → EXTERNAL_CALL_IN_PROGRESS → (MAPPING_COMPLETED | NOT_FOUND | TRANSIENT_ERROR | PERMANENT_ERROR | SERVICE_UNAVAILABLE). Transitions: LOOKUP_REQUESTED to FORMAT_VALIDATED on successful field validation; FORMAT_VALIDATED to CONFIG_RESOLVED when active KGID profile loaded; CONFIG_RESOLVED to EXTERNAL_CALL_IN_PROGRESS on authenticated outbound call; EXTERNAL_CALL_IN_PROGRESS to MAPPING_COMPLETED when employee record returned and mapped; EXTERNAL_CALL_IN_PROGRESS to NOT_FOUND when external system reports no record; EXTERNAL_CALL_IN_PROGRESS to TRANSIENT_ERROR on timeout or retryable HTTP or gateway fault; TRANSIENT_ERROR to EXTERNAL_CALL_IN_PROGRESS on retry attempt; TRANSIENT_ERROR to SERVICE_UNAVAILABLE when retry maximum exceeded; EXTERNAL_CALL_IN_PROGRESS to PERMANENT_ERROR on authentication or authorization failure; MAPPING_COMPLETED, NOT_FOUND, PERMANENT_ERROR, and SERVICE_UNAVAILABLE to AUDIT_PERSISTED on log write completion.

##### Search requirements

- Examination Administrator search of KGID lookup audit records by KGID number, correlation identifier, outcome status, and date range via Integration Observability feature

##### Documents

- KGID integration technical specification for developers
- Operations runbook for KGID API outage handling

##### Reports

- None within this feature; operational review uses integration call log register from F02-004

##### Notifications

- None; registration module handles candidate-facing messaging

##### Security

- KGID credentials retrieved only from encrypted credential store at runtime
- Internal lookup operations restricted to authorized registration service identities
- Response snapshots stored with field-level redaction policy for sensitive attributes if present in external payload
- All lookup attempts logged with actor or service identity and correlation identifier

##### Integrations

- External KGID government employee information API

##### Dependencies

- F01 Platform Role and Permission Catalog for Examination Administrator access to related configuration and logs
- F01 Staff Authentication Session and Credential Policy for administrator sessions
- F02-003 Integration Endpoint and Credential Administration for KGID endpoint and credential profiles
- F02-004 Integration Retry Logging and Error Observability for retry execution and call logging
- Module 05 Candidate Registration consumes lookup outcomes; registration confirmation UI is out of scope for this feature

##### Assumptions

- External KGID API exposes authenticated lookup by KGID number with employee name and employee details fields or equivalents mappable to canonical structure
- KGID API availability and field completeness may vary; partial payloads are handled without failing entire registration integration contract
- Network egress to KGID endpoints is permitted from application runtime environment
- Canonical employee detail schema is agreed with Candidate Registration module consumers before go-live

##### Risks

- KGID API downtime blocks automated employee verification for government department candidates
- External schema changes may require mapping updates
- Incomplete external data may limit auto-population despite successful lookup

##### Non-functional requirements

- Lookup operations must complete within configured timeout with retry for transient failures
- Audit records retained per enterprise retention policy
- Integration must support concurrent lookup volume during registration peaks
- Structured error codes suitable for downstream registration UX handling

##### Notes

Provides backend KGID connectivity consumed by Candidate Registration; does not include registration UI or fee logic.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| Integration | Authenticate with external KGID API using configured credentials | Medium | 16 |
| Integration | Fetch government employee record by KGID number from external KGID API | Easy | 8 |
| Integration | Map external KGID response fields to canonical employee detail structure | Medium | 16 |
| Integration | KGID-specific timeout and retry policy binding to shared retry engine | Simple | 4 |
| API | Lookup government employee by KGID number for registration consumers | Medium | 6 |
| API | Validate KGID number format before external lookup invocation | Easy | 4 |
| API | Return structured not-found outcome when KGID has no employee record | Easy | 4 |
| API | Return structured service-unavailable outcome when KGID API is unreachable after retry | Medium | 6 |
| Database | KGID lookup transaction log with correlation identifier and outcome status | Easy | 0.25 |
| Database | KGID lookup response snapshot storage for audit review | Medium | 0.3 |
| Testing | Successful employee retrieval with all available mapped fields | Medium | 0.3 |
| Testing | KGID not found in external system response handling | Easy | 0.25 |
| Testing | Malformed and out-of-pattern KGID number rejection | Easy | 0.25 |
| Testing | External API timeout with retry exhaustion to service-unavailable | Complex | 0.5 |
| Testing | KGID API authentication and authorization failure without retry | Medium | 0.3 |
| Documentation | KGID integration technical specification for developers | Medium | 0.3 |
| Documentation | Operations runbook for KGID API outage and recovery | Easy | 0.25 |

### F02-002 Payment Gateway Fee Transaction Integration

120.1 hours · Go-live · 23 tasks

##### Description

Implements payment gateway connectivity for online examination fee processing including payment session initiation, capture of gateway transaction references, asynchronous success and failure callback processing with signature verification, payment status retrieval, idempotent callback handling, and auditable payment transaction persistence for registration flows where payment is mandatory.

##### Business objective

Enable secure, traceable online examination fee collection through an external payment gateway with reliable status synchronization so registration can complete only after confirmed successful payment where applicable.

##### Actors

- Examination Administrator
- System Integration Service
- Candidate Registration module consumer
- External payment gateway

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Registration payment reference from Candidate Registration module
- Payable fee amount
- Candidate redirect return URLs supplied by registration consumer
- Active payment gateway integration configuration
- Encrypted payment gateway credentials
- Gateway callback payload with transaction reference and status
- Gateway callback signature or authentication headers

##### Outputs

- Payment initiation payload for candidate redirect or gateway session
- Internal payment transaction identifier
- Gateway transaction reference
- Payment status outcome (initiated, successful, failed, unknown)
- Callback event audit entries
- Structured reconciliation detail for registration confirmation storage

##### Business rules

- Registration completion after payment is enforced by Candidate Registration; this feature supplies authoritative payment status only
- Payment transaction reference and gateway transaction reference must be captured for successful payments
- Failed payment must not mark transaction as successful
- Duplicate success callbacks must not create duplicate successful financial completion events
- Payment amount at initiation must match amount supplied by registration consumer; this feature does not calculate applicable fee
- All callback processing must occur only after signature or authenticity verification passes
- Transaction state transitions must be monotonic: initiated to successful or initiated to failed; successful cannot revert to failed without manual administrative intervention outside automated callback flow

##### Validations

- Registration payment reference must be present
- Payable amount must be greater than zero for chargeable registrations
- Payable amount must not exceed configured maximum single-transaction limit
- Payment gateway configuration must be active before initiation
- Callback payload must include gateway transaction reference
- Callback signature must match gateway verification rules
- Callback referencing unknown gateway transaction reference must be rejected and logged
- Callback amount must match persisted initiated transaction amount when amount is present in callback
- Callback currency must match configured gateway currency when currency is present
- Status query request must include valid internal payment transaction reference

##### Calculations

- None; payable amount is supplied by Candidate Registration module

##### Workflow

States: PAYMENT_INITIATED → (PAYMENT_SUCCESSFUL | PAYMENT_FAILED | PAYMENT_UNKNOWN). Transitions: PAYMENT_INITIATED created on successful gateway session creation; PAYMENT_INITIATED to PAYMENT_SUCCESSFUL on verified success callback or reconciled success status query; PAYMENT_INITIATED to PAYMENT_FAILED on verified failure callback or reconciled failure status query; PAYMENT_INITIATED remains PAYMENT_UNKNOWN when callback not yet received and status query inconclusive; duplicate success callback while already PAYMENT_SUCCESSFUL transitions to IDEMPOTENT_NOOP with audit entry only.

##### Search requirements

- Examination Administrator search of payment transactions by internal reference, gateway transaction reference, status, and date range through integration logs and transaction audit views

##### Documents

- Payment gateway integration technical notes
- Finance reconciliation runbook for examination fee transactions

##### Reports

- None dedicated; reconciliation uses persisted transaction and callback history accessible to administrators

##### Notifications

- None within this feature; Candidate Registration and Notification Service handle candidate-facing payment confirmations

##### Security

- Payment gateway credentials stored encrypted and never logged in plaintext
- Callback endpoint protected against replay using signature verification and idempotency keys
- Internal status APIs restricted to authorized registration service identities
- PCI-sensitive card data never stored; gateway-hosted collection assumed

##### Integrations

- External online payment gateway for fee initiation
- External payment gateway asynchronous status callback channel
- External payment gateway transaction status query when supported by provider

##### Dependencies

- F01 Platform Role and Permission Catalog for administrator access to related logs and configuration
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for payment gateway profiles
- F02-004 Integration Retry Logging and Error Observability for initiation and status query logging
- Module 05 Candidate Registration supplies payable amount and consumes payment outcomes; fee rule determination and attempt history are out of scope

##### Assumptions

- Selected payment gateway supports server-to-server initiation and asynchronous callback notification
- Gateway provides verifiable callback signature mechanism
- Registration module persists payment details only after receiving successful status from this integration
- Single currency configuration per examination fee payment context

##### Risks

- Delayed or lost callbacks may leave transactions in unknown state until status query reconciliation
- Gateway schema or signature rule changes require urgent mapping updates
- Duplicate or out-of-order callbacks may cause reconciliation complexity without strict idempotency

##### Non-functional requirements

- Callback processing must be durable and idempotent under at-least-once delivery
- Initiation and callback handling must support registration peak load
- End-to-end audit trail linking registration reference, internal transaction id, and gateway reference
- Configurable timeout for status query reconciliation

##### Notes

Covers fee payment initiation, asynchronous status callback, and transaction reference capture; fee amount determination remains in Candidate Registration.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| Integration | Authenticate with payment gateway for transaction session creation | Medium | 16 |
| Integration | Initiate examination fee payment transaction with external payment gateway | Medium | 16 |
| Integration | Parse payment gateway success callback payload fields | Medium | 16 |
| Integration | Parse payment gateway failure callback payload fields | Easy | 8 |
| Integration | Verify payment gateway callback authenticity signature | Medium | 16 |
| Integration | Query payment status by gateway transaction reference | Easy | 8 |
| API | Create payment initiation request with registration reference and amount | Complex | 8 |
| API | Receive asynchronous payment status callback from gateway | Complex | 8 |
| API | Retrieve payment transaction status by internal registration payment reference | Medium | 6 |
| API | Persist gateway transaction reference on successful initiation response | Easy | 4 |
| API | Mark payment transaction failed from verified gateway failure callback | Easy | 4 |
| API | Mark payment transaction successful from verified gateway success callback | Medium | 6 |
| Database | Payment transaction core entity with status and reference fields | Medium | 0.3 |
| Database | Payment callback event history for idempotent callback processing | Medium | 0.3 |
| Database | Unique constraints on gateway transaction reference | Complex | 0.5 |
| Testing | Successful payment initiation followed by verified success callback | Complex | 0.5 |
| Testing | Payment initiation input validation for missing reference and invalid amount | Medium | 0.3 |
| Testing | Verified failure callback transitions transaction to failed state | Medium | 0.3 |
| Testing | Duplicate success callback idempotency without duplicate completion signal | Complex | 0.5 |
| Testing | Invalid or tampered callback signature rejection | Complex | 0.5 |
| Testing | Delayed callback reconciliation via status query endpoint | Medium | 0.3 |
| Documentation | Payment gateway integration technical notes for developers | Medium | 0.3 |
| Documentation | Finance reconciliation runbook for examination administrators | Medium | 0.3 |

### F02-003 Integration Endpoint and Credential Administration

175 hours · Go-live · 28 tasks

##### Description

Provides Examination Administrator capabilities to configure, update, and test KGID and payment gateway integration profiles including endpoint URLs, timeout and retry parameters, active status, and encrypted credential storage with rotation support and configuration change audit.

##### Business objective

Allow authorized administrators to manage external integration connectivity settings securely without code deployments, enabling environment-specific endpoints and credential lifecycle control for KGID lookup and fee payment flows.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

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

##### Inputs

- KGID endpoint URL
- KGID API key or client credentials
- KGID timeout seconds
- KGID retry attempt limit
- Payment gateway initiation endpoint URL
- Payment gateway status query endpoint URL
- Payment gateway merchant identifier and secret
- Payment gateway callback signing secret
- Payment gateway timeout seconds
- Active or inactive status flag per profile

##### Outputs

- Saved integration configuration profiles
- Masked credential metadata showing rotation timestamp without secret exposure
- Connection test success or failure result messages
- Configuration change audit records
- Validation error messages for invalid URLs and out-of-range timeout values

##### Business rules

- Only one active KGID profile and one active payment gateway profile may be designated per environment unless explicitly configured otherwise
- Credential values must never be returned in full after initial save; UI shows masked placeholders only
- Deactivating a profile prevents new lookup or payment initiation calls from using that profile
- Configuration changes must be auditable with administrator identity
- Connection test must not mutate production financial state for payment gateway beyond provider-permitted ping or token exchange

##### Validations

- Endpoint URL must be valid HTTPS URL format
- Timeout seconds must be positive integer within configured maximum
- Retry attempt limit must be non-negative integer within configured maximum
- KGID credentials must be provided on create and on rotation
- Payment gateway merchant identifier must be non-blank
- Payment gateway secret must be provided on create and on rotation
- Callback signing secret must meet minimum length requirement
- Active flag must be boolean
- Duplicate integration type profile name must be rejected if name uniqueness is enforced
- Administrator must hold integration configuration permission to save or rotate credentials

##### Calculations

- None

##### Workflow

Configuration states: DRAFT → ACTIVE → INACTIVE. Transitions: DRAFT to ACTIVE when administrator activates saved valid profile; ACTIVE to INACTIVE when administrator deactivates profile; INACTIVE to ACTIVE on reactivation after validation; credential rotation while ACTIVE creates new credential version then retires prior version on successful save.

##### Search requirements

- Filter integration configuration register by integration type (KGID, payment gateway)
- Filter by active or inactive status
- Sort by last updated timestamp

##### Documents

- Administrator guide for integration setup and activation
- Credential rotation and security procedures for examination administrators

##### Reports

- Configuration change audit listing exportable for compliance review

##### Notifications

- Optional in-application success or failure toast on save and connection test; no candidate notifications

##### Security

- Role-based access limited to Examination Administrator with integration configuration permission
- Credentials encrypted at rest with environment-specific encryption keys
- Connection test responses scrubbed of sensitive tokens before display
- Audit log captures administrator user identifier for every mutation

##### Integrations

- External KGID API for administrator-initiated connectivity test
- External payment gateway for administrator-initiated connectivity test

##### Dependencies

- F01 Platform Role and Permission Catalog defining Examination Administrator integration configuration permissions
- F01 Examination Administrator Account Lifecycle for administrator identities
- F01 Staff Authentication Session and Credential Policy
- F01 Downstream Module Authorization Integration Hooks for permission enforcement on configuration APIs
- F02-001 KGID Government Employee Lookup Integration consumes KGID profiles
- F02-002 Payment Gateway Fee Transaction Integration consumes payment gateway profiles

##### Assumptions

- Examination Administrator role from Module 01 includes distinct permission for integration configuration separate from registration operations
- Encryption key management is provided by platform infrastructure
- Payment gateway provider exposes a non-financial connectivity or token test operation suitable for administrator test action

##### Risks

- Misconfigured endpoints or expired credentials cause registration KGID lookup or payment outages
- Credential rotation errors may invalidate in-flight payment sessions if coordinated downtime is not observed

##### Non-functional requirements

- Configuration changes effective for new integration calls without application restart
- Save and test operations complete within administrator-acceptable interactive latency
- Audit records immutable after creation

##### Notes

Administrator-facing configuration for KGID and payment gateway connectivity; excludes registration business parameters.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Integration configuration register list with type and status filters | Medium | 16 |
| UI | Empty state when no integration profiles exist | Simple | 5 |
| UI | KGID integration endpoint configuration form | Medium | 16 |
| UI | Payment gateway integration endpoint configuration form | Medium | 16 |
| UI | Credential entry form with masked secret fields | Medium | 16 |
| UI | Credential rotation confirmation dialog | Simple | 5 |
| UI | KGID connection test result dialog | Easy | 14 |
| UI | Payment gateway connection test result dialog | Easy | 14 |
| UI | Configuration save validation error state on forms | Easy | 14 |
| API | List integration configuration profiles | Easy | 4 |
| API | Retrieve KGID integration configuration detail | Easy | 4 |
| API | Retrieve payment gateway integration configuration detail | Easy | 4 |
| API | Create KGID integration configuration profile | Medium | 6 |
| API | Update KGID integration configuration profile | Medium | 6 |
| API | Create payment gateway integration configuration profile | Medium | 6 |
| API | Update payment gateway integration configuration profile | Medium | 6 |
| API | Store and rotate encrypted integration credentials | Complex | 8 |
| API | Execute connectivity test against KGID endpoint | Medium | 6 |
| API | Execute connectivity test against payment gateway endpoint | Medium | 6 |
| Database | Integration configuration profile entity | Easy | 0.25 |
| Database | Encrypted credential blob storage per integration profile | Complex | 0.5 |
| Database | Integration configuration change audit trail | Medium | 0.3 |
| Testing | Examination Administrator authorized access to configuration save operations | Medium | 0.3 |
| Testing | Unauthorized role blocked from credential rotation | Medium | 0.3 |
| Testing | Invalid HTTPS URL and out-of-range timeout validation rejection | Easy | 0.25 |
| Testing | Credential encryption at rest and masked API responses | Complex | 0.5 |
| Documentation | Administrator guide for KGID and payment gateway setup | Medium | 0.3 |
| Documentation | Credential rotation and security procedures for administrators | Medium | 0.3 |

### F02-004 Integration Retry Logging and Error Observability

90 hours · Go-live · 19 tasks

##### Description

Delivers shared integration observability and resilience capabilities including structured call logging with correlation identifiers, transient versus permanent error classification, configurable retry execution for registration and payment integration calls, administrator log register with detail view and export, and sensitive field redaction suitable for production troubleshooting.

##### Business objective

Ensure KGID and payment integrations operate reliably under failure conditions with auditable evidence and administrator visibility into errors, retries, and outcomes without exposing secrets.

##### Actors

- Examination Administrator
- System Integration Service

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Integration type (KGID lookup or payment gateway operation)
- Correlation identifier from consuming flow
- Request metadata and redacted payload excerpts
- HTTP or gateway status codes and error messages
- Retry policy parameters from integration configuration profile
- Administrator filter criteria for log register

##### Outputs

- Integration call log entries with outcome status
- Retry attempt history records
- Error classification label per failed attempt
- Administrator log register rows
- Exported log file for filtered result set
- Structured permanent versus transient failure signals to calling integration features

##### Business rules

- Every external KGID and payment gateway call must produce a log record regardless of outcome
- Retry attempts must not exceed configured maximum for the active integration profile
- Permanent errors must never trigger automatic retry
- Secrets, API keys, and card-related data must be redacted before persistence
- Log export must respect same authorization scope as log register viewing
- Correlation identifier must be preserved across retry attempts for a single logical operation

##### Validations

- Correlation identifier must be non-blank when supplied by consumer
- Integration type must be one of supported values (KGID, payment gateway)
- Retry attempt number must increment monotonically per parent call
- Log list date-from must be before or equal to date-to
- Export row limit must not exceed configured maximum export size
- Administrator must hold integration observability permission to access log detail and export

##### Calculations

- Retry remaining attempts equals configured retry limit minus completed retry count

##### Workflow

Call lifecycle states: CALL_STARTED → (CALL_SUCCEEDED | RETRY_SCHEDULED | CALL_FAILED_PERMANENT | CALL_FAILED_EXHAUSTED). Transitions: CALL_STARTED to CALL_SUCCEEDED on successful external response; CALL_STARTED to RETRY_SCHEDULED on transient error when retries remain; RETRY_SCHEDULED to CALL_STARTED on next attempt execution; RETRY_SCHEDULED to CALL_FAILED_EXHAUSTED when retry limit reached; CALL_STARTED to CALL_FAILED_PERMANENT on permanent error classification without entering RETRY_SCHEDULED.

##### Search requirements

- Search integration call logs by correlation identifier partial match
- Filter by integration type KGID or payment gateway
- Filter by outcome status success, failed permanent, failed exhausted, or in progress
- Filter by date and time range
- Sort by call start time descending

##### Documents

- Integration troubleshooting guide for support staff
- Retry policy configuration technical notes for implementers

##### Reports

- Exported integration call log file for incident and audit analysis

##### Notifications

- None; administrators proactively review logs during incidents

##### Security

- Log access restricted to Examination Administrator with observability permission
- Automatic redaction of credential and PCI-related fields in stored payloads
- Export files exclude redacted secret placeholders replaced with non-reversible tokens only

##### Integrations

- Internal consumption by F02-001 KGID lookup calls
- Internal consumption by F02-002 payment gateway initiation, callback, and status query calls

##### Dependencies

- F01 Platform Role and Permission Catalog for observability permission
- F01 Staff Authentication Session and Credential Policy
- F02-003 Integration Endpoint and Credential Administration for retry limit and timeout parameters
- F02-001 KGID Government Employee Lookup Integration emits and consumes logging and retry behavior
- F02-002 Payment Gateway Fee Transaction Integration emits and consumes logging and retry behavior

##### Assumptions

- Registration and payment flows propagate correlation identifiers suitable for cross-module tracing
- Log retention period aligns with enterprise audit policy configured at platform level
- Export format is standard delimited or spreadsheet format acceptable to administrators

##### Risks

- High registration volume may produce large log volume requiring archival strategy outside this feature
- Incorrect transient classification may cause unnecessary load on failing external systems
- Insufficient redaction rules may expose secrets if gateway payloads change format

##### Non-functional requirements

- Logging must not materially block integration call completion path
- Log register queries must remain responsive for typical administrator filter combinations
- Retry scheduling must be safe under concurrent calls sharing similar failure windows

##### Notes

Shared cross-cutting capability supporting KGID lookup and payment gateway flows with administrator log review.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Integration call log register with date, type, and status filters | Medium | 16 |
| UI | Integration call log detail read-only view with redacted payloads | Medium | 16 |
| UI | Integration log register empty state for no matching records | Simple | 5 |
| UI | Export integration call logs download action | Easy | 14 |
| API | List integration call logs with search and filter parameters | Medium | 6 |
| API | Retrieve integration call log detail by correlation identifier | Easy | 4 |
| API | Export filtered integration call logs to downloadable file | Medium | 6 |
| API | Record integration call attempt with timing and outcome | Medium | 6 |
| API | Execute retry policy for classified transient integration errors | Complex | 8 |
| API | Classify integration errors as transient versus permanent | Medium | 6 |
| Database | Integration call log entity with correlation identifier | Medium | 0.3 |
| Database | Per-attempt retry history linked to parent integration call | Easy | 0.25 |
| Testing | Successful call logging with correlation identifier propagation across retries | Medium | 0.3 |
| Testing | Retry stops after configured maximum attempts with exhausted outcome | Complex | 0.5 |
| Testing | Permanent error classification skips retry scheduling | Medium | 0.3 |
| Testing | Sensitive credential redaction in stored log payloads | Complex | 0.5 |
| Testing | Unauthorized user blocked from log register and export | Medium | 0.3 |
| Documentation | Integration troubleshooting guide for support staff | Medium | 0.3 |
| Documentation | Retry policy configuration technical notes for implementers | Easy | 0.25 |
