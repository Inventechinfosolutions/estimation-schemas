# F02-001 — Unique File ID

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-001 |
| **Feature Name** | Unique File ID |
| **Module** | 02 — File Inward, Unique ID and Pre-Scan Control |

### Description
Allocate a unique file ID and record that it is marked on the front cover, back cover and internal noting pages before any page is scanned.

### Business Objective
Every physical file and its PDF/A share one ID for custody, QC, metadata and e-Office.

### Actors
Maker: Operator / Supervisor. Approver: none.

### User Journey
1. Who creates: Operator when the file is received (or Supervisor).
2. How they create: Unique ID register → Allocate ID → record file title as received → confirm covers/noting marked → Save.
3. How they edit: Correct title if Department agrees; ID itself is not reused.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox.
6. How the approver decides: No decision.
7. How the maker sees history: ID allocation history.
8. How the auditor sees history: Department Officer searches ID.

### Functional Capabilities
- Allocate unique ID
- Record marking on covers and noting pages
- Search by ID and title

### UI Screens
| Screen | Complexity |
|---|---|
| Unique file ID register | Medium |
| Allocate file ID form | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Allocate unique file ID | Complex |
| Search file IDs | Medium |
| Record cover marking | Easy |

### Inputs
Received file name/title, marking confirmation.

### Outputs
Unique ID used on all later steps.

### Business Rules
- ID unique for the project.
- Scanning (Module 03) requires an ID.
- IDs are not recycled.

### Validations
- Marking confirmation required.

### Calculations
None.

### Workflow
No approval.

### Search Requirements
ID, title, date allocated.

### Documents
Physical mark on the file (process); tool stores the ID.

### Reports
None.

### Notifications
None.

### Security
Operators allocate; Department Officer can search.

### Integrations
None.

### Dependencies
F01-002.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- ID format is a Department-approved simple pattern (not a statewide file-numbering product).

### Risks
Duplicate physical marks if two operators allocate offline.

### Non Functional Requirements
Allocation works without internet (site LAN).

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Unique file ID register | UI | Medium | 6 |
| Allocate file ID form | UI | Medium | 6 |
| Allocate unique file ID | API | Complex | 8 |
| Search file IDs | API | Medium | 6 |
| Record cover marking | API | Easy | 4 |
| Unique file ID records | DB | Easy | 2 |
| Unique file ID tests | Testing | Medium | 6 |
| Unique file ID implementation documentation | Documentation | Easy | 2 |

**Feature total: 40 hours**
