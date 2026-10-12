# F09-001 — Participation Evaluation and Eligibility Decision

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-001 |
| **Feature Name** | Participation Evaluation and Eligibility Decision |
| **Module** | 09 — Pre-Live Participation Evaluation |

### Description
When the auction’s evaluation flag is yes, the evaluation authority reviews each confirmed participant after the participation window: bidder details, participation documents, EMD status, eligibility, prequalification, and restricted-list conditions. The authority marks the bidder accepted or rejected and records remarks. When the flag is no, this screen is not used and no eligibility decision is required before live bidding.

### Business Objective
Live bidding opens only to bidders the authority has accepted, and only on auctions that asked for this pre-live evaluation.

### Actors
Maker: Evaluation Authority of the department. Subject: the confirmed bidder. Approver of the list as a whole: F09-002. This feature records the line-level decision.

### User Journey
1. Who creates: the Evaluation Authority creates the decision on each confirmed participant. The bidder does not.
2. How they create: after participation end, open the auction → participants → open a bidder’s dossier (profile, documents, EMD proof) → Accepted or Rejected, with remarks → Save.
3. How they edit: they can change a line decision until the list is submitted for approval in F09-002. After the list is approved, a line is not quietly flipped.
4. How they send for approval: when every confirmed participant has a decision, they submit the list in F09-002. This feature does not approve the list.
5. How the approver sees pending items: the line decisions are visible to the reviewing authority once the list is submitted. The inbox itself is F09-002.
6. How the approver decides: not on this feature.
7. How the maker sees history: the bidder sees their own outcome only after the list is approved, not while the evaluator is still drafting.
8. How the auditor sees history: the evaluation authority and the reviewing authority see each decision, remark, user, and time. Other bidders never see someone else’s outcome.

### Functional Capabilities
- List confirmed participants when evaluation is yes
- Open bidder details, documents, and EMD proof
- Check prequalified and restricted conditions
- Record accepted or rejected with remarks
- Skip the entire stage when evaluation is no

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Auction with evaluation yes
- Participant
- Decision
- Remarks

### Outputs
- Line-level eligibility decisions awaiting list approval

### Business Rules
- The stage does not appear for evaluation = no.
- Only confirmed participations are evaluated. In-progress participations are out of the list.
- A bidder not on a prequalified or restricted list is not on the participant list in the first place.
- Remarks are mandatory for a rejection and required for an acceptance as well, so the file shows why.
- Draft decisions are invisible to the bidder.
- Saving a decision does not admit the bidder to the live auction. Admission waits for F09-002.

### Validations
- Evaluation flag is yes.
- Participation is confirmed.
- Decision and remarks are present.
- The user holds Evaluation Authority for the department.
- The participation window has ended so the pack is frozen.

### Calculations
None. There is no numeric score. The source asks for a decision, not a mark sheet.

### Workflow
Frozen participation pack → line decision → ready for list submission. Bidders are not told the draft result.

### Search Requirements
Participant list by organisation and by decision status: pending, accepted, rejected.

### Documents
Read-only participation documents and EMD proofs.

### Reports
None. The accepted list in F09-002 is the output.

### Notifications
No bidder notification on a draft line decision. Notification happens when the list is approved.

### Security
Department evaluation role only. One bidder’s dossier is not shown to another bidder.

### Integrations
None.

### Dependencies
F07-002 confirmed participation, F07-003, F07-004, F04-001 evaluation flag.

### Assumptions
- Evaluation starts after participation end so documents are frozen, which matches the source order: participation, EMD and documents, then evaluation, then live auction.
- Acceptance remarks are required so a later audit can read the file. The source says remarks are entered where applicable; requiring them on every line is the operational rule in this baseline.

### Risks
Starting evaluation before participation end would race document replacements. The screen stays closed until the window ends.

### Non Functional Requirements
An auction with evaluation = no does not block live bidding on this feature’s account.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Evaluation participant register | UI | Complex | 12 |
| Bidder evaluation dossier | UI | Very High | 16 |
| Eligibility decision form | UI | Medium | 6 |
| List participants for evaluation | API | Medium | 6 |
| Read participation evaluation pack | API | Medium | 6 |
| Record eligibility decision | API | Complex | 8 |
| Eligibility decision records | DB | Medium | 4 |
| Participation evaluation tests | Testing | Very High | 12 |
| Participation evaluation notes | Documentation | Complex | 4 |

**Feature total: 74 hours**
