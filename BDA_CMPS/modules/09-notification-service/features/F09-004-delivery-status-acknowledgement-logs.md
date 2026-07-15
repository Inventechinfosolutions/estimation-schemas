# F09-004 — Delivery Status & Acknowledgement Logs

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-004 |
| **Feature Name** | Delivery Status & Acknowledgement Logs |
| **Module** | 09 — Notification Service |

### Description
Persist and expose delivery status and acknowledgement logs (where provider/channel supports) for SMS, email, and related dispatches for audit and operational troubleshooting.

### Business Objective
Prove notice/OTP/reminder delivery attempts and diagnose failures.

### Actors
- Super Administrator, Revenue/Estate officers (view batch results), Auditor, Ops

### User Journey
1. Dispatch updates status (queued/sent/delivered/failed/bounced).
2. Officer searches logs by recipient, lease, notice batch, date.
3. Exports failure list for follow-up / resend.

### Functional Capabilities
- Status lifecycle logging
- Provider message ids correlation
- Acknowledgement capture when available (email open/SMS DLR)
- Resend action (permissioned) creating new dispatch linked to original
- Export failed deliveries

### Inputs
- Provider callbacks/status payloads; manual resend requests

### Outputs
- Queryable delivery history

### Business Rules
- Acknowledgement only where available—do not fabricate.
- OTP message content not fully stored in logs.
- Retention of logs per policy (align F08-005 conceptually).

### Validations
- Callback authenticity (signatures) when provider supports

### Calculations
- Optional delivery success rate metrics

### Workflow
N/A (ops resend path).

### Search Requirements
By recipient, channel, status, source module, correlation id, date.

### Documents
Export CSV/Excel of logs.

### Reports
Delivery Failure Report.

### Notifications
Alert admins on elevated failure rates (optional).

### Security
Restrict PII columns; callback endpoint hardened.

### Integrations
Provider status webhooks via Module 10 connectors (consumption in Complex API).

### Dependencies
F09-001; Module 10; Module 01 RBAC

### Assumptions
- DLR/open tracking quality varies by provider—model statuses flexibly.

### Risks
- Incomplete DLR from SMS vendors — UI must show “sent, delivery unknown”.

### Non Functional Requirements
- Log writes non-blocking for dispatch path; searchable within configured windows

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Delivery log viewer | UI | Complex | 8 |
| Delivery & acknowledgement ops | API | Complex | 8 |
| Delivery log entities | Database | Medium | 4 |
| Delivery logging tests | Testing | Complex | 8 |
| Delivery logs guide | Documentation | Medium | 3 |
| **Total** | | | **31** |

### Estimation Assumptions
- Complex due to multi-status model + webhook handling + resend.
