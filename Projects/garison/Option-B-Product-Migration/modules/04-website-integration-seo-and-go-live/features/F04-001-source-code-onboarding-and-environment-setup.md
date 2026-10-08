# F04-001 — Source Code Onboarding & Environment Setup

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-001 |
| Feature Name | Source Code Onboarding & Environment Setup |
| Module | 04 — Website Integration, SEO & Go-live |
| Module Type | Shared |
| Release | Go-live |

### Description
Obtain the existing website source code and server/database access, assess the technology stack, set up local and staging environments that replicate the live site, take a full backup of the live site, and confirm the deployment method.

### Business Objective
Change the existing website safely, with a tested path back if anything goes wrong.

### Actors
- Delivery developer
- Garrison website/hosting contact

### User Journey
1. **Who creates:** The delivery developer performs onboarding with Garrison's hosting contact.
2. **How they create:** They receive code and access, set up local and staging copies, and write a short technical assessment.
3. **How they edit:** Environment changes are made by the developer as needed.
4. **How they send for approval:** Garrison approves the technical assessment and access arrangements by email.
5. **How the approver sees pending items:** No in-system inbox.
6. **How the approver decides:** Garrison's approval email is the decision.
7. **How the maker sees history:** Garrison receives the technical assessment note.
8. **How the approver / auditor sees history:** The delivery lead keeps the assessment and backup records.

### Functional Capabilities
- Code and access onboarding
- Stack assessment
- Local and staging environments
- Live backup and restore test
- Deployment method confirmation

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- None (no application operations in this feature)

### Inputs
- Source code, server, database and DNS access

### Outputs
- Working staging site
- Backup
- Assessment note

### Business Rules
- No changes on production before staging sign-off
- Full backup before any production deployment

### Validations
- Staging matches production for existing pages

### Calculations
- None

### Workflow
Access → Assessment → Staging → Ready

### Search Requirements
- None

### Documents
- Technical assessment note

### Reports
- None

### Notifications
- None

### Security
- Credentials stored securely and returned at handover

### Integrations
- Existing hosting server

### Dependencies
- Garrison provides code and access

### Assumptions
- Source code is complete and matches the live site
- Site runs on a self-hosted server (observed hosting on a cloud virtual server)

### Risks
- Code missing or out of sync with live site; re-estimation or Option A
- Existing SSL certificate did not validate from our review; Garrison to resolve

### Non Functional Requirements
- Staging accessible only to the project team and Garrison

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| Database | Live database backup and staging copy | Easy | 2 |
| Integration | Source code onboarding and stack assessment | Medium | 16 |
| Integration | Local and staging environments replicating the live site | Medium | 16 |
| Testing | Staging parity smoke test | Easy | 4 |
| Documentation | Technical assessment note | Medium | 3 |

**Feature Total: 41 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 2 | 32 | 4 | 3 | **41** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Infrastructure work represented as Integration rows; no UI or API artefacts
