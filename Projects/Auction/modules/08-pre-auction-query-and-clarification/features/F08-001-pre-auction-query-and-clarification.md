# F08-001 — Pre-auction Query and Clarification

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | Pre-auction Query and Clarification |
| **Module** | 08 — Pre-Auction Query and Clarification |

### Description
While the participation and query period is open, a bidder who can see the auction submits a question. An authorised department user reads it and records a clarification. The question and the answer stay on the auction. The bidder reads the answer. After the deadline, new questions are refused. A clarification does not change auction terms; a change of terms is a corrigendum.

### Business Objective
Bidders can ask, and the department can answer on the record, before the query deadline, without an off-system mail thread.

### Actors
Maker: eligible bidder, for the question. Responder: Auction Creator or Reviewing / Approving Authority of the department. Approver: none beyond the responder posting the clarification. There is no second committee.

### User Journey
1. Who creates: the bidder creates the query. The department user creates the clarification.
2. How they create: the bidder opens the auction → Ask a question → enters the question → Submit. The department user opens Queries → reads the question → writes the clarification → Post.
3. How they edit: the bidder may edit the question only until the department has posted a clarification and only before the deadline. The department may correct a clarification before the deadline; the previous text stays in the thread.
4. How they send for approval: the bidder’s submit is the send. It does not go to a separate approver. The department posts the answer directly.
5. How the approver sees pending items: there is no separate approver. The department user sees an inbox of unanswered queries for their auctions.
6. How the approver decides: posting the clarification is the response. They do not accept or reject the bidder for asking.
7. How the maker sees history: the bidder sees their question, the time, and the clarification when it exists.
8. How the auditor sees history: department users see every query on the auction, who asked, and the answers. Other bidders see published clarifications on the auction so that all eligible bidders receive the same answer. They do not see the asking bidder’s identity if the auction masks bidder identity; the question text is visible, the asker’s name is not, when masking applies. Before live bidding, masking is applied to the asker’s identity on the shared view in the same way, so one bidder does not learn who else is interested.

### Functional Capabilities
- Bidder submits a query before the deadline
- Department inbox of unanswered queries
- Department posts a clarification on the auction
- Eligible bidders read clarifications
- Refuse queries after the deadline

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Auction
- Question text
- Clarification text

### Outputs
- A query thread stored on the auction

### Business Rules
- The deadline is the participation end, unless the auction has recorded an earlier query deadline inside that window. The default is the participation end.
- Only an eligible bidder who can see the auction may ask.
- The answer does not alter title, prices, schedule, or items. Staff who need to change terms publish a corrigendum.
- Unanswered queries remain visible to the department after the deadline so they can be answered only if still before the deadline. After the deadline, posting is also closed.
- Queries are not accepted on drafts or on completed auctions.

### Validations
- Question text is mandatory.
- The bidder is eligible.
- The current time is before the deadline.
- Clarification text is mandatory when posting.

### Calculations
None.

### Workflow
Question submitted → department inbox → clarification posted → visible to eligible bidders. No further approval.

### Search Requirements
Bidder sees queries on the auction they opened. Department filters by auction and by unanswered.

### Documents
None required. A query is text. If the department needs to issue a paper, they use a corrigendum.

### Reports
None.

### Notifications
A new query notifies department users. A clarification notifies the asking bidder and is visible to other eligible bidders on the auction. Module 14 carries the alerts.

### Security
Internal drafts of an answer are not shown. Asker identity is hidden from other bidders. Staff see the identity so they can respond.

### Integrations
None.

### Dependencies
F07-001 eligibility. F04-005 window. Module 14.

### Assumptions
- The shared reading of clarifications follows the usual procurement practice that every eligible bidder sees the answer. The source says the bidder views the response and that the query stays on the auction. It does not say answers are private. Identity masking still applies.
- An earlier query deadline than participation end can be stored on the auction schedule as an optional field. If blank, participation end is the deadline.

### Risks
A clarification that actually changes terms, without a corrigendum, will mislead bidders. The screen tells the department user that term changes belong in a corrigendum. It cannot judge the prose.

### Non Functional Requirements
A query saved after the deadline is not stored.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder query form | UI | Medium | 6 |
| Bidder query thread | UI | Medium | 6 |
| Department query inbox | UI | Medium | 6 |
| Clarification response form | UI | Medium | 6 |
| Submit auction query | API | Medium | 6 |
| List auction queries | API | Medium | 6 |
| Post auction clarification | API | Complex | 8 |
| Auction query records | DB | Medium | 4 |
| Pre-auction query tests | Testing | Complex | 8 |
| Pre-auction query notes | Documentation | Medium | 3 |

**Feature total: 59 hours**
