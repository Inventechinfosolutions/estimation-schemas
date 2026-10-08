# F04-004 — Migration Reconciliation & Go-live

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-004 |
| Feature Name | Migration Reconciliation & Go-live |
| Module | 04 — Website Integration, SEO & Go-live |
| Module Type | Shared |
| Release | Go-live |

### Description
Reconciliation report comparing approved dataset counts per category with published pages (missing images, broken links, filter coverage), UAT support and defect fixes, production deployment with backup and rollback, post-go-live checks and handover.

### Business Objective
Prove that every approved product is live and correct, and launch without disrupting the existing website.

### Actors
- Delivery developer
- Delivery lead
- Garrison catalogue owner

### User Journey
1. **Who creates:** The delivery developer produces the reconciliation report and deploys.
2. **How they create:** They run the report on staging, support Garrison UAT, fix defects, then deploy to production.
3. **How they edit:** Defects found in UAT are fixed and the report is re-run.
4. **How they send for approval:** Garrison approves go-live after UAT by email.
5. **How the approver sees pending items:** No in-system inbox; UAT defects tracked in a shared list.
6. **How the approver decides:** Garrison's UAT sign-off email is the go-live decision.
7. **How the maker sees history:** Garrison receives the reconciliation report and handover document.
8. **How the approver / auditor sees history:** The delivery lead keeps reconciliation, UAT and deployment records.

### Functional Capabilities
- Reconciliation report
- UAT support and defect fixing
- Production deployment with rollback
- Post-go-live checks
- Handover document

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Generate reconciliation report
- Deploy to production with rollback

### Inputs
- Frozen dataset, staging site, UAT feedback

### Outputs
- Live catalogue
- Reconciliation report
- Handover document

### Business Rules
- Go-live only after UAT sign-off
- Rollback plan rehearsed on staging

### Validations
- Zero unexplained gaps in reconciliation

### Calculations
- Counts per category: approved versus published

### Workflow
Staging verified → UAT → Sign-off → Production → Post-go-live checks

### Search Requirements
- None

### Documents
- Reconciliation report, handover document

### Reports
- Reconciliation report

### Notifications
- None

### Security
- Deployment credentials handled securely

### Integrations
- Existing hosting

### Dependencies
- All features

### Assumptions
- Two UAT rounds

### Risks
- Production hosting constraints discovered late; staging mirrors production

### Non Functional Requirements
- Downtime under 15 minutes during deployment

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Generate reconciliation report | Complex | 8 |
| API | Deploy to production with rollback | Medium | 6 |
| Testing | UAT support and defect fixing | Complex | 8 |
| Testing | Post-go-live link and page checks | Easy | 4 |
| Documentation | Go-live and handover document | Medium | 3 |

**Feature Total: 29 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 14 | 0 | 0 | 12 | 3 | **29** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- UAT support estimated Complex given two rounds
- No external integration channel in this feature; Integration row omitted.
