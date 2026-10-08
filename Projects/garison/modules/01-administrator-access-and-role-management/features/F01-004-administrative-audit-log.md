# F01-004 — Administrative Audit Log

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F01-004 |
| Feature Name | Administrative Audit Log |
| Module | 01 — Administrator Access & Role Management |
| Module Type | Shared |
| Release | Go-live |

### Description
Append-only log of every administrative create, update, delete, workflow, publication, import and authentication event, with user, timestamp, entity, action and field-level before/after values. Searchable and exportable, with an entity history panel on product and combination records.

### Business Objective
Make every catalogue change traceable to a person and time, support Garrison's internal accountability, and help diagnose content issues.

### Actors
- Super Administrator
- Catalogue Administrator (view)
- Catalogue Reviewer (view)

### User Journey
1. **Who creates:** Audit entries are created automatically by the system whenever any administrator performs a recorded action; no user creates entries manually.
2. **How they create:** The audit interceptor captures user, role, timestamp, entity type and ID, action, and changed fields with old and new values.
3. **How they edit:** Audit entries cannot be edited or deleted by any role.
4. **How they send for approval:** No submission or approval applies to audit records.
5. **How the approver sees pending items:** There is no approver inbox; auditors use the audit log register.
6. **How the approver decides:** No decision applies.
7. **How the maker sees history:** A maker sees the history of the product or combination they edit in the entity history panel.
8. **How the approver / auditor sees history:** The Super Administrator and auditors search the audit log by user, entity, action and date, open a before/after diff and export results.

### Functional Capabilities
- Automatic capture across all admin modules (products, combinations, taxonomy, attributes, templates, media, sources, workflow, publishing, import, users, roles, settings, authentication)
- Field-level diff with old and new values
- Audit register with filters (user, entity type, entity code, action, date range)
- Entry detail with side-by-side before/after
- Entity history panel embedded in product and combination workspaces
- CSV/XLSX export of filtered results
- Retention setting (default 7 years) with archival of older entries

### UI Screens
- Audit log register with filters
- Audit entry detail with before/after comparison
- Entity history panel on product and combination workspaces
- Audit export dialog

### Logical API Operations
- Record audit event through cross-cutting interceptor
- Search audit log
- Get audit entry with field-level diff
- Get entity history timeline
- Export audit log
- Archive audit entries past retention

### Inputs
- System-captured action context (user, entity, before/after)
- Search filters
- Retention period setting

### Outputs
- Immutable audit entries
- Filtered audit views and exports
- Entity history timelines

### Business Rules
- Audit entries are append-only and never edited
- Passwords, tokens and secrets are never written to the audit log
- Workflow transitions and publications are always audited

### Validations
- Date range valid on search
- Export limited to 100,000 rows per request

### Calculations
- Field-level diff computed at capture time

### Workflow
Not applicable

### Search Requirements
- User, role, entity type, entity code/name, action, date range, free text on changed field

### Documents
- None

### Reports
- Audit export (CSV/XLSX)
- Entity change history

### Notifications
- None

### Security
- View restricted by permission
- Export action itself audited

### Integrations
- None

### Dependencies
- F01-001
- F01-003
- All administrative features

### Assumptions
- Public visitor actions are not audited here (analytics in F11-004; enquiries in F10-003)

### Risks
- High-volume bulk imports generate many entries; batched audit entries are used for imports

### Non Functional Requirements
- Audit writes do not noticeably slow admin saves (asynchronous where safe)
- Search under 3 seconds over one year of data

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Audit log register with filters | Complex | 12 |
| UI | Audit entry detail with before/after comparison | Medium | 6 |
| UI | Entity history panel on product and combination workspaces | Medium | 6 |
| UI | Audit export dialog | Simple | 2 |
| API | Record audit event through cross-cutting interceptor | Complex | 8 |
| API | Search audit log | Medium | 6 |
| API | Get audit entry with field-level diff | Medium | 6 |
| API | Get entity history timeline | Medium | 6 |
| API | Export audit log | Complex | 8 |
| API | Archive audit entries past retention | Easy | 4 |
| Database | Append-only audit store with field-level change detail | Complex | 6 |
| Database | Audit retention and archive configuration | Easy | 2 |
| Testing | Audit capture coverage across all modules | Complex | 8 |
| Testing | Diff accuracy and immutability | Medium | 6 |
| Testing | Search and export with large audit volume | Easy | 4 |
| Documentation | Audit log usage guide | Easy | 2 |

**Feature Total: 92 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 26 | 38 | 8 | 0 | 18 | 2 | **92** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Cross-cutting interceptor is the main complexity driver
- Bulk operations write summary audit entries plus per-record detail
- No external integration channel in this feature; Integration row omitted.
