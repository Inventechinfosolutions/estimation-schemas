# F02-005 — Catalogue Item Maintenance

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-005 |
| **Feature Name** | Catalogue Item Maintenance |
| **Module** | 02 — Category and Catalogue Management |

### Description
The administrator creates an item against one category. The form shows that category’s mapped fields in order, plus image, video, document, and geographical location when the category requires them. The item can be edited, activated, deactivated, searched, and viewed. Only an active item can be selected into an auction, and selecting it does not change this master record.

### Business Objective
The organisation has one reusable item record that later auctions can offer without copying or altering the master.

### Actors
Maker: System / Catalogue Administrator. Approver: none. Auction Creator is a later reader of active items, not an editor.

### User Journey
1. Who creates: the System / Catalogue Administrator creates the catalogue item.
2. How they create: Catalogue items → New → choose an active category → complete required fields, upload required media, capture location if required → Save. The item may be saved inactive until media is complete, and activated when it is ready to auction.
3. How they edit: open the item and change field values, media, location, or active status. Auctions that already selected the item keep the selection they made; they do not silently rewrite the master, and this edit does not rewrite those auctions.
4. How they send for approval: they do not. Making an item active is an administrative action, not an auction approval.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: item history shows field-value changes, media changes, location changes, and activation.
8. How the auditor sees history: the System / Catalogue Administrator reads that history. An auction reviewer can open the current item when reviewing a draft, which is a read in Module 05, not an edit.

### Functional Capabilities
- Build the item form from the category mapping
- Capture text, number, date, select, and boolean values
- Upload images, video, and documents when the category requires them
- Capture geographical location when required
- Activate, deactivate, search, and view items
- Offer only active items to auction creation

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Category
- Mapped field values
- Media files
- Location
- Active status

### Outputs
- A catalogue item that auction creation can select
- Item history

### Business Rules
- The category is chosen at creation and is not switched later, because the field set would no longer match.
- Required mapped fields must be filled before activation.
- If the category requires image, video, or location, activation is blocked until that requirement is met.
- Inactive items are excluded from auction item search.
- No action on an auction may update this item’s fields, media, or location.

### Validations
- Category is an active category.
- Select values must be active options.
- Number and date values must match the field type.
- Required fields and required media block activation.

### Calculations
None. The item does not compute a reserve or a bid.

### Workflow
Save and activate are immediate. There is no approval inbox. The auction that later uses the item has its own approval.

### Search Requirements
Category, name or identifying text fields, active status, and whether media is present.

### Documents
Images, video, and documents required by the category, stored on the item.

### Reports
None.

### Notifications
None.

### Security
Only the System / Catalogue Administrator creates and edits items. Auction Creator and reviewers get a read of active items. Bidders see item detail only through a published auction, not through this master screen.

### Integrations
None.

### Dependencies
F02-001 and F02-004. F02-003 for select values.

### Assumptions
- Geographical location is a captured point or place description the administrator enters. The source does not require a map product or a GIS integration.
- A catalogue size cap for media is an operational limit. The 70 MB figure in the source applies to auction supporting documents, not automatically to every catalogue video. The item screen still enforces whatever operational cap is configured and tells the administrator when a file is too large.

### Risks
Activating an item with the wrong category cannot be fixed by relabelling. The administrator must deactivate it and create a new item.

### Non Functional Requirements
Search returns only items the caller is allowed to use: all items for the administrator, active items for the auction creator.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Catalogue item register | UI | Complex | 12 |
| Dynamic catalogue item form | UI | Very High | 16 |
| Item media and location panel | UI | Complex | 12 |
| Catalogue item detail | UI | Medium | 6 |
| Save catalogue item | API | Complex | 8 |
| Search catalogue items | API | Medium | 6 |
| Activate or deactivate catalogue item | API | Easy | 4 |
| Upload catalogue item media | API | Medium | 6 |
| Catalogue item and media records | DB | Complex | 6 |
| Catalogue item tests | Testing | Complex | 8 |
| Catalogue item notes | Documentation | Complex | 4 |

**Feature total: 88 hours**
