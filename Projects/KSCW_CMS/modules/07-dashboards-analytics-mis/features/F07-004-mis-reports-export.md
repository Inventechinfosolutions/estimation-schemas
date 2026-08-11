# F07-004 — MIS Reports & Export

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F07-004 |
| Feature Name | MIS Reports & Export |
| Module | 07 — Dashboards, Analytics, Real-time Monitoring & MIS |
| Description | Standard MIS reports with export (e.g. Excel/PDF as FRS defines). |
| Business Objective | Satisfy statutory/management reporting needs. |
| Actors | Admin; Supervisor |

### User Journey

- User selects MIS report → sets parameters → runs report → exports file.

### Functional Capabilities

- Standard MIS report catalogue
- Parameterised run
- Export download

### Inputs

- Report type
- Date/location/category parameters

### Outputs

- On-screen report
- Exported file

### Business Rules

- Catalogue fixed to approved MIS list

### Validations

- Required parameters

### Calculations

- Report-specific aggregates

### Workflow

- Select → parameterize → generate → export

### Search Requirements

- N/A beyond parameters

### Documents

- Exported MIS files

### Reports

- MIS report set

### Notifications

- None

### Security

- Role-gated reports; audit export if required

### Integrations

- None

### Dependencies

- Modules 03–05

### Assumptions

- Report list approved before build

### Risks

- Late new report types expand hours

### Non Functional Requirements

- Exports complete within acceptable time for typical ranges

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | MIS report catalogue, parameter form, and download | Complex | 8 |
| API | Report generation and export (Excel/PDF) | Very High | 16 |
| Database | Report query support / indexes | Medium | 4 |
| Testing | Report parameter and export cases | Complex | 8 |
| Documentation | MIS reports notes | Medium | 3 |

**Feature Total: 39 hours**

### Estimation Assumptions

- Hours from Estimation Master only.
- Enterprise-grade validation, error handling, logging, and security included.
- No separate API/DB design artefacts in this estimate beyond logical effort.
- Delivery services (training, CERT-In/Safe-to-Host, warranty operations) are excluded from feature hours.
