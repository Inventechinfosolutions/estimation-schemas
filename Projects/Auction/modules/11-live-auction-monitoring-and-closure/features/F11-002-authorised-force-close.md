# F11-002 — Authorised Force Close

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-002 |
| **Feature Name** | Authorised Force Close |
| **Module** | 11 — Live Auction Monitoring and Closure |

### Description
The auctioning authority can close an auction that is still live, before the scheduled end. A reason is mandatory. The auction closes, further bids stop, the closure is written to the history, and accepted bids already taken are retained for ranking.

### Business Objective
The authority can stop a live auction for a recorded reason without waiting for the clock, and without losing the bids already accepted.

### Actors
Maker and decider: Auctioning Authority. Approver: none beyond this authority. The source assigns force close to this role and does not add a second approver.

### User Journey
1. Who creates: the Auctioning Authority creates the force-close record.
2. How they create: on the live auction → Force close → enter the reason → confirm.
3. How they edit: the reason is not edited after confirmation. A mistaken close is not reopened by this feature. Reopening would be a new auction.
4. How they send for approval: they do not. The authority’s confirm is the decision.
5. How the approver sees pending items: there is no second inbox. The confirm dialog is the decision point.
6. How the approver decides: confirming with a reason closes the auction. Cancelling the dialog leaves it live.
7. How the maker sees history: the authority sees the force-close reason, user, and time on the auction.
8. How the auditor sees history: the same event is on the auction history for authorised staff. Bidders see that the auction is closed. They see the reason because the source says the closed status is available in history; the reason is part of that closure record for staff, and bidders are told the auction was closed by the authority without being shown internal commentary beyond the fact of closure.

### Functional Capabilities
- Force close a live auction
- Require a reason
- Stop further bids
- Retain accepted bids
- Record the closure on the history

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Live auction
- Reason

### Outputs
- Closed auction
- History event
- Closure notification

### Business Rules
- Reason is mandatory. Confirm without a reason is refused.
- Only a live auction can be force closed. A scheduled close that has already happened is not force closed again.
- Force close does not delete accepted bids.
- Force close prevents any further delta extension.
- The user must hold Auctioning Authority for the department.

### Validations
- Auction is live.
- Reason is not blank.
- Role and department match.

### Calculations
None.

### Workflow
Live → force closed. Ranking can begin. No second approval.

### Search Requirements
Staff can filter closed auctions by closure type: scheduled or force closed.

### Documents
None.

### Reports
None.

### Notifications
Closure notifies participants and the creator through Module 14.

### Security
Only the auctioning authority. A bidder cannot force close.

### Integrations
None.

### Dependencies
F11-001 console as the place the action is offered. F10 for the bid freeze. Module 14.

### Assumptions
- Bidders are told the auction was closed by the authority. The detailed reason text is visible to staff on the history. The source requires the reason to be recorded; it does not require that prose to be broadcast to every bidder.

### Risks
Force close during a contested auction will be disputed. The reason and the user are therefore mandatory history, not optional notes.

### Non Functional Requirements
After confirm, a bid submit is rejected. The close cannot succeed while still accepting bids.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Force close dialog | UI | Easy | 4 |
| Force close confirmation | UI | Simple | 2 |
| Force close auction | API | Complex | 8 |
| Force close records | DB | Easy | 2 |
| Force close tests | Testing | Medium | 6 |
| Force close notes | Documentation | Easy | 2 |

**Feature total: 24 hours**
