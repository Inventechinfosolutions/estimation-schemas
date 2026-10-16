# F08-003 — Bidder Access to Draft Sale Deed

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F08-003 |
| Feature Name | Bidder Access to Draft Sale Deed |
| Module | 08 — Draft Sale Deed |
| Module Type | Business |
| Release | Go-live |

### Description
Publication of the approved draft sale deed to the bidder in the portal with status and approval date, download, acknowledgement, and an option to raise clarification requests on the draft.

### Business Objective
Let the bidder see and prepare for registration without visiting the office.

### Actors
- Successful Bidder
- Case Worker

### User Journey
1. **Who creates:** The system publishes the approved draft automatically.
2. **How they create:** The bidder opens the site, views and downloads the draft, and acknowledges.
3. **How they edit:** The bidder can raise a clarification request with comments.
4. **How they send for approval:** Clarifications go to the case worker.
5. **How the approver sees pending items:** The case worker sees clarification requests.
6. **How the approver decides:** The case worker responds or reopens the draft with DS approval.
7. **How the applicant / maker sees history:** The bidder sees responses.
8. **How the approver / auditor sees history:** Auditors see publication, downloads and clarifications.

### Functional Capabilities
- Publication on approval
- View / download with watermark
- Acknowledgement
- Clarification requests and responses

### UI Screens
- Draft deed view (bidder)
- Clarification request (bidder)
- Clarification response (staff)

### Logical API Operations
- Publish draft to bidder
- Download with watermark
- Acknowledge
- Raise / respond clarification

### Inputs
- Acknowledgement
- Clarification

### Outputs
- Published draft
- Responses

### Business Rules
- Only approved drafts visible

### Validations
- None

### Calculations
- None

### Workflow
Published → Acknowledged

### Search Requirements
- None

### Documents
- Approved draft deed

### Reports
- None

### Notifications
- Draft available notice

### Security
- Bidder sees own sites only

### Integrations
- None

### Dependencies
- F08-002
- F10-004

### Assumptions
- None

### Risks
- None significant

### Non Functional Requirements
- Standard

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Draft deed view (bidder) | Easy | 4 |
| UI | Clarification request (bidder) | Easy | 4 |
| UI | Clarification response (staff) | Easy | 4 |
| API | Publish draft to bidder | Easy | 4 |
| API | Download with watermark | Easy | 4 |
| API | Acknowledge | Simple | 2 |
| API | Raise / respond clarification | Easy | 4 |
| Database | Clarification store | Simple | 1 |
| Testing | Publication and clarification tests | Easy | 4 |
| Documentation | Bidder help for draft deed | Simple | 1 |

**Feature Total: 32 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 14 | 1 | 0 | 4 | 1 | **32** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Small
- No external integration channel in this feature; Integration row omitted.
