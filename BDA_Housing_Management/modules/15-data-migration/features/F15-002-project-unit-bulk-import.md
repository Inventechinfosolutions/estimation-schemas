# F15-002 — Project & Unit Bulk Import

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F15-002 |
| **Feature Name** | Project & Unit Bulk Import |
| **Module** | 15 — Data Migration |

### Description
Import agreed legacy housing projects and flat/villa units, preserving required relationships, financial values, documents metadata references where supplied, and lifecycle status.
### Business Objective
Establish reliable housing inventory in BHMS before go-live.
### Actors
- Vendor migration team; BDA Engineering/data owners
### User Journey
1. Approved project/unit batch is selected. 2. BHMS validates relationships and imports eligible records. 3. Exceptions are resolved and the batch result is retained.
### Functional Capabilities
- Project and unit import, relationship validation, batch control, duplicate prevention, status mapping, and exception handling.
### Inputs
- Validated project/unit extract, source identifiers, reference mappings, pricing/status values.
### Outputs
- Imported project/unit records, batch counts, and exception list.
### Business Rules
- Only agreed project/unit attributes and supported statuses are imported; records failing validation are excluded from final load pending resolution.
### Validations
- Required references, unique identifiers, project-unit relationships, valid financial/status values, and duplicate source keys.
### Calculations
- Imported/rejected counts and source-target totals.
### Workflow
- Validated batch → import → exception resolution → reconcile.
### Search Requirements
- By batch, project, unit, source identifier, status, and exception.
### Documents
- Source extract and batch outcome evidence.
### Reports
- Project/unit migration result and exception register.
### Notifications
- Batch completion/failure alerts through Module 12 where configured.
### Security
- Restricted migration roles, protected attachments, and auditable batch actions.
### Integrations
- Internal BHMS migration capabilities.
### Dependencies
- Modules 03–04; F15-001 and F15-005.
### Assumptions
- BDA provides agreed identifiers, reference mappings, and status interpretation.
### Risks
- Ambiguous legacy project/unit codes can delay imports.
### Non Functional Requirements
- Restartable batch processing, data integrity, and expected-volume performance.

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
- Estimation uses only Estimation Master values. BDA provides agreed identifiers, reference mappings, and status interpretation.
