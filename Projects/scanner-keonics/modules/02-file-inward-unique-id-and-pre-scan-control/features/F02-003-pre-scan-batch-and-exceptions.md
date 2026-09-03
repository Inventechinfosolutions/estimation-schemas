# F02-003 — Pre-Scan Batch and Exceptions

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Pre-Scan Batch and Exceptions |
| **Module** | 02 — File Inward, Unique ID and Pre-Scan Control |

### Description
Record batch preparation (de-staple, unbind, smooth, orient, segregate, paste torn sheets) and flag missing pages, missing documents, or files unfit for scanning, bringing them to the Department Official’s notice in the tool.

### Business Objective
Do not silently scan incomplete files or destroy chronology.

### Actors
Maker: Operator. Viewer: Department Officer. Approver: none.

### User Journey
1. Who creates: Operator during pre-scan.
2. How they create: Open unique ID → batch notes and/or exception (missing pages / unfit / chronology risk) → Save. Department Officer sees exception register.
3. How they edit: Close exception when Department instructs how to proceed.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No checker inbox; Department Officer uses the exception register as the notice board.
6. How the approver decides: No formal approve; they instruct on the floor; Operator records outcome.
7. How the maker sees history: Exception history on the file.
8. How the auditor sees history: Same.

### Functional Capabilities
- Batch-preparation note
- Exception types: missing page, missing document, unfit for scan
- Exception register for Department Officer

### UI Screens
| Screen | Complexity |
|---|---|
| Batch preparation form | Medium |
| Exception register | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Record batch preparation | Medium |
| Flag exception | Medium |
| Search exceptions | Medium |

### Inputs
Unique ID, batch notes, exception type, description.

### Outputs
Exception visible to Department; scan may be blocked until recorded outcome.

### Business Rules
- Unfit/missing flagged immediately, not after mass scan.
- Do not mix pages between files.
- Under no circumstances destroy or replace documents.

### Validations
- Exception type mandatory when flagging.

### Calculations
None.

### Workflow
No approval inbox.

### Search Requirements
Open exceptions by date and type.

### Documents
Physical condition as found.

### Reports
Open exception count on MIS.

### Notifications
None (in-tool register only).

### Security
Department Officer sees all exceptions.

### Integrations
None.

### Dependencies
F02-001, F02-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
Operators skip exception logging to keep throughput.

### Non Functional Requirements
Exception register obvious on Department Officer landing.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Batch preparation form | UI | Medium | 6 |
| Exception register | UI | Medium | 6 |
| Record batch preparation | API | Medium | 6 |
| Flag exception | API | Medium | 6 |
| Search exceptions | API | Medium | 6 |
| Batch and exception records | DB | Easy | 2 |
| Pre-scan batch and exceptions tests | Testing | Medium | 6 |
| Pre-scan batch and exceptions implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
