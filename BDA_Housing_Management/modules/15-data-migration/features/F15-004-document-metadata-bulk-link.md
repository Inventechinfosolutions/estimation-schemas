# F15-004 — Document Metadata Bulk Link

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F15-004 |
| **Feature Name** | Document Metadata Bulk Link |
| **Module** | 15 — Data Migration |

### Description
Bulk-link supplied digital document metadata to migrated projects, units, applicants, bookings, and other agreed BHMS records.
### Business Objective
Make available digital evidence discoverable from the correct migrated housing record without physical scanning.
### Actors
- Vendor migration team; BDA data owners; authorized officers
### User Journey
1. BDA supplies digital files and agreed metadata. 2. BHMS validates target references and links eligible documents. 3. Unmatched files are listed for resolution.
### Functional Capabilities
- Metadata intake, target matching, link creation, duplicate/exception handling, and batch evidence.
### Inputs
- File location/reference, document type, target source identifier, metadata, and batch reference.
### Outputs
- Linked-document outcome, unmatched/duplicate exceptions, and batch history.
### Business Rules
- Physical scanning is excluded; only supplied digital files with usable metadata are linked.
### Validations
- Document type, supported file/reference, valid target identifier, duplicate link, and access eligibility.
### Calculations
- Linked/unmatched/duplicate counts.
### Workflow
- Validate metadata → match target → link → review exceptions → reconcile.
### Search Requirements
- By batch, document type, target reference, file reference, and match status.
### Documents
- Supplied digital documents and metadata evidence.
### Reports
- Document-link migration and unmatched-file register.
### Notifications
- Batch completion/failure alerts through Module 12 where configured.
### Security
- Role-limited file access, target-record permissions, and audit of linking actions.
### Integrations
- Internal BHMS migration capabilities.
### Dependencies
- Target Modules 03–11; F15-001 and F15-005.
### Assumptions
- BDA provides accessible digital files and a stable metadata convention.
### Risks
- Incomplete or inconsistent metadata can cause unmatched documents.
### Non Functional Requirements
- Integrity verification, protected document access, and restartable batch processing.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Document-link import and exception workspace | UI | Complex | 8 |
| Metadata matching and bulk-link operations | API | Very High | 16 |
| Link outcome and exception state | Database | Complex | 6 |
| Document-link import tests | Testing | Very High | 12 |
| Document-link guide | Documentation | Complex | 4 |
| **Total** | | | **46** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. BDA provides accessible digital files and a stable metadata convention.
