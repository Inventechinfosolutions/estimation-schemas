# F03-003 — Exception Capture Devices

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-003 |
| **Feature Name** | Exception Capture Devices |
| **Module** | 03 — Scanning and Searchable PDF/A Production |

### Description
Record when a file or page-range used overhead scanner, flatbed, digital camera, or 600 dpi+ because the document was torn, fragile, not sheet-feedable, or not legible at 150–200 dpi.

### Business Objective
Prove IFQ device rules were followed for difficult documents.

### Actors
Maker: Operator. Approver: none.

### User Journey
1. Who creates: Operator when not using a normal sheet-feed path.
2. How they create: Exception device form on the unique ID → device type, reason, optional page range, DPI if high-res → Save.
3. How they edit: Update if device changes mid-file.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: List of exception captures on the file.
8. How the auditor sees history: Same list.

### Functional Capabilities
- Record overhead / flatbed / camera / high-DPI
- Reason codes (torn, fragile, illegible, not feedable)
- List by file

### UI Screens
| Screen | Complexity |
|---|---|
| Exception device form | Easy |
| Exception device list | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Record exception device | Medium |
| Search exception devices | Easy |

### Inputs
Unique ID, device, reason, page range, DPI.

### Outputs
Audit of special capture.

### Business Rules
- Camera only when no scanner type can capture.
- High DPI when not legible at 150–200.

### Validations
- Device and reason mandatory.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
By device type and date.

### Documents
Images still land in F03-002 package.

### Reports
None.

### Notifications
None.

### Security
Operators record; Supervisor views.

### Integrations
None.

### Dependencies
F03-001.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.

### Risks
Operators skip logging camera use.

### Non Functional Requirements
Two-field form on the scan station.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Exception device form | UI | Easy | 4 |
| Exception device list | UI | Easy | 4 |
| Record exception device | API | Medium | 6 |
| Search exception devices | API | Easy | 4 |
| Exception device records | DB | Easy | 2 |
| Exception capture devices tests | Testing | Easy | 4 |
| Exception capture devices implementation documentation | Documentation | Easy | 2 |

**Feature total: 26 hours**
