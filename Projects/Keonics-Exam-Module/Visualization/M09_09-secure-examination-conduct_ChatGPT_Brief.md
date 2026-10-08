# ChatGPT Visualization Brief — Module 09: Secure Examination Conduct

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 09 Secure Examination Conduct
**Features:** 8 (F09-001 … F09-008)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 09 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Credential login + network/device enforcement sequence
2. Paper assembly / randomisation sequence (preserve answer key)
3. Timer + heartbeat + autosave architecture
4. Security violation threshold → terminate flowchart
5. Submit/lock state machine + activity event taxonomy
6. Conduct ERD
7. Feature relationship / dependency graph within this module and to other modules
8. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Secure Examination Conduct
**Purpose:** Secure centre-based exam conduct: credential login, device/network enforcement, dynamic paper assembly, response capture, timer, security controls, activity log, submission lock.

**Actors (union across features):**
- Candidate
- Examination Centre/Invigilator User

**Feature list:**
- **F09-001** — Examination Credential Login and Session Gate
- **F09-002** — Authorised Centre Device and Network Enforcement
- **F09-003** — Dynamic Question Paper Assembly and Personalisation
- **F09-004** — Secure Examination Interface and Response Capture
- **F09-005** — Centrally Controlled Examination Timer
- **F09-006** — Examination Session Security Controls
- **F09-007** — Examination Activity Recording
- **F09-008** — Examination Submission and Response Locking

### DATA MODEL (from EXAM DB design v2.1)

- `exam_attempt (conduct fields)`
- `paper_instance`
- `paper_instance_item`
- `exam_response`
- `exam_activity_event`
- `access_denial_log`
- `conduct_security_policy`

### FEATURE CATALOGUE

#### F09-001 — Examination Credential Login and Session Gate

**One-liner / description:** Allows a candidate to authenticate for an allotted examination session using system-generated examination credentials, validating identity, centre, session, schedule window, allocation, and centre activation before…

**Business objective:** Ensure only the correctly allocated candidate can begin an examination at the authorised centre during the approved session window, using credentials issued for that specific attempt.

**Actors:** Candidate; Examination Centre/Invigilator User

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Examination credential identifier; Examination credential secret; Client centre context identifier; Client session context identifier; Client device identifier snapshot; Client network identifier snapshot; Current server timestamp

**Outputs:** Examination conduct session token; Login success confirmation with session metadata; Login denial response with reason code; Waiting-for-activation status view; Login attempt audit record

**Business rules:**
- Examination login is permitted only with system-generated credentials issued for the specific candidate attempt.
- Login is denied when the candidate is not allocated to the centre from which login is attempted.
- Login is denied when the candidate is not allocated to the active examination session.
- Login is denied outside the configured reporting-time and examination-start window unless a late-entry rule explicitly allows it.
- Login is denied when the examination session is cancelled or suspended.
- Login to the examination interface is blocked until centre invigilator activation is recorded in Module 08.
- Failed login attempts are recorded without revealing which individual validation rule failed beyond safe user messaging.

**Validations:**
- Credential identifier is required and must match an active issued credential record.
- Credential secret is required and must match the stored hash for the issued credential.
- Credential must not be expired or revoked.
- Credential must belong to the candidate attempt in scheduled or in-progress state.
- Allotted centre identifier must match centre context supplied at login.
- Session identifier must match candidate session allocation.
- Seat or computer assignment must match assigned resource when seat-level allocation exists.
- Current timestamp must fall within reporting-time to end-of-late-entry window.

**Workflow / states:** CredentialSubmitted → ValidatingCredential → ValidatingAllocation → ValidatingScheduleWindow → CheckingActivation → AwaitingActivation | SessionCreated → ReadyForPaperAssembly; any validation failure transitions to LoginDenied with immutable attempt log.

**Dependencies:**
- F06-005 Examination Credential Generation and Secure Distribution Handoff
- F06-003 Candidate Centre and Session Allocation
- F08-004 Candidate Examination Session Activation
- F03-004 Authorised Centre Access Restriction Configuration

**Risks:** Clock skew between centre clients and server may affect schedule window validation unless centrally synchronized.; Shared hall ticket exposure could allow credential use from wrong centre if centre enforcement in Feature 002 fails.

**Notes:** Consumes system-generated credentials from Module 06; does not generate credentials or hall tickets.

---

#### F09-002 — Authorised Centre Device and Network Enforcement

**One-liner / description:** Technically enforces that examination conduct occurs only from authorised examination centres, approved devices, and approved networks, validating at login and continuously during an active session with termination…

**Business objective:** Prevent candidates from taking examinations from home, personal devices, unauthorised networks, or centres other than their allotted authorised centre.

**Actors:** Candidate; Examination Centre/Invigilator User

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Client centre identifier; Device fingerprint attributes; Client IP address; Network segment metadata when available; Candidate examination conduct session identifier; Authorised centre restriction rules from Module 03

**Outputs:** Enforcement pass or fail decision; Access blocked reason code; Enforcement-bound session token; Reconnect warning state; Enforcement termination record; Enforcement event audit entries

**Business rules:**
- Examination access is denied when login centre cannot be resolved to an authorised active centre.
- Examination access is denied when resolved centre does not match candidate allotted centre.
- When centre device rules are configured, login device must match an approved centre device record.
- When centre network rules are configured, client network must match approved centre network ranges.
- Enforcement re-checks continue throughout active examination at configured interval.
- Transient network loss may allow grace period before session termination based on approved policy.
- Persistent enforcement failure terminates examination conduct session without manual submit.

**Validations:**
- Centre identifier must resolve to an active authorised examination centre.
- Resolved centre must equal candidate allotted centre identifier.
- Device fingerprint must match at least one approved centre device when device restriction enabled.
- Client IP must fall within approved centre network CIDR list when network restriction enabled.
- Enforcement token must remain bound to original device fingerprint for session lifetime when binding enabled.
- Re-validation interval must not be bypassed by client-side timer manipulation.

**Workflow / states:** CapturingContext → ValidatingCentre → ValidatingDevice → ValidatingNetwork → EnforcementPassed → ActiveMonitoring → TransientWarning | TerminatedEnforcement; login failure transitions to AccessBlocked.

**Dependencies:**
- F03-001 Authorised Examination Centre Master Lifecycle
- F03-004 Authorised Centre Access Restriction Configuration
- F03-002 Centre Capacity and Infrastructure Configuration
- F09-001 Examination Credential Login and Session Gate

**Risks:** Centre network reconfiguration on examination day may cause false enforcement failures.; Device fingerprint drift after browser update may require centre IT intervention.

**Notes:** Technical enforcement during login and continuously during active examination; complements centre restriction configuration in Module 03.

---

#### F09-003 — Dynamic Question Paper Assembly and Personalisation

**One-liner / description:** Assembles a unique immutable question paper for each candidate examination session by applying configured random selection rules, version assignment, question order randomisation, and answer option randomisation at…

**Business objective:** Deliver a fair, unpredictable, and auditably unique question paper per candidate while preserving examination integrity and immutability throughout the session.

**Actors:** Candidate

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Candidate examination conduct session identifier; Examination identifier; Random selection rules from Module 04; Multiple version and randomisation settings from Module 04; Approved question bank items from Module 04; Server-side random seed policy

**Outputs:** Assigned question paper version identifier; Ordered question list with randomised options; Frozen paper snapshot identifier; Assembly failure reason code; Assembly audit record

**Business rules:**
- Question paper is assembled once per candidate examination session.
- Assembled paper is immutable for the session lifetime.
- Random selection must satisfy all configured category count and difficulty rules.
- Version assignment follows configured multiple-version policy from Module 04.
- Re-login or refresh must not alter previously assigned paper content or order.
- Assembly failure blocks examination start until successful retry or administrator intervention.

**Validations:**
- Question pool must contain sufficient approved items for each required category.
- Selected questions must be in approved active status from question bank.
- Version assignment must reference a valid configured version slot.
- Randomisation must produce unique option mapping per question without empty option sets.
- Frozen snapshot must include question identifiers, order indices, and option mappings.
- Retry is blocked when session is already in in-progress or submitted state.

**Workflow / states:** AssemblyRequested → LoadingRules → SelectingQuestions → AssigningVersion → RandomisingOrder → RandomisingOptions → SnapshotPersisted → PaperReady; insufficient pool transitions to AssemblyFailed → RetryAssembly | AdministratorEscalation.

**Dependencies:**
- F04-005 Random Question Selection Rules
- F04-006 Multiple Question Paper Version and Randomisation Settings
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-001 Examination Credential Login and Session Gate

**Risks:** Insufficient pool depth may block examination start for late sessions if bank changes occur after scheduling.; Randomisation defects could cause duplicate exposure patterns detectable by candidates if seed policy is weak.

**Notes:** Runtime assembly only; question bank maintenance and rule configuration remain in Module 04.

---

#### F09-004 — Secure Examination Interface and Response Capture

**One-liner / description:** Provides the secure candidate examination interface for navigating assembled questions, capturing and auto-saving responses, displaying progress and remaining time, and preparing for submission confirmation.

**Business objective:** Enable candidates to complete examinations reliably with continuous response preservation, clear navigation, and secure interaction constraints during the active session.

**Actors:** Candidate

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Assembled question paper payload; Question identifier; Response value by question type; Mark-for-review flag; Client connectivity state; Session lock status

**Outputs:** Saved draft response records; Navigation summary counts; Auto-save status events; Offline queue recovery outcome; Read-only locked interface state

**Business rules:**
- Responses auto-save without requiring manual save action.
- Mark-for-review does not count as attempted unless a response exists.
- Clear response requires explicit confirmation.
- Interface becomes read-only immediately upon submission lock.
- Offline responses are queued client-side and replayed in order on reconnect.
- Navigation remains available unless session is locked or terminated.

**Validations:**
- Single-choice response must contain exactly one selected option identifier.
- Multiple-choice response must contain one or more valid option identifiers without duplicates.
- Numeric response must match configured numeric format and range when defined.
- Text response must not exceed configured maximum length.
- Response save rejected when session is locked or terminated.
- Question identifier must belong to session frozen paper snapshot.

**Workflow / states:** PaperReady → InProgress ↔ AutoSaving ↔ OfflineQueued → ReadyToSubmit; submission lock transitions to ResponseLocked read-only state.

**Dependencies:**
- F09-003 Dynamic Question Paper Assembly and Personalisation
- F04-002 Question Bank Item Lifecycle and Answer Key Management
- F09-006 Examination Session Security Controls

**Risks:** Extended offline period may cause response loss if queue exceeds client storage limits.; Large text responses may affect auto-save performance on low-spec centre hardware.

**Notes:** Candidate-facing examination UI; scoring and result display are out of scope.

---

#### F09-005 — Centrally Controlled Examination Timer

**One-liner / description:** Controls the official examination duration from a central server clock, displays remaining time to the candidate, warns on low time, stops the examination at expiry, and triggers automatic submission.

**Business objective:** Ensure uniform examination duration enforcement across all centres independent of client device clock manipulation.

**Actors:** Candidate

**User journey (10 steps):**
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

**Functional capabilities:**
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

**Inputs:** Examination duration from Module 04 configuration; Session official start timestamp; Current server timestamp; Client-reported local timestamp for drift detection; Low-time warning threshold configuration

**Outputs:** Remaining seconds value for client display; TimerExpired state transition; Auto-submission trigger event; Timer sync audit entries; Low-time warning display state

**Business rules:**
- Examination timer starts from official session start timestamp, not client login time, unless configured otherwise.
- Remaining time is calculated only on server; client display is advisory.
- Examination automatically stops at zero remaining time with no manual extension by candidate.
- Automatic submission is mandatory on timer expiry.
- Timer continues during brief offline periods using last known server sync plus elapsed server time.
- Invigilator manual time extension is out of scope in this module.

**Validations:**
- Timer initialisation requires valid examination duration greater than zero.
- Official start timestamp must be recorded before in-progress timer begins.
- Sync requests rejected for locked submitted or terminated sessions.
- Client drift beyond tolerance triggers forced resync without resetting remaining time.

**Workflow / states:** TimerInitialised → InProgress → LowTimeWarning → TimerExpired → AutoSubmitting → Submitted; drift detection loops ResyncDisplay without altering RemainingSeconds authority.

**Dependencies:**
- F04-004 Examination Master Configuration
- F09-004 Secure Examination Interface and Response Capture
- F09-008 Examination Submission and Response Locking

**Risks:** Server clock issues could affect all concurrent sessions simultaneously.; Auto-submit at expiry during unsaved response may lose last unsynced client draft if offline queue exhausted.

**Notes:** Server-authoritative timer; auto-submission handoff to Feature 008 on expiry.

---

#### F09-006 — Examination Session Security Controls

**One-liner / description:** Enforces examination security controls including single active session per candidate, browser and session restrictions as approved, focus and visibility monitoring, and forced termination on critical violations.

**Business objective:** Reduce examination malpractice risk by preventing concurrent sessions and detecting disallowed client behaviour during conduct.

**Actors:** Candidate; Examination Centre/Invigilator User

**User journey (10 steps):**
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

**Functional capabilities:**
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

**Inputs:** Candidate examination conduct session identifier; Client browser session fingerprint; Tab visibility state events; Window focus state events; Approved security policy configuration; Violation threshold configuration

**Outputs:** Active session registry entry; Concurrent login rejection response; Security violation events; Warning banner state; TerminatedSecurity session state; Security termination reason code

**Business rules:**
- Only one active examination conduct session is permitted per candidate attempt at a time.
- Second login attempt is blocked unless policy explicitly allows session takeover.
- Approved browser restrictions are enforced for entire in-progress session.
- Focus and tab visibility violations accumulate toward termination threshold.
- Critical violation immediate termination applies when configured for specific event types.
- Security termination locks responses and prevents manual submit without invigilator escalation path defined out of scope.

**Validations:**
- Session token must match registered active token for request processing.
- Browser session fingerprint must match bound fingerprint when binding enabled.
- Concurrent session check compares candidate attempt identifier not merely credential.
- Violation count resets only on new attempt not mid-session refresh.
- Security events rejected when session already submitted or terminated.

**Workflow / states:** SessionRegistered → SecuredChrome → Monitoring → WarningIssued → TerminatedSecurity; concurrent login attempt transitions to ConcurrentSessionBlocked.

**Dependencies:**
- F04-004 Examination Master Configuration
- F09-001 Examination Credential Login and Session Gate
- F09-007 Examination Activity Recording
- F08-005 Centre Live Examination Session Monitoring

**Risks:** False positives from legitimate invigilator interactions may trigger warnings if policy thresholds are too aggressive.; Browser compatibility gaps may limit effectiveness of specific restrictions.

**Notes:** Implements approved browser and session restrictions; standalone audit-log product is out of scope.

---

#### F09-007 — Examination Activity Recording

**One-liner / description:** Records a comprehensive examination activity trail including login, start, response saves, navigation, version assignment, centre and device context, abnormal events, and submission timestamps for audit and monitoring.

**Business objective:** Provide defensible examination conduct evidence for dispute resolution, monitoring, and downstream administration reporting without relying on a separate audit product.

**Actors:** Candidate; Examination Centre/Invigilator User

**User journey (11 steps):**
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

**Functional capabilities:**
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

**Inputs:** Examination conduct session identifier; Event type code; Event timestamp; Question identifier when applicable; Response snapshot hash when applicable; Paper version identifier; Centre device network snapshots; Abnormal event classification

**Outputs:** Append-only activity event records; Abnormal event flags for centre monitoring; Activity timeline query results for audit consumers; Response change history references

**Business rules:**
- All material examination conduct actions generate an activity event.
- Activity events are append-only and cannot be edited or deleted by candidates.
- Response activity stores content hash or reference not necessarily full text for large entries per policy.
- Abnormal events include security violations, enforcement failures, and repeated auto-save errors.
- Activity recording continues until session reaches terminal submitted or terminated state.
- Activity data is retained per platform retention policy for examination records.

**Validations:**
- Event timestamp must be server-generated or server-validated.
- Session identifier must exist and be in non-terminal state except for terminal event recording.
- Question identifier must belong to session frozen paper for question-scoped events.
- Event type must be from approved examination activity catalogue.
- Query access restricted to authorised roles via Module 01 authorization hooks.

**Workflow / states:** EventIngested → Appended → AvailableForMonitoring → ArchivedPerRetention; abnormal classification triggers AbnormalFlagged substate visible to Module 08.

**Dependencies:**
- F09-001 Examination Credential Login and Session Gate
- F09-002 Authorised Centre Device and Network Enforcement
- F09-003 Dynamic Question Paper Assembly and Personalisation
- F09-004 Secure Examination Interface and Response Capture
- F09-006 Examination Session Security Controls
- F09-008 Examination Submission and Response Locking
- F01-006 Downstream Module Authorization Integration Hooks

**Risks:** High-volume navigation logging may increase storage costs for large candidate counts.; Incomplete event ingestion during server outage may create audit gaps.

**Notes:** Records conduct audit trail; standalone audit-log product and scoring are out of scope.

---

#### F09-008 — Examination Submission and Response Locking

**One-liner / description:** Supports manual candidate submission with review and confirmation as well as automatic submission on timer expiry or approved termination paths, locking all responses upon submission completion.

**Business objective:** Finalise candidate examination attempts with immutable response locking suitable for downstream evaluation while giving candidates clear submission confirmation.

**Actors:** Candidate

**User journey (12 steps):**
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

**Functional capabilities:**
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

**Inputs:** Candidate examination conduct session identifier; Current draft responses; Submission trigger type manual automatic or termination; Session timer state; Session security or enforcement termination state

**Outputs:** Submission record with type and timestamp; Final locked response snapshot; Submission receipt metadata for candidate display; Response lock flags; Evaluation handoff readiness status

**Business rules:**
- Manual submission requires explicit candidate confirmation.
- Unattempted question warning is informational; submission may proceed if candidate confirms.
- Automatic submission on timer expiry does not require candidate confirmation.
- Once submitted, responses are immutable for the attempt.
- Double submission attempts are idempotent returning existing submission receipt.
- Submission blocked when session already terminated for enforcement unless policy allows salvage submit.
- Evaluation handoff occurs only after successful submission persistence.

**Validations:**
- Submission rejected when session not in in-progress or timer-expired eligible state.
- Submission rejected when responses already locked.
- Final snapshot must include all saved draft responses at lock time.
- Submission receipt must include session identifier submission timestamp and type.
- Retry allowed only when prior submit attempt did not persist lock record.

**Workflow / states:** ReadyToSubmit → ReviewSummary → ConfirmSubmit → LockingResponses → PersistingFinal → Submitted; timer expiry transitions TimerExpired → AutoSubmitting → Submitted; transient failure transitions to SubmitFailed → RetrySubmit.

**Dependencies:**
- F09-004 Secure Examination Interface and Response Capture
- F09-005 Centrally Controlled Examination Timer
- F09-007 Examination Activity Recording
- F10-001 Evaluation and Results
- F07-003 Examination Lifecycle Event Subscription and Template Routing

**Risks:** Partial lock during server failure could leave ambiguous state without idempotent retry design.; Auto-submit at expiry with pending offline drafts may submit last synced state only.

**Notes:** Manual and automatic submission; scoring in Module 10 is out of scope but locked responses must be handoff-ready.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 09 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 09 Secure Examination Conduct** (8 features).
> Features: F09-001 Examination Credential Login and Session Gate; F09-002 Authorised Centre Device and Network Enforcement; F09-003 Dynamic Question Paper Assembly and Personalisation; F09-004 Secure Examination Interface and Response Capture; F09-005 Centrally Controlled Examination Timer; F09-006 Examination Session Security Controls; F09-007 Examination Activity Recording; F09-008 Examination Submission and Response Locking.
> Purpose: Secure centre-based exam conduct: credential login, device/network enforcement, dynamic paper assembly, response capture, timer, security controls, activity log, submission lock.
> Draw: Credential login + network/device enforcement sequence; Paper assembly / randomisation sequence (preserve answer key); Timer + heartbeat + autosave architecture; Security violation threshold → terminate flowchart; ERD for `exam_attempt (conduct fields)`, `paper_instance`, `paper_instance_item`, `exam_response`, `exam_activity_event`, `access_denial_log`.
