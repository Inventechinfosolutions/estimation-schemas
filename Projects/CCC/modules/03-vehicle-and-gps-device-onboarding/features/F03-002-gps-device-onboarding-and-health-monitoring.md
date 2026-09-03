# F03-002 — GPS Device Onboarding and Health Monitoring

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | GPS Device Onboarding and Health Monitoring |
| **Module** | 03 — Vehicle and GPS Device Onboarding |

### Description
Administrator onboards GPS devices, maps them to vehicles, tracks warranty/AMC of devices, and monitors device health/status. Device supply is out of scope.

### Business Objective
Valid GPS device mapping for VLTS integration.

### Actors
Maker: Fleet/Device Administrator. Checker: Fleet Checker.

### User Journey
1. Who creates: Device Administrator.
2. How they create: Device register → New: device ID, vendor, AIS-140 attributes, map to vehicle, warranty/AMC dates, Save draft.
3. How they edit: Draft/Returned editable. Remap requires submit.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker device inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Device mapping history.
8. How the checker/auditor sees history: Same; health dashboard for operators.

### Functional Capabilities
- Device onboarding
- Vehicle mapping
- Warranty/AMC tracking
- Health/status monitoring

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Device register | Medium |
| Device mapping form | Complex |
| Device health panel | Complex |
| Device history | Medium |
| Device checker inbox | Medium |
| Device approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create device | Medium |
| Map device to vehicle | Complex |
| Search device | Medium |
| Read device health | Medium |
| Submit device change | Complex |
| Approve device | Complex |

### Inputs
Device ID, vendor, vehicle, warranty/AMC, health status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- One active device mapping per vehicle unless Department allows dual.
- Hardware supply not in this feature.

### Validations
- Device ID unique.
- Vehicle must be approved.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
None.

### Reports
Device health and warranty due.

### Notifications
Device offline alerts via Module 09.

### Security
Fleet Posts.

### Integrations
VLTS vendor identity.

### Dependencies
F03-001, Module 12.

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
| Device register | UI | Medium | 6 |
| Device mapping form | UI | Complex | 12 |
| Device health panel | UI | Complex | 12 |
| Device history | UI | Medium | 6 |
| Device checker inbox | UI | Medium | 6 |
| Device approval | UI | Easy | 4 |
| Create device | API | Medium | 6 |
| Map device to vehicle | API | Complex | 8 |
| Search device | API | Medium | 6 |
| Read device health | API | Medium | 6 |
| Submit device change | API | Complex | 8 |
| Approve device | API | Complex | 8 |
| Device and mapping history | DB | Complex | 6 |
| AIS-140 / VLTS device identity handshake | Integration | Medium | 16 |
| GPS Device Onboarding and Health Monitoring feature tests | Testing | Very High | 12 |
| GPS Device Onboarding and Health Monitoring implementation documentation | Documentation | Medium | 3 |

**Feature total: 125 hours**
