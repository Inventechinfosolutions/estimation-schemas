# F10-001 — Live Bid Submission

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F10-001 |
| **Feature Name** | Live Bid Submission |
| **Module** | 10 — Live Auction Bidding and Extension |

### Description
During the live window, a bidder who is allowed in opens the auction floor, sees the items or lots they may bid on, and submits a bid. Forward and reverse auctions both use this floor. An accepted bid becomes the current bid for that item or lot. Bidders who failed evaluation, who never confirmed participation, or who are outside a closed list cannot open the floor.

### Business Objective
Only eligible bidders can place a live bid, and the auction shows one current bid per item or lot after a bid is accepted.

### Actors
Maker: eligible bidder. Approver: none. The auctioning authority watches in Module 11 and does not place the bid.

### User Journey
1. Who creates: the eligible bidder creates the bid.
2. How they create: at or after live start, and before the effective end → Enter live auction → choose an item or a lot → enter the bid → Submit.
3. How they edit: a submitted bid is not edited. A later bid is a new submission. There is no draft bid.
4. How they send for approval: they do not. Validation in F10-002 accepts or rejects the bid immediately.
5. How the approver sees pending items: there is no approver inbox for bids.
6. How the approver decides: there is no human decision on an individual bid.
7. How the maker sees history: the bidder sees their own submitted bids, which were accepted, and which were rejected, with the reason.
8. How the auditor sees history: the auctioning authority sees bidding activity on the monitor. They see bidder identity according to the operational monitor. Other bidders do not see identity when masking is on, and they see the last accepted bid only when that display flag is yes.

### Functional Capabilities
- Admit only eligible bidders onto the floor
- Show items for an item-wise auction and lots for a lot-wise auction
- Accept a forward or a reverse bid submission
- Update the current bid only after validation accepts it
- Show the bidder their own bid history

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Auction
- Item or lot
- Bid amount

### Outputs
- An accepted current bid, or a rejected attempt stored on the bidder’s own history

### Business Rules
- When evaluation is yes, the bidder must be on the approved accepted list.
- When evaluation is no, the bidder must have a confirmed participation and must still be eligible under the direct, prequalified, or restricted rule.
- The live auction must be open. Scheduled end, cutoff, and force close all close it.
- Item-wise bids name an item. Lot-wise bids name a lot. A bid cannot name the other.
- The bidder cannot withdraw an accepted bid.

### Validations
- Eligibility, window, and item or lot are checked with F10-002 before the current bid changes.
- The amount is a number greater than zero.

### Calculations
None in this feature beyond storing the amount. Ranking is Module 12. Bid-change comparison is F10-002.

### Workflow
Enter floor → submit → accepted or rejected. No staff approval of a bid.

### Search Requirements
The bidder filters their own bids by item or lot.

### Documents
None.

### Reports
None. The monitor is Module 11.

### Notifications
Live commencement is a Module 14 event at live start. An individual bid does not email every participant.

### Security
A bidder cannot submit as another bidder. Masking is applied by F10-002 on what this floor displays.

### Integrations
None.

### Dependencies
F07-002, F09-002 when evaluation is yes, F04-001 direction and structure, F04-005 window, F10-002 validation.

### Assumptions
- One current bid is the latest accepted bid for that item or lot. The source says the current bid is updated when a bid is accepted.
- Rejected attempts remain visible to the bidder who made them so they can correct the next submission. They are not shown to other bidders.

### Risks
Clock skew between bidders can make a near-end bid feel late. The server time is the time that counts, and the floor shows that remaining time.

### Non Functional Requirements
Two bids arriving together produce one accepted current bid according to validation, not two current bids.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Live auction floor | UI | Very High | 16 |
| Item or lot bid panel | UI | Complex | 12 |
| My live bids | UI | Easy | 4 |
| Enter live auction | API | Complex | 8 |
| Submit live bid | API | Very High | 16 |
| Read own live bids | API | Medium | 6 |
| Live bid records | DB | Complex | 6 |
| Live bid submission tests | Testing | Very High | 12 |
| Live bid submission notes | Documentation | Complex | 4 |

**Feature total: 84 hours**
