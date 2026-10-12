# F10-003 — Delta Time Extension and Next-day Cutoff

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-003 |
| **Feature Name** | Delta Time Extension and Next-day Cutoff |
| **Module** | 10 — Live Auction Bidding and Extension |

### Description
When an accepted bid arrives close to the live end, the end moves forward by the auction’s delta, which is 15 or 30 minutes. The new remaining time is shown to bidders on the floor and to the auctioning authority. If that move would pass the next-day continuation cutoff, the end stops at the cutoff instead. A rejected bid does not extend the auction.

### Business Objective
A late accepted bid gets the configured extra time, and the auction cannot be extended without limit into the next day.

### Actors
The eligible bidder triggers the extension by an accepted bid. Bidders and the auctioning authority read the new time. Approver: none.

### User Journey
1. Who creates: nobody types an extension. An accepted qualifying bid creates it.
2. How they create: a bid accepted by F10-002 in the delta window before the current end causes the end to move by 15 or 30 minutes, or to the cutoff if that is sooner.
3. How they edit: staff cannot type a custom extension. Force close is a different feature and ends the auction instead of lengthening it.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no inbox.
6. How the approver decides: there is no decision.
7. How the maker sees history: the bidder sees the updated remaining time and an indication that the end moved.
8. How the auditor sees history: each extension is stored with the bid that caused it, the previous end, and the new end. The auctioning authority sees that on the monitor and on the history.

### Functional Capabilities
- Extend the live end by the configured 15 or 30 minutes when a qualifying bid is accepted near the end
- Refuse to extend on a rejected bid
- Stop the extension at the next-day continuation cutoff
- Show the updated remaining time to bidders and to the authority

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Accepted bid time
- Current live end
- Delta minutes
- Next-day cutoff

### Outputs
- A new effective live end
- An extension event
- Updated remaining time

### Business Rules
- Qualifying means the bid was accepted, not merely submitted.
- Near the end means the accepted bid falls inside the delta window before the current effective end. A bid accepted earlier does not extend.
- Delta is only the value stored on the auction: 15 or 30 minutes.
- If the computed new end is later than the cutoff on the following day, the effective end becomes the cutoff.
- Once the cutoff is reached, further qualifying bids do not extend.
- Extension does not reopen an auction that has been force closed.

### Validations
- Delta is 15 or 30.
- The bid is accepted.
- The auction is still live and not force closed.
- The new end is not after the cutoff.

### Calculations
Candidate end = current effective end + delta. If the bid time is before current end − delta, there is no extension. If candidate end passes the next-day cutoff, effective end = cutoff. Remaining time = effective end − server time.

### Workflow
Accepted bid in the window → end moves → remaining time republished. No approval.

### Search Requirements
Extension events are listed on the auction for staff.

### Documents
None.

### Reports
None.

### Notifications
The remaining time on the floor and the monitor is the notice. A separate email is not sent for every extension, because the source asks to display the updated time, not to email it.

### Security
The new end is the same fact for every participant and for the authority. It is not bidder-specific.

### Integrations
None.

### Dependencies
F04-005 delta and cutoff. F10-002 accepted bid. F11 must observe the same effective end.

### Assumptions
- The trigger window equals the delta itself: a bid accepted within the last 15 minutes of a 15-minute delta auction, or within the last 30 minutes of a 30-minute delta auction, qualifies. The source says a qualifying bid received near auction closing and names the delta as the extension length. Using that same length as the near-closing window is the rule in this baseline.
- The cutoff is the clock time on the calendar day after the original live-auction date, compared with the candidate end.

### Risks
A different reading of near closing would change how often auctions extend. The rule above is explicit so estimation and build share one meaning.

### Non Functional Requirements
All participants and the monitor read one effective end after an extension. A bidder is not left on the old clock.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Remaining time and extension banner | UI | Medium | 6 |
| Apply delta extension | API | Complex | 8 |
| Enforce next-day cutoff | API | Complex | 8 |
| Auction extension event records | DB | Easy | 2 |
| Delta extension tests | Testing | Complex | 8 |
| Delta extension notes | Documentation | Medium | 3 |

**Feature total: 35 hours**
