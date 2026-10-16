# F03-002 — Portal Content & Study Material Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F03-002 |
| Feature Name | Portal Content & Study Material Management |
| Module | 03 — CLT Web Portal & Mobile Application |
| Module Type | Business |
| Release | Go-live |

### Description
Content management for portal pages, announcements, FAQs, notices and study material (PDF, video links) in Kannada and English, with draft, approval, scheduling and archive.

### Business Objective
Keep the portal up to date with test information as required in the maintenance scope.

### Actors
- Content Administrator
- KEONICS Approver

### User Journey
1. **Who creates:** The Content Administrator creates content.
2. **How they create:** The administrator writes bilingual content, attaches files and sets publish dates.
3. **How they edit:** The administrator edits drafts.
4. **How they send for approval:** Content is submitted for approval.
5. **How the approver sees pending items:** The KEONICS Approver sees pending content.
6. **How the approver decides:** The approver publishes or returns.
7. **How the applicant / maker sees history:** Visitors see published content.
8. **How the approver / auditor sees history:** Auditors see versions.

### Functional Capabilities
- Page, announcement, FAQ, notice and material types
- Bilingual editor
- File uploads with virus scan
- Scheduled publish / expiry
- Approval workflow
- Version history

### UI Screens
- Content list
- Bilingual content editor
- Study material upload
- Approval queue

### Logical API Operations
- Save content
- Upload material
- Approve / publish
- Scheduled publish job

### Inputs
- Content
- Files

### Outputs
- Published content

### Business Rules
- Publish needs approval

### Validations
- File types PDF / images

### Calculations
- None

### Workflow
Draft → Approved → Published → Archived

### Search Requirements
- Content

### Documents
- Study material

### Reports
- Content list

### Notifications
- Approval requests

### Security
- Malware scan

### Integrations
- None

### Dependencies
- F03-001

### Assumptions
- Study material provided

### Risks
- None

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Content list | Easy | 4 |
| UI | Bilingual content editor | Medium | 6 |
| UI | Study material upload | Easy | 4 |
| UI | Approval queue | Easy | 4 |
| API | Save content | Easy | 4 |
| API | Upload material | Easy | 4 |
| API | Approve / publish | Easy | 4 |
| API | Scheduled publish job | Easy | 4 |
| Database | Content and versions | Easy | 2 |
| Testing | Content workflow tests | Easy | 4 |
| Documentation | Content admin guide | Easy | 2 |

**Feature Total: 42 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 18 | 16 | 2 | 0 | 4 | 2 | **42** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Standard CMS
- No external integration channel in this feature; Integration row omitted.
