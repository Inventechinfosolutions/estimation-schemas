# F05-001 — Examination Schedule Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Examination Schedule Management |
| **Module** | 05 — Scheduling, Allocation, Hall Tickets and Examination Credentials |

### Description
Examination Administrators create and manage examination schedules including examination name linkage, date, time, duration, reporting time, participating centres, seats/capacity and instructions. Schedules must exist before centre allocation and hall ticket publication.

### Business Objective
Establish authoritative session definitions so candidates can be allocated to centres and attend only scheduled, capacity-controlled sittings.

### Actors
Maker: Examination Administrator. Approver: none by default (publish is an admin action, not a separate checker inbox unless Department later requires dual control). Auditor: Examination Administrator / audit via change history.

### User Journey
1. Who creates: Examination Administrator.
2. How they create: Schedule register → New → enter examination, date/time, duration, reporting time, map centres with capacity, enter instructions → save as draft → publish when ready.
3. How they edit: Update draft schedules freely; published schedules allow controlled edits (capacity/instructions/time) with audit; cancellation/deactivation when no longer usable for allocation.
4. How they send for approval: Does not apply as a maker–checker workflow — the same administrator publishes the schedule. If dual control is later mandated, it would be a configuration change outside this baseline.
5. How the approver sees pending items: No separate approver inbox; draft vs published states appear on the schedule register.
6. How the approver decides: No second-person decision in baseline; publish/deactivate are administrator actions.
7. How the applicant / maker sees history: Administrator views schedule change history for each schedule record.
8. How the approver / auditor sees history: Same history screen supports audit of who published, changed capacity or deactivated.

### Functional Capabilities
- Create schedules linked to examinations from Module 03.
- Capture date, session time, duration and reporting time.
- Map one or more authorised centres with seat/capacity figures.
- Capture candidate-facing instructions for the session.
- Draft vs published lifecycle for schedules.
- Prevent use of unpublished schedules in allocation/hall ticket publish.
- Deactivate or cancel schedules with reason.
- Calendar-oriented view of upcoming sessions.
- Validate that centre capacities do not exceed centre master limits where configured.
- Block conflicting double-booking of the same centre slot when rules require.
- Audit all create/update/publish/deactivate events.
- Search/filter schedule register by examination, date, centre and status.

### UI Screens
| Screen | Purpose |
|---|---|
| Examination schedule register | List/filter schedules by status and exam |
| Schedule create and edit form | Capture schedule particulars |
| Centre and capacity mapping grid | Map centres and seats for the session |
| Schedule publish confirmation screen | Confirm publish of a draft schedule |
| Schedule calendar view | Visual upcoming sessions |
| Schedule change history screen | Audit of schedule changes |

### Logical API operations
| Operation | Purpose |
|---|---|
| List examination schedules | Register query with filters |
| Create examination schedule | Persist new draft schedule |
| Update examination schedule | Persist edits with validation |
| Publish examination schedule | Move draft to published |
| Deactivate or cancel schedule | Withdraw schedule from use |
| Get schedule change history | Return audit trail |

### Inputs
Examination; date; time; duration; reporting time; centre mappings; capacities; instructions; publish/deactivate actions; administrator identity.

### Outputs
Schedule records; published schedule available for allocation; history events.

### Business Rules
- Only active authorised centres may be mapped.
- Hall tickets and allocation consume published schedules only.
- Capacity on schedule cannot exceed centre master capacity when that rule is enabled.
- Duration aligns with examination parameters where Module 03 defines them.

### Validations
- Mandatory schedule fields; end after start; positive capacity; unique centre rows per schedule.
- Publish only when at least one centre mapped (unless Department allows TBA — baseline requires centres).

### Calculations
Aggregate session capacity across mapped centres for display.

### Workflow
Draft schedule → map centres/capacity → publish → available for F05-002. Deactivate ends further allocation use. No checker inbox in baseline.

### Search Requirements
By examination, date range, centre, published/draft/cancelled status.

### Documents
None required; instructions are text fields (attachments only if later configured — not baseline).

### Reports
Schedule lists feed Module 09 operational views.

### Notifications
Optional publish notifications via Module 09; not mandatory for schedule create.

### Security
Examination Administrator only; centre users do not create system-wide schedules.

### Integrations
None.

### Dependencies
Module 03 examination and centre masters; enables F05-002–F05-004.

### Assumptions
- Baseline is single-admin publish without maker–checker.
- Exact conflict rules finalised with Department; validation hooks included.

### Risks
Late schedule changes after allocation cause rework on hall tickets/credentials.

### Non Functional Requirements
Clear calendar usability; audited publish actions; consistent timezone handling as Department directs.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Examination schedule register | UI | Medium | 6 |
| Schedule create and edit form | UI | Complex | 12 |
| Centre and capacity mapping grid | UI | Complex | 12 |
| Schedule publish confirmation screen | UI | Easy | 4 |
| Schedule calendar view | UI | Very High | 16 |
| Schedule change history screen | UI | Easy | 4 |
| List examination schedules | API | Medium | 6 |
| Create examination schedule | API | Complex | 8 |
| Update examination schedule | API | Complex | 8 |
| Publish examination schedule | API | Medium | 6 |
| Deactivate or cancel schedule | API | Medium | 6 |
| Get schedule change history | API | Easy | 4 |
| Schedule and centre-capacity persistence | Database | Complex | 6 |
| Examination schedule management tests | Testing | Complex | 8 |
| Examination schedule management documentation | Documentation | Medium | 3 |

**Feature total: 109 hours**

### Estimation Assumptions
- Calendar view billed Very High UI for multi-centre session visualisation.
- Allocation engine hours remain on F05-002.
