# F03-001 — Scan Production Recording

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Scan Production Recording |
| **Module** | 03 — Scanning and Searchable PDF/A Production |

### Description
Record pages actually scanned for a unique file ID by size (A4/Legal vs A3+) and grey/colour, excluding blank pages, and reconcile to the inward census.

### Business Objective
Production quantities for Department visibility match IFQ counting rules (no blanks).

### Actors
Maker: Operator. Approver: none.

### User Journey
1. Who creates: Operator after or during scanning a file.
2. How they create: Scan production register → select unique ID → enter pages by size and colour/grey, device class → Save. System compares to inward census.
3. How they edit: Correct counts before QC close; history kept.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: Production history on the file.
8. How the auditor sees history: Supervisor/Department Officer same history.

### Functional Capabilities
- Record scanned pages by size and colour/grey
- Exclude blanks from count
- Reconcile to inward page census
- Search production by date and ID

### UI Screens
| Screen | Complexity |
|---|---|
| Scan production register | Medium |
| Scan production form | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Record scanned pages | Complex |
| Search scan production | Medium |
| Reconcile to inward census | Complex |

### Inputs
Unique ID, page counts, colour/grey, device class.

### Outputs
Production quantities; variance vs inward.

### Business Rules
- Blank pages not counted.
- All pages in the file are to be scanned unless exception closed.
- Variance from inward must be explainable (blanks, missing-page exception).

### Validations
- Unique ID has inward log.
- Counts ≥ 0.

### Calculations
Variance = inward total − blanks − scanned (as configured).

### Workflow
No approval.

### Search Requirements
Date, ID, variance flag.

### Documents
None (images in F03-002).

### Reports
Feeds F06-003.

### Notifications
None.

### Security
Operators record; Supervisor sees all.

### Integrations
None.

### Dependencies
F02-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Physical scanning labour is not in these hours.

### Risks
Operators under-count A3 to hide variance.

### Non Functional Requirements
Fast entry per file on the scan floor.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Scan production register | UI | Medium | 6 |
| Scan production form | UI | Medium | 6 |
| Record scanned pages | API | Complex | 8 |
| Search scan production | API | Medium | 6 |
| Reconcile to inward census | API | Complex | 8 |
| Scan production records | DB | Medium | 4 |
| Scan production recording tests | Testing | Complex | 8 |
| Scan production recording implementation documentation | Documentation | Easy | 2 |

**Feature total: 48 hours**
