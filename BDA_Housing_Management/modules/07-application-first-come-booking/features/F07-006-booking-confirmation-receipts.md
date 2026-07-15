# F07-006 — Booking Confirmation & Receipts

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F07-006 |
| **Feature Name** | Booking Confirmation & Receipts |
| **Module** | 07 — Application First Come Booking |

### Description
Generate, release, and retain the booking confirmation and linked booking payment receipt after a booking is confirmed.

### Business Objective
Give citizens and BDA a retrievable proof of the completed booking without duplicating payment accounting.

### Actors
Citizen; Housing/Estate Officer; Accounts Officer; Auditor.

### User Journey
On successful booking confirmation, the system creates the confirmation artefact and associates the settled booking receipt; the citizen downloads released copies and authorised officers can reissue a marked copy with history.

### Functional Capabilities
- Booking confirmation preview, release, download, and reissue controls.
- Linked booking receipt view and personal download route.
- Issue/reissue history and document availability status.

### Inputs
Confirmed booking, approved document template, payment receipt reference, authorised reissue reason, and release action.

### Outputs
Booking confirmation, linked receipt access, document history, and download/reissue audit.

### Business Rules
A confirmation is produced only for a confirmed booking; original issue remains immutable; reissue retains the original reference and reason; receipt figures are sourced from the settled payment record.

### Validations
Confirmed booking state, active template, valid receipt link, reissue authority/reason, and citizen ownership for download.

### Calculations
No independent financial calculation; displayed booking amount and payment details mirror the settled payment record.

### Workflow
Booking confirmed → confirmation generated/released → citizen download; authorised reissue → revised copy/history.

### Search Requirements
Booking number, application, citizen, project, unit, issue date, and reissue status.

### Documents
Booking confirmation, payment receipt, and reissue history.

### Reports
Booking-confirmation issue/reissue register and download audit.

### Notifications
Confirmation and receipt availability notice through Module 12.

### Security
Citizen-only own downloads, role-controlled reissue, template output protection, and auditable access.

### Integrations
Receipt/status consumption from Module 08 (Easy) and notification handoff (Easy).

### Dependencies
F07-004; Module 08; F06-005; Module 12.

### Assumptions
Document wording and number conventions are BDA-approved templates configured in Module 02.

### Risks
Template changes after issue require controlled reissue policy.

### Non Functional Requirements
Reliable PDF/document generation, accessible downloads, and archival-quality reproducibility.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Confirmation and receipt access screens | UI | Complex | 8 |
| Document generation, release, and reissue processing | API | Complex | 8 |
| Artefact issue and reissue persistence | Database | Medium | 4 |
| Payment receipt and notification handoffs | Integration | Easy | 8 |
| Confirmation artefact tests | Testing | Complex | 8 |
| Booking artefact guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
Payment receipt generation is owned by Module 08; this feature consumes and presents the linked receipt.
