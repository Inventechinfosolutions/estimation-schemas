# F02-005 — Existing Content Migration

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-005 |
| Feature Name | Existing Content Migration |
| Module | 02 — Website Build |
| Module Type | Business |
| Release | Go-live |

### Description
Move the content Garrison keeps from the current site into the new templates: clean up text, optimise and rename images, place content into content files, and check each migrated page against the original. Per-page effort is charged as a volume line.

### Business Objective
Carry over all useful existing content so nothing is lost in the redesign.

### Actors
- Delivery developer
- Garrison business owner (review)

### User Journey
1. **Who creates:** The delivery developer migrates content; Garrison reviews it on staging.
2. **How they create:** Content from the workbook (F01-001) is transformed into content files and images are optimised.
3. **How they edit:** Corrections from Garrison's review are applied to the content files.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** There is no approver inbox.
6. **How the approver decides:** No approval decision applies on this feature.
7. **How the maker sees history:** The developer sees the migration log per page.
8. **How the approver / auditor sees history:** The delivery lead checks the migration log against the page inventory.

### Functional Capabilities
- Text clean-up and formatting
- Image optimisation and renaming
- Content file population
- Per-page comparison with original
- Migration log

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Transform captured content into page content files
- Optimise and rename migrated images

### Inputs
- Content workbook (F01-001)

### Outputs
- Populated company pages
- Migration log

### Business Rules
- Only pages marked migrate or merge are moved
- No new copywriting; minor edits only

### Validations
- Every migrated page has a title, meta description and at least one heading

### Calculations
- Per-page volume: pages × rate

### Workflow
Captured → Transformed → Reviewed → Done

### Search Requirements
- None

### Documents
- None

### Reports
- Migration log

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- F01-001
- F02-003

### Assumptions
- About 15 pages at 1.5 hours each (volume line)

### Risks
- Pages needing new copy are outside this feature; Garrison provides the text

### Non Functional Requirements
- Migrated images under 200 KB each

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Transform captured content into page content files | Medium | 6 |
| API | Optimise and rename migrated images | Easy | 4 |
| Testing | Migrated page review against current site | Easy | 4 |
| Documentation | Content migration log | Simple | 1 |

**Feature Total: 15 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 10 | 0 | 0 | 4 | 1 | **15** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Tooling here; per-page labour is the separate volume line
- No external integration channel in this feature; Integration row omitted.
