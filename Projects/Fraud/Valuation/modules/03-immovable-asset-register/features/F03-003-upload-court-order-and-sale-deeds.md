# F03-003 — Upload court order and sale deeds

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Upload court order and sale deeds |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
The Officer uploads the court-order file and sale-deed files against the asset, with court-order number and details. A later valuer uses View (F04-003) to open these files; replacing a file is an auditable office action.

### Business Objective
Store the court order and sale deeds the assigned valuer will open, with auditable replace.

### Actors
Office user; Approved Valuer (view later).

### User Journey
1. Officer uploads court-order file and sale-deed files with court-order number and details.
2. Later valuer uses View (F04-003) to open these files.
3. Replacing a file is an auditable office action.

### Functional Capabilities
- Upload court order (number and details with file) and sale deeds (with file)
- Replace with history
- Serve the same files to valuer View

### Inputs
Court-order number and details; court-order file; sale-deed files.

### Outputs
Stored files on the asset; version history on replace.

### Business Rules
- Valuer does not invent a document if none was uploaded (F04-003 states the gap)
- Replace is office-only and audited

### Validations
- File present for each typed upload
- Court-order number when a court-order file is stored

### Calculations
None.

### Workflow
Upload → store on asset → valuer View; replace → history.

### Search Requirements
Court-order number, asset, upload date.

### Documents
Court order; sale deeds.

### Reports
Assets missing deed or order file.

### Notifications
None.

### Security
Need-to-know (F01-003); office upload; valuer view if assigned.

### Integrations
Internal document storage (embedded, not a DMS product).

### Dependencies
F03-001; F01-003; F04-003.

### Assumptions
- Scanning bureau is out of scope unless separately ordered.

### Risks
Large deed PDFs; replace without history would break valuer evidence.

### Non Functional Requirements
Files remain with the asset; HTTPS; AES-256 as programme NFR.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Court-order and sale-deed upload pack | UI | Medium | 6 |
| Deed/order attach and replace | API | Medium | 6 |
| Deed/order file metadata | Database | Medium | 4 |
| Internal document storage | Integration | Simple | 4 |
| Upload/replace tests | Testing | Medium | 6 |
| Deed/order upload note | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- Valuer View UX is F04-003; CAD is F03-006.
