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
1. Who creates: Officer
2. How they create: Officer uploads depositor documents, sets verification/tracking status, and saves.
3. How they edit: The system stores structured fields and a history of status changes (who, when).
4. How they send for approval: Officer reopens the profile and sees documents and history without relying on a PDF published on a home page. Upload/status → history row → reopen. Embedded documents.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload depositor documents.
- Set verification/tracking status.
- Append status history (who, when).
- Reopen profile to see documents and history.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Depositor document pack and status | Complex |
| Depositor status history | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Depositor document/status operations | Medium |
| Update depositor documents, status and history | Medium |
| Search depositor documents, status and history | Medium |
| Read depositor documents, status and history history | Easy |

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
| Update depositor documents, status and history | API | Medium | 6 |
| Search depositor documents, status and history | API | Medium | 6 |
| Read depositor documents, status and history history | API | Easy | 4 |
| Depositor document and history persistence | DB | Medium | 4 |
| Depositor documents, status and history feature tests | Testing | Medium | 6 |
| Depositor documents, status and history implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **50** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
