# F05-002 — Combination Record Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-002 |
| Feature Name | Combination Record Management |
| Module | 05 — Combinations & Product Relationships |
| Module Type | Business |
| Release | Go-live |

### Description
Manage combinations (multi-profile assemblies shown in the Garrison catalogue) as a separate catalogue entity: code, name, description, combination category/style, overall dimensions (overall height and projection), assembly image and drawing, documents, SEO and lifecycle identical to products.

### Business Objective
Represent combinations as structured, searchable entities with their own pages rather than free-text descriptions.

### Actors
- Catalogue Administrator
- Content Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates combinations.
2. **How they create:** From the Combination register they choose New combination, enter code, name, style and description, add overall dimensions, upload the assembly image and drawing, then add components (F05-003).
3. **How they edit:** They edit while Draft or Changes Requested; editing a Published combination creates a working draft.
4. **How they send for approval:** They submit the combination for review through F06-002 once completeness passes (minimum components, image, description).
5. **How the approver sees pending items:** Reviewers see combinations in the same review queue as products, filtered by type.
6. **How the approver decides:** Reviewers approve or request changes in F06-003.
7. **How the maker sees history:** The maker sees status, comments and history in the combination workspace.
8. **How the approver / auditor sees history:** Auditors see combination changes and decisions in the audit log.

### Functional Capabilities
- Combination register with filters (style, status, component product)
- Combination workspace (core, dimensions, media, components, documents, SEO)
- Overall dimensions with the same normalisation as products
- Assembly image and drawing management (reuses media manager)
- Preview using the public combination template
- Archive/restore with lifecycle identical to products

### UI Screens
- Combination register
- Combination create / edit form
- Combination media manager
- Combination preview

### Logical API Operations
- List combinations with filters
- Create combination draft
- Update combination
- Manage combination media
- Get combination workspace aggregate
- Archive or restore combination

### Inputs
- Code, name, style, description, overall height, overall projection, assembly image, drawing, documents

### Outputs
- Combination record for public combination pages and search

### Business Rules
- Combination codes unique across products and combinations
- Combinations follow the same workflow states as products
- A Published combination must have all components Published

### Validations
- Code and name mandatory
- Assembly image mandatory before submission
- At least two components before submission (F05-003)

### Calculations
- Overall dimensions normalised via F03-004

### Workflow
Draft → In Review → Approved → Published; Changes Requested → Draft; Archived

### Search Requirements
- Code, name, style, status, component code

### Documents
- Combination technical PDFs via F04-005

### Reports
- Combination list export

### Notifications
- Workflow notifications via F06-005

### Security
- Create/edit products permission applies to combinations

### Integrations
- None

### Dependencies
- F04-004
- F04-005
- F05-003
- F06-002
- F08-004

### Assumptions
- Combinations do not need their own category templates; they use a fixed attribute set

### Risks
- Garrison may want combination categories later; model allows adding them

### Non Functional Requirements
- Register under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Combination register | Medium | 6 |
| UI | Combination create / edit form | Complex | 12 |
| UI | Combination media manager | Medium | 6 |
| UI | Combination preview | Medium | 6 |
| API | List combinations with filters | Medium | 6 |
| API | Create combination draft | Complex | 8 |
| API | Update combination | Complex | 8 |
| API | Manage combination media | Medium | 6 |
| API | Get combination workspace aggregate | Medium | 6 |
| API | Archive or restore combination | Medium | 6 |
| Database | Combination entity with status and working-draft link | Medium | 4 |
| Database | Combination media links | Easy | 2 |
| Testing | Combination maintenance and lifecycle | Medium | 6 |
| Testing | Workflow parity with products | Medium | 6 |
| Documentation | Combination guide | Easy | 2 |

**Feature Total: 90 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 40 | 6 | 0 | 12 | 2 | **90** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses product media and workflow components, reducing UI effort
- No external integration channel in this feature; Integration row omitted.
