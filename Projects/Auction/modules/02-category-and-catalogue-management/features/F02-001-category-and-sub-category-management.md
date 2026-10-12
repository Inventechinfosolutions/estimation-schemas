# F02-001 — Category and Sub-category Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Category and Sub-category Management |
| **Module** | 02 — Category and Catalogue Management |

### Description
The catalogue administrator builds the tree of categories and sub-categories that will drive item forms. Each category can require an image, a video, and a geographical location. Categories can be deactivated so they disappear from new item capture and from new auctions without deleting items already stored.

### Business Objective
Every auctioned item sits under a controlled category whose media and location rules are known before the item is created.

### Actors
Maker: System / Catalogue Administrator. Approver: none.

### User Journey
1. Who creates: the System / Catalogue Administrator creates a category or a sub-category under a parent.
2. How they create: Category tree → New → name, optional parent, image required, video required, location required, active → Save.
3. How they edit: open the category, change the name or the three requirement flags, or move it under another parent. Items already saved keep the values they captured; the new flags apply to later edits and new items.
4. How they send for approval: they do not. Category maintenance is not an auction approval.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: category history shows parent moves, requirement-flag changes, and activation changes.
8. How the auditor sees history: the same history is available to the System / Catalogue Administrator.

### Functional Capabilities
- Create a category and a sub-category with a parent
- Prevent a cycle in the parent-child tree
- Set image, video, and geographical-location requirements
- Activate or deactivate a category
- Search and browse the tree

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Name
- Parent category or none
- Image required
- Video required
- Location required
- Active status

### Outputs
- Category tree used by field mapping and by catalogue items

### Business Rules
- A category cannot be its own parent and cannot sit under one of its descendants.
- A deactivated category is hidden from new item creation and from new field mapping. Existing items remain readable.
- Image, video, and location flags are category-level. They are not free choices on each item.
- Only the catalogue administrator maintains the tree. Auction creators select items; they do not edit categories.

### Validations
- Name is mandatory.
- Parent, if set, must be an existing category that does not create a cycle.
- Deactivating a parent shows the administrator that child categories will also be unavailable for new items.

### Calculations
None.

### Workflow
Immediate save. No approval.

### Search Requirements
Name, parent, active status.

### Documents
None on the category itself. Media belongs to the item in F02-005.

### Reports
None.

### Notifications
None.

### Security
System / Catalogue Administrator only.

### Integrations
None.

### Dependencies
F01-002 role permission.

### Assumptions
- A category may be a root or a child. The source asks for parent-child relationships and does not limit depth. A practical depth is enforced only to stop cycles, not to invent a fixed number of levels.
- Requirement flags default to not required until the administrator sets them.

### Risks
Changing a requirement flag after items exist can make older items look incomplete. History must show when the flag changed.

### Non Functional Requirements
The tree remains usable as a picker on the item form and on auction item search.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Category tree register | UI | Complex | 12 |
| Category form | UI | Medium | 6 |
| Save category | API | Medium | 6 |
| Move category parent | API | Complex | 8 |
| Activate or deactivate category | API | Easy | 4 |
| Search categories | API | Medium | 6 |
| Category hierarchy records | DB | Medium | 4 |
| Category management tests | Testing | Complex | 8 |
| Category management notes | Documentation | Medium | 3 |

**Feature total: 57 hours**
