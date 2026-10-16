# F06-001 — Question Paper Guidelines & Blueprint

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-001 |
| Feature Name | Question Paper Guidelines & Blueprint |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Maintenance of question paper guidelines (types, style, language, application-ability and 20% role-play / simulation share, difficulty definitions) and the blueprint (count per topic × difficulty × type), with Technical Committee approval and authoring targets derived for SMEs.

### Business Objective
Ensure the bank is built to an approved design before authoring starts.

### Actors
- Question Bank Administrator
- Technical Committee Member

### User Journey
1. **Who creates:** The Question Bank Administrator drafts guidelines and blueprint.
2. **How they create:** The administrator enters guidelines text and blueprint matrix; targets are computed.
3. **How they edit:** The administrator edits drafts.
4. **How they send for approval:** Drafts go to the Technical Committee.
5. **How the approver sees pending items:** Committee members see drafts.
6. **How the approver decides:** The committee approves (with minutes reference) or returns.
7. **How the applicant / maker sees history:** SMEs see approved guidelines and their targets.
8. **How the approver / auditor sees history:** Auditors see versions and approvals.

### Functional Capabilities
- Guidelines document with versions
- Blueprint matrix topic × difficulty × type
- Application and simulation share checks
- Authoring targets per SME
- Technical Committee approval
- Gap view: blueprint vs approved items

### UI Screens
- Guidelines editor
- Blueprint matrix
- Committee approval
- Blueprint gap view

### Logical API Operations
- Save guidelines
- Save blueprint
- Compute targets and gaps
- Committee decision

### Inputs
- Guidelines
- Blueprint counts

### Outputs
- Approved blueprint
- Targets

### Business Rules
- At least 2,000 items at launch; 5% annual growth
- 20% simulation / role-play items

### Validations
- Blueprint totals

### Calculations
- Gap = blueprint − approved

### Workflow
Draft → Approved

### Search Requirements
- Versions

### Documents
- Guidelines PDF

### Reports
- Gap report

### Notifications
- Approval requests

### Security
- Question bank roles only

### Integrations
- None

### Dependencies
- F02-001

### Assumptions
- Technical Committee formed by KEONICS

### Risks
- Committee availability

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Guidelines editor | Medium | 6 |
| UI | Blueprint matrix | Complex | 12 |
| UI | Committee approval | Easy | 4 |
| UI | Blueprint gap view | Medium | 6 |
| API | Save guidelines | Easy | 4 |
| API | Save blueprint | Medium | 6 |
| API | Compute targets and gaps | Medium | 6 |
| API | Committee decision | Easy | 4 |
| Database | Guidelines and blueprint | Easy | 2 |
| Testing | Blueprint tests | Medium | 6 |
| Documentation | Question bank governance note | Easy | 2 |

**Feature Total: 58 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 20 | 2 | 0 | 6 | 2 | **58** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard
- No external integration channel in this feature; Integration row omitted.
