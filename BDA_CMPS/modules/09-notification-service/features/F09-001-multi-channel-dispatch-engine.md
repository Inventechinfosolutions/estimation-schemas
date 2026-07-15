# F09-001 — Multi-channel Dispatch Engine

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F09-001 |
| **Feature Name** | Multi-channel Dispatch Engine |
| **Module** | 09 — Notification Service |

### Description
Core service to dispatch SMS and email notifications (event-driven and API-triggered) with queueing, retry, provider handoff via Integration Hub, and durable outbox semantics.

### Business Objective
Provide a reliable shared messaging backbone for OTPs, notices, reminders, receipts, and workflow alerts across CPMS.

### Actors
- System (producers), Super Administrator, technical operations

### User Journey
1. Business module requests send (SMS/email) with template key or body + recipients.
2. Engine enqueues message, renders content (F09-002), calls gateway connectors (Module 10).
3. Updates delivery status (F09-004); retries on transient failure.

### Functional Capabilities
- Unified send API for SMS and email
- Async outbox/queue processing
- Retry with backoff for transient errors
- Provider routing (primary/fallback configurable)
- Idempotency keys to prevent duplicate sends
- Admin test-send console

### Inputs
- Channel, recipients, template/body, merge data, priority, correlation/source ids

### Outputs
- Message ids; queued/sent/failed states

### Business Rules
- WhatsApp/RCS out of scope.
- Notice *policy/cohort selection* owned by business modules.
- Gateway credentials/connectors primarily Module 10; this feature consumes them (Easy each).
- Rate limits respected per provider config.

### Validations
- Recipient format (mobile/email); channel enabled
- Template exists when template mode used

### Calculations
None.

### Workflow
Enqueue → Render → Dispatch → Status update → (Retry) → Terminal state.

### Search Requirements
Admin search messages by id, recipient, status, date (detailed in F09-004).

### Documents
Optional PDF already archived in Module 08 before/parallel to notify.

### Reports
Dispatch volume/failure summary (ops).

### Notifications
N/A (this is the notifier).

### Security
Service-to-service auth; PII minimization in logs; no OTP plaintext in long-term logs.

### Integrations
- SMS Gateway via Module 10 — Easy (8)
- Email Service via Module 10 — Easy (8)
- Full connector hardening/retry mapping estimated in Module 10 as well — reconcile double-count at roll-up if Module 10 also books SMS/Email Medium/Easy separately.

### Dependencies
Module 10 connectors; F09-002 render; F09-004 logs; Module 01 for admin UI

### Assumptions
- Very High API for production-grade outbox/retry/idempotency.
- Gateway vendor SDKs accessed through hub.

### Risks
- Double-counting SMS/Email hours with Module 10 — flag for commercial roll-up.
- Provider outages need visible degraded mode.

### Non Functional Requirements
- High throughput for notice batches; async; monitoring hooks

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Dispatch admin / test send console | UI | Medium | 6 |
| Notification dispatch core ops | API | Very High | 16 |
| Outbox / message entities | Database | Medium | 4 |
| SMS gateway consumption | Integration | Easy | 8 |
| Email service consumption | Integration | Easy | 8 |
| Dispatch engine tests | Testing | Very High | 12 |
| Notification dispatch guide | Documentation | Medium | 3 |
| **Total** | | | **57** |

### Estimation Assumptions
- Module 10 owns raw gateway connector Very High items if categorized as such; here Easy consumption ×2.
