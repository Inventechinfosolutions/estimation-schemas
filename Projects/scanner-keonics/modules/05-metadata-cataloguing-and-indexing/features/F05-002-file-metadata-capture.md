# F05-002 — File Metadata Capture

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F05-002 |
| **Feature Name** | File Metadata Capture |
| **Module** | 05 — Metadata, Cataloguing and Indexing |

### Description
Capture metadata for Active, Closed and Archive files as in the IFQ (file no., quarry lease no., applicant/lease/crusher, subject, taluk, hobli, village, survey no., keywords, dates, document type, page size & no., status, remarks / closing / archive fields). Fields are extendable when the Department customises the list.

### Business Objective
Retrieve digitised quarry/lease files the way DMG searches them.

### Actors
Maker: Operator. Viewer: Department Officer. Approver: none.

### User Journey
1. Who creates: Operator after QC pass (or in parallel if Department allows).
2. How they create: Metadata form → select unique ID and file status (Active/Closed/Archive) → fill the matching field set → Save.
3. How they edit: Correct fields; history of last change.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No inbox. Incomplete metadata list for Supervisor.
6. How the approver decides: No decision.
7. How the maker sees history: Last updated metadata.
8. How the auditor sees history: Department Officer search.

### Functional Capabilities
- Status-dependent metadata sets
- Search by file no., lease no., survey, village, keywords
- Extendable extra fields (simple name/value additions without a new module)
- Block “ready to upload” if mandatory fields empty

### UI Screens
| Screen | Complexity |
|---|---|
| Metadata capture form | Complex |
| Metadata search | Medium |

### Logical API operations
| Operation | Complexity |
|---|---|
| Save metadata | Complex |
| Search by lease survey village | Complex |
| Read metadata | Easy |

### Inputs
Unique ID, status, Appendix C fields.

### Outputs
Searchable catalogue record.

### Business Rules
- Active/Closed/Archive show the IFQ field sets.
- Indicative fields may be expanded during the project.
- Keywords support search.

### Validations
- Mandatory subset per status (File No., status, at least one of lease/applicant/survey as Department confirms).

### Calculations
None.

### Workflow
No approval.

### Search Requirements
File no., quarry lease no., survey no., village, keywords, taluk, hobli.

### Documents
Linked PDF/A.

### Reports
None.

### Notifications
None.

### Security
Operators enter; Department Officer searches all.

### Integrations
None (upload separate).

### Dependencies
F05-001, F04-001 (QC pass recommended before complete).

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Typing 12,000 files is commercial line 5, not these software hours.

### Risks
Inconsistent village/taluk spelling harms search.

### Non Functional Requirements
Form usable for quarry-file clerks.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Metadata capture form | UI | Complex | 12 |
| Metadata search | UI | Medium | 6 |
| Save metadata | API | Complex | 8 |
| Search by lease survey village | API | Complex | 8 |
| Read metadata | API | Easy | 4 |
| Metadata records | DB | Complex | 6 |
| File metadata capture tests | Testing | Complex | 8 |
| File metadata capture implementation documentation | Documentation | Medium | 3 |

**Feature total: 55 hours**
