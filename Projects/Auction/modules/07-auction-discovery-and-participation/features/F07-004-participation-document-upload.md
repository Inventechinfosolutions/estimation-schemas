# F07-004 — Participation Document Upload

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-004 |
| **Feature Name** | Participation Document Upload |
| **Module** | 07 — Auction Discovery and Participation |

### Description
The bidder uploads the documents the auction requires for participation. Each requirement is listed, the file is stored against that bidder’s participation, and evaluation staff can open the files when Evaluation is yes. These files are separate from the bidder’s master profile documents.

### Business Objective
The participation pack contains the papers the auction asked for, tied to the bidder and the auction, ready for evaluation when evaluation is on.

### Actors
Maker: the participating bidder. Reader: Evaluation Authority. Approver: none.

### User Journey
1. Who creates: the bidder uploads each required document.
2. How they create: Participation → Documents → the checklist of requirements → upload a file against a requirement → Save.
3. How they edit: before confirmation and before participation end, they replace a file. The replaced file stays in history. After confirmation, the pack is frozen for evaluation.
4. How they send for approval: they do not. The pack is submitted by confirming participation.
5. How the approver sees pending items: there is no document-approval inbox. Evaluators open the pack in Module 09.
6. How the approver decides: there is no decision on this feature.
7. How the maker sees history: the bidder sees the current file and the replacements for their own participation.
8. How the auditor sees history: the evaluation authority sees the same history for participants of that auction.

### Functional Capabilities
- Show the auction’s participation document requirements
- Upload a file against a requirement
- Keep the file on that bidder’s participation
- Freeze the pack on confirmation
- Let evaluation staff read the pack

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Participation
- Requirement
- File

### Outputs
- Document checklist status
- Files for evaluation

### Business Rules
- Requirements come from the auction. The bidder cannot delete a requirement to make the list complete.
- A requirement is complete only when a file is stored against it.
- Profile master documents are not copied in automatically.
- Other bidders cannot read this pack.
- When Evaluation is no, the files are still stored and readable by department staff, because the source includes documents on the participation path in both branches.

### Validations
- File type and 70 MB size cap match auction documents.
- The participation belongs to the bidder.
- Upload after confirmation or after the participation end is rejected.

### Calculations
Checklist completeness is the share of requirements that have a file. If the auction states no extra requirements, the checklist is complete without a file. The source says required documents are uploaded; the creator has not been given a separate requirement-builder in the source. This feature therefore uses a single required participation-document set defined as at least the files the bidder is told to supply on the auction, captured as named requirements on the auction draft. Those requirement names are entered by the creator as part of auction documents configuration and shown here. If the creator defines none, confirmation does not wait for a file.

### Workflow
Upload → checklist complete → confirmation in F07-002 can proceed. No staff approval of each file.

### Search Requirements
Checklist on the participation. Staff filter participants by documents complete or incomplete.

### Documents
Participation documents for one bidder on one auction.

### Reports
None.

### Notifications
None of its own.

### Security
Bidder and authorised evaluation or department staff of that auction only.

### Integrations
None.

### Dependencies
F07-002. Auction document rules from F04-004 for file limits.

### Assumptions
- The source says the system displays applicable document requirements but does not define a library of requirement types. The creator names the requirements on the auction (for example registration certificate). That naming is included in this feature’s data, edited while the auction is still a draft, by the Auction Creator. It is not a separate module.
- If no requirement is named, the document step is empty and does not block confirmation.

### Risks
Free-text requirement names can be vague. The reviewer is expected to read them before approval.

### Non Functional Requirements
A file uploaded by one bidder is never listed on another bidder’s checklist.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Participation document checklist | UI | Medium | 6 |
| Participation document upload form | UI | Medium | 6 |
| Auction document requirement editor | UI | Medium | 6 |
| List participation document requirements | API | Easy | 4 |
| Upload participation document | API | Medium | 6 |
| Save participation document requirements | API | Medium | 6 |
| Participation document records | DB | Easy | 2 |
| Participation document tests | Testing | Medium | 6 |
| Participation document notes | Documentation | Easy | 2 |

**Feature total: 44 hours**
