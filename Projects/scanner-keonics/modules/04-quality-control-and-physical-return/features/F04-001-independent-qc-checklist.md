# F04-001 — Independent QC Checklist

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-001 |
| **Feature Name** | Independent QC Checklist |
| **Module** | 04 — Quality Control and Physical Return |

### Description
A team other than the scanners records pass/fail against the IFQ image checks (too dark/light, lighting, crop, orientation, colour patchiness, skew, blur, fold loss, binding bulge, edge darkness) and replica-of-original.

### Business Objective
Independent QC as mandated; failed files cannot be treated as complete.

### Actors
Maker: QC operator (not the scanner of that file). Approver: none.

### User Journey
1. Who creates: QC operator taking the next scanned file.
2. How they create: QC queue → open unique ID → complete checklist → Pass or Fail → Save. Scanner of that file must not be the QC user (enforced).
3. How they edit: Re-QC after rescan (F04-002).
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No checker inbox; Supervisor sees QC queue.
6. How the approver decides: No Department approve of image quality in-tool; Department may inspect samples.
7. How the maker sees history: QC history on the file.
8. How the auditor sees history: Department Officer views QC result.

### Functional Capabilities
- QC queue of files with PDF/A but no pass
- Full IFQ checklist
- Pass/fail with operator identity
- Block scanner-as-QC-on-own-file

### UI Screens
| Screen | Complexity |
|---|---|
| QC queue | Medium |
| QC checklist form | Complex |
| QC history | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Load file for QC | Medium |
| Save QC result | Complex |
| Search QC results | Medium |

### Inputs
Unique ID, checklist answers, pass/fail.

### Outputs
QC status for rescan and completeness.

### Business Rules
- QC user ≠ scan production user for that file.
- Fail requires F04-002.
- Licensed imaging software is used by SP; this records the business checklist.

### Validations
- All checklist items answered on submit.

### Calculations
None.

### Workflow
No maker–checker of QC itself.

### Search Requirements
Fail list, date, operator.

### Documents
View PDF/A during QC (F03-002).

### Reports
QC pending on MIS.

### Notifications
None.

### Security
QC role or Supervisor.

### Integrations
None.

### Dependencies
F03-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Not rebuilding the licensed QC imaging tool.

### Risks
Same person scans and ticks QC if roles are weakly assigned.

### Non Functional Requirements
Checklist usable at volume.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| QC queue | UI | Medium | 6 |
| QC checklist form | UI | Complex | 12 |
| QC history | UI | Easy | 4 |
| Load file for QC | API | Medium | 6 |
| Save QC result | API | Complex | 8 |
| Search QC results | API | Medium | 6 |
| QC result records | DB | Medium | 4 |
| Independent QC checklist tests | Testing | Complex | 8 |
| Independent QC checklist implementation documentation | Documentation | Medium | 3 |

**Feature total: 57 hours**
