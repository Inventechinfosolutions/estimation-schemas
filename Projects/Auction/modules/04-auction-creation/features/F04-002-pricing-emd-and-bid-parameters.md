# F04-002 — Pricing, EMD and Bid Parameters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Pricing, EMD and Bid Parameters |
| **Module** | 04 — Auction Creation |

### Description
On the draft, the creator sets whether bidding is item-wise or by lot, whether prices are inclusive or exclusive of GST, and how EMD is structured: a common EMD, an item-wise EMD, or a lot-level EMD when lot-wise EMD was switched on. The creator also records the bid-change price used later to accept or reject a live bid, and the reserve price amount that may be displayed. The system does not calculate GST and does not reject a bid for missing the reserve.

### Business Objective
Live bidding and participation apply one agreed commercial setup instead of improvising rules at bid time.

### Actors
Maker: Auction Creator. Approver: none on this step.

### User Journey
1. Who creates: the Auction Creator records the parameters on the draft they own.
2. How they create: Parameters step → item-wise or lot-wise, GST inclusive or exclusive, EMD type, bid-change price, reserve amounts at item or lot level once items exist → Save.
3. How they edit: while the draft is editable, they change the structure, the format, the EMD type, the bid-change price, and reserve amounts. After publication these commercial rules are not edited in place; a change of terms goes through a corrigendum.
4. How they send for approval: not from this step. Submit is F04-006.
5. How the approver sees pending items: the reviewer reads these parameters inside the dossier after submit.
6. How the approver decides: not on this feature.
7. How the maker sees history: parameter revisions are kept on the draft.
8. How the auditor sees history: the reviewing authority sees those revisions in the dossier.

### Functional Capabilities
- Choose item-wise or group/lot-wise structure
- Choose GST inclusive or exclusive as a label on bids, without computing tax
- Choose common EMD, item-wise EMD, or lot-wise EMD when the lot-wise flag is on
- Record the bid-change price for later live validation
- Record reserve price amounts for display, without turning them into an automatic floor

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Structure
- Pricing format
- EMD type
- Bid-change price
- Reserve amount per item or lot

### Outputs
- Commercial parameters stored on the draft and later enforced in participation and live bidding

### Business Rules
- Lot-wise EMD is available only when the auction’s lot-wise EMD flag is yes and the structure is group/lot-wise.
- Item-wise EMD is stored per selected item. Common EMD is one amount for the auction. Lot-wise EMD is one amount per lot.
- Bid-change price is a positive amount. Forward auctions use it as the minimum increase. Reverse auctions use it as the minimum decrease.
- Reserve amounts are hidden from bidders unless display reserve price is yes.
- No GST amount is computed from the format flag.
- A bid is not rejected later merely because it is on the wrong side of the reserve.

### Validations
- Structure, pricing format, and EMD type are required before submit.
- Bid-change price must be greater than zero before submit.
- EMD amounts must be zero or positive numbers. A blank EMD amount blocks submit.
- Lot-wise EMD cannot be combined with item-wise structure.

### Calculations
No tax calculation. The only numeric check is that a later live bid moves by at least the bid-change price in the auction’s direction. That check runs in F10-002; this feature only stores the number.

### Workflow
Draft save. Locked after submit until a return.

### Search Requirements
Not a search feature. Parameters are read with the draft.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
Creator and, after submit, the reviewing authority. Bidders see EMD requirements and the pricing format only after publication, and see the reserve only when the display flag allows.

### Integrations
None.

### Dependencies
F04-001 flags. Reserve and per-item EMD amounts can be completed after F04-003 has selected items; submit checks that they are present.

### Assumptions
- Bid-change price is included because the source requires live validation of the applicable bid change price, while the creation screen in the source does not name the field.
- Reserve amount is included so the display flag has a value to show. It is not an automatic commercial floor.

### Risks
If the organisation later wants bids below reserve to fail, F10-002 must change. This feature would then store a rule it does not store today.

### Non Functional Requirements
Parameter combinations that the source forbids are rejected on save, not only at go-live testing.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Parameter configuration step | UI | Complex | 12 |
| Save pricing and EMD parameters | API | Complex | 8 |
| Validate parameter combination | API | Medium | 6 |
| Auction commercial parameter records | DB | Medium | 4 |
| Pricing and EMD parameter tests | Testing | Complex | 8 |
| Pricing and EMD parameter notes | Documentation | Medium | 3 |

**Feature total: 41 hours**
