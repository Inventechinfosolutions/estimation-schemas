# F06-002 — Corrigendum Publication and Bidder Access

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F06-002 |
| **Feature Name** | Corrigendum Publication and Bidder Access |
| **Module** | 06 — Corrigendum Management |

### Description
An approved corrigendum is published on the auction. Eligible bidders then see it with the auction information, and they are notified. Unpublished corrigenda stay hidden. The latest published corrigendum is identified as the latest, while earlier published corrigenda remain readable.

### Business Objective
Bidders always have the issued corrections, in number order, and never a draft correction.

### Actors
Maker: Reviewing / Approving Authority, publishing an approved corrigendum. Reader: eligible bidder.

### User Journey
1. Who creates: the Reviewing / Approving Authority publishes the approved corrigendum. The bidder does not create it.
2. How they create: open the approved corrigendum → Publish. The bidder later opens the auction and sees the corrigendum list.
3. How they edit: a published corrigendum is not edited. A further change is a new corrigendum with the next number.
4. How they send for approval: already approved in F06-001.
5. How the approver sees pending items: the publication list shows approved, not-yet-published corrigenda.
6. How the approver decides: Publish is the act. There is no second reject.
7. How the maker sees history: the publisher sees the publication time on the corrigendum.
8. How the auditor sees history: staff see publication on the auction history. The bidder sees the published text and number, not the internal approval remark.

### Functional Capabilities
- Publish an approved corrigendum
- Show published corrigenda to eligible bidders in number order
- Mark the latest published corrigendum
- Hide drafts and unapproved corrigenda from bidders

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Approved corrigendum
- Publish action

### Outputs
- Bidder-visible corrigendum
- Notification to eligible bidders

### Business Rules
- Only an approved corrigendum can be published.
- Ineligible bidders do not see it.
- Publication does not change the auction notice number.
- Earlier published corrigenda stay visible so a bidder can read the sequence.

### Validations
- Status is approved.
- The user holds the reviewing authority for the department.
- The parent auction is still published and not completed.

### Calculations
None. Latest means the highest published number.

### Workflow
Approved → Published. Bidders are notified.

### Search Requirements
Bidder opens the auction and sees its corrigenda. They do not search a global corrigendum catalogue.

### Documents
The published corrigendum text and any attachment.

### Reports
None.

### Notifications
Publication notifies eligible bidders and the auction creator through Module 14.

### Security
Same eligibility as the auction itself. Internal remarks remain staff-only.

### Integrations
None.

### Dependencies
F06-001. Module 14.

### Assumptions
- A corrigendum can be published during participation or before the live auction. Publishing one after the auction is completed is refused, because the source ties corrigendum to the published auction bidders are still reading. A completed auction is read from history instead.

### Risks
A late corrigendum during live bidding can confuse bidders. The system allows it because the source does not forbid the timing, and the authority is accountable for publishing it.

### Non Functional Requirements
Bidders who already have the auction open see the new corrigendum without being shown another bidder’s data.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Publish corrigendum confirmation | UI | Easy | 4 |
| Bidder corrigendum viewer | UI | Medium | 6 |
| Publish corrigendum | API | Complex | 8 |
| List corrigenda for an auction | API | Medium | 6 |
| Corrigendum publication records | DB | Easy | 2 |
| Corrigendum publication tests | Testing | Medium | 6 |
| Corrigendum publication notes | Documentation | Easy | 2 |

**Feature total: 34 hours**
