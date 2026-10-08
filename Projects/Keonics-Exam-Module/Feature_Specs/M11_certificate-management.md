# Module 11: Certificate Management

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 6 (F11-001 … F11-006)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 11 Certificate Management

634.6 hours · 128 tasks · Business

Digital certificate issuance for eligible candidates, QR-enabled authenticity, and public online verification.

### F11-001 Eligibility-Triggered Certificate Issuance and Numbering

106.65 hours · Go-live · 25 tasks

##### Description

Automatically creates certificate lifecycle records when a candidate's published examination result satisfies Module 04 certificate eligibility and pass criteria. Assigns a unique certificate number and secure verification token, captures an approved public disclosure field snapshot, and exposes administrator monitoring with per-candidate retry for failed issuance rows.

##### Business objective

Ensure only eligible passed candidates receive department-issued digital certificates with unique numbering and verifiable tokens immediately after governed result publication, without manual re-entry of result data.

##### Actors

- Examination Administrator
- System (batch issuance job)

##### User journey

1. Examination Administrator completes governed result publication in Evaluation & Results (Module 10).
2. Certificate issuance batch job receives the set of candidates with published pass outcomes for the examination.
3. For each candidate, the system reads certificate eligibility rules configured in Question Bank & Examination Configuration (Module 04).
4. System evaluates pass status, eligibility flag, and absence of an existing active certificate for the same examination attempt.
5. Eligible candidates enter ISSUANCE_QUEUED; ineligible or duplicate-attempt candidates are recorded as ISSUANCE_SKIPPED with reason.
6. System allocates the next certificate number from the examination-specific numbering sequence.
7. System generates a secure verification token bound to the certificate record.
8. System persists the certificate lifecycle record with status ISSUED, issue date, links to candidate, examination, result, certificate number, token reference, and disclosure field snapshot.
9. System emits a certificate-available notification event to Notification Service (Module 07) when issuance succeeds.
10. Examination Administrator opens the issuance monitoring register filtered by examination and batch run.
11. Administrator reviews failed rows (e.g., missing mandatory disclosure source field, sequence exhaustion).
12. Administrator corrects upstream data if needed and triggers individual retry for a failed row.
13. Retry re-evaluates eligibility and either transitions the row to ISSUED or remains ISSUANCE_FAILED with updated reason.

##### Functional capabilities

- Evaluate certificate eligibility against published pass result and Module 04 eligibility configuration
- Skip issuance when an active certificate already exists for the same examination attempt
- Allocate unique certificate numbers from a per-examination sequence
- Generate secure verification tokens bound to certificate records
- Persist certificate lifecycle records with issue date and ISSUED status
- Capture approved public disclosure field snapshot at time of issuance
- Batch-process all eligible candidates immediately after result publication
- Record per-candidate issuance outcome with skip or failure reason
- Display issuance monitoring register with batch and row-level status
- Retry failed single-candidate issuance after prerequisite correction
- Emit certificate-available notification event on successful issuance

##### Inputs

- Published examination result identifier and pass/fail outcome
- Certificate eligibility configuration from Module 04
- Candidate profile fields required for certificate record and disclosure snapshot
- Examination master identifier and display name
- Examination-specific certificate numbering sequence configuration
- Batch run identifier and result publication timestamp

##### Outputs

- Certificate lifecycle record with unique certificate number
- Secure verification token reference linked to certificate
- Public disclosure field snapshot stored on certificate record
- Per-candidate issuance outcome log entry (ISSUED, ISSUANCE_SKIPPED, ISSUANCE_FAILED)
- Certificate-available notification event payload to Module 07

##### Business rules

- Issuance occurs only after results are in published state per Module 10 governance
- Candidate must meet both pass criteria and certificate eligibility flag from Module 04
- At most one active (non-revoked) certificate per candidate per examination attempt
- Certificate numbers must be unique within the examination numbering scope
- Verification tokens must not be reversible to internal primary keys in public contexts
- Failed issuance rows do not delete partial records; they remain auditable until resolved or marked permanent failure
- Disclosure snapshot is immutable after issuance; later configuration changes apply only to new certificates

##### Validations

- Published result must exist and show PASS before issuance proceeds
- Certificate eligibility flag from Module 04 must be true for the examination
- Candidate identifier must resolve to an active registration profile
- Duplicate active certificate check must pass for candidate plus examination attempt
- Mandatory disclosure source fields (e.g., candidate legal name, examination title, issue date) must be non-empty
- Certificate number sequence must not exceed configured maximum if a cap exists
- Retry allowed only from ISSUANCE_FAILED state, not from ISSUED or REVOKED

##### Calculations

- Next certificate number = previous sequence value + 1 formatted per examination numbering pattern
- Eligible candidate count = published pass candidates minus ineligible, duplicate, and failed rows

##### Workflow

RESULT_PUBLISHED → ELIGIBILITY_EVALUATED → ISSUANCE_QUEUED → NUMBER_ASSIGNED → TOKEN_GENERATED → ISSUED; alternate paths: ELIGIBILITY_EVALUATED → ISSUANCE_SKIPPED; ISSUANCE_QUEUED → ISSUANCE_FAILED → RETRY_PENDING → ISSUED | PERMANENT_FAILURE

##### Search requirements

- Issuance monitoring register searchable by examination name, batch run date, and row status
- Filter failed and skipped rows by failure reason code

##### Reports

- Issuance batch summary counts (issued, skipped, failed) exposed as register aggregates for Module 12 reporting hooks

##### Notifications

- Certificate-available event dispatched to Module 07 upon successful ISSUED transition

##### Security

- Only Examination Administrator role may view issuance monitoring and trigger retry
- Verification tokens stored using one-way hashing or secure vault reference; plain token never logged
- Batch job execution authenticated as system service account with least-privilege scope

##### Integrations

- Consume published result and pass outcome from Module 10 Evaluation & Results
- Read certificate eligibility configuration from Module 04 Question Bank & Examination Configuration
- Emit certificate-available notification event to Module 07 Notification Service

##### Dependencies

- F10-00x Governed Result Publication and Display (Module 10)
- F04-00x Certificate Eligibility Configuration (Module 04)
- F05-00x Candidate Registration profile fields (Module 05)
- F01-00x Examination Administrator authorization (Module 01)
- F07-00x Notification event subscription and dispatch (Module 07)

##### Assumptions

- Certificate numbering sequence and format are configured in Module 04 or examination master before first issuance
- Mandatory fields for disclosure snapshot are present on candidate profile or result record at publication time
- Batch job infrastructure handles examination-wide candidate volumes without manual intervention for happy path
- Notification template for certificate availability is configured in Module 07 prior to go-live

##### Risks

- Large candidate volumes may require batch throttling not explicitly sized in SOW
- Missing candidate photograph or optional fields may block PDF generation downstream if treated as mandatory
- Sequence exhaustion under high attempt volume requires administrator intervention

##### Non-functional requirements

- Issuance batch for a single examination should complete within operational SLA agreed at integration testing
- Issuance operations must be idempotent to prevent duplicate certificates on batch retry
- All issuance state transitions must be audit-logged with actor, timestamp, and reason

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Issuance monitoring register with batch status chips and failure reason column | Medium | 16 |
| UI | Issuance row failure detail read-only panel with candidate and examination context | Simple | 5 |
| UI | Individual issuance retry confirmation dialog | Simple | 5 |
| UI | Issuance monitoring empty state when no batches exist for selected examination | Simple | 5 |
| API | Evaluate certificate eligibility for candidate-examination pair against published result | Complex | 8 |
| API | Batch queue certificate issuance for all eligible candidates after result publication | Complex | 8 |
| API | Allocate next unique certificate number with sequence boundary handling | Medium | 6 |
| API | Generate secure verification token bound to certificate record | Medium | 6 |
| API | Create certificate lifecycle record with issue metadata and disclosure snapshot | Complex | 8 |
| API | List issuance batch outcomes with examination and status filters | Medium | 6 |
| API | Retry failed single-candidate issuance after prerequisite correction | Medium | 6 |
| Database | Core certificate entity with candidate examination and result linkage | Medium | 0.3 |
| Database | Certificate number uniqueness constraints and sequence allocation indexes | Complex | 0.5 |
| Database | Verification token secure reference storage | Medium | 0.3 |
| Database | Issuance batch run and per-candidate outcome audit persistence | Medium | 0.3 |
| Integration | Consume published pass result signal from Evaluation module | Medium | 16 |
| Integration | Read certificate eligibility configuration from Examination Configuration module | Simple | 4 |
| Integration | Emit certificate-available notification event to Notification Service | Simple | 4 |
| Testing | Happy path batch issuance for multiple eligible passed candidates | Medium | 0.3 |
| Testing | Duplicate active certificate rejection for same examination attempt | Medium | 0.3 |
| Testing | Certificate number sequence boundary and collision edge cases | Complex | 0.5 |
| Testing | Issuance failure when mandatory disclosure source fields are missing | Medium | 0.3 |
| Testing | Unauthorized role blocked from issuance monitoring and retry operations | Easy | 0.25 |
| Documentation | Administrator runbook for issuance monitoring and failure recovery | Medium | 0.3 |
| Documentation | Technical notes for numbering scheme token security and batch idempotency | Medium | 0.3 |

### F11-002 Digital Certificate PDF Generation with QR Embedding

83.65 hours · Go-live · 21 tasks

##### Description

Renders department-approved digital certificate PDF documents for issued certificate records, dynamically populating candidate and examination fields, embedding a QR code linked to the verification token URL, versioning generated documents, and supporting administrator-triggered regeneration when template or source data changes.

##### Business objective

Provide candidates and verifiers with a tamper-evident printable certificate document that embeds machine-readable QR verification aligned to the department's certificate template standards.

##### Actors

- Examination Administrator
- System (document generation job)
- Candidate

##### User journey

1. Certificate lifecycle record reaches ISSUED state (Feature F11-001).
2. System queues PDF generation job for the certificate record.
3. System resolves candidate name, examination title, issue date, certificate number, and photograph from upstream modules.
4. System renders PDF using the active certificate template version.
5. System generates QR code image encoding the public verification URL with verification token.
6. System embeds QR code at the configured position on the certificate PDF.
7. System persists the PDF binary reference, template version, checksum, and generation timestamp.
8. Certificate generation status transitions to DOCUMENT_READY on success or DOCUMENT_FAILED on error.
9. Examination Administrator opens certificate detail and views generation status indicator.
10. Administrator optionally opens template preview read-only page to validate field placement against sample data.
11. If source data or template was corrected, administrator initiates regeneration via confirmation dialog.
12. Regeneration creates a new document version while retaining prior version in history.
13. Candidate sees certificate as downloadable once DOCUMENT_READY (handled in Feature F11-003).

##### Functional capabilities

- Queue PDF generation automatically upon ISSUED transition
- Render certificate PDF from approved template with dynamic field binding
- Resolve candidate photograph from registration profile for template placement
- Generate QR code image from verification token URL
- Embed QR code into certificate PDF at configured coordinates
- Persist generated PDF with version checksum and template version reference
- Expose certificate document generation status on administrator detail view
- Regenerate certificate PDF on administrator request with version increment
- Retain superseded PDF versions in document history
- Surface generation failure reason to administrator detail view

##### Inputs

- Certificate record with certificate number issue date verification token reference
- Active certificate template version and field mapping configuration
- Candidate legal name and photograph from Module 05 profile
- Examination display name and completion or result date from Module 10
- QR placement coordinates and public verification base URL configuration

##### Outputs

- Generated certificate PDF binary stored with file reference
- QR code embedded within PDF document
- Document version record with template version checksum and timestamp
- Generation status DOCUMENT_READY or DOCUMENT_FAILED on certificate record

##### Business rules

- PDF generation executes only for certificates in ISSUED status
- Each regeneration increments document version; prior versions remain auditable
- QR code must encode the same verification token issued at certificate creation
- Template version active at generation time is recorded immutably on the document record
- Revoked certificates do not auto-regenerate; regeneration blocked while status is REVOKED

##### Validations

- Certificate record must exist and be in ISSUED status before generation starts
- Mandatory template fields (candidate name, examination name, certificate number, issue date) must resolve to non-empty values
- Photograph file reference must be valid format or fall back to configured placeholder image
- Template version identifier must reference an active approved template
- Regeneration request must be authorized to Examination Administrator role
- Public verification base URL must be configured before QR embedding proceeds

##### Calculations

- Document checksum computed over generated PDF bytes for integrity verification

##### Workflow

ISSUED → DOCUMENT_QUEUED → DOCUMENT_GENERATING → DOCUMENT_READY; alternate: DOCUMENT_GENERATING → DOCUMENT_FAILED → DOCUMENT_QUEUED (retry) → DOCUMENT_READY

##### Documents

- Digital certificate PDF with embedded QR code
- Certificate template version referenced at generation time

##### Security

- PDF storage access restricted to authorized administrators and owning candidate
- Verification token must not appear in plain text within PDF body outside QR encoding
- Regeneration actions audit-logged with administrator identity and reason

##### Integrations

- Resolve candidate photograph and profile fields from Candidate Registration module
- Resolve examination and result metadata from Evaluation & Results module
- QR code image generation library or internal service

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F05-00x Candidate profile and photograph storage (Module 05)
- F10-00x Published result metadata (Module 10)
- F04-00x Certificate template configuration (Module 04)

##### Assumptions

- Approved certificate template artwork and field map are supplied by client before UAT
- Public verification base URL is stable across environments with environment-specific configuration
- Photograph absence is handled via placeholder rather than blocking all issuances unless client mandates otherwise

##### Risks

- Template changes after bulk issuance may require mass regeneration outside initial scope
- Large photograph files may impact PDF render performance
- QR print quality at small sizes may affect scan success on low-resolution prints

##### Non-functional requirements

- Single certificate PDF generation should complete within interactive SLA for administrator-triggered regeneration
- Generated PDFs must meet print-ready resolution for QR scanning
- Document storage must support retention policy aligned with certificate lifecycle records

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate template preview read-only page for administrators | Medium | 16 |
| UI | Certificate generation status indicator on administrator certificate detail view | Simple | 5 |
| UI | Regenerate certificate PDF confirmation dialog for administrators | Simple | 5 |
| UI | Certificate generation failure alert banner on administrator detail view | Simple | 5 |
| API | Render certificate PDF from template with dynamic candidate and examination fields | Complex | 8 |
| API | Embed QR code encoding verification URL into certificate PDF output | Medium | 6 |
| API | Persist generated certificate PDF with version checksum and template reference | Medium | 6 |
| API | Regenerate certificate PDF for single record with version increment | Medium | 6 |
| API | Fetch certificate document generation status for administrator detail view | Easy | 4 |
| Database | Certificate document file reference and storage metadata entity | Easy | 0.25 |
| Database | Certificate document version history per certificate record | Medium | 0.3 |
| Database | Template version identifier stored on each generated document row | Simple | 0.1 |
| Integration | Resolve candidate photograph from registration profile for PDF rendering | Medium | 16 |
| Integration | QR code image generation library integration | Simple | 4 |
| Testing | Happy path PDF contains mandatory fields and scannable QR code | Medium | 0.3 |
| Testing | Template version upgrade produces distinguishable document version history | Medium | 0.3 |
| Testing | Missing candidate photograph renders configured placeholder image | Easy | 0.25 |
| Testing | PDF generation failure surfaces actionable error on administrator detail view | Medium | 0.3 |
| Testing | Unauthorized regeneration attempt rejected for non-administrator roles | Medium | 0.3 |
| Documentation | Administrator runbook for certificate regeneration after template or data correction | Easy | 0.25 |
| Documentation | Technical notes for PDF template field binding and QR placement configuration | Medium | 0.3 |

### F11-003 Candidate Portal Certificate List and Download

107.9 hours · Go-live · 19 tasks

##### Description

Enables authenticated candidates to view a portal list of their issued digital certificates per examination, inspect certificate metadata, and download the generated PDF when document status is ready and certificate status remains active.

##### Business objective

Allow eligible candidates to self-service download digitally generated examination certificates from their OTP-authenticated portal login without administrator intervention.

##### Actors

- Candidate

##### User journey

1. Candidate logs into the examination portal using OTP authentication (Module 01 / SOW Section 4.1).
2. Candidate navigates to the Certificates section from portal navigation.
3. System loads certificate list scoped strictly to the authenticated candidate identifier.
4. Candidate sees each row with examination name, certificate number, issue date, and status badge (ISSUED, DOCUMENT_PENDING, REVOKED).
5. If no certificates exist yet, candidate sees empty state messaging explaining certificates appear after results and issuance processing.
6. If list retrieval fails, candidate sees error state with retry action.
7. Candidate selects a certificate row to open read-only detail panel showing examination name, issue date, certificate number, and download eligibility indicator.
8. When status is ISSUED and document is DOCUMENT_READY, candidate clicks download.
9. System streams PDF to candidate browser and logs download event.
10. If certificate is REVOKED, download control is disabled with explanation tooltip.
11. If document is still generating, detail panel shows pending message without download action.

##### Functional capabilities

- List all certificate records belonging to authenticated candidate
- Display examination name issue date certificate number and status on list rows
- Show empty state when candidate has no issued certificates
- Show error state with retry when list retrieval fails
- Display read-only certificate detail panel with metadata before download
- Stream certificate PDF download for ISSUED certificates with ready documents
- Block download for REVOKED or cancelled certificates
- Block download while document generation is pending or failed
- Log each candidate download event with timestamp
- Enforce candidate-scoped access preventing cross-candidate record access

##### Inputs

- Authenticated candidate session token from OTP login
- Certificate list query parameters (optional examination filter)
- Certificate identifier selected for detail or download

##### Outputs

- Candidate-scoped certificate list with status badges
- Certificate metadata detail payload
- Downloaded certificate PDF file stream
- Candidate download audit log entry

##### Business rules

- Candidates may view and download only their own certificate records
- Download permitted only when certificate status is ISSUED and document status is DOCUMENT_READY
- Revoked certificates remain visible in list with REVOKED badge but download is disabled
- Certificates for examinations where results are not yet published must not appear in list
- Each download event is recorded for audit; repeated downloads are allowed

##### Validations

- Session must belong to valid authenticated candidate
- Requested certificate identifier must belong to session candidate identifier
- Download request rejected when certificate status is REVOKED or CANCELLED
- Download request rejected when document status is not DOCUMENT_READY
- Certificate identifier must be well-formed and exist or return not-found without leaking other candidates' data

##### Workflow

PORTAL_LOGIN → CERTIFICATE_LIST_LOADED → DETAIL_VIEWED → DOWNLOAD_REQUESTED → DOWNLOAD_STREAMED; alternate: DETAIL_VIEWED → DOWNLOAD_BLOCKED (revoked or pending document)

##### Search requirements

- Optional filter certificate list by examination name on client-side or lightweight server filter

##### Documents

- Downloaded digital certificate PDF from candidate portal

##### Security

- All list detail and download operations scoped to authenticated candidate identity
- Direct object reference attempts by tampered certificate identifier return generic not-found
- Download responses include cache-control headers discouraging unintended public caching

##### Integrations

- Validate candidate OTP portal session from User authentication module

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F01-00x Candidate OTP authentication session (Module 01)
- SOW Section 4.1 OTP-Based Candidate Login

##### Assumptions

- Portal navigation includes a Certificates entry point agreed in overall portal UX
- Candidates access portal primarily via web browser; responsive layout covers mobile browsers
- Certificate PDF file size is suitable for direct browser download on typical mobile networks

##### Risks

- Candidates may attempt to share portal credentials to download on behalf of others
- Pending document state may generate support queries if issuance-to-PDF delay is long

##### Non-functional requirements

- Certificate list should load within portal performance targets under concurrent login peaks
- Download streaming must support standard mobile and desktop browsers
- Portal certificate views must be readable on mobile screen widths

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal certificate list with examination name issue date and status badges | Easy | 14 |
| UI | Candidate certificate list empty state with pending issuance messaging | Simple | 5 |
| UI | Candidate certificate list error state with retry action | Simple | 5 |
| UI | Candidate certificate detail read-only panel with download eligibility indicator | Medium | 16 |
| UI | Candidate certificate PDF download button with in-progress indicator | Easy | 14 |
| UI | Revoked certificate row with download disabled and explanation tooltip | Easy | 14 |
| UI | Mobile-responsive layout for candidate certificate list and detail views | Medium | 16 |
| API | List certificates scoped to authenticated candidate identity | Easy | 4 |
| API | Get single certificate metadata for authenticated candidate | Easy | 4 |
| API | Stream certificate PDF download with issued-status and document-ready enforcement | Medium | 6 |
| API | Log candidate certificate download event with timestamp | Easy | 4 |
| Database | Candidate certificate download audit log persistence | Easy | 0.25 |
| Integration | Validate candidate portal session from authentication module | Simple | 4 |
| Testing | Happy path list and download for issued certificate with ready document | Easy | 0.25 |
| Testing | Revoked certificate download blocked with user-facing explanation message | Medium | 0.3 |
| Testing | Cross-candidate certificate identifier tampering returns not-found without data leak | Complex | 0.5 |
| Testing | Empty list when results published but certificate issuance not yet complete | Easy | 0.25 |
| Documentation | Candidate user guide for locating and downloading examination certificates | Easy | 0.25 |
| Documentation | Technical notes for candidate-scoped certificate authorization checks | Simple | 0.1 |

### F11-004 Public Online Certificate Verification Portal

127.7 hours · Go-live · 23 tasks

##### Description

Provides a public-facing verification experience for verifiers and third parties to confirm certificate authenticity by scanning the QR code or entering a certificate number, returning valid, not-found, or revoked/cancelled outcomes while displaying only administrator-approved public disclosure fields.

##### Business objective

Enable third parties to independently confirm that a certificate was issued by the department and determine whether it is currently valid, without exposing non-approved personal information.

##### Actors

- Verifier/Public User

##### User journey

1. Verifier scans QR code on printed certificate using mobile device camera or QR app.
2. QR encodes public verification URL with verification token parameter; browser opens verification landing page.
3. Landing page automatically submits token verification request without requiring login.
4. Alternatively, verifier navigates directly to public verification site and enters certificate number manually.
5. Verifier submits certificate number entry form.
6. System validates token or number format before lookup.
7. For valid active certificate, system displays approved disclosure fields only (e.g., candidate name, examination name, issue date, certificate number, pass status label).
8. For unknown token or certificate number, system displays uniform not-found outcome without revealing whether number format was partially matched.
9. For revoked or cancelled certificate, system displays revoked outcome with status explanation and issue date if approved for disclosure, suppressing other sensitive fields.
10. If rate limit threshold exceeded, verifier sees cooldown or challenge message before further attempts.
11. Verification request is audit-logged with outcome category without storing unnecessary PII.

##### Functional capabilities

- Verify certificate authenticity by QR verification token deep link
- Verify certificate authenticity by manual certificate number entry
- Display valid verification outcome with approved public disclosure fields only
- Display not-found outcome for unknown token or certificate number
- Display revoked or cancelled outcome with status explanation
- Validate token and certificate number format before lookup
- Apply rate limiting on public verification requests
- Audit-log verification requests with outcome category
- Auto-submit verification on QR deep link landing page
- Render mobile-responsive verification results for field scanning use case

##### Inputs

- Verification token from QR-encoded URL parameter
- Certificate number entered on public form
- Client IP address and request timestamp for rate limiting
- Approved public disclosure field snapshot stored on certificate record

##### Outputs

- Valid verification result panel with approved disclosure field values
- Not-found verification result panel
- Revoked or cancelled verification result panel
- Verification audit log entry with outcome category VALID NOT_FOUND or REVOKED

##### Business rules

- Public verification requires no authentication
- Only fields approved for public disclosure and captured in issuance snapshot may be displayed on valid outcome
- Revoked certificates must never present as valid regardless of token possession
- Not-found responses must be uniform for invalid token and unknown certificate number to reduce enumeration
- Verification displays department branding confirming issuer identity
- Disclosure snapshot on certificate record governs displayed fields; live profile changes do not alter verification output

##### Validations

- Verification token must match expected length and character set before database lookup
- Certificate number entry must match configured format pattern
- Empty token and empty certificate number submissions rejected with inline field message
- Rate limit counter enforced per client IP or token bucket configuration
- Revoked status checked after record match before returning valid outcome

##### Workflow

VERIFY_REQUESTED → TOKEN_OR_NUMBER_VALIDATED → LOOKUP_EXECUTED → OUTCOME_VALID | OUTCOME_NOT_FOUND | OUTCOME_REVOKED

##### Search requirements

- Exact match lookup by verification token
- Exact match lookup by certificate number within examination scope or global scope per configuration

##### Reports

- Verification volume and outcome counts exposed as reporting hook aggregates for Module 12

##### Security

- Public endpoints require no session but enforce rate limiting and abuse monitoring
- Responses must not expose internal identifiers candidate primary keys or audit internals
- Timing-safe comparison used for token validation to reduce side-channel leakage
- Verification audit logs store outcome category without full disclosure field payload

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering (verification token and disclosure snapshot)
- F04-00x Approved public disclosure field configuration (Module 04)
- F11-005 Certificate Cancellation and Revocation (revoked status propagation)
- SOW Sections 35 QR Code on Certificate and 36 Online Certificate Verification

##### Assumptions

- Public verification base URL is published on department website and embedded in QR codes
- Approved disclosure field set is finalized before UAT and snapshotted at issuance
- Rate limit thresholds are agreed with client security team prior to production

##### Risks

- Certificate number enumeration attempts despite uniform not-found responses
- Over-disclosure if disclosure configuration includes fields later deemed sensitive
- High QR scan traffic during result season may require CDN caching constraints review

##### Non-functional requirements

- Verification response must render within sub-second target for typical lookup under load
- Public verification page must be mobile-first for QR scan workflows
- Service must remain available during peak post-result verification spikes

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Public verification landing page with certificate number entry form | Easy | 14 |
| UI | QR deep link landing page auto-submitting token verification on load | Medium | 16 |
| UI | Valid verification result panel showing approved disclosure fields only | Medium | 16 |
| UI | Not-found verification result panel for unknown token or certificate number | Simple | 5 |
| UI | Revoked or cancelled verification result panel with status explanation | Simple | 5 |
| UI | Inline validation message for malformed token or certificate number entry | Simple | 5 |
| UI | Public verification rate-limit cooldown message screen | Medium | 16 |
| UI | Mobile-responsive layout for public verification pages | Easy | 14 |
| API | Verify certificate by QR verification token parameter | Medium | 6 |
| API | Verify certificate by public certificate number lookup | Medium | 6 |
| API | Return approved disclosure field snapshot for valid active certificate outcome | Medium | 6 |
| API | Return revoked outcome suppressing non-approved sensitive fields | Medium | 6 |
| API | Return uniform not-found outcome for unknown token and unknown number | Easy | 4 |
| API | Enforce rate limiting on public verification requests per client IP | Medium | 6 |
| Database | Public verification request audit log with outcome category | Easy | 0.25 |
| Database | Read-optimized indexes supporting token and certificate number verification lookup | Easy | 0.25 |
| Testing | Happy path valid QR token displays only approved disclosure fields | Medium | 0.3 |
| Testing | Revoked certificate verification shows revoked outcome without PII leakage | Medium | 0.3 |
| Testing | Unknown token and unknown certificate number both return identical not-found outcome | Easy | 0.25 |
| Testing | Tampered verification token rejected without record disclosure | Complex | 0.5 |
| Testing | Rate limit blocks excessive verification attempts from single client IP | Medium | 0.3 |
| Documentation | Public verifier instruction content for QR scan and manual number entry | Easy | 0.25 |
| Documentation | Technical notes on disclosure minimization and enumeration-safe public responses | Medium | 0.3 |

### F11-005 Certificate Cancellation and Revocation Management

104.4 hours · Go-live · 21 tasks

##### Description

Allows Examination Administrators to cancel or revoke previously issued certificates with mandatory reason capture, immutable status transition history, immediate propagation to public verification and candidate download blocking, while preserving full certificate lifecycle records for audit.

##### Business objective

Provide governed certificate invalidation when issuance errors, disqualifications, or administrative decisions require a previously issued certificate to be treated as no longer valid, without deleting historical records.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator opens certificate register and locates active ISSUED certificate (Feature F11-006) or receives directive to revoke specific record.
2. Administrator opens certificate administrator detail view with lifecycle timeline.
3. Administrator selects Revoke or Cancel action available only for ISSUED certificates.
4. System opens revocation reason dialog requiring reason code selection and mandatory notes text.
5. Administrator enters reason and confirms impact summary in confirmation dialog.
6. System transitions certificate status from ISSUED to REVOKED (or CANCELLED if configured as distinct outcome).
7. System appends immutable revocation event to certificate status history with actor timestamp reason code and notes.
8. Public verification immediately returns revoked outcome for associated token and certificate number.
9. Candidate portal download control becomes disabled for revoked certificate.
10. Administrator sees revoked badge on register row and may filter register to revoked status.
11. Attempt to revoke already-revoked certificate is rejected with inline message.

##### Functional capabilities

- Revoke or cancel active ISSUED certificate with mandatory reason capture
- Capture revocation reason code and free-text notes
- Transition certificate status ISSUED to REVOKED or CANCELLED
- Append immutable revocation event to certificate status history
- Propagate revoked status to public verification responses immediately
- Block candidate PDF download for revoked certificates
- Display revoked status badge on administrator register rows
- Filter administrator register by revoked or cancelled status
- Reject duplicate revocation on already-revoked certificate
- Preserve full certificate and document history without hard delete

##### Inputs

- Certificate identifier selected for revocation
- Revocation reason code from configured reference list
- Mandatory revocation notes text entered by administrator
- Administrator session identity and timestamp

##### Outputs

- Updated certificate status REVOKED or CANCELLED
- Revocation history event with reason actor and timestamp
- Revoked outcome on subsequent public verification requests
- Disabled download state on candidate portal certificate row

##### Business rules

- Only ISSUED certificates may be revoked; DOCUMENT_PENDING certificates follow separate cancellation path if needed
- Revocation does not delete certificate number token or document history records
- Revoked certificates cannot be reinstated to ISSUED within this module scope without separate client change request
- Revocation reason code must be selected from administrator-maintained reference list
- Public verification must reflect revoked status within same request cycle after commit
- Revocation action requires Examination Administrator authorization

##### Validations

- Certificate must exist and be in ISSUED status at time of revocation request
- Revocation reason code must be non-empty and valid reference value
- Revocation notes must meet minimum length threshold
- Administrator must hold permission for certificate revocation operation
- Duplicate revocation request on REVOKED certificate rejected with business error
- Revocation timestamp must not precede original issue date

##### Workflow

ISSUED → REVOKE_REQUESTED → REVOKE_CONFIRMED → REVOKED; alternate: REVOKED → REVOKE_REQUESTED → REVOKE_REJECTED (already revoked)

##### Search requirements

- Filter certificate register by REVOKED or CANCELLED status
- Search revoked certificates by revocation date range and reason code

##### Reports

- Revocation register export hook with reason code and date for Module 12 reporting

##### Notifications

- Optional revocation notification to candidate via Module 07 if client enables certificate-revoked template

##### Security

- Revocation restricted to authorized Examination Administrator roles
- Revocation history events are append-only and cannot be edited or deleted by administrators
- Revocation action audit includes source IP and session identifier

##### Integrations

- Emit optional certificate-revoked notification event to Notification Service

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-003 Candidate Portal Certificate List and Download
- F11-004 Public Online Certificate Verification Portal
- F01-00x Examination Administrator authorization (Module 01)
- SOW Section 37 Certificate Security

##### Assumptions

- Revocation reason code list is supplied by client before administrator training
- Certificate reinstatement after revocation is out of scope unless added by change request
- Cancelled and revoked may map to single REVOKED status with reason distinguishing administrative cancel vs fraud

##### Risks

- Delayed propagation to CDN-cached verification pages if caching introduced later
- Mass revocation after data correction event may require bulk tool outside current scope
- Candidates may retain previously downloaded PDF copies despite revocation

##### Non-functional requirements

- Revocation status must be immediately effective for verification and download enforcement
- Revocation history must satisfy audit retention requirements
- Revocation dialog must clearly communicate impact on verification and download

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Administrator certificate detail view with revoke action for ISSUED records | Medium | 16 |
| UI | Revocation reason capture dialog with mandatory reason code dropdown and notes field | Medium | 16 |
| UI | Revocation confirmation dialog summarizing verification and download impact | Simple | 5 |
| UI | Revoked status badge on administrator certificate register rows | Easy | 14 |
| UI | Certificate register status filter including revoked and cancelled values | Easy | 14 |
| UI | Inline rejection message when attempting to revoke already-revoked certificate | Simple | 5 |
| API | Revoke ISSUED certificate with reason code notes and actor audit | Complex | 8 |
| API | List revoked certificates with reason code and revocation timestamp for administrators | Medium | 6 |
| API | Propagate revoked status to public verification lookup responses | Medium | 6 |
| API | Enforce download block for revoked certificate on candidate portal stream endpoint | Easy | 4 |
| API | Reject duplicate revocation request for already-revoked certificate | Easy | 4 |
| Database | Certificate status transition history with reason actor and timestamp | Medium | 0.3 |
| Database | Revocation reason code reference values persistence | Simple | 0.1 |
| Integration | Emit optional certificate-revoked notification event to Notification Service | Simple | 4 |
| Testing | Happy path administrator revokes active ISSUED certificate with reason capture | Medium | 0.3 |
| Testing | Revoked certificate public verification returns revoked outcome immediately | Medium | 0.3 |
| Testing | Candidate download denied after revocation with explanatory message | Easy | 0.25 |
| Testing | Non-administrator role cannot execute revocation operation | Medium | 0.3 |
| Testing | Revocation history append-only behavior prevents modification of prior events | Medium | 0.3 |
| Documentation | Administrator runbook for certificate revocation policy and procedure | Medium | 0.3 |
| Documentation | Technical notes for revoked status propagation to verification and download endpoints | Easy | 0.25 |

### F11-006 Administrator Certificate Register Search and Export

104.3 hours · Go-live · 19 tasks

##### Description

Provides Examination Administrators with a searchable register of all certificate lifecycle records, advanced filtering, read-only detail with lifecycle timeline, and CSV export of filtered results to support operational oversight and Module 12 reporting hooks.

##### Business objective

Give examination administrators consolidated visibility into issued, pending, and revoked certificates across examinations for operational management audit response and downstream reporting.

##### Actors

- Examination Administrator

##### User journey

1. Examination Administrator navigates to Certificate Register from administration menu.
2. System loads paginated certificate register with default sort by issue date descending.
3. Administrator enters search text for certificate number or candidate name.
4. Administrator applies filters for examination, issue date range, status, and optionally allotted centre.
5. Register refreshes showing matching rows with certificate number candidate name examination issue date status and document status.
6. If no rows match, administrator sees empty state with guidance to adjust filters.
7. Administrator clicks row to open read-only certificate detail with lifecycle timeline showing issuance document generation and revocation events.
8. Administrator selects Export action to download CSV of currently filtered result set.
9. Export confirmation dialog warns row count and filter scope.
10. System generates CSV file with approved export columns and downloads to administrator browser.
11. Unauthorized roles attempting register access receive access denied outcome.

##### Functional capabilities

- Display paginated certificate register with sortable columns
- Search register by certificate number and candidate name
- Filter register by examination issue date range status and document status
- Show register empty state when no rows match criteria
- Open read-only administrator certificate detail with lifecycle timeline
- Export filtered certificate register to CSV file
- Confirm export scope and row count before download
- Enforce administrator role authorization for register access
- Expose register aggregates as reporting hooks for Module 12

##### Inputs

- Search text for certificate number or candidate name
- Filter values for examination identifier status issue date range document status
- Pagination page number and page size
- Sort column and direction
- Export request with current filter snapshot

##### Outputs

- Paginated certificate register row set
- Administrator certificate detail with lifecycle timeline events
- CSV export file of filtered certificate records
- Register aggregate counts by status for reporting hooks

##### Business rules

- Register includes ISSUED REVOKED DOCUMENT_PENDING and ISSUANCE_FAILED records within administrator visibility scope
- Export includes only columns approved for administrator operational use; verification tokens are never exported in plain form
- Export row set must match active filter criteria at time of export request
- Lifecycle timeline displays issuance document generation and revocation events in chronological order
- Register access limited to Examination Administrator and authorized oversight roles per Module 01

##### Validations

- Issue date range filter requires end date on or after start date
- Search text length must meet minimum threshold before server search executes
- Export request rejected when estimated row count exceeds configured export limit with administrator message
- Pagination parameters must be within allowed bounds
- Unauthorized session rejected before register data returned

##### Calculations

- Export row count equals count of records matching active filter at export time
- Register status aggregate counts computed per filter scope

##### Workflow

REGISTER_LOADED → SEARCH_OR_FILTER_APPLIED → ROW_SELECTED → DETAIL_VIEWED → EXPORT_REQUESTED → EXPORT_DOWNLOADED

##### Search requirements

- Partial match search on candidate name
- Exact or prefix match search on certificate number
- Combined filter by examination plus status plus issue date range
- Sort by issue date certificate number candidate name and status

##### Documents

- CSV export file of certificate register

##### Reports

- Certificate register status aggregate counts exposed for Module 12 Examination Administration and Reporting hooks

##### Security

- Register list detail and export require Examination Administrator authorization
- CSV export excludes verification token plain values and sensitive internal identifiers
- Export actions audit-logged with administrator identity filter snapshot and row count

##### Dependencies

- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F11-005 Certificate Cancellation and Revocation Management
- F01-00x Examination Administrator authorization (Module 01)
- F12-00x Examination Administration and Reporting hooks (Module 12)

##### Assumptions

- Administrator visibility is global across examinations unless client later requires centre-scoped restriction
- CSV export column set is agreed during requirements sign-off
- Export row limit threshold is configured to protect server performance

##### Risks

- Large export requests during peak season may require asynchronous export enhancement
- Centre-scoped visibility if added later increases authorization complexity
- PII in CSV exports requires client data handling policy compliance

##### Non-functional requirements

- Register search should return first page within interactive SLA under typical data volumes
- Export generation must complete or fail gracefully with clear message for oversized requests
- Register UI must support efficient navigation for thousands of certificate rows via pagination

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate register list with search box and paginated sortable columns | Medium | 16 |
| UI | Certificate register advanced filter panel for examination date range and status | Medium | 16 |
| UI | Certificate register empty state when no rows match active filters | Simple | 5 |
| UI | Administrator certificate detail read-only view with lifecycle timeline | Complex | 18 |
| UI | Certificate register CSV export action button on register toolbar | Easy | 14 |
| UI | Certificate register export confirmation dialog showing row count and filter scope | Simple | 5 |
| API | Search and list certificates with pagination and column sorting | Medium | 6 |
| API | Filter certificates by examination issue date range status and document status | Medium | 6 |
| API | Get administrator certificate detail with lifecycle timeline events | Medium | 6 |
| API | Export filtered certificate register to CSV with column whitelist | Medium | 6 |
| API | Return register status aggregate counts for reporting hook consumers | Easy | 4 |
| Database | Composite indexes supporting register search filter and sort columns | Complex | 0.5 |
| Testing | Happy path search by certificate number returns matching single row | Easy | 0.25 |
| Testing | Combined status and issue date range filter returns accurate row set | Medium | 0.3 |
| Testing | CSV export row set matches on-screen filtered register results | Medium | 0.3 |
| Testing | Export row count limit exceeded returns administrator-facing rejection message | Medium | 0.3 |
| Testing | Unauthorized role blocked from register list detail and export operations | Medium | 0.3 |
| Documentation | Administrator guide for certificate register search filters and export | Easy | 0.25 |
| Documentation | Technical notes for register reporting hook aggregates and export audit logging | Simple | 0.1 |
