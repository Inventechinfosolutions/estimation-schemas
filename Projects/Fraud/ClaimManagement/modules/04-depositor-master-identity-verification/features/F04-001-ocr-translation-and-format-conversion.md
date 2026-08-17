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
1. Officer or assisting staff uploads a hard-copy scan or photo (JPEG/PDF) against the depositor/claim work.
2. The system produces searchable OCR text, optional translation, and format conversion (for example JPEG to PDF to DOC).
3. Officer works on the text/working copy.
4. The original file stays unchanged and remains the source.

### Functional Capabilities
- Upload JPEG/PDF originals.
- Produce searchable OCR text.
- Optional translation for analysis.
- Format conversion for working copies.
- Keep original immutable and separately identifiable from working copies.

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
| Scan upload and OCR workbench | UI | Very High | 16 |
| OCR, translation and conversion operations | API | Very High | 16 |
| Original and working-copy persistence | DB | Medium | 4 |
| OCR/translation/conversion engine | Integration | Complex | 24 |
| OCR and conversion tests | Testing | Very High | 12 |
| OCR working-copy guide | Documentation | Complex | 4 |
| **Total** | | | **76** |

### Estimation Assumptions
- Uses Estimation Master values only.
- OCR is estimated above the typical range (engine Integration Complex 24, UI Very High workbench).
- No generative model is included.
