# F09-001 — Search Index & Publication Synchronisation

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F09-001 |
| Feature Name | Search Index & Publication Synchronisation |
| Module | 09 — Search & Filtering |
| Module Type | Business |
| Release | Go-live |

### Description
Maintain a dedicated search index of Published products and combinations: index documents flatten core data, taxonomy, materials, finishes, canonical dimension values and searchable attributes; incremental updates on publish/unpublish/archive and master/template changes; full re-index job; index health page.

### Business Objective
Provide fast, accurate search and faceting for a catalogue growing from about 100 to 10,000+ products.

### Actors
- System
- Super Administrator (index operations)

### User Journey
1. **Who creates:** Index documents are created automatically by the system when items are published.
2. **How they create:** The publish workflow (F06-004) queues index updates; master and template changes queue re-index of affected items.
3. **How they edit:** Index entries are updated on every republication and removed on unpublish or archive.
4. **How they send for approval:** No approval applies; indexing follows publication.
5. **How the approver sees pending items:** There is no approver inbox; the Super Administrator sees sync status and errors on the index status page.
6. **How the approver decides:** No decision applies; the Super Administrator may trigger a full re-index.
7. **How the maker sees history:** Not applicable to makers beyond seeing their item appear in public search after publication.
8. **How the approver / auditor sees history:** The Super Administrator sees sync job history and failures; re-index triggers are audited.

### Functional Capabilities
- Index schema covering text, keyword, numeric and facet fields
- Index document builder (products and combinations)
- Queue-based incremental sync with retry
- Re-index on master, template and category changes
- Full re-index job with progress and zero-downtime alias switch
- Index status page (document counts, last sync, failures)

### UI Screens
- Search index status page
- Full re-index trigger dialog

### Logical API Operations
- Build index document for product or combination
- Apply incremental index update on publication events
- Re-index items affected by master or template change
- Run full re-index job
- Check index health

### Inputs
- Publication events, master/template change events, re-index commands

### Outputs
- Up-to-date search index
- Sync logs

### Business Rules
- Only Published snapshot data is indexed
- Failed index updates retried 5 times then flagged
- Full re-index swaps index alias only after success

### Validations
- Index document schema validation before write

### Calculations
- Canonical dimension values indexed as numerics for range queries

### Workflow
Event → Queue → Index → Success | Retry | Failed

### Search Requirements
- Index status filters by status and date

### Documents
- None

### Reports
- Index sync status

### Notifications
- Optional alert to Super Administrator on repeated failures (F13-003)

### Security
- Index not publicly writable; queries go through the catalogue API

### Integrations
- Search engine (for example OpenSearch, Elasticsearch, Typesense or Algolia; confirmed at discovery)

### Dependencies
- F06-004
- F03-002
- F02-001
- F02-003
- F13-003

### Assumptions
- A dedicated search engine is used rather than plain database queries

### Risks
- Search engine choice depends on hosting; estimate assumes a mainstream engine

### Non Functional Requirements
- Published changes searchable within 1 minute; full re-index of 10,000 items under 15 minutes

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Search index status page | Medium | 6 |
| UI | Full re-index trigger dialog | Simple | 2 |
| API | Build index document for product or combination | Complex | 8 |
| API | Apply incremental index update on publication events | Complex | 8 |
| API | Re-index items affected by master or template change | Complex | 8 |
| API | Run full re-index job | Very High | 16 |
| API | Check index health | Easy | 4 |
| Database | Index sync queue and job log | Easy | 2 |
| Integration | Search engine service integration (schema, analysers, aliases) | Medium | 16 |
| Testing | Sync correctness for all publication events | Complex | 8 |
| Testing | Full re-index at 10,000 items | Medium | 6 |
| Documentation | Search index operations runbook | Easy | 2 |

**Feature Total: 86 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 44 | 2 | 16 | 14 | 2 | **86** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Full re-index is a Very High job API
- Search engine integration estimated as Medium (auth, mapping, retry)
