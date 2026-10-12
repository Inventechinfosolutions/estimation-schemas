# F12-002 — Successful Bidder Finalisation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-002 |
| **Feature Name** | Successful Bidder Finalisation |
| **Module** | 12 — Results, Finalisation and Approval |

### Description
The finalisation authority reviews the ranking for each item or lot, sees who is H1 or L1, and selects the successful bidder. When more than one bidder shares the top rank, the authority must choose one of them and record remarks. The selection is then submitted for approval. The system does not pick the winner by itself.

### Business Objective
A named person selects the successful bidder, including when the top rank is tied, and that choice is submitted rather than treated as already awarded.

### Actors
Maker: Finalisation Authority. Decider: Reviewing / Approving Authority in F12-003.

### User Journey
1. Who creates: the Finalisation Authority creates the selection.
2. How they create: open the closed auction’s results → for each item or lot, review the ladder → if the top rank is unique, confirm that bidder → if the top rank is tied, choose one of the tied bidders → enter remarks → save the selection.
3. How they edit: they can change the selection and remarks until they submit, and again if approval is sent back. After approval they cannot change it here.
4. How they send for approval: Submit finalisation sends the selections to the reviewing authority.
5. How the approver sees pending items: the inbox is F12-003, not this screen. The maker sees the status Submitted.
6. How the approver decides: not on this feature.
7. How the maker sees history: the authority sees the selection, the remarks, and whether it is draft, submitted, or returned.
8. How the auditor sees history: the reviewing authority sees the same pack. Bidders are not told the selection until award and notification in Module 13.

### Functional Capabilities
- Show the ranking and highlight the top rank
- Confirm a unique H1 or L1
- Force an explicit choice when the top rank is tied
- Record remarks
- Submit the finalisation for approval
- Cover every item or every lot before submit

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Ranking
- Selected bidder per item or lot
- Remarks

### Outputs
- A finalisation submission waiting for approval

### Business Rules
- The selected bidder must be one of the bidders on that item or lot ladder. For a tie, they must be one of the tied top bidders.
- A tie cannot be submitted without an explicit selection and remarks.
- A unique top bidder still requires remarks so the file is complete.
- Submit is refused while any item or lot has no selection.
- Submit does not award and does not generate a Letter of Intent.

### Validations
- Auction is closed and ranked.
- Selection is on the ladder.
- Tie rule above.
- User holds Finalisation Authority for the department.

### Calculations
None. The ranking is read from F12-001. This feature does not re-sort in order to hide a tie.

### Workflow
Ranked → selection saved → submitted for approval. Return from F12-003 reopens the selection.

### Search Requirements
Closed auctions in the department awaiting finalisation, by notice number and title.

### Documents
None added. The authority may read the auction pack.

### Reports
None.

### Notifications
Submit notifies the reviewing authority through Module 14.

### Security
Department finalisation role. Bidders have no access.

### Integrations
None.

### Dependencies
F12-001. Module 14. F12-003 is the next decision.

### Assumptions
- Each item or lot has its own successful bidder. The source allows item-wise and lot-wise results, so finalisation follows that grain rather than forcing one winner for a multi-item auction.
- Remarks are required on every selection, including an untied H1 or L1, so the approver always has a note.

### Risks
Selecting outside the tied set would invent a winner the ranking does not support. The validation forbids it.

### Non Functional Requirements
Submit stores the full set of selections or stores none of the submit. A partial submit is not left behind.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Finalisation workspace | UI | Complex | 12 |
| Tie and successful bidder selection | UI | Complex | 12 |
| Finalisation remarks form | UI | Medium | 6 |
| Select successful bidder | API | Complex | 8 |
| Submit finalisation | API | Medium | 6 |
| Finalisation selection records | DB | Medium | 4 |
| Bidder finalisation tests | Testing | Complex | 8 |
| Bidder finalisation notes | Documentation | Medium | 3 |

**Feature total: 59 hours**
