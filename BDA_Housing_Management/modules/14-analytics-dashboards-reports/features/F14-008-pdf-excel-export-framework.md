# F14-008 — PDF & Excel Export Framework

## Section 1 — Feature Specification
| Field | Value |
|---|---|
| **Feature ID** | F14-008 |
| **Feature Name** | PDF & Excel Export Framework |
| **Module** | 14 — Analytics, Dashboards & Reports |

### Description
Provide controlled PDF and Excel export for authorized dashboards and packaged reports, with export status and audit history.
### Business Objective
Allow BDA users to share report outputs while retaining access control and traceability.
### Actors
- Authorized officers; Auditor; Citizen for own permitted exports
### User Journey
1. User opens an authorized dashboard/report. 2. User chooses PDF or Excel export. 3. BHMS generates the output with the active authorized filter context and records the export.
### Functional Capabilities
- Common format selection, export generation, asynchronous status, authorized retrieval, and export audit history.
### Inputs
- Permitted source report/dashboard, active filters, format selection, and requester identity.
### Outputs
- PDF/Excel output, completion status, and audit entry.
### Business Rules
- Exports contain only the requester’s permitted data and retain the filters used to generate them.
### Validations
- Export permission, supported format, data-volume thresholds, and source-view authorization.
### Calculations
- Source report totals are preserved in the generated output.
### Workflow
- Request export → generate → retrieve/download → audit.
### Search Requirements
- By user, source report, date, format, and export status.
### Documents
- Generated PDF/Excel outputs.
### Reports
- Export volume, success/failure, and download audit.
### Notifications
- Completion/failure notice through Module 12 where configured.
### Security
- RBAC, ownership isolation, protected downloaded files, and auditable access.
### Integrations
- Internal reporting sources; no external BI platform.
### Dependencies
- F14-001–F14-007 and Module 12.
### Assumptions
- PDF/Excel layouts are defined for packaged BHMS reports only.
### Risks
- Large result sets or unsupported formatting may require batch processing.
### Non Functional Requirements
- Expected-volume export performance, secure temporary files, and reproducible output.

---
## Section 2 — Estimation Breakdown (Estimation Master)
| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Export selection and history view | UI | Medium | 6 |
| PDF/Excel export operations | API | Very High | 16 |
| Export job and audit state | Database | Medium | 4 |
| Export framework tests | Testing | Very High | 12 |
| Export guide | Documentation | Complex | 4 |
| **Total** | | | **42** |

### Estimation Assumptions
- Estimation uses only Estimation Master values. Export API is Very High (16) for authorized PDF/Excel generation.
