# Module 06: Examination Scheduling & Allocation

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 5 (F06-001 … F06-005)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 06 Examination Scheduling & Allocation

759 hours · 126 tasks · Business

Examination schedule management, candidate-to-centre allocation, hall ticket issuance, and examination credential generation.

### F06-001 Examination Schedule Creation and Maintenance

136.7 hours · Go-live · 25 tasks

##### Description

Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time, duration, reporting time, applicable centre, seat capacity, and candidate-facing instructions. Schedules progress through controlled lifecycle states and become the anchor for downstream allocation, hall ticket, and credential generation.

##### Business objective

Provide authoritative, capacity-aware examination session schedules that govern when and where registered candidates may be allocated and examined, while preventing conflicting or invalid session definitions.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Examination identifier (from Examination Master Configuration)
- Authorised examination centre identifier (from Centre Master)
- Session date
- Session start time
- Session duration (minutes)
- Reporting time
- Maximum seat capacity for session
- Examination instructions text
- Cancellation reason (on cancel action)

##### Outputs

- Draft schedule record
- Published schedule record eligible for allocation
- Cancelled schedule record with reason
- Schedule register search results
- Schedule detail view payload
- Schedule status transition audit entries
- Validation error messages for timing, capacity, and overlap conflicts

##### Business rules

- Only authorised examination-centre pairings configured in Centre Management may be scheduled
- Session seat capacity cannot exceed centre capacity configured for the examination
- Published schedules cannot be deleted; they may only be cancelled with reason
- Hall ticket and credential generation require Published schedule status (enforced in downstream features)
- Session date and start time must be in the future at time of publication unless administrator override policy allows same-day (configurable assumption)
- Reporting time must precede or equal session start time
- Cancelled schedules exclude new candidate allocations but retain historical audit

##### Validations

- Examination selection is mandatory and must reference an active examination open for scheduling
- Centre selection is mandatory and must be authorised for the selected examination
- Session date is mandatory and must be a valid calendar date
- Session start time is mandatory and valid 24-hour time format
- Duration is mandatory, positive integer minutes within configured min/max bounds
- Reporting time is mandatory and must not be after session start time
- Seat capacity is mandatory, positive integer, and less than or equal to centre capacity for examination
- Instructions text length within configured maximum character limit
- No overlapping Published sessions for same centre where session time ranges intersect
- Cancellation reason mandatory when transitioning Published or Draft to Cancelled

##### Calculations

- Derive session end time from start time plus duration
- Compute remaining allocatable seats as session capacity minus confirmed allocations (display only on detail view)

##### Workflow

Draft → Published (publish/finalise action) | Draft → Cancelled (cancel action) | Published → Cancelled (cancel action). Published schedules are not editable for core timing/centre fields without cancel-and-recreate policy (assumption: material fields locked after publish).

##### Search requirements

- Filter schedule register by examination name or code
- Filter by centre name or code
- Filter by session date range
- Filter by schedule status (Draft, Published, Cancelled)
- Sort by session date, centre, examination, status

##### Reports

- Schedule register export (CSV) for administrative review

##### Security

- Only Examination Administrator role with scheduling permission may create, publish, or cancel schedules
- Centre-scoped invigilator roles have no access to schedule maintenance screens
- All publish and cancel actions logged with administrator identity and timestamp

##### Dependencies

- Module 04 — Examination Master Configuration (examination definitions open for scheduling)
- Module 03 — Authorised Examination Centre Master and Centre Capacity Configuration
- Module 01 — Examination Administrator role and scheduling authorisation permissions

##### Assumptions

- Centre-examination authorisation and raw capacity values are maintained in Module 03
- Examination definitions and scheduling windows are maintained in Module 04
- Material schedule field edits after publication require cancel-and-recreate rather than in-place edit
- Complexity drivers: overlap detection across centre sessions, capacity cross-check against external centre master, and status-locked edit rules

##### Risks

- Late centre capacity changes in Module 03 may invalidate already-published schedules
- Overlapping session detection edge cases across midnight boundaries
- Administrators may publish schedules before registration cutoff causing allocation churn

##### Non-functional requirements

- Schedule register list/search response suitable for enterprise volumes (paginated)
- Audit history retained for compliance review
- Validation feedback field-level on create/edit forms

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination schedule register list with examination, centre, date range, and status filters | Medium | 16 |
| UI | Create examination schedule form with examination and centre dependent selectors | Medium | 16 |
| UI | Edit draft examination schedule form | Medium | 16 |
| UI | Schedule detail read-only view with status history and allocation summary | Easy | 14 |
| UI | Publish/finalise schedule confirmation dialog | Simple | 5 |
| UI | Cancel schedule confirmation dialog with mandatory reason field | Simple | 5 |
| UI | Schedule register empty state when no sessions exist | Simple | 5 |
| UI | Schedule form validation error state for overlap and capacity failures | Easy | 14 |
| UI | Schedule register CSV export action | Simple | 5 |
| API | List and search examination schedules with filters and pagination | Medium | 6 |
| API | Get examination schedule detail with status history | Easy | 4 |
| API | Create draft examination schedule with field and authorisation validation | Medium | 6 |
| API | Update draft examination schedule | Medium | 6 |
| API | Publish/finalise examination schedule with overlap and capacity checks | Complex | 8 |
| API | Cancel examination schedule with reason capture | Easy | 4 |
| API | Lookup examinations open for scheduling | Simple | 2 |
| API | Lookup authorised centres and capacity for selected examination | Simple | 2 |
| Database | Core examination session schedule entity persistence | Medium | 0.3 |
| Database | Schedule status transition audit and history persistence | Easy | 0.25 |
| Database | Centre session overlap constraints and capacity indexes | Complex | 0.5 |
| Testing | Happy-path draft create, edit, publish schedule lifecycle | Medium | 0.3 |
| Testing | Negative cases for capacity exceed, invalid reporting time, and overlap rejection | Medium | 0.3 |
| Testing | Edge and security cases for unauthorised centre, cancel audit, and locked published edits | Complex | 0.5 |
| Documentation | Examination Administrator runbook for schedule creation, publication, and cancellation | Medium | 0.3 |
| Documentation | Technical notes for schedule lifecycle states and overlap validation rules | Easy | 0.25 |

### F06-002 Candidate Centre and Session Allocation

187.75 hours · Go-live · 26 tasks

##### Description

Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and department business rules. Supports automated batch allocation with preview, exception handling, manual override, and finalisation that locks allocations for seat assignment and hall ticket generation.

##### Business objective

Fairly and deterministically assign each registered candidate to an examination session and centre consistent with their preferences and operational capacity while preserving an auditable allocation decision trail.

##### Actors

- Examination Administrator
- Candidate

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Examination identifier
- Published session schedule identifiers in scope
- Registered candidate identifiers with completed registration
- Centre preference 1 and preference 2 from registration
- Candidate category (Government employee, PSU/Board, etc.)
- Manual override centre identifier
- Manual override session schedule identifier
- Override reason text
- Allocation batch finalise confirmation

##### Outputs

- Candidate-to-centre-to-session allocation record
- Allocation preview result set
- Allocation batch run summary with allocated, fallback, and unallocated counts
- Finalised allocation lock state
- Candidate portal allotted centre and session display
- Exception/unallocated candidate list
- Allocation override audit entries

##### Business rules

- Allocation considers centre preference 1 before preference 2
- Candidate category may restrict eligible centres or sessions per department rules
- Session seat capacity reduced by confirmed allocations cannot be exceeded
- Only candidates with completed registration from Module 05 are eligible
- Finalised allocation required before seat assignment and hall ticket generation
- Manual override requires mandatory reason and administrator permission
- Cancelled schedules exclude new allocations; existing allocations flagged for administrator action

##### Validations

- Examination must have at least one Published session schedule before allocation
- Candidate registration status must be complete and payment satisfied where mandatory
- Manual override centre must be authorised for examination
- Manual override session must be Published and have remaining capacity
- Override reason mandatory and within maximum length
- Cannot finalise allocation batch while unallocated candidates remain unless administrator confirms force-finalise policy
- Candidate cannot receive duplicate allocation to multiple sessions for same examination
- Preference values must reference active centres at allocation time

##### Calculations

- Compute remaining session capacity during allocation preview and execution
- Derive preference satisfaction tier (Preference 1 matched, Preference 2 matched, Non-preference fallback)
- Count allocated, fallback-allocated, and unallocated candidates per batch run

##### Workflow

Pending → Allocated (auto or manual assignment) → Finalised (finalise batch action) | Allocated → Reallocated (manual override before hall ticket lock) | Finalised → Reopened (administrator reopen policy assumption for pre-hall-ticket corrections only).

##### Search requirements

- Search candidates in allocation register by name, registration number, mobile
- Filter by allocation status (Pending, Allocated, Finalised, Unallocated exception)
- Filter by candidate category
- Filter by allotted centre or session date
- Sort by preference match tier and registration date

##### Reports

- Allocation batch summary report with preference match statistics
- Unallocated candidate exception export

##### Security

- Only Examination Administrator with allocation permission may run batch, override, or finalise
- Candidates may view only their own allotted centre and session
- Override and batch run actions audit-logged with administrator identity

##### Dependencies

- F06-001 — Published examination session schedules
- Module 05 — Candidate Registration with centre preferences and registration completion status
- Module 03 — Authorised centres and capacity configuration
- Module 04 — Examination Master Configuration and category eligibility rules
- Module 01 — Examination Administrator allocation permissions

##### Assumptions

- Centre preferences captured during Module 05 registration are snapshot-read at allocation time
- Category-based centre restrictions are configurable via examination business rules from Module 04
- Complexity drivers: multi-rule batch engine, preview/commit pattern, and manual override audit
- Force-finalise with unallocated exceptions is policy-gated and off by default

##### Risks

- Preference saturation at popular centres causing high fallback rates
- Concurrent allocation runs against same session may cause capacity race conditions
- Registration data changes after allocation may desynchronise candidate category rules

##### Non-functional requirements

- Batch allocation preview completes within acceptable time for examination-sized candidate volumes
- Allocation decisions fully auditable for grievance review
- Candidate portal allotment view reflects finalised state within normal replication latency

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Candidate allocation workspace landing with examination selector | Easy | 14 |
| UI | Pending allocation register with preference, category, and status columns | Medium | 16 |
| UI | Auto-allocation wizard step for scope and session selection | Medium | 16 |
| UI | Auto-allocation wizard preview step showing projected assignments and exceptions | Complex | 18 |
| UI | Allocation results review grid with preference-match and exception indicators | Medium | 16 |
| UI | Manual allocation override dialog with centre, session, and reason | Medium | 16 |
| UI | Finalise allocation batch confirmation dialog | Simple | 5 |
| UI | Unallocated exceptions list panel | Easy | 14 |
| UI | Candidate portal registration status allotted centre and session display | Easy | 14 |
| UI | Candidate portal allocation pending empty state | Simple | 5 |
| API | List and search candidates pending allocation with filters | Medium | 6 |
| API | Preview automated allocation batch without commit | Complex | 8 |
| API | Execute automated allocation batch with preference and capacity rules | Very high | 12 |
| API | Manual assign or reassign candidate to centre and session | Complex | 8 |
| API | Finalise allocation batch to lock assignments | Complex | 8 |
| API | Get candidate allocation status for administrator register | Easy | 4 |
| API | Get candidate portal allotted centre and session detail | Easy | 4 |
| Database | Candidate centre session allocation core entity persistence | Medium | 0.3 |
| Database | Allocation batch run and outcome audit persistence | Medium | 0.3 |
| Database | Allocation override reason and history persistence | Easy | 0.25 |
| Database | Preference snapshot and capacity reservation indexes | Complex | 0.5 |
| Testing | Happy-path auto-allocation with preference 1 and preference 2 matching | Complex | 0.5 |
| Testing | Negative validation for capacity exceed, incomplete registration, and invalid centre override | Medium | 0.3 |
| Testing | Edge cases for category restrictions, tie-breaking, concurrent batch guard, and finalise lock | Very high | 1 |
| Documentation | Examination Administrator runbook for auto-allocation, override, and finalisation | Medium | 0.3 |
| Documentation | Technical notes for allocation rule precedence and batch audit model | Medium | 0.3 |

### F06-003 Candidate Seat and Computer Assignment

123.55 hours · Go-live · 23 tasks

##### Description

Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection, seating register views, and seat-map lock prior to hall ticket generation.

##### Business objective

Ensure each candidate has a unique, traceable seat or computer assignment within their allotted session to support orderly centre conduct and accurate hall ticket presentation.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

- Display session seating register filtered by assignment status
- Auto-assign available seat or computer identifiers to unassigned candidates in a session
- Display seating list or grid with candidate and seat mapping
- Manually assign or reassign seat or computer to individual candidate
- Detect and surface duplicate seat assignment conflicts
- Lock seat map for session to freeze assignments before hall ticket generation
- Unlock seat map under administrator policy for pre-hall-ticket corrections
- Validate seat identifiers against centre infrastructure capacity configuration
- Export session seating register

##### Inputs

- Finalised session schedule identifier
- Centre identifier
- Candidate allocation identifiers within session
- Available seat or computer identifier pool from centre infrastructure
- Manual seat or computer selection
- Reassignment reason text
- Lock seat map confirmation

##### Outputs

- Candidate seat or computer assignment record per session
- Auto-assignment batch summary
- Seating register view data
- Seat map locked status flag
- Seat conflict error detail
- Seating register export file
- Seat assignment change audit entries

##### Business rules

- Seat assignment permitted only after allocation finalisation for the session
- Each seat or computer identifier may be assigned to at most one candidate per session
- Seat identifiers must exist within centre infrastructure capacity defined in Module 03
- Hall ticket generation requires locked seat map when seat/computer assignment is applicable for examination type
- Manual reassignment after lock requires unlock action with audit

##### Validations

- Session must have Finalised candidate allocations before seat assignment
- Seat or computer identifier mandatory on manual assign
- Seat identifier must be within configured centre seat or computer range
- Duplicate seat within same session rejected
- Cannot lock seat map while unassigned candidates remain unless force-lock policy confirmed
- Reassignment reason required when changing assigned seat after initial assignment

##### Calculations

- Count assigned versus unassigned candidates for session
- Compute next available seat identifier during auto-assign sequence

##### Workflow

Unassigned → Assigned (auto or manual assign) → Locked (lock seat map action) | Assigned → Reassigned (manual change before or after unlock) | Locked → Unlocked (administrator unlock for corrections).

##### Search requirements

- Search seating register by candidate name or registration number
- Filter by assignment status (Unassigned, Assigned)
- Filter by seat or computer identifier
- Sort by seat identifier or candidate name

##### Reports

- Session seating register export for centre invigilator coordination

##### Security

- Only Examination Administrator with seat assignment permission may assign or lock seats
- Centre invigilator roles receive read-only seating visibility via Module 08 dependency only
- All lock, unlock, and reassignment actions audit-logged

##### Dependencies

- F06-002 — Finalised candidate centre and session allocation
- Module 03 — Centre Capacity and Infrastructure Configuration (seat or computer inventory)
- F06-001 — Published session schedule context
- Module 01 — Examination Administrator seat assignment permissions

##### Assumptions

- Seat/computer identifiers are pre-configured numeric or labelled inventory in Module 03
- Examinations not requiring computer assignment still use seat numbering from same inventory model
- Complexity drivers: uniqueness enforcement, lock/unlock governance, and auto-assign sequencing

##### Risks

- Centre infrastructure changes after seat lock may invalidate assignments
- Auto-assign ordering may not respect special accommodation needs without manual override

##### Non-functional requirements

- Auto-assign completes for full session candidate count within operational time limits
- Seating register supports centre-scale candidate volumes with pagination

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Session seat assignment register with assignment status filters | Medium | 16 |
| UI | Auto-assign seats action panel with scope selection | Easy | 14 |
| UI | Seating list grid showing candidate and seat or computer mapping | Medium | 16 |
| UI | Manual seat pick dialog with available seat selector | Medium | 16 |
| UI | Seat conflict resolution dialog for duplicate assignment | Simple | 5 |
| UI | Lock seat map confirmation dialog | Simple | 5 |
| UI | Unlock seat map confirmation dialog for corrections | Simple | 5 |
| UI | Seating register empty state when no finalised allocations exist | Simple | 5 |
| UI | Seating register CSV export action | Simple | 5 |
| API | List session seat assignments with search and filters | Medium | 6 |
| API | Auto-assign seats for session from centre inventory pool | Complex | 8 |
| API | Manual assign or reassign seat or computer to candidate | Medium | 6 |
| API | Lock seat map for session | Easy | 4 |
| API | Unlock seat map for session under policy | Easy | 4 |
| API | Validate seat uniqueness and inventory bounds | Medium | 6 |
| Database | Candidate seat or computer assignment entity persistence | Medium | 0.3 |
| Database | Session seat map lock state persistence | Simple | 0.1 |
| Database | Seat assignment change history and uniqueness constraints | Complex | 0.5 |
| Testing | Happy-path auto-assign, manual assign, and lock seat map | Medium | 0.3 |
| Testing | Negative cases for duplicate seat, out-of-range identifier, and lock with unassigned | Medium | 0.3 |
| Testing | Edge cases for unlock reassignment audit and concurrent assign attempts | Complex | 0.5 |
| Documentation | Examination Administrator runbook for seat assignment and seat map lock | Medium | 0.3 |
| Documentation | Technical notes for seat uniqueness rules and lock prerequisites | Easy | 0.25 |

### F06-004 Digital Hall Ticket Generation and Candidate Access

156.75 hours · Go-live · 27 tasks

##### Description

Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation, regeneration, and status monitoring plus Candidate portal view, download, and print access to hall tickets containing examination, session, centre, reporting time, and seat details.

##### Business objective

Deliver authoritative, tamper-evident hall tickets digitally so candidates know exactly when, where, and how to report for their allotted examination session.

##### Actors

- Examination Administrator
- Candidate

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Examination identifier
- Session schedule identifier scope
- Centre identifier scope
- Candidate identifier for regeneration
- Regeneration reason text
- Candidate authenticated portal session

##### Outputs

- Generated hall ticket PDF document per candidate
- Hall ticket generation batch status records
- Candidate portal hall ticket display payload
- Hall ticket eligibility boolean with reason codes
- Hall ticket version history on regeneration
- Failed generation error detail for administrator retry

##### Business rules

- Hall ticket generation blocked until candidate allocation is Finalised
- Hall ticket generation blocked until session schedule is Published
- When seat assignment applies, hall ticket generation blocked until seat map is Locked
- Regeneration supersedes prior hall ticket version; prior version retained in audit history
- Candidate may access only their own hall ticket
- Hall ticket must reflect final allotted centre, not merely preference
- Failed generation rows remain retryable without duplicating successful tickets

##### Validations

- Prerequisite checklist must pass before batch generation accepted
- Candidate must belong to generation scope examination
- Regeneration reason mandatory on administrator regenerate action
- Portal hall ticket request rejected when eligibility prerequisites unmet
- Download allowed only for successfully generated current version
- Candidate portal session must match hall ticket owner candidate identifier

##### Calculations

- Derive hall ticket eligibility from composite schedule, allocation, and seat lock states
- Increment hall ticket version number on regeneration

##### Workflow

Not Eligible → Eligible (prerequisites satisfied) → Generation Pending → Generated (success) | Generation Pending → Failed (error) → Generation Pending (retry) | Generated → Superseded (regeneration creates new current version).

##### Search requirements

- Administrator search generation register by candidate name, registration number, status
- Filter by examination, session date, centre, generation status
- Sort by generation timestamp and status

##### Documents

- Hall ticket PDF document with examination, centre, session, reporting time, seat, and instructions
- Print-friendly hall ticket render

##### Reports

- Hall ticket generation batch summary with success and failure counts

##### Security

- Candidate hall ticket access restricted to authenticated owner
- Hall ticket PDF served through authorised download token or session check
- Administrator regeneration and batch actions audit-logged
- Hall ticket document storage access limited to application document service

##### Integrations

- Internal document rendering service for PDF hall ticket generation

##### Dependencies

- F06-001 — Published examination session schedules
- F06-002 — Finalised candidate centre and session allocation
- F06-003 — Locked seat or computer assignment when applicable
- Module 05 — Candidate identity and registration details for hall ticket content
- Module 03 — Centre name and address for hall ticket display
- Module 04 — Examination name and instructions configuration
- Module 01 — Candidate portal authentication and administrator hall ticket permissions

##### Assumptions

- PDF template layout approved by department; branding fields supplied from configuration
- Document storage uses platform blob storage pattern
- Complexity drivers: prerequisite gating chain, batch generation monitoring, and PDF render integration

##### Risks

- Late allocation or seat changes after generation require mass regeneration
- PDF generation failures at scale may delay candidate access close to exam date
- Candidate downloads from shared devices pose informational disclosure risk mitigated by authentication

##### Non-functional requirements

- Batch generation supports examination-wide candidate volumes asynchronously
- PDF download responsive for candidate portal usage
- Generated documents retained per records retention policy

##### Notes

Hall ticket availability requires completed scheduling, finalised allocation, and locked seat map where seat assignment applies.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Hall ticket generation console with prerequisite checklist display | Medium | 16 |
| UI | Hall ticket generation batch progress and status register | Medium | 16 |
| UI | Hall ticket template preview dialog with sample candidate data | Easy | 14 |
| UI | Regenerate single candidate hall ticket dialog with reason | Simple | 5 |
| UI | Failed hall ticket generation retry action row control | Simple | 5 |
| UI | Candidate portal hall ticket detail view page | Medium | 16 |
| UI | Candidate portal hall ticket download PDF action | Easy | 14 |
| UI | Candidate portal hall ticket print-friendly view | Easy | 14 |
| UI | Candidate portal hall ticket not-yet-available empty state | Simple | 5 |
| UI | Candidate portal hall ticket generation failed error state | Simple | 5 |
| API | Evaluate candidate hall ticket eligibility with reason codes | Medium | 6 |
| API | Queue batch hall ticket generation for eligible candidates | Complex | 8 |
| API | List hall ticket generation status with filters | Medium | 6 |
| API | Regenerate hall ticket for single candidate with versioning | Medium | 6 |
| API | Retry failed hall ticket generation for candidate | Easy | 4 |
| API | Get candidate portal hall ticket display data | Easy | 4 |
| API | Download candidate hall ticket PDF document | Medium | 6 |
| Database | Hall ticket record with document reference and version persistence | Medium | 0.3 |
| Database | Hall ticket generation batch job status persistence | Easy | 0.25 |
| Database | Hall ticket regeneration history and audit persistence | Easy | 0.25 |
| Integration | Internal PDF document rendering service call for hall ticket template | Simple | 4 |
| Testing | Happy-path batch generation, candidate view, download, and print | Medium | 0.3 |
| Testing | Negative cases for blocked generation when allocation or seat lock missing | Medium | 0.3 |
| Testing | Edge and security cases for cross-candidate access denial, regeneration versioning, and retry | Complex | 0.5 |
| Documentation | Examination Administrator runbook for hall ticket batch generation and regeneration | Medium | 0.3 |
| Documentation | Candidate user guide for hall ticket download and print | Easy | 0.25 |
| Documentation | Technical notes for eligibility gating and document version model | Medium | 0.3 |

### F06-005 Examination Credential Generation and Secure Distribution Handoff

154.25 hours · Go-live · 25 tasks

##### Description

Generates unique examination login identifiers and passwords for candidates after schedule finalisation and eligible allocation state. Stores credentials securely, exposes administrator batch generation and regeneration controls, and hands off masked credential dispatch requests to the Notification Service via approved SMS and email channels without exposing plaintext passwords in administrative list views.

##### Business objective

Ensure each candidate receives unique, secure examination login credentials through approved communication channels only after scheduling and allocation are complete, enabling examination day login without administrator manual password handling.

##### Actors

- Examination Administrator
- Candidate

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Examination identifier
- Published session schedule finalisation confirmation
- Candidate identifiers in eligible scope
- Regenerate credentials reason text
- Resend dispatch handoff confirmation
- Notification template routing identifiers from Module 07
- Dispatch status callback payload from Notification Service

##### Outputs

- Examination login ID per candidate
- Securely hashed examination password record
- Credential generation batch status
- Distribution handoff request with correlation identifier
- Dispatch status per candidate (Pending, Dispatched, Failed)
- Regenerated credential pair with prior credential invalidated flag
- Administrator masked credential status view

##### Business rules

- Credential generation permitted only after examination schedule finalisation policy is satisfied and allocations are Finalised
- Each candidate receives one active examination credential set per examination attempt
- Plaintext password shown only transiently during generation handoff to Notification Service, never in administrator registers
- Regeneration invalidates previous login password pair immediately
- Resend handoff uses current active credential without regenerating unless administrator explicitly regenerates
- Examination conduct login validation is out of scope; credentials prepared for Module 09 consumption

##### Validations

- Eligibility checklist must pass before batch generation accepted
- Login ID must be unique within examination scope
- Generated password meets configured complexity and length rules
- Regenerate reason mandatory on administrator regenerate action
- Handoff blocked when candidate missing registered mobile or email required by channel policy
- Resend allowed only when active credential exists
- Dispatch callback correlation identifier must match existing handoff record

##### Calculations

- Generate random password meeting complexity policy
- Derive credential eligibility from schedule finalisation and allocation composite state

##### Workflow

Not Eligible → Eligible (prerequisites met) → Generated (credential created) → Handoff Pending (dispatch request queued) → Dispatched (Notification Service success callback) | Handoff Pending → Handoff Failed (callback failure) → Handoff Pending (resend) | Generated → Invalidated (regenerate action) → Generated (new active credential).

##### Search requirements

- Administrator search credential register by candidate name, registration number, login ID
- Filter by generation status, dispatch status, examination, session
- Sort by generation timestamp and dispatch status

##### Reports

- Credential generation and dispatch status summary export for examination readiness review

##### Notifications

- Examination credential dispatch handoff event to Module 07 for SMS delivery
- Examination credential dispatch handoff event to Module 07 for email delivery
- Credential regeneration notification handoff when policy requires informing candidate

##### Security

- Passwords stored hashed; plaintext never persisted in database or audit tables
- Administrator views show login ID and masked password indicator only
- Handoff payload encrypted in transit to Notification Service
- Regenerate and handoff actions restricted to Examination Administrator credential permission
- Rate limit resend handoff to prevent abuse

##### Integrations

- Module 07 Notification Service secure credential dispatch handoff API
- Module 07 dispatch status callback ingestion

##### Dependencies

- F06-001 — Published and finalised examination session schedules
- F06-002 — Finalised candidate allocation
- Module 07 — Notification Template Catalog, channel configuration, and dispatch engine
- Module 05 — Candidate registered mobile and email contact points
- Module 01 — Examination Administrator credential management permissions
- Module 09 — Secure Examination Conduct consumes generated credentials at login time

##### Assumptions

- Notification Service owns template wording and channel provider delivery
- Schedule finalisation for credentials aligns with Published schedule state plus optional administrator explicit finalisation flag
- Complexity drivers: secure secret handling, handoff idempotency, and dispatch status callback reconciliation

##### Risks

- Credential delivery failure leaves candidates without login details near examination time
- Regeneration after dispatch may confuse candidates receiving multiple messages
- Misconfigured Notification templates may expose credentials improperly if template not masked

##### Non-functional requirements

- Batch credential generation completes for examination-wide volumes
- Handoff processing idempotent to avoid duplicate SMS/email sends
- Credential hash algorithm meets organisational security standards

##### Notes

Credential plaintext distribution executed by Module 07 Notification Service; this feature generates credentials and hands off secure dispatch requests.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Examination credential generation console with eligibility checklist | Medium | 16 |
| UI | Credential generation and dispatch status register with masked secrets | Medium | 16 |
| UI | Generate credentials batch confirmation dialog | Simple | 5 |
| UI | Regenerate candidate credentials dialog with mandatory reason | Simple | 5 |
| UI | Initiate distribution handoff batch confirmation dialog | Simple | 5 |
| UI | Resend distribution handoff single candidate confirmation dialog | Simple | 5 |
| UI | Credential register empty state when prerequisites unmet | Simple | 5 |
| UI | Dispatch failed error state row with retry handoff action | Easy | 14 |
| API | Evaluate credential generation eligibility with reason codes | Medium | 6 |
| API | Generate examination login ID and password batch with hashing | Complex | 8 |
| API | List credential generation and dispatch status with filters | Medium | 6 |
| API | Regenerate single candidate credentials invalidating prior active set | Complex | 8 |
| API | Initiate secure distribution handoff batch to Notification Service | Complex | 8 |
| API | Resend secure distribution handoff for single candidate | Medium | 6 |
| API | Ingest dispatch status callback from Notification Service | Medium | 6 |
| Database | Examination credential record with hashed password persistence | Medium | 0.3 |
| Database | Credential generation batch and invalidation history persistence | Easy | 0.25 |
| Database | Distribution handoff correlation and dispatch status persistence | Medium | 0.3 |
| Integration | Notification Service secure credential dispatch handoff publish | Medium | 16 |
| Integration | Notification Service dispatch status callback mapping and retry handling | Medium | 16 |
| Testing | Happy-path credential generate, handoff, and dispatch status update | Medium | 0.3 |
| Testing | Negative validation for missing contact channel, weak password policy, and blocked prerequisites | Medium | 0.3 |
| Testing | Edge and security cases for regenerate invalidation, masked admin views, idempotent handoff, and hash storage | Very high | 1 |
| Documentation | Examination Administrator runbook for credential generation, handoff, and resend | Medium | 0.3 |
| Documentation | Technical security notes for hashing, handoff payload, and callback reconciliation | Complex | 0.5 |
