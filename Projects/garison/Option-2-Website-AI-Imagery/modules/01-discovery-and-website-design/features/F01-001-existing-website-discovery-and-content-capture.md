# F01-001 — Existing Website Discovery & Content Capture

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-001 |
| Feature Name | Existing Website Discovery & Content Capture |
| Module | 01 — Discovery & Website Design |
| Module Type | Business |
| Release | Go-live |

### Description
Review of the current Garrison website from its public pages, because neither source code nor admin logins are available. Every reachable page is crawled and recorded in a page inventory (URL, title, purpose, word count, images, forms, outbound links). Page text, images, logos, contact details and opening hours are captured into a content workbook. The current URLs are recorded for redirects. A kick-off workshop confirms Garrison's goals, audience, brand assets, required pages and the product sections to show.

### Business Objective
Rebuild the website without the original source code while keeping everything of value on the current site and preserving search rankings.

### Actors
- Delivery business analyst
- Delivery designer
- Garrison marketing/business owner

### User Journey
1. **Who creates:** The delivery business analyst performs discovery with the Garrison business owner.
2. **How they create:** They crawl the public site, build the page inventory and content workbook, and run the kick-off workshop.
3. **How they edit:** The inventory and workbook are updated after Garrison's comments and after any missing content is supplied.
4. **How they send for approval:** The discovery report is emailed to Garrison for confirmation.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's confirmation email freezes the page list and content scope for design.
7. **How the maker sees history:** Garrison sees the discovery report and content workbook versions.
8. **How the approver / auditor sees history:** The delivery lead keeps the workshop notes, inventory and confirmation email as the scope record.

### Functional Capabilities
- Public crawl of the current site (pages, images, documents, forms)
- Page inventory with URL, title, purpose and content notes
- Content workbook: text, images, contact details, opening hours, social links
- Current URL list for 301 redirects
- Brand asset collection (logo, colours, fonts, photos)
- Kick-off workshop and confirmed page list

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Crawl existing public website pages and assets
- Build page inventory and current URL map
- Capture page text and images into content workbook

### Inputs
- Public pages of www.garrisonindustries.ky
- Brand assets from Garrison
- Workshop input

### Outputs
- Page inventory
- Content workbook
- Current URL list
- Confirmed page list

### Business Rules
- Only public pages are read; no attempt is made to access admin areas
- Content Garrison wants retired is marked and not migrated
- Garrison supplies original high-resolution logos and photos where the site only has small versions

### Validations
- Every page in the inventory has an action: migrate, merge, rewrite or retire

### Calculations
- Page and asset counts for the content migration volume

### Workflow
Crawl → Inventory → Workshop → Garrison confirmation → Frozen scope

### Search Requirements
- None

### Documents
- Discovery report
- Content workbook

### Reports
- Page inventory

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- Current public website (read-only)

### Dependencies
- Garrison nominates a business owner for decisions

### Assumptions
- The current site has about 15 pages (confirmed in discovery; extra pages charged at the per-page rate)
- Automated fetches of the current site returned access errors during our review; browser-based capture is used where needed

### Risks
- Some content exists only in images or embedded widgets and must be retyped
- Brand assets may only exist at low resolution

### Non Functional Requirements
- Discovery completed within the first week

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Crawl existing public website pages and assets | Medium | 6 |
| API | Build page inventory and current URL map | Easy | 4 |
| API | Capture page text and images into content workbook | Medium | 6 |
| Database | Content inventory structure | Simple | 1 |
| Integration | Existing public website read-only access | Easy | 8 |
| Testing | Content capture completeness check against live site | Easy | 4 |
| Documentation | Discovery report and content inventory | Medium | 3 |
| Documentation | Kick-off workshop notes and confirmed page list | Easy | 2 |

**Feature Total: 34 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 16 | 1 | 8 | 4 | 5 | **34** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Crawl and capture scripted; workshop effort sits in the documentation rows
