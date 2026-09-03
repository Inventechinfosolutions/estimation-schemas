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
1. Who creates: Office user
2. How they create: Officer uploads court-order file and sale-deed files with court-order number and details.
3. How they edit: Later valuer uses View (F04-003) to open these files.
4. How they send for approval: Replacing a file is an auditable office action. Upload → store on asset → valuer View; replace → history.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Upload court order (number and details with file) and sale deeds (with file)
- Replace with history
- Serve the same files to valuer View

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My upload court order and sale deeds list / queue | Medium |
| Court-order and sale-deed upload pack | Medium |
| Upload court order and sale deeds history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Deed/order attach and replace | Medium |
| Update upload court order and sale deeds | Medium |
| Search upload court order and sale deeds | Medium |
| Read upload court order and sale deeds history | Easy |

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
|---|---|---|---|
| My upload court order and sale deeds list / queue | UI | Medium | 6 |
| Court-order and sale-deed upload pack | UI | Medium | 6 |
| Upload court order and sale deeds history | UI | Medium | 6 |
| Deed/order attach and replace | API | Medium | 6 |
| Update upload court order and sale deeds | API | Medium | 6 |
| Search upload court order and sale deeds | API | Medium | 6 |
| Read upload court order and sale deeds history | API | Easy | 4 |
| Upload court order and sale deeds persistence | DB | Medium | 4 |
| Internal document storage | Integration | Simple | 4 |
| Upload court order and sale deeds feature tests | Testing | Medium | 6 |
| Upload court order and sale deeds implementation documentation | Documentation | Easy | 2 |
| **Total** | | | **56** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
