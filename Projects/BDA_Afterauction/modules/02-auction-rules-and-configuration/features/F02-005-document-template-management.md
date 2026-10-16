# F02-005 — Document Template Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-005 |
| Feature Name | Document Template Management |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Bilingual (Kannada and English), versioned templates with merge fields for intimation letters, draft proceedings, rejection / unsold intimations, demand notices, reminders, show-cause and cancellation notices, extension orders, draft sale deeds and completion records, with approval before use.

### Business Objective
Let BDA control the wording of every official document without code changes and ensure only approved templates are used.

### Actors
- Auction Admin
- Approving Authority (template approval)
- Case Worker (uses templates)

### User Journey
1. **Who creates:** The Auction Admin creates and maintains templates.
2. **How they create:** The Auction Admin opens Templates, selects a document type, uploads or edits the Kannada and English text in the editor, inserts merge fields from the field picker, and saves a draft.
3. **How they edit:** The Auction Admin edits the draft and previews it with a sample case in both languages.
4. **How they send for approval:** The Auction Admin submits the template version for approval.
5. **How the approver sees pending items:** The Approving Authority sees pending templates with preview and change comparison.
6. **How the approver decides:** The Approving Authority approves (version becomes active) or returns with remarks.
7. **How the applicant / maker sees history:** Users generating documents see only active templates; the Auction Admin sees all versions.
8. **How the approver / auditor sees history:** Auditors see which template version produced each generated document.

### Functional Capabilities
- Template types per Appendix C of the SOW
- Rich text editor with Kannada Unicode fonts, tables, header / footer, BDA emblem and QR code placeholder
- Merge field catalogue (site, bidder, auction, amounts, dates, officer, DS office) with amounts in words in both languages
- Conditional blocks (e.g., EMD adjustment paragraph)
- Preview with sample case and PDF output
- Versioning, comparison and approval
- Signature placeholders for DSC

### UI Screens
- Template list by document type
- Bilingual template editor with merge fields
- Template preview with sample case
- Version comparison
- Template approval

### Logical API Operations
- Save template draft
- Merge field catalogue
- Render template to PDF with data
- Compare versions
- Approve / return template
- Resolve active template for type and language
- Amount and date in words (Kannada / English)

### Inputs
- Template text in Kannada and English
- Merge fields
- Conditional rules
- Approval remarks

### Outputs
- Approved template versions
- Preview PDFs

### Business Rules
- Only approved templates can be used for generation
- Each generated document records the template version
- Both language versions must be approved together

### Validations
- Merge fields exist in catalogue
- Mandatory placeholders present (signature, QR)

### Calculations
- Amount in words in Indian numbering (lakh, crore) in both languages

### Workflow
Draft → Submitted → Active → Superseded

### Search Requirements
- Templates by type, language, status

### Documents
- Templates themselves

### Reports
- Template usage by version

### Notifications
- Approval request and outcome

### Security
- Only Auction Admin edits; generated PDFs are tamper-evident through signatures

### Integrations
- None

### Dependencies
- Used by F04-004, F04-005, F05-003, F06-001, F06-007, F06-008, F08-001, F09-003

### Assumptions
- BDA supplies approved wording for each document

### Risks
- Kannada font rendering in PDF; validated in prototype phase

### Non Functional Requirements
- Document generation under 5 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Template list by document type | Easy | 4 |
| UI | Bilingual template editor with merge fields | Complex | 12 |
| UI | Template preview with sample case | Medium | 6 |
| UI | Version comparison | Medium | 6 |
| UI | Template approval | Easy | 4 |
| API | Save template draft | Medium | 6 |
| API | Merge field catalogue | Easy | 4 |
| API | Render template to PDF with data | Complex | 8 |
| API | Compare versions | Medium | 6 |
| API | Approve / return template | Easy | 4 |
| API | Resolve active template for type and language | Easy | 4 |
| API | Amount and date in words (Kannada / English) | Medium | 6 |
| Database | Template and version store | Medium | 4 |
| Testing | Rendering tests with Kannada fonts and conditional blocks | Complex | 8 |
| Testing | Template versioning and approval tests | Easy | 4 |
| Documentation | Template authoring guide with merge field list | Medium | 3 |

**Feature Total: 89 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 32 | 38 | 4 | 0 | 12 | 3 | **89** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- PDF rendering engine with Kannada support rated Complex
- No external integration channel in this feature; Integration row omitted.
