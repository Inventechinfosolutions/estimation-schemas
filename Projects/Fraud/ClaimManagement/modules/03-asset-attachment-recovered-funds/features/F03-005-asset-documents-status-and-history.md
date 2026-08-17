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
1. Officer opens the asset, uploads supporting documents and changes status, then saves.
2. The system appends a history row: who, when, previous status, new status.
3. An authorised user reopens the asset and replays document and status history.

### Functional Capabilities
- Upload supporting asset documents.
- Change and save asset status.
- Append-only history (who, when, previous, new).
- Replay document and status history on the asset.

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
| Asset document and history persistence | DB | Medium | 4 |
| Asset document/history tests | Testing | Medium | 6 |
| Asset history note | Documentation | Easy | 2 |
| **Total** | | | **34** |

### Estimation Assumptions
- Uses Estimation Master values only.
- Attachment order e-format is F03-003; this feature is supporting docs and status history.
