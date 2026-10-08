# F02-001 — Category & Sub-category Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-001 |
| Feature Name | Category & Sub-category Management |
| Module | 02 — Catalogue Taxonomy & Master Data |
| Module Type | Business |
| Release | Go-live |

### Description
Maintain the moulding category hierarchy (for example Casings, Back Bands, Plinth Blocks, Corner Blocks, Baseboards, Crown Moulds, Chair Rails, Door Stops, Panel Moulds, Quarter Rounds, Half Rounds, Brick Moulds, Window Stool, Tongue & Groove Paneling), with sub-categories, display order, image, introductory SEO text, linked attribute template and Active/Retired status.

### Business Objective
Give Garrison a configurable navigation and classification backbone that drives catalogue menus, listing pages, URLs, filters and the product form template.

### Actors
- Catalogue Administrator
- Super Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates categories and sub-categories; initial Garrison categories are seeded at go-live.
2. **How they create:** In the Category tree manager they add a category or child sub-category, enter name, slug, description, introductory text and image, and select the attribute template.
3. **How they edit:** They edit any field, drag to reorder, rename (the system creates a redirect for changed slugs), or retire or merge a category.
4. **How they send for approval:** Category changes do not go through review; they take effect on save because they are structural configuration.
5. **How the approver sees pending items:** There is no approver inbox for taxonomy changes.
6. **How the approver decides:** No approval decision applies; retire and merge require a confirmation that shows the impact.
7. **How the maker sees history:** The administrator sees the category's change history in the history panel.
8. **How the approver / auditor sees history:** Auditors see category creation, rename, reorder, retire and merge events in the audit log (F01-004).

### Functional Capabilities
- Two-level hierarchy (category → sub-category) with unlimited categories
- Drag-and-drop ordering controlling public menu and home tile order
- Category image, short description and SEO introductory text for listing pages
- Link to attribute template (F03-002); sub-categories inherit the parent template unless overridden
- Retire category (hidden publicly; products must be reassigned or archived first)
- Merge category into another with bulk product reassignment and redirect creation
- Usage summary: product count by status, combinations, collections
- Seed the initial Garrison category list

### UI Screens
- Category tree manager with drag-and-drop ordering
- Category create / edit form
- Sub-category form
- Retire / merge category dialog with impact summary
- Category usage summary panel

### Logical API Operations
- Get category tree
- Create category or sub-category
- Update category
- Reorder categories
- Retire category with usage check
- Merge category and reassign products
- Upload category image
- Seed initial Garrison categories

### Inputs
- Name, slug, parent, description, SEO introductory text, image, attribute template, display order, status

### Outputs
- Category hierarchy used by navigation, listings, product classification and templates
- Redirects for renamed/merged categories (F11-001)

### Business Rules
- Category names unique within the same parent
- A category with Published products cannot be retired until products are reassigned, archived or unpublished
- Merging moves all products and combinations and creates permanent redirects
- Maximum hierarchy depth is two levels

### Validations
- Name mandatory (max 80 characters)
- Slug lowercase, hyphenated, unique within parent
- Image type JPG/PNG/WebP, max 5 MB

### Calculations
- Product counts per category by status

### Workflow
Active ↔ Retired (structural configuration — no review workflow)

### Search Requirements
- Category name, status

### Documents
- None

### Reports
- Category usage summary

### Notifications
- None

### Security
- Manage categories permission (Super Administrator, Catalogue Administrator)

### Integrations
- None

### Dependencies
- F03-002 (template link)
- F11-001 (redirects)
- F09-001 (re-index on change)

### Assumptions
- Two-level hierarchy is sufficient for the Garrison range
- Combinations are handled as a separate entity (Module 05), not as a product category

### Risks
- Late taxonomy changes after population increase rework; taxonomy is confirmed at discovery

### Non Functional Requirements
- Tree loads instantly for up to 200 categories

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Category tree manager with drag-and-drop ordering | Complex | 12 |
| UI | Category create / edit form | Medium | 6 |
| UI | Sub-category form | Easy | 4 |
| UI | Retire / merge category dialog with impact summary | Medium | 6 |
| UI | Category usage summary panel | Easy | 4 |
| API | Get category tree | Easy | 4 |
| API | Create category or sub-category | Medium | 6 |
| API | Update category | Medium | 6 |
| API | Reorder categories | Medium | 6 |
| API | Retire category with usage check | Complex | 8 |
| API | Merge category and reassign products | Complex | 8 |
| API | Upload category image | Easy | 4 |
| API | Seed initial Garrison categories | Easy | 4 |
| Database | Category hierarchy with ordering and status | Medium | 4 |
| Database | Category SEO fields and image reference | Easy | 2 |
| Testing | Hierarchy, ordering, retire and merge rules | Medium | 6 |
| Testing | Effect of rename on listings, filters and URLs | Medium | 6 |
| Documentation | Taxonomy maintenance guide | Easy | 2 |

**Feature Total: 98 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 46 | 6 | 0 | 12 | 2 | **98** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Merge with bulk reassignment and redirect creation is the main complexity driver
- No external integration channel in this feature; Integration row omitted.
