# F04-006 — Product Duplicate, Archive & Restore

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-006 |
| Feature Name | Product Duplicate, Archive & Restore |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Duplicate an existing product as a template for a similar profile (choosing which sections to copy), archive retired products with an impact check on relationships, combinations and collections, and restore archived products to Draft.

### Business Objective
Speed up entry of similar profiles and retire products safely without broken links or orphaned combinations.

### Actors
- Catalogue Administrator
- Super Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator duplicates or archives products.
2. **How they create:** Duplicate: from a product they choose Duplicate, enter the new code and name, tick sections to copy (attributes, materials, finishes, lengths, relationships, documents; media optional), and a new Draft is created.
3. **How they edit:** Archive: they choose Archive, review the impact (relationships, combinations, collections), confirm with a reason; restore returns the product to Draft.
4. **How they send for approval:** Duplicated products follow the normal review workflow. Archiving a Published product is a direct action for users with publish permission, with no review.
5. **How the approver sees pending items:** There is no approver inbox for archive actions; archived products appear in the Archived register.
6. **How the approver decides:** No approval decision applies; the impact confirmation is the control.
7. **How the maker sees history:** The maker sees lineage (duplicated from) and lifecycle history on the product.
8. **How the approver / auditor sees history:** Auditors see duplicate, archive and restore events with reason in the audit log.

### Functional Capabilities
- Duplicate with section selection and new identity
- Lineage tracking (duplicated from)
- Archive impact analysis (relationships, combinations, collections, enquiries)
- Archive unpublishes, removes from search, keeps URL with redirect to category (F11-001)
- Archived products register
- Restore archived product to Draft

### UI Screens
- Duplicate product dialog with section selection
- Archive confirmation with impact summary
- Archived products register
- Restore confirmation

### Logical API Operations
- Duplicate product with selected sections
- Analyse archive impact
- Archive product
- Restore product to Draft
- List archived products

### Inputs
- New code and name, section selection (duplicate)
- Archive reason

### Outputs
- New Draft product
- Archived product with redirect
- Impact summary

### Business Rules
- Duplicate never copies status, provenance rights confirmation or SEO slug
- Archiving a product that is a mandatory component of a Published combination requires the combination to be updated or archived first
- Restore always returns to Draft

### Validations
- New code unique
- Archive reason mandatory

### Calculations
- Impact counts

### Workflow
Any → Archived → Draft (restore)

### Search Requirements
- Archived register by code, name, category, archived date

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- Duplicate: create product permission; Archive/restore: publish permission

### Integrations
- None

### Dependencies
- F04-001
- F05-001
- F05-003
- F11-001
- F09-001

### Assumptions
- Archived products are retained indefinitely

### Risks
- Duplicating media may inflate storage; media copy is optional

### Non Functional Requirements
- Duplicate completes under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Duplicate product dialog with section selection | Medium | 6 |
| UI | Archive confirmation with impact summary | Medium | 6 |
| UI | Archived products register | Easy | 4 |
| UI | Restore confirmation | Simple | 2 |
| API | Duplicate product with selected sections | Complex | 8 |
| API | Analyse archive impact | Complex | 8 |
| API | Archive product | Complex | 8 |
| API | Restore product to Draft | Medium | 6 |
| API | List archived products | Easy | 4 |
| Database | Archive metadata and duplication lineage | Easy | 2 |
| Testing | Duplicate copies selected sections correctly | Medium | 6 |
| Testing | Archive impact, search removal and redirect | Medium | 6 |
| Documentation | Product lifecycle actions guide | Simple | 1 |

**Feature Total: 67 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 34 | 2 | 0 | 12 | 1 | **67** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Impact analysis and multi-section copy drive Complex API rows
- No external integration channel in this feature; Integration row omitted.
