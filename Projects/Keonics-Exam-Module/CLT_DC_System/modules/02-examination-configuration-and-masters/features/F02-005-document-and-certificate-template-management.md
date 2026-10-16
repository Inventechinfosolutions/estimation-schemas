# F02-005 — Document & Certificate Template Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-005 |
| Feature Name | Document & Certificate Template Management |
| Module | 02 — Examination Configuration & Masters |
| Module Type | Business |
| Release | Go-live |

### Description
Bilingual templates with merge fields for hall ticket (barcode, receipt details, no photo), score card, qualifying certificate (watermark, QR, signature block), rescheduling notices, attendance sheets and malpractice reports, with preview, versioning and approval.

### Business Objective
Let KEONICS control document wording and layout.

### Actors
- KEONICS Administrator
- Approving Authority

### User Journey
1. **Who creates:** The KEONICS Administrator creates templates.
2. **How they create:** The administrator edits Kannada and English text, inserts merge fields and layout elements, and saves a draft.
3. **How they edit:** The administrator previews with sample data.
4. **How they send for approval:** The draft is submitted for approval.
5. **How the approver sees pending items:** The Approving Authority sees preview and changes.
6. **How the approver decides:** The Approving Authority approves or returns.
7. **How the applicant / maker sees history:** Generated documents use the active template.
8. **How the approver / auditor sees history:** Auditors see template versions per document.

### Functional Capabilities
- Template types: hall ticket, score card, certificate, notices, attendance sheet, admission certificate, malpractice report
- Kannada Unicode rendering
- Barcode, QR and watermark placeholders
- Merge fields
- Preview and PDF
- Versioning and approval

### UI Screens
- Template list
- Bilingual template editor
- Preview
- Approval

### Logical API Operations
- Save template
- Render to PDF with barcode / QR / watermark
- Approve template
- Resolve active template

### Inputs
- Text
- Fields

### Outputs
- Approved templates

### Business Rules
- Only approved templates used

### Validations
- Mandatory placeholders

### Calculations
- None

### Workflow
Draft → Active → Superseded

### Search Requirements
- Templates

### Documents
- Templates

### Reports
- None

### Notifications
- Approval requests

### Security
- Admin only

### Integrations
- None

### Dependencies
- F05-004
- F11-004

### Assumptions
- Formats approved by KEONICS

### Risks
- Kannada rendering

### Non Functional Requirements
- PDF under 3 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template list | Easy | 4 |
| UI | Bilingual template editor | Complex | 12 |
| UI | Preview | Medium | 6 |
| UI | Approval | Easy | 4 |
| API | Save template | Medium | 6 |
| API | Render to PDF with barcode / QR / watermark | Complex | 8 |
| API | Approve template | Easy | 4 |
| API | Resolve active template | Easy | 4 |
| Database | Template store | Easy | 2 |
| Testing | Rendering tests with Kannada fonts | Complex | 8 |
| Documentation | Template guide | Easy | 2 |

**Feature Total: 60 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 22 | 2 | 0 | 8 | 2 | **60** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Renderer rated Complex
- No external integration channel in this feature; Integration row omitted.
