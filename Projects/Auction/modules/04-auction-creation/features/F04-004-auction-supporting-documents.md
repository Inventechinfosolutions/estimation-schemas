# F04-004 — Auction Supporting Documents

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-004 |
| **Feature Name** | Auction Supporting Documents |
| **Module** | 04 — Auction Creation |

### Description
The creator uploads the papers that explain the auction: PDF, DOC, XLS, JPG, or PNG, each no larger than 70 MB. After publication these files are what eligible bidders and the reviewer can open. Draft files stay with the draft and are not public.

### Business Objective
Bidders and reviewers read the same supporting papers the creator filed, within the formats and size the source states.

### Actors
Maker: Auction Creator. Approver: none on this step. Readers later: reviewing authority and eligible bidders.

### User Journey
1. Who creates: the Auction Creator uploads each supporting document on the draft.
2. How they create: Documents step → choose file → label → Upload. The list shows name, type, and size.
3. How they edit: while the draft is editable, they add another file or remove a file that was uploaded in error. After publication, papers change only by corrigendum, not by deleting the published file in silence.
4. How they send for approval: not from this step.
5. How the approver sees pending items: the reviewer opens the documents from the dossier after submit.
6. How the approver decides: not on this feature.
7. How the maker sees history: the draft shows files added and removed, with who and when.
8. How the auditor sees history: the reviewing authority sees that file history in the dossier.

### Functional Capabilities
- Upload PDF, DOC, XLS, JPG, and PNG up to 70 MB
- Label each file
- Remove a file while the auction is still an editable draft
- Show published files to eligible bidders and hide drafts

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- File
- Label

### Outputs
- Document list on the auction

### Business Rules
- Formats outside PDF, DOC, XLS, JPG, and PNG are rejected.
- Files over 70 MB are rejected.
- Bidders cannot see documents before publication.
- A published document is not removed by a draft-style delete. A correction is a corrigendum.

### Validations
- File and label are required.
- Type and size are checked before the file is stored.
- At least one document is not mandatory unless the creator’s department practice says so. The source allows upload; it does not say every auction has a paper. Submit therefore does not invent a minimum document count.

### Calculations
None beyond the size check.

### Workflow
Draft upload. No separate document approval. The auction approval covers the pack.

### Search Requirements
The document list is filtered by label on the draft.

### Documents
Auction supporting documents.

### Reports
None.

### Notifications
None.

### Security
Creator and reviewer while in draft or review. Eligible bidders after publication. Ineligible bidders do not receive the files.

### Integrations
None.

### Dependencies
F04-001 draft exists.

### Assumptions
- 70 MB is per file, as the source states for the auction creation documents.
- DOC and XLS mean the common office document and spreadsheet types used for those extensions. The source does not mention DOCX or XLSX; those extensions are accepted as the same document kinds so creators are not blocked by a file-save default. If the organisation forbids them, the allowed list can be tightened without a process change.

### Risks
Very large packs will be slow to open. The size cap is still 70 MB per file as stated.

### Non Functional Requirements
A rejected file is not stored and does not appear on the list.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction document upload panel | UI | Medium | 6 |
| Auction document list | UI | Easy | 4 |
| Upload auction document | API | Medium | 6 |
| Remove draft auction document | API | Easy | 4 |
| Auction document records | DB | Easy | 2 |
| Auction document tests | Testing | Medium | 6 |
| Auction document notes | Documentation | Easy | 2 |

**Feature total: 30 hours**
