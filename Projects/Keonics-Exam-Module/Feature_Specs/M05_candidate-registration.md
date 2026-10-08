# Module 05: Candidate Registration

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 14 (F05-021 … F05-034)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 05 Candidate Registration

1,466.5 hours · 253 tasks · Business

End-to-end candidate portal access and examination registration for government and non-government employee categories.

### F05-021 Candidate OTP Login and Portal Session Security

93.7 hours · Go-live · 21 tasks

##### Description

Provides mobile-number-based OTP authentication for candidates accessing the examination registration portal, including OTP generation, delivery handoff, verification, resend controls, expiry enforcement, failed-attempt tracking, retry limits, and post-login session timeout handling.

##### Business objective

Ensure only candidates with access to the registered mobile number can enter the portal while enforcing enterprise-grade OTP and session security controls mandated for government examination registration.

##### Actors

- Candidate

##### User journey

1. Candidate opens the examination candidate portal landing page. 2. Candidate enters registered mobile number on the login screen. 3. System validates mobile number format and eligibility for portal access. 4. Candidate submits mobile number to request OTP. 5. System generates time-bound OTP and dispatches via notification channel (Module 07). 6. Candidate receives OTP on mobile device. 7. Candidate enters OTP on verification screen. 8. On successful verification, system creates authenticated candidate session and redirects to portal home or in-progress registration. 9. If OTP is incorrect, system increments failed-attempt counter and displays remaining attempts. 10. If retry limit exceeded, system blocks further attempts for configured cooldown period. 11. Candidate may request OTP resend subject to resend interval and maximum resend count. 12. If OTP expires before entry, candidate must request new OTP. 13. During active session, idle timeout locks session and requires re-authentication.

##### Functional capabilities

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

##### Inputs

- Mobile number
- OTP code
- Resend OTP request
- Session idle activity signals

##### Outputs

- Authenticated candidate session token
- OTP delivery status
- Failed-attempt and block status messages
- Security audit events

##### Business rules

- Candidate login shall occur exclusively through OTP; password login is out of scope for candidates
- OTP shall expire after configured duration
- Failed OTP attempts shall be tracked and limited
- OTP resend shall be rate-limited
- Active candidate sessions shall timeout after configured idle period
- Concurrent session policy shall align with Module 01 session controls

##### Validations

- Mobile number required and must match approved national mobile format pattern
- Mobile number must correspond to a candidate-permitted portal identity
- OTP must be numeric and match length configured for the portal
- Expired OTP rejected with explicit expiry message
- Incorrect OTP rejected and failed-attempt counter incremented
- Resend blocked until minimum interval elapsed
- Verification blocked when retry limit or resend limit exceeded

##### Calculations

- OTP expiry timestamp from generation time plus configured TTL
- Remaining OTP retry attempts = configured limit minus failed attempts
- Remaining resend attempts = configured resend limit minus resends used
- Session idle expiry from last activity timestamp plus timeout duration

##### Workflow

UNAUTHENTICATED → MOBILE_ENTERED → OTP_REQUESTED → OTP_PENDING → OTP_VERIFIED → SESSION_ACTIVE → SESSION_IDLE_WARNING (optional) → SESSION_EXPIRED → UNAUTHENTICATED; OTP_PENDING → OTP_FAILED (increment attempts) → OTP_BLOCKED when limit exceeded; OTP_PENDING → OTP_EXPIRED → OTP_REQUESTED on resend

##### Notifications

- OTP SMS/delivery via Module 07 Notification Service

##### Security

- OTP values stored hashed or single-use with short TTL
- Failed-attempt and resend counters protected against bypass
- Session token bound to candidate identity and timeout policy
- Login security events available to Module 01 audit register

##### Integrations

- Module 07 Notification Service for OTP dispatch
- Module 01 Candidate Role and session/concurrent-session policy hooks

##### Dependencies

- Module 01 — Candidate Role and Portal Permission Catalogue
- Module 01 — Session Timeout Idle Lock and Concurrent Session Controls
- Module 01 — User Access Audit Register and Security Event Trace
- Module 07 — Multi-Channel Notification Dispatch Engine

##### Assumptions

- Candidate mobile numbers are pre-validated or captured during first registration journey in later features
- OTP channel provider configuration is managed in Module 07
- Session timeout duration aligns with Module 01 global policy

##### Risks

- SMS delivery delays may cause OTP expiry before candidate entry
- Shared mobile devices may expose OTP to unauthorised viewers
- Brute-force OTP guessing if retry limits set too high

##### Non-functional requirements

- OTP generation and verification response within acceptable portal latency
- Security controls configurable without code deployment
- Login flow usable on mobile browsers used by candidates

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate portal login landing with mobile number entry | Easy | 14 |
| UI | OTP entry screen with expiry countdown and attempt remaining indicator | Medium | 16 |
| UI | OTP resend action with cooldown timer and max-resend messaging | Simple | 5 |
| UI | Retry-limit and account-blocked error state screen | Simple | 5 |
| UI | Session idle timeout warning and re-login redirect screen | Simple | 5 |
| API | Validate mobile number format and portal login eligibility | Medium | 6 |
| API | Generate OTP with expiry and persist hashed OTP challenge | Complex | 8 |
| API | Verify OTP with attempt increment and lockout enforcement | Complex | 8 |
| API | Resend OTP with interval and maximum resend validation | Medium | 6 |
| API | Create candidate authenticated session with idle timeout binding | Medium | 6 |
| API | Terminate or refresh session on idle timeout breach | Easy | 4 |
| Database | OTP challenge store with expiry and attempt counters | Medium | 0.3 |
| Database | Candidate login attempt and resend audit history | Easy | 0.25 |
| Integration | OTP dispatch request to Module 07 notification engine | Simple | 4 |
| Integration | Session policy alignment hook with Module 01 concurrent session controls | Simple | 4 |
| Testing | Happy-path mobile login through OTP verification to active session | Medium | 0.3 |
| Testing | Incorrect OTP, expiry, and retry-limit rejection cases | Complex | 0.5 |
| Testing | Resend interval, max resend, and idle session timeout edge cases | Complex | 0.5 |
| Testing | Security audit event emission for failed and successful login | Medium | 0.3 |
| Documentation | Candidate portal login and OTP troubleshooting user guide | Easy | 0.25 |
| Documentation | Administrator OTP policy configuration and security runbook | Medium | 0.3 |

### F05-022 Registration Category Type Selection

63.7 hours · Go-live · 15 tasks

##### Description

Allows an authenticated candidate to choose between Registration Type 1 (Government Department Employee) and Registration Type 2 (PSU/Board/Corporation/Society/Other eligible organisation) at the start of a new examination registration, persisting the selection for downstream profile, document, and fee paths.

##### Business objective

Route each candidate into the correct registration path with distinct data capture, document, and fee rules before any category-specific steps begin.

##### Actors

- Candidate

##### User journey

1. Authenticated candidate initiates new examination registration from portal home. 2. System presents registration category type selection screen with two paths: Government Department Employee and Other Organisation Employee. 3. Candidate reads category descriptions and eligibility guidance. 4. Candidate selects one registration type. 5. System validates selection is allowed for candidate context. 6. System persists registration type on draft registration record. 7. System routes candidate to Government KGID path (F05-003) or Other Organisation manual path (F05-005). 8. If candidate navigates back, system warns that changing type may reset captured data.

##### Functional capabilities

- Registration type selection screen with two distinct paths
- Eligibility guidance text per registration category
- Persist selected registration type on draft registration
- Route to government or other-organisation downstream features
- Back-navigation guard when type change would invalidate captured data
- Display previously selected type when resuming incomplete registration

##### Inputs

- Selected registration type
- Draft registration identifier

##### Outputs

- Persisted registration category type
- Route decision to government or other-organisation flow

##### Business rules

- Exactly one registration type must be selected before profile capture begins
- Registration type determines mandatory KGID path versus manual detail path
- Registration type determines fee rules and competent authority document requirement
- Changing registration type after downstream data capture may require draft reset per policy

##### Validations

- Registration type selection required before proceeding
- Selected type must be one of configured enum values
- Draft registration must belong to authenticated candidate
- Type change blocked or confirmed when dependent data already captured

##### Workflow

DRAFT_CREATED → TYPE_UNSELECTED → TYPE_SELECTED_GOV or TYPE_SELECTED_OTHER → routed to category path; TYPE_SELECTED_* → TYPE_CHANGE_PENDING (if back) → TYPE_UNSELECTED or retained with confirmation

##### Security

- Only authenticated candidate may set type on own draft registration

##### Dependencies

- F05-001 — Candidate OTP Login and Portal Session Security
- Module 04 — Examination Master Configuration for open registration context

##### Assumptions

- Candidate self-declares category; cross-check for other-org occurs via competent authority document

##### Risks

- Candidate selects wrong category requiring restart or administrator intervention

##### Non-functional requirements

- Type selection screen readable on mobile browsers
- Category labels configurable by administrator

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration type selection screen with government and other-organisation cards | Medium | 16 |
| UI | Category eligibility guidance panel per registration type | Simple | 5 |
| UI | Registration type change confirmation dialog when downstream data exists | Simple | 5 |
| UI | Resume incomplete registration type display on draft continuation | Easy | 14 |
| API | Create draft registration shell for authenticated candidate | Easy | 4 |
| API | Persist registration category type on draft registration | Medium | 6 |
| API | Validate type change impact and reset dependent draft sections when confirmed | Complex | 8 |
| API | Fetch draft registration with current type for resume flow | Easy | 4 |
| Database | Draft registration header with category type and workflow state | Easy | 0.25 |
| Testing | Happy-path type selection routing to government path | Easy | 0.25 |
| Testing | Happy-path type selection routing to other-organisation path | Easy | 0.25 |
| Testing | Type change with existing captured data confirmation and reset behaviour | Medium | 0.3 |
| Testing | Unauthenticated or cross-candidate draft access rejection | Medium | 0.3 |
| Documentation | Candidate registration category selection guidance | Easy | 0.25 |
| Documentation | Technical notes on draft registration type state transitions | Simple | 0.1 |

### F05-023 Government Employee KGID Lookup and Detail Retrieval

103.45 hours · Go-live · 19 tasks

##### Description

Captures mandatory KGID number for government department employee registrations, invokes KGID integration to retrieve available employee information, and displays retrieved details for candidate review before confirmation.

##### Business objective

Automate government employee identity and employment detail retrieval through authoritative KGID integration while ensuring candidates review system-fetched data before proceeding.

##### Actors

- Candidate

##### User journey

1. Candidate on government registration path reaches KGID entry step. 2. Candidate enters KGID number. 3. System validates KGID format. 4. Candidate submits KGID for lookup. 5. System calls KGID integration hub with KGID number. 6. On success, system displays retrieved fields: employee name, KGID number, department, and other available employment details. 7. On integration failure or not-found, system shows error with retry option. 8. On partial data, system displays available fields and flags missing attributes. 9. Candidate proceeds to confirmation step (F05-004) with retrieved payload attached to draft.

##### Functional capabilities

- KGID number entry form for government path
- KGID format validation before lookup
- KGID integration lookup invocation
- Retrieved employee detail read-only display panel
- Integration error and not-found handling with retry
- Partial retrieval display with missing-field indicators
- Attach retrieved KGID payload to draft registration
- Lookup attempt logging for audit

##### Inputs

- KGID number
- Draft registration identifier

##### Outputs

- Retrieved employee detail snapshot
- KGID lookup status
- Integration error messages

##### Business rules

- KGID number is mandatory for government department employee registrations
- Retrieved KGID details must be displayed before candidate may confirm
- KGID lookup result is subject to data availability from external KGID system
- Duplicate KGID use across active registrations may be restricted per department policy

##### Validations

- KGID number required on government path
- KGID must match configured format pattern
- Lookup blocked when integration unavailable if policy requires live verification
- Retrieved KGID must match entered KGID
- Draft registration must be government category type

##### Workflow

KGID_PENDING → KGID_SUBMITTED → KGID_LOOKUP_IN_PROGRESS → KGID_RETRIEVED or KGID_NOT_FOUND or KGID_INTEGRATION_ERROR → KGID_RETRIEVED proceeds to confirmation

##### Security

- KGID lookup requests scoped to authenticated candidate draft
- Integration credentials managed in Module 02 only

##### Integrations

- Module 02 — KGID Government Employee Lookup Integration

##### Dependencies

- F05-002 — Registration Category Type Selection
- Module 02 — KGID Government Employee Lookup Integration
- Module 02 — Integration Retry Logging and Error Observability

##### Assumptions

- KGID API returns subset of fields listed in FRS; UI adapts to available attributes
- KGID integration retry handled by Module 02 hub

##### Risks

- KGID service downtime blocks government registration path
- Stale KGID data if source system not updated

##### Non-functional requirements

- Lookup feedback with loading state during integration call
- Graceful degradation messaging on timeout

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | KGID number entry form with format hint and submit action | Medium | 16 |
| UI | KGID lookup in-progress loading state | Simple | 5 |
| UI | Retrieved government employee detail read-only review panel | Medium | 16 |
| UI | KGID not-found error state with retry action | Simple | 5 |
| UI | KGID integration failure error state with support guidance | Simple | 5 |
| UI | Partial KGID retrieval display with missing-field indicators | Easy | 14 |
| API | Validate KGID format and government path eligibility | Medium | 6 |
| API | Invoke KGID lookup and map response to registration draft snapshot | Complex | 8 |
| API | Persist KGID lookup result and lookup timestamp on draft | Medium | 6 |
| API | Record KGID lookup attempt outcome for audit trace | Easy | 4 |
| Database | Government employee KGID lookup snapshot on draft registration | Medium | 0.3 |
| Database | KGID lookup attempt log with status and error code | Easy | 0.25 |
| Integration | KGID employee lookup call through Module 02 integration hub | Medium | 16 |
| Testing | Happy-path KGID lookup with full field display | Medium | 0.3 |
| Testing | Invalid KGID format and not-found rejection cases | Medium | 0.3 |
| Testing | Integration timeout and retry error presentation cases | Complex | 0.5 |
| Testing | Non-government draft blocked from KGID lookup | Easy | 0.25 |
| Documentation | Candidate KGID entry and lookup troubleshooting guide | Easy | 0.25 |
| Documentation | Technical KGID mapping and error-code handling notes | Medium | 0.3 |

### F05-024 Government Employee Detail Confirmation and Supplementary Capture

84 hours · Go-live · 16 tasks

##### Description

Enables government department employee candidates to confirm retrieved KGID details as correct and capture additional registration fields such as mobile number and other required information before saving validated candidate profile to the draft registration.

##### Business objective

Ensure government candidates explicitly attest to KGID-retrieved identity data and supply any registration fields not available from KGID before examination selection.

##### Actors

- Candidate

##### User journey

1. Candidate views retrieved KGID details from prior step. 2. Candidate confirms details are correct via explicit confirmation control. 3. If details incorrect, candidate returns to KGID re-entry or support guidance. 4. Upon confirmation, system unlocks supplementary detail form. 5. Candidate enters mobile number and other required registration fields. 6. System validates all supplementary fields. 7. Candidate submits profile section. 8. System saves validated government employee profile to draft registration. 9. System advances candidate to examination selection (F05-007).

##### Functional capabilities

- KGID retrieved detail confirmation checkbox or attestation control
- Incorrect-detail escalation guidance and return-to-KGID navigation
- Supplementary registration field form post-confirmation
- Mobile number capture and validation on government path
- Configurable additional field capture per approved requirements
- Profile save with validation summary errors
- Mark government profile section complete on draft

##### Inputs

- KGID confirmation attestation
- Mobile number
- Additional configurable registration fields

##### Outputs

- Validated government employee profile on draft
- Profile section completion status

##### Business rules

- Candidate must confirm KGID retrieved details before supplementary capture
- Mobile number required for government registrations as applicable
- Confirmed KGID snapshot retained even if supplementary fields edited later before submission
- Profile must pass validation before examination selection unlocked

##### Validations

- KGID confirmation attestation required
- Mobile number required and valid format
- Mobile number uniqueness policy per registration rules if enforced
- Configurable additional fields requiredness enforced per field definition
- Cannot confirm without successful prior KGID retrieval

##### Workflow

KGID_RETRIEVED → AWAITING_CONFIRMATION → CONFIRMED → SUPPLEMENTARY_CAPTURE → PROFILE_VALIDATED → PROFILE_COMPLETE; AWAITING_CONFIRMATION → REJECTED returns to KGID step

##### Security

- Profile edits limited to authenticated owner draft

##### Dependencies

- F05-003 — Government Employee KGID Lookup and Detail Retrieval
- Module 04 — Configurable registration field definitions if centrally managed

##### Assumptions

- Exact supplementary field list finalised at requirements sign-off

##### Risks

- Candidate confirms incorrect KGID data without noticing discrepancies

##### Non-functional requirements

- Form supports mobile data entry
- Field-level inline validation messages

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | KGID retrieved detail confirmation attestation screen | Medium | 16 |
| UI | Incorrect KGID detail guidance with return-to-lookup navigation | Simple | 5 |
| UI | Government supplementary registration detail form | Complex | 18 |
| UI | Profile validation error summary panel | Simple | 5 |
| UI | Government profile section completion status indicator on registration stepper | Easy | 14 |
| API | Record KGID detail confirmation attestation with timestamp | Medium | 6 |
| API | Validate and save government supplementary profile fields | Complex | 8 |
| API | Enforce profile section completion gate before examination selection | Medium | 6 |
| API | Fetch government profile section for draft resume | Easy | 4 |
| Database | Government employee profile extension fields on draft registration | Medium | 0.3 |
| Database | KGID confirmation attestation audit record | Easy | 0.25 |
| Testing | Happy-path confirmation and supplementary profile save | Medium | 0.3 |
| Testing | Missing attestation and invalid mobile rejection cases | Medium | 0.3 |
| Testing | Attempt to skip confirmation or save without KGID retrieval blocked | Complex | 0.5 |
| Documentation | Candidate government profile confirmation instructions | Easy | 0.25 |
| Documentation | Configurable supplementary field administration notes | Simple | 0.1 |

### F05-025 Other Organisation Manual Candidate and Employment Detail Capture

121.15 hours · Go-live · 18 tasks

##### Description

Captures manual candidate and employment details for PSU, Board, Corporation, Society, and other eligible organisation employees including organisation category selection, candidate name, mobile number, employee ID, organisation or department, and other configurable fields.

##### Business objective

Collect complete identity and employment information for non-government candidates who cannot use KGID retrieval, enabling fee, document, and registration processing.

##### Actors

- Candidate

##### User journey

1. Candidate on other-organisation path reaches manual detail capture step. 2. Candidate selects organisation sub-category: PSU, Board, Corporation, Society, or Other eligible organisation. 3. Candidate enters candidate name. 4. Candidate enters mobile number. 5. Candidate enters employee ID. 6. Candidate enters organisation or department name. 7. Candidate completes other configurable required fields. 8. System validates all entries. 9. Candidate submits manual profile section. 10. System saves validated profile to draft registration. 11. System routes candidate to competent authority document steps (F05-006).

##### Functional capabilities

- Organisation sub-category selection control
- Manual candidate name capture
- Mobile number capture
- Employee ID capture
- Organisation or department name capture
- Configurable additional field rendering and validation
- Manual profile save to draft registration
- Profile section completion marker for other-organisation path

##### Inputs

- Organisation sub-category
- Candidate name
- Mobile number
- Employee ID
- Organisation or department
- Configurable additional fields

##### Outputs

- Validated other-organisation employee profile on draft
- Organisation sub-category persisted

##### Business rules

- Other-organisation path requires full manual detail capture
- Examination registration fee is mandatory for this category path
- Competent authority digitally signed document required before registration completion
- Field configurability subject to final approved requirements

##### Validations

- Organisation sub-category required
- Candidate name required with minimum length
- Mobile number required and valid format
- Employee ID required per configuration
- Organisation or department name required
- Configurable fields enforced for requiredness and format
- Draft must be other-organisation registration type

##### Workflow

MANUAL_PROFILE_PENDING → MANUAL_PROFILE_IN_PROGRESS → MANUAL_PROFILE_VALIDATED → MANUAL_PROFILE_COMPLETE

##### Security

- Profile data editable only by owning candidate on draft

##### Dependencies

- F05-002 — Registration Category Type Selection
- F05-006 — Competent Authority Document Template Download and Digitally Signed Upload

##### Assumptions

- Final field list and configurability confirmed at requirements freeze

##### Risks

- Manual entry errors without authoritative identity source
- Fraudulent organisation claims pending document verification

##### Non-functional requirements

- Form usable on mobile devices
- Configurable fields loaded without redeployment where supported

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Other-organisation sub-category selection control | Medium | 16 |
| UI | Manual candidate identity detail form | Complex | 18 |
| UI | Manual employment and organisation detail form | Complex | 18 |
| UI | Configurable dynamic field renderer for additional required attributes | Complex | 18 |
| UI | Manual profile validation error summary | Simple | 5 |
| UI | Other-organisation profile step completion indicator on registration stepper | Easy | 14 |
| API | Validate organisation sub-category against allowed enumeration | Easy | 4 |
| API | Validate and save manual candidate identity fields | Complex | 8 |
| API | Validate and save employment and organisation fields | Complex | 8 |
| API | Load configurable field definitions for other-organisation path | Medium | 6 |
| API | Mark manual profile section complete on draft registration | Easy | 4 |
| Database | Other-organisation candidate profile entity on draft registration | Medium | 0.3 |
| Database | Organisation sub-category and employee identifier indexes for lookup | Easy | 0.25 |
| Testing | Happy-path manual profile capture for each sub-category | Medium | 0.3 |
| Testing | Required field and format validation rejection cases | Complex | 0.5 |
| Testing | Government draft blocked from manual profile save | Easy | 0.25 |
| Documentation | Candidate manual detail entry guide for other-organisation employees | Easy | 0.25 |
| Documentation | Administrator configurable field setup notes | Medium | 0.3 |

### F05-026 Competent Authority Document Template Download and Digitally Signed Upload

116.7 hours · Go-live · 19 tasks

##### Description

Provides prescribed competent authority document template download, digitally signed document upload during other-organisation registration, file validation, registration association, and administrator review visibility linkage.

##### Business objective

Obtain legally attested employment confirmation from competent authority for non-government candidates and make uploaded evidence available for administrator verification.

##### Actors

- Candidate
- Examination Administrator

##### User journey

1. Other-organisation candidate reaches competent authority document step. 2. Candidate views document requirement instructions. 3. Candidate downloads prescribed competent authority document template. 4. Candidate completes template offline and obtains competent authority digital signature. 5. Candidate returns to portal upload screen. 6. Candidate selects digitally signed document file. 7. System validates file type, size, and digital signature presence per policy. 8. On success, system stores document linked to draft registration. 9. Candidate sees upload success with file name and timestamp. 10. On validation failure, candidate sees specific error and may re-upload. 11. Uploaded document associated for administrator review on registration record. 12. Candidate proceeds to examination selection once document requirement satisfied.

##### Functional capabilities

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

##### Inputs

- Template download request
- Digitally signed document file

##### Outputs

- Stored competent authority document
- Upload validation result
- Document metadata for administrator review

##### Business rules

- Competent authority document mandatory for other-organisation registrations
- Document must be digitally signed by competent authority
- Template format prescribed by department and downloadable from portal
- Uploaded document associated with candidate registration for verification
- Document replace allowed until registration finalised

##### Validations

- Upload required before registration completion on other-organisation path
- File extension must match allowed signed document types
- File size within configured maximum
- Digital signature validation per approved technical policy
- Only one active competent authority document per draft unless replace flow used
- Upload blocked for government registration path

##### Workflow

DOCUMENT_PENDING → TEMPLATE_DOWNLOADED → UPLOAD_SELECTED → UPLOAD_VALIDATING → DOCUMENT_ACCEPTED or DOCUMENT_REJECTED → DOCUMENT_ACCEPTED enables next step; DOCUMENT_ACCEPTED → DOCUMENT_REPLACED on re-upload

##### Search requirements

- Administrator registration views must locate associated competent authority document by registration identifier

##### Documents

- Prescribed competent authority confirmation template
- Candidate-uploaded digitally signed competent authority document

##### Security

- Document access restricted to candidate owner and authorised administrators
- Stored document integrity checksum

##### Integrations

- Digital signature validation service or library per approved client infrastructure

##### Dependencies

- F05-005 — Other Organisation Manual Candidate and Employment Detail Capture
- Module 01 — Examination Administrator Role and Organisation-Wide Permissions
- F05-014 — Optional Registration Application Verification and Administrator Review Gate

##### Assumptions

- Digital signature validation mechanism finalised with client PKI policy
- Template file hosted and versioned by administrator

##### Risks

- Invalid or forged signatures if validation weak
- Large file uploads on slow mobile networks

##### Non-functional requirements

- Upload progress indicator
- Template download available without authentication loss mid-flow

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Competent authority document requirement instruction screen | Easy | 14 |
| UI | Prescribed template download button with version label | Simple | 5 |
| UI | Digitally signed document file upload form with drag-and-drop | Medium | 16 |
| UI | Upload validation error detail panel | Simple | 5 |
| UI | Upload success summary with file name and replace action | Easy | 14 |
| UI | Administrator registration document preview link in review context | Medium | 16 |
| API | Serve competent authority template file for download | Easy | 4 |
| API | Accept document upload with type and size validation | Complex | 8 |
| API | Verify digital signature on uploaded competent authority document | Very high | 12 |
| API | Persist document blob metadata linked to draft registration | Complex | 8 |
| API | Replace existing competent authority document on draft | Medium | 6 |
| API | Expose document metadata for administrator registration review | Medium | 6 |
| Database | Registration document metadata with signature validation outcome | Medium | 0.3 |
| Database | Document blob storage reference and checksum | Complex | 0.5 |
| Testing | Happy-path template download and valid signed upload | Medium | 0.3 |
| Testing | Oversized, wrong type, and unsigned document rejection cases | Complex | 0.5 |
| Testing | Document replace and administrator metadata visibility cases | Medium | 0.3 |
| Documentation | Candidate competent authority document preparation and upload guide | Complex | 0.5 |
| Documentation | Administrator template version and signature policy runbook | Medium | 0.3 |

### F05-027 Open Examination Selection for Registration

81.7 hours · Go-live · 15 tasks

##### Description

Displays examinations currently open for candidate registration, allows candidate to select target examination, view applicable examination details, and bind examination choice to the in-progress registration draft.

##### Business objective

Ensure candidates register only for examinations accepting registrations and understand examination parameters before centre preference and fee steps.

##### Actors

- Candidate

##### User journey

1. Candidate completes category-specific profile and document prerequisites. 2. Candidate reaches examination selection step. 3. System lists examinations with registration currently open. 4. Candidate browses examination name, schedule summary, and instructions excerpt. 5. Candidate selects one examination. 6. System displays full applicable examination details for selected item. 7. Candidate confirms examination selection. 8. System binds examination to draft registration. 9. System advances to centre preference selection (F05-008). 10. If no examinations open, candidate sees empty state with guidance.

##### Functional capabilities

- Open-for-registration examination list for candidates
- Examination summary card with key details
- Examination detail view for selected examination
- Single examination selection per registration draft
- Bind selected examination to draft registration
- Empty state when no examinations open
- Change examination selection before final submission if policy allows

##### Inputs

- Selected examination identifier
- Draft registration identifier

##### Outputs

- Examination bound to draft registration
- Examination detail display

##### Business rules

- Only examinations marked open for registration appear
- One examination selected per registration instance
- Examination selection required before centre preferences
- Examination eligibility may consider candidate category from Module 04 configuration

##### Validations

- Selected examination must be in open-for-registration state
- Selected examination must be eligible for candidate category
- Profile and document prerequisites must be complete before selection saved
- Draft must belong to authenticated candidate

##### Workflow

EXAM_UNSELECTED → EXAM_LIST_VIEWED → EXAM_SELECTED → EXAM_CONFIRMED → EXAM_BOUND; EXAM_CONFIRMED → EXAM_CHANGE_PENDING if change allowed → EXAM_SELECTED

##### Search requirements

- Filter open examinations by registration window and candidate category eligibility

##### Security

- Examination list respects candidate portal visibility rules

##### Dependencies

- Module 04 — Examination Master Configuration
- F05-004 or F05-005 — Profile completion features
- F05-006 — Competent authority document for other-organisation path

##### Assumptions

- Examination open/close windows maintained in Module 04

##### Risks

- Candidate selects wrong examination requiring draft amendment

##### Non-functional requirements

- Examination list performant for concurrent registration period

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Open examination list with registration status chips | Medium | 16 |
| UI | Examination summary card with schedule and instruction excerpt | Easy | 14 |
| UI | Selected examination detail panel with confirm action | Medium | 16 |
| UI | No open examinations empty state with guidance message | Simple | 5 |
| UI | Examination change confirmation dialog when preferences already captured | Simple | 5 |
| API | List examinations open for candidate registration with category filter | Medium | 6 |
| API | Fetch examination detail for candidate registration context | Easy | 4 |
| API | Bind selected examination to draft registration with eligibility check | Complex | 8 |
| API | Clear dependent centre preferences when examination changed | Medium | 6 |
| Database | Draft registration examination binding with selection timestamp | Easy | 0.25 |
| Testing | Happy-path examination selection and draft binding | Medium | 0.3 |
| Testing | Closed examination and category-ineligible selection rejection | Medium | 0.3 |
| Testing | Examination change clears downstream preferences validation | Complex | 0.5 |
| Documentation | Candidate examination selection guidance | Easy | 0.25 |
| Documentation | Technical notes on open-registration eligibility rules | Simple | 0.1 |

### F05-028 Examination Centre First and Second Preference Selection

81.4 hours · Go-live · 15 tasks

##### Description

Captures candidate's first and second preferred authorised examination centres from administrator-configured active centre list for use during downstream centre allocation while displaying selection rules and validation feedback.

##### Business objective

Collect candidate centre preferences to inform administrator and system centre allocation per capacity, schedule, and business rules without performing final allocation in this module.

##### Actors

- Candidate

##### User journey

1. Candidate completes examination selection. 2. Candidate reaches centre preference step. 3. System loads list of active authorised examination centres from Module 03. 4. Candidate selects Centre Preference 1 from dropdown or searchable list. 5. Candidate selects Centre Preference 2 from remaining centres. 6. System validates preferences are distinct and centres active. 7. Candidate submits preferences. 8. System persists both preferences on draft registration. 9. System advances to attempt and fee evaluation (F05-009). 10. Candidate may edit preferences until registration finalised.

##### Functional capabilities

- Active authorised centre list for preference selection
- Centre Preference 1 selection control
- Centre Preference 2 selection control
- Distinct preference validation
- Centre search or filter within preference pickers
- Persist both preferences on draft registration
- Display centre name and location summary in picker
- Edit preferences before registration submission

##### Inputs

- Centre Preference 1 identifier
- Centre Preference 2 identifier
- Draft registration identifier

##### Outputs

- Persisted centre preferences on draft
- Preference validation messages

##### Business rules

- Candidates must select exactly two preferred centres
- Preference 1 and Preference 2 must be different centres
- Only active authorised centres available for selection
- Final centre allocation performed in Module 06; preferences are inputs only
- Preferences used during allocation considering capacity and schedule

##### Validations

- Centre Preference 1 required
- Centre Preference 2 required
- Preferences must reference distinct centre identifiers
- Selected centres must be active and authorised
- Examination must be selected before preferences saved

##### Workflow

PREFERENCES_PENDING → PREFERENCE_1_SELECTED → PREFERENCE_2_SELECTED → PREFERENCES_VALIDATED → PREFERENCES_SAVED

##### Search requirements

- Searchable centre list by centre name or district where configured

##### Security

- Centre list exposes only candidate-visible active centres

##### Dependencies

- F05-007 — Open Examination Selection for Registration
- Module 03 — Authorised Examination Centre Register and Search

##### Assumptions

- Centre master maintained in Module 03
- Allocation engine in Module 06 consumes preferences

##### Risks

- Popular centres oversubscribed; candidate may not receive preferred centre

##### Non-functional requirements

- Centre picker performant for large centre catalogues

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre Preference 1 searchable dropdown selector | Medium | 16 |
| UI | Centre Preference 2 searchable dropdown selector excluding Preference 1 | Medium | 16 |
| UI | Centre preference summary review panel before submit | Easy | 14 |
| UI | Duplicate preference validation inline error display | Simple | 5 |
| UI | Inactive centre unavailable messaging in picker | Simple | 5 |
| API | List active authorised centres for examination registration context | Medium | 6 |
| API | Search centres by name or location facet | Medium | 6 |
| API | Validate and save dual centre preferences on draft registration | Complex | 8 |
| API | Fetch saved centre preferences for draft resume | Easy | 4 |
| Database | Draft registration centre preference 1 and preference 2 fields | Easy | 0.25 |
| Testing | Happy-path dual distinct preference save | Medium | 0.3 |
| Testing | Duplicate preference and inactive centre rejection cases | Easy | 0.25 |
| Testing | Preference save blocked without examination selection | Easy | 0.25 |
| Documentation | Candidate centre preference selection instructions | Easy | 0.25 |
| Documentation | Technical notes on preference consumption by allocation module | Simple | 0.1 |

### F05-029 Examination Attempt History and Category Fee Applicability Determination

90.7 hours · Go-live · 17 tasks

##### Description

Evaluates candidate prior examination attempt history against selected examination and category to determine applicable fee: free first attempt for government employees, fee for subsequent government attempts, and mandatory fee for other-organisation candidates per administrator-configured fee rules from Module 04.

##### Business objective

Apply correct category-based and attempt-based fee rules automatically before payment routing so candidates see accurate fee obligation and free-registration eligibility.

##### Actors

- Candidate

##### User journey

1. Candidate completes centre preferences. 2. System evaluates attempt history for candidate against selected examination. 3. System identifies registration category: government or other-organisation. 4. For government employee: system checks if first examination attempt for configured scope. 5. If first attempt, system marks fee as not applicable (free registration). 6. If subsequent attempt, system retrieves configured fee amount from Module 04. 7. For other-organisation: system retrieves mandatory configured fee amount. 8. System displays fee determination summary screen with amount, reason, and attempt count context. 9. Candidate acknowledges fee summary. 10. System routes to payment (F05-010) if fee applicable or directly toward confirmation path if free.

##### Functional capabilities

- Attempt history lookup for candidate and examination
- First-attempt versus subsequent-attempt classification for government employees
- Government first-attempt free registration rule application
- Government subsequent-attempt fee retrieval
- Other-organisation mandatory fee retrieval
- Fee determination summary display with explanatory reason
- Persist fee applicability outcome on draft registration
- Route to payment or skip payment based on determination

##### Inputs

- Candidate identifier
- Selected examination identifier
- Registration category type
- Historical registration and attempt records

##### Outputs

- Fee applicable flag
- Applicable fee amount
- Attempt classification label
- Fee determination audit record

##### Business rules

- Government department employees receive free registration for first examination attempt
- Fee applicable for second and subsequent government employee attempts
- Fee amounts configurable by administrator in Module 04
- Fee mandatory for eligible non-government organisation candidates
- Attempt history maintained to support fee determination
- Registration complete only after successful payment where payment mandatory

##### Validations

- Examination and category must be set before fee evaluation
- Fee configuration must exist when fee applicable
- Attempt history query scoped to authenticated candidate only
- Free path blocked if attempt history indicates subsequent attempt

##### Calculations

- Attempt count for candidate against examination or configured attempt scope
- Fee applicable = false when government and attempt count equals zero per rules
- Fee applicable = true when government subsequent attempt or other-organisation path
- Payable amount = configured fee rule amount when applicable else zero

##### Workflow

FEE_EVAL_PENDING → ATTEMPT_HISTORY_LOADED → FEE_NOT_APPLICABLE (government first) or FEE_APPLICABLE → FEE_DETERMINED → routes to PAYMENT_REQUIRED or PAYMENT_SKIPPED

##### Search requirements

- Attempt history query by candidate, examination, and registration category

##### Security

- Attempt history visible only to owning candidate and authorised administrators

##### Dependencies

- F05-002 — Registration Category Type Selection
- F05-007 — Open Examination Selection for Registration
- Module 04 — Certificate Eligibility and Examination Fee Configuration

##### Assumptions

- Attempt scope definition (per examination vs global) confirmed in Module 04 fee rules
- Prior attempts recorded from completed registrations in this system

##### Risks

- Incorrect attempt count if historical data incomplete
- Fee rule changes mid-registration handled by snapshot at determination time

##### Non-functional requirements

- Fee determination completes within portal step transition latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Fee determination summary screen with amount and attempt context | Medium | 16 |
| UI | Government first-attempt free registration informational panel | Simple | 5 |
| UI | Subsequent-attempt fee applicable notice for government employees | Easy | 14 |
| UI | Other-organisation mandatory fee notice panel | Easy | 14 |
| UI | Missing fee configuration error state for administrator escalation | Simple | 5 |
| API | Query candidate attempt history for selected examination scope | Complex | 8 |
| API | Classify first versus subsequent attempt for government category | Complex | 8 |
| API | Resolve applicable fee rule from Module 04 configuration | Complex | 8 |
| API | Persist fee applicability outcome and calculated amount on draft | Medium | 6 |
| API | Expose fee determination result for payment initiation feature | Easy | 4 |
| Database | Registration fee determination snapshot with attempt count | Medium | 0.3 |
| Database | Candidate examination attempt history index for fee lookup | Complex | 0.5 |
| Testing | Happy-path government first-attempt free determination | Medium | 0.3 |
| Testing | Government subsequent-attempt and other-organisation fee applicable cases | Complex | 0.5 |
| Testing | Missing fee configuration and attempt history edge cases | Medium | 0.3 |
| Documentation | Candidate fee rules explanation by category and attempt | Medium | 0.3 |
| Documentation | Technical attempt-count scope and fee rule resolution notes | Complex | 0.5 |

### F05-030 Registration Fee Payment Initiation and Success Completion

134.8 hours · Go-live · 21 tasks

##### Description

Initiates payment gateway transaction when registration fee is applicable, handles successful payment callback, records transaction and reference numbers, generates payment receipt, and progresses registration toward completion after successful payment confirmation.

##### Business objective

Collect mandatory examination registration fees through integrated payment gateway and mark registration fee-compliant upon successful payment as prerequisite to registration finalisation.

##### Actors

- Candidate

##### User journey

1. Fee determination indicates payment required (F05-009). 2. Candidate views payment summary with examination, fee amount, and candidate details. 3. Candidate initiates payment. 4. System creates payment transaction record and calls payment gateway via Module 02. 5. Candidate redirected to payment gateway hosted page or embedded flow. 6. Candidate completes payment on gateway. 7. System receives success callback with transaction reference. 8. System verifies callback authenticity and amount match. 9. System updates payment status to successful on draft registration. 10. System stores transaction and reference number. 11. Candidate views payment success confirmation. 12. Candidate downloads or views payment receipt. 13. System enables registration finalisation step (F05-012).

##### Functional capabilities

- Payment summary screen before gateway handoff
- Payment initiation with transaction record creation
- Payment gateway redirect or embed handoff
- Successful payment callback verification
- Transaction and reference number persistence
- Payment receipt display and download
- Registration fee-compliant status update on success
- Advance registration workflow after successful payment

##### Inputs

- Draft registration identifier
- Applicable fee amount
- Payment gateway callback payload

##### Outputs

- Payment transaction record
- Transaction reference number
- Payment receipt
- Fee-compliant registration status

##### Business rules

- Payment mandatory where fee determination marks fee applicable
- Registration not complete until successful payment when mandatory
- Successful payment callback must match initiated amount and registration
- Transaction reference stored for audit and receipt
- Free registrations skip this feature entirely

##### Validations

- Payment initiation blocked when fee not applicable
- Payment amount must match determined fee amount
- Callback signature or token verified per gateway policy
- Duplicate success callback idempotent handling
- Draft must be in payment-pending state for initiation

##### Calculations

- Payable amount equals fee determination snapshot amount
- Payment status derived from gateway callback outcome

##### Workflow

PAYMENT_PENDING → PAYMENT_INITIATED → GATEWAY_IN_PROGRESS → PAYMENT_SUCCESS → FEE_COMPLIANT → REGISTRATION_FINALISATION_ENABLED; PAYMENT_INITIATED → PAYMENT_ABANDONED if candidate returns without completion

##### Search requirements

- Candidate payment history by registration identifier

##### Documents

- Payment receipt PDF or printable view

##### Notifications

- Payment confirmation notification via Module 07 upon success

##### Security

- Payment callback verification prevents tampering
- PCI-sensitive data not stored beyond gateway references

##### Integrations

- Module 02 — Payment Gateway Fee Transaction Integration
- Module 07 — Payment confirmation notification dispatch

##### Dependencies

- F05-009 — Examination Attempt History and Category Fee Applicability Determination
- Module 02 — Payment Gateway Fee Transaction Integration
- F05-012 — Registration Confirmation Application Number and Status Visibility

##### Assumptions

- Payment gateway supports redirect and callback pattern configured in Module 02
- Receipt format approved by finance stakeholder

##### Risks

- Callback delay leaves registration in pending payment state
- Amount mismatch between initiation and callback

##### Non-functional requirements

- Payment handoff secure over HTTPS
- Idempotent callback processing for reliability

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration payment summary screen with fee breakdown | Medium | 16 |
| UI | Payment gateway redirect loading and return landing screen | Easy | 14 |
| UI | Payment success confirmation screen with reference number | Medium | 16 |
| UI | Payment receipt view and download screen | Medium | 16 |
| UI | Payment already completed informational read-only state | Simple | 5 |
| API | Initiate payment transaction with amount and registration binding | Complex | 8 |
| API | Process successful payment gateway callback with signature verification | Very high | 12 |
| API | Persist transaction reference and payment success status | Complex | 8 |
| API | Generate payment receipt data for candidate download | Medium | 6 |
| API | Mark registration fee-compliant and unlock finalisation | Medium | 6 |
| API | Fetch payment status for draft registration resume | Easy | 4 |
| Database | Registration payment transaction entity with gateway references | Complex | 0.5 |
| Database | Payment receipt metadata and issuance timestamp | Easy | 0.25 |
| Integration | Payment gateway initiation call via Module 02 hub | Medium | 16 |
| Integration | Payment success notification trigger to Module 07 | Simple | 4 |
| Testing | Happy-path payment initiation through success callback to receipt | Complex | 0.5 |
| Testing | Amount mismatch and invalid callback signature rejection | Very high | 1 |
| Testing | Duplicate success callback idempotent processing | Complex | 0.5 |
| Testing | Free registration path skips payment initiation | Easy | 0.25 |
| Documentation | Candidate payment and receipt download guide | Medium | 0.3 |
| Documentation | Technical payment callback verification and reconciliation notes | Complex | 0.5 |

### F05-031 Failed Payment Handling and Registration Recovery

115.15 hours · Go-live · 20 tasks

##### Description

Handles failed, declined, cancelled, and abandoned payment scenarios during registration including failure reason display, draft preservation in payment-pending state, retry payment initiation, duplicate-transaction safeguards, and clear guidance until successful payment or candidate exits.

##### Business objective

Prevent loss of registration progress on payment failure and give candidates a controlled recovery path to complete mandatory fee payment without duplicate charges or orphaned registrations.

##### Actors

- Candidate

##### User journey

1. Candidate initiates payment from F05-010. 2. Payment gateway returns failure, decline, cancellation, or timeout. 3. System receives failure callback or detects abandoned session. 4. System records failed payment attempt with reason code. 5. Candidate redirected to failed payment screen showing reason and registration summary. 6. Candidate reviews remaining fee amount due unchanged. 7. Candidate chooses retry payment action. 8. System validates no successful payment already recorded. 9. System initiates new payment transaction linked to same draft. 10. On repeated failures, system shows escalating guidance and support contact. 11. Registration remains incomplete and not confirmed until success. 12. Candidate may exit and resume payment later from registration status view (F05-013).

##### Functional capabilities

- Failed payment callback processing
- Abandoned payment session detection
- Failed payment reason display to candidate
- Preserve draft registration in payment-pending state
- Retry payment initiation from failure screen
- Prevent duplicate successful charges for same registration
- Failed attempt counter and audit trail
- Resume failed payment from registration status view
- Block registration finalisation while payment failed or pending

##### Inputs

- Payment failure callback payload
- Abandoned session signal
- Retry payment request

##### Outputs

- Failed payment attempt record
- Payment-pending draft state
- Retry payment transaction
- Candidate failure guidance messages

##### Business rules

- Registration incomplete when mandatory payment fails
- Candidate may retry payment without re-entering prior registration steps
- Each retry creates new gateway transaction unless policy reuses open session
- Successful payment on any attempt completes fee requirement
- Failed attempts logged for administrator reconciliation in Module 12 scope

##### Validations

- Failure callback authenticity verified
- Retry blocked if registration already fee-compliant
- Retry blocked if maximum retry count exceeded when configured
- Draft ownership verified on retry
- Concurrent retry initiation prevented

##### Calculations

- Failed attempt count incremented per distinct failure event
- Outstanding fee amount remains fee determination snapshot until success

##### Workflow

PAYMENT_INITIATED → PAYMENT_FAILED or PAYMENT_CANCELLED or PAYMENT_ABANDONED → PAYMENT_PENDING_RETRY → PAYMENT_INITIATED (retry) → PAYMENT_SUCCESS or PAYMENT_FAILED; PAYMENT_PENDING_RETRY → RESUMED_FROM_STATUS_VIEW

##### Search requirements

- Candidate views failed payment attempts on own registration

##### Notifications

- Optional payment failure alert via Module 07

##### Security

- Failure callbacks verified same as success callbacks
- Retry tokens bound to candidate session

##### Integrations

- Module 02 — Payment Gateway Fee Transaction Integration failure callbacks
- Module 07 — Optional payment failure notification

##### Dependencies

- F05-010 — Registration Fee Payment Initiation and Success Completion
- F05-013 — Candidate Registration Status Self-Service Visibility

##### Assumptions

- Gateway provides distinct failure reason codes mappable to user messages

##### Risks

- Multiple partial gateway sessions causing reconciliation complexity
- Candidate abandons registration indefinitely in payment-pending state

##### Non-functional requirements

- Failure screen displayed within seconds of gateway return
- Retry flow idempotent under double-click

##### Notes

Covers FRS §13 failed payment handling explicitly called out as prior coverage gap.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Payment failed screen with gateway reason and registration summary | Medium | 16 |
| UI | Payment cancelled or abandoned return screen with retry action | Medium | 16 |
| UI | Retry payment confirmation dialog with outstanding amount | Simple | 5 |
| UI | Maximum retry exceeded blocked state with support guidance | Simple | 5 |
| UI | Resume incomplete payment banner on registration status view | Easy | 14 |
| API | Process failed payment gateway callback with reason mapping | Complex | 8 |
| API | Detect and mark abandoned payment sessions after timeout | Complex | 8 |
| API | Initiate payment retry with duplicate-success guard | Complex | 8 |
| API | List failed payment attempts for candidate registration | Medium | 6 |
| API | Enforce registration finalisation block while payment unresolved | Medium | 6 |
| Database | Failed payment attempt log with reason code and timestamp | Medium | 0.3 |
| Database | Draft registration payment-pending state flag | Easy | 0.25 |
| Integration | Failure callback handling through Module 02 payment hub | Medium | 16 |
| Integration | Optional payment failure notification to Module 07 | Simple | 4 |
| Testing | Happy-path failure display and successful retry completion | Complex | 0.5 |
| Testing | Declined, cancelled, timeout, and abandoned session cases | Complex | 0.5 |
| Testing | Retry blocked when already paid and concurrent retry prevention | Complex | 0.5 |
| Testing | Registration finalisation blocked with unresolved failed payment | Medium | 0.3 |
| Documentation | Candidate failed payment recovery instructions | Medium | 0.3 |
| Documentation | Administrator failed transaction review and retry policy runbook | Complex | 0.5 |

### F05-032 Registration Confirmation and Unique Application Number Generation

125.35 hours · Go-live · 20 tasks

##### Description

Finalises eligible draft registrations by validating prerequisites, generating unique registration or application number, persisting complete application including examination, centre preferences, documents, and payment details, and displaying registration confirmation to the candidate.

##### Business objective

Provide candidates with definitive proof of completed examination registration and a unique reference for all downstream scheduling, allocation, and support interactions.

##### Actors

- Candidate

##### User journey

1. Candidate completes all mandatory steps: profile, documents (if applicable), examination, preferences, and payment (if applicable). 2. Candidate reaches registration review and submit step. 3. System displays registration summary for final review. 4. Candidate submits registration. 5. System validates all prerequisites complete and fee-compliant if required. 6. System generates unique application or registration number. 7. System persists complete registration record from draft. 8. System transitions registration status to submitted or confirmed per policy. 9. Candidate views confirmation screen with application number. 10. System triggers registration confirmation notification via Module 07. 11. Candidate may print or save confirmation summary.

##### Functional capabilities

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

##### Inputs

- Draft registration identifier
- Final submit action

##### Outputs

- Unique application or registration number
- Completed registration record
- Confirmation display
- Confirmation notification

##### Business rules

- Unique application number generated for each completed registration
- Registration complete only after successful payment where mandatory
- All mandatory sections must be complete before submission
- Complete application stored including examination, preferences, documents, payment
- Optional verification gate may change post-submit status (F05-014)

##### Validations

- Profile section complete for registration category
- Competent authority document present for other-organisation path
- Examination selected
- Both centre preferences captured
- Fee compliance verified when payment mandatory
- Draft not already finalised
- Application number uniqueness enforced

##### Calculations

- Application number generated per configured numbering scheme
- Registration status derived from submit outcome and optional verification policy

##### Workflow

DRAFT_READY → REVIEW_SUBMITTED → VALIDATING → CONFIRMED (application number issued) or VALIDATION_FAILED; CONFIRMED → PENDING_VERIFICATION if optional approval enabled

##### Documents

- Registration confirmation summary printable view

##### Notifications

- Registration confirmation via Module 07

##### Security

- Submit allowed only by owning authenticated candidate
- Application number generation concurrency-safe

##### Integrations

- Module 07 — Registration confirmation notification

##### Dependencies

- F05-004 or F05-005 — Profile features
- F05-006 — Competent authority document for other-organisation
- F05-007 — Examination selection
- F05-008 — Centre preferences
- F05-009 — Fee determination
- F05-010 or payment-skipped free path — Fee compliance
- F05-011 — No unresolved failed payment
- Module 07 — Examination Lifecycle Event Subscription

##### Assumptions

- Application numbering scheme provided by department
- Verification optional per F05-014

##### Risks

- Concurrent submit attempts could race without idempotency
- Numbering scheme exhaustion under high volume

##### Non-functional requirements

- Confirmation generated within acceptable submit latency
- Application number human-readable for candidate support

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Registration final review summary with all captured sections | Complex | 18 |
| UI | Submit registration confirmation dialog | Simple | 5 |
| UI | Registration confirmation success screen with application number | Medium | 16 |
| UI | Printable registration confirmation summary view | Easy | 14 |
| UI | Prerequisite incomplete validation error panel on submit | Medium | 16 |
| API | Validate all registration prerequisites before finalisation | Very high | 12 |
| API | Generate unique application number with concurrency control | Complex | 8 |
| API | Finalise draft into completed registration record | Very high | 12 |
| API | Persist examination, preferences, document, and payment snapshots on registration | Complex | 8 |
| API | Transition registration status to confirmed or pending verification | Complex | 8 |
| Database | Completed candidate registration entity with application number | Complex | 0.5 |
| Database | Application number uniqueness constraint and sequence | Complex | 0.5 |
| Database | Registration finalisation audit event | Easy | 0.25 |
| Integration | Registration confirmation notification dispatch to Module 07 | Simple | 4 |
| Testing | Happy-path full registration finalisation with application number | Complex | 0.5 |
| Testing | Submit blocked for incomplete profile, document, payment, or preferences | Very high | 1 |
| Testing | Concurrent submit idempotency and duplicate number prevention | Complex | 0.5 |
| Testing | Government free path finalisation without payment | Medium | 0.3 |
| Documentation | Candidate registration confirmation and application number guide | Medium | 0.3 |
| Documentation | Technical application numbering and finalisation state notes | Complex | 0.5 |

### F05-033 Candidate Registration Status Self-Service Visibility

122.1 hours · Go-live · 18 tasks

##### Description

Allows logged-in candidates to view list and detail of their examination registrations including application number, registration status, examination details, centre preferences, payment status, document status, and actions to resume incomplete registrations or retry pending payments.

##### Business objective

Give candidates continuous visibility into registration progress and outcomes from login without administrator intervention for standard status queries.

##### Actors

- Candidate

##### User journey

1. Authenticated candidate navigates to My Registrations from portal. 2. System lists candidate registrations with application number, examination name, status chip, and date. 3. Candidate filters or searches own registrations if list large. 4. Candidate selects one registration to view detail. 5. Detail view shows examination, preferences, fee and payment status, document status, and overall registration status. 6. For incomplete drafts, candidate sees resume action to continue registration. 7. For payment-pending registrations, candidate sees retry payment action linking to F05-011. 8. For confirmed registrations, candidate sees read-only summary. 9. Candidate returns to list or portal home.

##### Functional capabilities

- My Registrations list for authenticated candidate
- Registration status chips for submitted, pending payment, pending verification, confirmed
- Registration detail read-only view
- Examination and centre preference display on detail
- Payment status and receipt link on detail
- Document upload status on detail for other-organisation
- Resume incomplete draft registration action
- Retry pending payment shortcut
- Search or filter own registrations

##### Inputs

- Authenticated candidate identifier
- Registration search or filter criteria

##### Outputs

- Registration list
- Registration detail view
- Resume and retry payment deep links

##### Business rules

- Candidates view only own registrations
- Registration status reflects payment, verification, and submission state
- Incomplete drafts accessible for resume until expiry policy if any
- Final centre allocation and hall ticket not shown here; handled in Module 06

##### Validations

- List and detail scoped to authenticated candidate identity
- Resume action only for incomplete owned drafts
- Retry payment only when fee pending and not fee-compliant

##### Workflow

LIST_VIEW → DETAIL_VIEW → RESUME_DRAFT or RETRY_PAYMENT or READ_ONLY_CONFIRMED

##### Search requirements

- Search own registrations by application number
- Filter by registration status
- Filter by examination name

##### Documents

- Link to payment receipt where payment completed

##### Security

- Strict candidate ownership scoping on all queries
- No cross-candidate data leakage in search

##### Dependencies

- F05-001 — Candidate OTP Login
- F05-012 — Registration Confirmation
- F05-011 — Failed Payment Handling for retry links

##### Assumptions

- Status vocabulary aligned with optional verification feature when enabled

##### Risks

- Stale status if asynchronous payment callback delayed

##### Non-functional requirements

- List pagination for candidates with many registrations
- Mobile-friendly status views

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | My Registrations list with status chips and application numbers | Medium | 16 |
| UI | Registration search by application number filter bar | Easy | 14 |
| UI | Registration status filter dropdown | Simple | 5 |
| UI | Registration detail read-only view with section summaries | Complex | 18 |
| UI | Resume incomplete registration action button | Easy | 14 |
| UI | Retry pending payment action button on detail | Easy | 14 |
| UI | Empty registrations list first-time candidate state | Simple | 5 |
| API | List candidate registrations with status and summary fields | Medium | 6 |
| API | Search candidate registrations by application number | Medium | 6 |
| API | Filter candidate registrations by status and examination | Medium | 6 |
| API | Fetch registration detail with payment and document status | Complex | 8 |
| API | Resolve resume draft deep link to correct workflow step | Complex | 8 |
| Database | Registration list query indexes by candidate and status | Easy | 0.25 |
| Testing | Happy-path list and detail for confirmed registration | Medium | 0.3 |
| Testing | Resume draft and retry payment action availability rules | Complex | 0.5 |
| Testing | Cross-candidate registration access denied | Complex | 0.5 |
| Documentation | Candidate my registrations and status meanings guide | Medium | 0.3 |
| Documentation | Registration status vocabulary technical reference | Easy | 0.25 |

### F05-034 Optional Registration Application Verification and Administrator Review Gate

132.6 hours · Optional · 19 tasks

##### Description

Supports optional post-submission registration verification where examination administrators review candidate applications including KGID snapshot, manual details, and competent authority document before approving or rejecting registration for downstream scheduling eligibility.

##### Business objective

Provide controlled administrator verification gate for registrations requiring manual approval without standalone workflow engine module.

##### Actors

- Candidate
- Examination Administrator

##### User journey

1. Candidate completes registration submission (F05-012). 2. If verification enabled, registration status set to pending verification. 3. Candidate sees pending verification status in self-service view. 4. Administrator opens registration verification queue. 5. Administrator reviews application summary, profile data, KGID snapshot or manual details, competent authority document, and payment status. 6. Administrator approves or rejects with reason. 7. On approval, registration status transitions to verified or confirmed eligible for scheduling. 8. On rejection, candidate notified with reason and guidance. 9. Candidate views updated status in portal.

##### Functional capabilities

- Post-submit pending verification status assignment when enabled
- Administrator registration verification queue list
- Administrator application detail review screen
- Competent authority document review in verification context
- Approve registration action with audit
- Reject registration action with mandatory reason
- Candidate pending and outcome status visibility
- Verification outcome notification trigger

##### Inputs

- Submitted registration
- Administrator approve or reject action
- Rejection reason text

##### Outputs

- Updated registration verification status
- Verification audit record
- Candidate notification

##### Business rules

- Verification optional and configurable per examination or globally
- Rejected registrations not eligible for Module 06 scheduling until remediated per policy
- Administrator actions audited
- Competent authority document must be reviewable in verification context

##### Validations

- Approve or reject only by authorised examination administrator
- Rejection reason required on reject
- Verification actions only on pending verification registrations
- Candidate cannot self-approve

##### Workflow

CONFIRMED → PENDING_VERIFICATION → APPROVED or REJECTED; REJECTED → candidate notified; APPROVED → eligible for scheduling handoff to Module 06

##### Search requirements

- Administrator queue search by application number, candidate name, examination, status
- Filter pending verification registrations

##### Documents

- Competent authority document viewed in verification context

##### Notifications

- Verification outcome notification via Module 07

##### Security

- Administrator role required from Module 01
- Verification audit immutable

##### Integrations

- Module 07 — Verification outcome notifications

##### Dependencies

- F05-012 — Registration Confirmation
- F05-006 — Competent authority document
- Module 01 — Examination Administrator Role
- Module 06 — Scheduling eligibility consumes verification outcome

##### Assumptions

- Client confirms whether verification mandatory or disabled at go-live

##### Risks

- Verification backlog delays scheduling
- Inconsistent rejection reasons without structured codes

##### Non-functional requirements

- Verification queue pagination for high registration volume

##### Notes

Embedded optional approval per module notes; enable when client requires application verification before scheduling.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate pending verification status banner on registration detail | Simple | 5 |
| UI | Candidate registration rejected status view with administrator reason | Medium | 16 |
| UI | Administrator registration verification queue list with filters | Complex | 18 |
| UI | Administrator registration verification detail review screen | Very high | 24 |
| UI | Administrator approve registration confirmation dialog | Simple | 5 |
| UI | Administrator reject registration dialog with reason capture | Medium | 16 |
| API | Assign pending verification status on submit when policy enabled | Medium | 6 |
| API | List pending verification registrations for administrator queue | Medium | 6 |
| API | Search and filter verification queue by application and examination | Medium | 6 |
| API | Fetch registration verification detail bundle | Complex | 8 |
| API | Approve registration with audit trail | Complex | 8 |
| API | Reject registration with mandatory reason and audit trail | Complex | 8 |
| Database | Registration verification status and decision audit history | Complex | 0.5 |
| Integration | Verification outcome notification to Module 07 | Simple | 4 |
| Testing | Happy-path administrator approve to eligible status | Complex | 0.5 |
| Testing | Reject with reason and candidate visibility cases | Medium | 0.3 |
| Testing | Unauthorized user and double-decision prevention | Complex | 0.5 |
| Documentation | Administrator registration verification procedure runbook | Complex | 0.5 |
| Documentation | Candidate pending verification and rejection guidance | Medium | 0.3 |
