# F10-002 — Live Bid Validation and Visibility

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-002 |
| **Feature Name** | Live Bid Validation and Visibility |
| **Module** | 10 — Live Auction Bidding and Extension |

### Description
Every live submission is checked against the bid-change price, the auction direction, the item or lot, the server time, the bidder’s eligibility, and whether the auction is still live. Display flags decide whether the bidder sees the reserve price, the last accepted bid, and the bidder list. When identity is masked, the bidder does not see who else is bidding. A failed check leaves the current bid unchanged.

### Business Objective
The current bid moves only when the published rules say it may, and bidders see only what the auction was configured to show.

### Actors
The bidder submits. The system applies the rules. The auctioning authority does not approve each bid. Approver: none.

### User Journey
1. Who creates: the bidder’s submission in F10-001 creates the attempt. This feature creates the accept or reject outcome.
2. How they create: there is no separate form. The outcome is returned on submit: accepted, or rejected with a reason the bidder can read.
3. How they edit: staff do not override a rejection from this screen. A bidder submits a new amount if they still have time.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no inbox of bids waiting for a person.
6. How the approver decides: there is no human decision.
7. How the maker sees history: the bidder sees the rejection reason on their own attempt.
8. How the auditor sees history: the auctioning authority can see accepted bids and, on the monitor, the activity the masking rules allow them to operate with. Rejection reasons for a bidder are not broadcast to other bidders.

### Functional Capabilities
- Reject a bid that does not move by at least the bid-change price in the right direction
- Reject a bid for the wrong item or lot, a closed auction, or an ineligible bidder
- Leave the current bid unchanged on rejection
- Show or hide reserve, last accepted bid, and bidder list according to the auction flags
- Mask other bidders’ identities when the bidder list is not displayed

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Bid attempt
- Stored bid-change price
- Direction
- Display flags
- Reserve amount
- Current bid
- Server time
- Eligibility

### Outputs
- Accepted bid or a rejection reason
- The visibility set for the floor

### Business Rules
- Forward: the bid must be at least the current accepted bid plus the bid-change price. The first accepted bid has no previous bid; it must still be a positive amount. It is not compared with the reserve.
- Reverse: the bid must be at most the current accepted bid minus the bid-change price, and still greater than zero. The first accepted bid is any positive amount. It is not compared with the reserve.
- Reserve is shown only when display reserve price is yes. It never auto-rejects.
- Last accepted bid is shown only when that flag is yes.
- Bidder list and identities are shown to bidders only when display bidder list is yes. Otherwise identity is masked.
- A bid after the effective end, including after force close or cutoff, is rejected.

### Validations
- All of the rules above are validations of the attempt.
- Missing configuration (no bid-change price) cannot occur on a published auction because submit of the draft required it. If it is missing, the bid is rejected and the auction is flagged to staff rather than accepted.

### Calculations
Forward minimum = current accepted bid + bid-change price, after the first bid. Reverse maximum = current accepted bid − bid-change price, after the first bid, and the result must stay above zero.

### Workflow
Immediate accept or reject. No queue.

### Search Requirements
None beyond the bidder’s own attempts.

### Documents
None.

### Reports
None.

### Notifications
None per bid.

### Security
Rejection reasons go to the submitting bidder and to the authority monitor, not to other bidders. Masking is applied on every read of the floor, not only on the first paint.

### Integrations
None.

### Dependencies
F04-001 display flags, F04-002 bid-change and reserve, F10-001 submission, F11 closure state.

### Assumptions
- The first bid is not tested against the reserve and is not tested against a previous bid, because there is no previous bid. The source does not state a starting price other than the optional reserve display.
- Display bidder list = no means identity is masked, which is the source rule that bidders are not exposed to other bidders’ identities where masking applies.

### Risks
Bidders who cannot see the last bid must still bid in the right direction by the change price. The rejection reason has to tell them the minimum or maximum they may submit, without revealing a hidden last bid if that flag is no. When the last bid is hidden, the reason states that the bid did not meet the change rule and does not quote the hidden figure.

### Non Functional Requirements
Visibility flags are read from the published auction on every response so a stale screen cannot reveal a hidden reserve.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bid rejection message | UI | Simple | 2 |
| Visibility-controlled bid board | UI | Complex | 12 |
| Validate live bid | API | Very High | 16 |
| Apply bid display masks | API | Complex | 8 |
| Bid rule snapshot | DB | Easy | 2 |
| Live bid validation tests | Testing | Very High | 12 |
| Live bid validation notes | Documentation | Complex | 4 |

**Feature total: 56 hours**
