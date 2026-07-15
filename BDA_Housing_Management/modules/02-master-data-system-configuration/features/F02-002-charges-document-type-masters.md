# F02-002 — Charges & Document Type Masters

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F02-002 |
| **Feature Name** | Charges & Document Type Masters |
| **Module** | 02 — Master Data & System Configuration |

### Description
Maintain charge heads, payment lookup values, and document-type requirements used in housing processes.

### Business Objective
Standardise financial components and document capture across BHMS.

### Actors
Super Administrator; Accounts administrator; section administrator; Auditor.

### User Journey
Administrator configures a charge or document type, sets applicability/status, and authorised forms consume the active configuration.

### Functional Capabilities
Charge master; payment lookup master; document type and required/optional classification; activate/deactivate; export.

### Inputs
Charge name, applicability, amount basis/reference, document type, requirement flag, status.

### Outputs
Active charge/document configurations and registers.

### Business Rules
Only active configurations may be selected for new records; document requirements are applied by owning business process.

### Validations
Unique active codes; valid applicability; no deactivation when prohibited by policy.

### Calculations
None.

### Workflow
Direct maintenance with audit.

### Search Requirements
Configuration type, code, applicability, status.

### Documents
None.

### Reports
Charges Master and Document Type Register exports.

### Notifications
None by default.

### Security
Role-restricted configuration; audit changes.

### Integrations
None.

### Dependencies
Module 01; F02-001.

### Assumptions
Payment computation and transactional document upload are owned by later modules.

### Risks
Incorrect configuration can cause incomplete documentation or incorrect charge display.

### Non Functional Requirements
Fast lookup response; traceable configuration history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Charges and document-type register | UI | Complex | 8 |
| Charge/document-type editor | UI | Complex | 8 |
| Configuration maintenance operations | API | Complex | 8 |
| Charges and document-type persistence | Database | Complex | 6 |
| Configuration tests | Testing | Complex | 8 |
| Configuration guide | Documentation | Medium | 3 |
| **Total** | | | **41** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
