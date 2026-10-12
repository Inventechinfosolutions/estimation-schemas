# F05-001 — Auction Review and Decision

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-001 |
| **Feature Name** | Auction Review and Decision |
| **Module** | 05 — Auction Review, Approval and Publication |

### Description
The reviewing authority opens a submitted auction, checks items, parameters, documents, and both schedules, and either approves it or sends it back to the creator with remarks. Approval makes the auction eligible for publication. Send-back unlocks the draft for correction. Bidders still cannot see it.

### Business Objective
No auction is published until a designated authority has accepted the pack or sent it back for a recorded correction.

### Actors
Maker: Auction Creator, who submitted. Decider: Reviewing / Approving Authority.

### User Journey
1. Who creates: the creator already submitted. The authority creates the decision.
2. How they create: Review inbox → open the auction dossier → read header, parameters, items or lots, documents, and schedule → Approve or Send back, with remarks → Confirm.
3. How they edit: they do not rewrite the creator’s items on this screen. A send-back lets the creator edit. The authority may replace a decision only while it has not yet been published; once published, changes go through a corrigendum.
4. How they send for approval: the creator already did that in F04-006. This feature is the decision.
5. How the approver sees pending items: the inbox lists auctions submitted for review in the authority’s department, oldest first, with title and submitted time.
6. How the approver decides: Approve, which records approval and allows publication, or Send back, which returns the auction to the creator as an editable draft and keeps the remarks.
7. How the maker sees history: the creator sees approved or returned, and the remarks on a return.
8. How the auditor sees history: the authority and the creator see who decided, when, and the remark. Bidders do not see internal return remarks.

### Functional Capabilities
- List submitted auctions for the authority’s department
- Read the full dossier including documents and schedule
- Approve, which permits publication
- Send back with remarks and reopen the draft
- Keep a decision history

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Submitted auction
- Decision
- Remarks

### Outputs
- Approved auction awaiting publication, or a returned draft
- Decision history
- Notification to the creator

### Business Rules
- Only a submitted auction can be approved or returned.
- The authority cannot approve an auction they created if the organisation has given both roles to one person is still technically possible; the source does not forbid it. The screen records the user either way.
- Send-back remarks are mandatory. Approval remarks are optional.
- A returned auction has no notice number.
- Bidders cannot open the inbox or the dossier.

### Validations
- The auction is in submitted status.
- Send-back requires remarks.
- The user holds Reviewing / Approving Authority for that department.

### Calculations
None.

### Workflow
Submitted → Approved, or Submitted → Returned for correction. A corrected resubmit comes back to this inbox.

### Search Requirements
Inbox filter by title, department, and submitted date.

### Documents
Read-only access to the auction supporting documents.

### Reports
None.

### Notifications
Approval and return notify the creator through Module 14.

### Security
Department-scoped. Internal remarks stay off the bidder portal.

### Integrations
None.

### Dependencies
F04-006. Module 14.

### Assumptions
- One reviewing authority role covers this decision. The source does not require a multi-step committee.
- The same role later approves corrigenda, evaluation lists, and finalisation, which are separate inboxes.

### Risks
A reviewer who also created the auction can approve their own draft if both roles are assigned. That is an organisational assignment issue the source permits.

### Non Functional Requirements
The dossier shows the pack as submitted. A concurrent edit by the creator is impossible because submit locked the draft.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Auction review inbox | UI | Medium | 6 |
| Auction review dossier | UI | Very High | 16 |
| Review decision form | UI | Medium | 6 |
| List auctions pending review | API | Medium | 6 |
| Read auction review dossier | API | Medium | 6 |
| Record auction review decision | API | Complex | 8 |
| Auction review decision records | DB | Medium | 4 |
| Auction review tests | Testing | Complex | 8 |
| Auction review notes | Documentation | Medium | 3 |

**Feature total: 63 hours**
