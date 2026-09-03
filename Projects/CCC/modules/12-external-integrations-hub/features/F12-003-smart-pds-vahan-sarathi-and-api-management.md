# F12-003 — SMART-PDS Vahan Sarathi and API Management

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-003 |
| **Feature Name** | SMART-PDS Vahan Sarathi and API Management |
| **Module** | 12 — External Integrations Hub |

### Description
API management hooks for SMART-PDS and external APIs such as Vahan, Sarathi and other identified departmental systems.

### Business Objective
Interoperate with existing and future FCS digital platforms.

### Actors
Maker: Integration Administrator. Checker: Integration Checker. Department confirms field maps.

### User Journey
1. Who creates: Integration Administrator.
2. How they create: API hub → New consumer/provider: system (SMART-PDS/Vahan/Sarathi/other), operations, auth, Save draft, Test.
3. How they edit: Draft editable; live change new version.
4. How they send for approval: Submit to checker / Department acknowledge.
5. How the approver sees pending items: Checker API inbox.
6. How the approver decides: Approve go-live of API mapping.
7. How the maker sees history: API call and mapping history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- API catalogue
- SMART-PDS hooks
- Vahan/Sarathi hooks
- Test and audit of calls

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| API catalogue | Complex |
| API mapping form | Very High |
| API test console | Complex |
| API call log | Medium |
| API checker inbox | Medium |
| API approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Invoke SMART-PDS exchange | Very High |
| Invoke Vahan lookup | Complex |
| Invoke Sarathi lookup | Complex |
| Submit API mapping | Complex |
| Approve API mapping | Complex |

### Inputs
System, operation, auth, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Exact operations confirmed during requirement study.

### Validations
- System and operation mandatory.

### Calculations
Success/fail counts.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Interface catalogue.

### Reports
API success.

### Notifications
Fail alerts.

### Security
Integration admin; secrets protected.

### Integrations
SMART-PDS, Vahan, Sarathi.

### Dependencies
Module 01; vehicle master for lookups.

### Assumptions
- Hours use Estimation Master values; each named screen and logical API is billed independently.
- GPS/CCTV/RFID/ANPR field hardware supply and install are out of application-software hours unless stated otherwise.
- Hosting is on KSDC; KSDC consumption INR and AMC/O&M person-months are out of this estimate per confirmed scope.

### Risks
Incomplete vendor API documentation for VLTS, CCTV, SMART-PDS, Vahan or Sarathi would delay integration features.

### Non Functional Requirements
Screens remain usable under concurrent State CCC load; privileged actions are attributable to Person + Post.

## Section 2 — Estimation Breakdown

| Artefact | Category | Complexity | Hours |
|---|---|---|---:|
| API catalogue | UI | Complex | 12 |
| API mapping form | UI | Very High | 16 |
| API test console | UI | Complex | 12 |
| API call log | UI | Medium | 6 |
| API checker inbox | UI | Medium | 6 |
| API approval | UI | Easy | 4 |
| Invoke SMART-PDS exchange | API | Very High | 16 |
| Invoke Vahan lookup | API | Complex | 8 |
| Invoke Sarathi lookup | API | Complex | 8 |
| Submit API mapping | API | Complex | 8 |
| Approve API mapping | API | Complex | 8 |
| API mappings and call log | DB | Complex | 6 |
| SMART-PDS, Vahan, Sarathi and other FCS APIs | Integration | Very High | 40 |
| SMART-PDS Vahan Sarathi and API Management feature tests | Testing | Very High | 12 |
| SMART-PDS Vahan Sarathi and API Management implementation documentation | Documentation | Complex | 4 |

**Feature total: 166 hours**
