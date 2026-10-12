# F13-003 — Auction Completion and Successful-bidder Advice

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-003 |
| **Feature Name** | Auction Completion and Successful-bidder Advice |
| **Module** | 13 — Award and Letter of Intent |

### Description
After the letters have been issued, the awarding authority advises the successful bidder and marks the auction complete. The advice points to the letter. Completion is refused while any approved selection lacks an issued letter. Other bidders are not told that they won.

### Business Objective
The auction reaches a completed state only when the successful bidder has been advised and the letter exists.

### Actors
Maker: Awarding Authority. Recipient: the successful bidder. Approver: none beyond the award already given.

### User Journey
1. Who creates: the Awarding Authority creates the completion.
2. How they create: on the awarded auction, after letters are issued → Advise successful bidder and complete → confirm.
3. How they edit: completion is not reversed here.
4. How they send for approval: they do not.
5. How the approver sees pending items: the authority’s list shows awarded auctions whose letters are issued and which are not yet complete.
6. How the approver decides: confirm is the decision. There is no second approver.
7. How the maker sees history: the authority sees the completion time.
8. How the auditor sees history: the history shows advice and completion. The successful bidder sees the advice in their notifications and the letter. Unsuccessful bidders are not sent a winning advice.

### Functional Capabilities
- Advise each successful bidder that the letter is available
- Complete the auction only when every selection has an issued letter
- Record completion on the auction
- Leave unsuccessful bidders without a winning advice

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Awarded auction with issued letters
- Complete action

### Outputs
- Completed auction
- Advice to each successful bidder

### Business Rules
- Completion checks that every approved selection has an issued letter.
- Advice goes only to the successful bidder for that selection.
- Completion does not create a contract or a payment.
- A completed auction does not accept a new corrigendum.

### Validations
- Letters issued for every selection.
- User holds Awarding Authority.
- Auction is awarded and not already complete.

### Calculations
None.

### Workflow
Letters issued → advice sent → completed.

### Search Requirements
Awarded-not-complete list for the authority.

### Documents
The advice refers to the letter. It does not create a second document type.

### Reports
None.

### Notifications
Successful-bidder advice and auction-completion events go through Module 14. The advice is bidder-specific.

### Security
The advice payload does not include other bidders’ results.

### Integrations
Email delivery of the advice is F14-002. This feature records the business completion and raises the event.

### Dependencies
F13-002. Module 14. Module 15 shows the completed stage.

### Assumptions
- One completion covers the auction after all of its letters are issued.
- Unsuccessful bidders are not given a separate regret letter, because the source names successful-bidder notification and does not name a regret letter.

### Risks
Completing before the bidder has actually opened the letter is still valid. The obligation is to advise, not to collect an acknowledgement. The source does not require the bidder to accept the letter inside the system.

### Non Functional Requirements
Completion is a single event. Repeating the action does not send a second advice storm beyond the original notification.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Complete auction confirmation | UI | Easy | 4 |
| Mark auction complete | API | Complex | 8 |
| Raise successful-bidder advice | API | Medium | 6 |
| Auction completion records | DB | Easy | 2 |
| Auction completion tests | Testing | Medium | 6 |
| Auction completion notes | Documentation | Easy | 2 |

**Feature total: 28 hours**
