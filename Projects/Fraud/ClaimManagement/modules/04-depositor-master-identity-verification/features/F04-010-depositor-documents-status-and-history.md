# F04-010 — Depositor documents, status and history

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-010 |
| **Feature Name** | Depositor documents, status and history |
| **Module** | 04 — Depositor Master & Identity Verification |

### Description
The Officer uploads depositor documents, sets verification/tracking status, and saves. The system stores structured fields and a history of status changes (who, when). The Officer can reopen the profile and see documents and history without relying on a PDF published on a home page.

### Business Objective
Keep depositor documents and status history as structured records on the profile.

### Actors
Officer; authorised viewer.

### User Journey
1. Officer uploads depositor documents, sets verification/tracking status, and saves.
2. The system stores structured fields and a history of status changes (who, when).
3. Officer reopens the profile and sees documents and history without relying on a PDF published on a home page.

### Functional Capabilities
- Upload depositor documents.
- Set verification/tracking status.
- Append status history (who, when).
- Reopen profile to see documents and history.

### Inputs
Files, status, remarks.

### Outputs
Document list; status history on the profile.

### Business Rules
- Publishing a PDF on a home page is not how these records are kept.
- Originals remain unaltered when they are source scans (F04-001).

### Validations
- Allowed file types.
- Status from the tracking set.

### Calculations
None.

### Workflow
Upload/status → history row → reopen. Embedded documents.

### Search Requirements
Profile documents by type; status.

### Documents
KYC and identity papers on the depositor (claim-pack copies also in Module 06).

### Reports
None standalone (F09-006 depositor-wise reports consume structured data).

### Notifications
None.

### Security
View/download per F01-009. History identifies Person and Post.

### Integrations
None.

### Dependencies
F04-002; F04-001 when OCR working copies exist.

### Assumptions
- Claim-pack mandatory documents at Submit are enforced in F06-004 even if some papers also sit on the profile.

### Risks
- Relying on website PDFs would fail structured-data reporting.

### Non Functional Requirements
Structured depositor data supports automated reports.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Depositor document pack and status | UI | Complex | 12 |
| Depositor status history | UI | Easy | 4 |
| Depositor document/status operations | API | Medium | 6 |
| Depositor document and history persistence | DB | Medium | 4 |
| Depositor document/history tests | Testing | Medium | 6 |
| Depositor document history note | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Uses Estimation Master values only.
- OCR engine hours are in F04-001, not repeated here.
