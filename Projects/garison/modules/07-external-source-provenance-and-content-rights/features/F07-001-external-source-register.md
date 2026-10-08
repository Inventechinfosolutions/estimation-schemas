# F07-001 — External Source Register

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F07-001 |
| Feature Name | External Source Register |
| Module | 07 — External Source, Provenance & Content Rights |
| Module Type | Business |
| Release | Go-live |

### Description
Master of external reference sources (for example Brenlo and other approved industry catalogues): source name, website URL, catalogue/series, contact, default data usage status, default rights position, rights agreement documents and notes.

### Business Objective
Track which external sources Garrison uses and on what terms, as the basis for per-product provenance.

### Actors
- Catalogue Administrator
- Super Administrator
- Catalogue Reviewer (view)

### User Journey
1. **Who creates:** The Catalogue Administrator registers external sources.
2. **How they create:** They add a source with name, URL, catalogue/series, contact, default usage (Approved/Pending/Restricted), default rights (Confirmed/To be confirmed) and upload any rights agreement or permission email.
3. **How they edit:** They edit source details and defaults or retire a source; changing defaults does not alter existing products automatically.
4. **How they send for approval:** No approval is required to register a source; Garrison's decision to include profiles is recorded per product (F07-002).
5. **How the approver sees pending items:** There is no approver inbox; reviewers can view the register.
6. **How the approver decides:** No decision applies on this feature.
7. **How the maker sees history:** The administrator sees the source's change history and linked product counts.
8. **How the approver / auditor sees history:** Auditors see source changes and agreement uploads in the audit log.

### Functional Capabilities
- Source register with linked product counts by rights status
- Source form with defaults and notes
- Rights agreement / permission evidence upload
- Retire source

### UI Screens
- External source register
- Source create / edit form
- Source detail with linked products

### Logical API Operations
- List sources
- Create or update source
- Get source with linked product counts
- Upload rights agreement document
- Retire source

### Inputs
- Name, URL, catalogue/series, contact, default usage, default rights, agreement files, notes

### Outputs
- Source records referenced by product provenance

### Business Rules
- Source name unique
- Retired sources cannot be selected for new products

### Validations
- URL format
- Agreement files PDF/image/email export max 10 MB

### Calculations
- Linked product counts by status

### Workflow
Active ↔ Retired

### Search Requirements
- Name, status

### Documents
- Rights agreements and permission evidence

### Reports
- Sources with linked product and rights counts

### Notifications
- None

### Security
- Manage sources permission; Reviewer view only

### Integrations
- None (no automated scraping of external sites)

### Dependencies
- F07-002

### Assumptions
- Sources are maintained manually; no automated data extraction from external websites

### Risks
- None significant

### Non Functional Requirements
- Register loads instantly (small data set)

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | External source register | Easy | 4 |
| UI | Source create / edit form | Medium | 6 |
| UI | Source detail with linked products | Medium | 6 |
| API | List sources | Simple | 2 |
| API | Create or update source | Medium | 6 |
| API | Get source with linked product counts | Medium | 6 |
| API | Upload rights agreement document | Easy | 4 |
| API | Retire source | Easy | 4 |
| Database | Source master and agreement documents | Easy | 2 |
| Testing | Source maintenance and product linkage | Easy | 4 |
| Documentation | Source register guide | Simple | 1 |

**Feature Total: 45 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 22 | 2 | 0 | 4 | 1 | **45** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, security checks and unit tests included in each row.
- Small master with document upload
- No external integration channel in this feature; Integration row omitted.
