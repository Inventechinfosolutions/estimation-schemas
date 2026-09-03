# F12-001 — VLTS and Multi-vendor GPS Integration

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F12-001 |
| **Feature Name** | VLTS and Multi-vendor GPS Integration |
| **Module** | 12 — External Integrations Hub |

### Description
Integration Administrator configures mappings and schedules to ingest AIS-140/VLTS data from multiple GPS vendors; coordinates with GPS vendors. Device hardware out of scope.

### Business Objective
Reliable live and historical GPS data into CCC.

### Actors
Maker: Integration Administrator. Checker: Integration Checker. Operator: monitors runs.

### User Journey
1. Who creates: Integration Administrator.
2. How they create: Integrations → VLTS mapping: vendor, fields, schedule, Save draft, Test fetch.
3. How they edit: Draft editable; live change is new version.
4. How they send for approval: Submit mapping to checker.
5. How the approver sees pending items: Checker mapping inbox; failed-run inbox for operators.
6. How the approver decides: Approve mapping; retry/abandon failed run.
7. How the maker sees history: Run log.
8. How the checker/auditor sees history: Approved mappings and run log.

### Functional Capabilities
- Multi-vendor GPS APIs
- Field mapping
- Test/prod runs
- Health status

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| VLTS mapping form | Complex |
| VLTS run monitor | Medium |
| Mapping checker inbox | Medium |
| Mapping approval | Easy |
| Failed-run inbox | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Fetch VLTS positions | Very High |
| Test VLTS connection | Complex |
| Submit mapping | Complex |
| Approve mapping | Complex |
| Record run result | Medium |

### Inputs
Vendor, schedule, field map, run status.

### Outputs
Persisted records, searchable history, and role-scoped views as described in the journey.

### Business Rules
- GPS devices, SIM, field install out of scope.

### Validations
- Approved mapping required to run.

### Calculations
Read/error counts.

### Workflow
Maker–checker mapping.

### Search Requirements
Search by the identifiers and filters named in Inputs and UI screens, scoped by the acting Post.

### Documents
Interface note.

### Reports
Run success.

### Notifications
Failed run alert.

### Security
Integration admin Posts.

### Integrations
GPS vendors.

### Dependencies
F03-002.

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
| VLTS mapping form | UI | Complex | 12 |
| VLTS run monitor | UI | Medium | 6 |
| Mapping checker inbox | UI | Medium | 6 |
| Mapping approval | UI | Easy | 4 |
| Failed-run inbox | UI | Medium | 6 |
| Fetch VLTS positions | API | Very High | 16 |
| Test VLTS connection | API | Complex | 8 |
| Submit mapping | API | Complex | 8 |
| Approve mapping | API | Complex | 8 |
| Record run result | API | Medium | 6 |
| VLTS mapping and run log | DB | Complex | 6 |
| Multi-vendor AIS-140 / VLTS APIs | Integration | Very High | 40 |
| VLTS and Multi-vendor GPS Integration feature tests | Testing | Very High | 12 |
| VLTS and Multi-vendor GPS Integration implementation documentation | Documentation | Complex | 4 |

**Feature total: 142 hours**
