# F02-003 — Document Type Master
## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F02-003 |
| **Feature Name** | Document Type Master |
| **Module** | 02 — Master Data & System Configuration |
### Description
Configure document types available within embedded layout, site, classification, and auction records.
### Business Objective
Standardise document labelling and mandatory-document controls without a standalone DMS.
### Actors
Super Administrator; section administrator; operational users (lookup).
### User Journey
Administrator creates and activates document types; operational feature users select permitted types while attaching files.
### Functional Capabilities
Document type CRUD, applicability/mandatory indicators as configured, activation control, search, export, audit.
### Inputs
Type name, code, applicable process, status, mandatory indicator.
### Outputs
Available document-type lookup and configuration export.
### Business Rules
Deactivated types remain on historical attachments; documents stay embedded in owning business records.
### Validations
Unique code; valid applicable process; active selection for new attachments.
### Calculations
None.
### Workflow
Direct configuration with audit.
### Search Requirements
Code, name, process applicability, status.
### Documents
This feature configures types only; it does not store business documents.
### Reports
Document-type configuration export.
### Notifications
Optional critical-type change notification.
### Security
Administrator-only changes and audit.
### Integrations
Internal document attachment consumption (Simple).
### Dependencies
Module 01; embedded document features in Modules 03–08.
### Assumptions
File storage and document handling remain embedded in business features.
### Risks
Incomplete applicability configuration may prevent required attachments.
### Non Functional Requirements
Reliable lookup availability; auditability.
---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---:|---:|
| Document-type register | UI | Medium | 6 |
| Document-type editor | UI | Medium | 6 |
| Document-type lifecycle operations | API | Medium | 6 |
| Document-type persistence | Database | Medium | 4 |
| Internal attachment lookup consumption | Integration | Simple | 4 |
| Configuration tests | Testing | Complex | 8 |
| Administration guide | Documentation | Medium | 3 |
| **Total** | | | **37** |
### Estimation Assumptions
No standalone document-management feature is created.
