# F04-006 — Draft Review and Submit for Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-006 |
| **Feature Name** | Draft Review and Submit for Approval |
| **Module** | 04 — Auction Creation |

### Description
Before submission the creator reads the whole draft: basic information, direction, bid type, procedure, parameters, pricing, EMD, items, documents, both schedules, delta, cutoff, display flags, and evaluation. They may save the draft, go back to a step, or submit for approval. Until submit, the auction stays a draft and is invisible to bidders.

### Business Objective
Only a complete draft reaches the reviewing authority, and the creator has seen every part of it first.

### Actors
Maker: Auction Creator. The submit creates work for the Reviewing / Approving Authority, who decides in F05-001.

### User Journey
1. Who creates: the Auction Creator assembles the draft across the earlier steps and creates the submission.
2. How they create: Review step → read each section → Save draft, go back, or Submit for approval. Submit is refused while any mandatory gap from F04-001 through F04-005 remains.
3. How they edit: Save draft keeps the auction editable. Go back opens the earlier step. After submit, the creator cannot edit unless the reviewer returns it.
4. How they send for approval: Submit for approval moves the auction to the reviewing authority and notifies them.
5. How the approver sees pending items: not on this screen. Their inbox is F05-001. The creator sees the status Submitted.
6. How the approver decides: not on this feature.
7. How the maker sees history: the creator sees save, submit, and any later return on the draft register.
8. How the auditor sees history: the reviewing authority sees the submitted pack and the submit event in the dossier.

### Functional Capabilities
- Present the full draft in one review
- Save a draft without submitting
- Return the creator to an earlier step
- Submit only when mandatory creation rules are met
- Lock the draft on submit and notify the reviewer

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- The draft built in F04-001 through F04-005
- The creator’s submit action

### Outputs
- Either a still-editable draft, or a submitted auction waiting in the review inbox

### Business Rules
- A draft is not visible to bidders and has no notice number.
- Submit checks title, direction, bid type, procedure, evaluation, commercial parameters, bid-change price, EMD amounts, at least one valid item or lot arrangement, schedule sequence, and delta.
- Submit does not approve the auction.
- A second submit of an already submitted auction is rejected.
- Go back does not discard saved data.

### Validations
- The mandatory set listed in the rules.
- The acting user must be the creator for that department or the catalogue administrator.
- Submit is blocked when the live start is not in the future.

### Calculations
None beyond the completeness checks defined on the earlier steps.

### Workflow
Draft → Submitted for review. The next decision is approve or return in F05-001.

### Search Requirements
Creator’s draft register by title, department, and status: draft, submitted, returned.

### Documents
The review lists the documents from F04-004. It does not upload a new kind of file.

### Reports
None.

### Notifications
Submit notifies the Reviewing / Approving Authority through Module 14.

### Security
Only the owning creator submits. Bidders cannot open the review step.

### Integrations
None.

### Dependencies
F04-001 through F04-005. Module 14 for the submit alert.

### Assumptions
- Save and continue on earlier steps is the same draft save. This feature is the explicit whole-draft review and the only submit.
- Returned auctions become editable drafts again and are resubmitted through this same action.

### Risks
A creator can submit a commercially odd but complete auction. The control for that is the reviewer, not a second automatic score.

### Non Functional Requirements
Submit either finishes completely or leaves the auction in draft. It must not leave a half-submitted status.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction review step | UI | Complex | 12 |
| Creator draft register | UI | Medium | 6 |
| Save auction draft | API | Medium | 6 |
| Submit auction for approval | API | Complex | 8 |
| Read full auction draft | API | Medium | 6 |
| Auction submission status records | DB | Easy | 2 |
| Draft review and submit tests | Testing | Complex | 8 |
| Draft review and submit notes | Documentation | Medium | 3 |

**Feature total: 51 hours**
