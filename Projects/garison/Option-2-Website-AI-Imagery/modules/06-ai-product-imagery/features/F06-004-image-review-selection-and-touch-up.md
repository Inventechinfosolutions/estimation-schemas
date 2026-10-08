# F06-004 — Image Review, Selection & Touch-up

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-004 |
| Feature Name | Image Review, Selection & Touch-up |
| Module | 06 — AI Product Imagery |
| Module Type | Technical |
| Release | Go-live |

### Description
Internal review gallery showing each product's candidates beside its silhouette and reference, with approve, reject and regenerate (with prompt note) actions, light retouching of the chosen image, progress tracking, and export of the approved set. Garrison reviews the approved images in the review workbook (F04-004).

### Business Objective
Make sure only accurate, on-brand images are published.

### Actors
- Delivery imagery specialist
- Garrison catalogue owner (final review)

### User Journey
1. **Who creates:** The delivery imagery specialist reviews candidates.
2. **How they create:** They compare candidates with the silhouette and approve one per product or request regeneration.
3. **How they edit:** Approved images can be retouched or replaced before Garrison's review.
4. **How they send for approval:** The approved set is added to the review workbook for Garrison.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's workbook sign-off approves the images with the product data.
7. **How the maker sees history:** The specialist sees review history per product.
8. **How the approver / auditor sees history:** The delivery lead keeps the review decisions and Garrison sign-off.

### Functional Capabilities
- Side-by-side review gallery
- Approve / reject / regenerate with note
- Light retouching
- Progress dashboard
- Approved set export

### UI Screens
- Review gallery with candidates beside silhouette
- Approve / reject / regenerate controls
- Review progress dashboard

### Logical API Operations
- Record review decisions
- Queue regeneration with revised prompt
- Export approved image set

### Inputs
- Candidates
- Silhouettes

### Outputs
- One approved image per product

### Business Rules
- Images that misrepresent the profile are rejected
- No product is published without an approved image or a marked placeholder

### Validations
- Exactly one approved image per product

### Calculations
- Approval rate and regeneration count

### Workflow
Candidates → Reviewed → Approved | Regenerate

### Search Requirements
- None

### Documents
- None

### Reports
- Review progress

### Notifications
- None

### Security
- Internal tool on restricted staging access

### Integrations
- None

### Dependencies
- F06-003
- F04-004

### Assumptions
- Per-product review time is the separate volume line (0.2 h per product)

### Risks
- Low first-pass approval increases AI cost and review time

### Non Functional Requirements
- Gallery loads 50 products per page smoothly

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Review gallery with candidates beside silhouette | Complex | 12 |
| UI | Approve / reject / regenerate controls | Medium | 6 |
| UI | Review progress dashboard | Easy | 4 |
| API | Record review decisions | Easy | 4 |
| API | Queue regeneration with revised prompt | Medium | 6 |
| API | Export approved image set | Easy | 4 |
| Database | Review decision store | Simple | 1 |
| Testing | Review flow tests | Easy | 4 |
| Documentation | Reviewer guide | Simple | 1 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 22 | 14 | 1 | 0 | 4 | 1 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Internal tool; per-product review labour is a volume line
- No external integration channel in this feature; Integration row omitted.
