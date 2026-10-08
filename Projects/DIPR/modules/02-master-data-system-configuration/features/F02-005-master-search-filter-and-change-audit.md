# F02-005 — Master search, filter & change audit

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-005 |
| Feature Name | Master search, filter & change audit |
| Module | 02 — Master Data & System Configuration |
| Description | Search and filter across reference masters and retain change history for configuration and lookup edits. |
| Business Objective | Speed administrator support and prove what changed in masters before campaign or PoD incidents. |
| Actors | DIPR Administrator; Auditor (read-only history) |

### User Journey

- Administrator opens Master Search → enters keyword or selects master type → opens record → views Change history tab with user, timestamp, old/new values → exports slice if needed for ticket attachment.

### Functional Capabilities

- Unified search across media/campaign lookups, vendors, locations, templates, parameters
- Filters by master category, editor, date range
- Per-record change timeline with field-level diff summary
- Optional export of search results (codes and status, not bulk secrets)

### Inputs

- Search text, filters; system captures edits automatically

### Outputs

- Filtered master result set; audit timeline views

### Business Rules

- Parameter secrets (API keys) masked in history display
- History retained per retention parameter

### Validations

- Export row limits enforced

### Calculations

- None

### Workflow

- Edit on any F02 feature → audit row → visible in timeline

### Search Requirements

- Cross-master keyword and structured filters

### Documents

- CSV export of search results

### Reports

- Supports operational investigations ahead of Module 07 exports

### Notifications

- None

### Security

- History read restricted; no delete of audit rows

### Integrations

- None

### Dependencies

- All F02-001–F02-004 write paths emit audit events

### Assumptions

- Field-level diff sufficient without full JSON snapshot for large templates

### Risks

- High-volume template edits produce long timelines without pagination

### Non Functional Requirements

- Search returns within interactive SLA for typical master volumes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Unified master search screen with type-ahead | Medium | 6 |
| UI | Search results grouped by master type | Medium | 6 |
| UI | Master record quick-open drawer | Easy | 4 |
| UI | Master change history timeline panel | Easy | 4 |
| UI | Filter by master type and editor user | Easy | 4 |
| UI | Change diff view (before/after fields) | Medium | 6 |
| API | Cross-master federated search | Complex | 8 |
| API | Retrieve change audit trail for master key | Medium | 6 |
| API | List recent master changes with filters | Medium | 6 |
| Database | Change audit linkage to master records | Medium | 4 |
| Database | Search indexing metadata for masters | Easy | 2 |
| Testing | Audit emitted on vendor and parameter edits | Medium | 6 |
| Testing | Search returns correct master types | Medium | 6 |
| Testing | Unauthorized audit access denied | Easy | 4 |
| Documentation | Master audit investigation guide | Easy | 2 |
| Documentation | UAT trace vendor master edit | Easy | 2 |

**Feature Total: 76 hours**

### Estimation Assumptions

- Deep integration with enterprise SIEM is via Module 09/10, not duplicate logging here.
