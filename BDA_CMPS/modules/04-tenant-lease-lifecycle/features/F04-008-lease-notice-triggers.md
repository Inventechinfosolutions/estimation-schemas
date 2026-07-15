# F04-008 — Lease Notice Triggers

## Section 1 — Feature Specification

| Field | Value |
|-------|-------|
| **Feature ID** | F04-008 |
| **Feature Name** | Lease Notice Triggers |
| **Module** | 04 — Tenant & Lease Lifecycle |

### Description
Auto and manual generation of lease-related notices: lease expiry/renewal reminders, eviction/legal notice templates, and deposit-related notices, with delivery via Notification Service and PDF archive (M3-AC3).

### Business Objective
Ensure timely tenant communication for renewals, deposits, and escalations without a separate legal case system.

### Actors
- Estate Officer, Revenue Officer
- System scheduler
- Tenant (recipient)

### User Journey
1. Scheduler finds leases within configurable lead time of expiry (M3-AC3).
2. Officer reviews batch; generates notices from templates (F02-010).
3. System dispatches SMS/email/in-app; archives PDF (Modules 09/08).
4. Officer may manually issue eviction/deposit notices with reason.

### Functional Capabilities
- Configurable lead-time alerts for expiry/renewal
- Batch and single notice generation
- Notice types: expiry/renewal, eviction/legal (template), deposit-related
- Delivery status log
- Rent due/overdue primarily Module 05; this feature may deep-link but does not own rent arrears engine

### Inputs
- Lead times, lease selection, notice type, template, channel

### Outputs
- Notice instances; dispatch requests; archived PDFs

### Business Rules
- System generates renewal/expiry alerts based on configurable lead time (M3-AC3).
- Legal/eviction content is template-based; court process offline.
- Delivery channels: in-app, email, SMS, downloadable PDF.

### Validations
- Active template exists; tenant contact present for channel

### Calculations
- Expiry window membership (lease end − lead days ≤ today)

### Workflow
Select cohort → Preview → Approve send (optional) → Dispatch → Log.

### Search Requirements
Notice history by lease/tenant/type/date/status.

### Documents
PDF notices in Module 08.

### Reports
Notices issued register.

### Notifications
Via Module 09.

### Security
RBAC for legal notice issue; audit.

### Integrations
Internal Notification Service (Simple); DMS archive.

### Dependencies
F02-010; F04-003/006/007; Modules 08–09

### Assumptions
- Rent overdue campaign owned mainly by Module 05; shared notice framework.
- No WhatsApp baseline.

### Risks
- Wrong cohort selection — require preview + test tenants.

### Non Functional Requirements
- Batch generation scalable to portfolio; delivery async

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|----------|----------|------------|-------|
| Lease notice batch / manual UI | UI | Complex | 8 |
| Notice preview & history | UI | Medium | 6 |
| Notice trigger & generate ops | API | Complex | 8 |
| Notice instance entities | Database | Easy | 2 |
| Notification dispatch handoff | Integration | Simple | 4 |
| Lease notice tests | Testing | Complex | 8 |
| Lease notice guide | Documentation | Easy | 2 |
| **Total** | | | **38** |

### Estimation Assumptions
- Template config in F02-010; gateway in Module 09/10.
