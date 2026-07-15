# F15-003 — Booking & Applicant Bulk Import

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F15-003 |
| **Feature Name** | Booking & Applicant Bulk Import |
| **Module** | 15 — Data Migration |

### Description
Import available legacy applicant and booking records, linking them to migrated projects/units where reliable identifiers exist.
### Business Objective
Preserve agreed active housing commitments and citizen records for operational continuity.
### Actors
- Vendor migration team; BDA Housing/data owners
### User Journey
1. Approved applicant/booking data is validated against migrated inventory. 2. Eligible records are imported and linked. 3. Exceptions and unresolved links are recorded for BDA decision.
### Functional Capabilities
- Applicant/booking import, identity and ownership checks, project/unit linking, status mapping, batch controls, and exceptions.
### Inputs
- Validated applicant/booking extract, source references, mapped project/unit keys, and available payment/status data.
### Outputs
- Imported applicant/booking records, linkage result, counts, and exception register.
### Business Rules
- Only records with sufficient BDA-approved linkage and status data are imported; unavailable history is not reconstructed.
### Validations
- Required applicant fields, valid project/unit linkage, duplicate identity/source keys, and allowed booking statuses.
### Calculations
- Imported/rejected/unlinked counts and source-target reconciliation totals.
### Workflow
- Validated batch → link/import → exception resolution → reconcile.
### Search Requirements
- By batch, applicant, booking, project/unit, status, and exception.
### Documents
- Source extracts and migration evidence; no physical scanning.
### Reports
- Applicant/booking migration and unresolved-link report.
### Notifications
- Batch completion/failure alerts through Module 12 where configured.
### Security
- Restricted access to personal data, citizen ownership protection, and audit history.
### Integrations
- Internal BHMS migration capabilities.
### Dependencies
- Modules 06–08; F15-001, F15-002, and F15-005.
### Assumptions
- BDA confirms which legacy applicant fields and booking statuses are authoritative.
### Risks
- Incomplete citizen or booking linkage can require manual remediation.
### Non Functional Requirements
- Restartable import, privacy protection, and clear reconciliation evidence.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Bulk-import mapping and exception workspace | UI | Very High | 16 |
| Import and validation operations | API | Very High | 16 |
| Import batch and exception state | Database | Complex | 6 |
| Bulk-import tests | Testing | Very High | 12 |
| Bulk-import guide | Documentation | Very High | 6 |
| **Total** | | | **56** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. BDA confirms which legacy applicant fields and booking statuses are authoritative.
