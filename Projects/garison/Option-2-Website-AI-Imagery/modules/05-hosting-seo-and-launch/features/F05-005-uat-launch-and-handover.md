# F05-005 — UAT, Launch & Handover

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F05-005 |
| Feature Name | UAT, Launch & Handover |
| Module | 05 — Hosting, SEO & Launch |
| Module Type | Shared |
| Release | Go-live |

### Description
Migration reconciliation report (approved products per category versus published pages, missing images, broken links), user acceptance testing support with defect fixes, production release with rollback, post-launch checks, handover document and a recorded walkthrough of how content and product updates are requested and made.

### Business Objective
Prove every approved product and page is live and correct, and launch smoothly.

### Actors
- Delivery developer
- Delivery lead
- Garrison business owner

### User Journey
1. **Who creates:** The delivery lead runs user acceptance testing with Garrison.
2. **How they create:** The reconciliation report is produced on staging; Garrison tests the site; defects are fixed.
3. **How they edit:** Defects found in testing are fixed and the report is re-run.
4. **How they send for approval:** Garrison approves go-live by email after testing.
5. **How the approver sees pending items:** There is no in-system inbox; the delivery lead tracks the review round and open comments in a shared list.
6. **How the approver decides:** Garrison's sign-off email is the go-live decision.
7. **How the maker sees history:** Garrison receives the reconciliation report and handover document.
8. **How the approver / auditor sees history:** The delivery lead keeps reconciliation, testing and release records.

### Functional Capabilities
- Reconciliation report
- User acceptance testing support and fixes
- Production release with rollback
- Post-launch checks
- Handover document and walkthrough recording

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- Generate migration reconciliation report
- Production release with rollback

### Inputs
- Frozen dataset
- Staging site
- Testing feedback

### Outputs
- Live website
- Reconciliation report
- Handover document

### Business Rules
- Go-live only after Garrison sign-off
- Rollback rehearsed on staging

### Validations
- Zero unexplained gaps in reconciliation

### Calculations
- Approved versus published counts per category

### Workflow
Staging verified → Testing → Sign-off → Production → Post-launch checks

### Search Requirements
- None

### Documents
- Reconciliation report, handover document

### Reports
- Reconciliation report

### Notifications
- None

### Security
- Site-wide controls apply: HTTPS, escaped inputs, no admin login surface

### Integrations
- None

### Dependencies
- All features

### Assumptions
- Two testing rounds
- 30-day post-launch defect warranty

### Risks
- Late content from Garrison delays launch

### Non Functional Requirements
- Launch with no email disruption

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Generate migration reconciliation report | Complex | 8 |
| API | Production release with rollback | Easy | 4 |
| Testing | User acceptance testing support and defect fixing (two rounds) | Complex | 8 |
| Testing | Post-launch checks | Easy | 4 |
| Documentation | Handover document and update guide | Medium | 3 |
| Documentation | Walkthrough recording for Garrison | Simple | 1 |

**Feature Total: 28 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 12 | 0 | 0 | 12 | 4 | **28** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Testing support sized Complex for two rounds
- No external integration channel in this feature; Integration row omitted.
