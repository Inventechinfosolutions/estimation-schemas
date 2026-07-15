# F04-003 — Unit Documents & Media

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F04-003 |
| **Feature Name** | Unit Documents & Media |
| **Module** | 04 — Flats & Villas Inventory & Status |

### Description
Embed floor plans, images, drawings, brochures, and supporting files within each Flat or Villa record.

### Business Objective
Provide authorised users and publication processes with complete unit evidence and marketing information.

### Actors
Engineering Section; Housing officers; Approvers; Auditor.

### User Journey
Officer opens a unit, uploads/classifies a file, replaces it when necessary, and retrieves the current or prior file through the unit record.

### Functional Capabilities
Upload/list/preview/download; classify; replace/version; secure retrieval; document history.

### Inputs
Unit reference, file, type, title, description, replacement reason.

### Outputs
Unit document/media set and retrieval links.

### Business Rules
Files belong to the unit; only authorised users may alter them; published-content changes follow configured controls.

### Validations
Supported type/size; required type; valid unit; classification required.

### Calculations
None.

### Workflow
Upload/replace → history recorded → files are available to authorised unit and publication views.

### Search Requirements
Project, unit, type, title, uploader, date, current/superseded status.

### Documents
Floor plans, images, drawings, brochures, supporting files.

### Reports
Unit Document Register export.

### Notifications
Optional notice on replacement of published unit material.

### Security
Document ACL, secure access, upload/download audit.

### Integrations
Internal document storage handoff (Simple).

### Dependencies
F04-001; F04-005; F02-002.

### Assumptions
Standalone DMS and physical scanning are excluded.

### Risks
Misclassified or obsolete files may be exposed in public material.

### Non Functional Requirements
Reliable retrieval; file-size controls; version history.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Unit document list and filters | UI | Medium | 6 |
| Unit upload/replace panel | UI | Complex | 8 |
| Unit document operations | API | Complex | 8 |
| Unit document metadata persistence | Database | Medium | 4 |
| Document storage handoff | Integration | Simple | 4 |
| Unit document tests | Testing | Complex | 8 |
| Unit document guide | Documentation | Easy | 2 |
| **Total** | | | **40** |

### Estimation Assumptions
- The estimate uses Estimation Master complexity values only.
- Documents and approval workflow actions are included within this owning feature where applicable.
