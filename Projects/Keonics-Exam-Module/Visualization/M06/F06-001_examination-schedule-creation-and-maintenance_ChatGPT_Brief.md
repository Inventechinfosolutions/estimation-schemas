# ChatGPT Visualization Brief — F06-001: Examination Schedule Creation and Maintenance

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `Feature_Specs/M06_examination-scheduling-and-allocation.md`  
**Module:** 06 Examination Scheduling & Allocation  
**Feature:** F06-001 — Examination Schedule Creation and Maintenance  
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql`  
**Primary table:** `exam_session`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the feature specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. Schedule create → edit → publish → cancel state machine
2. Administrator schedule-creation swimlane / sequence (form → validation → draft → publish)
3. Capacity and non-overlap validation decision flowchart
4. Schedule register UI information architecture (filters, list, detail, empty state)
5. ERD focused on `exam_session` and links to examination / centre masters
6. Dependency map: F06-001 ↔ Modules 01, 03, 04 and downstream F06-002…005

Do not invent features outside this specification. Do not include estimation hours or task tables.

---

### FEATURE OVERVIEW

**ID:** F06-001  
**Name:** Examination Schedule Creation and Maintenance  
**Module:** 06 Examination Scheduling & Allocation  
**Primary data objects:** `exam_session`

### FEATURE SPECIFICATION

#### F06-001 — Examination Schedule Creation and Maintenance

**One-liner / description:** Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time, dura…

**Full description:** Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time, duration, reporting time, applicable centre, seat capacity, and candidate-facing instructions. Schedules progress through controlled lifecycle states and become the anchor for downstream allocation, hall ticket, and credential generation.

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

**Inputs:**
- Examination identifier (from Examination Master Configuration)
- Authorised examination centre identifier (from Centre Master)
- Session date
- Session start time
- Session duration (minutes)
- Reporting time
- Maximum seat capacity for session
- Examination instructions text
- Cancellation reason (on cancel action)

**Outputs:**
- Draft schedule record
- Published schedule record eligible for allocation
- Cancelled schedule record with reason
- Schedule register search results
- Schedule detail view payload
- Schedule status transition audit entries
- Validation error messages for timing, capacity, and overlap conflicts

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
- No overlapping Published sessions for same centre where session time ranges intersect
- Cancellation reason mandatory when transitioning Published or Draft to Cancelled

**Calculations:**
- Derive session end time from start time plus duration
- Compute remaining allocatable seats as session capacity minus confirmed allocations (display only on detail view)

**Workflow / states:** Draft → Published (publish/finalise action) | Draft → Cancelled (cancel action) | Published → Cancelled (cancel action). Published schedules are not editable for core timing/centre fields without cancel-and-recreate policy (assumption: material fields locked after publish).

**Search requirements:**
- Filter schedule register by examination name or code
- Filter by centre name or code
- Filter by session date range
- Filter by schedule status (Draft, Published, Cancelled)
- Sort by session date, centre, examination, status

**Reports:**
- Schedule register export (CSV) for administrative review

**Security:**
- Only Examination Administrator role with scheduling permission may create, publish, or cancel schedules
- Centre-scoped invigilator roles have no access to schedule maintenance screens
- All publish and cancel actions logged with administrator identity and timestamp

**Dependencies:**
- Module 04 — Examination Master Configuration (examination definitions open for scheduling)
- Module 03 — Authorised Examination Centre Master and Centre Capacity Configuration
- Module 01 — Examination Administrator role and scheduling authorisation permissions

**Assumptions:**
- Centre-examination authorisation and raw capacity values are maintained in Module 03
- Examination definitions and scheduling windows are maintained in Module 04
- Material schedule field edits after publication require cancel-and-recreate rather than in-place edit
- Complexity drivers: overlap detection across centre sessions, capacity cross-check against external centre master, and status-locked edit rules

**Risks:** Late centre capacity changes in Module 03 may invalidate already-published schedules; Overlapping session detection edge cases across midnight boundaries; Administrators may publish schedules before registration cutoff causing allocation churn

**Non-functional requirements:**
- Schedule register list/search response suitable for enterprise volumes (paginated)
- Audit history retained for compliance review
- Validation feedback field-level on create/edit forms

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

> Visualize KEONICS Exam **F06-001 Examination Schedule Creation and Maintenance** (Module 06).
> Purpose: Enables Examination Administrators to create, maintain, publish, and cancel examination session schedules linked to configured examinations and authorised centres. Each schedule captures session date, start time, dura…
> Primary table: `exam_session`.
> Draw: Draft→Published→Cancelled state machine; create/publish sequence; overlap+capacity validation flowchart; ERD for `exam_session`; dependency to M03/M04 and F06-002.
