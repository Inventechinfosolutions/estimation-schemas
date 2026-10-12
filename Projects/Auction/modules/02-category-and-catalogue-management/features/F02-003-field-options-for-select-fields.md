# F02-003 — Field Options for Select Fields

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Field Options for Select Fields |
| **Module** | 02 — Category and Catalogue Management |

### Description
For a field whose type is select, the administrator maintains the list of options a user may pick on a catalogue item. Options can be added, edited, reordered, and deactivated. Text, number, date, and boolean fields have no options.

### Business Objective
Select fields offer a controlled list, in a stable order, instead of free text that cannot be compared later.

### Actors
Maker: System / Catalogue Administrator. Approver: none.

### User Journey
1. Who creates: the System / Catalogue Administrator adds an option on a select field.
2. How they create: open the select field → Options → Add option → label and active → Save. Then drag or set the display order.
3. How they edit: change the label, reorder, or deactivate. An option already stored on an item remains visible on that item and is marked inactive for new selection.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: option history shows adds, renames, reorders, and deactivations.
8. How the auditor sees history: the System / Catalogue Administrator reads that history.

### Functional Capabilities
- Add and rename an option on a select field
- Set and change display order
- Deactivate an option so new items cannot pick it
- Reject option maintenance on non-select fields

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Select field
- Option label
- Display order
- Active status

### Outputs
- Ordered active options on the catalogue item form

### Business Rules
- Options exist only for select fields.
- Option labels are unique within the field.
- Inactive options are hidden on new items and on edits that have not already selected them.
- Order is explicit. A new option does not jump to the top unless the administrator places it there.

### Validations
- Label is mandatory.
- Duplicate label on the same field is rejected.
- The parent field must be type select.

### Calculations
None.

### Workflow
Immediate save. No approval.

### Search Requirements
Find a field, then list its options. Filter options by active status.

### Documents
None.

### Reports
None.

### Notifications
None.

### Security
System / Catalogue Administrator only.

### Integrations
None.

### Dependencies
F02-002 field of type select.

### Assumptions
- Single choice per select field on the item. The source does not ask for multi-select.
- Reorder is part of maintenance, as the source asks to maintain option order.

### Risks
Renaming an option changes the label bidders see on older items. History keeps the previous label.

### Non Functional Requirements
Option order on the item form matches the order saved here.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Select-field option list | UI | Medium | 6 |
| Option form | UI | Easy | 4 |
| Save field option | API | Easy | 4 |
| Reorder field options | API | Medium | 6 |
| Field option records | DB | Easy | 2 |
| Field option tests | Testing | Easy | 4 |
| Field option notes | Documentation | Easy | 2 |

**Feature total: 28 hours**
