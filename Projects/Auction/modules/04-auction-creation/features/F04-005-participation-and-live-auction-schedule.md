# F04-005 — Participation and Live Auction Schedule

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-005 |
| **Feature Name** | Participation and Live Auction Schedule |
| **Module** | 04 — Auction Creation |

### Description
The creator sets Participation Start, Participation End, Live Auction Start, and Live Auction End, in that order. They also set delta time to either 15 or 30 minutes, and the next-day continuation cutoff that stops an extension from running too far into the following day.

### Business Objective
Participation, live bidding, queries, and automatic extension all use one validated timetable.

### Actors
Maker: Auction Creator. Approver: none on this step.

### User Journey
1. Who creates: the Auction Creator enters the timetable on the draft.
2. How they create: Schedule step → four date-times in order, delta 15 or 30 minutes, next-day cutoff clock time → Save.
3. How they edit: while the draft is editable, they change the four points, the delta, or the cutoff. After publication, timetable changes are a corrigendum, not a silent edit.
4. How they send for approval: not from this step.
5. How the approver sees pending items: the reviewer checks the timetable in the dossier.
6. How the approver decides: not on this feature.
7. How the maker sees history: timetable revisions are stored on the draft.
8. How the auditor sees history: the reviewing authority sees those revisions.

### Functional Capabilities
- Capture the four schedule points in the required order
- Allow only a 15 or 30 minute delta
- Capture the next-day continuation cutoff
- Reject a timetable that overlaps the stages

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Participation start
- Participation end
- Live auction start
- Live auction end
- Delta time
- Next-day cutoff

### Outputs
- The timetable that publication, participation, live bidding, and extension will enforce

### Business Rules
- Participation Start is before Participation End, which is before Live Auction Start, which is before Live Auction End.
- Delta time is 15 or 30 minutes. No other value can be stored.
- The next-day cutoff is a clock time. An extension in F10-003 may not push the live end past that cutoff on the following day.
- The query window sits inside the participation period. This feature does not create a second calendar.

### Validations
- All six values are required before submit.
- The sequence is checked on save.
- Delta is restricted to the two allowed values.
- Live start in the past is rejected on submit.

### Calculations
The sequence comparison is the only calculation. Extension arithmetic runs later, using the delta stored here.

### Workflow
Draft save. Locked after submit until return.

### Search Requirements
Creator can filter drafts by live-auction date.

### Documents
None.

### Reports
None.

### Notifications
None on edit. Live-commencement notification uses the published start.

### Security
Same as the rest of the draft: creator, then reviewer. Bidders see the schedule only after publication.

### Integrations
None.

### Dependencies
F04-001 draft.

### Assumptions
- Times are in the organisation’s single local timezone. The source does not describe multiple zones.
- The cutoff is set per auction because the source does not fix one default clock time.

### Risks
A timetable that is valid at submit can still be tight for bidders. That is a business choice the reviewer is expected to check.

### Non Functional Requirements
The saved order is the order later features enforce. They do not re-interpret an inconsistent draft because an inconsistent draft cannot be submitted.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Schedule and extension rules step | UI | Complex | 12 |
| Save auction schedule | API | Complex | 8 |
| Validate schedule sequence | API | Medium | 6 |
| Auction schedule records | DB | Easy | 2 |
| Auction schedule tests | Testing | Complex | 8 |
| Auction schedule notes | Documentation | Medium | 3 |

**Feature total: 39 hours**
