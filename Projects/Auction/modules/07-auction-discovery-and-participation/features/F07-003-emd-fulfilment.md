# F07-003 — EMD Fulfilment

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-003 |
| **Feature Name** | EMD Fulfilment |
| **Module** | 07 — Auction Discovery and Participation |

### Description
The bidder completes the earnest money requirement configured on the auction. That may be one common amount, an amount per item, or an amount per lot. The bidder records the amount, the instrument or reference, and uploads proof. This is not a payment-gateway collection, and it does not refund or forfeit money.

### Business Objective
The next stage can see that the bidder has met the EMD rule the auction was published with, with evidence attached.

### Actors
Maker: the participating bidder. Reader: Evaluation Authority and other authorised department users. Approver: none. Acceptance of the proof, when Evaluation is yes, is part of Module 09 rather than an automatic payment success.

### User Journey
1. Who creates: the bidder creates the fulfilment against their participation.
2. How they create: Participation → EMD → the screen shows common, item, or lot amounts taken from the auction → the bidder enters the instrument or reference and uploads proof for each required line → Save.
3. How they edit: before participation end and before confirmation, they may replace the reference or the proof. After confirmation, changes are closed so evaluation does not chase a moving document. A department user does not edit the bidder’s reference.
4. How they send for approval: they do not. Completeness unblocks confirmation. When Evaluation is yes, the evaluator later accepts or rejects the bidder, which includes this proof.
5. How the approver sees pending items: there is no EMD approval inbox. The evaluation dossier shows EMD status.
6. How the approver decides: there is no separate EMD decision.
7. How the maker sees history: the bidder sees what they filed and whether each line is complete.
8. How the auditor sees history: the evaluator sees the reference, the proof, and replacements that happened before confirmation.

### Functional Capabilities
- Show the EMD structure and amounts from the auction
- Capture instrument or reference and proof per common, item, or lot line
- Mark the participation’s EMD complete only when every required line has proof
- Block confirmation while EMD is incomplete

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Participation
- Reference
- Proof file
- The configured amounts

### Outputs
- EMD fulfilment lines on the participation

### Business Rules
- The bidder cannot change the amount the auction demands. They can only fulfil it.
- Common EMD is one line. Item-wise EMD is one line per item. Lot-wise EMD is one line per lot.
- Proof is required on every line. A reference without a file is incomplete.
- No money is captured by a payment service.
- Refund and forfeiture are out of scope and have no actions here.

### Validations
- The participation belongs to the signed-in bidder.
- The window for edits is the participation window, and only before confirmation.
- File type follows the auction document types. Size follows the 70 MB cap.
- Amount fields from the auction are read-only.

### Calculations
Completeness is the count of required lines that have both a reference and a proof. There is no interest or tax calculation.

### Workflow
Lines saved → EMD complete flag on the participation → confirmation allowed in F07-002. No payment status such as authorised or settled.

### Search Requirements
The bidder sees EMD on their participation. Staff see EMD status on the participant list.

### Documents
EMD proof files on the fulfilment lines.

### Reports
None.

### Notifications
None beyond the participation confirmation notification, which waits until EMD is included in a confirmed participation.

### Security
A bidder cannot read another bidder’s proof. Evaluation staff of the auction can.

### Integrations
None. Payment gateway is out of scope.

### Dependencies
F04-002 EMD configuration. F07-002 participation. F04-003 items or lots.

### Assumptions
- Instrument or reference is free text plus a proof file, because the source says the bidder completes the EMD requirement and does not name a bank integration.
- Staff do not mark EMD paid. Completeness is file-and-reference completeness. Eligibility judgement sits in Module 09 when evaluation is on.

### Risks
A forged proof can be uploaded. The control is evaluation when the flag is yes, and the authority’s later award process. There is no bank confirmation in this scope.

### Non Functional Requirements
EMD amounts displayed to the bidder match the published auction, including after a corrigendum that changed them, once that corrigendum is published.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| EMD requirement summary | UI | Medium | 6 |
| EMD fulfilment form | UI | Complex | 12 |
| Read EMD requirement | API | Medium | 6 |
| Record EMD fulfilment | API | Complex | 8 |
| EMD fulfilment records | DB | Medium | 4 |
| EMD fulfilment tests | Testing | Complex | 8 |
| EMD fulfilment notes | Documentation | Medium | 3 |

**Feature total: 47 hours**
