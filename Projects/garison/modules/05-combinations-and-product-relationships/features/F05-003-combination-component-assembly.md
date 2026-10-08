# F05-003 — Combination Component Assembly

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-003 |
| Feature Name | Combination Component Assembly |
| Module | 05 — Combinations & Product Relationships |
| Module Type | Business |
| Release | Go-live |

### Description
Link component profiles to a combination with role/position (for example Crown, Back band, Casing, Baseboard, Cap), order and quantity, validate the assembly, and expose the reverse 'Used in combinations' lookup for product pages.

### Business Objective
Let customers see exactly which profiles form a combination and navigate to each component's product page.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator assembles components within a combination they created or maintain.
2. **How they create:** In the Components tab they add products through the component picker, assign a role/position, set order and optional quantity.
3. **How they edit:** They edit roles and order or remove components while the combination is editable.
4. **How they send for approval:** The assembly is submitted with the combination through Submit for review; validation must pass first.
5. **How the approver sees pending items:** Reviewers see the component list in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes.
7. **How the maker sees history:** The maker sees component changes in combination history.
8. **How the approver / auditor sees history:** Auditors see component changes in the audit log.

### Functional Capabilities
- Component picker filtered by category
- Component role master (Crown, Back band, Casing, Baseboard, Cap, Panel mould, Other)
- Order and quantity per component
- Assembly validation (minimum two components, no duplicates of same role and product, components not Archived)
- Reverse lookup 'Used in combinations' for products

### UI Screens
- Component assembly editor
- Component picker filtered by category
- Assembly validation summary

### Logical API Operations
- Add component to combination
- Update component role, order and quantity
- Remove component
- Validate assembly
- Get combinations using a product

### Inputs
- Component products, role, order, quantity

### Outputs
- Component list on combination page
- 'Used in combinations' list on product page

### Business Rules
- Minimum two components
- Combination cannot be published while any component is unpublished
- Archiving a component triggers the impact check in F04-006

### Validations
- Component product exists and not Archived
- Role mandatory

### Calculations
- None

### Workflow
Edited within combination workflow

### Search Requirements
- Picker search by code, name, category

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Create/edit products permission

### Integrations
- None

### Dependencies
- F05-002
- F04-006
- F08-003
- F08-004

### Assumptions
- Visual hotspot mapping of components on the assembly image is handled in F08-004 using component order

### Risks
- Combinations referencing external products with unconfirmed rights cannot publish

### Non Functional Requirements
- Reverse lookup cached on publish

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Component assembly editor | Complex | 12 |
| UI | Component picker filtered by category | Medium | 6 |
| UI | Assembly validation summary | Easy | 4 |
| API | Add component to combination | Medium | 6 |
| API | Update component role, order and quantity | Easy | 4 |
| API | Remove component | Easy | 4 |
| API | Validate assembly | Complex | 8 |
| API | Get combinations using a product | Medium | 6 |
| Database | Combination component link with role, order and quantity | Easy | 2 |
| Database | Component role master | Simple | 1 |
| Testing | Assembly rules and unpublished component handling | Medium | 6 |
| Testing | Reverse 'Used in combinations' lookup | Easy | 4 |
| Documentation | Combination assembly guide | Simple | 1 |

**Feature Total: 64 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 28 | 3 | 0 | 10 | 1 | **64** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Validation across component statuses is the main complexity driver
- No external integration channel in this feature; Integration row omitted.
