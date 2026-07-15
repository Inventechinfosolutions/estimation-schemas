# F08-001 — Document Repository Upload & Linkage

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F08-001 |
| **Feature Name** | Document Repository Upload & Linkage |
| **Module** | 08 — Document Management |

### Description
Provide a central document repository to upload, classify/tag, and link documents to property, tenant, lease, vendor, complaint, and other entities across categories such as lease, possession, plans, tax receipts, utility bills, insurance, NOC, photos, KYC, vendor agreements, completion certificates, and legal supporting docs (M7-AC1).

### Business Objective
Create a single authoritative store for operational and compliance artefacts used throughout CPMS.

### Actors
- All officer roles (as permitted), Super Administrator, Auditor (read), Tenant (via linked own docs in later feature)

### User Journey
1. User opens entity (e.g., lease) Documents panel or central repository.
2. Uploads file, selects category/tags, links entity refs.
3. Document becomes available for preview/download per ACL (F08-003).

### Functional Capabilities
- Upload with category and tags
- Multi-entity linkage (property/tenant/lease/vendor/complaint/etc.)
- Reusable entity document panel for consuming modules
- Central repository browser
- Replace metadata without breaking links
- File type/size policy enforcement

### Inputs
- File binary, category, tags, entity links, title/remarks

### Outputs
- Stored document metadata + blob reference
- Linked document lists on entities

### Business Rules
- Every lease and property can store multiple categorized documents (M7-AC1)—versioning in F08-002.
- Legacy physical scanning services out of scope (accept uploads of scans).
- DigiLocker connector out of scope (optional Module 10).
- Business modules own when to prompt upload; this module owns storage/link APIs.

### Validations
- Allowed MIME/extensions; max size; mandatory category
- At least one entity link for business docs (configurable)

### Calculations
None.

### Workflow
N/A (direct upload with audit). Optional approval for certain categories (configurable light hook).

### Search Requirements
Basic filters in browser; advanced search in F08-004.

### Documents
N/A (this is the document system).

### Reports
Document inventory export (basic).

### Notifications
Optional upload failure alerts to admin.

### Security
Auth required; virus/malware scan hook if platform provides; audit upload actor/time.

### Integrations
None external baseline (object storage is infrastructure, not Integration Master GIS/ERP tier).

### Dependencies
Module 01 RBAC; consumed by Modules 03–07, 11

### Assumptions
- Object storage (S3/compatible or equivalent) available in hosting.
- Virus scanning if required is platform service—integration light.
- Testing Very High due to cross-entity linkage matrix.

### Risks
- Unbounded storage growth — retention (F08-005) and quotas needed.
- Double storage if modules also keep local copies — enforce DMS-only pattern.

### Non Functional Requirements
- Reliable upload for typical office PDFs/images; resumable nice-to-have not baseline
- English UI

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Document repository browser | UI | Complex | 8 |
| Upload / classify / link dialog | UI | Complex | 8 |
| Entity document panel (reusable) | UI | Medium | 6 |
| Upload store classify link ops | API | Complex | 8 |
| Document metadata & linkage schema | Database | Complex | 6 |
| Repository core tests | Testing | Very High | 12 |
| Document repository guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Shared panel reused by other modules; those modules estimate only thin consumption.
