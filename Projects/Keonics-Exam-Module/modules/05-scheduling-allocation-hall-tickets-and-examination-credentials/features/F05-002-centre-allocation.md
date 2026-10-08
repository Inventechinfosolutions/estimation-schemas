# F05-002 — Centre Allocation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Centre Allocation |
| **Module** | 05 — Scheduling, Allocation, Hall Tickets and Examination Credentials |

### Description
Allocate confirmed (and verified, where required) candidates to examination centres for a published schedule using centre preferences, availability, capacity, schedule, category and other Department rules. The final allotted centre is what appears later on the hall ticket.

### Business Objective
Produce fair, capacity-respecting centre allotments that honour preferences where possible and produce a definitive centre for each scheduled candidate.

### Actors
Maker: Examination Administrator running allocation. Approver: none in baseline (commit allocation is admin action). Auditor: Examination Administrator via allocation audit history. Applicant: Candidate (sees final centre after hall ticket publish).

### User Journey
1. Who creates: Examination Administrator initiates allocation for a published schedule and examination cohort.
2. How they create: Open allocation workspace → load eligible candidates → review preference vs capacity → run auto allocation → review results → apply manual overrides where permitted → commit allocation.
3. How they edit: Before hall ticket publish lock, admin may re-run or override individual allotments within capacity; after publish, changes follow controlled re-allocation policy with audit.
4. How they send for approval: Does not apply — allocation commit is not a separate checker workflow in baseline.
5. How the approver sees pending items: No approver inbox; unallocated / exception lists appear inside the allocation workspace.
6. How the approver decides: No second-person approve; administrator commits or adjusts.
7. How the applicant / maker sees history: Candidate sees final allotted centre on hall ticket (F05-003), not the admin workspace; admin maker sees run history in allocation audit.
8. How the approver / auditor sees history: Allocation audit history shows auto-run parameters, overrides, actor and timestamps.

### Functional Capabilities
- Load eligible candidates (confirmed registration; verified if configured; fee compliant).
- Consider preference 1 then preference 2 against remaining capacity.
- Apply capacity limits from schedule-centre mapping.
- Apply category and other Department allocation rules.
- Run auto allocation producing provisional results.
- Support manual override of individual allotments with reason.
- Validate no over-capacity commits.
- Commit allocation as final for hall ticket generation.
- Show preference vs allotment outcome for operations review.
- Handle unallocated exceptions with clear reasons.
- Prevent allocation against unpublished schedules.
- Full audit of runs, overrides and commits.
- Search committed allocations by centre, candidate, examination.

### UI Screens
| Screen | Purpose |
|---|---|
| Centre allocation workspace | Operational hub for a schedule/exam |
| Preference versus capacity view | Compare demand to seats |
| Auto allocation run confirmation screen | Confirm parameters before run |
| Manual allocation override form | Change individual allotment with reason |
| Allocation results register | Review committed/provisional results |
| Allocation audit history screen | Runs, overrides and commits trail |

### Logical API operations
| Operation | Purpose |
|---|---|
| Load eligible candidates for allocation | Cohort query with eligibility gates |
| Run automatic centre allocation | Apply preference/capacity/rules engine |
| Apply manual allocation override | Persist override with reason |
| Validate centre capacity for commit | Block over-capacity |
| Commit centre allocations | Finalise allotments for hall tickets |
| Search committed allocations | Operational search |
| Get allocation audit history | Return run/override trail |

### Inputs
Published schedule; examination; candidate preferences; capacities; category/rules; override reasons; administrator identity.

### Outputs
Provisional and committed centre allotments; exception list; audit events; readiness for F05-003.

### Business Rules
- Preferences are inputs, not guarantees.
- Final allotted centre must match a centre on the schedule the candidate may attend.
- Hall ticket unavailable until allocation committed (with schedule).
- Over-capacity commits are forbidden.
- Only eligible registrations are allocated.

### Validations
- Schedule published; capacities positive; override target centre on schedule; candidate eligible.

### Calculations
Remaining capacity per centre; preference satisfaction counts for operational display.

### Workflow
Published schedule → load eligible → auto allocate → review/override → validate capacity → commit → available for hall tickets/credentials. No checker inbox.

### Search Requirements
By registration number, name, preferred centres, allotted centre, unallocated flag.

### Documents
None.

### Reports
Allocation summary by centre feeds Module 09.

### Notifications
Allocation/hall-ticket readiness notifications owned with F05-003 / Module 09.

### Security
Administrator-only allocation controls; candidates cannot self-allot.

### Integrations
None.

### Dependencies
F04 confirmed registrations; F05-001 published schedules; Module 03 centres; enables F05-003/F05-004.

### Assumptions
- Detailed scoring weights for preferences finalised with Department; engine hooks included as Complex/Very High API.
- Dual-control approval not in baseline.

### Risks
Preference conflict under constrained capacity increases manual overrides and candidate complaints.

### Non Functional Requirements
Allocation run performs at cohort volume; auditable overrides; clear exception messaging.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Centre allocation workspace | UI | Very High | 16 |
| Preference versus capacity view | UI | Complex | 12 |
| Auto allocation run confirmation screen | UI | Medium | 6 |
| Manual allocation override form | UI | Complex | 12 |
| Allocation results register | UI | Medium | 6 |
| Allocation audit history screen | UI | Easy | 4 |
| Load eligible candidates for allocation | API | Medium | 6 |
| Run automatic centre allocation | API | Very High | 16 |
| Apply manual allocation override | API | Complex | 8 |
| Validate centre capacity for commit | API | Medium | 6 |
| Commit centre allocations | API | Complex | 8 |
| Search committed allocations | API | Medium | 6 |
| Get allocation audit history | API | Easy | 4 |
| Allocation result persistence | Database | Complex | 6 |
| Centre allocation tests | Testing | Very High | 12 |
| Centre allocation implementation documentation | Documentation | Complex | 4 |

**Feature total: 132 hours**

### Estimation Assumptions
- Auto allocation API billed Very High for rules + transaction orchestration.
- Hall ticket generation hours remain on F05-003.
