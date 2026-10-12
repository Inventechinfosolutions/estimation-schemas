# F02-002 — Reusable Field Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Reusable Field Master |
| **Module** | 02 — Category and Catalogue Management |

### Description
The administrator defines fields once and reuses them on many categories. A field has a name and a type: text, number, date, select, or boolean. Select fields gain their options in F02-003. Mapping a field onto a category happens in F02-004, not here.

### Business Objective
Category forms stay consistent because the same fact (for example a capacity or a year) is defined once.

### Actors
Maker: System / Catalogue Administrator. Approver: none.

### User Journey
1. Who creates: the System / Catalogue Administrator creates a field.
2. How they create: Field master → New → name, type (text, number, date, select, boolean), active → Save.
3. How they edit: open the field and change the name or active status. The type cannot be changed after the field has been mapped or filled on an item, because stored values would no longer match.
4. How they send for approval: they do not.
5. How the approver sees pending items: there is no approver inbox.
6. How the approver decides: there is no approval decision.
7. How the maker sees history: field history shows name, type at creation, and activation changes.
8. How the auditor sees history: the System / Catalogue Administrator reads that history.

### Functional Capabilities
- Create a reusable field of one of the five types
- Deactivate a field so it cannot be newly mapped
- Search fields by name and type
- Block a type change after the field is in use

### UI Screens
| Screen | Complexity |
|---|---|


### Logical API operations
| Operation | Complexity |
|---|---|


### Inputs
- Field name
- Type
- Active status

### Outputs
- Field definitions available for category mapping

### Business Rules
- Types are only text, number, date, select, and boolean.
- A field is not tied to one category at creation. Mapping is F02-004.
- Deactivated fields remain on items that already captured them and are hidden from new mappings.
- Two fields may not share the same name.

### Validations
- Name and type are mandatory.
- Type change is rejected once any category mapping or item value exists.

### Calculations
None. Number fields store a number; they do not calculate a price.

### Workflow
Immediate save. No approval.

### Search Requirements
Name, type, active status.

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
None beyond the catalogue administrator role.

### Assumptions
- The source lists those five types and no others. File-upload is not a field type; images and documents are category media on the item.
- Field name is the business label shown on the item form.

### Risks
A poorly named field reused across unrelated categories will confuse bidders. Governance sits with the administrator, not with a second approval workflow.

### Non Functional Requirements
The field list is selectable when mapping a category, including type so the administrator does not map a select field by mistake.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Field register | UI | Medium | 6 |
| Field definition form | UI | Medium | 6 |
| Save field | API | Medium | 6 |
| Search fields | API | Medium | 6 |
| Field master records | DB | Easy | 2 |
| Field master tests | Testing | Medium | 6 |
| Field master notes | Documentation | Easy | 2 |

**Feature total: 34 hours**
