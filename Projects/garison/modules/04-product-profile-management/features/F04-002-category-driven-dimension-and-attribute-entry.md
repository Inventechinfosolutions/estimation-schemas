# F04-002 — Category-driven Dimension & Attribute Entry

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-002 |
| Feature Name | Category-driven Dimension & Attribute Entry |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Dynamic dimensions and attributes panel in the product workspace, rendered from the category's published template: only applicable fields appear, grouped and ordered, with mandatory and conditional rules, permitted values, unit-aware dimension inputs and inline validation.

### Business Objective
Capture accurate, structured technical data for each profile, so detail pages, specification search and filters work without irrelevant fields.

### Actors
- Catalogue Administrator
- Data population team (via admin)

### User Journey
1. **Who creates:** The Catalogue Administrator enters dimension and attribute values for a product they created or are maintaining.
2. **How they create:** On opening the Dimensions tab the system renders the template fields; they type dimensions in any accepted format (F03-004) and select list values.
3. **How they edit:** They edit values while the product is Draft, Changes Requested or in a working draft; conditional fields appear or disappear as controlling values change.
4. **How they send for approval:** Values are submitted with the product through Submit for review (F06-002); missing mandatory values block submission.
5. **How the approver sees pending items:** Reviewers see the values in the review workspace with changes since the last publication highlighted (F06-003).
6. **How the approver decides:** Reviewers approve or request changes, optionally commenting on specific attributes.
7. **How the maker sees history:** The maker sees reviewer comments next to the affected attribute and the attribute change history.
8. **How the approver / auditor sees history:** Auditors see each attribute value change (old/new) in the audit log.

### Functional Capabilities
- Runtime form rendering from template schema
- Unit-aware dimension inputs with live normalisation preview
- List, multi-select and yes/no inputs from permitted values
- Conditional show/mandatory logic evaluated client-side and server-side
- Missing mandatory summary with jump-to-field
- Re-apply template after template change (F03-003)

### UI Screens
- Dynamic dimensions panel rendered from template
- Additional attributes panel
- Missing mandatory attributes summary

### Logical API Operations
- Get product attribute form schema and values
- Save product attribute values
- Validate values against template rules
- Re-apply template to product after template change

### Inputs
- Attribute values per template: numeric dimensions, list selections, text, yes/no

### Outputs
- Typed attribute values with canonical numerics
- Validation results feeding completeness (F06-001)

### Business Rules
- Only attributes in the product category's published template can be saved
- Server re-validates all rules on save
- Values for attributes removed from the template are retained but hidden

### Validations
- Mandatory attributes present before submission
- Numeric values within attribute min/max
- List values in permitted values

### Calculations
- Canonical values via F03-004

### Workflow
Edited within product workflow (Module 06)

### Search Requirements
- None on this feature (values are searchable through Module 09)

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Create/edit products permission (not Content Administrator)

### Integrations
- None

### Dependencies
- F03-002
- F03-004
- F04-001
- F06-001

### Assumptions
- About 3–8 dimensions per category

### Risks
- Very large templates would slow entry; templates are kept focused

### Non Functional Requirements
- Panel renders under 500 ms; validation feedback instant

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Dynamic dimensions panel rendered from template | Very High | 16 |
| UI | Additional attributes panel | Complex | 12 |
| UI | Missing mandatory attributes summary | Easy | 4 |
| API | Get product attribute form schema and values | Medium | 6 |
| API | Save product attribute values | Complex | 8 |
| API | Validate values against template rules | Complex | 8 |
| API | Re-apply template to product after template change | Medium | 6 |
| Database | Typed product attribute value store | Complex | 6 |
| Database | Numeric range search indexes | Easy | 2 |
| Testing | Dimension sets for Crown, Casing, Baseboard and Half Round | Complex | 8 |
| Testing | Conditional mandatory and permitted values | Medium | 6 |
| Documentation | Dimension entry guide | Easy | 2 |

**Feature Total: 84 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 28 | 8 | 0 | 14 | 2 | **84** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Runtime dynamic form is a Very High UI
- Typed value storage with range indexes is a Complex DB item
- No external integration channel in this feature; Integration row omitted.
