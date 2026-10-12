# F04-003 — Catalogue Item Selection and Lot Organisation

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Catalogue Item Selection and Lot Organisation |
| **Module** | 04 — Auction Creation |

### Description
The creator searches the active catalogue, selects items, and sees the selected count. If the auction is item-wise, each selected item stands alone for later bidding. If it is group/lot-wise, the creator bundles the selected items into lots. The catalogue master is not edited from this step.

### Business Objective
The auction offers real catalogue items, arranged the way the commercial structure requires, without corrupting the master.

### Actors
Maker: Auction Creator. Approver: none on this step.

### User Journey
1. Who creates: the Auction Creator selects items and, where needed, defines lots on the draft.
2. How they create: Items step → search and filter active catalogue items → select → confirm the count. For a lot-wise auction, create a lot, name it, and place selected items into it.
3. How they edit: while the draft is editable, they add or remove items and move items between lots. Removing an item here does not deactivate it in the catalogue.
4. How they send for approval: not from this step.
5. How the approver sees pending items: the reviewer sees the selected items and lots in the dossier after submit.
6. How the approver decides: not on this feature.
7. How the maker sees history: the draft records items added, items removed, and lot moves.
8. How the auditor sees history: the reviewing authority sees that selection history in the dossier.

### Functional Capabilities
- Search and filter active catalogue items
- Select items and show the selected count
- Refuse inactive items
- Arrange selected items into lots when the structure is group/lot-wise
- Leave the catalogue master unchanged

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Selected catalogue items
- Lot names and item membership when lot-wise

### Outputs
- The auction’s item or lot list
- A selection that later bidding uses

### Business Rules
- Only active catalogue items can be added.
- An item may sit in only one lot on the same auction.
- A lot-wise auction cannot be submitted with an item left outside a lot, or with an empty lot.
- An item-wise auction has no lots.
- Opening an item from this step is read-only. Field edits belong in F02-005.

### Validations
- At least one item before submit.
- Lot-wise rules above.
- The same catalogue item cannot be selected twice onto one auction.

### Calculations
Selected-item count is the number of distinct catalogue items on the draft.

### Workflow
Draft save. Locked after submit until return.

### Search Requirements
Catalogue search by category and identifying text, active items only.

### Documents
Item media is shown read-only from the catalogue. It is not re-uploaded here.

### Reports
None.

### Notifications
None.

### Security
Creator searches the active catalogue. They cannot open inactive items or edit masters. Bidders do not see the selection until publication.

### Integrations
None.

### Dependencies
F02-005 active items. F04-002 structure decides whether lots are required.

### Assumptions
- The source’s items screen is search, filter, list, select, and count, plus lot organisation when configured. No price is taken from the catalogue because the catalogue does not store a selling price.

### Risks
If a catalogue item is deactivated after it was selected onto a draft, the draft keeps the selection and the reviewer can see that the master is now inactive. Submit warns the creator. The master is still not edited.

### Non Functional Requirements
Selecting an item writes an auction selection only. A comparison of the catalogue item before and after selection shows no master change.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Catalogue selection workspace | UI | Complex | 12 |
| Selected items and lots organiser | UI | Complex | 12 |
| Search selectable catalogue items | API | Medium | 6 |
| Attach items to auction | API | Complex | 8 |
| Organise auction lots | API | Complex | 8 |
| Auction item and lot records | DB | Medium | 4 |
| Item selection and lot tests | Testing | Complex | 8 |
| Item selection and lot notes | Documentation | Medium | 3 |

**Feature total: 61 hours**
