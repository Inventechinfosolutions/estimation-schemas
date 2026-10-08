# ChatGPT Visualization Brief — F06-004: Digital Hall Ticket Generation and Candidate Access

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `Feature_Specs/M06_examination-scheduling-and-allocation.md`  
**Module:** 06 Examination Scheduling & Allocation  
**Feature:** F06-004 — Digital Hall Ticket Generation and Candidate Access  
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql`  
**Primary table:** `hall_ticket`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the feature specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Prerequisite gating flowchart (Published schedule + Finalised allocation + Locked seat map)
2. Admin batch generate → progress → regenerate / retry sequence
3. Candidate portal view → download PDF → print sequence
4. Hall ticket status state machine (Not Eligible → Eligible → Pending → Generated / Failed / Superseded)
5. Hall ticket document content block diagram (identity, exam, centre, session, seat, instructions)
6. ERD for `hall_ticket` including payload / document reference and versioning
7. Dependency map: F06-004 ↔ F06-001/002/003 and Modules 01/03/04/05

Do not invent features outside this specification. Do not include estimation hours or task tables.

---

### FEATURE OVERVIEW

**ID:** F06-004  
**Name:** Digital Hall Ticket Generation and Candidate Access  
**Module:** 06 Examination Scheduling & Allocation  
**Primary data objects:** `hall_ticket`, `candidate_allocation`, `exam_session`, `seat_assignment`

### FEATURE SPECIFICATION

#### F06-004 — Digital Hall Ticket Generation and Candidate Access

**One-liner / description:** Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation, regener…

**Full description:** Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation, regeneration, and status monitoring plus Candidate portal view, download, and print access to hall tickets containing examination, session, centre, reporting time, and seat details.

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

**Inputs:**
- Examination identifier
- Session schedule identifier scope
- Centre identifier scope
- Candidate identifier for regeneration
- Regeneration reason text
- Candidate authenticated portal session

**Outputs:**
- Generated hall ticket PDF document per candidate
- Hall ticket generation batch status records
- Candidate portal hall ticket display payload
- Hall ticket eligibility boolean with reason codes
- Hall ticket version history on regeneration
- Failed generation error detail for administrator retry

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

**Calculations:**
- Derive hall ticket eligibility from composite schedule, allocation, and seat lock states
- Increment hall ticket version number on regeneration

**Workflow / states:** Not Eligible → Eligible (prerequisites satisfied) → Generation Pending → Generated (success) | Generation Pending → Failed (error) → Generation Pending (retry) | Generated → Superseded (regeneration creates new current version).

**Search requirements:**
- Administrator search generation register by candidate name, registration number, status
- Filter by examination, session date, centre, generation status
- Sort by generation timestamp and status

**Documents:**
- Hall ticket PDF document with examination, centre, session, reporting time, seat, and instructions
- Print-friendly hall ticket render

**Reports:**
- Hall ticket generation batch summary with success and failure counts

**Security:**
- Candidate hall ticket access restricted to authenticated owner
- Hall ticket PDF served through authorised download token or session check
- Administrator regeneration and batch actions audit-logged
- Hall ticket document storage access limited to application document service

**Integrations:**
- Internal document rendering service for PDF hall ticket generation

**Dependencies:**
- F06-001 — Published examination session schedules
- F06-002 — Finalised candidate centre and session allocation
- F06-003 — Locked seat or computer assignment when applicable
- Module 05 — Candidate identity and registration details for hall ticket content
- Module 03 — Centre name and address for hall ticket display
- Module 04 — Examination name and instructions configuration
- Module 01 — Candidate portal authentication and administrator hall ticket permissions

**Assumptions:**
- PDF template layout approved by department; branding fields supplied from configuration
- Document storage uses platform blob storage pattern
- Complexity drivers: prerequisite gating chain, batch generation monitoring, and PDF render integration

**Risks:** Late allocation or seat changes after generation require mass regeneration; PDF generation failures at scale may delay candidate access close to exam date; Candidate downloads from shared devices pose informational disclosure risk mitigated by authentication

**Non-functional requirements:**
- Batch generation supports examination-wide candidate volumes asynchronously
- PDF download responsive for candidate portal usage
- Generated documents retained per records retention policy

**Notes:** Hall ticket availability requires completed scheduling, finalised allocation, and locked seat map where seat assignment applies.

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

> Visualize KEONICS Exam **F06-004 Digital Hall Ticket Generation and Candidate Access** (Module 06).
> Purpose: Generates digital hall tickets for candidates after examination scheduling, centre allocation finalisation, and seat assignment prerequisites are satisfied. Provides Examination Administrator batch generation, regener…
> Primary table: `hall_ticket`.
> Draw: prerequisite gating flowchart; admin generate + candidate download sequences; eligibility/generation state machine; hall ticket content blocks; ERD for `hall_ticket`.
