# F08-001 — CCTV Camera Onboarding and Health

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F08-001 |
| **Feature Name** | CCTV Camera Onboarding and Health |
| **Module** | 08 — CCTV Surveillance Monitoring |

### Description
Administrator registers godown CCTV cameras for CCC integration, monitors availability/recording health. Camera supply/install is out of scope.

### Business Objective
Known camera inventory with health for centralized monitoring.

### Actors
Maker: Surveillance Administrator. Checker: Surveillance Checker.

### User Journey
1. Who creates: Surveillance Administrator.
2. How they create: CCTV register → New: camera ID, godown, stream reference, Save draft.
3. How they edit: Draft/Returned editable.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker CCTV inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Camera history.
8. How the checker/auditor sees history: Same; operators see health dashboard.

### Functional Capabilities
- Camera onboarding
- Health/uptime
- Recording availability flag

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| CCTV camera register | Medium |
| CCTV camera form | Complex |
| Camera health dashboard | Complex |
| CCTV history | Medium |
| CCTV checker inbox | Medium |
| CCTV approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Register camera | Medium |
| Update camera | Medium |
| Query camera health | Complex |
| Submit camera | Complex |
| Approve camera | Complex |

### Inputs
Camera ID, godown, stream ref, health, recording status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Camera hardware, NVR and field networking out of hours.

### Validations
- Godown mandatory.
- Stream reference mandatory.

### Calculations
Uptime % for reports.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Camera uptime (Module 11).

### Notifications
Camera down → Module 09.

### Security
Surveillance Posts.

### Integrations
CCTV vendors ONVIF.

### Dependencies
F02-002, Module 12.

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
| CCTV camera register | UI | Medium | 6 |
| CCTV camera form | UI | Complex | 12 |
| Camera health dashboard | UI | Complex | 12 |
| CCTV history | UI | Medium | 6 |
| CCTV checker inbox | UI | Medium | 6 |
| CCTV approval | UI | Easy | 4 |
| Register camera | API | Medium | 6 |
| Update camera | API | Medium | 6 |
| Query camera health | API | Complex | 8 |
| Submit camera | API | Complex | 8 |
| Approve camera | API | Complex | 8 |
| CCTV camera master and health | DB | Complex | 6 |
| ONVIF / multi-vendor CCTV interface | Integration | Very High | 40 |
| CCTV Camera Onboarding and Health feature tests | Testing | Very High | 12 |
| CCTV Camera Onboarding and Health implementation documentation | Documentation | Complex | 4 |

**Feature total: 144 hours**
