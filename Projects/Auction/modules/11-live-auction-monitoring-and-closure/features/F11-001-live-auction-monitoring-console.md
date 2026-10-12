# F11-001 — Live Auction Monitoring Console

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F11-001 |
| **Feature Name** | Live Auction Monitoring Console |
| **Module** | 11 — Live Auction Monitoring and Closure |

### Description
The auctioning authority watches an open auction: live status, each item or lot, current bidding activity, participant activity, remaining time, extensions, and closure. The remaining time matches the floor. Bidder-facing masking still applies to bidders; the authority’s console shows the identities needed to monitor the auction.

### Business Objective
The authority can see the live auction as it happens, including extensions, without placing bids.

### Actors
Reader: Auctioning Authority of the department. Maker: none on this screen. Bidders create the activity elsewhere. Approver: none.

### User Journey
1. Who creates: the authority does not create the auction here. They open the console.
2. How they create: Live auctions → open an auction that is live → the console shows status, items or lots, activity, participants, remaining time, and extensions.
3. How they edit: they do not edit bids. Force close is F11-002 and is a separate action.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no inbox.
6. How the approver decides: there is no decision.
7. How the maker sees history: the authority sees extension events and the current accepted bid per item or lot on the console.
8. How the auditor sees history: the same console trail is retained for the auction history. Bidders do not open this console.

### Functional Capabilities
- Show live status and remaining time, including after an extension
- Show item or lot status and the current accepted bid
- Show participant activity to the authority, including identity
- Show extension and closure information
- Keep this view off the bidder portal

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- The live auction

### Outputs
- An operational view of the live auction

### Business Rules
- The console is only for the auctioning authority of that department.
- It does not accept a bid.
- Remaining time uses the same effective end as the bidder floor.
- Identity shown here is for the authority. It does not change the masking bidders see.
- A not-yet-live or already completed auction can be opened as a read-only status, but activity is the live view.

### Validations
- The user holds Auctioning Authority for the department.
- The auction exists and is published.

### Calculations
Remaining time is effective end minus server time, the same figure as F10-003.

### Workflow
Observation only. No approval.

### Search Requirements
The authority filters live auctions in their department by title and notice number.

### Documents
None.

### Reports
The console is the operational view. It is not exported as a management report in this feature.

### Notifications
None from watching. Closure notifications belong to closure.

### Security
Bidders receive no route to this console. Department scope applies.

### Integrations
None.

### Dependencies
F10-001, F10-002, F10-003.

### Assumptions
- The authority sees bidder identity even when bidders are masked from each other, because the source gives the authority participant activity and says identity is displayed in accordance with masking rules. Masking governs bidder-to-bidder display. The authority remains able to monitor who is acting.

### Risks
A console that lagged the floor would let the authority act on a stale clock. The remaining time must be the same effective end.

### Non Functional Requirements
The console reflects an accepted bid and an extension without requiring the authority to reload into a contradictory time.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Live monitoring console | UI | Very High | 16 |
| Read live auction monitor | API | Very High | 16 |
| Live activity records | DB | Medium | 4 |
| Live monitoring tests | Testing | Very High | 12 |
| Live monitoring notes | Documentation | Complex | 4 |

**Feature total: 52 hours**
