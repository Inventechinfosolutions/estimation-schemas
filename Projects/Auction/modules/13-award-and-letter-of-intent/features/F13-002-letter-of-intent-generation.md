# F13-002 — Letter of Intent Generation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F13-002 |
| **Feature Name** | Letter of Intent Generation |
| **Module** | 13 — Award and Letter of Intent |

### Description
After the award is approved, the system generates a Letter of Intent for the successful bidder of each item or lot. The letter carries the auction, the auction notice number, the successful bidder, the item or lot, the final accepted result, and the award. It is available to that bidder and to the awarding authority. Other bidders do not receive it.

### Business Objective
The successful bidder receives a formal letter assembled from the awarded result, and no other bidder receives that letter.

### Actors
Maker: Awarding Authority, who generates and issues the letter. Reader: the successful bidder. Approver: the award approval already given in F13-001.

### User Journey
1. Who creates: the Awarding Authority generates the letter. The bidder does not draft it.
2. How they create: on the awarded auction → preview the letter for each successful bidder and item or lot → Issue. The bidder later opens Letters on their portal.
3. How they edit: the issued letter is not hand-edited. A change of winner would have required a different finalisation, which is already approved. Template wording is the organisation’s wording, applied consistently, not retyped per letter.
4. How they send for approval: award approval is the approval. Issue does not open another inbox.
5. How the approver sees pending items: the authority sees awarded auctions that do not yet have letters issued.
6. How the approver decides: Issue is the act. They can abandon the preview without issuing.
7. How the maker sees history: the authority sees when each letter was issued and for which item or lot.
8. How the auditor sees history: staff history shows the issue event. The successful bidder sees their own letter. Other bidders see neither the letter nor the fact of another bidder’s letter on their portal.

### Functional Capabilities
- Assemble the letter from auction, notice number, bidder, item or lot, final result, and award
- Preview it before issue
- Issue it to the successful bidder only
- Refuse to generate a letter before award approval
- Keep one letter per successful item or lot selection

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Awarded auction
- Organisation letter wording
- Issue action

### Outputs
- Letter of Intent available to the successful bidder and the awarding authority

### Business Rules
- No letter before award approval, and no award before finalisation approval.
- The letter is generated, not uploaded as an uncontrolled file, so the notice number and result match the auction.
- One letter is produced for each approved selection (each item or each lot).
- Other bidders cannot open the letter.
- The letter is not a digitally signed instrument. No signature service is in scope.

### Validations
- Award exists.
- Each selection has a successful bidder and a final amount.
- The user holds Awarding Authority.
- Issue is refused if a letter for that selection already exists.

### Calculations
The amount on the letter is the final accepted bid of the selected bidder for that item or lot. No tax is added.

### Workflow
Award approved → preview → issued. Bidder notification is F13-003.

### Search Requirements
Authority searches issued letters by notice number. The bidder sees only their own.

### Documents
The Letter of Intent itself.

### Reports
None.

### Notifications
Issue does not by itself complete the auction. F13-003 sends the advice and completes. The letter becomes visible to the bidder at issue so the advice in F13-003 has something to point to.

### Security
Successful bidder and awarding authority only, plus staff who already hold award or review roles for that department when they open the auction history.

### Integrations
None.

### Dependencies
F13-001. Template wording supplied by the organisation.

### Assumptions
- The organisation supplies the fixed wording around the data fields. The system fills auction, notice number, bidder, item or lot, amount, and award date.
- A multi-item auction produces one letter per item or lot, not a merged letter, so each result stays traceable. The bidder sees all of their letters for that auction together.

### Risks
If the template wording is late, letters cannot be issued. That is an organisation dependency, not a system guess at legal text.

### Non Functional Requirements
The figures on the letter match the approved selection. They are not retyped.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Letter of Intent preview | UI | Complex | 12 |
| Letter issue confirmation | UI | Easy | 4 |
| Bidder letter view | UI | Medium | 6 |
| Generate letter of intent | API | Complex | 8 |
| Issue letter of intent | API | Complex | 8 |
| Letter of intent records | DB | Medium | 4 |
| Letter of intent tests | Testing | Complex | 8 |
| Letter of intent notes | Documentation | Complex | 4 |

**Feature total: 54 hours**
