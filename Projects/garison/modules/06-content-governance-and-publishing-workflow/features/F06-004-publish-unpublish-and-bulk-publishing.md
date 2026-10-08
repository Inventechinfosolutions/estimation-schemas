# F06-004 — Publish, Unpublish & Bulk Publishing

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-004 |
| Feature Name | Publish, Unpublish & Bulk Publishing |
| Module | 06 — Content Governance & Publishing Workflow |
| Module Type | Business |
| Release | Go-live |

### Description
Publish approved products and combinations (individually or in bulk), creating the public snapshot and triggering search indexing, sitemap update, cache purge and URL activation; unpublish with reason; publication log.

### Business Objective
Control exactly when approved content goes live and make go-live of the initial population a single controlled action.

### Actors
- Catalogue Administrator
- Super Administrator

### User Journey
1. **Who creates:** Publishing is performed by users with publish permission on items already Approved.
2. **How they create:** They click Publish on an approved item, or select approved items in Bulk publish; the rights gate (F07-003) and completeness are re-checked and results shown.
3. **How they edit:** They unpublish a Published item with a reason (the item returns to Approved and is removed from the public catalogue with a temporary redirect).
4. **How they send for approval:** Publishing requires prior approval (F06-003); publish itself is a direct permission-controlled action.
5. **How the approver sees pending items:** Users with publish permission see items ready to publish in the Bulk publish screen (Approved filter).
6. **How the approver decides:** The publisher decides to publish or not; failed gate items are listed with reasons.
7. **How the maker sees history:** Makers see Published status and publication date on their items.
8. **How the approver / auditor sees history:** Auditors see publish/unpublish events with user, time and reason in the publication log and audit log.

### Functional Capabilities
- Publish single item with gate re-check
- Bulk publish with per-item results (supports 1,000+ items for population go-live)
- Public snapshot creation; working draft merged
- Side effects: search index update, sitemap regeneration, cache purge, redirect activation
- Unpublish with reason and redirect behaviour
- Publication log

### UI Screens
- Publish confirmation with gate results
- Bulk publish screen with results summary
- Unpublish dialog with reason
- Publication log

### Logical API Operations
- Publish item with snapshot and side effects
- Bulk publish items
- Unpublish item
- Get publication log

### Inputs
- Approved item(s)
- Unpublish reason

### Outputs
- Published public snapshot
- Index, sitemap and cache updates
- Publication log entries

### Business Rules
- Only Approved items can be published
- Rights gate and completeness re-checked at publish
- Unpublish keeps the URL returning a temporary redirect to the category page
- Publishing a combination requires all components Published

### Validations
- Unpublish reason mandatory

### Calculations
- None

### Workflow
Approved → Published; Published → Approved (unpublish); Published → Archived (F04-006)

### Search Requirements
- Publication log by user, date, item, action

### Documents
- None

### Reports
- Publication log export

### Notifications
- Maker notified on publication (F06-005)

### Security
- Publish permission (Super Administrator, Catalogue Administrator)

### Integrations
- Internal search, sitemap and cache services

### Dependencies
- F06-003
- F07-003
- F09-001
- F11-002
- F13-001

### Assumptions
- No scheduled (future-dated) publishing in this phase

### Risks
- Bulk publish of large batches must be resilient; implemented as a background job with progress

### Non Functional Requirements
- Single publish visible publicly within 1 minute; bulk publish of 1,000 items within 15 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Publish confirmation with gate results | Medium | 6 |
| UI | Bulk publish screen with results summary | Complex | 12 |
| UI | Unpublish dialog with reason | Easy | 4 |
| UI | Publication log | Medium | 6 |
| API | Publish item with snapshot and side effects | Very High | 16 |
| API | Bulk publish items | Very High | 16 |
| API | Unpublish item | Complex | 8 |
| API | Get publication log | Medium | 6 |
| Database | Publication snapshot and publication log | Medium | 4 |
| Integration | Search index, sitemap and cache purge triggers | Simple | 4 |
| Testing | Publish side effects (index, sitemap, cache, URL) | Complex | 8 |
| Testing | Bulk publish at population volume | Medium | 6 |
| Testing | Unpublish visibility and redirects | Easy | 4 |
| Documentation | Publishing guide | Easy | 2 |

**Feature Total: 102 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 46 | 4 | 4 | 18 | 2 | **102** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Publish orchestration with side effects is a Very High workflow API
- Bulk publish runs as a background job
