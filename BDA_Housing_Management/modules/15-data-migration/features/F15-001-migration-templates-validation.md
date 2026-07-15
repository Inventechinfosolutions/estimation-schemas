# F15-001 — Migration Templates & Validation

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F15-001 |
| **Feature Name** | Migration Templates & Validation |
| **Module** | 15 — Data Migration |

### Description
Provide agreed migration templates and validation controls for legacy project, unit, booking, and applicant extracts.
### Business Objective
Make supplied legacy data fit for controlled trial and final import.
### Actors
- Vendor migration team; BDA data owners; Super Administrator
### User Journey
1. BDA obtains the agreed template. 2. Data is prepared and validated. 3. Exceptions are reviewed before import.
### Functional Capabilities
- Templates, field-level validation, exception register, correction/revalidation cycle, and import-readiness status.
### Inputs
- Completed extracts, agreed field mappings, validation settings, and data-owner comments.
### Outputs
- Validation result, exception register, and import-ready batch.
### Business Rules
- Only agreed datasets and supplied source values are migrated; missing history is not reconstructed.
### Validations
- Template version, mandatory fields, reference values, duplicates, and data-format rules.
### Calculations
- Record/error counts and validation summary.
### Workflow
- Prepare template → upload/validate → resolve exceptions → approve import readiness.
### Search Requirements
- By dataset, batch, field, exception type, source value, and status.
### Documents
- BDA source extracts and exception evidence.
### Reports
- Validation and exception register.
### Notifications
- Readiness/exception alerts through Module 12 where configured.
### Security
- Role-limited migration access, protected personal data, and traceable corrections.
### Integrations
- Internal BHMS migration capabilities.
### Dependencies
- Internal target-module reference data.
### Assumptions
- Modules 02–11; BDA data owners; F15-002–F15-005.
### Risks
- BDA supplies cleanable extracts and timely business decisions.
### Non Functional Requirements
- Poor source data can expand exception-cleansing effort.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Migration template and validation workspace | UI | Very High | 16 |
| Validation and exception operations | API | Very High | 16 |
| Template, run, and exception state | Database | Complex | 6 |
| Template/validation tests | Testing | Very High | 12 |
| Migration template guide | Documentation | Very High | 6 |
| **Total** | | | **56** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. [('Migration template and validation workspace', 'UI', 'Very High', 16), ('Validation and exception operations', 'API', 'Very High', 16), ('Template, run, and exception state', 'Database', 'Complex', 6), ('Template/validation tests', 'Testing', 'Very High', 12), ('Migration template guide', 'Documentation', 'Very High', 6)]
