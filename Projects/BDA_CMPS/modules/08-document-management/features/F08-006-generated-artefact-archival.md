# F08-006 — Generated Artefact Archival

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F08-006 |
| **Feature Name** | Generated Artefact Archival |
| **Module** | 08 — Document Management |

### Description
Archive system-generated notice PDFs and digital receipts (and similar artefacts) produced by business modules and Notification flows, with linkage back to source transactions (supports M7-AC3 archive aspect).

### Business Objective
Ensure notices and receipts remain retrievable for audit, disputes, and tenant downloads.

### Actors
- System (ingest), Officers, Auditors, Tenants (download via ACL)

### User Journey
1. Module 04/05/06/09 generates notice/receipt PDF.
2. Calls DMS archive ingest with category, entity links, source ids.
3. Artefact appears on lease/tenant/payment document lists and search.

### Functional Capabilities
- Ingest API for generated PDFs/files
- Categories: Notice, Receipt, Possession Certificate (generated), Demand PDF, etc.
- Link to source entity ids (notice id, payment id, lease id)
- Browse archived notices/receipts
- Idempotent ingest (no duplicate archives for same source)

### Inputs
- File stream/bytes, category, source refs, entity links, generated timestamp

### Outputs
- Archived document records

### Business Rules
- Batch overdue notices are archived after generation (M7-AC3 archive portion)—generation cohort logic remains in business modules.
- SMS/email transport is Module 09—not duplicated here.
- Template management is Module 02.

### Validations
- Source type/id required; ACL category valid
- Idempotency key unique

### Calculations
None.

### Workflow
N/A.

### Search Requirements
Filter generated artefacts by source type/date (uses F08-004).

### Documents
N/A.

### Reports
Archived notices/receipts counts by period.

### Notifications
None.

### Security
Same ACL model; system ingest service account constrained.

### Integrations
Internal producers (Modules 04–07, 09)—Simple/internal within Complex API package.

### Dependencies
F08-001–004; notice/receipt producers; Module 09 handoff

### Assumptions
- Does not implement batch notice selection (Module 05/04/06).
- M7-AC3 generation correctness owned by business modules; this guarantees archive persistence.

### Risks
- Producers forgetting to archive — provide shared client helper and tests.

### Non Functional Requirements
- High-volume ingest during notice batches; async acceptable

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Archived notices/receipts browser | UI | Medium | 6 |
| Artefact archive ingest APIs | API | Complex | 8 |
| Generated artefact metadata | Database | Medium | 4 |
| Archive ingest tests | Testing | Complex | 8 |
| Generated artefact archive guide | Documentation | Easy | 2 |
| **Total** | | | **28** |

### Estimation Assumptions
- PDF generation itself estimated in producing modules / templates.
