# F06-001 — Corrigendum Draft and Approval

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-001 |
| **Feature Name** | Corrigendum Draft and Approval |
| **Module** | 06 — Corrigendum Management |

### Description
An authorised user drafts a correction to a published auction, with the details of what changed. The corrigendum receives the next sequential number for that auction and is submitted for approval. Bidders do not see it until it is published in F06-002.

### Business Objective
Corrections to a live notice are numbered, reviewed, and not slipped into the original papers unseen.

### Actors
Maker: Auction Creator of that department, or the Reviewing / Approving Authority. Decider: Reviewing / Approving Authority.

### User Journey
1. Who creates: an authorised department user creates the corrigendum on a published auction.
2. How they create: open the published auction → Corrigenda → New → describe the correction → Save draft → Submit for approval.
3. How they edit: while it is draft or returned, the author edits the text. The sequential number is reserved at submit and does not change if the text is edited before approval.
4. How they send for approval: Submit for approval places it in the corrigendum inbox of the Reviewing / Approving Authority.
5. How the approver sees pending items: the inbox lists corrigenda awaiting approval for the department, with auction title, notice number, and proposed corrigendum number.
6. How the approver decides: Approve, or send back with remarks. Approval does not by itself show the corrigendum to bidders; publication is F06-002.
7. How the maker sees history: the author sees draft, submitted, returned, or approved.
8. How the auditor sees history: staff see the decision and remarks. Bidders see nothing until publication.

### Functional Capabilities
- Draft a corrigendum against a published auction
- Assign the next sequential number for that auction
- Submit, approve, or return
- Hide the draft from bidders

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Published auction
- Corrigendum text
- Decision and remarks

### Outputs
- An approved corrigendum waiting to be published, or a returned draft

### Business Rules
- Only a published auction can take a corrigendum.
- Numbers start at 1 for each auction and increase by 1. A returned draft keeps its number. A rejected gap is not created because send-back is not a cancellation.
- Two drafts cannot take the same next number.
- Approval is required before publication, for every corrigendum.
- The corrigendum does not silently rewrite history. The original published pack remains readable alongside the correction.

### Validations
- Text is mandatory.
- The auction is published.
- The decider holds the reviewing authority role and is not forced to be a different person from the author, because the source does not require two different people. The action is still recorded.

### Calculations
Next number is one more than the highest corrigendum number already used on that auction.

### Workflow
Draft → Submitted → Approved or Returned. Publication is the next feature.

### Search Requirements
By auction notice number, corrigendum number, and status.

### Documents
The corrigendum text is the document. Supporting files use the same type and size rules as auction documents when the author attaches a file.

### Reports
None.

### Notifications
Submit notifies the reviewing authority. Return and approval notify the author. Bidders are not notified until publication.

### Security
Department staff only. Bidders have no draft access.

### Integrations
None.

### Dependencies
F05-002 published auction. Module 14 for staff alerts.

### Assumptions
- Every corrigendum is approved before publication, because the source says approval where applicable and this Statement of Work applies that control to all corrigenda.
- The author may be the creator. The approver is the reviewing authority.

### Risks
If author and approver are the same person, the control is a recorded approval rather than a second pair of eyes. The organisation can split the roles.

### Non Functional Requirements
Number allocation does not issue two corrigenda with the same number when two authors submit together.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Corrigendum register | UI | Medium | 6 |
| Corrigendum form | UI | Complex | 12 |
| Corrigendum approval inbox | UI | Medium | 6 |
| Save corrigendum | API | Complex | 8 |
| Submit corrigendum | API | Medium | 6 |
| Decide corrigendum | API | Complex | 8 |
| Corrigendum records | DB | Medium | 4 |
| Corrigendum approval tests | Testing | Complex | 8 |
| Corrigendum approval notes | Documentation | Medium | 3 |

**Feature total: 61 hours**
