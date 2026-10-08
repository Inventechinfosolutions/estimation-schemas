# F03-002 — Category Attribute Templates

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Category Attribute Templates |
| Module | 03 — Dynamic Attribute & Dimension Framework |
| Module Type | Business |
| Release | Go-live |

### Description
Per-category template defining which attributes apply, in what order and group, which are mandatory or conditionally mandatory, which appear on product cards and detail pages, and which are filterable and searchable. For example Crown uses Projection, Height and Thickness; Half Round uses Diameter and Length.

### Business Objective
Make the product form, product page, completeness rules and filters adapt to each category, so Garrison can add a new category with its own dimension set without database redesign or code change.

### Actors
- Catalogue Administrator
- Super Administrator

### User Journey
1. **Who creates:** The Catalogue Administrator creates a template for each category; initial templates for Garrison categories are configured during discovery.
2. **How they create:** In the Template designer they add attributes from the library, set mandatory/conditional rules, order and groups, tick 'show on card', 'filterable' and 'searchable', and preview the resulting product form.
3. **How they edit:** They edit a template and publish a new template version; the impact on existing products is shown before publishing (F03-003).
4. **How they send for approval:** Templates have no editorial review; publishing a template version is a deliberate confirmed action by the Catalogue Administrator.
5. **How the approver sees pending items:** There is no approver inbox; templates with unpublished changes show a 'Draft changes' badge in the template register.
6. **How the approver decides:** No approval decision applies.
7. **How the maker sees history:** The administrator sees template version history with what changed.
8. **How the approver / auditor sees history:** Auditors see template versions and changes in the audit log.

### Functional Capabilities
- One template per category; sub-categories inherit or override
- Add/remove attributes from the library with display order and group
- Mandatory, optional and conditional mandatory (for example 'Spring Angle mandatory when Profile Shape = Sprung')
- Flags: show on product card, show on detail, filterable, searchable, include in import template
- Template preview rendering the product form
- Copy template from another category
- Template versioning with draft changes and publish

### UI Screens
- Template register by category
- Template designer
- Conditional rule builder
- Template preview (rendered product form)
- Copy template from another category dialog

### Logical API Operations
- Get template for category
- Save template draft configuration
- Validate template rules
- Copy template
- Render product form schema from template
- Publish template version

### Inputs
- Category, attribute selections, order, group, mandatory/conditional rules, display and search flags

### Outputs
- Published template version that drives product entry, completeness, detail display, filters, search indexing and import templates

### Business Rules
- Only one published template version per category at a time
- An attribute cannot be both hidden on detail and mandatory
- Conditional rules may reference only list or yes/no attributes in the same template
- Sub-category override replaces, not merges, the parent template

### Validations
- At least one attribute per template
- No circular conditional rules
- Filterable attributes must be numeric or list type

### Calculations
- None beyond rule evaluation

### Workflow
Template draft changes → Published version (with impact review in F03-003)

### Search Requirements
- Category name

### Documents
- None

### Reports
- Template matrix export (category × attribute)

### Notifications
- None

### Security
- Manage attributes and templates permission

### Integrations
- None

### Dependencies
- F02-001
- F03-001
- F03-003
- F04-002
- F06-001
- F09-003
- F12-001

### Assumptions
- Number of categories at go-live is about 15 with about 30 attributes in total

### Risks
- Overly complex conditional rules confuse data entry; guidance limits rules to one level

### Non Functional Requirements
- Form schema rendering under 300 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template register by category | Easy | 4 |
| UI | Template designer | Very High | 16 |
| UI | Conditional rule builder | Complex | 12 |
| UI | Template preview (rendered product form) | Medium | 6 |
| UI | Copy template from another category dialog | Easy | 4 |
| API | Get template for category | Medium | 6 |
| API | Save template draft configuration | Complex | 8 |
| API | Validate template rules | Medium | 6 |
| API | Copy template | Easy | 4 |
| API | Render product form schema from template | Complex | 8 |
| API | Publish template version | Complex | 8 |
| Database | Template header and versions | Medium | 4 |
| Database | Template attribute rules (order, flags, conditions) | Complex | 6 |
| Testing | Template-driven form rendering per category | Complex | 8 |
| Testing | Conditional mandatory logic | Medium | 6 |
| Testing | Template versioning and inheritance | Medium | 6 |
| Documentation | Template configuration guide with Crown and Half Round examples | Medium | 3 |

**Feature Total: 115 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 42 | 40 | 10 | 0 | 20 | 3 | **115** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Template designer is a dynamic configuration UI (Very High)
- Versioning and conditional rules drive Complex API and DB rows
- No external integration channel in this feature; Integration row omitted.
