# F04-007 — Product Preview

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-007 |
| Feature Name | Product Preview |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Render a draft or working-draft product using the actual public product page template, with a draft banner, device toggle (desktop/tablet/mobile) and a time-limited preview link that reviewers can open without the product being published.

### Business Objective
Let makers and reviewers see exactly how a product will look publicly before it goes live.

### Actors
- Catalogue Administrator
- Content Administrator
- Catalogue Reviewer

### User Journey
1. **Who creates:** Makers open a preview from the product workspace; no record is created other than an optional preview link.
2. **How they create:** They click Preview to open the public template in a new tab with a 'Draft preview' banner and toggle device widths.
3. **How they edit:** Changes saved in the workspace are reflected on refresh.
4. **How they send for approval:** Preview has no approval step; it supports the review in F06-003.
5. **How the approver sees pending items:** There is no approver inbox; reviewers open the preview from the review workspace or a shared link.
6. **How the approver decides:** No decision applies on preview.
7. **How the maker sees history:** Makers see preview links they generated, with expiry.
8. **How the approver / auditor sees history:** Auditors see preview link generation in the audit log.

### Functional Capabilities
- Public template rendering of unpublished content
- Draft banner and noindex headers
- Device width toggle
- Time-limited preview link (default 7 days) restricted to authenticated administrators

### UI Screens
- Draft preview page using public template
- Device width toggle
- Preview link dialog

### Logical API Operations
- Render draft product preview
- Generate time-limited preview token
- Validate preview token

### Inputs
- Product (draft or working draft)
- Preview expiry

### Outputs
- Rendered preview page
- Preview link

### Business Rules
- Preview pages are never indexed by search engines
- Preview links require administrator authentication
- Third-party media failing the rights gate are shown with a watermark notice in preview

### Validations
- Token valid and unexpired

### Calculations
- Expiry date

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- None

### Notifications
- None

### Security
- noindex, authentication required, short-lived tokens

### Integrations
- None

### Dependencies
- F04-001
- F08-003
- F06-003

### Assumptions
- Combination preview reuses this capability (F05-002)

### Risks
- Template divergence between preview and live page; mitigated by reusing the same template

### Non Functional Requirements
- Preview renders within 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Draft preview page using public template | Complex | 12 |
| UI | Device width toggle | Easy | 4 |
| UI | Preview link dialog | Easy | 4 |
| API | Render draft product preview | Complex | 8 |
| API | Generate time-limited preview token | Medium | 6 |
| API | Validate preview token | Easy | 4 |
| Database | Preview token store | Simple | 1 |
| Testing | Preview fidelity against published page | Medium | 6 |
| Testing | Token expiry and access restriction | Easy | 4 |
| Documentation | Preview usage note | Simple | 1 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 18 | 1 | 0 | 10 | 1 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Reuses public template; main work is draft data binding
- No external integration channel in this feature; Integration row omitted.
