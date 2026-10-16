# F02-006 — Reference Masters

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F02-006 |
| Feature Name | Reference Masters |
| Module | 02 — Auction Rules & Configuration |
| Module Type | Business |
| Release | Go-live |

### Description
Maintenance of reference data used across the Module: layouts, blocks and sectors, site categories, Sub-Registrar offices, BDA bank accounts, payment modes, document types, rejection / re-auction / cancellation reasons, dispute categories, and the holiday calendar.

### Business Objective
Provide consistent, controlled lists for data entry, rules and reports.

### Actors
- Auction Admin
- Super Admin

### User Journey
1. **Who creates:** The Auction Admin creates master entries.
2. **How they create:** The Auction Admin opens Masters, selects a master, adds entries with code and Kannada / English names, or uploads them from Excel.
3. **How they edit:** The Auction Admin edits or deactivates entries; deactivated entries remain on old records.
4. **How they send for approval:** Master changes do not need approval except bank accounts, which need Finance Officer confirmation.
5. **How the approver sees pending items:** The Finance Officer sees pending bank account changes.
6. **How the approver decides:** The Finance Officer confirms or rejects the bank account change.
7. **How the applicant / maker sees history:** Users see active entries in drop-downs.
8. **How the approver / auditor sees history:** Auditors see master change history.

### Functional Capabilities
- Generic master framework with code, Kannada and English names, active flag, sort order
- Layouts, blocks, sectors and wards hierarchy
- Sub-Registrar offices
- BDA collection bank accounts with Finance confirmation
- Payment modes, document types, reasons, dispute categories
- Holiday calendar by year with Excel upload
- Excel import / export for all masters

### UI Screens
- Master list and selector
- Master entry form
- Layout hierarchy maintenance
- Holiday calendar
- Bank account maintenance with confirmation
- Excel import result

### Logical API Operations
- Generic master CRUD
- Hierarchy maintenance
- Import / export masters
- Confirm bank account change
- Lookup service for drop-downs

### Inputs
- Codes and names
- Hierarchy parent
- Holiday dates
- Bank account details
- Import files

### Outputs
- Active master lists
- Exports

### Business Rules
- Codes unique within a master
- In-use entries are deactivated, never deleted
- Bank accounts become active only after Finance Officer confirmation

### Validations
- IFSC format
- Dates valid
- Mandatory bilingual names

### Calculations
- None

### Workflow
Active ↔ Inactive; Bank account: Pending → Confirmed / Rejected

### Search Requirements
- Entries by code and name

### Documents
- None

### Reports
- Master exports

### Notifications
- Bank account confirmation request to Finance Officer

### Security
- Masters editable only by Auction Admin / Super Admin

### Integrations
- Layout list may be seeded from CDRMS during migration

### Dependencies
- Used across all modules

### Assumptions
- BDA supplies initial master data

### Risks
- Inconsistent layout names versus KPPP and CDRMS; mitigated by alias mapping in F03-003

### Non Functional Requirements
- Look-ups under 200 ms

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Master list and selector | Easy | 4 |
| UI | Master entry form | Easy | 4 |
| UI | Layout hierarchy maintenance | Medium | 6 |
| UI | Holiday calendar | Easy | 4 |
| UI | Bank account maintenance with confirmation | Easy | 4 |
| UI | Excel import result | Easy | 4 |
| API | Generic master CRUD | Medium | 6 |
| API | Hierarchy maintenance | Medium | 6 |
| API | Import / export masters | Medium | 6 |
| API | Confirm bank account change | Easy | 4 |
| API | Lookup service for drop-downs | Easy | 4 |
| Database | Generic master store | Easy | 2 |
| Database | Layout hierarchy | Easy | 2 |
| Database | Holiday calendar | Simple | 1 |
| Testing | Master maintenance and import tests | Medium | 6 |
| Documentation | Masters maintenance guide | Easy | 2 |

**Feature Total: 65 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 26 | 5 | 0 | 6 | 2 | **65** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Generic framework keeps per-master effort low
- No external integration channel in this feature; Integration row omitted.
