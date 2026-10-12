# F05-002 — Auction Notice and Publication

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | Auction Notice and Publication |
| **Module** | 05 — Auction Review, Approval and Publication |

### Description
After approval, an authorised user publishes the auction. The system assigns an auction notice number, and the auction becomes visible to eligible bidders with the configured details, documents, schedule, and participation conditions. Publication is refused if the auction is not approved.

### Business Objective
Eligible bidders discover a single published notice, and unpublished auctions stay hidden.

### Actors
Maker: Reviewing / Approving Authority, or the Auction Creator if the organisation allows the creator to publish after approval. The source says the approved auction is published; this feature lets the approving authority publish so publication stays a deliberate act. Approver: the approval already happened in F05-001.

### User Journey
1. Who creates: the Reviewing / Approving Authority publishes an auction they, or another holder of the role, have approved.
2. How they create: open the approved auction → review the notice preview → Publish. The system assigns the notice number and shows it on the confirmation.
3. How they edit: the notice number is not edited by hand and is not reused. After publication, content changes go through a corrigendum, not through a second publish that replaces the number.
4. How they send for approval: approval is already recorded. Publish does not open a second approval.
5. How the approver sees pending items: the publication list shows approved auctions that are not yet published.
6. How the approver decides: the decision is Publish. There is no separate reject at this step; send-back would have happened before approval.
7. How the maker sees history: the publisher sees the notice number, the time of publication, and their own name on the auction.
8. How the auditor sees history: the same publication event is on the auction history for authorised staff. Bidders see the published notice, not the internal approval remark.

### Functional Capabilities
- List approved auctions waiting to be published
- Assign one auction notice number
- Publish details, documents, schedule, and participation conditions to eligible bidders
- Refuse publication when the auction is not approved

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Approved auction
- Publish action

### Outputs
- Published auction with a notice number
- Bidder-visible pack

### Business Rules
- A notice number is generated once and is unique.
- Draft, submitted, and returned auctions cannot be published.
- Eligible bidders are those who pass the bid type and procedure. Ineligible bidders do not see the auction.
- Publication does not open live bidding early. Participation and live windows still follow the schedule.
- Publishing notifies eligible bidders and the creator.

### Validations
- Status is approved.
- Notice number generation must succeed before the status becomes published. If number generation fails, the auction stays approved.
- The user holds the reviewing authority role for the department.

### Calculations
The notice number is a sequential business number. It is not a bid and not a rank.

### Workflow
Approved → Published. This is the gate after F05-001.

### Search Requirements
Approved-but-unpublished list by title and department. After publication, bidder search is F07-001.

### Documents
Published copies of the supporting documents become readable by eligible bidders.

### Reports
None.

### Notifications
Publication notifies the creator and eligible bidders through Module 14.

### Security
Only the reviewing authority publishes. Bidders cannot call publish. Ineligible bidders receive neither the notice nor the documents.

### Integrations
None.

### Dependencies
F05-001 approval. Module 14.

### Assumptions
- The publisher is the Reviewing / Approving Authority so that publication is not an accidental side effect of clicking approve. The source lists approve and publish as a sequence, not as one click.
- Notice numbers are unique across the system, sequential, and not reset each year unless the organisation later asks for a year prefix. A year prefix would be a presentation change, not a new process.

### Risks
Publishing close to the participation start leaves bidders little time. The reviewer is expected to have checked the schedule before approval.

### Non Functional Requirements
Either the auction is published with a notice number, or it remains approved with no number. Bidders never see a number that was rolled back.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Publication waiting list | UI | Medium | 6 |
| Published notice preview | UI | Medium | 6 |
| Generate auction notice number | API | Complex | 8 |
| Publish auction | API | Complex | 8 |
| Auction notice records | DB | Easy | 2 |
| Auction publication tests | Testing | Complex | 8 |
| Auction publication notes | Documentation | Medium | 3 |

**Feature total: 41 hours**
