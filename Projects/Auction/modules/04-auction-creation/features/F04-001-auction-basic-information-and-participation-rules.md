# F04-001 — Auction Basic Information and Participation Rules

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Auction Basic Information and Participation Rules |
| **Module** | 04 — Auction Creation |

### Description
The auction creator starts a draft with the title, department, description, direction, bid type, procedure, display flags, and the evaluation flag. When the bid type is prequalified or restricted, the creator names the bidders who may participate, chosen from active bidder accounts. Direct auctions do not use a closed list. Nothing on this step is visible to bidders.

### Business Objective
The draft records how the auction will behave before any item or schedule is added, including whether live bidding will be gated by evaluation.

### Actors
Maker: Auction Creator, for auctions in their department. Approver: none until F04-006 submits the whole draft.

### User Journey
1. Who creates: the Auction Creator creates the draft. A bidder cannot.
2. How they create: Auctions → New draft → title, department, description, forward or reverse, bid type (direct, prequalified, restricted), procedure (open or restricted), display flags, evaluation yes or no. If the bid type is prequalified or restricted, search active bidders and add them to the list → Save draft.
3. How they edit: while the auction is draft or returned, the creator changes any of these fields, including the evaluation flag and the closed list. After submission, this step is locked until the reviewer sends it back.
4. How they send for approval: not from this step alone. Submit of the whole draft is F04-006.
5. How the approver sees pending items: the reviewer does not see the draft until F04-006 submits it.
6. How the approver decides: not on this feature.
7. How the maker sees history: the creator sees revisions of title, direction, bid type, flags, and list membership while the draft is editable.
8. How the auditor sees history: after submission, the reviewing authority sees the same revision history as part of the dossier in F05-001.

### Functional Capabilities
- Capture title, department, description, and forward or reverse direction
- Set direct, prequalified, or restricted bid type
- Set open or restricted procedure
- Set display of reserve price, last accepted bid, and bidder list
- Set lot-wise EMD yes or no and evaluation yes or no
- Build the prequalified or restricted bidder list from active bidders

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Title
- Department
- Description
- Direction
- Bid type
- Procedure
- Display flags
- Lot-wise EMD flag
- Evaluation flag
- Bidder list when required

### Outputs
- Draft auction header used by the later creation steps

### Business Rules
- Title is required. Department must be an active department, and must be the creator’s department unless the user is the System / Catalogue Administrator.
- Direction is forward or reverse. It cannot be blank.
- Prequalified and restricted auctions must contain at least one active bidder before the draft can be submitted. Direct auctions must not keep a closed list.
- Evaluation yes means Module 09 will run. Evaluation no means it will not. The flag is not a post-auction score.
- Display flags do not themselves enter a reserve amount. The amount is F04-002.
- Bidders never see a draft.

### Validations
- Title, department, direction, bid type, procedure, and evaluation are mandatory.
- Closed-list bidders must be active.
- A direct auction with a leftover closed list is rejected on save.

### Calculations
None.

### Workflow
Part of the draft. Editable until submit, and again if the reviewer returns the auction. No approval on this step by itself.

### Search Requirements
Creator searches their drafts by title, department, and draft status. Bidder search does not include drafts.

### Documents
None on this step.

### Reports
None.

### Notifications
None until submit in F04-006.

### Security
Creator sees their department’s drafts. Another department’s creator does not. Bidders have no access.

### Integrations
None.

### Dependencies
F01-003 departments. F03-002 active bidders for a closed list.

### Assumptions
- Procedure type Open means visible to eligible bidders, and Restricted means participation is limited, as the source states. Combined with bid type, eligibility is the intersection of the two: a bidder must pass both the bid-type list (if any) and the procedure limitation.
- The creator may save an incomplete header as a draft. Submit, not this save, enforces the full set.

### Risks
Changing evaluation from yes to no after bidders have been evaluated is blocked once the auction is published. On a draft it is still allowed.

### Non Functional Requirements
Saving this step does not publish the auction and does not generate a notice number.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction basic information step | UI | Complex | 12 |
| Prequalified or restricted bidder picker | UI | Complex | 12 |
| Save auction basic information | API | Complex | 8 |
| Search active bidders for a closed list | API | Medium | 6 |
| Auction header records | DB | Medium | 4 |
| Auction basic information tests | Testing | Complex | 8 |
| Auction basic information notes | Documentation | Medium | 3 |

**Feature total: 53 hours**
