# ChatGPT Visualization Brief — Module 08: Centre Operations

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 08 Centre Operations
**Features:** 5 (F08-001 … F08-005)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 08 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Exam-day centre ops swimlane (dashboard → register → verify → activate → monitor)
2. Attendance/verification state machine with correction rules
3. Activation eligibility gate diagram
4. Live monitor metrics from exam_attempt
5. Feature relationship / dependency graph within this module and to other modules
6. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Centre Operations
**Purpose:** Centre exam-day operations: dashboard, scheduled candidate register, identity verification and attendance, session activation, live monitoring.

**Actors (union across features):**
- Examination Centre/Invigilator User

**Feature list:**
- **F08-001** — Centre Examination Day Dashboard
- **F08-002** — Centre Scheduled Candidate Register
- **F08-003** — Candidate Identity Verification and Attendance Marking
- **F08-004** — Candidate Examination Session Activation
- **F08-005** — Centre Live Examination Session Monitoring

### DATA MODEL (from EXAM DB design v2.1)

- `exam_attempt (attendance/activation fields)`
- `attendance_event`
- `centre_ops_snapshot`

### FEATURE CATALOGUE

#### F08-001 — Centre Examination Day Dashboard

**One-liner / description:** Centre-scoped landing dashboard for invigilators showing today's and upcoming scheduled examination sessions for the logged-in authorised centre, with operational counts for registered candidates, attendance,…

**Business objective:** Give examination centre invigilators a single operational view at the start of examination day so they can prioritise verification, attendance, activation, and monitoring tasks without accessing department-wide administration data.

**Actors:** Examination Centre/Invigilator User

**User journey (12 steps):**
1. Invigilator logs in through centre-scoped staff authentication and lands on the Centre Examination Day Dashboard.
2. System resolves the invigilator's assigned authorised centre and loads only that centre's data.
3. Invigilator reviews today's examination session cards showing examination name, session slot, scheduled start time, and high-level status.
4. Invigilator reviews aggregate widgets showing total scheduled candidates, present count, verified count, activated count, and not-yet-arrived count per session.
5. Invigilator reviews session status chips showing counts in scheduled, verification-in-progress, activation-ready, in-progress, and completed states.
6. Invigilator scans the upcoming examination timeline for the next seven days to prepare staffing and logistics.
7. Invigilator selects a session card or quick-link to open the Scheduled Candidate Register filtered to that session.
8. Invigilator selects quick-link to Candidate Verification queue for the active session.
9. Invigilator selects quick-link to Session Activation list for the active session.
10. Invigilator selects quick-link to Live Session Monitoring when examinations are underway.
11. If no sessions are scheduled today, invigilator sees an empty-state message with upcoming session preview only.
12. If summary data fails to load, invigilator sees an error state with retry action.

**Functional capabilities:**
- Display today examination session cards scoped to logged-in centre
- Display upcoming examination timeline for next seven days at centre
- Display per-session scheduled candidate count aggregate
- Display per-session present attendance count aggregate
- Display per-session identity verified count aggregate
- Display per-session session activated count aggregate
- Display session status distribution chips for scheduled through completed states
- Provide quick navigation to candidate register filtered by session
- Provide quick navigation to verification queue for selected session
- Provide quick navigation to activation list for selected session
- Provide quick navigation to live monitoring view for in-progress session
- Show empty state when no examinations scheduled today at centre

**Inputs:** Logged-in invigilator user identity and centre assignment; Examination schedule and session slot dates from scheduling module; Centre candidate allocation records for logged-in centre; Candidate attendance marks for today's sessions; Candidate identity verification records for today's sessions; Candidate session activation records for today's sessions; Live examination session status from secure conduct module

**Outputs:** Today session summary cards with operational counts; Upcoming session timeline list; Session status distribution summary; Navigation context to downstream centre operational screens

**Business rules:**
- Dashboard data must be limited to the invigilator's assigned authorised examination centre only
- Only scheduled examination sessions allocated to the centre appear on the dashboard
- Counts reflect candidates allocated to the centre for each session regardless of other centres
- Activation and monitoring counts include only candidates in centre allocation for the session
- Upcoming timeline excludes sessions more than seven days in the future
- Completed session status applies when all allocated candidates have reached submitted or completed conduct state or session end time has passed per examination configuration

**Validations:**
- Reject dashboard request when invigilator has no active centre assignment
- Reject dashboard request when invigilator centre assignment is inactive
- Validate requested date range parameters are not malformed
- Validate session identifier in drill-down navigation belongs to logged-in centre

**Workflow / states:** Dashboard load: AUTHENTICATED -> CENTRE_RESOLVED -> SUMMARY_LOADED | SUMMARY_EMPTY | SUMMARY_ERROR. Session card drill-down: CARD_SELECTED -> REGISTER_FILTERED | VERIFICATION_QUEUE | ACTIVATION_LIST | MONITORING_VIEW.

**Dependencies:**
- F01 centre-scoped invigilator account lifecycle and authentication session
- F03 authorised examination centre master and invigilator user assignment to centre
- F06 examination schedule creation and candidate centre session allocation
- F09 secure examination conduct session state for in-progress monitoring counts

**Risks:** Stale conduct module status may cause monitoring count lag without refresh interval agreement; High candidate volume per session may require aggregate query optimisation; Partial upstream data availability could produce incomplete widget counts

---

#### F08-002 — Centre Scheduled Candidate Register

**One-liner / description:** Centre-scoped searchable register of candidates scheduled and allocated to the logged-in examination centre, showing registration identity, hall ticket reference, session slot, and operational status flags for…

**Business objective:** Enable invigilators to locate and review every candidate expected at their centre for a given examination session before verification, attendance marking, and session activation activities begin.

**Actors:** Examination Centre/Invigilator User

**User journey (13 steps):**
1. Invigilator opens Scheduled Candidate Register from dashboard or main navigation.
2. System loads paginated list of candidates allocated to invigilator's centre defaulting to today's sessions.
3. Invigilator selects examination name filter to narrow the register.
4. Invigilator selects session slot filter to narrow to one examination session.
5. Invigilator enters registration number, candidate name fragment, or hall ticket number in search bar.
6. System returns matching centre-allocated candidates only.
7. Invigilator applies verification status filter to find pending verifications.
8. Invigilator applies attendance status filter to find not-yet-marked candidates.
9. Invigilator applies activation status filter to find verified present but not activated candidates.
10. Invigilator clicks a candidate row to open read-only detail drawer with registration snapshot, allocated seat or computer if assigned, and current operational flags.
11. Invigilator initiates export action to download CSV day sheet for selected session filter.
12. Invigilator confirms export dialog and receives CSV file.
13. If session has zero allocated candidates, invigilator sees empty-state guidance to verify schedule and allocation.

**Functional capabilities:**
- List paginated scheduled candidates allocated to logged-in centre
- Default register view to today sessions at centre
- Search candidates by registration number
- Search candidates by candidate name partial match
- Search candidates by hall ticket number
- Filter register by examination name
- Filter register by session slot
- Filter register by identity verification status
- Filter register by attendance status
- Filter register by session activation status
- Open read-only candidate schedule detail drawer
- Show empty state when session has zero centre-allocated candidates

**Inputs:** Centre allocation records from scheduling module; Candidate registration profile fields from registration module; Hall ticket reference from scheduling module; Seat or computer assignment when configured in scheduling module; Verification attendance activation status from centre operations records

**Outputs:** Paginated candidate register list with operational status columns; Candidate detail drawer content; CSV export file of filtered register rows

**Business rules:**
- Register includes only candidates with centre allocation matching logged-in centre
- Candidates allocated to other centres never appear in register results
- Hall ticket number displayed only for candidates allocated to viewing centre
- Export includes only rows matching active filter set and centre scope
- Register is read-only; status changes occur in verification attendance activation features

**Validations:**
- Reject list request when invigilator centre assignment missing or inactive
- Validate pagination page size within allowed maximum
- Validate examination filter identifier belongs to scheduled sessions at centre
- Validate session slot filter belongs to logged-in centre schedule
- Validate search registration number format when provided
- Validate hall ticket number format when provided
- Reject export when result set exceeds configured export row limit with user message

**Workflow / states:** Register view: OPEN -> LOAD_DEFAULT -> FILTERED | SEARCHED -> DETAIL_DRAWER_OPEN. Export: EXPORT_REQUESTED -> EXPORT_CONFIRMED -> CSV_DOWNLOADED.

**Dependencies:**
- F06 candidate centre and session allocation
- F06 digital hall ticket generation and candidate access reference
- F06 candidate seat and computer assignment when seat assignment configured
- F05 candidate registration profile data for register display

**Risks:** Late allocation changes after invigilator prints CSV day sheet may cause on-floor mismatch; Large sessions may require pagination performance tuning

---

#### F08-003 — Candidate Identity Verification and Attendance Marking

**One-liner / description:** Invigilator workflows at the examination centre to verify candidate identity against registration records, reject verification with documented reason when identity cannot be confirmed, mark candidate attendance as…

**Business objective:** Ensure only identity-confirmed and physically present candidates at the authorised centre proceed to examination session activation, creating an auditable pre-examination record for each allocated candidate.

**Actors:** Examination Centre/Invigilator User

**User journey (16 steps):**
1. Invigilator opens Candidate Verification queue for a selected centre session.
2. System lists centre-allocated candidates with verification status UNVERIFIED or REJECTED at top of queue.
3. Invigilator selects a candidate row to open verification detail screen.
4. Invigilator compares displayed registration name, registration number, photograph if available, category, and hall ticket reference against candidate physical ID and hall ticket document.
5. Invigilator confirms identity and selects Mark Verified action.
6. System prompts confirmation dialog; invigilator confirms.
7. System transitions candidate verification status to VERIFIED with invigilator and timestamp audit.
8. Alternatively invigilator selects Reject Verification, enters mandatory rejection reason, and confirms.
9. System transitions candidate verification status to REJECTED and records reason.
10. Invigilator returns to queue or opens attendance action for verified candidate.
11. Invigilator selects Mark Present for candidate who has arrived; system records PRESENT with timestamp.
12. For candidate who did not arrive, invigilator selects Mark Absent, enters mandatory absent reason, and confirms.
13. System records ABSENT status blocking downstream activation.
14. If invigilator marked attendance incorrectly, invigilator opens attendance correction dialog, selects corrected status, enters mandatory correction reason, and confirms.
15. System writes correction audit entry preserving prior mark history.
16. When all candidates processed, queue shows empty state with counts of verified rejected present absent.

**Functional capabilities:**
- List candidate verification queue for centre session ordered by pending status
- Display candidate verification detail with registration identity snapshot fields
- Mark candidate identity verified with invigilator audit stamp
- Reject candidate verification with mandatory rejection reason
- Display verification status badge on candidate rows
- Mark candidate attendance present with session timestamp
- Mark candidate attendance absent with mandatory absent reason
- Correct attendance mark with mandatory correction reason and audit history
- Display attendance status badge on candidate rows
- Show verification queue empty state when no pending candidates remain

**Inputs:** Centre-allocated candidate list for session; Candidate registration identity snapshot name registration number category photograph reference; Hall ticket reference from scheduling module; Invigilator user identity for audit; Rejection reason text or selected reason code; Absent reason text or selected reason code; Attendance correction reason text

**Outputs:** Updated verification status VERIFIED or REJECTED per candidate; Verification rejection reason record; Updated attendance status PRESENT or ABSENT per candidate; Attendance correction audit history entries; Updated operational flags visible in register and activation eligibility

**Business rules:**
- Verification and attendance actions allowed only for candidates allocated to invigilator's centre for the session
- Verification can be marked only while session is in pre-start operational window per examination schedule
- Rejected verification prevents session activation for that candidate
- Absent attendance prevents session activation for that candidate
- Present attendance requires prior VERIFIED status before activation eligibility evaluation
- Attendance correction allowed only before candidate session activation
- Each verification and attendance change records invigilator user and timestamp
- Re-verification after VERIFIED requires supervisor policy if platform configures lock after verify

**Validations:**
- Reject verification action when candidate not allocated to logged-in centre
- Reject verify when session not in allowed pre-start window
- Reject rejection submission when rejection reason is blank or below minimum length
- Reject present mark when candidate verification status is REJECTED
- Reject absent reason submission when absent reason is blank or below minimum length
- Reject attendance correction when candidate session already ACTIVATED
- Reject attendance correction when correction reason is blank
- Reject duplicate verify when candidate already VERIFIED unless correction policy enabled

**Workflow / states:** Verification: UNVERIFIED -> VERIFIED | REJECTED. Attendance: UNMARKED -> PRESENT | ABSENT. Correction: PRESENT <-> ABSENT with audit before ACTIVATED.

**Dependencies:**
- F08-002 centre scheduled candidate register for candidate selection context
- F05 candidate registration profile and confirmation data
- F06 candidate centre session allocation and hall ticket reference
- F01 invigilator authentication and centre-scoped authorization

**Risks:** Incorrect manual verification could allow wrong candidate activation without biometric enforcement; Concurrent invigilator actions on same candidate require optimistic locking; Attendance correction disputes require clear audit history for administration review

---

#### F08-004 — Candidate Examination Session Activation

**One-liner / description:** Centre invigilator activation of eligible candidate examination sessions immediately prior to examination start, enforcing registration completeness, fee compliance, schedule allocation, centre assignment, physical…

**Business objective:** Allow authorised centre staff to start candidate examination sessions only for candidates who meet all pre-examination eligibility conditions, handing activated sessions to secure examination conduct without re-entering registration or scheduling data.

**Actors:** Examination Centre/Invigilator User

**User journey (14 steps):**
1. Invigilator opens Session Activation list for selected centre examination session.
2. System displays centre-allocated candidates with eligibility indicator per row.
3. Invigilator filters list to show only activation-ready candidates.
4. Invigilator selects a candidate row to open activation detail with eligibility checklist.
5. Invigilator reviews checklist items: registration complete, fee compliant, scheduled for session, allocated to this centre, attendance PRESENT, verification VERIFIED, session not already activated.
6. For eligible candidate invigilator selects Activate Session action.
7. System shows confirmation dialog with candidate name and examination name.
8. Invigilator confirms activation.
9. System transitions activation status to ACTIVATED, records invigilator and timestamp, and sends handoff to secure examination conduct module.
10. For ineligible candidate invigilator views blocked detail panel listing each failed rule with plain-language reason.
11. Invigilator switches to batch activation screen, multi-selects eligible candidates, and submits batch activate.
12. System processes each candidate, activates eligible rows, and reports per-row success or block reason for failures.
13. Invigilator refreshes list to see updated activation statuses.
14. If no verified present candidates remain, empty state displays guidance to complete verification and attendance first.

**Functional capabilities:**
- List centre-allocated candidates with activation eligibility indicator
- Filter activation list to activation-ready candidates only
- Display activation detail eligibility checklist for single candidate
- Evaluate registration complete flag for candidate
- Evaluate fee compliance flag for candidate
- Evaluate scheduled session match for candidate
- Evaluate centre allocation match for logged-in centre
- Evaluate attendance PRESENT requirement
- Evaluate identity VERIFIED requirement
- Activate single candidate examination session with audit
- Batch activate multiple eligible candidate examination sessions
- Return activation block reasons for ineligible candidate

**Inputs:** Candidate registration completion status from registration module; Candidate fee payment compliance status from fee management; Examination schedule and session allocation from scheduling module; Centre allocation record for candidate; Verification status from centre verification records; Attendance status from centre attendance records; Invigilator user identity; Batch candidate selection list

**Outputs:** Activation status ACTIVATED for eligible candidates; Activation event with invigilator timestamp and eligibility snapshot; Handoff signal to secure examination conduct for credential session readiness; Per-candidate block reason list for ineligible candidates; Batch activation result summary with success and failure counts

**Business rules:**
- Activation permitted only for candidates allocated to invigilator's authorised centre
- Candidate registration must be complete and confirmed
- Candidate fee must be compliant including free first-attempt and paid subsequent rules where applicable
- Candidate must be scheduled for the selected examination session
- Candidate attendance must be PRESENT
- Candidate verification must be VERIFIED
- Already ACTIVATED candidates cannot be activated again
- REJECTED verification or ABSENT attendance permanently blocks activation for that session unless attendance corrected before activation

**Validations:**
- Reject activation when candidate not centre-allocated to logged-in centre
- Reject activation when registration status incomplete
- Reject activation when fee compliance flag false
- Reject activation when candidate not scheduled for requested session
- Reject activation when attendance not PRESENT
- Reject activation when verification not VERIFIED
- Reject activation when session already ACTIVATED
- Reject activation outside allowed pre-start time window

**Workflow / states:** Activation eligibility: INACTIVE -> ELIGIBILITY_EVALUATED -> ELIGIBLE | BLOCKED. Activation execution: ELIGIBLE -> ACTIVATE_CONFIRMED -> ACTIVATED -> HANDOFF_TO_CONDUCT.

**Dependencies:**
- F08-003 candidate identity verification and attendance marking statuses
- F05 registration confirmation and fee compliance determination
- F02 payment gateway fee transaction integration for paid registrations
- F06 examination schedule centre allocation and examination credentials handoff
- F09 secure examination conduct to receive activated session

**Risks:** Partial batch failure may cause invigilator confusion without clear per-row feedback; Handoff failure after local ACTIVATED record requires reconciliation procedure; Clock skew between centre client and server may affect pre-start window validation

**Notes:** Activation limited to registered fee-compliant scheduled centre-allocated present verified candidates per SOW centre-level activation rules.

---

#### F08-005 — Centre Live Examination Session Monitoring

**One-liner / description:** Real-time centre-scoped monitoring view for invigilators to track examination progress of activated candidates through started, active, submitted, and completed conduct states during an in-progress session, with…

**Business objective:** Enable invigilators to supervise examination progress at their centre, identify candidates who have not started or submitted within expected timelines, and confirm session completion counts without accessing question content or department-wide analytics.

**Actors:** Examination Centre/Invigilator User

**User journey (12 steps):**
1. Invigilator opens Live Session Monitoring from dashboard or navigation.
2. Invigilator selects in-progress examination session at their centre.
3. System loads monitoring landing screen with aggregate header counts for not-started, started, active, submitted, and completed candidates.
4. Invigilator reviews candidate status grid with one row per activated centre-allocated candidate.
5. Invigilator identifies candidates still in not-started column after activation.
6. Invigilator selects grid row to open read-only drill-down showing session start time, last activity timestamp, current conduct status, and submission timestamp if submitted.
7. Invigilator triggers manual refresh to pull latest status from conduct module.
8. Invigilator optionally enables auto-refresh interval to keep grid current during examination.
9. System displays abnormal session alert banner when candidate remains in started state without activity beyond configured threshold.
10. Invigilator continues monitoring until all candidates reach submitted or completed state.
11. Invigilator opens session end summary read-only screen showing final completion counts.
12. If no candidates activated yet, monitoring shows empty state directing invigilator to activation feature.

**Functional capabilities:**
- Select in-progress centre examination session for monitoring
- Display monitoring aggregate header counts by conduct status
- Display candidate status grid with not-started started active submitted completed columns
- Open read-only candidate live session drill-down detail panel
- Manual refresh monitoring data on demand
- Configure auto-refresh interval for monitoring grid
- Display abnormal session alert banner for stuck inactive candidates
- Display monitoring empty state before first activation
- Display session end summary read-only screen with final counts

**Inputs:** Centre-allocated activated candidate list; Live examination conduct session status from secure conduct module; Session start and end times from examination schedule; Last activity timestamps from conduct activity recording; Abnormal idle threshold from examination configuration

**Outputs:** Live status grid per activated candidate; Aggregate status counts header; Candidate drill-down session progress detail; Session end completion summary counts; Abnormal session alert indicators

**Business rules:**
- Monitoring includes only candidates activated at logged-in centre for selected session
- Non-activated candidates appear in not-started or excluded per monitoring configuration agreed with conduct module
- Question content and candidate answers are never displayed in monitoring views
- Status values map to conduct module states: NOT_STARTED, STARTED, ACTIVE, SUBMITTED, COMPLETED
- Abnormal alert triggers when candidate in STARTED state exceeds idle threshold without transition to ACTIVE
- Monitoring read-only; invigilator cannot modify conduct state from this feature
- Session end summary available when session end time reached or all candidates submitted or completed

**Validations:**
- Reject monitoring request when session not allocated to logged-in centre
- Reject monitoring request when invigilator lacks centre monitoring permission
- Validate selected session identifier belongs to centre schedule
- Validate auto-refresh interval within allowed minimum and maximum seconds

**Workflow / states:** Conduct status progression monitored: NOT_STARTED -> STARTED -> ACTIVE -> SUBMITTED -> COMPLETED. Monitoring view: SESSION_SELECTED -> GRID_LOADED -> REFRESHED -> SESSION_END_SUMMARY.

**Dependencies:**
- F08-004 candidate examination session activation producing ACTIVATED candidates
- F09 secure examination conduct session states and activity recording
- F06 examination schedule session timing
- F04 examination master configuration for session parameters

**Risks:** Polling lag may delay abnormal alert visibility; Conduct module downtime would leave monitoring grid stale with no status updates; Definition of SUBMITTED versus COMPLETED for summary counts must align with conduct module

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 08 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 08 Centre Operations** (5 features).
> Features: F08-001 Centre Examination Day Dashboard; F08-002 Centre Scheduled Candidate Register; F08-003 Candidate Identity Verification and Attendance Marking; F08-004 Candidate Examination Session Activation; F08-005 Centre Live Examination Session Monitoring.
> Purpose: Centre exam-day operations: dashboard, scheduled candidate register, identity verification and attendance, session activation, live monitoring.
> Draw: Exam-day centre ops swimlane (dashboard → register → verify → activate → monitor); Attendance/verification state machine with correction rules; Activation eligibility gate diagram; Live monitor metrics from exam_attempt; ERD for `exam_attempt (attendance/activation fields)`, `attendance_event`, `centre_ops_snapshot`.
