# F07-001 — Published Auction Search and Detail

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-001 |
| **Feature Name** | Published Auction Search and Detail |
| **Module** | 07 — Auction Discovery and Participation |

### Description
An active bidder searches published auctions and opens one they are allowed to see. The detail shows auction information, items or lots, description, documents, participation schedule, live schedule, terms, EMD requirements, and published corrigenda. Drafts and auctions outside the bidder’s eligibility stay hidden.

### Business Objective
A bidder can find the auctions they may consider and read the pack as published, including corrections.

### Actors
Maker: none. The bidder is a reader. The pack was created by staff. Approver: none.

### User Journey
1. Who creates: nobody creates an auction here. The bidder creates a search.
2. How they create: Bidder home → search by title, filter by department, status, and date → open a result.
3. How they edit: they cannot edit the auction. They can change their own search filters.
4. How they send for approval: they do not. Reading is not participation. Participation is F07-002.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: the bidder sees published corrigenda and the current schedule on the detail. They do not see draft revisions or internal send-back remarks.
8. How the auditor sees history: staff use Module 15 for the full history. This screen is the bidder’s reading view.

### Functional Capabilities
- Search published auctions by title
- Filter by department, status, and date
- Hide auctions the bidder is not eligible to see
- Show items or lots, documents, schedules, terms, EMD requirements, and published corrigenda

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Search text
- Department
- Status
- Date range

### Outputs
- A list of eligible published auctions and the detail of one auction

### Business Rules
- Only published auctions appear.
- A prequalified or restricted auction appears only to bidders on its list.
- Direct auctions appear to active bidders.
- Reserve price, last bid, and bidder names are not part of this pre-live detail except where the auction has already configured information that is meant to be visible before live bidding. Reserve display is enforced again during live bidding. Before live start, the detail shows EMD and terms, not other bidders’ bids.
- Documents are the published set plus published corrigenda.

### Validations
- The caller is an active bidder.
- The auction in the detail request is one the bidder is eligible to see. Otherwise the detail is refused, not returned empty of secret fields.

### Calculations
None.

### Workflow
No approval. Read only.

### Search Requirements
Title, department, status, participation or live dates.

### Documents
Published auction documents and corrigenda, read only.

### Reports
None.

### Notifications
None.

### Security
No cross-bidder data. No internal remarks. Ineligible auction identifiers do not reveal the title.

### Integrations
None.

### Dependencies
F05-002 and F06-002. F03-003 session.

### Assumptions
- Status filters a bidder may use are published, participation open, participation closed, live, and closed. Internal statuses such as submitted or returned are not offered.
- Terms and conditions are the description plus the published documents. There is no separate terms engine.

### Risks
A bidder who is added to a restricted list after publication should see the auction on the next search. Eligibility is checked at search time, not cached for the life of the notice.

### Non Functional Requirements
Search does not return another bidder’s participation or documents.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Bidder auction search | UI | Complex | 12 |
| Bidder auction detail | UI | Complex | 12 |
| Search published auctions for a bidder | API | Complex | 8 |
| Read bidder auction detail | API | Medium | 6 |
| Bidder-visible auction projection | DB | Medium | 4 |
| Published auction search tests | Testing | Complex | 8 |
| Published auction search notes | Documentation | Medium | 3 |

**Feature total: 53 hours**
