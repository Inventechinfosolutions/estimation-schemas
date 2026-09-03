# F12-002 — CCTV ONVIF and Multi-vendor Video Integration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-002 |
| **Feature Name** | CCTV ONVIF and Multi-vendor Video Integration |
| **Module** | 12 — External Integrations Hub |

### Description
Configure multi-vendor CCTV/ONVIF connections for live and playback into CCC. Camera hardware out of scope.

### Business Objective
Centralized video access across godown CCTV systems.

### Actors
Maker: Integration Administrator. Checker: Integration Checker.

### User Journey
1. Who creates: Integration Administrator.
2. How they create: CCTV integration → New site/vendor connection, protocol ONVIF/other, Save draft, Test.
3. How they edit: Draft editable; live change new version.
4. How they send for approval: Submit to checker.
5. How the approver sees pending items: Checker inbox.
6. How the approver decides: Approve or reject.
7. How the maker sees history: Connection and test history.
8. How the checker/auditor sees history: Same.

### Functional Capabilities
- ONVIF/multi-vendor
- Connection test
- Site binding

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| CCTV connection form | Complex |
| Connection test panel | Medium |
| Connection checker inbox | Medium |
| Connection approval | Easy |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Register CCTV connection | Complex |
| Test ONVIF connection | Very High |
| Submit connection | Complex |
| Approve connection | Complex |

### Inputs
Vendor, site, protocol, credentials ref, status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- Camera supply/install/NVR out of scope.

### Validations
- Site and protocol mandatory.

### Calculations
None.

### Workflow
Maker–checker.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Interface note.

### Reports
Connection health.

### Notifications
Connection fail alert.

### Security
Integration admin.

### Integrations
CCTV vendors.

### Dependencies
F08-001.

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
| CCTV connection form | UI | Complex | 12 |
| Connection test panel | UI | Medium | 6 |
| Connection checker inbox | UI | Medium | 6 |
| Connection approval | UI | Easy | 4 |
| Register CCTV connection | API | Complex | 8 |
| Test ONVIF connection | API | Very High | 16 |
| Submit connection | API | Complex | 8 |
| Approve connection | API | Complex | 8 |
| CCTV connection config | DB | Complex | 6 |
| ONVIF and multi-vendor CCTV platforms | Integration | Very High | 40 |
| CCTV ONVIF and Multi-vendor Video Integration feature tests | Testing | Very High | 12 |
| CCTV ONVIF and Multi-vendor Video Integration implementation documentation | Documentation | Complex | 4 |

**Feature total: 130 hours**
