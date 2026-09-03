# F03-002 — Searchable PDF/A Package

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Searchable PDF/A Package |
| **Module** | 03 — Scanning and Searchable PDF/A Production |

### Description
Store one searchable PDF/A (ISO 19005-1:2005) per unique file ID, with English and/or Kannada search as on the pages, suitable for page-by-page viewing and 1:1 print after compression.

### Business Objective
The digital file is the replica used in e-Office.

### Actors
Maker: Operator / scan software output registered by Operator. Approver: none.

### User Journey
1. Who creates: Operator attaches or generates the PDF/A against the unique ID.
2. How they create: Digital file register → select ID → store PDF/A → confirm searchable flag and language(s) present.
3. How they edit: Replace package only if QC/rescan requires; history of versions kept simply (current + replaced).
4. How they send for approval: Does not apply (QC is Module 04).
5. How the approver sees pending items: No inbox here.
6. How the approver decides: No decision here.
7. How the maker sees history: Package versions on the file.
8. How the auditor sees history: Department Officer opens the current package.

### Functional Capabilities
- Store PDF/A per file
- Record English/Kannada searchability
- Open/download for QC and Department view on site
- Block complete status without a package

### UI Screens
| Screen | Complexity |
|---|---|
| Digital file register | Medium |
| PDF/A package detail | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Store PDF/A package | Complex |
| Validate PDF/A present | Medium |
| Open or download package | Easy |

### Inputs
Unique ID, PDF/A file, language flags.

### Outputs
Stored package linked to ID.

### Business Rules
- One current package per ID.
- Must be PDF/A as required by IFQ.
- Multipage file should be stored so pages can be viewed without waiting for the entire file (production practice; tool stores the file the scanners produce).

### Validations
- File attached; unique ID exists.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
By unique ID.

### Documents
The PDF/A is the document.

### Reports
None.

### Notifications
None.

### Security
Site access only; confidentiality.

### Integrations
None (upload is F06-001).

### Dependencies
F03-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- OCR/searchable PDF creation uses Service Provider scan/QC tools; this feature is assembly, storage and validation recording, not building a new OCR engine.

### Risks
Huge files slow the site LAN.

### Non Functional Requirements
Open a page reasonably on Department PCs.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Digital file register | UI | Medium | 6 |
| PDF/A package detail | UI | Easy | 4 |
| Store PDF/A package | API | Complex | 8 |
| Validate PDF/A present | API | Medium | 6 |
| Open or download package | API | Easy | 4 |
| PDF/A package records | DB | Medium | 4 |
| Searchable PDF/A package tests | Testing | Complex | 8 |
| Searchable PDF/A package implementation documentation | Documentation | Medium | 3 |

**Feature total: 43 hours**
