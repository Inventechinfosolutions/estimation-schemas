# F04-005 — Technical Document Management

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F04-005 |
| Feature Name | Technical Document Management |
| Module | 04 — Product Profile Management |
| Module Type | Business |
| Release | Go-live |

### Description
Upload and maintain technical PDFs (specification sheets, installation guides) and supporting documents per product and combination, with title, document type, version, public/internal visibility and download tracking.

### Business Objective
Provide downloadable specifications for architects and contractors while keeping documents current through versioning.

### Actors
- Catalogue Administrator
- Content Administrator
- Visitor (download)

### User Journey
1. **Who creates:** The Catalogue Administrator or Content Administrator uploads documents to a product or combination.
2. **How they create:** In the Documents tab they upload a PDF, enter title and type, and choose Public or Internal.
3. **How they edit:** They replace a document with a new version (the previous version is retained in history) or withdraw it.
4. **How they send for approval:** Documents are submitted with the product through Submit for review; the template may make a technical PDF mandatory.
5. **How the approver sees pending items:** Reviewers see documents in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes.
7. **How the maker sees history:** The maker sees version history per document.
8. **How the approver / auditor sees history:** Auditors see upload, replace and withdraw events in the audit log.

### Functional Capabilities
- Upload PDF documents with title, type (Specification, Installation, Brochure, Other) and visibility
- Versioning with previous versions retained
- Withdraw document
- Public download links with download tracking (analytics in F11-004)
- Documents on combinations as well as products

### UI Screens
- Product documents panel
- Document upload form
- Document version history dialog

### Logical API Operations
- Upload document
- Update document metadata
- Replace document with new version
- List document versions
- Withdraw document
- Serve public document download with tracking

### Inputs
- PDF file, title, type, visibility

### Outputs
- Document records and public download links

### Business Rules
- Only the latest version is publicly downloadable
- Internal documents are never exposed publicly
- Withdrawn documents return 410 Gone on old links

### Validations
- PDF only, max 25 MB, content-sniffed
- Title mandatory

### Calculations
- Download counts

### Workflow
Edited within product workflow

### Search Requirements
- None

### Documents
- Technical PDFs, installation guides

### Reports
- Download counts in F11-004 dashboard

### Notifications
- None

### Security
- Manage documents permission; upload scanning (F13-002)

### Integrations
- Object storage (shared connector)

### Dependencies
- F04-001
- F05-002
- F13-001
- F13-002

### Assumptions
- CAD file downloads are a future enhancement

### Risks
- Outdated PDFs if Garrison does not maintain versions

### Non Functional Requirements
- Downloads served through CDN

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Product documents panel | Easy | 4 |
| UI | Document upload form | Easy | 4 |
| UI | Document version history dialog | Easy | 4 |
| API | Upload document | Medium | 6 |
| API | Update document metadata | Easy | 4 |
| API | Replace document with new version | Medium | 6 |
| API | List document versions | Easy | 4 |
| API | Withdraw document | Easy | 4 |
| API | Serve public document download with tracking | Medium | 6 |
| Database | Document and version store | Easy | 2 |
| Testing | Versioning and public/internal visibility | Easy | 4 |
| Testing | PDF validation and download | Easy | 4 |
| Documentation | Document management guide | Simple | 1 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 30 | 2 | 0 | 8 | 1 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Straightforward document handling with versions
- No external integration channel in this feature; Integration row omitted.
