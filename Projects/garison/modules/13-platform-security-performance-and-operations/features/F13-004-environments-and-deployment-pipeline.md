# F13-004 — Environments & Deployment Pipeline

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F13-004 |
| Feature Name | Environments & Deployment Pipeline |
| Module | 13 — Platform Security, Performance & Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Development, staging and production environments; automated build, test and deployment pipeline; database migrations and seed data automation; configuration and secrets management; production go-live, rollback procedure and deployment documentation.

### Business Objective
Release the catalogue reliably and let future changes be deployed safely.

### Actors
- Delivery team
- Garrison IT / hosting contact

### User Journey
1. **Who creates:** Environments and the pipeline are created by the delivery team with Garrison's hosting contact.
2. **How they create:** The team provisions environments, configures the pipeline and deploys builds to staging for Garrison review.
3. **How they edit:** Pipeline and environment changes are made through version-controlled configuration.
4. **How they send for approval:** Production deployment requires Garrison's go-live approval (project checkpoint).
5. **How the approver sees pending items:** No in-system approver inbox.
6. **How the approver decides:** Garrison approves go-live outside the system.
7. **How the maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Deployment history is retained in the pipeline tool.

### Functional Capabilities
- Dev, staging and production environments
- CI pipeline: build, unit tests, static checks
- CD pipeline: staged deployment with approval gate and rollback
- Database migrations and seed automation (categories, attributes, templates, roles)
- Configuration and secrets management
- Go-live checklist and hypercare handover

### UI Screens
- None (no user interface artefacts in this feature)

### Logical API Operations
- None (no application operations in this feature)

### Inputs
- Hosting access, domain and certificates, secrets

### Outputs
- Running environments, repeatable deployments

### Business Rules
- No manual changes in production outside the pipeline
- Production deploys only from approved release tags

### Validations
- Smoke tests pass before traffic switch

### Calculations
- None

### Workflow
Commit → Build → Test → Staging → Approval → Production

### Search Requirements
- None

### Documents
- Deployment and maintenance documentation

### Reports
- Release notes

### Notifications
- Deployment notifications to the delivery team

### Security
- Secrets stored in a managed vault, not in code

### Integrations
- Hosting provider and source control/CI service

### Dependencies
- Garrison hosting access
- F13-003

### Assumptions
- Hosting is provided by Garrison or procured separately; hosting charges excluded

### Risks
- Late hosting access delays staging; requested in Week 1

### Non Functional Requirements
- Deployment with under 5 minutes of downtime, ideally zero

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| Database | Database migration scripts and seed automation | Medium | 4 |
| Integration | Build and deployment pipeline | Medium | 16 |
| Integration | Environment provisioning for development, staging and production | Medium | 16 |
| Testing | Deployment smoke tests | Easy | 4 |
| Testing | Production readiness checklist verification | Easy | 4 |
| Documentation | Deployment documentation | Complex | 4 |
| Documentation | Maintenance documentation | Medium | 3 |

**Feature Total: 51 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 4 | 32 | 8 | 7 | **51** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Infrastructure work represented as Integration rows; no UI or API artefacts
