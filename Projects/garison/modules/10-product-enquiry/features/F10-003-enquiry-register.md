# F10-003 — Enquiry Register

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F10-003 |
| Feature Name | Enquiry Register |
| Module | 10 — Product Enquiry |
| Module Type | Business |
| Release | Go-live |

### Description
Basic administrative register of enquiries with filters (date, category, product, role, status), enquiry detail with product link and email delivery status, mark as Handled with internal note, export, and retention-based purge of personal data.

### Business Objective
Give Garrison a backup record of all enquiries and simple handling status, without a full CRM.

### Actors
- Catalogue Administrator
- Super Administrator
- Content Administrator (view)

### User Journey
1. **Who creates:** Enquiry records are created by visitors through F10-001.
2. **How they create:** Administrators open the register and the enquiry detail.
3. **How they edit:** They mark enquiries as Handled and add internal notes; enquiry content itself cannot be edited.
4. **How they send for approval:** No approval applies.
5. **How the approver sees pending items:** There is no approver inbox; New enquiries are highlighted in the register.
6. **How the approver decides:** No decision applies beyond marking Handled.
7. **How the maker sees history:** Administrators see status and notes history on each enquiry.
8. **How the approver / auditor sees history:** Auditors see status changes, exports and purges in the audit log.

### Functional Capabilities
- Register with filters and New/Handled status
- Enquiry detail with product link and delivery status
- Mark handled with internal note
- Export to CSV/XLSX
- Retention setting (default 24 months) with automatic purge of personal data

### UI Screens
- Enquiry register with filters
- Enquiry detail
- Mark handled and internal note dialog
- Enquiry export dialog

### Logical API Operations
- List enquiries with filters
- Get enquiry detail
- Update enquiry status and note
- Export enquiries
- Purge enquiries past retention

### Inputs
- Status, internal note, filters, retention period

### Outputs
- Enquiry list, detail, exports

### Business Rules
- Enquiry content is read-only
- Purge removes personal fields but keeps anonymised product/category statistics

### Validations
- Note max 1,000 characters

### Calculations
- Age of enquiry; counts by status

### Workflow
New → Handled

### Search Requirements
- Date range, category, product code, role, status, email

### Documents
- None

### Reports
- Enquiry export; enquiries by category in F11-004

### Notifications
- None

### Security
- Manage enquiry register permission; export audited

### Integrations
- None

### Dependencies
- F10-001
- F10-002
- F01-004

### Assumptions
- Full enquiry management (assignment, follow-ups, quotes) is a future enhancement

### Risks
- Garrison may need CRM integration later; export provides an interim path

### Non Functional Requirements
- Register loads under 2 seconds

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Enquiry register with filters | Medium | 6 |
| UI | Enquiry detail | Easy | 4 |
| UI | Mark handled and internal note dialog | Simple | 2 |
| UI | Enquiry export dialog | Simple | 2 |
| API | List enquiries with filters | Medium | 6 |
| API | Get enquiry detail | Easy | 4 |
| API | Update enquiry status and note | Easy | 4 |
| API | Export enquiries | Complex | 8 |
| API | Purge enquiries past retention | Medium | 6 |
| Database | Enquiry status and notes | Simple | 1 |
| Database | Enquiry retention settings | Simple | 1 |
| Testing | Register filters and status updates | Easy | 4 |
| Testing | Export and retention purge | Easy | 4 |
| Documentation | Enquiry register guide | Simple | 1 |

**Feature Total: 53 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 28 | 2 | 0 | 8 | 1 | **53** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Basic register; export is Complex per standard export handling
- No external integration channel in this feature; Integration row omitted.
