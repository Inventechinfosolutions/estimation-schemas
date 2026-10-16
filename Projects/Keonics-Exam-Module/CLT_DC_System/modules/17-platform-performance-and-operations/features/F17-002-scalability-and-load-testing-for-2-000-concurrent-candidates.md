# F17-002 — Scalability & Load Testing for 2,000 Concurrent Candidates

## Feature Specification

| Field | Value |
|-------|-------|
| Feature ID | F17-002 |
| Feature Name | Scalability & Load Testing for 2,000 Concurrent Candidates |
| Module | 17 — Platform, Performance & Operations |
| Module Type | Technical |
| Release | Go-live |

### Description
Performance engineering for peak sessions: stateless services with horizontal scaling, caching of papers and media, queue-based writes for responses, audit and recording uploads, database tuning and partitioning, capacity plan for compute, storage (video) and bandwidth, and load tests at 2,000 concurrent candidates with recordings, plus soak and spike tests.

### Business Objective
Meet the 2,000 concurrent candidates and sub-second response requirements.

### Actors
- Service Provider performance team
- KEONICS

### User Journey
1. **Who creates:** Performance team plans tests.
2. **How they create:** Scripts and scenarios built.
3. **How they edit:** Tuning iterations.
4. **How they send for approval:** Results presented to KEONICS.
5. **How the approver sees pending items:** KEONICS sees report.
6. **How the approver decides:** KEONICS accepts.
7. **How the applicant / maker sees history:** Not applicable.
8. **How the approver / auditor sees history:** Auditors see test reports.

### Functional Capabilities
- Horizontal scaling
- Caching
- Write queues
- DB partitioning
- Capacity plan (compute, storage, bandwidth)
- Load, soak and spike tests

### UI Screens
- None (no user interface in this feature)

### Logical API Operations
- Caching layer
- Queue-based write pipeline
- DB partitioning and tuning

### Inputs
- Scenarios

### Outputs
- Performance report

### Business Rules
- Pass criteria: under 1 second LAN, no errors

### Validations
- None

### Calculations
- Throughput, latency

### Workflow
Planned → Executed → Accepted

### Search Requirements
- None

### Documents
- Reports

### Reports
- Performance report

### Notifications
- None

### Security
- None

### Integrations
- None

### Dependencies
- All modules

### Assumptions
- SDC test environment mirrors production

### Risks
- Video bandwidth at SDC

### Non Functional Requirements
- 2,000 concurrent; under 1 second LAN

## Estimation Breakdown

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| API | Caching layer | Medium | 6 |
| API | Queue-based write pipeline | Complex | 8 |
| API | DB partitioning and tuning | Complex | 8 |
| Database | Partitioning scheme | Medium | 4 |
| Testing | Load test at 2,000 concurrent with recordings | Very High | 12 |
| Testing | Soak and spike tests | Complex | 8 |
| Documentation | Capacity plan and performance report | Complex | 4 |

**Feature Total: 50 hours**

| UI | API | Database | Integration | Testing | Documentation | Total |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 22 | 4 | 0 | 20 | 4 | **50** |

### Estimation Assumptions
- Every UI screen and logical API operation listed above is estimated as its own row using the Estimation Master.
- Enterprise-grade implementation: validation, error handling, logging, audit hooks, security checks and unit tests included in each row.
- Load testing rated Very High
- No external integration channel in this feature; Integration row omitted.
