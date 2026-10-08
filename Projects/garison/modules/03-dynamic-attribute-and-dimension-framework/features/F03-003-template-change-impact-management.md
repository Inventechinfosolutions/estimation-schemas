# F03-003 — Template Change Impact Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-003 |
| Feature Name | Template Change Impact Management |
| Module | 03 — Dynamic Attribute & Dimension Framework |
| Module Type | Business |
| Release | Go-live |

### Description
When a template version is about to be published, analyse which existing products are affected (new mandatory attributes, removed attributes, changed permitted values), present an impact report, optionally apply default values, and place affected products on a re-validation worklist without taking published products offline.

### Business Objective
Allow Garrison to evolve templates safely after the catalogue is populated, without breaking published pages or silently creating incomplete records.

### Actors
- Catalogue Administrator

### User Journey
1. **Who creates:** The impact analysis is triggered by the Catalogue Administrator when publishing a template version (F03-002).
2. **How they create:** The system shows counts and lists of affected products by status, and the administrator can bulk-apply a default value for a new mandatory attribute.
3. **How they edit:** After publishing, the administrator opens the re-validation worklist and edits each flagged product (or bulk-sets values) until it passes completeness.
4. **How they send for approval:** No separate approval is needed for the template change; products edited from the worklist follow the normal review workflow (Module 06) before republication.
5. **How the approver sees pending items:** There is no approver inbox for impact items; reviewers see edited products in the standard review queue.
6. **How the approver decides:** No decision applies on this feature; reviewers decide on the edited products in F06-003.
7. **How the maker sees history:** The administrator sees each product's re-validation flag and resolution date.
8. **How the approver / auditor sees history:** Auditors see the template change, impact snapshot and bulk default application in the audit log.

### Functional Capabilities
- Impact analysis before template publish
- Impact report with product list, status and missing attributes
- Bulk apply default value to affected products
- Re-validation worklist with filters and progress
- Published products remain published and are flagged 'Needs update' until fixed

### UI Screens
- Template change impact report
- Re-validation worklist
- Bulk set default value dialog

### Logical API Operations
- Analyse template change impact
- Queue affected products for re-validation
- Apply default value to affected products
- Get re-validation worklist

### Inputs
- Draft template version
- Default value selections

### Outputs
- Impact snapshot
- Re-validation flags on products
- Bulk updated attribute values

### Business Rules
- Published products are never automatically unpublished by template changes
- Removed attributes are hidden from display but their values are retained for 90 days
- Bulk default application is audited per product

### Validations
- Default value must satisfy attribute type and permitted values

### Calculations
- Affected product counts by status and attribute

### Workflow
Template draft → Impact review → Publish → Re-validation worklist → Product edits → Review → Republish

### Search Requirements
- Worklist filter by category, status, missing attribute

### Documents
- None

### Reports
- Impact report export

### Notifications
- Optional email to Catalogue Administrators summarising flagged products

### Security
- Manage templates permission

### Integrations
- None

### Dependencies
- F03-002
- F04-002
- F06-001

### Assumptions
- Template changes after go-live are infrequent

### Risks
- Large worklists after major template changes; bulk default mitigates

### Non Functional Requirements
- Impact analysis completes within 10 seconds for 10,000 products

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template change impact report | Complex | 12 |
| UI | Re-validation worklist | Medium | 6 |
| UI | Bulk set default value dialog | Medium | 6 |
| API | Analyse template change impact | Complex | 8 |
| API | Queue affected products for re-validation | Complex | 8 |
| API | Apply default value to affected products | Complex | 8 |
| API | Get re-validation worklist | Medium | 6 |
| Database | Template change and impact log | Easy | 2 |
| Database | Product re-validation flags | Easy | 2 |
| Testing | Impact detection for added, removed and changed attributes | Medium | 6 |
| Testing | Published product protection and flagging | Medium | 6 |
| Documentation | Template change procedure | Easy | 2 |

**Feature Total: 72 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 24 | 30 | 4 | 0 | 12 | 2 | **72** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Bulk operations over many products drive Complex API rows
- No external integration channel in this feature; Integration row omitted.
