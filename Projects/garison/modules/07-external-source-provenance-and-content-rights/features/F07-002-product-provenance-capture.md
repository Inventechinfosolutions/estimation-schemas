# F07-002 — Product Provenance Capture

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-002 |
| Feature Name | Product Provenance Capture |
| Module | 07 — External Source, Provenance & Content Rights |
| Module Type | Business |
| Release | Go-live |

### Description
Per-product provenance panel for externally referenced products: source (from register), source URL, source catalogue, original product code, source category, data usage status (Approved/Pending/Restricted), content rights status (Confirmed/To be confirmed), date verified, Garrison product status (Reference/Garrison/Other) and evidence notes, with status history and bulk update.

### Business Objective
Record exactly where each external profile came from and what Garrison may reproduce.

### Actors
- Catalogue Administrator
- Catalogue Reviewer (view)

### User Journey
1. **Who creates:** The Catalogue Administrator records provenance when creating or importing an external product.
2. **How they create:** In the Provenance tab they mark the product as External, select the source and enter the provenance fields; the import template can carry these fields (F12-001).
3. **How they edit:** They change rights or usage status through a dialog that requires an evidence note and date verified; bulk update applies to selected products.
4. **How they send for approval:** Provenance is submitted with the product; for external products complete provenance is mandatory before submission (F06-001).
5. **How the approver sees pending items:** Reviewers see provenance and rights status in the review workspace.
6. **How the approver decides:** Reviewers approve or request changes; rights gating at publish is enforced by F07-003.
7. **How the maker sees history:** The maker sees provenance status history.
8. **How the approver / auditor sees history:** Auditors see each status change with evidence note in the audit log.

### Functional Capabilities
- Provenance panel with all proposal fields
- Rights/usage status change with evidence note
- Status history
- Bulk provenance update for selected products
- Provenance completeness validation for external products

### UI Screens
- Provenance panel on product workspace
- Rights status change dialog with evidence note
- Provenance history
- Bulk provenance update

### Logical API Operations
- Save product provenance
- Change rights or usage status with evidence
- Get provenance history
- Bulk update provenance for selection
- Validate provenance completeness

### Inputs
- External flag, source, source URL, source catalogue, original code, source category, usage status, rights status, date verified, Garrison product status, evidence note

### Outputs
- Provenance record and status history used by the rights gate

### Business Rules
- Source and source reference are mandatory for external products
- Rights status change requires an evidence note
- Provenance is never shown publicly unless Garrison chooses to display source attribution

### Validations
- Source URL format
- Date verified not in the future

### Calculations
- Days since verification

### Workflow
Edited within product workflow; status changes recorded with history

### Search Requirements
- Register filters: source, usage status, rights status, verified before date

### Documents
- Evidence notes; agreements held at source level (F07-001)

### Reports
- External products by rights status (F07-003 dashboard)

### Notifications
- None

### Security
- Manage sources and rights permission; Reviewer view only

### Integrations
- None

### Dependencies
- F07-001
- F06-001
- F07-003
- F12-001

### Assumptions
- Garrison confirms rights; the platform records but does not verify legal status

### Risks
- Incorrect rights marking by users; evidence notes and audit mitigate

### Non Functional Requirements
- Provenance saved with product transactionally

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Provenance panel on product workspace | Complex | 12 |
| UI | Rights status change dialog with evidence note | Medium | 6 |
| UI | Provenance history | Easy | 4 |
| UI | Bulk provenance update | Medium | 6 |
| API | Save product provenance | Complex | 8 |
| API | Change rights or usage status with evidence | Medium | 6 |
| API | Get provenance history | Easy | 4 |
| API | Bulk update provenance for selection | Complex | 8 |
| API | Validate provenance completeness | Medium | 6 |
| Database | Product provenance | Medium | 4 |
| Database | Provenance status history | Easy | 2 |
| Testing | Provenance mandatory for external products | Medium | 6 |
| Testing | Status change audit and history | Easy | 4 |
| Testing | Bulk provenance update | Easy | 4 |
| Documentation | Provenance capture guide with examples | Easy | 2 |

**Feature Total: 82 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 28 | 32 | 6 | 0 | 14 | 2 | **82** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Bulk update and evidence-driven status changes drive Complex rows
- No external integration channel in this feature; Integration row omitted.
