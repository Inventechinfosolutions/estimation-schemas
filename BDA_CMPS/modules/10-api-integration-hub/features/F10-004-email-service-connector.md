# F10-004 — Email Service Connector

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F10-004 |
| **Feature Name** | Email Service Connector |
| **Module** | 10 — API / Integration Hub |

### Description
Email service connector (SMTP/API provider) with auth, send (HTML/text/attachments), bounce/complaint handling where supported, for Module 09 notices and alerts.

### Business Objective
Reliable email delivery for notices, receipts, and workflow alerts.

### Actors
- Tech admin, Module 09

### User Journey
1. Module 09 requests email send (subject/body/attachments refs).
2. Hub sends via provider; returns id.
3. Bounce webhook (if any) updates failure status.

### Functional Capabilities
- Send email with optional attachments (size limits)
- From/reply-to configuration
- Bounce/complaint processing when provider supports
- Health check
- Sandbox suppressions for non-prod

### Inputs
- Recipients, subject, body, attachments, headers

### Outputs
- Provider ids; accept/reject

### Business Rules
- Attachment binaries preferably fetched from DMS refs not inline megabytes.
- **Reconcile:** F09-001 Easy consumption; this owns Medium connector.

### Validations
- Email format; attachment size; recipient count limits

### Calculations
None.

### Workflow
Send → (Bounce) → Status.

### Search Requirements
Via Module 09 delivery logs.

### Documents
DNS/SPF/DKIM setup checklist (BDA IT dependency).

### Reports
Bounce extracts.

### Notifications
Connector unhealthy alerts.

### Security
No open relay; credential security; header injection guards.

### Integrations
Email Service — **Medium (16)**.

### Dependencies
F10-001; Module 08/09

### Assumptions
- SPF/DKIM domain setup is ops effort outside estimate except documentation.

### Risks
- Bulk email throttling — align with F09-005 throttle.

### Non Functional Requirements
- Support notice-day batches within provider limits

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Email connector config UI | UI | Easy | 4 |
| Email send facade | API | Medium | 6 |
| Email delivery map entities | Database | Easy | 2 |
| Email Service integration | Integration | Medium | 16 |
| Email connector tests | Testing | Complex | 8 |
| Email connector guide | Documentation | Medium | 3 |
| **Total** | | | **39** |

### Estimation Assumptions
- Medium Integration for auth+mapping+retry.
