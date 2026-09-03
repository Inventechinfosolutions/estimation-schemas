# F02-002 — Inward Log and Page Census

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Inward Log and Page Census |
| **Module** | 02 — File Inward, Unique ID and Pre-Scan Control |

### Description
Record the IFQ inward log when a file is collected: document name, page counts by size, grey/colour intent, Department official, Service Provider collector, dates, expected return. Page numbers are cross-checked in sequence.

### Business Objective
Know exactly what entered the scan room so scanned pages and returned files can be reconciled.

### Actors
Maker: Operator. Department Officer: named as “collected from”. Approver: none (countersignature is custody, not a checker inbox).

### User Journey
1. Who creates: Operator receiving the file from an authorised Department Officer.
2. How they create: Inward register → New → unique ID → fill Appendix D fields including page counts A4/Legal/A3/A2/A1/A0/other and grey/colour → Save. Department name selected from authorised list.
3. How they edit: Correct counts if recount agreed with Department; history kept.
4. How they send for approval: Does not apply.
5. How the approver sees pending items: No checker inbox. Department Officer can open the inward register.
6. How the approver decides: No approve/reject of content.
7. How the maker sees history: Inward history on the file.
8. How the auditor sees history: Same inward history.

### Functional Capabilities
- Capture all inward log fields
- Page census by size
- Bind to unique ID and authorised staff
- Search inward by date, officer, ID

### UI Screens
| Screen | Complexity |
|---|---|
| Inward log register | Medium |
| Inward log form | Complex |
| Inward change history | Easy |

### Logical API operations
| Operation | Complexity |
|---|---|
| Create inward log | Complex |
| Update inward log | Medium |
| Search inward logs | Medium |
| Read inward log | Easy |

### Inputs
Unique ID; Appendix D fields; page counts.

### Outputs
Inward record; expected return date.

### Business Rules
- Collected from / collected by must be authorised (F01-003).
- Page census is the baseline for scan reconciliation (blanks later excluded).
- Files do not leave premises — location remains DMG site.

### Validations
- Unique ID mandatory and existing.
- At least one page-count field > 0 unless exception (F02-003).
- Dates consistent (collection ≤ expected return).

### Calculations
Total pages = sum of size buckets.

### Workflow
No maker–checker.

### Search Requirements
ID, date, Department officer, document name.

### Documents
Physical file remains with SP on site.

### Reports
Feeds progress MIS (F06-003).

### Notifications
None.

### Security
Operators create; Department Officer views.

### Integrations
None.

### Dependencies
F02-001, F01-003.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- Paper log may still be signed; this is the digital mirror.

### Risks
Wrong page census causes payment/reconciliation disputes.

### Non Functional Requirements
Form usable while standing at a handover desk.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| Inward log register | UI | Medium | 6 |
| Inward log form | UI | Complex | 12 |
| Inward change history | UI | Easy | 4 |
| Create inward log | API | Complex | 8 |
| Update inward log | API | Medium | 6 |
| Search inward logs | API | Medium | 6 |
| Read inward log | API | Easy | 4 |
| Inward log records | DB | Medium | 4 |
| Inward log and page census tests | Testing | Complex | 8 |
| Inward log and page census implementation documentation | Documentation | Medium | 3 |

**Feature total: 61 hours**
