# F02-002 — Vendor / agency master

## Feature Specification

| Field | Value |
|---|---|
| Feature ID | F02-002 |
| Feature Name | Vendor / agency master |
| Module | 02 — Master Data & System Configuration |
| Description | Maintain vendor/agency profiles used in campaign assignment and vendor user linkage. |
| Business Objective | Give DIPR a single register of agencies executing print, digital, and outdoor work with contact and compliance attributes. |
| Actors | DIPR Administrator; Campaign Officer (read/search) |

### User Journey

- Administrator opens Vendor register → searches agency → creates profile with contacts and service channels → links vendor users (F01-001) → Campaign Officer selects vendor on campaign assignment (F03-005).

### Functional Capabilities

- Vendor register with search (name, code, channel capability, status)
- Profile form: legal name, trade name, contacts, address, GST/tax ID as applicable, supported media channels
- Activate/deactivate vendor; block new assignments when inactive
- View campaigns currently assigned to vendor (read-only link)

### Inputs

- Vendor code, names, contacts, channel capabilities, tax identifiers, status

### Outputs

- Vendor master record; filtered lists for campaign UI

### Business Rules

- Inactive vendors cannot be newly assigned to campaigns
- Vendor user accounts must reference active vendor

### Validations

- Unique vendor code; mandatory name and primary contact

### Calculations

- None

### Workflow

- Register → Active → Inactive

### Search Requirements

- Name, code, channel, status

### Documents

- Optional attachment slot for registration certificate (metadata only)

### Reports

- None

### Notifications

- None

### Security

- Administrator write; campaign roles read per permission matrix

### Integrations

- None

### Dependencies

- F01-001 for vendor users

### Assumptions

- Payment to vendors outside AMT unless later scope added

### Risks

- Incomplete vendor channel flags cause wrong assignment options

### Non Functional Requirements

- Register supports DIPR’s expected agency count with pagination

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|---|---|---|---:|
| UI | Vendor/agency register with search and pagination | Easy | 4 |
| UI | Vendor profile form (contacts, GST, channels) | Medium | 6 |
| UI | Outdoor/print/digital capability toggles panel | Medium | 6 |
| UI | Vendor document attachment slot list | Easy | 4 |
| UI | Deactivate vendor confirmation with campaign warning | Simple | 2 |
| UI | Vendor quick-view drawer from register | Easy | 4 |
| API | List vendors with filters and pagination | Medium | 6 |
| API | Get vendor profile by id | Simple | 2 |
| API | Create vendor profile | Medium | 6 |
| API | Update vendor profile | Medium | 6 |
| API | Deactivate vendor with assignment eligibility check | Medium | 6 |
| API | Vendor autocomplete for campaign assignment | Easy | 4 |
| Database | Vendor profile entity | Easy | 2 |
| Database | Vendor channel capability flags | Simple | 1 |
| Database | Vendor contact child records | Easy | 2 |
| Database | Active campaign assignment guard index | Easy | 2 |
| Testing | Inactive vendor blocked on campaign assignment | Medium | 6 |
| Testing | Mandatory fields and GST format validation | Easy | 4 |
| Testing | Deactivate vendor with open campaigns | Medium | 6 |
| Documentation | Vendor master administration notes | Easy | 2 |
| Documentation | UAT vendor onboarding script | Easy | 2 |

**Feature Total: 83 hours**

### Estimation Assumptions

- Vendor performance scoring is out of scope; history lives on campaign assignment feature.
