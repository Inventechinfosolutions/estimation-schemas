# F04-001 — OCR, translation and format conversion

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | OCR, translation and format conversion |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
An Officer (or assisting staff) uploads a hard-copy scan or photo (JPEG/PDF). The system produces searchable OCR text, optional translation, and format conversion (for example JPEG to PDF to DOC). The Officer works on the text copy. The original file stays unchanged and remains the source.

### Business Objective
Give Officers a searchable working copy without altering the original evidence file.

### Actors
Officer; assisting staff.

### User Journey
1. Who creates: Officer
2. How they create: Officer or assisting staff uploads a hard-copy scan or photo (JPEG/PDF) against the depositor/claim work.
3. How they edit: The system produces searchable OCR text, optional translation, and format conversion (for example JPEG to PDF to DOC).
4. How they send for approval: Officer works on the text/working copy. Upload original → OCR/convert/translate → Officer works on copy. Human remains responsible for identity decisions.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record. The original file stays unchanged and remains the source.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload JPEG/PDF originals.
- Produce searchable OCR text.
- Optional translation for analysis.
- Format conversion for working copies.
- Keep original immutable and separately identifiable from working copies.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My ocr, translation and format conversion list / queue | Medium |
| Scan upload and OCR workbench | Very High |
| Ocr, translation and format conversion history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| OCR, translation and conversion operations | Very High |
| Update ocr, translation and format conversion | Medium |
| Search ocr, translation and format conversion | Medium |
| Read ocr, translation and format conversion history | Easy |

### Inputs
JPEG/PDF (or similar) original scan/photo.

### Outputs
OCR text; optional translation; converted working copy; unchanged original.

### Business Rules
- Original scans/JPEGs/PDFs are retained unaltered.
- OCR and conversions are working copies, separately identifiable.
- No generative AI compose of claimant communications or identity text.

### Validations
- Allowed file types and size limits.
- Failed OCR is visible as failed; it does not replace the original.

### Calculations
None.

### Workflow
Upload original → OCR/convert/translate → Officer works on copy. Human remains responsible for identity decisions.

### Search Requirements
Searchable OCR text on the working copy; original remains the evidence file.

### Documents
Original scan/photo; OCR/working copies.

### Reports
None.

### Notifications
On-screen processing result.

### Security
KYC images are need-to-know. Working copies do not become a public website PDF.

### Integrations
OCR / translation / conversion engine as contracted.

### Dependencies
Module 01 document rights; depositor/claim context in F04-002/F04-010.

### Assumptions
- Language/script translation is for analysis as required, not a public chatbot.

### Risks
- Treating OCR text as the original would fail BSA 2023 evidence practice for in-KA originals.

### Non Functional Requirements
Integrity: source files immutable; working copies identifiable. Usable staff screens for original physical-document digitisation.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| My ocr, translation and format conversion list / queue | UI | Medium | 6 |
| Scan upload and OCR workbench | UI | Very High | 16 |
| Ocr, translation and format conversion history | UI | Medium | 6 |
| OCR, translation and conversion operations | API | Very High | 16 |
| Update ocr, translation and format conversion | API | Medium | 6 |
| Search ocr, translation and format conversion | API | Medium | 6 |
| Read ocr, translation and format conversion history | API | Easy | 4 |
| Original and working-copy persistence | DB | Medium | 4 |
| OCR/translation/conversion engine | Integration | Complex | 24 |
| OCR, translation and format conversion feature tests | Testing | Very High | 12 |
| OCR, translation and format conversion implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **104** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
