# F04-002 — Other Organisation Registration and Competent Authority Document

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-002 |
| **Feature Name** | Other Organisation Registration and Competent Authority Document |
| **Module** | 04 — Candidate Registration and Fee Payment |

### Description
Other-organisation candidates complete Type 2 registration by manually entering demographic and employment particulars, downloading the competent-authority confirmation template, uploading a digitally signed confirmation document (configured formats and sizes), and associating that document with the registration for later administrator verification. Document upload is **embedded** in this feature — there is no separate DMS module.

### Business Objective
Allow non-government organisation employees to register with evidence of competent-authority confirmation, so eligibility can be verified and mandatory fee payment can proceed on a complete Type 2 draft.

### Actors
Maker: Candidate (other organisation) via candidate portal after OTP login. Approver: none for document upload itself (Examination Administrator verifies in F04-006). Auditor: Examination Administrator (document association and upload events).

### User Journey
1. Who creates: The candidate who selects **Other organisation** as registration type.
2. How they create: Open registration → choose Other Organisation → enter name, father’s name, mobile, email, employee ID, organisation, date of joining, designation and configurable fields → download competent-authority format → obtain digital signature outside the system (or as Department directs) → upload signed document → associate to draft → save Type 2 draft.
3. How they edit: Before registration completion lock, candidate may update manual fields, replace the uploaded document (with version retained), and re-download the template if the format is updated.
4. How they send for approval: Does not apply as a separate submit-to-inbox step inside this feature; document is attached for admin verification in F04-006 after the registration package advances.
5. How the approver sees pending items: No approver inbox here; F04-006 provides the admin registration verification inbox that shows the associated document.
6. How the approver decides: No decision in this feature.
7. How the applicant / maker sees history: Candidate sees upload status, file name, upload time and whether a document is attached on the draft and later on status (F04-005).
8. How the approver / auditor sees history: Administrator views document association, upload/replace history and file metadata on the registration record during verification.

### Functional Capabilities
- Other-organisation registration type selection distinct from KGID path (F04-001).
- Manual capture of mandatory Type 2 fields including organisation employment particulars.
- Configurable additional fields without a separate form-builder product.
- Download of Department competent-authority confirmation template/format.
- Upload of digitally signed confirmation within configured file types and size limits.
- Client- and server-side validation of format/size before accept.
- Associate uploaded document to the registration draft for admin verification.
- Allow replace/re-upload before completion lock with retained prior version for audit.
- Block Type 2 completion path when competent-authority document is missing (gate shared with fee/confirmation).
- Persist Type 2 identity and document metadata with the candidate session.
- Present clear guidance that digital signing occurs as directed by Department (template provided by system).
- Audit upload, replace and association events with user and timestamp.
- Embedded storage/association only — not a full enterprise DMS product.

### UI Screens
| Screen | Purpose |
|---|---|
| Other organisation registration form | Manual demographic and employment fields |
| Competent authority template download screen | Download prescribed format |
| Digitally signed document upload screen | Select and upload confirmation file |
| Upload validation and association feedback screen | Show accept/reject reasons and association status |
| Type 2 draft with document summary screen | Review fields and attached document before continuing |
| Competent authority document history screen | Upload/replace history for candidate and admin |

### Logical API operations
| Operation | Purpose |
|---|---|
| Save other organisation registration details | Persist Type 2 manual fields |
| Download competent authority template | Return current approved template |
| Upload competent authority document | Accept file within configured constraints |
| Validate document metadata and association | Check type/size and bind to draft |
| Replace associated document | Supersede prior upload with audit retention |
| Get document association history | Return upload/replace trail for the draft |

### Inputs
Name; father’s name; mobile; email; employee ID; organisation; date of joining; designation; other configurable fields; digitally signed confirmation file; candidate session identity.

### Outputs
Type 2 registration identity draft; associated document reference and metadata; upload audit events; readiness flag for examination selection (F04-003) subject to document presence.

### Business Rules
- Type 2 path does not use KGID retrieval.
- Competent-authority document is mandatory for Type 2 completion (with mandatory fee in F04-004).
- Only configured formats/sizes are accepted.
- Document remains associated for administrator verification (F04-006).
- Signing of the document is outside this feature unless Department later directs otherwise.
- Embedded document handling only — no separate DMS module or product rebuild.

### Validations
- Mandatory Type 2 field presence and formats (mobile, email, dates).
- File type and size limits.
- Virus/malware scan hook if infrastructure provides (assumed available at hosting layer).
- Candidate may upload only against own draft.

### Calculations
None.

### Workflow
Type 2 draft started → manual fields saved → template downloaded → signed document uploaded and associated → draft ready for F04-003. No approval decision inside this feature.

### Search Requirements
Admin may find drafts by organisation, employee ID, name, mobile and document-attached flag for verification support.

### Documents
Competent-authority confirmation (digitally signed) — embedded upload and association only.

### Reports
Document-missing Type 2 counts feed Module 09; not billed as a separate report here.

### Notifications
In-portal prompts for missing document; lifecycle notifications owned by Module 09 / confirmation features.

### Security
Candidate access limited to own uploads; admin document view for verification roles; audit of every upload/replace; storage access controlled.

### Integrations
None as a separate channel — file storage is application-embedded. Digital signature itself is candidate-side / Department-directed, not a billed external connector on this feature.

### Dependencies
Module 02 (OTP login); F04-003–F04-006; Module 03 for later fee/exam rules.

### Assumptions
- No separate Document Management System module; upload is embedded here per SOW consolidation.
- Template content is supplied/approved by the Department.
- Hours use Estimation Master; each screen and logical API is independently estimated.

### Risks
Incorrect or non-machine-readable signatures increase admin rejection; large files or wrong formats cause repeat uploads.

### Non Functional Requirements
Reliable upload for configured sizes; clear validation messages; durable association for audit and verification.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Other organisation registration form | UI | Complex | 12 |
| Competent authority template download screen | UI | Easy | 4 |
| Digitally signed document upload screen | UI | Complex | 12 |
| Upload validation and association feedback screen | UI | Medium | 6 |
| Type 2 draft with document summary screen | UI | Easy | 4 |
| Competent authority document history screen | UI | Easy | 4 |
| Save other organisation registration details | API | Complex | 8 |
| Download competent authority template | API | Easy | 4 |
| Upload competent authority document | API | Complex | 8 |
| Validate document metadata and association | API | Medium | 6 |
| Replace associated document | API | Medium | 6 |
| Get document association history | API | Easy | 4 |
| Type 2 identity and embedded document metadata persistence | Database | Complex | 6 |
| Other organisation registration and document tests | Testing | Complex | 8 |
| Other organisation registration implementation documentation | Documentation | Medium | 3 |

**Feature total: 95 hours**

### Estimation Assumptions
- Document upload is embedded; Integration row omitted (no external DMS/payment/KGID channel on this feature).
- Admin verification workflow hours remain on F04-006.
