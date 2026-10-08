# F02-002 — Media Hosting & Delivery Setup

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-002 |
| Feature Name | Media Hosting & Delivery Setup |
| Module | 02 — Product Data Store on Existing Website |
| Module Type | Technical |
| Release | Go-live |

### Description
Place optimised product images in the website's media location or storage, configure cache headers and lazy loading, and confirm acceptable page weight on the existing hosting.

### Business Objective
Ensure product images load quickly without disrupting the existing site.

### Actors
- Delivery developer

### User Journey
1. **Who creates:** The delivery developer deploys images with each load.
2. **How they create:** Images are synced to the configured media path on staging and production.
3. **How they edit:** Re-syncs add, replace or remove images to match the dataset.
4. **How they send for approval:** No approval step applies to this feature; output is verified through the Garrison review workbook (F01-004) and UAT (F04-004).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees sync summaries.
8. **How the approver / auditor sees history:** The delivery lead checks page-weight results in testing.

### Functional Capabilities
- Media path and sync
- Cache headers
- Lazy loading support in templates

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Sync media to website storage
- Configure cache headers and lazy loading

### Inputs
- Optimised images

### Outputs
- Images served from the website

### Business Rules
- Image URLs are versioned so updates bypass stale caches

### Validations
- Every product image URL returns successfully after sync

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Sync summary

### Notifications
- None

### Security
- Media folder not writable from the web

### Integrations
- Existing hosting

### Dependencies
- F01-002
- F04-001

### Assumptions
- No separate CDN is required for about 350 small images

### Risks
- Limited disk space on current hosting

### Non Functional Requirements
- Images cached for at least 30 days

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Sync media to website storage | Easy | 4 |
| API | Configure cache headers and lazy loading | Easy | 4 |
| Integration | Existing hosting media storage configuration | Simple | 4 |
| Testing | Page weight and cache checks | Easy | 4 |
| Documentation | Media deployment note | Simple | 1 |

**Feature Total: 17 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 8 | 0 | 4 | 4 | 1 | **17** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Small configuration task; no database effort
