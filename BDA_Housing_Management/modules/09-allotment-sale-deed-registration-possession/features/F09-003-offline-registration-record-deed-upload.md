# F09-003 — Offline Registration Record & Deed Upload

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F09-003 |
| **Feature Name** | Offline Registration Record & Deed Upload |
| **Module** | 09 — Allotment Sale Deed Registration Possession |

### Description
Record the outcome of offline Sub-Registrar registration, capture required registration particulars, upload the registered sale deed, and release the artefact to the citizen when authorised.

### Business Objective
Close the gap between the approved in-system draft and the legally executed offline registration outcome.

### Actors
Registration Section; Housing Officer; Citizen; Auditor.

### User Journey
Following offline registration, a Registration officer opens the approved deed case, enters the registration number/date, document/book numbers, SRO, stamp duty, and registration charges, uploads the registered deed, validates completeness, and marks registration completed.

### Functional Capabilities
- Registration-pending worklist, details capture, registered-deed upload, completeness review, and correction history.
- Citizen document release control and registration-completed status transition.
- Missing-document exception list.

### Inputs
Approved draft deed, registration number/date, document/book numbers, SRO, stamp duty, registration charges, registered deed scan, and officer remarks.

### Outputs
Registration record, uploaded registered deed, registration-completed status, and citizen release availability.

### Business Rules
Registration is performed outside BHMS; BHMS records only the completed outcome; registration-completed status requires configured mandatory particulars and registered deed upload; edits after completion retain audit history.

### Validations
Approved draft link, required SRO fields, registration-date plausibility, unique registration reference as configured, permitted document type/size, and authorised release.

### Calculations
Registration/stamp-duty amounts are captured values; registration-pending ageing is calculated from approved draft date.

### Workflow
Approved draft → offline registration → particulars entered/deed uploaded → validation complete → registration completed → citizen release.

### Search Requirements
Registration number, deed number, booking, citizen, project, unit, SRO, registration date, and upload status.

### Documents
Approved draft deed, registered sale deed, registration support evidence, and correction notes.

### Reports
Registration register, pending-registration ageing, and missing-deed exception report.

### Notifications
Registration completion and registered-deed availability notices through Module 12.

### Security
Registration-section access, controlled correction/release, citizen-only own document download, and auditable uploads.

### Integrations
Deed/booking status consumption (Medium) and notification handoff (Easy); no Sub-Registrar integration.

### Dependencies
F09-002, F09-004, Modules 07, 08, and 12.

### Assumptions
BDA supplies the digital registered deed; physical scanning is BDA responsibility.

### Risks
Missing or illegible registered deed scans and inaccurate SRO data can delay possession.

### Non Functional Requirements
Reliable large-file upload, secure document storage/retrieval, and complete audit of registration changes.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Registration worklist, capture, and upload UI | UI | Complex | 8 |
| Registration validation and completion processing | API | Complex | 8 |
| Registration and deed-metadata persistence | Database | Complex | 6 |
| Deed/status and notification handoffs | Integration | Medium | 16 |
| Registration recording tests | Testing | Complex | 8 |
| Registration capture guide | Documentation | Complex | 4 |
| **Total** | | | **50** |

### Estimation Assumptions
No online Kaveri/Sub-Registrar connector is included; this feature records officer-entered offline registration results.
