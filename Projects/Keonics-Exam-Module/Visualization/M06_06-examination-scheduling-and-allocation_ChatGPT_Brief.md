# ChatGPT Visualization Brief — Module 06: Examination Scheduling & Allocation

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 06 Examination Scheduling & Allocation
**Features:** 5 (F06-001 … F06-005)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 06 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Schedule create → allocate → seat → hall ticket → credential pipeline
2. Preference 1/2 allocation decision flowchart
3. Hall ticket + credential distribution sequence
4. Scheduling ERD
5. Feature relationship / dependency graph within this module and to other modules
6. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Examination Scheduling & Allocation
**Purpose:** Create examination schedules/sessions; allocate candidates to centres/sessions; assign seats/computers; issue hall tickets; generate and distribute examination credentials.

**Actors (union across features):**
- Candidate
- Examination Administrator

**Feature list:**
- **F06-001** — Examination Schedule Creation and Maintenance
- **F06-002** — Candidate Centre and Session Allocation
- **F06-003** — Candidate Seat and Computer Assignment
- **F06-004** — Digital Hall Ticket Generation and Candidate Access
- **F06-005** — Examination Credential Generation and Secure Distribution Handoff

### DATA MODEL (from EXAM DB design v2.1)

- `exam_session`
- `candidate_allocation`
- `seat_assignment`
- `hall_ticket`
- `exam_credential`

### FEATURE CATALOGUE

#### F06-001 — Examination Schedule Creation and Maintenance

**One-liner / description:** Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time,…

**Business objective:** Provide authoritative, capacity-aware examination session schedules that govern when and where registered candidates may be allocated and examined, while preventing conflicting or invalid session definitions.

**Actors:** Examination Administrator

**User journey (14 steps):**
1. Examination Administrator opens the Examination Schedule register from the scheduling menu.
2. Administrator applies filters for examination, centre, session date range, and schedule status (Draft, Published, Cancelled).
3. Administrator selects Create Schedule to open the create form.
4. Administrator selects the target examination from examinations open for scheduling (sourced from Examination Master Configuration).
5. Administrator selects the authorised examination centre from centres active for that examination (sourced from Centre Master).
6. Administrator enters session date, session start time, duration, reporting time, maximum seat capacity for the session, and examination instructions text.
7. System validates centre capacity ceiling, date/time rules, and non-overlapping session constraints for the same centre.
8. Administrator saves the schedule in Draft status.
9. Administrator opens the saved Draft schedule in edit mode to adjust fields before publication.
10. Administrator selects Publish/Finalise; system displays a confirmation dialog summarising session timing, centre, and capacity impact.
11. Administrator confirms publication; schedule transitions to Published and becomes eligible for candidate allocation.
12. For a Published schedule requiring change, Administrator either edits allowed fields per business policy or cancels the schedule with mandatory reason.
13. Administrator opens schedule detail read-only view to audit timing, centre, capacity, status history, and linked allocation counts.
14. When no schedules match filters, Administrator sees empty-state guidance to create the first session schedule.

**Functional capabilities:**
- Display paginated examination schedule register with examination, centre, date range, and status filters
- Create draft examination session schedule with examination, centre, date, time, duration, reporting time, seat capacity, and instructions
- Edit draft examination session schedule fields before publication
- Publish/finalise draft schedule after validation of capacity and timing rules
- Cancel/deactivate published or draft schedule with mandatory reason capture
- View read-only schedule detail including status history and allocation summary counts
- Validate session does not exceed configured centre capacity for the examination
- Validate non-overlapping session times for the same centre on the same date
- Prevent publication when mandatory fields or centre-examination authorisation is missing
- Record schedule status transitions with audit metadata

**Inputs:** Examination identifier (from Examination Master Configuration); Authorised examination centre identifier (from Centre Master); Session date; Session start time; Session duration (minutes); Reporting time; Maximum seat capacity for session; Examination instructions text

**Outputs:** Draft schedule record; Published schedule record eligible for allocation; Cancelled schedule record with reason; Schedule register search results; Schedule detail view payload; Schedule status transition audit entries; Validation error messages for timing, capacity, and overlap conflicts

**Business rules:**
- Only authorised examination-centre pairings configured in Centre Management may be scheduled
- Session seat capacity cannot exceed centre capacity configured for the examination
- Published schedules cannot be deleted; they may only be cancelled with reason
- Hall ticket and credential generation require Published schedule status (enforced in downstream features)
- Session date and start time must be in the future at time of publication unless administrator override policy allows same-day (configurable assumption)
- Reporting time must precede or equal session start time
- Cancelled schedules exclude new candidate allocations but retain historical audit

**Validations:**
- Examination selection is mandatory and must reference an active examination open for scheduling
- Centre selection is mandatory and must be authorised for the selected examination
- Session date is mandatory and must be a valid calendar date
- Session start time is mandatory and valid 24-hour time format
- Duration is mandatory, positive integer minutes within configured min/max bounds
- Reporting time is mandatory and must not be after session start time
- Seat capacity is mandatory, positive integer, and less than or equal to centre capacity for examination
- Instructions text length within configured maximum character limit

**Workflow / states:** Draft → Published (publish/finalise action) | Draft → Cancelled (cancel action) | Published → Cancelled (cancel action). Published schedules are not editable for core timing/centre fields without cancel-and-recreate policy (assumption: material fields locked after publish).

**Dependencies:**
- Module 04 — Examination Master Configuration (examination definitions open for scheduling)
- Module 03 — Authorised Examination Centre Master and Centre Capacity Configuration
- Module 01 — Examination Administrator role and scheduling authorisation permissions

**Risks:** Late centre capacity changes in Module 03 may invalidate already-published schedules; Overlapping session detection edge cases across midnight boundaries; Administrators may publish schedules before registration cutoff causing allocation churn

---

#### F06-002 — Candidate Centre and Session Allocation

**One-liner / description:** Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and…

**Business objective:** Fairly and deterministically assign each registered candidate to an examination session and centre consistent with their preferences and operational capacity while preserving an auditable allocation decision trail.

**Actors:** Examination Administrator; Candidate

**User journey (14 steps):**
1. Examination Administrator opens the Candidate Allocation workspace for a selected examination.
2. Administrator views the pending allocation register showing registered candidates without finalised allocation.
3. Administrator reviews each candidate's centre preference 1, centre preference 2, candidate category, and registration status.
4. Administrator selects Run Auto-Allocation to open the allocation wizard.
5. Wizard step 1: Administrator confirms target published session schedules and allocation scope (all pending or filtered subset).
6. Wizard step 2: System previews projected allocations showing preference match tier, centre, session, and unallocated exceptions.
7. Administrator confirms execution; system runs allocation batch and records run identifier.
8. Administrator reviews allocation results grid highlighting preference-satisfied, preference-fallback, and unallocated candidates.
9. For exceptions, Administrator opens manual override dialog, selects alternate centre and session, and enters override reason.
10. Administrator re-runs preview for remaining unallocated candidates if needed.
11. Administrator selects Finalise Allocation; confirmation dialog warns that hall ticket generation will require finalised allocation.
12. System transitions batch to Finalised; candidates become locked for centre-session assignment downstream.
13. Candidate logs into portal and opens Registration Status; allotted centre, session date, reporting time, and allocation status display.
14. Candidate sees not-yet-allocated empty state when allocation is pending.

**Functional capabilities:**
- Display pending candidate allocation register with preference and category columns
- Filter allocation register by allocation status, category, centre preference, and registration completeness
- Preview automated allocation outcomes before committing batch
- Execute automated allocation applying preference order, capacity, schedule, and category rules
- Display allocation results with preference-match indicator and exception flags
- Manually override individual candidate centre and session assignment with reason
- Reallocate candidate from one finalised assignment to another prior to hall ticket generation lock
- Finalise allocation batch to lock candidate-centre-session mappings
- Expose candidate allotted centre and session on candidate portal registration status
- Record allocation batch run audit with rule version and outcome counts
- Block allocation against non-Published or Cancelled schedules

**Inputs:** Examination identifier; Published session schedule identifiers in scope; Registered candidate identifiers with completed registration; Centre preference 1 and preference 2 from registration; Candidate category (Government employee, PSU/Board, etc.); Manual override centre identifier; Manual override session schedule identifier; Override reason text

**Outputs:** Candidate-to-centre-to-session allocation record; Allocation preview result set; Allocation batch run summary with allocated, fallback, and unallocated counts; Finalised allocation lock state; Candidate portal allotted centre and session display; Exception/unallocated candidate list; Allocation override audit entries

**Business rules:**
- Allocation considers centre preference 1 before preference 2
- Candidate category may restrict eligible centres or sessions per department rules
- Session seat capacity reduced by confirmed allocations cannot be exceeded
- Only candidates with completed registration from Module 05 are eligible
- Finalised allocation required before seat assignment and hall ticket generation
- Manual override requires mandatory reason and administrator permission
- Cancelled schedules exclude new allocations; existing allocations flagged for administrator action

**Validations:**
- Examination must have at least one Published session schedule before allocation
- Candidate registration status must be complete and payment satisfied where mandatory
- Manual override centre must be authorised for examination
- Manual override session must be Published and have remaining capacity
- Override reason mandatory and within maximum length
- Cannot finalise allocation batch while unallocated candidates remain unless administrator confirms force-finalise policy
- Candidate cannot receive duplicate allocation to multiple sessions for same examination
- Preference values must reference active centres at allocation time

**Workflow / states:** Pending → Allocated (auto or manual assignment) → Finalised (finalise batch action) | Allocated → Reallocated (manual override before hall ticket lock) | Finalised → Reopened (administrator reopen policy assumption for pre-hall-ticket corrections only).

**Dependencies:**
- F06-001 — Published examination session schedules
- Module 05 — Candidate Registration with centre preferences and registration completion status
- Module 03 — Authorised centres and capacity configuration
- Module 04 — Examination Master Configuration and category eligibility rules
- Module 01 — Examination Administrator allocation permissions

**Risks:** Preference saturation at popular centres causing high fallback rates; Concurrent allocation runs against same session may cause capacity race conditions; Registration data changes after allocation may desynchronise candidate category rules

---

#### F06-003 — Candidate Seat and Computer Assignment

**One-liner / description:** Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection,…

**Business objective:** Ensure each candidate has a unique, traceable seat or computer assignment within their allotted session to support orderly centre conduct and accurate hall ticket presentation.

**Actors:** Examination Administrator

**User journey (11 steps):**
1. Examination Administrator opens Seat Assignment for a selected finalised session at a centre.
2. Administrator views the session seating register listing allocated candidates without seat assignment.
3. Administrator selects Auto-Assign Seats to fill available seat or computer identifiers from centre infrastructure configuration.
4. System displays auto-assignment summary showing assigned count and remaining unassigned candidates.
5. Administrator reviews seating list/grid showing candidate name, registration number, seat or computer identifier, and assignment status.
6. For conflicts or special accommodations, Administrator opens manual seat pick dialog and selects an available seat or computer.
7. System validates seat uniqueness and capacity bounds; Administrator saves reassignment with optional reason.
8. Administrator resolves seat conflict dialog when duplicate seat detected.
9. Administrator selects Lock Seat Map when all candidates are assigned; confirmation dialog warns that changes require unlock policy.
10. Locked seat map blocks further auto-assign and displays read-only seating register.
11. Administrator exports seating register for centre coordination.

**Functional capabilities:**
- Display session seating register filtered by assignment status
- Auto-assign available seat or computer identifiers to unassigned candidates in a session
- Display seating list or grid with candidate and seat mapping
- Manually assign or reassign seat or computer to individual candidate
- Detect and surface duplicate seat assignment conflicts
- Lock seat map for session to freeze assignments before hall ticket generation
- Unlock seat map under administrator policy for pre-hall-ticket corrections
- Validate seat identifiers against centre infrastructure capacity configuration
- Export session seating register

**Inputs:** Finalised session schedule identifier; Centre identifier; Candidate allocation identifiers within session; Available seat or computer identifier pool from centre infrastructure; Manual seat or computer selection; Reassignment reason text; Lock seat map confirmation

**Outputs:** Candidate seat or computer assignment record per session; Auto-assignment batch summary; Seating register view data; Seat map locked status flag; Seat conflict error detail; Seating register export file; Seat assignment change audit entries

**Business rules:**
- Seat assignment permitted only after allocation finalisation for the session
- Each seat or computer identifier may be assigned to at most one candidate per session
- Seat identifiers must exist within centre infrastructure capacity defined in Module 03
- Hall ticket generation requires locked seat map when seat/computer assignment is applicable for examination type
- Manual reassignment after lock requires unlock action with audit

**Validations:**
- Session must have Finalised candidate allocations before seat assignment
- Seat or computer identifier mandatory on manual assign
- Seat identifier must be within configured centre seat or computer range
- Duplicate seat within same session rejected
- Cannot lock seat map while unassigned candidates remain unless force-lock policy confirmed
- Reassignment reason required when changing assigned seat after initial assignment

**Workflow / states:** Unassigned → Assigned (auto or manual assign) → Locked (lock seat map action) | Assigned → Reassigned (manual change before or after unlock) | Locked → Unlocked (administrator unlock for corrections).

**Dependencies:**
- F06-002 — Finalised candidate centre and session allocation
- Module 03 — Centre Capacity and Infrastructure Configuration (seat or computer inventory)
- F06-001 — Published session schedule context
- Module 01 — Examination Administrator seat assignment permissions

**Risks:** Centre infrastructure changes after seat lock may invalidate assignments; Auto-assign ordering may not respect special accommodation needs without manual override

---

#### F06-004 — Digital Hall Ticket Generation and Candidate Access

**One-liner / description:** Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation,…

**Business objective:** Deliver authoritative, tamper-evident hall tickets digitally so candidates know exactly when, where, and how to report for their allotted examination session.

**Actors:** Examination Administrator; Candidate

**User journey (13 steps):**
1. Examination Administrator opens Hall Ticket Generation console for a selected examination.
2. System displays prerequisite checklist: Published schedules, Finalised allocations, Locked seat map (if applicable).
3. Administrator selects Generate Hall Tickets for scope (examination, session, or centre subset).
4. System queues generation batch and displays progress register.
5. Administrator opens sample hall ticket preview for template verification.
6. Upon completion, Administrator reviews generation status register showing success, failed, and pending rows per candidate.
7. For individual candidate detail changes, Administrator opens Regenerate Hall Ticket dialog with reason.
8. Candidate logs into portal and navigates to Hall Ticket section.
9. If prerequisites not met, Candidate sees not-yet-available message explaining pending scheduling or allocation.
10. When eligible, Candidate views hall ticket page showing candidate name, examination name, session date, reporting time, centre name and address, seat or computer number, and instructions.
11. Candidate selects Download PDF to save hall ticket document.
12. Candidate selects Print to open print-friendly view.
13. If generation failed for candidate, Administrator retries from failed queue row.

**Functional capabilities:**
- Display hall ticket generation console with prerequisite checklist
- Trigger batch hall ticket generation for eligible candidates
- Monitor hall ticket generation job status per candidate
- Preview hall ticket document template with sample data
- Regenerate hall ticket for individual candidate with reason and version increment
- Retry failed hall ticket generation for candidate
- Determine candidate hall ticket eligibility based on scheduling and allocation state
- Display candidate hall ticket detail on portal
- Provide candidate hall ticket PDF download
- Provide candidate hall ticket print view
- Display not-eligible empty and error states on candidate portal
- Record hall ticket document storage reference and generation audit

**Inputs:** Examination identifier; Session schedule identifier scope; Centre identifier scope; Candidate identifier for regeneration; Regeneration reason text; Candidate authenticated portal session

**Outputs:** Generated hall ticket PDF document per candidate; Hall ticket generation batch status records; Candidate portal hall ticket display payload; Hall ticket eligibility boolean with reason codes; Hall ticket version history on regeneration; Failed generation error detail for administrator retry

**Business rules:**
- Hall ticket generation blocked until candidate allocation is Finalised
- Hall ticket generation blocked until session schedule is Published
- When seat assignment applies, hall ticket generation blocked until seat map is Locked
- Regeneration supersedes prior hall ticket version; prior version retained in audit history
- Candidate may access only their own hall ticket
- Hall ticket must reflect final allotted centre, not merely preference
- Failed generation rows remain retryable without duplicating successful tickets

**Validations:**
- Prerequisite checklist must pass before batch generation accepted
- Candidate must belong to generation scope examination
- Regeneration reason mandatory on administrator regenerate action
- Portal hall ticket request rejected when eligibility prerequisites unmet
- Download allowed only for successfully generated current version
- Candidate portal session must match hall ticket owner candidate identifier

**Workflow / states:** Not Eligible → Eligible (prerequisites satisfied) → Generation Pending → Generated (success) | Generation Pending → Failed (error) → Generation Pending (retry) | Generated → Superseded (regeneration creates new current version).

**Dependencies:**
- F06-001 — Published examination session schedules
- F06-002 — Finalised candidate centre and session allocation
- F06-003 — Locked seat or computer assignment when applicable
- Module 05 — Candidate identity and registration details for hall ticket content
- Module 03 — Centre name and address for hall ticket display
- Module 04 — Examination name and instructions configuration
- Module 01 — Candidate portal authentication and administrator hall ticket permissions

**Risks:** Late allocation or seat changes after generation require mass regeneration; PDF generation failures at scale may delay candidate access close to exam date; Candidate downloads from shared devices pose informational disclosure risk mitigated by authentication

**Notes:** Hall ticket availability requires completed scheduling, finalised allocation, and locked seat map where seat assignment applies.

---

#### F06-005 — Examination Credential Generation and Secure Distribution Handoff

**One-liner / description:** Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and…

**Business objective:** Ensure each candidate receives unique, secure examination login credentials through approved communication channels only after scheduling and allocation are complete, enabling examination day login without administrator manual password handling.

**Actors:** Examination Administrator; Candidate

**User journey (11 steps):**
1. Examination Administrator opens Examination Credential Generation console for a selected examination.
2. System displays eligibility checklist: Published schedules, Finalised allocations, and schedule finalisation policy satisfied.
3. Administrator selects Generate Credentials for candidate scope.
4. System generates unique examination login ID and random password per eligible candidate, stores password using secure hashing, and queues credential records.
5. Administrator views credential generation status register showing generated, pending dispatch, dispatched, and failed rows with masked secret display only.
6. Administrator selects Initiate Distribution Handoff for batch; system publishes secure dispatch payload to Notification Service without logging plaintext password.
7. Module 07 dispatches SMS and/or email to candidate using configured templates; this feature records handoff correlation identifier and dispatch status callbacks.
8. For compromised or undelivered credentials, Administrator opens Regenerate Credentials dialog; system invalidates prior credential and creates new pair.
9. Administrator triggers Resend Distribution Handoff for individual candidate to Notification Service.
10. Candidate receives login ID and password via SMS/email from Notification Service (outside this feature UI).
11. Candidate uses credentials at examination login (Module 09 scope); this feature does not provide conduct interface.

**Functional capabilities:**
- Display credential generation console with schedule finalisation eligibility checklist
- Generate unique examination login ID and password batch for eligible candidates
- Store examination password using secure one-way hashing
- Display credential generation and dispatch status register with masked secrets
- Initiate secure distribution handoff batch to Notification Service
- Receive and persist dispatch status callback updates from Notification Service
- Regenerate credentials for individual candidate invalidating prior active credential
- Trigger resend distribution handoff for individual candidate
- Block credential generation until schedule finalisation and allocation prerequisites met
- Audit all generate, regenerate, and handoff actions without plaintext password retention in logs

**Inputs:** Examination identifier; Published session schedule finalisation confirmation; Candidate identifiers in eligible scope; Regenerate credentials reason text; Resend dispatch handoff confirmation; Notification template routing identifiers from Module 07; Dispatch status callback payload from Notification Service

**Outputs:** Examination login ID per candidate; Securely hashed examination password record; Credential generation batch status; Distribution handoff request with correlation identifier; Dispatch status per candidate (Pending, Dispatched, Failed); Regenerated credential pair with prior credential invalidated flag; Administrator masked credential status view

**Business rules:**
- Credential generation permitted only after examination schedule finalisation policy is satisfied and allocations are Finalised
- Each candidate receives one active examination credential set per examination attempt
- Plaintext password shown only transiently during generation handoff to Notification Service, never in administrator registers
- Regeneration invalidates previous login password pair immediately
- Resend handoff uses current active credential without regenerating unless administrator explicitly regenerates
- Examination conduct login validation is out of scope; credentials prepared for Module 09 consumption

**Validations:**
- Eligibility checklist must pass before batch generation accepted
- Login ID must be unique within examination scope
- Generated password meets configured complexity and length rules
- Regenerate reason mandatory on administrator regenerate action
- Handoff blocked when candidate missing registered mobile or email required by channel policy
- Resend allowed only when active credential exists
- Dispatch callback correlation identifier must match existing handoff record

**Workflow / states:** Not Eligible → Eligible (prerequisites met) → Generated (credential created) → Handoff Pending (dispatch request queued) → Dispatched (Notification Service success callback) | Handoff Pending → Handoff Failed (callback failure) → Handoff Pending (resend) | Generated → Invalidated (regenerate action) → Generated (new active credential).

**Dependencies:**
- F06-001 — Published and finalised examination session schedules
- F06-002 — Finalised candidate allocation
- Module 07 — Notification Template Catalog, channel configuration, and dispatch engine
- Module 05 — Candidate registered mobile and email contact points
- Module 01 — Examination Administrator credential management permissions
- Module 09 — Secure Examination Conduct consumes generated credentials at login time

**Risks:** Credential delivery failure leaves candidates without login details near examination time; Regeneration after dispatch may confuse candidates receiving multiple messages; Misconfigured Notification templates may expose credentials improperly if template not masked

**Notes:** Credential plaintext distribution executed by Module 07 Notification Service; this feature generates credentials and hands off secure dispatch requests.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 06 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 06 Examination Scheduling & Allocation** (5 features).
> Features: F06-001 Examination Schedule Creation and Maintenance; F06-002 Candidate Centre and Session Allocation; F06-003 Candidate Seat and Computer Assignment; F06-004 Digital Hall Ticket Generation and Candidate Access; F06-005 Examination Credential Generation and Secure Distribution Handoff.
> Purpose: Create examination schedules/sessions; allocate candidates to centres/sessions; assign seats/computers; issue hall tickets; generate and distribute examination credentials.
> Draw: Schedule create → allocate → seat → hall ticket → credential pipeline; Preference 1/2 allocation decision flowchart; Hall ticket + credential distribution sequence; Scheduling ERD; ERD for `exam_session`, `candidate_allocation`, `seat_assignment`, `hall_ticket`, `exam_credential`.
