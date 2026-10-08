# ChatGPT Visualization Brief — F06-003: Candidate Seat and Computer Assignment

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `Feature_Specs/M06_examination-scheduling-and-allocation.md`  
**Module:** 06 Examination Scheduling & Allocation  
**Feature:** F06-003 — Candidate Seat and Computer Assignment  
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql`  
**Primary table:** `seat_assignment`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the feature specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Auto-assign seats → review → manual reassign → lock seat map pipeline
2. Seat uniqueness / conflict detection decision flowchart
3. Seat assignment state machine (Unassigned → Assigned → Locked / Unlocked / Reassigned)
4. Seating register UI information architecture (list/grid, conflict dialog, export)
5. ERD for `seat_assignment` with unique (exam_session, seat_label) constraint callout
6. Dependency map: F06-003 ↔ F06-001/002, Module 03 inventory, downstream F06-004

Do not invent features outside this specification. Do not include estimation hours or task tables.

---

### FEATURE OVERVIEW

**ID:** F06-003  
**Name:** Candidate Seat and Computer Assignment  
**Module:** 06 Examination Scheduling & Allocation  
**Primary data objects:** `seat_assignment`, `candidate_allocation`, `exam_session`

### FEATURE SPECIFICATION

#### F06-003 — Candidate Seat and Computer Assignment

**One-liner / description:** Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection, seating…

**Full description:** Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection, seating register views, and seat-map lock prior to hall ticket generation.

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

**Inputs:**
- Finalised session schedule identifier
- Centre identifier
- Candidate allocation identifiers within session
- Available seat or computer identifier pool from centre infrastructure
- Manual seat or computer selection
- Reassignment reason text
- Lock seat map confirmation

**Outputs:**
- Candidate seat or computer assignment record per session
- Auto-assignment batch summary
- Seating register view data
- Seat map locked status flag
- Seat conflict error detail
- Seating register export file
- Seat assignment change audit entries

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

**Calculations:**
- Count assigned versus unassigned candidates for session
- Compute next available seat identifier during auto-assign sequence

**Workflow / states:** Unassigned → Assigned (auto or manual assign) → Locked (lock seat map action) | Assigned → Reassigned (manual change before or after unlock) | Locked → Unlocked (administrator unlock for corrections).

**Search requirements:**
- Search seating register by candidate name or registration number
- Filter by assignment status (Unassigned, Assigned)
- Filter by seat or computer identifier
- Sort by seat identifier or candidate name

**Reports:**
- Session seating register export for centre invigilator coordination

**Security:**
- Only Examination Administrator with seat assignment permission may assign or lock seats
- Centre invigilator roles receive read-only seating visibility via Module 08 dependency only
- All lock, unlock, and reassignment actions audit-logged

**Dependencies:**
- F06-002 — Finalised candidate centre and session allocation
- Module 03 — Centre Capacity and Infrastructure Configuration (seat or computer inventory)
- F06-001 — Published session schedule context
- Module 01 — Examination Administrator seat assignment permissions

**Assumptions:**
- Seat/computer identifiers are pre-configured numeric or labelled inventory in Module 03
- Examinations not requiring computer assignment still use seat numbering from same inventory model
- Complexity drivers: uniqueness enforcement, lock/unlock governance, and auto-assign sequencing

**Risks:** Centre infrastructure changes after seat lock may invalidate assignments; Auto-assign ordering may not respect special accommodation needs without manual override

**Non-functional requirements:**
- Auto-assign completes for full session candidate count within operational time limits
- Seating register supports centre-scale candidate volumes with pagination

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

> Visualize KEONICS Exam **F06-003 Candidate Seat and Computer Assignment** (Module 06).
> Purpose: Maps finalised candidate allocations to specific seat or computer identifiers within an examination session at an authorised centre. Supports automated seat assignment, manual reassignment, conflict detection, seating…
> Primary table: `seat_assignment`.
> Draw: auto-assign→lock pipeline; uniqueness conflict flowchart; Unassigned→Assigned→Locked state machine; ERD for `seat_assignment` with unique seat per session; dependency to F06-002/004.
