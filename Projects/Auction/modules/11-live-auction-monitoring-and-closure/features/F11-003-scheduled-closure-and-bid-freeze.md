# F11-003 — Scheduled Closure and Bid Freeze

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-003 |
| **Feature Name** | Scheduled Closure and Bid Freeze |
| **Module** | 11 — Live Auction Monitoring and Closure |

### Description
When the effective live end is reached, the auction closes without a person pressing a button. The effective end is the scheduled end plus any delta extensions that stayed inside the next-day cutoff. Further bids are refused. Final accepted bids remain for ranking, and the auction moves to result processing.

### Business Objective
The auction ends at the time the rules produced, and the bid book used for ranking is frozen.

### Actors
No human maker. The schedule and the extension rules create the closure. The auctioning authority and bidders see the result. Approver: none.

### User Journey
1. Who creates: the system creates the closure when server time reaches the effective end. A person does not.
2. How they create: there is no form. Bidders see the floor change to closed. The authority sees the console change to closed.
3. How they edit: the closure time is not edited. A force close before this point is a different closure and this feature does not also fire.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no inbox.
6. How the approver decides: there is no decision.
7. How the maker sees history: bidders see the closed status and that no further bids are accepted.
8. How the auditor sees history: staff see the effective end, whether extensions applied, and that closure was scheduled rather than forced.

### Functional Capabilities
- Close the auction at the effective live end
- Refuse bids after that instant
- Retain final accepted bids for ranking
- Record scheduled closure distinctly from force close
- Move the auction to post-auction processing

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Effective live end
- Server time
- Accepted bids

### Outputs
- Closed auction ready for ranking

### Business Rules
- Effective end includes valid extensions and respects the cutoff.
- A force-closed auction is not closed a second time by the schedule.
- Bids submitted after the end are rejected and do not change the current bid.
- Accepted bids up to the end are the population Module 12 ranks.
- Closure notifies participants.

### Validations
- The auction was live.
- Server time is at or past the effective end.
- No force-close record exists.

### Calculations
The end used is the effective end from F10-003, or the original live end if there was no extension.

### Workflow
Live → closed (scheduled) → ready for ranking. No approval.

### Search Requirements
Staff filter by closure type.

### Documents
None.

### Reports
None.

### Notifications
Closure notification through Module 14, same event family as force close, with the closure type identified.

### Security
Bidders cannot postpone the end.

### Integrations
None.

### Dependencies
F04-005, F10-003, F11-002 so the two closure types stay distinct.

### Assumptions
- Closure is detected when the server reaches the effective end. Bidders do not have to refresh for a bid after the end to be rejected; the submit itself is rejected.

### Risks
A delay in applying the end would accept a late bid. The submit path must read the effective end at the moment of the attempt.

### Non Functional Requirements
The bid book used for ranking does not change after closure.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Scheduled closure notice | UI | Simple | 2 |
| Close auction at scheduled end | API | Complex | 8 |
| Freeze further live bids | API | Complex | 8 |
| Scheduled closure records | DB | Easy | 2 |
| Scheduled closure tests | Testing | Complex | 8 |
| Scheduled closure notes | Documentation | Medium | 3 |

**Feature total: 31 hours**
