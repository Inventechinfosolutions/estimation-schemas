# F02-004 — Category–Field Mapping

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-004 |
| **Feature Name** | Category–Field Mapping |
| **Module** | 02 — Category and Catalogue Management |

### Description
The administrator chooses which reusable fields appear on a category, whether each is required or optional, and the order they appear on the item form. The same field may be required on one category and optional on another.

### Business Objective
The catalogue item form for a category shows the right questions, in the right order, with the right mandatory rules.

### Actors
Maker: System / Catalogue Administrator. Approver: none.

### User Journey
1. Who creates: the System / Catalogue Administrator maps fields onto a category.
2. How they create: open the category → Mapped fields → add a field → required or optional, display order → Save.
3. How they edit: change required or optional, change order, or remove a mapping. Removal stops the field appearing on new items. Values already stored on items remain readable.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: mapping history shows fields added, required-flag changes, reorders, and removals.
8. How the auditor sees history: the System / Catalogue Administrator reads that history.

### Functional Capabilities
- Map an active field to an active category
- Set required or optional per mapping
- Set display order per mapping
- Remove a mapping without deleting the reusable field or existing item values
- Expose the resulting form definition to catalogue item capture

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Category
- Field
- Required or optional
- Display order

### Outputs
- The dynamic form definition consumed by F02-005

### Business Rules
- A field is mapped at most once to the same category.
- Only active fields and active categories can receive a new mapping.
- Select fields bring their active options from F02-003. This screen does not edit options.
- Required is enforced when an item of that category is saved, not when the mapping is saved.

### Validations
- Category and field are mandatory.
- Duplicate mapping is rejected.
- Display order is a positive sequence without two fields on the same position.

### Calculations
None.

### Workflow
Immediate save. No approval.

### Search Requirements
From a category, list mapped fields. From a field, list categories that use it.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
System / Catalogue Administrator only. Auction creators see the result on the item, not this mapping screen.

### Integrations
None.

### Dependencies
F02-001 and F02-002. F02-003 when the field is select.

### Assumptions
- Category-specific configuration in the source is the required flag, display order, and the category’s own media flags. No further per-category formula language is included.
- Unmapped categories can still hold media and location if those flags are set, but they have no extra questions.

### Risks
Removing a required field from a category does not backfill old items. Operators must read history before they change a live category.

### Non Functional Requirements
Item capture reads the current mapping at the time the item is opened, so a just-saved mapping is what the administrator sees next.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Category field mapping screen | UI | Complex | 12 |
| Save category field mapping | API | Complex | 8 |
| Read category form definition | API | Medium | 6 |
| Category field mapping records | DB | Medium | 4 |
| Category field mapping tests | Testing | Medium | 6 |
| Category field mapping notes | Documentation | Medium | 3 |

**Feature total: 39 hours**
