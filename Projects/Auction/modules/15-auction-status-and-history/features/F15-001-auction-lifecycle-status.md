# F15-001 — Auction Lifecycle Status

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-001 |
| **Feature Name** | Auction Lifecycle Status |
| **Module** | 15 — Auction Status and History |

### Description
Authorised users see the current stage of an auction: draft, submitted, returned, approved, published, participation, under evaluation when the flag is yes, eligible list final, live, extended, closed, ranked, finalisation submitted or returned or approved, awarded, letter issued, and completed. A force close is shown as a closed auction whose closure type is force close. Ordinary users do not type a new status. The stage changes because a business action happened.

### Business Objective
Anyone allowed to open the auction can see where it is, including whether evaluation applies, without editing the stage by hand.

### Actors
Reader: department staff according to their role, and the bidder for the limited status they are allowed to see. Maker: the business actions in other modules. Approver: none here.

### User Journey
1. Who creates: no one creates a status by hand. Each business action moves it.
2. How they create: submitting, approving, publishing, starting participation by the clock, evaluating, going live, extending, closing, ranking, finalising, awarding, issuing the letter, and completing all move the stage.
3. How they edit: there is no status drop-down for ordinary users.
4. How they send for approval: they do not, on this screen.
5. How the approver sees pending items: inboxes live in the owning modules. This screen shows the resulting stage.
6. How the approver decides: not here.
7. How the maker sees history: the creator sees the current stage on the draft register and on the auction.
8. How the auditor sees history: staff see the stage and the closure type. The bidder sees a reduced stage: not visible, published, participation open, live, closed, and, if they are the successful bidder, letter issued. They do not see internal labels such as returned or finalisation submitted.

### Functional Capabilities
- Show the current stage from the business actions
- Show the evaluation branch only when evaluation is yes
- Show force close as the closure type on a closed auction
- Show the bidder a reduced stage list
- Refuse a manual status edit

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- The auction and the last business action

### Outputs
- Current stage for staff or the reduced stage for a bidder

### Business Rules
- Status is a consequence, not a field the creator edits except by doing the real action (submit, and so on).
- Evaluation stages are absent when the flag is no. Those auctions go from participation to live for eligible participants.
- Extended is still a live auction. The stage shows that the end has moved.
- Completed is reached only through F13-003.
- Bidders do not see draft, submitted, returned, or internal approval labels.

### Validations
- The reader is allowed to know the auction.
- A bidder’s request for an internal stage is refused.

### Calculations
None. The stage is the latest applicable business state.

### Workflow
The workflow is the lifecycle in the Statement of Work. This feature displays it.

### Search Requirements
Staff filter auctions by stage and by closure type.

### Documents
None.

### Reports
None.

### Notifications
None. The events that move the stage already notify.

### Security
Department scope for staff. Bidder reduction rules as above.

### Integrations
None.

### Dependencies
Modules 04 through 13 write the stage. This feature reads it.

### Assumptions
- Labels follow the Statement of Work appendix. Wording on screen may be shortened, but the sequence and the evaluation branch may not be dropped.
- Clock-driven stages (participation open, live) change because server time crossed the schedule, not because a user picked them.

### Risks
A bidder-facing label that leaks ‘returned for correction’ would expose internal review. The reduced list is therefore explicit.

### Non Functional Requirements
The stage shown to two staff users of the same auction is the same stage.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction status tracker | UI | Medium | 6 |
| Staff auction stage board | UI | Easy | 4 |
| Read auction status | API | Medium | 6 |
| Advance auction lifecycle status | API | Complex | 8 |
| Auction status records | DB | Medium | 4 |
| Auction status tests | Testing | Medium | 6 |
| Auction status notes | Documentation | Easy | 2 |

**Feature total: 36 hours**
