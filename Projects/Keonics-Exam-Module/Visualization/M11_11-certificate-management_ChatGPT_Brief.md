# ChatGPT Visualization Brief — Module 11: Certificate Management

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 11 Certificate Management
**Features:** 6 (F11-001 … F11-006)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 11 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Eligibility-triggered issuance + numbering sequence
2. PDF + QR embed + public verify portal flow
3. Certificate lifecycle (ISSUED / CANCELLED / REVOKED)
4. Issuance log outcomes (ISSUED / SKIPPED / FAILED)
5. Certificate ERD
6. Feature relationship / dependency graph within this module and to other modules
7. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Certificate Management
**Purpose:** Eligibility-triggered certificate issuance and numbering, PDF with QR, candidate download, public verification, cancellation/revocation, admin register/export.

**Actors (union across features):**
- Candidate
- Examination Administrator
- System (batch issuance job)
- System (document generation job)
- Verifier/Public User

**Feature list:**
- **F11-001** — Eligibility-Triggered Certificate Issuance and Numbering
- **F11-002** — Digital Certificate PDF Generation with QR Embedding
- **F11-003** — Candidate Portal Certificate List and Download
- **F11-004** — Public Online Certificate Verification Portal
- **F11-005** — Certificate Cancellation and Revocation Management
- **F11-006** — Administrator Certificate Register Search and Export

### DATA MODEL (from EXAM DB design v2.1)

- `certificate_number_sequence`
- `certificate`
- `certificate_document`
- `certificate_verification_token`
- `certificate_verification_hit`
- `certificate_download_log`
- `certificate_issuance_log`
- `certificate_export_run`

### FEATURE CATALOGUE

#### F11-001 — Eligibility-Triggered Certificate Issuance and Numbering

**One-liner / description:** Automatically creates certificate lifecycle records when a candidate's published examination result satisfies Module 04 certificate eligibility and pass criteria. Assigns a unique certificate number and secure…

**Business objective:** Ensure only eligible passed candidates receive department-issued digital certificates with unique numbering and verifiable tokens immediately after governed result publication, without manual re-entry of result data.

**Actors:** Examination Administrator; System (batch issuance job)

**User journey (13 steps):**
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

**Functional capabilities:**
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

**Inputs:** Published examination result identifier and pass/fail outcome; Certificate eligibility configuration from Module 04; Candidate profile fields required for certificate record and disclosure snapshot; Examination master identifier and display name; Examination-specific certificate numbering sequence configuration; Batch run identifier and result publication timestamp

**Outputs:** Certificate lifecycle record with unique certificate number; Secure verification token reference linked to certificate; Public disclosure field snapshot stored on certificate record; Per-candidate issuance outcome log entry (ISSUED, ISSUANCE_SKIPPED, ISSUANCE_FAILED); Certificate-available notification event payload to Module 07

**Business rules:**
- Issuance occurs only after results are in published state per Module 10 governance
- Candidate must meet both pass criteria and certificate eligibility flag from Module 04
- At most one active (non-revoked) certificate per candidate per examination attempt
- Certificate numbers must be unique within the examination numbering scope
- Verification tokens must not be reversible to internal primary keys in public contexts
- Failed issuance rows do not delete partial records; they remain auditable until resolved or marked permanent failure
- Disclosure snapshot is immutable after issuance; later configuration changes apply only to new certificates

**Validations:**
- Published result must exist and show PASS before issuance proceeds
- Certificate eligibility flag from Module 04 must be true for the examination
- Candidate identifier must resolve to an active registration profile
- Duplicate active certificate check must pass for candidate plus examination attempt
- Mandatory disclosure source fields (e.g., candidate legal name, examination title, issue date) must be non-empty
- Certificate number sequence must not exceed configured maximum if a cap exists
- Retry allowed only from ISSUANCE_FAILED state, not from ISSUED or REVOKED

**Workflow / states:** RESULT_PUBLISHED → ELIGIBILITY_EVALUATED → ISSUANCE_QUEUED → NUMBER_ASSIGNED → TOKEN_GENERATED → ISSUED; alternate paths: ELIGIBILITY_EVALUATED → ISSUANCE_SKIPPED; ISSUANCE_QUEUED → ISSUANCE_FAILED → RETRY_PENDING → ISSUED | PERMANENT_FAILURE

**Dependencies:**
- F10-00x Governed Result Publication and Display (Module 10)
- F04-00x Certificate Eligibility Configuration (Module 04)
- F05-00x Candidate Registration profile fields (Module 05)
- F01-00x Examination Administrator authorization (Module 01)
- F07-00x Notification event subscription and dispatch (Module 07)

**Risks:** Large candidate volumes may require batch throttling not explicitly sized in SOW; Missing candidate photograph or optional fields may block PDF generation downstream if treated as mandatory; Sequence exhaustion under high attempt volume requires administrator intervention

---

#### F11-002 — Digital Certificate PDF Generation with QR Embedding

**One-liner / description:** Renders department-approved digital certificate PDF documents for issued certificate records, dynamically populating candidate and examination fields, embedding a QR code linked to the verification token URL,…

**Business objective:** Provide candidates and verifiers with a tamper-evident printable certificate document that embeds machine-readable QR verification aligned to the department's certificate template standards.

**Actors:** Examination Administrator; System (document generation job); Candidate

**User journey (13 steps):**
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

**Functional capabilities:**
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

**Inputs:** Certificate record with certificate number issue date verification token reference; Active certificate template version and field mapping configuration; Candidate legal name and photograph from Module 05 profile; Examination display name and completion or result date from Module 10; QR placement coordinates and public verification base URL configuration

**Outputs:** Generated certificate PDF binary stored with file reference; QR code embedded within PDF document; Document version record with template version checksum and timestamp; Generation status DOCUMENT_READY or DOCUMENT_FAILED on certificate record

**Business rules:**
- PDF generation executes only for certificates in ISSUED status
- Each regeneration increments document version; prior versions remain auditable
- QR code must encode the same verification token issued at certificate creation
- Template version active at generation time is recorded immutably on the document record
- Revoked certificates do not auto-regenerate; regeneration blocked while status is REVOKED

**Validations:**
- Certificate record must exist and be in ISSUED status before generation starts
- Mandatory template fields (candidate name, examination name, certificate number, issue date) must resolve to non-empty values
- Photograph file reference must be valid format or fall back to configured placeholder image
- Template version identifier must reference an active approved template
- Regeneration request must be authorized to Examination Administrator role
- Public verification base URL must be configured before QR embedding proceeds

**Workflow / states:** ISSUED → DOCUMENT_QUEUED → DOCUMENT_GENERATING → DOCUMENT_READY; alternate: DOCUMENT_GENERATING → DOCUMENT_FAILED → DOCUMENT_QUEUED (retry) → DOCUMENT_READY

**Dependencies:**
- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F05-00x Candidate profile and photograph storage (Module 05)
- F10-00x Published result metadata (Module 10)
- F04-00x Certificate template configuration (Module 04)

**Risks:** Template changes after bulk issuance may require mass regeneration outside initial scope; Large photograph files may impact PDF render performance; QR print quality at small sizes may affect scan success on low-resolution prints

---

#### F11-003 — Candidate Portal Certificate List and Download

**One-liner / description:** Enables authenticated candidates to view a portal list of their issued digital certificates per examination, inspect certificate metadata, and download the generated PDF when document status is ready and certificate…

**Business objective:** Allow eligible candidates to self-service download digitally generated examination certificates from their OTP-authenticated portal login without administrator intervention.

**Actors:** Candidate

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Authenticated candidate session token from OTP login; Certificate list query parameters (optional examination filter); Certificate identifier selected for detail or download

**Outputs:** Candidate-scoped certificate list with status badges; Certificate metadata detail payload; Downloaded certificate PDF file stream; Candidate download audit log entry

**Business rules:**
- Candidates may view and download only their own certificate records
- Download permitted only when certificate status is ISSUED and document status is DOCUMENT_READY
- Revoked certificates remain visible in list with REVOKED badge but download is disabled
- Certificates for examinations where results are not yet published must not appear in list
- Each download event is recorded for audit; repeated downloads are allowed

**Validations:**
- Session must belong to valid authenticated candidate
- Requested certificate identifier must belong to session candidate identifier
- Download request rejected when certificate status is REVOKED or CANCELLED
- Download request rejected when document status is not DOCUMENT_READY
- Certificate identifier must be well-formed and exist or return not-found without leaking other candidates' data

**Workflow / states:** PORTAL_LOGIN → CERTIFICATE_LIST_LOADED → DETAIL_VIEWED → DOWNLOAD_REQUESTED → DOWNLOAD_STREAMED; alternate: DETAIL_VIEWED → DOWNLOAD_BLOCKED (revoked or pending document)

**Dependencies:**
- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F01-00x Candidate OTP authentication session (Module 01)
- SOW Section 4.1 OTP-Based Candidate Login

**Risks:** Candidates may attempt to share portal credentials to download on behalf of others; Pending document state may generate support queries if issuance-to-PDF delay is long

---

#### F11-004 — Public Online Certificate Verification Portal

**One-liner / description:** Provides a public-facing verification experience for verifiers and third parties to confirm certificate authenticity by scanning the QR code or entering a certificate number, returning valid, not-found, or…

**Business objective:** Enable third parties to independently confirm that a certificate was issued by the department and determine whether it is currently valid, without exposing non-approved personal information.

**Actors:** Verifier/Public User

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Verification token from QR-encoded URL parameter; Certificate number entered on public form; Client IP address and request timestamp for rate limiting; Approved public disclosure field snapshot stored on certificate record

**Outputs:** Valid verification result panel with approved disclosure field values; Not-found verification result panel; Revoked or cancelled verification result panel; Verification audit log entry with outcome category VALID NOT_FOUND or REVOKED

**Business rules:**
- Public verification requires no authentication
- Only fields approved for public disclosure and captured in issuance snapshot may be displayed on valid outcome
- Revoked certificates must never present as valid regardless of token possession
- Not-found responses must be uniform for invalid token and unknown certificate number to reduce enumeration
- Verification displays department branding confirming issuer identity
- Disclosure snapshot on certificate record governs displayed fields; live profile changes do not alter verification output

**Validations:**
- Verification token must match expected length and character set before database lookup
- Certificate number entry must match configured format pattern
- Empty token and empty certificate number submissions rejected with inline field message
- Rate limit counter enforced per client IP or token bucket configuration
- Revoked status checked after record match before returning valid outcome

**Workflow / states:** VERIFY_REQUESTED → TOKEN_OR_NUMBER_VALIDATED → LOOKUP_EXECUTED → OUTCOME_VALID | OUTCOME_NOT_FOUND | OUTCOME_REVOKED

**Dependencies:**
- F11-001 Eligibility-Triggered Certificate Issuance and Numbering (verification token and disclosure snapshot)
- F04-00x Approved public disclosure field configuration (Module 04)
- F11-005 Certificate Cancellation and Revocation (revoked status propagation)
- SOW Sections 35 QR Code on Certificate and 36 Online Certificate Verification

**Risks:** Certificate number enumeration attempts despite uniform not-found responses; Over-disclosure if disclosure configuration includes fields later deemed sensitive; High QR scan traffic during result season may require CDN caching constraints review

---

#### F11-005 — Certificate Cancellation and Revocation Management

**One-liner / description:** Allows Examination Administrators to cancel or revoke previously issued certificates with mandatory reason capture, immutable status transition history, immediate propagation to public verification and candidate…

**Business objective:** Provide governed certificate invalidation when issuance errors, disqualifications, or administrative decisions require a previously issued certificate to be treated as no longer valid, without deleting historical records.

**Actors:** Examination Administrator

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Certificate identifier selected for revocation; Revocation reason code from configured reference list; Mandatory revocation notes text entered by administrator; Administrator session identity and timestamp

**Outputs:** Updated certificate status REVOKED or CANCELLED; Revocation history event with reason actor and timestamp; Revoked outcome on subsequent public verification requests; Disabled download state on candidate portal certificate row

**Business rules:**
- Only ISSUED certificates may be revoked; DOCUMENT_PENDING certificates follow separate cancellation path if needed
- Revocation does not delete certificate number token or document history records
- Revoked certificates cannot be reinstated to ISSUED within this module scope without separate client change request
- Revocation reason code must be selected from administrator-maintained reference list
- Public verification must reflect revoked status within same request cycle after commit
- Revocation action requires Examination Administrator authorization

**Validations:**
- Certificate must exist and be in ISSUED status at time of revocation request
- Revocation reason code must be non-empty and valid reference value
- Revocation notes must meet minimum length threshold
- Administrator must hold permission for certificate revocation operation
- Duplicate revocation request on REVOKED certificate rejected with business error
- Revocation timestamp must not precede original issue date

**Workflow / states:** ISSUED → REVOKE_REQUESTED → REVOKE_CONFIRMED → REVOKED; alternate: REVOKED → REVOKE_REQUESTED → REVOKE_REJECTED (already revoked)

**Dependencies:**
- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-003 Candidate Portal Certificate List and Download
- F11-004 Public Online Certificate Verification Portal
- F01-00x Examination Administrator authorization (Module 01)
- SOW Section 37 Certificate Security

**Risks:** Delayed propagation to CDN-cached verification pages if caching introduced later; Mass revocation after data correction event may require bulk tool outside current scope; Candidates may retain previously downloaded PDF copies despite revocation

---

#### F11-006 — Administrator Certificate Register Search and Export

**One-liner / description:** Provides Examination Administrators with a searchable register of all certificate lifecycle records, advanced filtering, read-only detail with lifecycle timeline, and CSV export of filtered results to support…

**Business objective:** Give examination administrators consolidated visibility into issued, pending, and revoked certificates across examinations for operational management audit response and downstream reporting.

**Actors:** Examination Administrator

**User journey (11 steps):**
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

**Functional capabilities:**
- Display paginated certificate register with sortable columns
- Search register by certificate number and candidate name
- Filter register by examination issue date range status and document status
- Show register empty state when no rows match criteria
- Open read-only administrator certificate detail with lifecycle timeline
- Export filtered certificate register to CSV file
- Confirm export scope and row count before download
- Enforce administrator role authorization for register access
- Expose register aggregates as reporting hooks for Module 12

**Inputs:** Search text for certificate number or candidate name; Filter values for examination identifier status issue date range document status; Pagination page number and page size; Sort column and direction; Export request with current filter snapshot

**Outputs:** Paginated certificate register row set; Administrator certificate detail with lifecycle timeline events; CSV export file of filtered certificate records; Register aggregate counts by status for reporting hooks

**Business rules:**
- Register includes ISSUED REVOKED DOCUMENT_PENDING and ISSUANCE_FAILED records within administrator visibility scope
- Export includes only columns approved for administrator operational use; verification tokens are never exported in plain form
- Export row set must match active filter criteria at time of export request
- Lifecycle timeline displays issuance document generation and revocation events in chronological order
- Register access limited to Examination Administrator and authorized oversight roles per Module 01

**Validations:**
- Issue date range filter requires end date on or after start date
- Search text length must meet minimum threshold before server search executes
- Export request rejected when estimated row count exceeds configured export limit with administrator message
- Pagination parameters must be within allowed bounds
- Unauthorized session rejected before register data returned

**Workflow / states:** REGISTER_LOADED → SEARCH_OR_FILTER_APPLIED → ROW_SELECTED → DETAIL_VIEWED → EXPORT_REQUESTED → EXPORT_DOWNLOADED

**Dependencies:**
- F11-001 Eligibility-Triggered Certificate Issuance and Numbering
- F11-002 Digital Certificate PDF Generation with QR Embedding
- F11-005 Certificate Cancellation and Revocation Management
- F01-00x Examination Administrator authorization (Module 01)
- F12-00x Examination Administration and Reporting hooks (Module 12)

**Risks:** Large export requests during peak season may require asynchronous export enhancement; Centre-scoped visibility if added later increases authorization complexity; PII in CSV exports requires client data handling policy compliance

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 11 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 11 Certificate Management** (6 features).
> Features: F11-001 Eligibility-Triggered Certificate Issuance and Numbering; F11-002 Digital Certificate PDF Generation with QR Embedding; F11-003 Candidate Portal Certificate List and Download; F11-004 Public Online Certificate Verification Portal; F11-005 Certificate Cancellation and Revocation Management; F11-006 Administrator Certificate Register Search and Export.
> Purpose: Eligibility-triggered certificate issuance and numbering, PDF with QR, candidate download, public verification, cancellation/revocation, admin register/export.
> Draw: Eligibility-triggered issuance + numbering sequence; PDF + QR embed + public verify portal flow; Certificate lifecycle (ISSUED / CANCELLED / REVOKED); Issuance log outcomes (ISSUED / SKIPPED / FAILED); ERD for `certificate_number_sequence`, `certificate`, `certificate_document`, `certificate_verification_token`, `certificate_verification_hit`, `certificate_download_log`.
