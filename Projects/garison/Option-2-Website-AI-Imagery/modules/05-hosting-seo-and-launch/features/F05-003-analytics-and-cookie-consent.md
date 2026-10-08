# F05-003 — Analytics & Cookie Consent

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-003 |
| Feature Name | Analytics & Cookie Consent |
| Module | 05 — Hosting, SEO & Launch |
| Module Type | Shared |
| Release | Go-live |

### Description
Web analytics with key events (product view, filter use, search, enquiry submitted) and a cookie consent banner that loads analytics only after consent.

### Business Objective
Show Garrison which products and pages generate interest and enquiries.

### Actors
- Visitor
- Garrison business owner (reads reports in the analytics tool)

### User Journey
1. **Who creates:** Analytics events are configured by the delivery developer.
2. **How they create:** Visitors accept or decline cookies; events are recorded only after consent.
3. **How they edit:** Event changes are made by a developer.
4. **How they send for approval:** No in-system approval applies; output is verified through the Garrison review workbook (F04-004) and user acceptance testing (F05-005).
5. **How the approver sees pending items:** Not applicable for visitors; there is no approver inbox.
6. **How the approver decides:** No approval decision applies on public pages.
7. **How the maker sees history:** Not applicable for visitors.
8. **How the approver / auditor sees history:** Garrison sees reports in its own analytics account.

### Functional Capabilities
- Cookie consent banner
- Analytics page views and key events
- Consent-aware loading

### UI Screens
- Cookie consent banner

### Logical API Operations
- Track key events (product view, search, enquiry)

### Inputs
- Visitor consent choice

### Outputs
- Analytics data in Garrison's account

### Business Rules
- No analytics cookies before consent

### Validations
- Events fire once per action

### Calculations
- None

### Workflow
Not applicable

### Search Requirements
- None

### Documents
- None

### Reports
- Analytics tool standard reports

### Notifications
- None

### Security
- No personal data sent in events

### Integrations
- Web analytics service

### Dependencies
- F02-001

### Assumptions
- Garrison owns the analytics account

### Risks
- None significant

### Non Functional Requirements
- Consent banner does not block page rendering

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Cookie consent banner | Easy | 4 |
| API | Track key events (product view, search, enquiry) | Easy | 4 |
| Integration | Web analytics service (for example GA4) | Simple | 4 |
| Testing | Consent and event tracking checks | Easy | 4 |
| Documentation | Analytics event list | Simple | 1 |

**Feature Total: 17 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 4 | 0 | 4 | 4 | 1 | **17** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Standard analytics set-up
