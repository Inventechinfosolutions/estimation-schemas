# F09-005 — Batch & Event Notification Orchestration

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-005 |
| **Feature Name** | Batch & Event Notification Orchestration |
| **Module** | 09 — Notification Service |

### Description
Orchestrate batch notification campaigns and event-driven alerts (workflow, SLA, payments) including progress monitoring and coordination with PDF archive in Module 08 when notice PDFs are produced.

### Business Objective
Support high-volume notice runs and reliable event alerts without blocking producer modules.

### Actors
- Revenue/Estate officers (batch monitors), System event producers, Super Admin

### User Journey
1. Business module submits batch (list of recipients + template + optional PDF bytes/refs).
2. Orchestrator chunks, enqueues, tracks progress %, successes/failures.
3. Archives PDF via Module 08 when provided; dispatches channels via F09-001.
4. Officer monitors batch dashboard; retries failed subset.

### Functional Capabilities
- Batch create/progress/cancel (cancel remaining only)
- Event-driven single sends from domain events
- Chunking and throttling
- Failed-subset retry
- Link batch to source (ageing cohort, lease expiry set, etc.)
- Coordinate DMS archival handoff

### Inputs
- Batch payload items; event payload; throttle settings

### Outputs
- Batch id; progress metrics; per-item results

### Business Rules
- Cohort selection remains in Modules 04–06; this orchestrates send.
- M7-AC3 batch generation correctness is producer+archive; dispatch reliability here.
- Throttle to protect SMS/email providers.

### Validations
- Max batch size; required fields per item

### Calculations
- Progress % = processed/total

### Workflow
Submit batch → Process chunks → Complete/Partial → Retry failed.

### Search Requirements
Batches by date, source module, status.

### Documents
PDFs via F08-006.

### Reports
Batch summary report.

### Notifications
In-app to officer when batch completes.

### Security
Permission to run large batches; audit initiator.

### Integrations
Internal DMS archive (Simple).

### Dependencies
F09-001–004; F08-006; business producers

### Assumptions
- Testing Very High for volume/partial failure scenarios.
- Complex monitor UI.

### Risks
- Producer sends huge batches synchronously — require async contract.

### Non Functional Requirements
- Sustain notice-day peaks; observable metrics

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Batch campaign monitor UI | UI | Complex | 8 |
| Batch enqueue & progress ops | API | Complex | 8 |
| Batch job entities | Database | Medium | 4 |
| DMS archive handoff for notice PDF | Integration | Simple | 4 |
| Batch dispatch tests | Testing | Very High | 12 |
| Batch notification guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Does not re-estimate business notice selection UIs.
