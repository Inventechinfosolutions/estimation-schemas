# F03-001 — Public Information Portal

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-001 |
| Feature Name | Public Information Portal |
| Module | 03 — CLT Web Portal & Mobile Application |
| Module Type | Business |
| Release | Go-live |

### Description
Public portal at clt.karnataka.gov.in with home, about CLT, eligibility, syllabus, test pattern, schedules and seat availability summary, registration centres and test centre addresses with map and contact persons, FAQs, published helpdesk numbers, announcements, and entry points to registration, booking, mock test and certificate verification.

### Business Objective
Give candidates and departments complete public information and a single entry point.

### Actors
- Public
- Candidate

### User Journey
1. **Who creates:** Content is published by the Content Administrator (F03-002).
2. **How they create:** Visitors browse pages; no creation by the public.
3. **How they edit:** Not applicable.
4. **How they send for approval:** Not applicable.
5. **How the approver sees pending items:** Not applicable.
6. **How the approver decides:** Not applicable.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Page analytics available to administrators.

### Functional Capabilities
- Home with announcements
- Syllabus and pattern pages from F02-001
- Schedule and availability summary
- Centre directory with map and contacts
- FAQs and helpdesk numbers
- Links to registration, mock test, verification
- Search
- Visitor analytics

### UI Screens
- Home page
- About, eligibility and syllabus pages
- Schedule and availability page
- Centre directory with map
- FAQ and contact page
- Announcements page

### Logical API Operations
- Public content API
- Schedule summary API
- Centre directory API
- Site search

### Inputs
- None

### Outputs
- Public pages

### Business Rules
- Only published content visible

### Validations
- None

### Calculations
- Availability summary

### Workflow
Not applicable

### Search Requirements
- Site search

### Documents
- None

### Reports
- Visitor analytics

### Notifications
- None

### Security
- Public read-only; WAF

### Integrations
- Map tiles

### Dependencies
- F03-002
- F02-001
- F02-002

### Assumptions
- Domain clt.karnataka.gov.in provided

### Risks
- Traffic spikes at booking open

### Non Functional Requirements
- Pages under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Home page | Medium | 6 |
| UI | About, eligibility and syllabus pages | Easy | 4 |
| UI | Schedule and availability page | Medium | 6 |
| UI | Centre directory with map | Medium | 6 |
| UI | FAQ and contact page | Easy | 4 |
| UI | Announcements page | Easy | 4 |
| API | Public content API | Easy | 4 |
| API | Schedule summary API | Medium | 6 |
| API | Centre directory API | Easy | 4 |
| API | Site search | Easy | 4 |
| Database | Public content cache | Simple | 1 |
| Testing | Portal content and load tests | Medium | 6 |
| Documentation | Portal page inventory | Simple | 1 |

**Feature Total: 56 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 30 | 18 | 1 | 0 | 6 | 1 | **56** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Public pages
- No external integration channel in this feature; Integration row omitted.
