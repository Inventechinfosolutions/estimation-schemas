# F15-002 — Auction History for Authorised Users

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F15-002 |
| **Feature Name** | Auction History for Authorised Users |
| **Module** | 15 — Auction Status and History |

### Description
Authorised staff open one auction and read the trace of what happened: creation, draft saves, submission, review, approval or return, publication, corrigenda, participation, evaluation where it applied, live bidding and extensions, closure and the force-close reason when that was the closure, ranking, finalisation, award, letter, and completion. The bidder sees only the history they are allowed: published events, their own participation, their own evaluation outcome, their own bids, and their own letter.

### Business Objective
A later reader can reconstruct the auction from the record, including who force-closed it and who approved the winner.

### Actors
Reader: department staff with a role on the auction, and the System / Catalogue Administrator. The bidder reads a reduced history. Approver: none.

### User Journey
1. Who creates: the business actions create the history rows. The reader does not.
2. How they create: each of the actions listed in the description appends a row with who, when, and what.
3. How they edit: history rows are not edited or deleted from this screen.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no inbox. The history is a record of decisions already taken.
6. How the approver decides: not here.
7. How the maker sees history: the creator sees the full staff history of auctions they may open, including return remarks.
8. How the auditor sees history: the reviewing authority and the catalogue administrator see that same staff history. The bidder’s view omits internal remarks, other bidders’ documents, other bidders’ outcomes, and the force-close reason text. The bidder does see that the auction was closed, their own outcome, and their own letter if they received one.

### Functional Capabilities
- Append a history row for each lifecycle action
- Show staff the full sequence for one auction
- Show the force-close reason to staff
- Show the bidder a reduced history
- Filter the staff history by stage

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Auction
- Optional stage filter

### Outputs
- Ordered history of the auction

### Business Rules
- Rows are added by the business action that happened. Users do not add free-text history.
- Return remarks, evaluation remarks, finalisation remarks, and the force-close reason are on the staff history.
- The bidder does not see other bidders’ rows.
- History is not deleted when the auction is completed.
- Catalogue item edits remain on the item, not copied into every auction that once selected the item.

### Validations
- The reader may open the auction.
- A bidder filter is applied before the response is built, not only hidden on screen.

### Calculations
None.

### Workflow
Read-only trace. No approval.

### Search Requirements
Filter staff history by stage: creation, approval, publication, corrigendum, participation, evaluation, live, closure, finalisation, award.

### Documents
History entries link to the document, corrigendum, or letter where the action had one. They do not store a second copy as the master.

### Reports
None. The history is the record.

### Notifications
None.

### Security
Department staff and the catalogue administrator for the full trace. Bidder reduction is mandatory. Another department’s staff do not open the history.

### Integrations
None.

### Dependencies
History rows written as part of Modules 04 through 13. This feature presents them.

### Assumptions
- Participation history on the staff view shows that a bidder confirmed, not the contents of their documents. The documents open from the evaluation dossier, which remains access-controlled.
- Live bidding history on the staff view lists accepted bids. Rejected attempts stay on the bidder’s own bid list and are not copied into the shared staff timeline except as a count if needed for support. The timeline itself records accepted bids, extensions, and closure.

### Risks
A history view that loads every rejected keystroke will be unreadable. Rejected bids stay on the bidder’s own list, as stated above.

### Non Functional Requirements
The staff sequence is in the order the actions were recorded. Completion does not drop earlier rows.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction history timeline | UI | Complex | 12 |
| History event detail | UI | Easy | 4 |
| Read auction history | API | Complex | 8 |
| Filter auction history | API | Medium | 6 |
| Auction history event records | DB | Medium | 4 |
| Auction history tests | Testing | Complex | 8 |
| Auction history notes | Documentation | Medium | 3 |

**Feature total: 45 hours**
