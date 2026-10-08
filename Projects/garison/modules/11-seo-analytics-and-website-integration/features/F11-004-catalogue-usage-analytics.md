# F11-004 — Catalogue Usage Analytics

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F11-004 |
| Feature Name | Catalogue Usage Analytics |
| Module | 11 — SEO, Analytics & Website Integration |
| Module Type | Shared |
| Release | Go-live |

### Description
Analytics event layer for catalogue interactions (search with term and result count, filter use, product and combination views, drawing zoom, document downloads, enquiry starts and submissions) sent to Garrison's web analytics property with consent; plus an in-portal catalogue insight dashboard of top products, top and zero-result searches and enquiries by category from platform data.

### Business Objective
Show Garrison how customers use the catalogue and where content gaps are (for example frequent zero-result searches).

### Actors
- Super Administrator
- Catalogue Administrator
- Visitor (tracked anonymously with consent)

### User Journey
1. **Who creates:** Analytics events are created automatically by the system as visitors interact (subject to consent); administrators configure the analytics settings.
2. **How they create:** The Super Administrator enters the analytics measurement ID and consent mode in Analytics settings.
3. **How they edit:** Settings can be changed at any time.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** Catalogue Administrators view the insight dashboard.
8. **How the approver / auditor sees history:** Auditors see analytics setting changes in the audit log.

### Functional Capabilities
- Event dictionary and data layer
- Consent-aware loading of analytics
- Search term, zero-result and filter events
- Product/combination view, drawing zoom, download and enquiry events
- Insight dashboard from platform data (top viewed, top searched, zero-result terms, enquiries by category, downloads)
- Daily aggregation job

### UI Screens
- Analytics settings
- Catalogue insight dashboard

### Logical API Operations
- Publish analytics events through data layer
- Get insight dashboard aggregates
- Aggregate daily usage statistics

### Inputs
- Visitor interactions (anonymous)
- Measurement ID, consent settings

### Outputs
- Analytics events
- Insight dashboard

### Business Rules
- No analytics before consent where consent is required
- No personal data sent to analytics

### Validations
- Measurement ID format

### Calculations
- Daily counts and rankings over selectable periods (7/30/90 days)

### Workflow
Not applicable

### Search Requirements
- Dashboard period and category filters

### Documents
- None

### Reports
- Catalogue insight dashboard

### Notifications
- None

### Security
- Dashboard restricted to administrators

### Integrations
- Web analytics (for example Google Analytics 4, Garrison property)

### Dependencies
- F09-002
- F08-003
- F10-001
- F04-005
- F08-005

### Assumptions
- Garrison provides the analytics property

### Risks
- Consent rejection reduces analytics coverage; platform-side dashboard still works

### Non Functional Requirements
- Event code adds no noticeable page delay (async)

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Analytics settings | Easy | 4 |
| UI | Catalogue insight dashboard | Very High | 16 |
| API | Publish analytics events through data layer | Complex | 8 |
| API | Get insight dashboard aggregates | Medium | 6 |
| API | Aggregate daily usage statistics | Medium | 6 |
| Database | Daily usage aggregates | Easy | 2 |
| Integration | Web analytics tag and event integration | Easy | 8 |
| Testing | Event firing verification | Medium | 6 |
| Testing | Dashboard figure reconciliation | Easy | 4 |
| Documentation | Analytics event dictionary | Easy | 2 |

**Feature Total: 62 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 20 | 20 | 2 | 8 | 10 | 2 | **62** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Insight dashboard is Very High UI
- Analytics integration estimated as Easy (REST/tag)
