# F04-001 — Product Register & Core Profile

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-001 |
| Feature Name | Product Register & Core Profile |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Product register and core profile maintenance: product code, product name, category, sub-category, style, collections, short description, detailed description (rich text), featured flag and status, inside a product workspace that organises all product sections (dimensions, materials, media, documents, relationships, provenance, SEO) with a completeness meter.

### Business Objective
Give administrators one structured place to create and maintain each moulding profile, from product 001 to product 10,000, with no developer involvement.

### Actors
- Catalogue Administrator
- Content Administrator (content fields)
- Super Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates products; the Content Administrator can edit descriptions and content fields only.
2. **How they create:** They choose New product, select the category (which loads the template), enter product code and name, save as Draft, then complete the core profile in the product workspace.
3. **How they edit:** They edit any section from the workspace while the product is Draft or Changes Requested; editing a Published product creates a working draft while the published version stays live.
4. **How they send for approval:** They send the product for review using Submit for review (F06-002) once the completeness meter shows all mandatory items complete.
5. **How the approver sees pending items:** Reviewers see submitted products in the review queue (F06-002).
6. **How the approver decides:** Reviewers approve or request changes in F06-003.
7. **How the maker sees history:** The maker sees status, completeness, reviewer comments and the entity history panel in the workspace, and their own items in My submissions.
8. **How the approver / auditor sees history:** Reviewers and auditors see the full change and approval history through the history panel and audit log.

### Functional Capabilities
- Product register with filters: category, sub-category, style, collection, status, completeness band, source type (Garrison/External), featured, needs-update flag
- Saved register views and column chooser
- Two-step create: category and identity first, then workspace
- Core profile form with rich-text detailed description
- Product workspace with section tabs, completeness meter and status badge
- Working draft of Published products (published version stays live until republished)
- Change category with guided attribute remapping
- Product code uniqueness check as the user types

### UI Screens
- Product register with filters
- New product step: category and identity
- Core profile form
- Product workspace with section tabs and completeness meter
- Rich-text description editor
- Saved register views and column chooser

### Logical API Operations
- List and search products with filters and pagination
- Create product draft
- Update core profile
- Get product workspace aggregate
- Check product code uniqueness
- Save register view preferences
- Change product category with attribute remap
- Create working draft of published product

### Inputs
- Product code, product name, category, sub-category, style, collections, short description (max 300 characters), detailed description (rich text), featured flag

### Outputs
- Draft product record and workspace
- Working draft for published products
- Audit entries

### Business Rules
- Product code unique across products and combinations
- Status transitions only through Module 06 workflow
- Editing a Published product never changes the public page until republication
- Content Administrator cannot change code, category or dimensions

### Validations
- Code mandatory, pattern configurable (default letters, digits, hyphen; max 30)
- Name mandatory (max 120)
- Category mandatory and Active
- Short description mandatory before submission

### Calculations
- Completeness percentage displayed from F06-001

### Workflow
Draft → In Review → Approved → Published; Changes Requested → Draft; Published → Working draft → In Review → Republished; Archived (F04-006)

### Search Requirements
- Code (exact/prefix), name, category, style, collection, status, completeness, source type, updated by, updated date

### Documents
- Technical documents handled in F04-005

### Reports
- Product register export (CSV) of current filter

### Notifications
- Workflow notifications via F06-005

### Security
- Create/edit products permission; field-scope for Content Administrator

### Integrations
- None

### Dependencies
- F02-001
- F02-002
- F03-002
- F06-001
- F06-002
- F01-004

### Assumptions
- Single language (English)

### Risks
- Working-draft model increases complexity but is essential for safe edits to live pages

### Non Functional Requirements
- Register under 2 seconds for 10,000 products
- Workspace autosave every 60 seconds for drafts

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Product register with filters | Complex | 12 |
| UI | New product step: category and identity | Medium | 6 |
| UI | Core profile form | Complex | 12 |
| UI | Product workspace with section tabs and completeness meter | Very High | 16 |
| UI | Rich-text description editor | Medium | 6 |
| UI | Saved register views and column chooser | Easy | 4 |
| API | List and search products with filters and pagination | Medium | 6 |
| API | Create product draft | Complex | 8 |
| API | Update core profile | Complex | 8 |
| API | Get product workspace aggregate | Medium | 6 |
| API | Check product code uniqueness | Simple | 2 |
| API | Save register view preferences | Easy | 4 |
| API | Change product category with attribute remap | Complex | 8 |
| API | Create working draft of published product | Complex | 8 |
| Database | Product core entity with status and working-draft link | Medium | 4 |
| Database | Product classification links (style, collections) | Easy | 2 |
| Database | Register filter indexes | Easy | 2 |
| Testing | Create and edit core profile | Medium | 6 |
| Testing | Working draft of published product | Medium | 6 |
| Testing | Category change remapping | Medium | 6 |
| Testing | Register filters and pagination at 10,000 products | Medium | 6 |
| Documentation | Product creation guide | Medium | 3 |

**Feature Total: 141 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 56 | 50 | 8 | 0 | 24 | 3 | **141** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Workspace is a multi-section tabbed UI (Very High)
- Working-draft model drives Complex API rows
- No external integration channel in this feature; Integration row omitted.
