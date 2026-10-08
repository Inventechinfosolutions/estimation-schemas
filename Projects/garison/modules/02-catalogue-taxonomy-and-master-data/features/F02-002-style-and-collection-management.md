# F02-002 — Style & Collection Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Style & Collection Management |
| Module | 02 — Catalogue Taxonomy & Master Data |
| Module Type | Business |
| Release | Go-live |

### Description
Maintain styles (for example Classic, Traditional, Modern, Transitional, Colonial) and collections (for example Heritage) as a classification layer independent of category and material. Collections can be curated with an ordered product list and hero image for collection pages.

### Business Objective
Support discovery-oriented browsing by design intent and keep style data separate from category and material so that filters stay accurate.

### Actors
- Catalogue Administrator
- Content Administrator (collection content)

### User Journey
1. **Who creates:** The Catalogue Administrator creates styles and collections.
2. **How they create:** They add a style (name, slug, description, order) or a collection (name, slug, description, hero image, curated products).
3. **How they edit:** They edit, reorder, and add or remove curated products; they retire styles or collections no longer used.
4. **How they send for approval:** No review is required; style and collection configuration takes effect on save. Curated products appear publicly only if they are Published.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies.
7. **How the maker sees history:** The administrator sees change history on the record.
8. **How the approver / auditor sees history:** Auditors see changes in the audit log.

### Functional Capabilities
- Style master with order and description
- Collection master with hero image, description and SEO text
- Curated product list per collection with manual ordering
- Retire with usage check; products keep the value hidden until reassigned
- Products can belong to one style and many collections

### UI Screens
- Style register
- Style create / edit form
- Collection register
- Collection form with hero image and curated product picker
- Retire style / collection dialog

### Logical API Operations
- List styles
- Create or update style
- List collections
- Create or update collection
- Curate collection products (add, remove, reorder)
- Retire style or collection with usage check

### Inputs
- Style: name, slug, description, order
- Collection: name, slug, description, hero image, SEO text, curated product list

### Outputs
- Style and collection masters used by product classification, listings and filters

### Business Rules
- Style and collection names unique
- Unpublished curated products are hidden publicly
- Retired values cannot be newly assigned

### Validations
- Name mandatory
- Slug unique
- Hero image JPG/PNG/WebP max 5 MB

### Calculations
- Product counts per style and collection

### Workflow
Active ↔ Retired

### Search Requirements
- Name, status

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Manage taxonomy permission; Content Administrator may edit collection content fields only

### Integrations
- None

### Dependencies
- F04-001
- F08-002
- F09-003

### Assumptions
- A product has at most one style

### Risks
- Garrison may want multiple styles per product; the model supports changing to multi-select with minor effort

### Non Functional Requirements
- Collection pages cacheable

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Style register | Easy | 4 |
| UI | Style create / edit form | Easy | 4 |
| UI | Collection register | Easy | 4 |
| UI | Collection form with hero image and curated product picker | Medium | 6 |
| UI | Retire style / collection dialog | Simple | 2 |
| API | List styles | Simple | 2 |
| API | Create or update style | Easy | 4 |
| API | List collections | Simple | 2 |
| API | Create or update collection | Medium | 6 |
| API | Curate collection products (add, remove, reorder) | Medium | 6 |
| API | Retire style or collection with usage check | Medium | 6 |
| Database | Style master | Simple | 1 |
| Database | Collection master with curated product list | Easy | 2 |
| Testing | Independent classification and filtering | Easy | 4 |
| Testing | Curated collection ordering and visibility rules | Easy | 4 |
| Documentation | Style and collection guide | Simple | 1 |

**Feature Total: 58 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 26 | 3 | 0 | 8 | 1 | **58** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Curated ordering adds a product picker interaction
- No external integration channel in this feature; Integration row omitted.
