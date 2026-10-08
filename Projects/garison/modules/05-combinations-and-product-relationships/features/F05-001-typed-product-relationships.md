# F05-001 — Typed Product Relationships

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-001 |
| Feature Name | Typed Product Relationships |
| Module | 05 — Combinations & Product Relationships |
| Module Type | Business |
| Release | Go-live |

### Description
Define typed relationships between profiles: Related product, Matching casing, Matching crown, Matching baseboard, Alternative profile and Similar product, with optional automatic reciprocal links, ordering, and a relationship type master.

### Business Objective
Help customers assemble coordinated room trim and find substitutes, and increase cross-discovery across the catalogue.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates relationships from a product workspace.
2. **How they create:** In the Relationships tab they choose a relationship type, search and pick target products in the picker, and choose whether to create the reciprocal link.
3. **How they edit:** They reorder relationships within each type or remove them (reciprocal removed too, if created together).
4. **How they send for approval:** Relationships are submitted with the product through Submit for review.
5. **How the approver sees pending items:** Reviewers see relationships in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes.
7. **How the maker sees history:** The maker sees relationship changes in product history.
8. **How the approver / auditor sees history:** Auditors see relationship add/remove events in the audit log.

### Functional Capabilities
- Relationship types master (name, reciprocal type, public label, order)
- Product picker with search by code/name and filters by category/style
- Automatic reciprocal creation (for example Matching casing ↔ Matching casing; Alternative ↔ Alternative)
- Ordering within type
- Self-link and duplicate prevention
- Public display only of Published related products

### UI Screens
- Relationships panel grouped by type
- Product picker dialog with search and filters
- Relationship type master
- Reciprocal relationship confirmation

### Logical API Operations
- Search products for picker
- Add relationship with reciprocal
- Remove relationship and reciprocal
- Reorder relationships
- Get product relationships for admin and public
- Maintain relationship types

### Inputs
- Source product, relationship type, target products, reciprocal flag, order

### Outputs
- Typed relationships used on product detail pages (F08-003)

### Business Rules
- A product cannot relate to itself
- The same pair cannot have the same type twice
- Reciprocal links are removed together only when they were created together
- Only Published targets display publicly

### Validations
- Target product exists and is not Archived

### Calculations
- None

### Workflow
Edited within product workflow

### Search Requirements
- Picker search by code, name, category, style

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
- F04-001
- F08-003

### Assumptions
- Relationships are curated manually (no automatic recommendations)

### Risks
- Relationship maintenance effort grows with catalogue size; import supports relationships (F12-001)

### Non Functional Requirements
- Picker results under 500 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Relationships panel grouped by type | Complex | 12 |
| UI | Product picker dialog with search and filters | Medium | 6 |
| UI | Relationship type master | Easy | 4 |
| UI | Reciprocal relationship confirmation | Simple | 2 |
| API | Search products for picker | Medium | 6 |
| API | Add relationship with reciprocal | Complex | 8 |
| API | Remove relationship and reciprocal | Medium | 6 |
| API | Reorder relationships | Easy | 4 |
| API | Get product relationships for admin and public | Medium | 6 |
| API | Maintain relationship types | Easy | 4 |
| Database | Product relationship with type, order and reciprocal link | Medium | 4 |
| Database | Relationship type master | Simple | 1 |
| Testing | Reciprocity, self-link and duplicate prevention | Medium | 6 |
| Testing | Unpublished related products hidden publicly | Easy | 4 |
| Documentation | Relationship guide | Simple | 1 |

**Feature Total: 74 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 34 | 5 | 0 | 10 | 1 | **74** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reciprocity handling drives the Complex API row
- No external integration channel in this feature; Integration row omitted.
