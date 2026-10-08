# Module 08: Centre Operations

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 5 (F08-001 … F08-005)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 08 Centre Operations

659.5 hours · 104 tasks · Business

Examination-day centre dashboard and invigilator workflows for candidate verification, session activation, and monitoring.

### F08-001 Centre Examination Day Dashboard

108.75 hours · Go-live · 19 tasks

##### Description

Centre-scoped landing dashboard for invigilators showing today's and upcoming scheduled examination sessions for the logged-in authorised centre, with operational counts for registered candidates, attendance, identity verification, session activation, and in-progress session status distribution.

##### Business objective

Give examination centre invigilators a single operational view at the start of examination day so they can prioritise verification, attendance, activation, and monitoring tasks without accessing department-wide administration data.

##### Actors

- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

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
- Show error and retry state when dashboard summary load fails

##### Inputs

- Logged-in invigilator user identity and centre assignment
- Examination schedule and session slot dates from scheduling module
- Centre candidate allocation records for logged-in centre
- Candidate attendance marks for today's sessions
- Candidate identity verification records for today's sessions
- Candidate session activation records for today's sessions
- Live examination session status from secure conduct module

##### Outputs

- Today session summary cards with operational counts
- Upcoming session timeline list
- Session status distribution summary
- Navigation context to downstream centre operational screens

##### Business rules

- Dashboard data must be limited to the invigilator's assigned authorised examination centre only
- Only scheduled examination sessions allocated to the centre appear on the dashboard
- Counts reflect candidates allocated to the centre for each session regardless of other centres
- Activation and monitoring counts include only candidates in centre allocation for the session
- Upcoming timeline excludes sessions more than seven days in the future
- Completed session status applies when all allocated candidates have reached submitted or completed conduct state or session end time has passed per examination configuration

##### Validations

- Reject dashboard request when invigilator has no active centre assignment
- Reject dashboard request when invigilator centre assignment is inactive
- Validate requested date range parameters are not malformed
- Validate session identifier in drill-down navigation belongs to logged-in centre

##### Calculations

- Scheduled candidate count equals count of centre-allocated candidates for session
- Present count equals centre-allocated candidates with attendance status PRESENT
- Verified count equals centre-allocated candidates with verification status VERIFIED
- Activated count equals centre-allocated candidates with activation status ACTIVATED
- Not-yet-arrived count equals scheduled minus present minus explicitly marked absent
- In-progress session count equals sessions with at least one activated candidate and session end not reached

##### Workflow

Dashboard load: AUTHENTICATED -> CENTRE_RESOLVED -> SUMMARY_LOADED | SUMMARY_EMPTY | SUMMARY_ERROR. Session card drill-down: CARD_SELECTED -> REGISTER_FILTERED | VERIFICATION_QUEUE | ACTIVATION_LIST | MONITORING_VIEW.

##### Search requirements

- No free-text search on dashboard; filtering is by today default and upcoming date window only

##### Security

- Centre-scoped data isolation enforced on every dashboard aggregate query
- Invigilator role permission required to access centre operations dashboard
- No candidate PII beyond counts and session labels on dashboard widgets
- Audit log entry for dashboard access optional at platform policy level

##### Integrations

- Staff authentication and centre assignment resolution from Module 01 User and Role Management
- Examination schedule and centre allocation read from Module 06 Examination Scheduling and Allocation
- Live session status counts read from Module 09 Secure Examination Conduct

##### Dependencies

- F01 centre-scoped invigilator account lifecycle and authentication session
- F03 authorised examination centre master and invigilator user assignment to centre
- F06 examination schedule creation and candidate centre session allocation
- F09 secure examination conduct session state for in-progress monitoring counts

##### Assumptions

- Invigilator users are assigned to exactly one active centre for examination-day operations
- Schedule and allocation data is finalised before examination day dashboard use
- Dashboard aggregates are read-only operational views over upstream module data
- Seven-day upcoming window is sufficient for centre planning without department analytics

##### Risks

- Stale conduct module status may cause monitoring count lag without refresh interval agreement
- High candidate volume per session may require aggregate query optimisation
- Partial upstream data availability could produce incomplete widget counts

##### Non-functional requirements

- Dashboard summary should load within acceptable enterprise web response time for up to 500 allocated candidates per session
- Dashboard must remain usable on standard centre desktop browsers
- Widget counts must be consistent with downstream register and queue screens for same session

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre dashboard landing screen with today examination session cards | Medium | 16 |
| UI | Dashboard empty state when no examinations scheduled today | Simple | 5 |
| UI | Dashboard error state with retry action for failed summary load | Simple | 5 |
| UI | Session status summary widget with scheduled through completed count chips | Medium | 16 |
| UI | Candidate operational count widget for scheduled present verified activated | Medium | 16 |
| UI | Upcoming examination timeline panel for next seven days | Easy | 14 |
| UI | Quick navigation panel to register verification activation monitoring screens | Simple | 5 |
| API | Get centre-scoped today examination sessions summary | Medium | 6 |
| API | Get centre-scoped upcoming examination sessions list by date window | Medium | 6 |
| API | Get centre dashboard attendance aggregate counts by session | Complex | 8 |
| API | Get centre session status distribution counts for dashboard widgets | Medium | 6 |
| Database | Centre date session summary query indexes for dashboard aggregates | Easy | 0.25 |
| Database | Operational status aggregate read model over schedule allocation attendance verification activation | Medium | 0.3 |
| Integration | Resolve invigilator assigned centre scope from authorization service | Simple | 4 |
| Testing | Happy path dashboard metrics for multi-session examination day | Medium | 0.3 |
| Testing | Centre isolation prevents cross-centre dashboard data exposure | Medium | 0.3 |
| Testing | Empty schedule and zero-count widget edge cases | Easy | 0.25 |
| Documentation | Invigilator dashboard interpretation user runbook | Easy | 0.25 |
| Documentation | Centre scoping technical notes for dashboard aggregate queries | Simple | 0.1 |

### F08-002 Centre Scheduled Candidate Register

105.6 hours · Go-live · 18 tasks

##### Description

Centre-scoped searchable register of candidates scheduled and allocated to the logged-in examination centre, showing registration identity, hall ticket reference, session slot, and operational status flags for verification, attendance, and activation without exposing candidates allocated to other centres.

##### Business objective

Enable invigilators to locate and review every candidate expected at their centre for a given examination session before verification, attendance marking, and session activation activities begin.

##### Actors

- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

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
- Export filtered register to CSV day sheet

##### Inputs

- Centre allocation records from scheduling module
- Candidate registration profile fields from registration module
- Hall ticket reference from scheduling module
- Seat or computer assignment when configured in scheduling module
- Verification attendance activation status from centre operations records

##### Outputs

- Paginated candidate register list with operational status columns
- Candidate detail drawer content
- CSV export file of filtered register rows

##### Business rules

- Register includes only candidates with centre allocation matching logged-in centre
- Candidates allocated to other centres never appear in register results
- Hall ticket number displayed only for candidates allocated to viewing centre
- Export includes only rows matching active filter set and centre scope
- Register is read-only; status changes occur in verification attendance activation features

##### Validations

- Reject list request when invigilator centre assignment missing or inactive
- Validate pagination page size within allowed maximum
- Validate examination filter identifier belongs to scheduled sessions at centre
- Validate session slot filter belongs to logged-in centre schedule
- Validate search registration number format when provided
- Validate hall ticket number format when provided
- Reject export when result set exceeds configured export row limit with user message

##### Workflow

Register view: OPEN -> LOAD_DEFAULT -> FILTERED | SEARCHED -> DETAIL_DRAWER_OPEN. Export: EXPORT_REQUESTED -> EXPORT_CONFIRMED -> CSV_DOWNLOADED.

##### Search requirements

- Partial match search on candidate name case-insensitive
- Exact or prefix match on registration number
- Exact match on hall ticket number
- Combined search with examination session verification attendance activation filters

##### Documents

- CSV day sheet export of scheduled candidate register

##### Security

- Centre-scoped query enforcement on all list search filter export operations
- Invigilator permission required for candidate register access
- CSV export restricted to same centre scope as on-screen register
- Sensitive registration fields masked per platform PII policy in list view if configured

##### Integrations

- Read examination schedule and centre allocation from Module 06 Examination Scheduling and Allocation
- Read candidate registration profile snapshot from Module 05 Candidate Registration
- Read hall ticket reference from Module 06 hall ticket generation handoff

##### Dependencies

- F06 candidate centre and session allocation
- F06 digital hall ticket generation and candidate access reference
- F06 candidate seat and computer assignment when seat assignment configured
- F05 candidate registration profile data for register display

##### Assumptions

- Centre allocation is authoritative before examination day register use
- Hall ticket numbers are unique within an examination schedule
- Register row counts align with dashboard scheduled candidate aggregates

##### Risks

- Late allocation changes after invigilator prints CSV day sheet may cause on-floor mismatch
- Large sessions may require pagination performance tuning

##### Non-functional requirements

- Search and filter should return first page within enterprise list response targets for up to 500 rows per session
- CSV export should complete for full session candidate list without timeout under normal centre hardware

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Scheduled candidate register list with default today session filter | Medium | 16 |
| UI | Candidate search bar for registration number name hall ticket | Easy | 14 |
| UI | Filter panel by examination session slot verification attendance activation status | Medium | 16 |
| UI | Read-only candidate schedule detail drawer | Easy | 14 |
| UI | Register empty state for session with zero allocated candidates | Simple | 5 |
| UI | Export scheduled candidate list confirmation dialog | Simple | 5 |
| API | List paginated scheduled candidates for logged-in centre | Medium | 6 |
| API | Search scheduled candidates by registration number name hall ticket | Medium | 6 |
| API | Filter scheduled candidates by examination session operational status | Medium | 6 |
| API | Get scheduled candidate detail for centre invigilator view | Easy | 4 |
| API | Export centre scheduled candidate register CSV | Complex | 8 |
| Database | Centre-scoped candidate allocation list query indexes | Easy | 0.25 |
| Database | Registration number and hall ticket search indexes for centre register | Easy | 0.25 |
| Integration | Read examination schedule and centre allocation from scheduling module | Simple | 4 |
| Testing | Happy path list search filter and detail drawer flow | Medium | 0.3 |
| Testing | Cross-centre candidate record exclusion from register results | Medium | 0.3 |
| Testing | CSV export column completeness for invigilator day sheet | Easy | 0.25 |
| Documentation | Scheduled candidate register invigilator user guide | Easy | 0.25 |

### F08-003 Candidate Identity Verification and Attendance Marking

159.65 hours · Go-live · 26 tasks

##### Description

Invigilator workflows at the examination centre to verify candidate identity against registration records, reject verification with documented reason when identity cannot be confirmed, mark candidate attendance as present or absent with mandatory absent reason, and correct mistaken attendance marks with audit history before session activation.

##### Business objective

Ensure only identity-confirmed and physically present candidates at the authorised centre proceed to examination session activation, creating an auditable pre-examination record for each allocated candidate.

##### Actors

- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Centre-allocated candidate list for session
- Candidate registration identity snapshot name registration number category photograph reference
- Hall ticket reference from scheduling module
- Invigilator user identity for audit
- Rejection reason text or selected reason code
- Absent reason text or selected reason code
- Attendance correction reason text

##### Outputs

- Updated verification status VERIFIED or REJECTED per candidate
- Verification rejection reason record
- Updated attendance status PRESENT or ABSENT per candidate
- Attendance correction audit history entries
- Updated operational flags visible in register and activation eligibility

##### Business rules

- Verification and attendance actions allowed only for candidates allocated to invigilator's centre for the session
- Verification can be marked only while session is in pre-start operational window per examination schedule
- Rejected verification prevents session activation for that candidate
- Absent attendance prevents session activation for that candidate
- Present attendance requires prior VERIFIED status before activation eligibility evaluation
- Attendance correction allowed only before candidate session activation
- Each verification and attendance change records invigilator user and timestamp
- Re-verification after VERIFIED requires supervisor policy if platform configures lock after verify

##### Validations

- Reject verification action when candidate not allocated to logged-in centre
- Reject verify when session not in allowed pre-start window
- Reject rejection submission when rejection reason is blank or below minimum length
- Reject present mark when candidate verification status is REJECTED
- Reject absent reason submission when absent reason is blank or below minimum length
- Reject attendance correction when candidate session already ACTIVATED
- Reject attendance correction when correction reason is blank
- Reject duplicate verify when candidate already VERIFIED unless correction policy enabled

##### Calculations

- Queue sort priority: UNVERIFIED first, then REJECTED awaiting review, then VERIFIED with UNMARKED attendance

##### Workflow

Verification: UNVERIFIED -> VERIFIED | REJECTED. Attendance: UNMARKED -> PRESENT | ABSENT. Correction: PRESENT <-> ABSENT with audit before ACTIVATED.

##### Search requirements

- Verification queue filter by verification status pending verified rejected
- Verification queue filter by attendance status unmarked present absent

##### Security

- Centre scope enforced on all verification and attendance mutations
- Invigilator role permission required for verify and attendance actions
- Immutable audit trail for verification rejection attendance and correction events
- Rejected candidates must not expose activation actions in downstream screens

##### Integrations

- Fetch candidate registration identity snapshot from Module 05 Candidate Registration
- Write audit events consumable by Module 12 Examination Administration reporting

##### Dependencies

- F08-002 centre scheduled candidate register for candidate selection context
- F05 candidate registration profile and confirmation data
- F06 candidate centre session allocation and hall ticket reference
- F01 invigilator authentication and centre-scoped authorization

##### Assumptions

- Registration photograph or identity fields are available from registration module when captured
- Invigilator performs physical ID check outside system; system records outcome only
- Session pre-start window defined by examination schedule start time from Module 06

##### Risks

- Incorrect manual verification could allow wrong candidate activation without biometric enforcement
- Concurrent invigilator actions on same candidate require optimistic locking
- Attendance correction disputes require clear audit history for administration review

##### Non-functional requirements

- Verification detail screen must load registration snapshot within standard form response time
- Audit records must be durable before activation eligibility reflects updated status

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate verification queue list for current centre session | Medium | 16 |
| UI | Candidate verification detail screen with registration identity fields | Complex | 18 |
| UI | Mark candidate identity verified confirmation dialog | Simple | 5 |
| UI | Reject verification dialog with mandatory reason field | Easy | 14 |
| UI | Mark candidate present action with timestamp display | Easy | 14 |
| UI | Mark candidate absent dialog with mandatory reason field | Easy | 14 |
| UI | Verification status badge on candidate register rows | Simple | 5 |
| UI | Attendance status badge with correction dialog for mistaken mark | Medium | 16 |
| UI | Verification queue empty state when all candidates processed | Simple | 5 |
| API | List candidates pending identity verification for centre session | Medium | 6 |
| API | Get candidate verification profile with registration snapshot fields | Medium | 6 |
| API | Mark candidate identity verified with invigilator audit stamp | Complex | 8 |
| API | Reject candidate verification with mandatory reason | Medium | 6 |
| API | Mark candidate attendance present with session timestamp | Medium | 6 |
| API | Mark candidate attendance absent with mandatory reason | Medium | 6 |
| API | Correct attendance mark with reason and audit history entry | Complex | 8 |
| Database | Candidate centre identity verification record persistence | Medium | 0.3 |
| Database | Candidate attendance record with correction audit history | Medium | 0.3 |
| Database | Verification rejection reason reference values | Simple | 0.1 |
| Integration | Fetch candidate registration identity snapshot from registration module | Simple | 4 |
| Testing | Happy path identity verify then mark present flow | Medium | 0.3 |
| Testing | Reject verification requires reason and blocks activation eligibility | Medium | 0.3 |
| Testing | Absent marking prevents downstream session activation | Medium | 0.3 |
| Testing | Attendance correction audit trail and duplicate verify rejection | Complex | 0.5 |
| Documentation | Invigilator identity verification checklist runbook | Medium | 0.3 |
| Documentation | Verification attendance audit technical notes | Easy | 0.25 |

### F08-004 Candidate Examination Session Activation

145.7 hours · Go-live · 22 tasks

##### Description

Centre invigilator activation of eligible candidate examination sessions immediately prior to examination start, enforcing registration completeness, fee compliance, schedule allocation, centre assignment, physical presence, and identity verification prerequisites, with single and batch activation support and explicit blocked-reason feedback for ineligible candidates.

##### Business objective

Allow authorised centre staff to start candidate examination sessions only for candidates who meet all pre-examination eligibility conditions, handing activated sessions to secure examination conduct without re-entering registration or scheduling data.

##### Actors

- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

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
- Show activation queue empty state when no eligible candidates
- Refresh candidate row activation status after successful activation

##### Inputs

- Candidate registration completion status from registration module
- Candidate fee payment compliance status from fee management
- Examination schedule and session allocation from scheduling module
- Centre allocation record for candidate
- Verification status from centre verification records
- Attendance status from centre attendance records
- Invigilator user identity
- Batch candidate selection list

##### Outputs

- Activation status ACTIVATED for eligible candidates
- Activation event with invigilator timestamp and eligibility snapshot
- Handoff signal to secure examination conduct for credential session readiness
- Per-candidate block reason list for ineligible candidates
- Batch activation result summary with success and failure counts

##### Business rules

- Activation permitted only for candidates allocated to invigilator's authorised centre
- Candidate registration must be complete and confirmed
- Candidate fee must be compliant including free first-attempt and paid subsequent rules where applicable
- Candidate must be scheduled for the selected examination session
- Candidate attendance must be PRESENT
- Candidate verification must be VERIFIED
- Already ACTIVATED candidates cannot be activated again
- REJECTED verification or ABSENT attendance permanently blocks activation for that session unless attendance corrected before activation
- Batch activation skips ineligible candidates without blocking eligible ones in same batch
- Activation allowed only within configured pre-start window before session official start time

##### Validations

- Reject activation when candidate not centre-allocated to logged-in centre
- Reject activation when registration status incomplete
- Reject activation when fee compliance flag false
- Reject activation when candidate not scheduled for requested session
- Reject activation when attendance not PRESENT
- Reject activation when verification not VERIFIED
- Reject activation when session already ACTIVATED
- Reject activation outside allowed pre-start time window
- Reject batch request when selection list empty
- Validate each batch item independently without failing entire batch on single invalid row

##### Calculations

- Eligibility ready flag equals all checklist rules true
- Batch success count equals activated rows
- Batch failure count equals rows with block reasons

##### Workflow

Activation eligibility: INACTIVE -> ELIGIBILITY_EVALUATED -> ELIGIBLE | BLOCKED. Activation execution: ELIGIBLE -> ACTIVATE_CONFIRMED -> ACTIVATED -> HANDOFF_TO_CONDUCT.

##### Search requirements

- Filter activation list by eligibility ready blocked already activated
- Search activation list by registration number or candidate name

##### Security

- Centre scope on all activation queries and mutations
- Invigilator permission required for session activation actions
- Activation audit log with eligibility snapshot for dispute resolution
- Idempotent activation request handling to prevent duplicate conduct sessions

##### Integrations

- Read fee compliance from Module 05 Candidate Registration and Module 02 Payment Gateway Fee Transaction Integration
- Push session activation handoff to Module 09 Secure Examination Conduct
- Read schedule allocation from Module 06 Examination Scheduling and Allocation

##### Dependencies

- F08-003 candidate identity verification and attendance marking statuses
- F05 registration confirmation and fee compliance determination
- F02 payment gateway fee transaction integration for paid registrations
- F06 examination schedule centre allocation and examination credentials handoff
- F09 secure examination conduct to receive activated session

##### Assumptions

- Examination credentials generation completed in Module 06 before activation handoff
- Fee compliance flag maintained upstream and read at activation time
- Conduct module creates examination session only upon successful activation handoff

##### Risks

- Partial batch failure may cause invigilator confusion without clear per-row feedback
- Handoff failure after local ACTIVATED record requires reconciliation procedure
- Clock skew between centre client and server may affect pre-start window validation

##### Non-functional requirements

- Single activation should complete including handoff within enterprise transaction response targets
- Batch activation of up to 50 candidates should provide progress feedback
- Activation state must be immediately visible in monitoring feature after handoff

##### Notes

Activation limited to registered fee-compliant scheduled centre-allocated present verified candidates per SOW centre-level activation rules.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Activation eligible candidate list with eligibility indicator icons | Medium | 16 |
| UI | Activation candidate detail with eligibility checklist panel | Complex | 18 |
| UI | Activate single candidate session confirmation dialog | Simple | 5 |
| UI | Multi-select batch activation screen for eligible candidates | Medium | 16 |
| UI | Activation blocked detail panel listing failed eligibility rules | Medium | 16 |
| UI | Activation queue empty state when no verified present candidates | Simple | 5 |
| UI | Post-activation status refresh on candidate register row | Simple | 5 |
| API | List candidates for session activation at centre with eligibility flags | Complex | 8 |
| API | Evaluate single candidate activation eligibility rule set | Complex | 8 |
| API | Activate single candidate examination session for centre | Complex | 8 |
| API | Batch activate multiple eligible candidate examination sessions | Very high | 12 |
| API | Get activation block reasons for ineligible candidate | Medium | 6 |
| Database | Centre session activation event record with invigilator timestamp | Medium | 0.3 |
| Database | Activation eligibility snapshot stored at activation time | Easy | 0.25 |
| Integration | Push session activation handoff to secure examination conduct module | Medium | 16 |
| Integration | Read candidate fee compliance flag from registration payment data | Simple | 4 |
| Testing | Happy path activation for registered fee-compliant scheduled verified present candidate | Medium | 0.3 |
| Testing | Block activation when candidate not identity verified | Medium | 0.3 |
| Testing | Block activation when absent or fee non-compliant or wrong centre | Complex | 0.5 |
| Testing | Batch activation partial failure per-row result and audit logging | Complex | 0.5 |
| Documentation | Session activation invigilator procedure runbook | Medium | 0.3 |
| Documentation | Activation eligibility rule technical reference notes | Easy | 0.25 |

### F08-005 Centre Live Examination Session Monitoring

139.8 hours · Go-live · 19 tasks

##### Description

Real-time centre-scoped monitoring view for invigilators to track examination progress of activated candidates through started, active, submitted, and completed conduct states during an in-progress session, with aggregate status header counts and drill-down read-only candidate session detail.

##### Business objective

Enable invigilators to supervise examination progress at their centre, identify candidates who have not started or submitted within expected timelines, and confirm session completion counts without accessing question content or department-wide analytics.

##### Actors

- Examination Centre/Invigilator User

##### User journey

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

##### Functional capabilities

- Select in-progress centre examination session for monitoring
- Display monitoring aggregate header counts by conduct status
- Display candidate status grid with not-started started active submitted completed columns
- Open read-only candidate live session drill-down detail panel
- Manual refresh monitoring data on demand
- Configure auto-refresh interval for monitoring grid
- Display abnormal session alert banner for stuck inactive candidates
- Display monitoring empty state before first activation
- Display session end summary read-only screen with final counts

##### Inputs

- Centre-allocated activated candidate list
- Live examination conduct session status from secure conduct module
- Session start and end times from examination schedule
- Last activity timestamps from conduct activity recording
- Abnormal idle threshold from examination configuration

##### Outputs

- Live status grid per activated candidate
- Aggregate status counts header
- Candidate drill-down session progress detail
- Session end completion summary counts
- Abnormal session alert indicators

##### Business rules

- Monitoring includes only candidates activated at logged-in centre for selected session
- Non-activated candidates appear in not-started or excluded per monitoring configuration agreed with conduct module
- Question content and candidate answers are never displayed in monitoring views
- Status values map to conduct module states: NOT_STARTED, STARTED, ACTIVE, SUBMITTED, COMPLETED
- Abnormal alert triggers when candidate in STARTED state exceeds idle threshold without transition to ACTIVE
- Monitoring read-only; invigilator cannot modify conduct state from this feature
- Session end summary available when session end time reached or all candidates submitted or completed

##### Validations

- Reject monitoring request when session not allocated to logged-in centre
- Reject monitoring request when invigilator lacks centre monitoring permission
- Validate selected session identifier belongs to centre schedule
- Validate auto-refresh interval within allowed minimum and maximum seconds

##### Calculations

- Not-started count equals activated candidates with conduct status NOT_STARTED
- Completed count equals candidates with conduct status COMPLETED plus SUBMITTED if examination treats submitted as complete for monitoring
- Abnormal candidate flag equals STARTED with last activity older than idle threshold

##### Workflow

Conduct status progression monitored: NOT_STARTED -> STARTED -> ACTIVE -> SUBMITTED -> COMPLETED. Monitoring view: SESSION_SELECTED -> GRID_LOADED -> REFRESHED -> SESSION_END_SUMMARY.

##### Search requirements

- Filter monitoring grid by conduct status column
- Search monitoring grid by registration number or candidate name

##### Security

- Centre-scoped monitoring queries exclude other centres' candidates
- No examination question or answer content exposed in monitoring UI
- Invigilator read-only access to conduct status fields only
- Monitoring access logged for audit when platform policy requires

##### Integrations

- Poll or subscribe to examination session state updates from Module 09 Secure Examination Conduct
- Read examination session schedule window from Module 06 Examination Scheduling and Allocation
- Read idle threshold from Module 04 Examination Master Configuration

##### Dependencies

- F08-004 candidate examination session activation producing ACTIVATED candidates
- F09 secure examination conduct session states and activity recording
- F06 examination schedule session timing
- F04 examination master configuration for session parameters

##### Assumptions

- Conduct module is authoritative source for started active submitted completed states
- Monitoring refresh interval balances timeliness with conduct module load
- Invigilator intervention for abnormal sessions occurs operationally outside this read-only view

##### Risks

- Polling lag may delay abnormal alert visibility
- Conduct module downtime would leave monitoring grid stale with no status updates
- Definition of SUBMITTED versus COMPLETED for summary counts must align with conduct module

##### Non-functional requirements

- Manual refresh should return updated grid within enterprise response targets for up to 500 activated candidates
- Auto-refresh must not degrade centre client browser performance at minimum interval
- Monitoring grid counts must reconcile with dashboard in-progress aggregates

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Live session monitoring landing screen for selected examination session | Medium | 16 |
| UI | Candidate status grid with not-started started active submitted completed columns | Complex | 18 |
| UI | Candidate live session drill-down read-only detail panel | Medium | 16 |
| UI | Manual refresh control for monitoring data | Simple | 5 |
| UI | Auto-refresh interval selector for monitoring view | Easy | 14 |
| UI | Abnormal session alert banner for stuck inactive candidates | Medium | 16 |
| UI | Monitoring empty state before first candidate activation | Simple | 5 |
| UI | Session end summary read-only screen with completion counts | Easy | 14 |
| API | List centre candidates with live examination session status | Medium | 6 |
| API | Get single candidate live session progress detail | Medium | 6 |
| API | Get session monitoring aggregate counts for status header | Medium | 6 |
| Database | Centre live session status read access over examination conduct states | Medium | 0.3 |
| Integration | Poll examination session state updates from secure conduct module | Medium | 16 |
| Testing | Happy path status progression from activated through submitted completed | Medium | 0.3 |
| Testing | Centre isolation on live monitoring candidate list | Medium | 0.3 |
| Testing | Auto-refresh stale data and session end summary count accuracy | Easy | 0.25 |
| Testing | Monitoring view for candidate with not-started conduct state after activation | Easy | 0.25 |
| Documentation | Live monitoring invigilator runbook during examination | Medium | 0.3 |
| Documentation | Monitoring conduct status terminology technical notes | Simple | 0.1 |
