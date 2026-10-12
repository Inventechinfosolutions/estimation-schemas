# F12-001 — Item and Lot Bid Ranking

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-001 |
| **Feature Name** | Item and Lot Bid Ranking |
| **Module** | 12 — Results, Finalisation and Approval |

### Description
After closure, authorised staff see the result of each item or each lot. A forward auction ranks the highest accepted bid as H1, then H2, then H3. A reverse auction ranks the lowest accepted bid as L1, then L2, then L3. Only final accepted bids are ranked. Rejected attempts are ignored. Ties at the top are shown as a tie; they are not broken here.

### Business Objective
Finalisation starts from a ranking that follows the auction direction and the frozen bid book.

### Actors
Reader: Finalisation Authority and Reviewing / Approving Authority. The ranking is produced from the closed bids. Approver: none on the ranking itself.

### User Journey
1. Who creates: the closure creates the occasion. Staff do not type ranks.
2. How they create: open a closed auction → Results. Ranks are shown per item or per lot.
3. How they edit: ranks are not hand-edited. A correction of a bid is not available after closure.
4. How they send for approval: they do not. Selecting the winner is F12-002.
5. How the approver sees pending items: there is no ranking inbox.
6. How the approver decides: there is no decision.
7. How the maker sees history: the finalisation authority sees the ranked bids, amounts, and bidder identities.
8. How the auditor sees history: the reviewing authority sees the same ranking when the finalisation is submitted. Bidders do not see the full ladder unless the organisation later publishes it. This feature is a staff result. Each bidder can see their own accepted bids from F10-001, not everyone else’s rank.

### Functional Capabilities
- Rank accepted bids highest-first for a forward auction
- Rank accepted bids lowest-first for a reverse auction
- Rank at item level or lot level to match the structure
- Ignore rejected attempts
- Show a tie at the top without auto-selecting a winner

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Closed auction
- Accepted bids
- Direction
- Structure

### Outputs
- H1, H2, H3 or L1, L2, L3 per item or lot
- A tie marker when the top amounts are equal

### Business Rules
- Ranking waits until the auction is closed.
- Forward uses highest valid bid first. Reverse uses lowest valid bid first.
- Valid means accepted during the live auction. Rejected submissions are excluded.
- Equal top amounts are a tie. The rank label is shared and F12-002 must choose.
- Item-wise auctions do not produce a single auction-wide winner. Each item has its own ladder. Lot-wise auctions rank each lot.

### Validations
- Auction is closed.
- The reader holds finalisation or reviewing authority for the department.

### Calculations
Forward: sort accepted amounts descending. Reverse: sort accepted amounts ascending. Ties are equal amounts at the top position. Subsequent positions follow the sort. No average and no preference for an earlier timestamp is used to break a tie, because the source asks finalisation to handle multiple L1 situations rather than a silent time rule. The same applies to a tied H1.

### Workflow
Closed → ranked. No approval of the arithmetic.

### Search Requirements
Results by item or lot and by rank label.

### Documents
None.

### Reports
The ranking view is the result staff use. It is not a separate export product.

### Notifications
Closure has already been notified. Ranking does not send a second mail by itself.

### Security
Staff of the department only. Bidders do not receive the full ranking in this feature.

### Integrations
None.

### Dependencies
F11 closure and the accepted bids from F10.

### Assumptions
- Multiple items mean multiple ladders. The source says ranking is at item or lot level.
- Timestamp is not a tie-break. Finalisation handles the tie explicitly.

### Risks
If two bids of the same amount both show as H1, users may think the system failed. The screen has to say the top rank is tied and must be resolved in finalisation.

### Non Functional Requirements
Reopening the ranking view does not reshuffle a tie into a single winner.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Result ranking register | UI | Complex | 12 |
| Item or lot rank detail | UI | Medium | 6 |
| Calculate bid ranking | API | Very High | 16 |
| Read bid ranking | API | Medium | 6 |
| Bid rank snapshot | DB | Medium | 4 |
| Bid ranking tests | Testing | Very High | 12 |
| Bid ranking notes | Documentation | Complex | 4 |

**Feature total: 60 hours**
