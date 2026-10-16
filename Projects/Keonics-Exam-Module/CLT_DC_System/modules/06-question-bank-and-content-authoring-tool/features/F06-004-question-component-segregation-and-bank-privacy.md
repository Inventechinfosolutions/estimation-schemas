# F06-004 — Question Component Segregation & Bank Privacy

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F06-004 |
| Feature Name | Question Component Segregation & Bank Privacy |
| Module | 06 — Question Bank & Content Authoring Tool |
| Module Type | Business |
| Release | Go-live |

### Description
Component-level access policies so that reviewers, committee and administrators see only permitted components (for example stem and options without key, or key without stem), with encrypted storage of components, watermarked screens with user ID, copy / print / screenshot deterrents and full access logging.

### Business Objective
Meet the RFP confidentiality requirement for the question bank.

### Actors
- Question Bank Administrator
- All question bank roles
- Auditor

### User Journey
1. **Who creates:** The administrator configures component visibility per role.
2. **How they create:** The administrator sets policies; policies need second approval.
3. **How they edit:** Policies are versioned.
4. **How they send for approval:** Activation by a second administrator.
5. **How the approver sees pending items:** Approver sees pending policies.
6. **How the approver decides:** Approver activates.
7. **How the applicant / maker sees history:** Users see only permitted components with watermark.
8. **How the approver / auditor sees history:** Auditors see every component access.

### Functional Capabilities
- Component visibility policy per role
- Separate encryption of answer keys
- Screen watermark with user and time
- Copy, print and right-click blocking
- Access log per component view
- Bulk export prohibited

### UI Screens
- Component policy editor
- Access log viewer

### Logical API Operations
- Evaluate component visibility
- Encrypt / decrypt components with separate keys
- Log component access
- Policy activation

### Inputs
- Policies

### Outputs
- Segregated views

### Business Rules
- Only author sees all components
- No bulk export of items

### Validations
- Policy completeness

### Calculations
- None

### Workflow
Draft → Active

### Search Requirements
- Access logs

### Documents
- None

### Reports
- Component access report

### Notifications
- Unusual access alerts

### Security
- Separate key for answer keys via HSM

### Integrations
- HSM via F15-005

### Dependencies
- F06-002
- F16-001
- F15-005

### Assumptions
- None

### Risks
- Screenshots by phone cannot be technically prevented

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Component policy editor | Medium | 6 |
| UI | Access log viewer | Medium | 6 |
| API | Evaluate component visibility | Complex | 8 |
| API | Encrypt / decrypt components with separate keys | Complex | 8 |
| API | Log component access | Easy | 4 |
| API | Policy activation | Easy | 4 |
| Database | Policy and access logs | Easy | 2 |
| Testing | Segregation and leakage tests | Complex | 8 |
| Documentation | Question bank security note | Easy | 2 |

**Feature Total: 48 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 24 | 2 | 0 | 8 | 2 | **48** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Policy engine rated Complex
- No external integration channel in this feature; Integration row omitted.
