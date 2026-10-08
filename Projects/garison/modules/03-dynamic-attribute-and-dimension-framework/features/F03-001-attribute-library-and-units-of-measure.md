# F03-001 — Attribute Library & Units of Measure

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | Attribute Library & Units of Measure |
| Module | 03 — Dynamic Attribute & Dimension Framework |
| Module Type | Business |
| Release | Go-live |

### Description
Central library of attribute definitions used by category templates: technical dimensions (width, height, thickness, projection, diameter, length, spring angle and other category-specific measures) and descriptive attributes, each with data type, unit, permitted values, display format and attribute group (Classification, Technical, Material, Finish, Commercial/Availability).

### Business Objective
Define every product characteristic once, so it is captured, displayed, filtered and searched consistently and new characteristics can be added without code change.

### Actors
- Catalogue Administrator
- Super Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates attribute definitions; standard moulding attributes are seeded at go-live.
2. **How they create:** They add an attribute with code, label, help text, data type (number, text, single list, multi-select, yes/no), unit, decimal/fraction precision, permitted values and group.
3. **How they edit:** They edit labels, help text, permitted values and order freely; changing data type or unit of an in-use attribute is blocked or requires a guided conversion.
4. **How they send for approval:** No review is required; attribute definitions take effect on save.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies; the change guard warns when an attribute is used by templates and products.
7. **How the maker sees history:** The administrator sees the attribute change history.
8. **How the approver / auditor sees history:** Auditors see attribute and permitted-value changes in the audit log.

### Functional Capabilities
- Attribute library register with group, type, unit and usage count
- Data types: decimal number, integer, text, single-select list, multi-select list, yes/no
- Units of measure master (inch, foot, millimetre, degree) with conversion factors
- Permitted values editor with order and retire
- Attribute groups controlling display sections on the product page
- Change guard on in-use attributes (type and unit changes)
- Seed: Width, Height, Thickness, Projection, Diameter, Length, Spring Angle, Profile Shape and commercial attributes

### UI Screens
- Attribute library register
- Attribute definition form
- Permitted values list editor
- Unit of measure master
- Attribute group master

### Logical API Operations
- List attributes with usage
- Create attribute definition
- Update attribute definition with change guard
- Maintain permitted values
- Maintain units and conversion factors
- Maintain attribute groups
- Seed standard moulding attributes

### Inputs
- Code, label, help text, data type, unit, precision, permitted values, group, display order

### Outputs
- Attribute definitions consumed by templates (F03-002), product entry (F04-002), filters (F09-003) and import (F12-001)

### Business Rules
- Attribute code unique and immutable after creation
- Data type of an in-use attribute cannot change
- Retired permitted values remain on existing products but cannot be newly selected

### Validations
- Label mandatory
- Unit mandatory for numeric dimension attributes
- Permitted values unique within attribute

### Calculations
- Usage count across templates and products

### Workflow
Active ↔ Retired

### Search Requirements
- Label, code, group, type

### Documents
- None

### Reports
- Attribute dictionary export for data population team

### Notifications
- None

### Security
- Manage attributes permission

### Integrations
- None

### Dependencies
- F03-002
- F03-004
- F04-002

### Assumptions
- Dimension values are single numbers (not ranges) per product; ranges handled as two attributes if needed

### Risks
- Attribute sprawl if every source term becomes a new attribute; governed by Garrison approval at discovery

### Non Functional Requirements
- Library cached for form rendering

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Attribute library register | Medium | 6 |
| UI | Attribute definition form | Complex | 12 |
| UI | Permitted values list editor | Medium | 6 |
| UI | Unit of measure master | Easy | 4 |
| UI | Attribute group master | Easy | 4 |
| API | List attributes with usage | Medium | 6 |
| API | Create attribute definition | Complex | 8 |
| API | Update attribute definition with change guard | Complex | 8 |
| API | Maintain permitted values | Medium | 6 |
| API | Maintain units and conversion factors | Easy | 4 |
| API | Maintain attribute groups | Easy | 4 |
| API | Seed standard moulding attributes | Easy | 4 |
| Database | Attribute definition | Medium | 4 |
| Database | Permitted value list | Easy | 2 |
| Database | Unit of measure and conversion factors | Easy | 2 |
| Database | Attribute group | Simple | 1 |
| Testing | Attribute data type validation matrix | Medium | 6 |
| Testing | Change guard on in-use attributes | Medium | 6 |
| Documentation | Attribute library reference | Medium | 3 |

**Feature Total: 96 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 40 | 9 | 0 | 12 | 3 | **96** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Change guard and conversion handling drive the Complex API rows
- No external integration channel in this feature; Integration row omitted.
