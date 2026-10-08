# ChatGPT Visualization Brief — Module 05: Candidate Registration

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 05 Candidate Registration
**Features:** 14 (F05-021 … F05-034)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 05 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. End-to-end registration journey swimlane (Govt vs Other Org)
2. OTP login sequence + lockout state machine
3. Fee determination decision tree (category × attempt)
4. Payment success/fail recovery flowchart
5. Registration status state machine + admin verification gate
6. Registration ERD
7. Feature relationship / dependency graph within this module and to other modules
8. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Candidate Registration
**Purpose:** Candidate OTP portal access; government and other-organisation registration paths; centre preferences; fee determination and payment; confirmation; optional admin verification.

**Actors (union across features):**
- Candidate
- Examination Administrator

**Feature list:**
- **F05-021** — Candidate OTP Login and Portal Session Security
- **F05-022** — Registration Category Type Selection
- **F05-023** — Government Employee KGID Lookup and Detail Retrieval
- **F05-024** — Government Employee Detail Confirmation and Supplementary Capture
- **F05-025** — Other Organisation Manual Candidate and Employment Detail Capture
- **F05-026** — Competent Authority Document Template Download and Digitally Signed Upload
- **F05-027** — Open Examination Selection for Registration
- **F05-028** — Examination Centre First and Second Preference Selection
- **F05-029** — Examination Attempt History and Category Fee Applicability Determination
- **F05-030** — Registration Fee Payment Initiation and Success Completion
- **F05-031** — Failed Payment Handling and Registration Recovery
- **F05-032** — Registration Confirmation and Unique Application Number Generation
- **F05-033** — Candidate Registration Status Self-Service Visibility
- **F05-034** — Optional Registration Application Verification and Administrator Review Gate

### DATA MODEL (from EXAM DB design v2.1)

- `candidate`
- `otp_security_parameter`
- `otp_challenge`
- `candidate_portal_session`
- `document_template`
- `registration`
- `registration_centre_preference`
- `competent_authority_document`
- `payment_transaction`
- `registration_admin_review`
- `candidate_exam_attempt_counter`
- `fee_determination_audit`

### FEATURE CATALOGUE

#### F05-021 — Candidate OTP Login and Portal Session Security

**One-liner / description:** Provides mobile-number-based OTP authentication for candidates accessing the examination registration portal, including OTP generation, delivery handoff, verification, resend controls, expiry enforcement,…

**Business objective:** Ensure only candidates with access to the registered mobile number can enter the portal while enforcing enterprise-grade OTP and session security controls mandated for government examination registration.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate opens the examination candidate portal landing page. 2. Candidate enters registered mobile number on the login screen. 3. System validates mobile number format and eligibility for portal access. 4. Candidate submits mobile number to request OTP. 5. System generates time-bound OTP and dispatches via notification channel (Module 07). 6. Candidate receives OTP on mobile device. 7. Candidate enters OTP on verification screen. 8. On successful verification, system creates authenticated candidate session and redirects to portal home or in-progress registration. 9. If OTP is incorrect, system increments failed-attempt counter and displays remaining attempts. 10. If retry limit exceeded, system blocks further attempts for configured cooldown period. 11. Candidate may request OTP resend subject to resend interval and maximum resend count. 12. If OTP expires before entry, candidate must request new OTP. 13. During active session, idle timeout locks session and requires re-authentication.

**Functional capabilities:**
- Mobile number entry screen for login initiation
- Mobile number format and portal-eligibility validation
- OTP generation with configurable expiry duration
- OTP dispatch request to notification service
- OTP entry and verification screen
- Failed OTP attempt counter with retry limit enforcement
- OTP resend with interval and maximum resend controls
- Session creation upon successful OTP verification
- Idle session timeout and forced re-login
- Login audit event recording for security trace
- Blocked-state messaging when retry or resend limits exceeded
- Portal redirect for authenticated candidate with existing registration context

**Inputs:** Mobile number; OTP code; Resend OTP request; Session idle activity signals

**Outputs:** Authenticated candidate session token; OTP delivery status; Failed-attempt and block status messages; Security audit events

**Business rules:**
- Candidate login shall occur exclusively through OTP; password login is out of scope for candidates
- OTP shall expire after configured duration
- Failed OTP attempts shall be tracked and limited
- OTP resend shall be rate-limited
- Active candidate sessions shall timeout after configured idle period
- Concurrent session policy shall align with Module 01 session controls

**Validations:**
- Mobile number required and must match approved national mobile format pattern
- Mobile number must correspond to a candidate-permitted portal identity
- OTP must be numeric and match length configured for the portal
- Expired OTP rejected with explicit expiry message
- Incorrect OTP rejected and failed-attempt counter incremented
- Resend blocked until minimum interval elapsed
- Verification blocked when retry limit or resend limit exceeded

**Workflow / states:** UNAUTHENTICATED → MOBILE_ENTERED → OTP_REQUESTED → OTP_PENDING → OTP_VERIFIED → SESSION_ACTIVE → SESSION_IDLE_WARNING (optional) → SESSION_EXPIRED → UNAUTHENTICATED; OTP_PENDING → OTP_FAILED (increment attempts) → OTP_BLOCKED when limit exceeded; OTP_PENDING → OTP_EXPIRED → OTP_REQUESTED on resend

**Dependencies:**
- Module 01 — Candidate Role and Portal Permission Catalogue
- Module 01 — Session Timeout Idle Lock and Concurrent Session Controls
- Module 01 — User Access Audit Register and Security Event Trace
- Module 07 — Multi-Channel Notification Dispatch Engine

**Risks:** SMS delivery delays may cause OTP expiry before candidate entry; Shared mobile devices may expose OTP to unauthorised viewers; Brute-force OTP guessing if retry limits set too high

---

#### F05-022 — Registration Category Type Selection

**One-liner / description:** Allows an authenticated candidate to choose between Registration Type 1 (Government Department Employee) and Registration Type 2 (PSU/Board/Corporation/Society/Other eligible organisation) at the start of a new…

**Business objective:** Route each candidate into the correct registration path with distinct data capture, document, and fee rules before any category-specific steps begin.

**Actors:** Candidate

**User journey (1 steps):**
1. Authenticated candidate initiates new examination registration from portal home. 2. System presents registration category type selection screen with two paths: Government Department Employee and Other Organisation Employee. 3. Candidate reads category descriptions and eligibility guidance. 4. Candidate selects one registration type. 5. System validates selection is allowed for candidate context. 6. System persists registration type on draft registration record. 7. System routes candidate to Government KGID path (F05-003) or Other Organisation manual path (F05-005). 8. If candidate navigates back, system warns that changing type may reset captured data.

**Functional capabilities:**
- Registration type selection screen with two distinct paths
- Eligibility guidance text per registration category
- Persist selected registration type on draft registration
- Route to government or other-organisation downstream features
- Back-navigation guard when type change would invalidate captured data
- Display previously selected type when resuming incomplete registration

**Inputs:** Selected registration type; Draft registration identifier

**Outputs:** Persisted registration category type; Route decision to government or other-organisation flow

**Business rules:**
- Exactly one registration type must be selected before profile capture begins
- Registration type determines mandatory KGID path versus manual detail path
- Registration type determines fee rules and competent authority document requirement
- Changing registration type after downstream data capture may require draft reset per policy

**Validations:**
- Registration type selection required before proceeding
- Selected type must be one of configured enum values
- Draft registration must belong to authenticated candidate
- Type change blocked or confirmed when dependent data already captured

**Workflow / states:** DRAFT_CREATED → TYPE_UNSELECTED → TYPE_SELECTED_GOV or TYPE_SELECTED_OTHER → routed to category path; TYPE_SELECTED_* → TYPE_CHANGE_PENDING (if back) → TYPE_UNSELECTED or retained with confirmation

**Dependencies:**
- F05-001 — Candidate OTP Login and Portal Session Security
- Module 04 — Examination Master Configuration for open registration context

**Risks:** Candidate selects wrong category requiring restart or administrator intervention

---

#### F05-023 — Government Employee KGID Lookup and Detail Retrieval

**One-liner / description:** Captures mandatory KGID number for government department employee registrations, invokes KGID integration to retrieve available employee information, and displays retrieved details for candidate review before…

**Business objective:** Automate government employee identity and employment detail retrieval through authoritative KGID integration while ensuring candidates review system-fetched data before proceeding.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate on government registration path reaches KGID entry step. 2. Candidate enters KGID number. 3. System validates KGID format. 4. Candidate submits KGID for lookup. 5. System calls KGID integration hub with KGID number. 6. On success, system displays retrieved fields: employee name, KGID number, department, and other available employment details. 7. On integration failure or not-found, system shows error with retry option. 8. On partial data, system displays available fields and flags missing attributes. 9. Candidate proceeds to confirmation step (F05-004) with retrieved payload attached to draft.

**Functional capabilities:**
- KGID number entry form for government path
- KGID format validation before lookup
- KGID integration lookup invocation
- Retrieved employee detail read-only display panel
- Integration error and not-found handling with retry
- Partial retrieval display with missing-field indicators
- Attach retrieved KGID payload to draft registration
- Lookup attempt logging for audit

**Inputs:** KGID number; Draft registration identifier

**Outputs:** Retrieved employee detail snapshot; KGID lookup status; Integration error messages

**Business rules:**
- KGID number is mandatory for government department employee registrations
- Retrieved KGID details must be displayed before candidate may confirm
- KGID lookup result is subject to data availability from external KGID system
- Duplicate KGID use across active registrations may be restricted per department policy

**Validations:**
- KGID number required on government path
- KGID must match configured format pattern
- Lookup blocked when integration unavailable if policy requires live verification
- Retrieved KGID must match entered KGID
- Draft registration must be government category type

**Workflow / states:** KGID_PENDING → KGID_SUBMITTED → KGID_LOOKUP_IN_PROGRESS → KGID_RETRIEVED or KGID_NOT_FOUND or KGID_INTEGRATION_ERROR → KGID_RETRIEVED proceeds to confirmation

**Dependencies:**
- F05-002 — Registration Category Type Selection
- Module 02 — KGID Government Employee Lookup Integration
- Module 02 — Integration Retry Logging and Error Observability

**Risks:** KGID service downtime blocks government registration path; Stale KGID data if source system not updated

---

#### F05-024 — Government Employee Detail Confirmation and Supplementary Capture

**One-liner / description:** Enables government department employee candidates to confirm retrieved KGID details as correct and capture additional registration fields such as mobile number and other required information before saving validated…

**Business objective:** Ensure government candidates explicitly attest to KGID-retrieved identity data and supply any registration fields not available from KGID before examination selection.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate views retrieved KGID details from prior step. 2. Candidate confirms details are correct via explicit confirmation control. 3. If details incorrect, candidate returns to KGID re-entry or support guidance. 4. Upon confirmation, system unlocks supplementary detail form. 5. Candidate enters mobile number and other required registration fields. 6. System validates all supplementary fields. 7. Candidate submits profile section. 8. System saves validated government employee profile to draft registration. 9. System advances candidate to examination selection (F05-007).

**Functional capabilities:**
- KGID retrieved detail confirmation checkbox or attestation control
- Incorrect-detail escalation guidance and return-to-KGID navigation
- Supplementary registration field form post-confirmation
- Mobile number capture and validation on government path
- Configurable additional field capture per approved requirements
- Profile save with validation summary errors
- Mark government profile section complete on draft

**Inputs:** KGID confirmation attestation; Mobile number; Additional configurable registration fields

**Outputs:** Validated government employee profile on draft; Profile section completion status

**Business rules:**
- Candidate must confirm KGID retrieved details before supplementary capture
- Mobile number required for government registrations as applicable
- Confirmed KGID snapshot retained even if supplementary fields edited later before submission
- Profile must pass validation before examination selection unlocked

**Validations:**
- KGID confirmation attestation required
- Mobile number required and valid format
- Mobile number uniqueness policy per registration rules if enforced
- Configurable additional fields requiredness enforced per field definition
- Cannot confirm without successful prior KGID retrieval

**Workflow / states:** KGID_RETRIEVED → AWAITING_CONFIRMATION → CONFIRMED → SUPPLEMENTARY_CAPTURE → PROFILE_VALIDATED → PROFILE_COMPLETE; AWAITING_CONFIRMATION → REJECTED returns to KGID step

**Dependencies:**
- F05-003 — Government Employee KGID Lookup and Detail Retrieval
- Module 04 — Configurable registration field definitions if centrally managed

**Risks:** Candidate confirms incorrect KGID data without noticing discrepancies

---

#### F05-025 — Other Organisation Manual Candidate and Employment Detail Capture

**One-liner / description:** Captures manual candidate and employment details for PSU, Board, Corporation, Society, and other eligible organisation employees including organisation category selection, candidate name, mobile number, employee ID,…

**Business objective:** Collect complete identity and employment information for non-government candidates who cannot use KGID retrieval, enabling fee, document, and registration processing.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate on other-organisation path reaches manual detail capture step. 2. Candidate selects organisation sub-category: PSU, Board, Corporation, Society, or Other eligible organisation. 3. Candidate enters candidate name. 4. Candidate enters mobile number. 5. Candidate enters employee ID. 6. Candidate enters organisation or department name. 7. Candidate completes other configurable required fields. 8. System validates all entries. 9. Candidate submits manual profile section. 10. System saves validated profile to draft registration. 11. System routes candidate to competent authority document steps (F05-006).

**Functional capabilities:**
- Organisation sub-category selection control
- Manual candidate name capture
- Mobile number capture
- Employee ID capture
- Organisation or department name capture
- Configurable additional field rendering and validation
- Manual profile save to draft registration
- Profile section completion marker for other-organisation path

**Inputs:** Organisation sub-category; Candidate name; Mobile number; Employee ID; Organisation or department; Configurable additional fields

**Outputs:** Validated other-organisation employee profile on draft; Organisation sub-category persisted

**Business rules:**
- Other-organisation path requires full manual detail capture
- Examination registration fee is mandatory for this category path
- Competent authority digitally signed document required before registration completion
- Field configurability subject to final approved requirements

**Validations:**
- Organisation sub-category required
- Candidate name required with minimum length
- Mobile number required and valid format
- Employee ID required per configuration
- Organisation or department name required
- Configurable fields enforced for requiredness and format
- Draft must be other-organisation registration type

**Workflow / states:** MANUAL_PROFILE_PENDING → MANUAL_PROFILE_IN_PROGRESS → MANUAL_PROFILE_VALIDATED → MANUAL_PROFILE_COMPLETE

**Dependencies:**
- F05-002 — Registration Category Type Selection
- F05-006 — Competent Authority Document Template Download and Digitally Signed Upload

**Risks:** Manual entry errors without authoritative identity source; Fraudulent organisation claims pending document verification

---

#### F05-026 — Competent Authority Document Template Download and Digitally Signed Upload

**One-liner / description:** Provides prescribed competent authority document template download, digitally signed document upload during other-organisation registration, file validation, registration association, and administrator review…

**Business objective:** Obtain legally attested employment confirmation from competent authority for non-government candidates and make uploaded evidence available for administrator verification.

**Actors:** Candidate; Examination Administrator

**User journey (1 steps):**
1. Other-organisation candidate reaches competent authority document step. 2. Candidate views document requirement instructions. 3. Candidate downloads prescribed competent authority document template. 4. Candidate completes template offline and obtains competent authority digital signature. 5. Candidate returns to portal upload screen. 6. Candidate selects digitally signed document file. 7. System validates file type, size, and digital signature presence per policy. 8. On success, system stores document linked to draft registration. 9. Candidate sees upload success with file name and timestamp. 10. On validation failure, candidate sees specific error and may re-upload. 11. Uploaded document associated for administrator review on registration record. 12. Candidate proceeds to examination selection once document requirement satisfied.

**Functional capabilities:**
- Competent authority document requirement instruction panel
- Prescribed template download action
- Digitally signed document file upload control
- Upload file type and size validation
- Digital signature verification check on uploaded file
- Document storage linked to registration draft
- Upload success and failure feedback
- Replace document before registration submission
- Administrator review association flag on registration
- Document metadata visible in administrator registration context

**Inputs:** Template download request; Digitally signed document file

**Outputs:** Stored competent authority document; Upload validation result; Document metadata for administrator review

**Business rules:**
- Competent authority document mandatory for other-organisation registrations
- Document must be digitally signed by competent authority
- Template format prescribed by department and downloadable from portal
- Uploaded document associated with candidate registration for verification
- Document replace allowed until registration finalised

**Validations:**
- Upload required before registration completion on other-organisation path
- File extension must match allowed signed document types
- File size within configured maximum
- Digital signature validation per approved technical policy
- Only one active competent authority document per draft unless replace flow used
- Upload blocked for government registration path

**Workflow / states:** DOCUMENT_PENDING → TEMPLATE_DOWNLOADED → UPLOAD_SELECTED → UPLOAD_VALIDATING → DOCUMENT_ACCEPTED or DOCUMENT_REJECTED → DOCUMENT_ACCEPTED enables next step; DOCUMENT_ACCEPTED → DOCUMENT_REPLACED on re-upload

**Dependencies:**
- F05-005 — Other Organisation Manual Candidate and Employment Detail Capture
- Module 01 — Examination Administrator Role and Organisation-Wide Permissions
- F05-014 — Optional Registration Application Verification and Administrator Review Gate

**Risks:** Invalid or forged signatures if validation weak; Large file uploads on slow mobile networks

---

#### F05-027 — Open Examination Selection for Registration

**One-liner / description:** Displays examinations currently open for candidate registration, allows candidate to select target examination, view applicable examination details, and bind examination choice to the in-progress registration draft.

**Business objective:** Ensure candidates register only for examinations accepting registrations and understand examination parameters before centre preference and fee steps.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate completes category-specific profile and document prerequisites. 2. Candidate reaches examination selection step. 3. System lists examinations with registration currently open. 4. Candidate browses examination name, schedule summary, and instructions excerpt. 5. Candidate selects one examination. 6. System displays full applicable examination details for selected item. 7. Candidate confirms examination selection. 8. System binds examination to draft registration. 9. System advances to centre preference selection (F05-008). 10. If no examinations open, candidate sees empty state with guidance.

**Functional capabilities:**
- Open-for-registration examination list for candidates
- Examination summary card with key details
- Examination detail view for selected examination
- Single examination selection per registration draft
- Bind selected examination to draft registration
- Empty state when no examinations open
- Change examination selection before final submission if policy allows

**Inputs:** Selected examination identifier; Draft registration identifier

**Outputs:** Examination bound to draft registration; Examination detail display

**Business rules:**
- Only examinations marked open for registration appear
- One examination selected per registration instance
- Examination selection required before centre preferences
- Examination eligibility may consider candidate category from Module 04 configuration

**Validations:**
- Selected examination must be in open-for-registration state
- Selected examination must be eligible for candidate category
- Profile and document prerequisites must be complete before selection saved
- Draft must belong to authenticated candidate

**Workflow / states:** EXAM_UNSELECTED → EXAM_LIST_VIEWED → EXAM_SELECTED → EXAM_CONFIRMED → EXAM_BOUND; EXAM_CONFIRMED → EXAM_CHANGE_PENDING if change allowed → EXAM_SELECTED

**Dependencies:**
- Module 04 — Examination Master Configuration
- F05-004 or F05-005 — Profile completion features
- F05-006 — Competent authority document for other-organisation path

**Risks:** Candidate selects wrong examination requiring draft amendment

---

#### F05-028 — Examination Centre First and Second Preference Selection

**One-liner / description:** Captures candidate's first and second preferred authorised examination centres from administrator-configured active centre list for use during downstream centre allocation while displaying selection rules and…

**Business objective:** Collect candidate centre preferences to inform administrator and system centre allocation per capacity, schedule, and business rules without performing final allocation in this module.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate completes examination selection. 2. Candidate reaches centre preference step. 3. System loads list of active authorised examination centres from Module 03. 4. Candidate selects Centre Preference 1 from dropdown or searchable list. 5. Candidate selects Centre Preference 2 from remaining centres. 6. System validates preferences are distinct and centres active. 7. Candidate submits preferences. 8. System persists both preferences on draft registration. 9. System advances to attempt and fee evaluation (F05-009). 10. Candidate may edit preferences until registration finalised.

**Functional capabilities:**
- Active authorised centre list for preference selection
- Centre Preference 1 selection control
- Centre Preference 2 selection control
- Distinct preference validation
- Centre search or filter within preference pickers
- Persist both preferences on draft registration
- Display centre name and location summary in picker
- Edit preferences before registration submission

**Inputs:** Centre Preference 1 identifier; Centre Preference 2 identifier; Draft registration identifier

**Outputs:** Persisted centre preferences on draft; Preference validation messages

**Business rules:**
- Candidates must select exactly two preferred centres
- Preference 1 and Preference 2 must be different centres
- Only active authorised centres available for selection
- Final centre allocation performed in Module 06; preferences are inputs only
- Preferences used during allocation considering capacity and schedule

**Validations:**
- Centre Preference 1 required
- Centre Preference 2 required
- Preferences must reference distinct centre identifiers
- Selected centres must be active and authorised
- Examination must be selected before preferences saved

**Workflow / states:** PREFERENCES_PENDING → PREFERENCE_1_SELECTED → PREFERENCE_2_SELECTED → PREFERENCES_VALIDATED → PREFERENCES_SAVED

**Dependencies:**
- F05-007 — Open Examination Selection for Registration
- Module 03 — Authorised Examination Centre Register and Search

**Risks:** Popular centres oversubscribed; candidate may not receive preferred centre

---

#### F05-029 — Examination Attempt History and Category Fee Applicability Determination

**One-liner / description:** Evaluates candidate prior examination attempt history against selected examination and category to determine applicable fee: free first attempt for government employees, fee for subsequent government attempts, and…

**Business objective:** Apply correct category-based and attempt-based fee rules automatically before payment routing so candidates see accurate fee obligation and free-registration eligibility.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate completes centre preferences. 2. System evaluates attempt history for candidate against selected examination. 3. System identifies registration category: government or other-organisation. 4. For government employee: system checks if first examination attempt for configured scope. 5. If first attempt, system marks fee as not applicable (free registration). 6. If subsequent attempt, system retrieves configured fee amount from Module 04. 7. For other-organisation: system retrieves mandatory configured fee amount. 8. System displays fee determination summary screen with amount, reason, and attempt count context. 9. Candidate acknowledges fee summary. 10. System routes to payment (F05-010) if fee applicable or directly toward confirmation path if free.

**Functional capabilities:**
- Attempt history lookup for candidate and examination
- First-attempt versus subsequent-attempt classification for government employees
- Government first-attempt free registration rule application
- Government subsequent-attempt fee retrieval
- Other-organisation mandatory fee retrieval
- Fee determination summary display with explanatory reason
- Persist fee applicability outcome on draft registration
- Route to payment or skip payment based on determination

**Inputs:** Candidate identifier; Selected examination identifier; Registration category type; Historical registration and attempt records

**Outputs:** Fee applicable flag; Applicable fee amount; Attempt classification label; Fee determination audit record

**Business rules:**
- Government department employees receive free registration for first examination attempt
- Fee applicable for second and subsequent government employee attempts
- Fee amounts configurable by administrator in Module 04
- Fee mandatory for eligible non-government organisation candidates
- Attempt history maintained to support fee determination
- Registration complete only after successful payment where payment mandatory

**Validations:**
- Examination and category must be set before fee evaluation
- Fee configuration must exist when fee applicable
- Attempt history query scoped to authenticated candidate only
- Free path blocked if attempt history indicates subsequent attempt

**Workflow / states:** FEE_EVAL_PENDING → ATTEMPT_HISTORY_LOADED → FEE_NOT_APPLICABLE (government first) or FEE_APPLICABLE → FEE_DETERMINED → routes to PAYMENT_REQUIRED or PAYMENT_SKIPPED

**Dependencies:**
- F05-002 — Registration Category Type Selection
- F05-007 — Open Examination Selection for Registration
- Module 04 — Certificate Eligibility and Examination Fee Configuration

**Risks:** Incorrect attempt count if historical data incomplete; Fee rule changes mid-registration handled by snapshot at determination time

---

#### F05-030 — Registration Fee Payment Initiation and Success Completion

**One-liner / description:** Initiates payment gateway transaction when registration fee is applicable, handles successful payment callback, records transaction and reference numbers, generates payment receipt, and progresses registration toward…

**Business objective:** Collect mandatory examination registration fees through integrated payment gateway and mark registration fee-compliant upon successful payment as prerequisite to registration finalisation.

**Actors:** Candidate

**User journey (1 steps):**
1. Fee determination indicates payment required (F05-009). 2. Candidate views payment summary with examination, fee amount, and candidate details. 3. Candidate initiates payment. 4. System creates payment transaction record and calls payment gateway via Module 02. 5. Candidate redirected to payment gateway hosted page or embedded flow. 6. Candidate completes payment on gateway. 7. System receives success callback with transaction reference. 8. System verifies callback authenticity and amount match. 9. System updates payment status to successful on draft registration. 10. System stores transaction and reference number. 11. Candidate views payment success confirmation. 12. Candidate downloads or views payment receipt. 13. System enables registration finalisation step (F05-012).

**Functional capabilities:**
- Payment summary screen before gateway handoff
- Payment initiation with transaction record creation
- Payment gateway redirect or embed handoff
- Successful payment callback verification
- Transaction and reference number persistence
- Payment receipt display and download
- Registration fee-compliant status update on success
- Advance registration workflow after successful payment

**Inputs:** Draft registration identifier; Applicable fee amount; Payment gateway callback payload

**Outputs:** Payment transaction record; Transaction reference number; Payment receipt; Fee-compliant registration status

**Business rules:**
- Payment mandatory where fee determination marks fee applicable
- Registration not complete until successful payment when mandatory
- Successful payment callback must match initiated amount and registration
- Transaction reference stored for audit and receipt
- Free registrations skip this feature entirely

**Validations:**
- Payment initiation blocked when fee not applicable
- Payment amount must match determined fee amount
- Callback signature or token verified per gateway policy
- Duplicate success callback idempotent handling
- Draft must be in payment-pending state for initiation

**Workflow / states:** PAYMENT_PENDING → PAYMENT_INITIATED → GATEWAY_IN_PROGRESS → PAYMENT_SUCCESS → FEE_COMPLIANT → REGISTRATION_FINALISATION_ENABLED; PAYMENT_INITIATED → PAYMENT_ABANDONED if candidate returns without completion

**Dependencies:**
- F05-009 — Examination Attempt History and Category Fee Applicability Determination
- Module 02 — Payment Gateway Fee Transaction Integration
- F05-012 — Registration Confirmation Application Number and Status Visibility

**Risks:** Callback delay leaves registration in pending payment state; Amount mismatch between initiation and callback

---

#### F05-031 — Failed Payment Handling and Registration Recovery

**One-liner / description:** Handles failed, declined, cancelled, and abandoned payment scenarios during registration including failure reason display, draft preservation in payment-pending state, retry payment initiation, duplicate-transaction…

**Business objective:** Prevent loss of registration progress on payment failure and give candidates a controlled recovery path to complete mandatory fee payment without duplicate charges or orphaned registrations.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate initiates payment from F05-010. 2. Payment gateway returns failure, decline, cancellation, or timeout. 3. System receives failure callback or detects abandoned session. 4. System records failed payment attempt with reason code. 5. Candidate redirected to failed payment screen showing reason and registration summary. 6. Candidate reviews remaining fee amount due unchanged. 7. Candidate chooses retry payment action. 8. System validates no successful payment already recorded. 9. System initiates new payment transaction linked to same draft. 10. On repeated failures, system shows escalating guidance and support contact. 11. Registration remains incomplete and not confirmed until success. 12. Candidate may exit and resume payment later from registration status view (F05-013).

**Functional capabilities:**
- Failed payment callback processing
- Abandoned payment session detection
- Failed payment reason display to candidate
- Preserve draft registration in payment-pending state
- Retry payment initiation from failure screen
- Prevent duplicate successful charges for same registration
- Failed attempt counter and audit trail
- Resume failed payment from registration status view
- Block registration finalisation while payment failed or pending

**Inputs:** Payment failure callback payload; Abandoned session signal; Retry payment request

**Outputs:** Failed payment attempt record; Payment-pending draft state; Retry payment transaction; Candidate failure guidance messages

**Business rules:**
- Registration incomplete when mandatory payment fails
- Candidate may retry payment without re-entering prior registration steps
- Each retry creates new gateway transaction unless policy reuses open session
- Successful payment on any attempt completes fee requirement
- Failed attempts logged for administrator reconciliation in Module 12 scope

**Validations:**
- Failure callback authenticity verified
- Retry blocked if registration already fee-compliant
- Retry blocked if maximum retry count exceeded when configured
- Draft ownership verified on retry
- Concurrent retry initiation prevented

**Workflow / states:** PAYMENT_INITIATED → PAYMENT_FAILED or PAYMENT_CANCELLED or PAYMENT_ABANDONED → PAYMENT_PENDING_RETRY → PAYMENT_INITIATED (retry) → PAYMENT_SUCCESS or PAYMENT_FAILED; PAYMENT_PENDING_RETRY → RESUMED_FROM_STATUS_VIEW

**Dependencies:**
- F05-010 — Registration Fee Payment Initiation and Success Completion
- F05-013 — Candidate Registration Status Self-Service Visibility

**Risks:** Multiple partial gateway sessions causing reconciliation complexity; Candidate abandons registration indefinitely in payment-pending state

**Notes:** Covers FRS §13 failed payment handling explicitly called out as prior coverage gap.

---

#### F05-032 — Registration Confirmation and Unique Application Number Generation

**One-liner / description:** Finalises eligible draft registrations by validating prerequisites, generating unique registration or application number, persisting complete application including examination, centre preferences, documents, and…

**Business objective:** Provide candidates with definitive proof of completed examination registration and a unique reference for all downstream scheduling, allocation, and support interactions.

**Actors:** Candidate

**User journey (1 steps):**
1. Candidate completes all mandatory steps: profile, documents (if applicable), examination, preferences, and payment (if applicable). 2. Candidate reaches registration review and submit step. 3. System displays registration summary for final review. 4. Candidate submits registration. 5. System validates all prerequisites complete and fee-compliant if required. 6. System generates unique application or registration number. 7. System persists complete registration record from draft. 8. System transitions registration status to submitted or confirmed per policy. 9. Candidate views confirmation screen with application number. 10. System triggers registration confirmation notification via Module 07. 11. Candidate may print or save confirmation summary.

**Functional capabilities:**
- Registration final review summary screen
- Prerequisite completeness validation before submit
- Unique application number generation
- Persist complete registration from draft
- Store examination details on registration
- Store centre preferences on registration
- Store uploaded documents reference on registration
- Store payment details where applicable
- Registration confirmation display
- Registration confirmation notification trigger

**Inputs:** Draft registration identifier; Final submit action

**Outputs:** Unique application or registration number; Completed registration record; Confirmation display; Confirmation notification

**Business rules:**
- Unique application number generated for each completed registration
- Registration complete only after successful payment where mandatory
- All mandatory sections must be complete before submission
- Complete application stored including examination, preferences, documents, payment
- Optional verification gate may change post-submit status (F05-014)

**Validations:**
- Profile section complete for registration category
- Competent authority document present for other-organisation path
- Examination selected
- Both centre preferences captured
- Fee compliance verified when payment mandatory
- Draft not already finalised
- Application number uniqueness enforced

**Workflow / states:** DRAFT_READY → REVIEW_SUBMITTED → VALIDATING → CONFIRMED (application number issued) or VALIDATION_FAILED; CONFIRMED → PENDING_VERIFICATION if optional approval enabled

**Dependencies:**
- F05-004 or F05-005 — Profile features
- F05-006 — Competent authority document for other-organisation
- F05-007 — Examination selection
- F05-008 — Centre preferences
- F05-009 — Fee determination
- F05-010 or payment-skipped free path — Fee compliance
- F05-011 — No unresolved failed payment
- Module 07 — Examination Lifecycle Event Subscription

**Risks:** Concurrent submit attempts could race without idempotency; Numbering scheme exhaustion under high volume

---

#### F05-033 — Candidate Registration Status Self-Service Visibility

**One-liner / description:** Allows logged-in candidates to view list and detail of their examination registrations including application number, registration status, examination details, centre preferences, payment status, document status, and…

**Business objective:** Give candidates continuous visibility into registration progress and outcomes from login without administrator intervention for standard status queries.

**Actors:** Candidate

**User journey (1 steps):**
1. Authenticated candidate navigates to My Registrations from portal. 2. System lists candidate registrations with application number, examination name, status chip, and date. 3. Candidate filters or searches own registrations if list large. 4. Candidate selects one registration to view detail. 5. Detail view shows examination, preferences, fee and payment status, document status, and overall registration status. 6. For incomplete drafts, candidate sees resume action to continue registration. 7. For payment-pending registrations, candidate sees retry payment action linking to F05-011. 8. For confirmed registrations, candidate sees read-only summary. 9. Candidate returns to list or portal home.

**Functional capabilities:**
- My Registrations list for authenticated candidate
- Registration status chips for submitted, pending payment, pending verification, confirmed
- Registration detail read-only view
- Examination and centre preference display on detail
- Payment status and receipt link on detail
- Document upload status on detail for other-organisation
- Resume incomplete draft registration action
- Retry pending payment shortcut
- Search or filter own registrations

**Inputs:** Authenticated candidate identifier; Registration search or filter criteria

**Outputs:** Registration list; Registration detail view; Resume and retry payment deep links

**Business rules:**
- Candidates view only own registrations
- Registration status reflects payment, verification, and submission state
- Incomplete drafts accessible for resume until expiry policy if any
- Final centre allocation and hall ticket not shown here; handled in Module 06

**Validations:**
- List and detail scoped to authenticated candidate identity
- Resume action only for incomplete owned drafts
- Retry payment only when fee pending and not fee-compliant

**Workflow / states:** LIST_VIEW → DETAIL_VIEW → RESUME_DRAFT or RETRY_PAYMENT or READ_ONLY_CONFIRMED

**Dependencies:**
- F05-001 — Candidate OTP Login
- F05-012 — Registration Confirmation
- F05-011 — Failed Payment Handling for retry links

**Risks:** Stale status if asynchronous payment callback delayed

---

#### F05-034 — Optional Registration Application Verification and Administrator Review Gate

**One-liner / description:** Supports optional post-submission registration verification where examination administrators review candidate applications including KGID snapshot, manual details, and competent authority document before approving or…

**Business objective:** Provide controlled administrator verification gate for registrations requiring manual approval without standalone workflow engine module.

**Actors:** Candidate; Examination Administrator

**User journey (1 steps):**
1. Candidate completes registration submission (F05-012). 2. If verification enabled, registration status set to pending verification. 3. Candidate sees pending verification status in self-service view. 4. Administrator opens registration verification queue. 5. Administrator reviews application summary, profile data, KGID snapshot or manual details, competent authority document, and payment status. 6. Administrator approves or rejects with reason. 7. On approval, registration status transitions to verified or confirmed eligible for scheduling. 8. On rejection, candidate notified with reason and guidance. 9. Candidate views updated status in portal.

**Functional capabilities:**
- Post-submit pending verification status assignment when enabled
- Administrator registration verification queue list
- Administrator application detail review screen
- Competent authority document review in verification context
- Approve registration action with audit
- Reject registration action with mandatory reason
- Candidate pending and outcome status visibility
- Verification outcome notification trigger

**Inputs:** Submitted registration; Administrator approve or reject action; Rejection reason text

**Outputs:** Updated registration verification status; Verification audit record; Candidate notification

**Business rules:**
- Verification optional and configurable per examination or globally
- Rejected registrations not eligible for Module 06 scheduling until remediated per policy
- Administrator actions audited
- Competent authority document must be reviewable in verification context

**Validations:**
- Approve or reject only by authorised examination administrator
- Rejection reason required on reject
- Verification actions only on pending verification registrations
- Candidate cannot self-approve

**Workflow / states:** CONFIRMED → PENDING_VERIFICATION → APPROVED or REJECTED; REJECTED → candidate notified; APPROVED → eligible for scheduling handoff to Module 06

**Dependencies:**
- F05-012 — Registration Confirmation
- F05-006 — Competent authority document
- Module 01 — Examination Administrator Role
- Module 06 — Scheduling eligibility consumes verification outcome

**Risks:** Verification backlog delays scheduling; Inconsistent rejection reasons without structured codes

**Notes:** Embedded optional approval per module notes; enable when client requires application verification before scheduling.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 05 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 05 Candidate Registration** (14 features).
> Features: F05-021 Candidate OTP Login and Portal Session Security; F05-022 Registration Category Type Selection; F05-023 Government Employee KGID Lookup and Detail Retrieval; F05-024 Government Employee Detail Confirmation and Supplementary Capture; F05-025 Other Organisation Manual Candidate and Employment Detail Capture; F05-026 Competent Authority Document Template Download and Digitally Signed Upload; F05-027 Open Examination Selection for Registration; F05-028 Examination Centre First and Second Preference Selection; F05-029 Examination Attempt History and Category Fee Applicability Determination; F05-030 Registration Fee Payment Initiation and Success Completion; F05-031 Failed Payment Handling and Registration Recovery; F05-032 Registration Confirmation and Unique Application Number Generation; F05-033 Candidate Registration Status Self-Service Visibility; F05-034 Optional Registration Application Verification and Administrator Review Gate.
> Purpose: Candidate OTP portal access; government and other-organisation registration paths; centre preferences; fee determination and payment; confirmation; optional admin verification.
> Draw: End-to-end registration journey swimlane (Govt vs Other Org); OTP login sequence + lockout state machine; Fee determination decision tree (category × attempt); Payment success/fail recovery flowchart; ERD for `candidate`, `otp_security_parameter`, `otp_challenge`, `candidate_portal_session`, `document_template`, `registration`.
