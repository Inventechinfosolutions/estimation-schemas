# F07-002 — Expression of Interest and Participation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-002 |
| **Feature Name** | Expression of Interest and Participation |
| **Module** | 07 — Auction Discovery and Participation |

### Description
During the participation window, an eligible bidder expresses interest and starts a participation on that auction. The participation has a status that shows whether it has been started, whether EMD and documents are still outstanding, and whether it is confirmed. Confirming participation is refused until the EMD and required documents for that auction are complete. One bidder has one participation per auction.

### Business Objective
The organisation knows which eligible bidders have committed to an auction, and the bidder can see their own status.

### Actors
Maker: eligible active bidder. Approver: none on this feature. Evaluation, when required, is Module 09.

### User Journey
1. Who creates: the bidder creates the participation.
2. How they create: from the auction detail, during the participation window → Participate. The status becomes in progress until EMD and documents are complete, then the bidder confirms.
3. How they edit: before confirmation, they may withdraw the in-progress participation. After confirmation, they cannot silently delete it. A correction of documents before the participation end is done on F07-004 and leaves the participation in place.
4. How they send for approval: confirmation is the bidder’s own submission. It is not an authority approval. When Evaluation is yes, Module 09 is the later decision. When Evaluation is no, confirmation plus completed EMD and documents is what makes them an eligible participant.
5. How the approver sees pending items: there is no approval inbox on this feature. The evaluation inbox exists only when Evaluation is yes, and it is Module 09.
6. How the approver decides: there is no decision here.
7. How the maker sees history: the bidder sees started, EMD outstanding or complete, documents outstanding or complete, confirmed, and the times.
8. How the auditor sees history: the creator and the evaluation authority see the participation status of bidders on that auction. They do not see unrelated auctions’ participations from this screen except through the auction they are allowed to open.

### Functional Capabilities
- Start a participation during the participation window
- Keep one participation per bidder per auction
- Show status for EMD, documents, and confirmation
- Confirm only when EMD and required documents are complete
- Refuse bidders who are outside a closed list or outside the window

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Auction
- Participate action
- Confirm action

### Outputs
- Participation record and status

### Business Rules
- The bidder must be active and eligible for the auction.
- Participate is refused before participation start and after participation end.
- Confirm is refused while EMD fulfilment or a required participation document is missing.
- A confirmed participation is the list Module 09 evaluates when Evaluation is yes, and the list Module 10 admits when Evaluation is no, subject to eligibility.
- Withdrawing before confirmation removes the in-progress participation. Withdrawing after confirmation is not offered.

### Validations
- Window check.
- Eligibility check.
- Duplicate participation is rejected.
- Confirm checks F07-003 and F07-004 completeness.

### Calculations
None.

### Workflow
Started → in progress → confirmed. No staff approval on this feature.

### Search Requirements
The bidder’s own participation list by auction title and status. Staff on the auction see the participant list.

### Documents
None stored here. Documents are F07-004.

### Reports
None.

### Notifications
Confirmation notifies the bidder and the auction’s department users through Module 14.

### Security
A bidder sees only their participation. Staff of the department see participants of their auction. Other bidders’ identities are not shown to a bidder on this screen.

### Integrations
None.

### Dependencies
F07-001, F07-003, F07-004, F04-005 window, F04-001 eligibility.

### Assumptions
- Expression of interest and participation are one act in this system, because the source describes a single path: express interest / participate, then EMD, documents, and confirmation.
- There is no separate shortlisting before this participation.

### Risks
Bidders may confirm late in the window. The end time is enforced. There is no grace period, because the source does not provide one.

### Non Functional Requirements
Two confirms do not create two participations.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Participation action panel | UI | Medium | 6 |
| My participation register | UI | Medium | 6 |
| Participation confirmation | UI | Simple | 2 |
| Submit auction participation | API | Complex | 8 |
| Read participation status | API | Medium | 6 |
| Participation records | DB | Medium | 4 |
| Participation tests | Testing | Complex | 8 |
| Participation notes | Documentation | Medium | 3 |

**Feature total: 43 hours**
