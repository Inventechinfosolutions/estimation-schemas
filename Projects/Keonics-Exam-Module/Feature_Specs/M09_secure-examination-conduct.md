# Module 09: Secure Examination Conduct

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 8 (F09-001 … F09-008)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 09 Secure Examination Conduct

845.1 hours · 188 tasks · Business

Authorised-centre-only examination delivery including login validation, secure interface, timing, activity capture, and submission.

### F09-001 Examination Credential Login and Session Gate

115.5 hours · Go-live · 26 tasks

##### Description

Allows a candidate to authenticate for an allotted examination session using system-generated examination credentials, validating identity, centre, session, schedule window, allocation, and centre activation before granting access to the secure examination conduct flow.

##### Business objective

Ensure only the correctly allocated candidate can begin an examination at the authorised centre during the approved session window, using credentials issued for that specific attempt.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. Candidate arrives at the allotted authorised examination centre and opens the secure examination login page on the assigned centre computer.
2. Candidate enters examination credential fields provided via hall ticket or secure distribution (credential identifier and secret).
3. System validates credential authenticity against issued credential records from Module 06.
4. System validates that the candidate record linked to the credential matches the registration and allocation.
5. System validates that login is attempted from the candidate's allotted examination centre.
6. System validates that the candidate is assigned to the current examination session and seat/computer where applicable.
7. System validates current date-time against session reporting time, session start time, and late-entry policy if configured.
8. System checks whether the centre invigilator has activated the candidate session in Module 08.
9. If activation is pending, candidate sees a waiting state with session details and cannot enter the examination interface.
10. If all gates pass, system creates an examination conduct session and routes the candidate to question paper assembly.
11. If any gate fails, candidate sees a specific denial reason and guidance without exposing sensitive validation internals.

##### Functional capabilities

- Render secure examination credential login form
- Validate issued examination credential identifier and secret
- Match credential to candidate registration and allocation record
- Validate login centre against allotted centre
- Validate login against assigned examination session
- Validate login against seat or computer assignment when allocated
- Enforce session reporting-time and start-time window rules
- Detect cancelled or suspended examination session
- Check centre session activation status from centre operations
- Display waiting-for-activation state when session not yet activated
- Display field-level and rule-level login denial messages
- Persist login attempt outcome for audit
- Create candidate examination conduct session on successful gate

##### Inputs

- Examination credential identifier
- Examination credential secret
- Client centre context identifier
- Client session context identifier
- Client device identifier snapshot
- Client network identifier snapshot
- Current server timestamp

##### Outputs

- Examination conduct session token
- Login success confirmation with session metadata
- Login denial response with reason code
- Waiting-for-activation status view
- Login attempt audit record

##### Business rules

- Examination login is permitted only with system-generated credentials issued for the specific candidate attempt.
- Login is denied when the candidate is not allocated to the centre from which login is attempted.
- Login is denied when the candidate is not allocated to the active examination session.
- Login is denied outside the configured reporting-time and examination-start window unless a late-entry rule explicitly allows it.
- Login is denied when the examination session is cancelled or suspended.
- Login to the examination interface is blocked until centre invigilator activation is recorded in Module 08.
- Failed login attempts are recorded without revealing which individual validation rule failed beyond safe user messaging.

##### Validations

- Credential identifier is required and must match an active issued credential record.
- Credential secret is required and must match the stored hash for the issued credential.
- Credential must not be expired or revoked.
- Credential must belong to the candidate attempt in scheduled or in-progress state.
- Allotted centre identifier must match centre context supplied at login.
- Session identifier must match candidate session allocation.
- Seat or computer assignment must match assigned resource when seat-level allocation exists.
- Current timestamp must fall within reporting-time to end-of-late-entry window.
- Session status must not be cancelled or suspended.
- Activation status must be active before examination interface access is granted.

##### Calculations

- Remaining minutes until session start when candidate arrives before start time.
- Late-entry eligibility based on configured grace period from Module 04 examination configuration consumed at runtime.

##### Workflow

CredentialSubmitted → ValidatingCredential → ValidatingAllocation → ValidatingScheduleWindow → CheckingActivation → AwaitingActivation | SessionCreated → ReadyForPaperAssembly; any validation failure transitions to LoginDenied with immutable attempt log.

##### Search requirements

- Lookup issued credential by credential identifier for validation only; no candidate-facing search register in this feature.

##### Documents

- Hall ticket credential reference used by candidate at login; document generation is out of scope in Module 06.

##### Reports

- Login attempt outcomes available to downstream administration reporting in Module 12; no standalone report UI in this feature.

##### Notifications

- No direct candidate notification dispatch in this feature; failed login messaging is on-screen only.

##### Security

- Credential secret validated using stored secure hash comparison.
- Rate limiting on repeated failed login attempts per credential and client endpoint.
- Login denial messages avoid disclosing whether credential identifier or secret was incorrect.
- Examination conduct session token issued only after all gate validations pass.

##### Integrations

- Module 06 Examination Credential Generation and Secure Distribution Handoff for issued credential validation.
- Module 06 Candidate Centre and Session Allocation for centre and session matching.
- Module 03 Authorised Examination Centre Master for centre identity resolution.
- Module 08 Candidate Examination Session Activation for activation status check.

##### Dependencies

- F06-005 Examination Credential Generation and Secure Distribution Handoff
- F06-003 Candidate Centre and Session Allocation
- F08-004 Candidate Examination Session Activation
- F03-004 Authorised Centre Access Restriction Configuration

##### Assumptions

- Examination credentials are issued before examination day by Module 06.
- Centre context identifier is available from centre-locked examination client deployment.
- Late-entry grace rules are configured in Module 04 and readable at login validation time.

##### Risks

- Clock skew between centre clients and server may affect schedule window validation unless centrally synchronized.
- Shared hall ticket exposure could allow credential use from wrong centre if centre enforcement in Feature 002 fails.

##### Non-functional requirements

- Login validation response within 2 seconds under nominal centre load.
- Login gate available during entire scheduled session window with high availability matching examination conduct SLA.

##### Notes

Consumes system-generated credentials from Module 06; does not generate credentials or hall tickets.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination credential login form with identifier and secret fields | Easy | 14 |
| UI | Invalid credential denial screen with safe generic messaging | Simple | 5 |
| UI | Wrong centre denial screen with allotted centre reference | Simple | 5 |
| UI | Outside schedule window denial screen with reporting and start times | Simple | 5 |
| UI | Waiting-for-invigilator-activation read-only status page | Simple | 5 |
| UI | Cancelled or suspended session denial screen | Simple | 5 |
| API | Validate issued examination credential identifier and secret | Medium | 6 |
| API | Match credential to candidate registration and attempt record | Medium | 6 |
| API | Validate login centre against candidate allotted centre | Medium | 6 |
| API | Validate login against assigned examination session | Medium | 6 |
| API | Validate login against assigned seat or computer when allocated | Medium | 6 |
| API | Enforce reporting-time and examination-start schedule window | Complex | 8 |
| API | Reject login for cancelled or suspended session | Easy | 4 |
| API | Fetch centre session activation status gate | Easy | 4 |
| API | Create candidate examination conduct session on successful gate | Complex | 8 |
| Database | Examination login attempt persistence with outcome reason code | Easy | 0.25 |
| Database | Candidate examination conduct session core record | Medium | 0.3 |
| Integration | Issued credential lookup handoff from Module 06 | Easy | 8 |
| Integration | Candidate allocation lookup handoff from Module 06 | Easy | 8 |
| Integration | Centre activation status lookup handoff from Module 08 | Simple | 4 |
| Testing | Successful login at correct centre within schedule window | Medium | 0.3 |
| Testing | Invalid credential and revoked credential rejection cases | Medium | 0.3 |
| Testing | Wrong centre wrong session and wrong seat rejection cases | Complex | 0.5 |
| Testing | Out-of-window cancelled session and pre-activation blocking cases | Medium | 0.3 |
| Documentation | Candidate examination login user runbook | Easy | 0.25 |
| Documentation | Technical notes on login validation chain and reason codes | Medium | 0.3 |

### F09-002 Authorised Centre Device and Network Enforcement

106.75 hours · Go-live · 24 tasks

##### Description

Technically enforces that examination conduct occurs only from authorised examination centres, approved devices, and approved networks, validating at login and continuously during an active session with termination on persistent violation.

##### Business objective

Prevent candidates from taking examinations from home, personal devices, unauthorised networks, or centres other than their allotted authorised centre.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. After credential validation, system captures client centre identifier, device fingerprint, and network address snapshot.
2. System resolves centre identity against authorised centre registry from Module 03.
3. System confirms candidate-centre allocation mapping matches resolved centre.
4. System evaluates device against centre-approved device rules when configured.
5. System evaluates network address against centre-approved network rules when configured.
6. If enforcement fails at login, candidate sees access blocked screen with approved reason code.
7. If enforcement passes, candidate proceeds to examination conduct with enforcement token bound to session.
8. During active examination, system periodically re-validates centre, device, and network context.
9. On transient network blip, candidate sees reconnect warning with grace timer per policy.
10. On persistent enforcement failure, system transitions session to TerminatedEnforcement and blocks further responses.
11. Enforcement events are recorded for audit and centre monitoring visibility in Module 08.

##### Functional capabilities

- Capture client centre device and network snapshot at login
- Resolve centre identity against authorised centre registry
- Validate candidate-centre allocation against resolved centre
- Validate device against centre device allow rules
- Validate network against centre network allow rules
- Display access blocked screen with reason code at login
- Bind enforcement context token to active examination session
- Periodic re-validation of centre device network during active session
- Display reconnect warning on transient enforcement failure
- Terminate session on persistent enforcement violation
- Persist enforcement pass and fail events with snapshots

##### Inputs

- Client centre identifier
- Device fingerprint attributes
- Client IP address
- Network segment metadata when available
- Candidate examination conduct session identifier
- Authorised centre restriction rules from Module 03

##### Outputs

- Enforcement pass or fail decision
- Access blocked reason code
- Enforcement-bound session token
- Reconnect warning state
- Enforcement termination record
- Enforcement event audit entries

##### Business rules

- Examination access is denied when login centre cannot be resolved to an authorised active centre.
- Examination access is denied when resolved centre does not match candidate allotted centre.
- When centre device rules are configured, login device must match an approved centre device record.
- When centre network rules are configured, client network must match approved centre network ranges.
- Enforcement re-checks continue throughout active examination at configured interval.
- Transient network loss may allow grace period before session termination based on approved policy.
- Persistent enforcement failure terminates examination conduct session without manual submit.

##### Validations

- Centre identifier must resolve to an active authorised examination centre.
- Resolved centre must equal candidate allotted centre identifier.
- Device fingerprint must match at least one approved centre device when device restriction enabled.
- Client IP must fall within approved centre network CIDR list when network restriction enabled.
- Enforcement token must remain bound to original device fingerprint for session lifetime when binding enabled.
- Re-validation interval must not be bypassed by client-side timer manipulation.

##### Calculations

- Grace period remaining during transient network enforcement failure.
- Count of consecutive enforcement failures before session termination.

##### Workflow

CapturingContext → ValidatingCentre → ValidatingDevice → ValidatingNetwork → EnforcementPassed → ActiveMonitoring → TransientWarning | TerminatedEnforcement; login failure transitions to AccessBlocked.

##### Search requirements

- Resolve authorised centre by centre identifier.
- Lookup centre device allow list by centre identifier.
- Lookup centre network allow list by centre identifier.

##### Reports

- Enforcement failure events feed centre live monitoring in Module 08.

##### Notifications

- On-screen reconnect warning only; no outbound notification in this feature.

##### Security

- Enforcement decisions made server-side using client-reported and server-observed network attributes.
- Session termination on enforcement failure is immediate and cannot be reversed by candidate.
- Enforcement snapshots stored for post-examination audit.

##### Integrations

- Module 03 Authorised Examination Centre Master Lifecycle for centre resolution.
- Module 03 Authorised Centre Access Restriction Configuration for device and network rules.
- Module 08 Centre Live Examination Session Monitoring for enforcement alert visibility.

##### Dependencies

- F03-001 Authorised Examination Centre Master Lifecycle
- F03-004 Authorised Centre Access Restriction Configuration
- F03-002 Centre Capacity and Infrastructure Configuration
- F09-001 Examination Credential Login and Session Gate

##### Assumptions

- Centre examination clients are deployed on centre-managed computers with stable centre identifier provisioning.
- Network allow lists are maintained by examination administrators in Module 03 before examination day.

##### Risks

- Centre network reconfiguration on examination day may cause false enforcement failures.
- Device fingerprint drift after browser update may require centre IT intervention.

##### Non-functional requirements

- Initial enforcement check completes within 1 second of login gate completion.
- Periodic re-validation imposes negligible impact on examination interface responsiveness.

##### Notes

Technical enforcement during login and continuously during active examination; complements centre restriction configuration in Module 03.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Access blocked screen for unauthorised centre | Simple | 5 |
| UI | Access blocked screen for unapproved device | Simple | 5 |
| UI | Access blocked screen for unapproved network | Simple | 5 |
| UI | Transient network reconnect warning banner with grace countdown | Medium | 16 |
| UI | Enforcement termination full-screen lock with reason code | Simple | 5 |
| API | Resolve client centre identifier against authorised centre registry | Easy | 4 |
| API | Validate candidate-centre allocation against resolved centre | Medium | 6 |
| API | Validate client device against centre device allow rules | Medium | 6 |
| API | Validate client network against centre network allow rules | Medium | 6 |
| API | Bind enforcement context token to examination conduct session | Complex | 8 |
| API | Periodic centre device network re-validation during active session | Complex | 8 |
| API | Apply transient enforcement grace period policy | Medium | 6 |
| API | Terminate session on persistent enforcement violation | Complex | 8 |
| Database | Enforcement event log with device and network snapshots | Medium | 0.3 |
| Database | Session enforcement binding record with grace state | Easy | 0.25 |
| Integration | Authorised centre registry lookup from Module 03 | Simple | 4 |
| Integration | Centre device and network restriction rule lookup from Module 03 | Easy | 8 |
| Integration | Enforcement alert feed to Module 08 live monitoring | Simple | 4 |
| Testing | Approved centre device and network login happy path | Medium | 0.3 |
| Testing | Home network and wrong centre rejection at login | Complex | 0.5 |
| Testing | Mid-examination network loss grace and termination paths | Complex | 0.5 |
| Testing | Device fingerprint mismatch and bypass attempt cases | Medium | 0.3 |
| Documentation | Centre IT setup guide for device and network enforcement | Medium | 0.3 |
| Documentation | Technical troubleshooting notes for enforcement reason codes | Medium | 0.3 |

### F09-003 Dynamic Question Paper Assembly and Personalisation

83 hours · Go-live · 22 tasks

##### Description

Assembles a unique immutable question paper for each candidate examination session by applying configured random selection rules, version assignment, question order randomisation, and answer option randomisation at examination start.

##### Business objective

Deliver a fair, unpredictable, and auditably unique question paper per candidate while preserving examination integrity and immutability throughout the session.

##### Actors

- Candidate

##### User journey

1. After login gate and enforcement pass, candidate session transitions to paper assembly state.
2. Candidate sees question paper loading progress screen.
3. System reads examination random selection rules and version settings from Module 04 configuration.
4. System selects questions from approved question bank pool per category and count rules.
5. System assigns a question paper version identifier to the candidate session.
6. System randomises question display order per approved settings.
7. System randomises answer option order per question where applicable.
8. System persists a frozen paper snapshot bound to the session.
9. On success, candidate transitions to secure examination interface with assembled paper.
10. On assembly failure due to pool insufficiency or rule conflict, candidate sees failure screen with retry option.
11. On session refresh, candidate receives the same frozen paper without re-randomisation.

##### Functional capabilities

- Display question paper assembly progress screen
- Load examination random selection rules for session
- Select questions from approved pool per category counts
- Assign question paper version to candidate session
- Randomise question order for candidate session
- Randomise answer option order per question
- Persist frozen question paper snapshot
- Serve assembled paper to examination interface
- Display assembly failure screen with retry action
- Return existing frozen paper on session resume without re-randomisation

##### Inputs

- Candidate examination conduct session identifier
- Examination identifier
- Random selection rules from Module 04
- Multiple version and randomisation settings from Module 04
- Approved question bank items from Module 04
- Server-side random seed policy

##### Outputs

- Assigned question paper version identifier
- Ordered question list with randomised options
- Frozen paper snapshot identifier
- Assembly failure reason code
- Assembly audit record

##### Business rules

- Question paper is assembled once per candidate examination session.
- Assembled paper is immutable for the session lifetime.
- Random selection must satisfy all configured category count and difficulty rules.
- Version assignment follows configured multiple-version policy from Module 04.
- Re-login or refresh must not alter previously assigned paper content or order.
- Assembly failure blocks examination start until successful retry or administrator intervention.

##### Validations

- Question pool must contain sufficient approved items for each required category.
- Selected questions must be in approved active status from question bank.
- Version assignment must reference a valid configured version slot.
- Randomisation must produce unique option mapping per question without empty option sets.
- Frozen snapshot must include question identifiers, order indices, and option mappings.
- Retry is blocked when session is already in in-progress or submitted state.

##### Calculations

- Per-category question count fulfillment check against selection rules.
- Deterministic random seed derivation from session identifier and examination identifier for reproducible audit.

##### Workflow

AssemblyRequested → LoadingRules → SelectingQuestions → AssigningVersion → RandomisingOrder → RandomisingOptions → SnapshotPersisted → PaperReady; insufficient pool transitions to AssemblyFailed → RetryAssembly | AdministratorEscalation.

##### Search requirements

- Retrieve approved question pool filtered by examination and category for selection engine.
- Retrieve existing frozen snapshot by session identifier on resume.

##### Reports

- Assigned version and question identifiers available to downstream evaluation in Module 10.

##### Security

- Correct answer keys are not exposed to candidate client in assembled payload.
- Assembly random seed and snapshot identifiers stored for audit reconstruction.
- Paper content served only to authenticated active session token.

##### Integrations

- Module 04 Random Question Selection Rules for selection criteria.
- Module 04 Multiple Question Paper Version and Randomisation Settings for version and shuffle policy.
- Module 04 Question Bank Item Lifecycle for approved question retrieval.

##### Dependencies

- F04-005 Random Question Selection Rules
- F04-006 Multiple Question Paper Version and Randomisation Settings
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-001 Examination Credential Login and Session Gate

##### Assumptions

- Question bank contains sufficient approved items before examination day.
- Examination configuration in Module 04 defines all selection and randomisation parameters consumed at runtime.

##### Risks

- Insufficient pool depth may block examination start for late sessions if bank changes occur after scheduling.
- Randomisation defects could cause duplicate exposure patterns detectable by candidates if seed policy is weak.

##### Non-functional requirements

- Paper assembly completes within 5 seconds for standard examination size under nominal load.
- Snapshot storage supports concurrent assembly for full centre capacity.

##### Notes

Runtime assembly only; question bank maintenance and rule configuration remain in Module 04.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Question paper assembly progress screen | Simple | 5 |
| UI | Assembly failure screen with retry action | Simple | 5 |
| API | Load random selection rules for examination session | Easy | 4 |
| API | Select questions from approved pool per category rules | Very high | 12 |
| API | Assign question paper version to candidate session | Medium | 6 |
| API | Randomise question display order for session | Medium | 6 |
| API | Randomise answer option order per question | Medium | 6 |
| API | Persist frozen question paper snapshot | Complex | 8 |
| API | Serve assembled paper to examination interface | Medium | 6 |
| API | Return existing frozen paper on session resume | Medium | 6 |
| Database | Candidate session question paper assignment record | Medium | 0.3 |
| Database | Frozen question order and option mapping storage | Complex | 0.5 |
| Database | Version and selection rule reference linkage | Easy | 0.25 |
| Integration | Random selection rule retrieval from Module 04 | Simple | 4 |
| Integration | Version and randomisation setting retrieval from Module 04 | Simple | 4 |
| Integration | Approved question bank item retrieval from Module 04 | Easy | 8 |
| Testing | Happy path assembly with order and option randomisation | Complex | 0.5 |
| Testing | Insufficient pool and rule conflict failure cases | Medium | 0.3 |
| Testing | Session resume immutability without re-randomisation | Medium | 0.3 |
| Testing | Answer key non-exposure in client payload verification | Medium | 0.3 |
| Documentation | Administrator runbook on assembly behaviour and retry | Easy | 0.25 |
| Documentation | Technical notes on random seed and snapshot audit reconstruction | Medium | 0.3 |

### F09-004 Secure Examination Interface and Response Capture

180.35 hours · Go-live · 27 tasks

##### Description

Provides the secure candidate examination interface for navigating assembled questions, capturing and auto-saving responses, displaying progress and remaining time, and preparing for submission confirmation.

##### Business objective

Enable candidates to complete examinations reliably with continuous response preservation, clear navigation, and secure interaction constraints during the active session.

##### Actors

- Candidate

##### User journey

1. Candidate enters examination interface after paper assembly completes.
2. Candidate sees examination shell with question panel, navigation panel, timer area, and auto-save indicator.
3. Candidate views first question with response controls appropriate to question type.
4. Candidate selects or enters a response; system auto-saves draft within seconds.
5. Candidate navigates to another question using navigation panel or next/previous controls.
6. Candidate marks a question for review; navigation panel updates status chip.
7. Candidate clears a response via clear action and confirms in dialog.
8. Auto-save indicator shows saving, saved, or error retry state.
9. If connection is lost, candidate sees offline banner; responses queue until reconnect.
10. Candidate reviews navigation summary showing attempted, unattempted, and marked counts.
11. Candidate initiates submit flow routed to submission feature when ready or when timer expires.

##### Functional capabilities

- Render examination shell layout with timer and auto-save areas
- Render question navigation panel with status chips
- Render single-question view with type-specific response controls
- Capture single-choice response selection
- Capture multiple-choice response selection
- Capture numeric response entry where applicable
- Capture text response entry where applicable
- Toggle mark-for-review per question
- Clear response with confirmation dialog
- Auto-save draft response on change
- Display auto-save status indicator
- Display connection loss offline banner
- Recover queued responses after reconnect
- Display navigation summary counts
- Block interface interaction after response lock from submission

##### Inputs

- Assembled question paper payload
- Question identifier
- Response value by question type
- Mark-for-review flag
- Client connectivity state
- Session lock status

##### Outputs

- Saved draft response records
- Navigation summary counts
- Auto-save status events
- Offline queue recovery outcome
- Read-only locked interface state

##### Business rules

- Responses auto-save without requiring manual save action.
- Mark-for-review does not count as attempted unless a response exists.
- Clear response requires explicit confirmation.
- Interface becomes read-only immediately upon submission lock.
- Offline responses are queued client-side and replayed in order on reconnect.
- Navigation remains available unless session is locked or terminated.

##### Validations

- Single-choice response must contain exactly one selected option identifier.
- Multiple-choice response must contain one or more valid option identifiers without duplicates.
- Numeric response must match configured numeric format and range when defined.
- Text response must not exceed configured maximum length.
- Response save rejected when session is locked or terminated.
- Question identifier must belong to session frozen paper snapshot.

##### Calculations

- Attempted question count based on non-empty saved responses.
- Unattempted question count as total minus attempted.
- Marked-for-review count independent of attempt status.

##### Workflow

PaperReady → InProgress ↔ AutoSaving ↔ OfflineQueued → ReadyToSubmit; submission lock transitions to ResponseLocked read-only state.

##### Search requirements

- Retrieve current session paper state and saved responses by session identifier.

##### Security

- Response payload excludes correct answer key material.
- Examination interface disables copy paste and context menu per security feature coordination.
- Auto-save requests require active authenticated session token.

##### Integrations

- Module 04 question type metadata for response control rendering.
- Feature F09-003 frozen paper snapshot for question content.
- Feature F09-005 timer display sync for remaining time area.

##### Dependencies

- F09-003 Dynamic Question Paper Assembly and Personalisation
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-006 Examination Session Security Controls

##### Assumptions

- Supported question types are limited to those configured in Module 04 for the examination.
- Centre network may have brief intermittent connectivity; offline queue duration is bounded by examination policy.

##### Risks

- Extended offline period may cause response loss if queue exceeds client storage limits.
- Large text responses may affect auto-save performance on low-spec centre hardware.

##### Non-functional requirements

- Auto-save completes within 1 second of response change under nominal conditions.
- Examination interface remains responsive for papers up to configured maximum question count.

##### Notes

Candidate-facing examination UI; scoring and result display are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination shell layout with header timer and question panel | Complex | 18 |
| UI | Question navigation panel with attempted unattempted marked chips | Medium | 16 |
| UI | Single-choice question response control | Easy | 14 |
| UI | Multiple-choice question response control | Easy | 14 |
| UI | Numeric question response input control | Easy | 14 |
| UI | Text question response input control | Easy | 14 |
| UI | Mark-for-review toggle control per question | Simple | 5 |
| UI | Clear response confirmation dialog | Simple | 5 |
| UI | Auto-save status indicator component | Simple | 5 |
| UI | Connection loss offline banner with retry state | Medium | 16 |
| UI | Navigation summary counts panel before submit handoff | Easy | 14 |
| UI | Read-only locked interface state after submission lock | Simple | 5 |
| API | Fetch current session paper and saved response state | Medium | 6 |
| API | Auto-save single question draft response | Medium | 6 |
| API | Batch replay queued offline draft responses | Complex | 8 |
| API | Toggle mark-for-review flag for question | Easy | 4 |
| API | Clear question draft response | Easy | 4 |
| API | Retrieve navigation summary counts for session | Easy | 4 |
| API | Validate response format by question type | Medium | 6 |
| Database | Draft response storage with save timestamps | Medium | 0.3 |
| Database | Mark-for-review flag storage per question | Simple | 0.1 |
| Testing | Happy path navigation auto-save and mark-for-review | Medium | 0.3 |
| Testing | Invalid response format rejection by question type | Medium | 0.3 |
| Testing | Offline queue replay and conflict handling | Complex | 0.5 |
| Testing | Read-only behaviour after session response lock | Easy | 0.25 |
| Documentation | Candidate secure examination interface user guide | Medium | 0.3 |
| Documentation | Technical notes on auto-save frequency and offline replay | Medium | 0.3 |

### F09-005 Centrally Controlled Examination Timer

71.45 hours · Go-live · 19 tasks

##### Description

Controls the official examination duration from a central server clock, displays remaining time to the candidate, warns on low time, stops the examination at expiry, and triggers automatic submission.

##### Business objective

Ensure uniform examination duration enforcement across all centres independent of client device clock manipulation.

##### Actors

- Candidate

##### User journey

1. When candidate enters in-progress state, system initialises timer from examination duration configuration.
2. Candidate sees countdown timer in examination shell header.
3. System periodically syncs remaining time from server on configured interval.
4. When remaining time crosses low-time threshold, candidate sees warning banner.
5. Candidate continues responding while timer counts down.
6. At zero remaining time, system transitions session to TimerExpired state.
7. Candidate sees time-expired overlay and auto-submit in-progress modal.
8. System invokes automatic submission workflow in Feature 008.
9. After auto-submit completes, candidate sees submission outcome screen from submission feature.
10. If candidate attempts action after expiry before auto-submit completes, action is blocked.

##### Functional capabilities

- Initialise examination timer from configured duration
- Calculate server-authoritative remaining time
- Expose remaining time sync endpoint for client display
- Correct client display for clock drift
- Display countdown timer in examination interface
- Display low-time warning banner at threshold
- Display time-expired overlay at zero remaining
- Display auto-submit in-progress modal during expiry handling
- Transition session to TimerExpired state at zero
- Trigger automatic submission on timer expiry
- Block candidate actions after expiry pending submission completion
- Persist timer anchor and sync audit events

##### Inputs

- Examination duration from Module 04 configuration
- Session official start timestamp
- Current server timestamp
- Client-reported local timestamp for drift detection
- Low-time warning threshold configuration

##### Outputs

- Remaining seconds value for client display
- TimerExpired state transition
- Auto-submission trigger event
- Timer sync audit entries
- Low-time warning display state

##### Business rules

- Examination timer starts from official session start timestamp, not client login time, unless configured otherwise.
- Remaining time is calculated only on server; client display is advisory.
- Examination automatically stops at zero remaining time with no manual extension by candidate.
- Automatic submission is mandatory on timer expiry.
- Timer continues during brief offline periods using last known server sync plus elapsed server time.
- Invigilator manual time extension is out of scope in this module.

##### Validations

- Timer initialisation requires valid examination duration greater than zero.
- Official start timestamp must be recorded before in-progress timer begins.
- Sync requests rejected for locked submitted or terminated sessions.
- Client drift beyond tolerance triggers forced resync without resetting remaining time.

##### Calculations

- Remaining seconds equals configured duration minus elapsed server time since official start.
- Low-time warning when remaining seconds less than or equal to configured threshold.

##### Workflow

TimerInitialised → InProgress → LowTimeWarning → TimerExpired → AutoSubmitting → Submitted; drift detection loops ResyncDisplay without altering RemainingSeconds authority.

##### Search requirements

- Retrieve session timer state by examination conduct session identifier.

##### Reports

- Timer start and expiry timestamps available in activity recording for audit.

##### Security

- Client cannot extend remaining time via manipulated local clock.
- Timer expiry transition is idempotent to prevent duplicate auto-submission triggers.

##### Integrations

- Module 04 Examination Master Configuration for duration and warning threshold.
- Feature F09-008 Examination Submission for auto-submit on expiry.

##### Dependencies

- F04-004 Examination Master Configuration
- F09-004 Secure Examination Interface and Response Capture
- F09-008 Examination Submission and Response Locking

##### Assumptions

- Official session start timestamp is set when candidate transitions to in-progress after paper assembly.
- Examination duration is fixed per examination configuration without per-candidate variation.

##### Risks

- Server clock issues could affect all concurrent sessions simultaneously.
- Auto-submit at expiry during unsaved response may lose last unsynced client draft if offline queue exhausted.

##### Non-functional requirements

- Timer sync endpoint responds within 200 milliseconds under nominal load.
- Timer expiry processing initiates auto-submission within 2 seconds of reaching zero.

##### Notes

Server-authoritative timer; auto-submission handoff to Feature 008 on expiry.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Countdown timer display in examination header | Easy | 14 |
| UI | Low-time warning banner at configured threshold | Simple | 5 |
| UI | Time-expired full-screen overlay | Simple | 5 |
| UI | Auto-submit in-progress modal during expiry handling | Simple | 5 |
| API | Initialise timer from examination duration configuration | Medium | 6 |
| API | Calculate server-authoritative remaining seconds | Medium | 6 |
| API | Remaining time sync endpoint for client display | Easy | 4 |
| API | Detect and correct client clock drift without resetting authority | Medium | 6 |
| API | Transition session to TimerExpired state at zero remaining | Medium | 6 |
| API | Trigger automatic submission workflow on timer expiry | Complex | 8 |
| API | Block candidate actions after expiry pending submission | Easy | 4 |
| Database | Timer start anchor and official duration storage | Easy | 0.25 |
| Database | Timer sync and expiry audit event storage | Easy | 0.25 |
| Testing | Happy path countdown display and expiry auto-submit trigger | Medium | 0.3 |
| Testing | Client clock drift forced resync cases | Medium | 0.3 |
| Testing | Expiry during unsaved draft edge handling | Complex | 0.5 |
| Testing | Idempotent TimerExpired transition under duplicate sync calls | Medium | 0.3 |
| Documentation | Administrator runbook on timer behaviour and thresholds | Easy | 0.25 |
| Documentation | Technical notes on server clock authority and sync protocol | Medium | 0.3 |

### F09-006 Examination Session Security Controls

103.8 hours · Go-live · 23 tasks

##### Description

Enforces examination security controls including single active session per candidate, browser and session restrictions as approved, focus and visibility monitoring, and forced termination on critical violations.

##### Business objective

Reduce examination malpractice risk by preventing concurrent sessions and detecting disallowed client behaviour during conduct.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. On successful login, system registers active examination session token bound to client.
2. If candidate attempts second login elsewhere, system rejects with single-session enforcement alert.
3. Candidate enters secure examination chrome with restricted copy paste and context menu.
4. If fullscreen is required by policy, candidate sees fullscreen prompt before questions display.
5. During examination, system monitors tab visibility and window focus loss events.
6. On first focus loss, candidate sees warning banner per policy.
7. On repeated violations exceeding threshold, system transitions to TerminatedSecurity state.
8. Candidate sees session termination security violation screen with reason code.
9. Security events stream to activity recording and centre monitoring in Module 08.
10. Terminated session responses remain locked per submission rules.

##### Functional capabilities

- Register active examination session token on login
- Reject second concurrent session for same candidate attempt
- Invalidate prior session when policy allows replacement login
- Bind session token to browser session fingerprint
- Disable copy paste in examination chrome
- Disable context menu in examination chrome
- Prompt fullscreen mode when policy requires
- Record tab visibility change events
- Record window focus loss events
- Display focus loss warning banner
- Evaluate security violation counts against threshold
- Force terminate session on critical violation threshold
- Display security termination screen with reason code
- Stream security events to activity recording

##### Inputs

- Candidate examination conduct session identifier
- Client browser session fingerprint
- Tab visibility state events
- Window focus state events
- Approved security policy configuration
- Violation threshold configuration

##### Outputs

- Active session registry entry
- Concurrent login rejection response
- Security violation events
- Warning banner state
- TerminatedSecurity session state
- Security termination reason code

##### Business rules

- Only one active examination conduct session is permitted per candidate attempt at a time.
- Second login attempt is blocked unless policy explicitly allows session takeover.
- Approved browser restrictions are enforced for entire in-progress session.
- Focus and tab visibility violations accumulate toward termination threshold.
- Critical violation immediate termination applies when configured for specific event types.
- Security termination locks responses and prevents manual submit without invigilator escalation path defined out of scope.

##### Validations

- Session token must match registered active token for request processing.
- Browser session fingerprint must match bound fingerprint when binding enabled.
- Concurrent session check compares candidate attempt identifier not merely credential.
- Violation count resets only on new attempt not mid-session refresh.
- Security events rejected when session already submitted or terminated.

##### Calculations

- Accumulated violation count by event type within session.
- Remaining warnings before termination equals threshold minus current count.

##### Workflow

SessionRegistered → SecuredChrome → Monitoring → WarningIssued → TerminatedSecurity; concurrent login attempt transitions to ConcurrentSessionBlocked.

##### Search requirements

- Lookup active session registry by candidate attempt identifier.

##### Reports

- Security violation summary visible on centre live monitoring in Module 08.

##### Security

- Session tokens are non-guessable and rotated on successful login.
- Security termination is server-authoritative and cannot be dismissed by client.
- Violation thresholds configurable per examination from Module 04 consumed at runtime.

##### Integrations

- Module 04 Examination Master Configuration for approved restriction policy flags.
- Module 08 Centre Live Examination Session Monitoring for violation visibility.
- Feature F09-007 Examination Activity Recording for security event persistence.

##### Dependencies

- F04-004 Examination Master Configuration
- F09-001 Examination Credential Login and Session Gate
- F09-007 Examination Activity Recording
- F08-005 Centre Live Examination Session Monitoring

##### Assumptions

- Examination clients use supported modern browsers capable of visibility and focus APIs.
- Approved restriction set is signed off by examination authority before go-live.

##### Risks

- False positives from legitimate invigilator interactions may trigger warnings if policy thresholds are too aggressive.
- Browser compatibility gaps may limit effectiveness of specific restrictions.

##### Non-functional requirements

- Security event ingestion handles burst events without examination interface lag.
- Concurrent session check completes within login gate time budget.

##### Notes

Implements approved browser and session restrictions; standalone audit-log product is out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Single-session enforcement alert on duplicate login attempt | Simple | 5 |
| UI | Fullscreen requirement prompt before examination start | Simple | 5 |
| UI | Tab visibility focus loss warning banner | Easy | 14 |
| UI | Security violation session termination screen | Simple | 5 |
| UI | Secure examination chrome with copy paste disabled | Medium | 16 |
| API | Register active examination session token | Medium | 6 |
| API | Reject second concurrent session for candidate attempt | Medium | 6 |
| API | Invalidate prior session on approved takeover login | Complex | 8 |
| API | Bind session token to browser session fingerprint | Medium | 6 |
| API | Ingest tab visibility change security events | Easy | 4 |
| API | Ingest window focus loss security events | Easy | 4 |
| API | Evaluate violation count against termination threshold | Medium | 6 |
| API | Force terminate session on critical security threshold | Complex | 8 |
| Database | Active session registry with device binding | Medium | 0.3 |
| Database | Security violation event stream storage | Medium | 0.3 |
| Integration | Security policy flag retrieval from Module 04 | Simple | 4 |
| Integration | Security alert feed to Module 08 live monitoring | Simple | 4 |
| Testing | Happy path single session maintained throughout examination | Medium | 0.3 |
| Testing | Duplicate login blocked and takeover policy path | Complex | 0.5 |
| Testing | Focus loss accumulation and termination threshold cases | Complex | 0.5 |
| Testing | Client restriction bypass attempt handling | Medium | 0.3 |
| Documentation | Approved security controls configuration guide for administrators | Medium | 0.3 |
| Documentation | Technical security event catalogue and threshold reference | Medium | 0.3 |

### F09-007 Examination Activity Recording

65.05 hours · Go-live · 22 tasks

##### Description

Records a comprehensive examination activity trail including login, start, response saves, navigation, version assignment, centre and device context, abnormal events, and submission timestamps for audit and monitoring.

##### Business objective

Provide defensible examination conduct evidence for dispute resolution, monitoring, and downstream administration reporting without relying on a separate audit product.

##### Actors

- Candidate
- Examination Centre/Invigilator User

##### User journey

1. System records login timestamp and credential context when login gate succeeds.
2. System records enforcement snapshot at session start.
3. System records official examination start timestamp when paper assembly completes and in-progress begins.
4. Each auto-save persists a response activity event with question identifier and timestamp.
5. Each navigation action records from-question and to-question identifiers.
6. System records assigned paper version and question identifiers at assembly time.
7. System records centre identifier, device snapshot, and network snapshot on material changes.
8. Security and enforcement abnormal events append to activity stream with classification.
9. System records manual or automatic submission timestamp with submission type.
10. Authorised invigilator monitoring in Module 08 reads abnormal indicators derived from this stream.
11. Authorised administrators query activity timeline through downstream reporting in Module 12.

##### Functional capabilities

- Record login timestamp with credential and centre context
- Record official examination start timestamp
- Record response save activity per question
- Record question navigation from-to events
- Record assigned paper version identifier
- Record assigned question identifier set reference
- Record centre identifier on session events
- Record device snapshot on material changes
- Record network snapshot on material changes
- Record security abnormal events with classification
- Record enforcement abnormal events with classification
- Record manual submission timestamp
- Record automatic submission timestamp
- Expose activity timeline query for authorised audit consumers
- Maintain append-only immutability for recorded events

##### Inputs

- Examination conduct session identifier
- Event type code
- Event timestamp
- Question identifier when applicable
- Response snapshot hash when applicable
- Paper version identifier
- Centre device network snapshots
- Abnormal event classification
- Submission type manual or automatic

##### Outputs

- Append-only activity event records
- Abnormal event flags for centre monitoring
- Activity timeline query results for audit consumers
- Response change history references

##### Business rules

- All material examination conduct actions generate an activity event.
- Activity events are append-only and cannot be edited or deleted by candidates.
- Response activity stores content hash or reference not necessarily full text for large entries per policy.
- Abnormal events include security violations, enforcement failures, and repeated auto-save errors.
- Activity recording continues until session reaches terminal submitted or terminated state.
- Activity data is retained per platform retention policy for examination records.

##### Validations

- Event timestamp must be server-generated or server-validated.
- Session identifier must exist and be in non-terminal state except for terminal event recording.
- Question identifier must belong to session frozen paper for question-scoped events.
- Event type must be from approved examination activity catalogue.
- Query access restricted to authorised roles via Module 01 authorization hooks.

##### Calculations

- Response change count per question from save event stream.
- Time between login and official start.
- Time between official start and submission.

##### Workflow

EventIngested → Appended → AvailableForMonitoring → ArchivedPerRetention; abnormal classification triggers AbnormalFlagged substate visible to Module 08.

##### Search requirements

- Query activity events by session identifier ordered by timestamp.
- Filter activity events by abnormal classification for monitoring feeds.
- Query response change history by session and question identifier.

##### Reports

- Activity timeline underpins Module 12 examination administration reporting.

##### Security

- Activity query endpoints enforce role permissions from Module 01.
- Sensitive credential secrets never stored in activity payloads.
- Append-only storage prevents tampering by application users.

##### Integrations

- Module 08 Centre Live Examination Session Monitoring for abnormal event indicators.
- Module 01 Downstream Module Authorization Integration Hooks for query access control.
- Module 12 Examination Administration and Reporting as downstream consumer.

##### Dependencies

- F09-001 Examination Credential Login and Session Gate
- F09-002 Authorised Centre Device and Network Enforcement
- F09-003 Dynamic Question Paper Assembly and Personalisation
- F09-004 Secure Examination Interface and Response Capture
- F09-006 Examination Session Security Controls
- F09-008 Examination Submission and Response Locking
- F01-006 Downstream Module Authorization Integration Hooks

##### Assumptions

- Event ingestion is synchronous for critical events and asynchronous for high-volume navigation events if performance requires.
- Module 12 provides reporting UI; this feature provides recording and query capability only.

##### Risks

- High-volume navigation logging may increase storage costs for large candidate counts.
- Incomplete event ingestion during server outage may create audit gaps.

##### Non-functional requirements

- Critical event ingestion adds less than 50 milliseconds to request path under nominal load.
- Activity query by session returns within 3 seconds for full examination timeline.

##### Notes

Records conduct audit trail; standalone audit-log product and scoring are out of scope.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| API | Record login timestamp with credential and centre context | Easy | 4 |
| API | Record official examination start timestamp | Easy | 4 |
| API | Record response save activity per question | Medium | 6 |
| API | Record question navigation from-to event | Easy | 4 |
| API | Record assigned paper version identifier at assembly | Easy | 4 |
| API | Record centre device network snapshot on material change | Medium | 6 |
| API | Record security abnormal event with classification | Medium | 6 |
| API | Record enforcement abnormal event with classification | Medium | 6 |
| API | Record manual submission timestamp event | Easy | 4 |
| API | Record automatic submission timestamp event | Easy | 4 |
| API | Query activity timeline by session for authorised auditors | Medium | 6 |
| Database | Append-only examination activity event store | Complex | 0.5 |
| Database | Response change history per question reference | Medium | 0.3 |
| Database | Abnormal event classification indexes | Easy | 0.25 |
| Integration | Abnormal event indicator feed to Module 08 monitoring | Simple | 4 |
| Integration | Authorisation hook for activity query from Module 01 | Simple | 4 |
| Testing | Happy path complete activity trail from login through submit | Complex | 0.5 |
| Testing | Event ordering immutability and append-only enforcement | Medium | 0.3 |
| Testing | Missing event resilience under transient failure | Medium | 0.3 |
| Testing | Unauthorised activity query rejection cases | Medium | 0.3 |
| Documentation | Activity record field guide for auditors and invigilators | Medium | 0.3 |
| Documentation | Technical notes on retention event catalogue and query access | Medium | 0.3 |

### F09-008 Examination Submission and Response Locking

119.2 hours · Go-live · 25 tasks

##### Description

Supports manual candidate submission with review and confirmation as well as automatic submission on timer expiry or approved termination paths, locking all responses upon submission completion.

##### Business objective

Finalise candidate examination attempts with immutable response locking suitable for downstream evaluation while giving candidates clear submission confirmation.

##### Actors

- Candidate

##### User journey

1. Candidate selects submit examination action from navigation summary.
2. Candidate sees review summary with attempted, unattempted, and marked counts.
3. If unattempted questions exist, candidate sees unattempted questions warning dialog.
4. Candidate confirms final submission in confirmation dialog.
5. System validates submission eligibility including session state and timer not already expired in conflicting manner.
6. System locks all responses preventing further edits.
7. System persists final response snapshot with submission type manual.
8. Candidate sees submission success read-only confirmation page.
9. If timer expires, system automatically initiates submission without candidate confirmation.
10. During auto-submit, candidate sees auto-submitted banner on confirmation page.
11. If submission fails due to transient error, candidate sees retry dialog until success or invigilator escalation.
12. Locked responses become available for Module 10 evaluation handoff.

##### Functional capabilities

- Display pre-submit review summary with question counts
- Display unattempted questions warning dialog
- Display final submission confirmation dialog
- Validate submission eligibility for session state
- Lock all responses on submit initiation
- Persist final response snapshot
- Record manual submission type
- Initiate automatic submission on timer expiry
- Initiate automatic submission on approved termination path when policy requires
- Record automatic submission type
- Generate submission receipt metadata
- Prevent further response updates after lock
- Display submission success confirmation page
- Display auto-submitted banner for expiry path
- Display submission failed retry dialog

##### Inputs

- Candidate examination conduct session identifier
- Current draft responses
- Submission trigger type manual automatic or termination
- Session timer state
- Session security or enforcement termination state

##### Outputs

- Submission record with type and timestamp
- Final locked response snapshot
- Submission receipt metadata for candidate display
- Response lock flags
- Evaluation handoff readiness status

##### Business rules

- Manual submission requires explicit candidate confirmation.
- Unattempted question warning is informational; submission may proceed if candidate confirms.
- Automatic submission on timer expiry does not require candidate confirmation.
- Once submitted, responses are immutable for the attempt.
- Double submission attempts are idempotent returning existing submission receipt.
- Submission blocked when session already terminated for enforcement unless policy allows salvage submit.
- Evaluation handoff occurs only after successful submission persistence.

##### Validations

- Submission rejected when session not in in-progress or timer-expired eligible state.
- Submission rejected when responses already locked.
- Final snapshot must include all saved draft responses at lock time.
- Submission receipt must include session identifier submission timestamp and type.
- Retry allowed only when prior submit attempt did not persist lock record.

##### Calculations

- Final attempted count at lock time.
- Final unattempted count at lock time.

##### Workflow

ReadyToSubmit → ReviewSummary → ConfirmSubmit → LockingResponses → PersistingFinal → Submitted; timer expiry transitions TimerExpired → AutoSubmitting → Submitted; transient failure transitions to SubmitFailed → RetrySubmit.

##### Search requirements

- Retrieve submission status by session identifier to enforce idempotency.

##### Documents

- Submission receipt metadata displayed to candidate; printable certificate is out of scope in Module 11.

##### Reports

- Submission counts and timestamps feed Module 12 administration reporting.

##### Notifications

- Optional examination lifecycle notification handoff to Module 07 on submission event subscription.

##### Security

- Submission lock is server-authoritative; client cannot unlock responses.
- Submission endpoints require active session token until lock completes.

##### Integrations

- Feature F09-005 Centrally Controlled Examination Timer for expiry trigger.
- Feature F09-007 Examination Activity Recording for submit events.
- Module 10 Evaluation and Results for locked response handoff.
- Module 07 Examination Lifecycle Event Subscription for optional submit notification.

##### Dependencies

- F09-004 Secure Examination Interface and Response Capture
- F09-005 Centrally Controlled Examination Timer
- F09-007 Examination Activity Recording
- F10-001 Evaluation and Results
- F07-003 Examination Lifecycle Event Subscription and Template Routing

##### Assumptions

- Module 10 consumes locked final snapshot via agreed handoff interface without scoring logic in this module.
- Transient submission failures are rare; retry UI sufficient for centre recovery.

##### Risks

- Partial lock during server failure could leave ambiguous state without idempotent retry design.
- Auto-submit at expiry with pending offline drafts may submit last synced state only.

##### Non-functional requirements

- Manual submission completes within 3 seconds under nominal load.
- Submission lock is strongly consistent before success confirmation displayed to candidate.

##### Notes

Manual and automatic submission; scoring in Module 10 is out of scope but locked responses must be handoff-ready.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Pre-submit review summary screen with question counts | Medium | 16 |
| UI | Unattempted questions warning dialog | Simple | 5 |
| UI | Final submission confirmation dialog | Simple | 5 |
| UI | Submission success read-only confirmation page | Easy | 14 |
| UI | Auto-submitted banner on expiry submission confirmation page | Simple | 5 |
| UI | Submission failed retry dialog | Simple | 5 |
| API | Validate submission eligibility for session state | Medium | 6 |
| API | Lock all responses on submit initiation | Complex | 8 |
| API | Persist final response snapshot for manual submit | Complex | 8 |
| API | Persist final response snapshot for automatic submit on timer expiry | Complex | 8 |
| API | Persist final response snapshot for approved termination auto-submit path | Complex | 8 |
| API | Generate submission receipt metadata | Easy | 4 |
| API | Prevent further response updates after lock | Medium | 6 |
| API | Idempotent resubmit returning existing receipt | Medium | 6 |
| Database | Submission record with manual or automatic type | Medium | 0.3 |
| Database | Final locked response snapshot storage | Complex | 0.5 |
| Database | Response lock flag persistence per session | Easy | 0.25 |
| Integration | Locked response handoff readiness signal to Module 10 | Easy | 8 |
| Integration | Optional submission event publish to Module 07 notification routing | Simple | 4 |
| Testing | Happy path manual submit with response lock verification | Complex | 0.5 |
| Testing | Automatic submit on timer expiry path | Medium | 0.3 |
| Testing | Submit blocked for invalid session state cases | Medium | 0.3 |
| Testing | Double submit idempotency and transient retry cases | Complex | 0.5 |
| Documentation | Candidate submission process user guide | Easy | 0.25 |
| Documentation | Technical notes on submission state machine and lock semantics | Medium | 0.3 |
