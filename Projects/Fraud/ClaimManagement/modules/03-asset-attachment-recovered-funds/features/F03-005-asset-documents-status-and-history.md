# F03-005 — Asset documents, status and history

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-005 |
| **Feature Name** | Asset documents, status and history |
| **Module** | 03 — Asset Attachment & Recovered Funds |

### Description
The Officer uploads supporting documents, changes asset status, and saves. The system appends a history row (who, when, previous status, new status). An authorised user can open the asset and replay document and status history.

### Business Objective
Keep structured asset documents and an append-only status history instead of a homepage PDF.

### Actors
Officer; authorised viewer; auditor.

### User Journey
1. Who creates: Officer
2. How they create: Officer opens the asset, uploads supporting documents and changes status, then saves.
3. How they edit: The system appends a history row: who, when, previous status, new status.
4. How they send for approval: An authorised user reopens the asset and replays document and status history. Upload/status change → history row → replay. Embedded documents, not a DMS module.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Officer works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Officer opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload supporting asset documents.
- Change and save asset status.
- Append-only history (who, when, previous, new).
- Replay document and status history on the asset.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Asset document pack and status | Complex |
| Asset history replay | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Document and status operations | Medium |
| Update asset documents, status and history | Medium |
| Search asset documents, status and history | Medium |
| Read asset documents, status and history history | Easy |

### Inputs
Files, status value, remarks.

### Outputs
Document list on the asset; status history trail.

### Business Rules
- History is not overwritten; prior status remains visible.
- Structured records, not publishing a PDF on a home page, are how history is kept.

### Validations
- Status values from the recovery lifecycle set.
- Uploads follow allowed types (for example PDF/JPEG).

### Calculations
None.

### Workflow
Upload/status change → history row → replay. Embedded documents, not a DMS module.

### Search Requirements
Asset by status; documents by type on the asset.

### Documents
Supporting asset papers (orders may also sit in F03-003).

### Reports
History extract on the asset.

### Notifications
None.

### Security
View/download of asset papers follows Post rights. History identifies Person and Post.

### Integrations
None.

### Dependencies
F03-001.

### Assumptions
- Document handling is embedded in this process.

### Risks
- Losing history on status overwrite would fail audit.

### Non Functional Requirements
Source files immutable where they are originals; history retrievable.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Asset document pack and status | UI | Complex | 12 |
| Asset history replay | UI | Easy | 4 |
| Document and status operations | API | Medium | 6 |
| Update asset documents, status and history | API | Medium | 6 |
| Search asset documents, status and history | API | Medium | 6 |
| Read asset documents, status and history history | API | Easy | 4 |
| Asset document and history persistence | DB | Medium | 4 |
| Asset documents, status and history feature tests | Testing | Medium | 6 |
| Asset documents, status and history implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **50** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
