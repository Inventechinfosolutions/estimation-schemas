# ChatGPT Visualization Brief — F06-002: Candidate Centre and Session Allocation

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `Feature_Specs/M06_examination-scheduling-and-allocation.md`  
**Module:** 06 Examination Scheduling & Allocation  
**Feature:** F06-002 — Candidate Centre and Session Allocation  
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql`  
**Primary table:** `candidate_allocation`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the feature specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Auto-allocation wizard sequence (scope → preview → execute → review → finalise)
2. Preference 1 / Preference 2 / fallback allocation decision flowchart
3. Allocation lifecycle state machine (Pending → Allocated → Finalised / Reallocated / Reopened)
4. Administrator + Candidate swimlanes (admin allocate vs candidate portal allotment view)
5. ERD for `candidate_allocation` linked to `exam_session` and registration
6. Dependency map: F06-002 ↔ F06-001, Modules 01/03/04/05, downstream F06-003/004/005

Do not invent features outside this specification. Do not include estimation hours or task tables.

---

### FEATURE OVERVIEW

**ID:** F06-002  
**Name:** Candidate Centre and Session Allocation  
**Module:** 06 Examination Scheduling & Allocation  
**Primary data objects:** `candidate_allocation`, `exam_session`

### FEATURE SPECIFICATION

#### F06-002 — Candidate Centre and Session Allocation

**One-liner / description:** Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and departme…

**Full description:** Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and department business rules. Supports automated batch allocation with preview, exception handling, manual override, and finalisation that locks allocations for seat assignment and hall ticket generation.

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

**Inputs:**
- Examination identifier
- Published session schedule identifiers in scope
- Registered candidate identifiers with completed registration
- Centre preference 1 and preference 2 from registration
- Candidate category (Government employee, PSU/Board, etc.)
- Manual override centre identifier
- Manual override session schedule identifier
- Override reason text
- Allocation batch finalise confirmation

**Outputs:**
- Candidate-to-centre-to-session allocation record
- Allocation preview result set
- Allocation batch run summary with allocated, fallback, and unallocated counts
- Finalised allocation lock state
- Candidate portal allotted centre and session display
- Exception/unallocated candidate list
- Allocation override audit entries

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

**Calculations:**
- Compute remaining session capacity during allocation preview and execution
- Derive preference satisfaction tier (Preference 1 matched, Preference 2 matched, Non-preference fallback)
- Count allocated, fallback-allocated, and unallocated candidates per batch run

**Workflow / states:** Pending → Allocated (auto or manual assignment) → Finalised (finalise batch action) | Allocated → Reallocated (manual override before hall ticket lock) | Finalised → Reopened (administrator reopen policy assumption for pre-hall-ticket corrections only).

**Search requirements:**
- Search candidates in allocation register by name, registration number, mobile
- Filter by allocation status (Pending, Allocated, Finalised, Unallocated exception)
- Filter by candidate category
- Filter by allotted centre or session date
- Sort by preference match tier and registration date

**Reports:**
- Allocation batch summary report with preference match statistics
- Unallocated candidate exception export

**Security:**
- Only Examination Administrator with allocation permission may run batch, override, or finalise
- Candidates may view only their own allotted centre and session
- Override and batch run actions audit-logged with administrator identity

**Dependencies:**
- F06-001 — Published examination session schedules
- Module 05 — Candidate Registration with centre preferences and registration completion status
- Module 03 — Authorised centres and capacity configuration
- Module 04 — Examination Master Configuration and category eligibility rules
- Module 01 — Examination Administrator allocation permissions

**Assumptions:**
- Centre preferences captured during Module 05 registration are snapshot-read at allocation time
- Category-based centre restrictions are configurable via examination business rules from Module 04
- Complexity drivers: multi-rule batch engine, preview/commit pattern, and manual override audit
- Force-finalise with unallocated exceptions is policy-gated and off by default

**Risks:** Preference saturation at popular centres causing high fallback rates; Concurrent allocation runs against same session may cause capacity race conditions; Registration data changes after allocation may desynchronise candidate category rules

**Non-functional requirements:**
- Batch allocation preview completes within acceptable time for examination-sized candidate volumes
- Allocation decisions fully auditable for grievance review
- Candidate portal allotment view reflects finalised state within normal replication latency

---

### MODULE PIPELINE CONTEXT (for dependency diagrams only)

```text
F06-001 Schedule → F06-002 Allocation → F06-003 Seat → F06-004 Hall Ticket
                              ↘ F06-005 Credentials → Module 07 Notify → Module 09 Conduct
```

Upstream modules commonly involved: 01 IAM · 03 Centre · 04 Config · 05 Registration.  
Highlight only dependencies listed for this feature.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: this feature’s services vs other Module 06 features vs external modules
- Call out audit, security, capacity, and lock/finalise gates explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **F06-002 Candidate Centre and Session Allocation** (Module 06).
> Purpose: Allocates registered candidates to published examination sessions and authorised centres using captured centre preferences, centre availability, session capacity, examination schedule, candidate category, and departme…
> Primary table: `candidate_allocation`.
> Draw: Pref1→Pref2→fallback flowchart; allocation wizard sequence; Pending→Allocated→Finalised state machine; ERD for `candidate_allocation`; admin vs candidate swimlanes.
