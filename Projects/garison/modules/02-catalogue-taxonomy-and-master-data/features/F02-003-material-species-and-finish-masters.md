# F02-003 — Material, Species & Finish Masters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-003 |
| Feature Name | Material, Species & Finish Masters |
| Module | 02 — Catalogue Taxonomy & Master Data |
| Module Type | Business |
| Release | Go-live |

### Description
Maintain material/species values (for example Oak, Maple, Poplar, Pine, Cherry, MDF, Engineered) with material type, and finish values (for example Unfinished, Primed, Painted, Stained, Custom), with swatch images, display order and usage protection including merge of duplicates.

### Business Objective
Standardise material and finish terminology across products so that filters and product pages are consistent, especially during data normalisation of the initial population.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates material and finish values; initial values are seeded from discovery.
2. **How they create:** They add a material (name, type, description, swatch, order) or a finish (name, description, swatch, order).
3. **How they edit:** They edit values, reorder, retire unused values, or merge duplicates (for example 'Poplar' and 'Popular Wood') with automatic product reassignment.
4. **How they send for approval:** No review is required; masters take effect on save.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies; merge requires confirmation with impact count.
7. **How the maker sees history:** The administrator sees change history on the record.
8. **How the approver / auditor sees history:** Auditors see changes and merges in the audit log.

### Functional Capabilities
- Material master with type (Hardwood, Softwood, Engineered, MDF, Other)
- Finish master with swatch image
- Display order controlling chips on product pages and filter order
- Retire with usage check
- Merge duplicate values with product reassignment

### UI Screens
- Material / species register
- Material create / edit form
- Finish register
- Finish create / edit form with swatch upload
- Usage and merge dialog

### Logical API Operations
- List materials
- Create or update material
- List finishes
- Create or update finish with swatch
- Merge duplicate master values with product reassignment
- Check usage before retire

### Inputs
- Name, type (materials), description, swatch image, display order, status

### Outputs
- Material and finish masters used by products, filters and import validation

### Business Rules
- Names unique
- Merge reassigns all products and re-indexes affected published products
- Retired values cannot be newly assigned

### Validations
- Name mandatory
- Swatch JPG/PNG/WebP max 2 MB

### Calculations
- Usage counts per value

### Workflow
Active ↔ Retired; Merge (source value retired after reassignment)

### Search Requirements
- Name, type, status

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Manage masters permission

### Integrations
- None

### Dependencies
- F04-003
- F09-001
- F12-001

### Assumptions
- Finish availability is descriptive (no pricing or stock)

### Risks
- Inconsistent source terminology inflates master lists before normalisation

### Non Functional Requirements
- Master lookups cached

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Material / species register | Easy | 4 |
| UI | Material create / edit form | Easy | 4 |
| UI | Finish register | Easy | 4 |
| UI | Finish create / edit form with swatch upload | Easy | 4 |
| UI | Usage and merge dialog | Medium | 6 |
| API | List materials | Simple | 2 |
| API | Create or update material | Easy | 4 |
| API | List finishes | Simple | 2 |
| API | Create or update finish with swatch | Medium | 6 |
| API | Merge duplicate master values with product reassignment | Complex | 8 |
| API | Check usage before retire | Easy | 4 |
| Database | Material master | Simple | 1 |
| Database | Finish master with swatch reference | Simple | 1 |
| Database | Product-material and product-finish link indexes | Easy | 2 |
| Testing | Master maintenance, retire and merge | Easy | 4 |
| Testing | Display order on product pages and filters | Simple | 2 |
| Documentation | Material and finish master guide | Simple | 1 |

**Feature Total: 59 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 26 | 4 | 0 | 6 | 1 | **59** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Merge with re-index is the main complexity driver
- No external integration channel in this feature; Integration row omitted.
