# F09-002 — Accepted Bidder List Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-002 |
| **Feature Name** | Accepted Bidder List Approval |
| **Module** | 09 — Pre-Live Participation Evaluation |

### Description
The evaluation authority submits the completed eligibility decisions. The reviewing authority approves the accepted list or sends it back. Only after approval may accepted bidders enter the live auction. Rejected bidders stay out. Auctions with evaluation = no never use this list.

### Business Objective
The set of bidders who may bid live is an approved list, not a draft the evaluator can still change.

### Actors
Maker: Evaluation Authority. Decider: Reviewing / Approving Authority.

### User Journey
1. Who creates: the evaluation authority creates the submission of the list. The reviewing authority creates the approval decision.
2. How they create: from the participant register, when every confirmed bidder has a decision → Submit list. The reviewer opens Finalise eligible list → reads accepted and rejected rows → Approve or Send back.
3. How they edit: a send-back reopens line decisions in F09-001. An approval freezes them.
4. How they send for approval: Submit list is that send.
5. How the approver sees pending items: an inbox of evaluation lists submitted for their department, with auction title and counts of accepted and rejected.
6. How the approver decides: Approve, which publishes outcomes to each bidder and opens live entry to accepted bidders, or Send back with remarks to the evaluator.
7. How the maker sees history: the evaluator sees submitted, returned, or approved. Each bidder sees only their own final outcome after approval.
8. How the auditor sees history: both authorities see the submission, the decision, the remarks, and the frozen list.

### Functional Capabilities
- Submit the list only when every confirmed participant has a decision
- Show accepted and rejected counts to the reviewer
- Approve the list and freeze it
- Send the list back for correction
- Notify each bidder of their own outcome after approval

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Completed line decisions
- Approve or send back
- Remarks on send-back

### Outputs
- Approved accepted-bidder list controlling live entry
- Bidder-specific outcome messages

### Business Rules
- Not used when evaluation is no.
- Live bidding for an evaluation = yes auction checks this approved list and ignores draft acceptances.
- A rejected bidder is not on the list and cannot bid.
- Send-back remarks are mandatory.
- Each bidder’s notification states only their own result.

### Validations
- Every confirmed participant has a decision.
- The submitter holds Evaluation Authority.
- The decider holds Reviewing / Approving Authority.
- Send-back includes remarks.

### Calculations
Counts of accepted and rejected are totals of line decisions. They are not scores.

### Workflow
Line decisions complete → list submitted → approved or returned. Approval is the gate into Module 10 for this auction.

### Search Requirements
Inbox by auction title and status.

### Documents
The reviewer can open the same dossiers as the evaluator, read only.

### Reports
The approved list is the operational output. It is not a separate warehouse report.

### Notifications
Approval notifies accepted bidders and rejected bidders, each with their own result, through Module 14. Return notifies the evaluator.

### Security
Bidders never receive the full list of who else was accepted or rejected.

### Integrations
None.

### Dependencies
F09-001. Module 14. Module 10 reads the approved list.

### Assumptions
- The approver is the Reviewing / Approving Authority, as set in the Statement of Work, because the source requires submission for approval where required and this baseline always requires it when evaluation is yes.

### Risks
If the approver delays past the live start, accepted bidders still cannot enter until approval. The schedule should leave time between participation end and live start. The system does not auto-approve.

### Non Functional Requirements
Approval and bidder notifications succeed together from the bidder’s point of view: a bidder is not admitted while being told they were rejected.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Eligible bidder list | UI | Medium | 6 |
| Evaluation approval decision | UI | Easy | 4 |
| Submit evaluation list | API | Medium | 6 |
| Approve or return evaluation list | API | Complex | 8 |
| Evaluation list approval records | DB | Easy | 2 |
| Evaluation list approval tests | Testing | Complex | 8 |
| Evaluation list approval notes | Documentation | Medium | 3 |

**Feature total: 37 hours**
