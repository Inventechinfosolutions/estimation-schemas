# Guest House Booking and Access Management Platform — Module List

Source: `SoW_GHB_Detailed.md` (production-grade SOW from draft `SOW`)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User Registration & Authentication | Shared | OTP registration, government ID, login/session, roles | Explicit |
| 02 | Site, Building & Room Configuration | Business | Multi-site property hierarchy, floors, rooms, pricing | Explicit |
| 03 | Booking & Room Allocation | Business | Search, book, conflict checks, allocate, confirm | Explicit |
| 04 | Online Payment Processing | Business | Gateway checkout, success/failure, retry | Explicit |
| 05 | Access Credentials & Guest Check-in | Business | QR/ID credentials, delivery, check-in, occupancy, optional hardware | Explicit |
| 06 | Administration, Monitoring & Reports | Business | Dashboards, admin controls, overrides, reports | Explicit |
| 07 | Notification Service | Technical | Templates and dispatch for OTP, confirmation, credentials | Derived |
| 08 | Integration Hub | Technical | Payment, SMS/email, optional access-hardware adapters | Derived |

---

## Module Details

### 01. User Registration & Authentication

- **Type:** Shared
- **Summary:** Government-employee registration via mobile OTP, government identity submission, secure authentication/session, and User→Role permissions.
- **Source:** Explicit (SOW §6.01 / draft §2.3)
- **In Scope:** OTP registration; identity document capture and validation status; login/session; role assignment for employee and admin users
- **Out of Scope:** Central government employee directory integration (future); biometric login
- **Key Actors:** Employee Guest; Platform Administrator; Auditor (read-only)
- **Dependencies:** Notification Service (OTP); Integration Hub (SMS)
- **Notes:** Access model is User → Role → Permissions per SOW Section 8

### 02. Site, Building & Room Configuration

- **Type:** Business
- **Summary:** Configure sites/locations, buildings, floors, and rooms including type, capacity, amenities, pricing, and availability.
- **Source:** Explicit (SOW §6.02 / draft §2.1–2.2)
- **In Scope:** Site master; building and floor setup; room catalogue; support for heterogeneous building structures
- **Out of Scope:** GIS mapping; third-party property management systems
- **Key Actors:** Platform Administrator; Site Administrator
- **Dependencies:** Module 01 (admin access)
- **Notes:** Document attachments for site/room info embedded if needed — no separate DMS

### 03. Booking & Room Allocation

- **Type:** Business
- **Summary:** Employee browse/search, date-based booking with conflict prevention, pricing summary, post-payment allocation, and confirmation.
- **Source:** Explicit (SOW §6.03 / draft §2.4, §2.6)
- **In Scope:** Availability search; booking request; conflict validation; pricing preview; automatic allocation; confirmation record
- **Out of Scope:** Waitlist engine; multi-currency pricing
- **Key Actors:** Employee Guest; Site Administrator
- **Dependencies:** Modules 01, 02, 04 (payment success), 05 (credential references on confirmation)
- **Notes:** Confirmation content references access credentials owned by Module 05

### 04. Online Payment Processing

- **Type:** Business
- **Summary:** Initiate gateway payment (UPI, net banking, cards), handle success/failure, and retry.
- **Source:** Explicit (SOW §6.04 / draft §2.5)
- **In Scope:** Checkout initiation; success handling linked to booking; failure/retry/status visibility
- **Out of Scope:** Merchant onboarding; settlement accounting beyond status needed for operations
- **Key Actors:** Employee Guest; Platform Administrator (status monitoring)
- **Dependencies:** Module 03 (pending booking); Module 08 (payment adapter)
- **Notes:** Booking confirms only on successful payment

### 05. Access Credentials & Guest Check-in

- **Type:** Business
- **Summary:** Generate and deliver QR/unique credentials; self check-in; occupancy/no-show; optional hardware handoff; manual key override recording.
- **Source:** Explicit (SOW §6.05 / draft §2.7–2.8)
- **In Scope:** Credential generation; SMS/other delivery; check-in; occupancy states; optional hardware; manual override events
- **Out of Scope:** Hardware supply/install; proprietary lock firmware development
- **Key Actors:** Employee Guest; Site Administrator; On-site authority
- **Dependencies:** Modules 03, 07, 08 (optional hardware)
- **Notes:** F05-004 is optional/conditional per site hardware

### 06. Administration, Monitoring & Reports

- **Type:** Business
- **Summary:** Operational dashboards; admin controls for masters/users; exceptional booking overrides; activity/revenue/utilization reports.
- **Source:** Explicit (SOW §6.06 / draft §2.9)
- **In Scope:** Dashboards; administrative controls; overrides with audit; standard reports
- **Out of Scope:** Advanced BI / predictive analytics (future)
- **Key Actors:** Platform Administrator; Site Administrator; Auditor
- **Dependencies:** Modules 01–05 for underlying data
- **Notes:** Deep master editing may deep-link into Module 02 screens; this module owns oversight UX and overrides/reports

### 07. Notification Service

- **Type:** Technical
- **Summary:** Template catalogue and dispatch/status for OTP, booking confirmation, and access credentials.
- **Source:** Derived (SOW §6.07)
- **In Scope:** Templates; outbound dispatch; delivery status
- **Out of Scope:** Marketing campaigns; push-notification mobile SDK
- **Key Actors:** Platform Administrator; system (event-driven)
- **Dependencies:** Module 08 communication adapter
- **Notes:** Consumed by Modules 01, 03, 05

### 08. Integration Hub

- **Type:** Technical
- **Summary:** Adapters for payment gateway, communication providers, and optional access-control hardware.
- **Source:** Derived (SOW §6.08)
- **In Scope:** Payment adapter; SMS/email adapter; optional hardware adapter
- **Out of Scope:** Building the external provider platforms themselves
- **Key Actors:** Platform Administrator; system
- **Dependencies:** Client-provisioned gateway and communication credentials
- **Notes:** F08-003 optional/conditional — does not block go-live without hardware

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Document storage for ID proofs / confirmations | Embedded in Modules 01 and 03/05 — no standalone DMS |
| Generic workflow engine | Not separate — no multi-level approval inbox in Phase 1 registration/booking (admin override is exceptional) |
| Audit logging | Cross-cutting NFR; events recorded in owning modules |
| Search/filter on lists | Embedded in each register screen |
| File store / job scheduler | Platform support — not separate modules |
| Mobile apps / central employee DB / advanced analytics | Out of Phase 1 (future) |

---

## Assumptions

1. Production SOW `SoW_GHB_Detailed.md` is the scope authority.
2. Access model is User → Role → Permissions.
3. Payment gateway and SMS/email are client-provisioned.
4. Access hardware varies by site; Module 05/08 hardware features are conditional.
5. No Phase 1 data migration.
6. User asked to run all CONTROL steps — module confirmation gate skipped unless they request changes.

---

## Risks

1. Identity verification depth may expand beyond document capture + status.
2. Hardware vendor diversity may complicate F08-003.
3. Network outages at sites affect check-in and payment callbacks.
4. Payment reconciliation disputes if gateway status mapping is incomplete.
5. Heterogeneous building structures increase configuration UX complexity in Module 02.
