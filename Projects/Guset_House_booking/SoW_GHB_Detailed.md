# SoW GHB — Detailed Statement of Work

## Guest House Booking and Access Management Platform

**Project code:** GHB  
**Document purpose:** RFP-ready business Statement of Work and baseline for effort estimation  
**Source:** Draft SOW — Guest House Booking and Access Management Platform

---

## 1. Introduction

This Statement of Work defines the functional and non-functional scope for a centralized digital platform to manage guest-house accommodations across multiple locations for government employees. It consolidates the draft requirements into implementation-oriented modules with numbered capabilities suitable for vendor response and estimation.

The platform will streamline room booking, enforce identity-validated access for government employees only, support online payment, issue access credentials, and provide administrative oversight of occupancy and revenue. Optional integration with on-site access-control hardware is included where infrastructure permits; physical key override remains with on-site authorities.

---

## 2. Project Overview

The Guest House Booking and Access Management Platform is a web-based system covering:

- Multi-site property configuration (sites, buildings, floors, rooms)
- Government-employee registration with OTP and mandatory government identity
- Availability search, booking, conflict prevention, and payment-gated confirmation
- Automatic room allocation and booking confirmation with access credentials
- Check-in / occupancy tracking including no-shows
- Administrative dashboards, overrides, and operational reports
- Integrations for payment gateway, SMS/email communications, and optional door-access hardware

Mobile applications, centralized government employee directory integration, and advanced analytics are noted as future considerations and are out of Phase 1 scope unless separately commissioned.

---

## 3. Project Objectives

1. Provide a single digital channel for government employees to discover and book guest-house rooms across locations.
2. Restrict access to validated government employees through OTP and government identity checks.
3. Prevent double booking and ensure confirmation only after successful payment.
4. Allocate rooms automatically after payment and communicate confirmation with access credentials.
5. Support self check-in and occupancy visibility for operational control.
6. Equip administrators with dashboards, master-data controls, exceptional overrides, and utilization/revenue reports.
7. Allow optional automated door access where hardware exists, without removing manual key override.

---

## 4. In Scope / Out of Scope

### In Scope

- Web employee (guest) portal and web administrative interface
- Site, building, floor, and room configuration with pricing and availability status
- User registration (mobile OTP), government identity submission, authentication, and session management
- Browse / search, date-based booking, conflict validation, pricing summary, and confirmation
- Online payment via payment gateway (UPI, net banking, cards), failure handling, and retries
- Automatic room allocation after successful payment
- QR code or unique booking identifier generation and delivery via SMS/other configured channels
- Self check-in (including QR where supported) and occupancy status (active stay, no-show)
- Administrative dashboards, master and user management controls, booking overrides, and standard reports
- Integration adapters for payment gateway, communication services, and optional access-control hardware
- Embedded handling of identity documents and booking confirmations within business processes (no standalone DMS product)
- Basic system documentation for administrators and end users

### Out of Scope (Phase 1)

- Native mobile applications for employees or administrators
- Integration with centralized government employee databases (future consideration)
- Advanced analytics / BI beyond the operational reports listed herein
- Supply, installation, or maintenance of access-control hardware, locks, or physical keys
- Payment gateway merchant account provisioning and SMS/email service contracts (assumed provisioned separately)
- Legacy data migration (unless separately commissioned)
- Detailed technical architecture, API contracts, database design, class diagrams, and UI wireframes (design stage)

---

## 5. Solution Expectations (Business-level Only)

- Configuration-driven property hierarchy that tolerates buildings with different floor and room structures
- Clear booking journey from search → summary → payment → allocation → confirmation → check-in
- Identity and payment gates before room confirmation
- Auditable administrative actions for masters, users, and booking overrides
- Channel-ready notifications for OTP, confirmation, and access credentials
- Hardware access treated as optional enhancement; operations remain viable with manual key override

---

## 6. Consolidated Functional Modules

### 01. User Registration & Authentication

**Purpose:** Restrict platform use to government employees; register users via mobile OTP; capture government identity; provide secure login and role-based access for employees and administrators.

**Functional requirements:**
- Allow registration using mobile number with OTP verification.
- Require submission of valid government identification as part of onboarding.
- Maintain secure authentication and session management.
- Support distinct employee and administrator access according to assigned roles.

**Acceptance criteria:**
- Only OTP-verified users with required identity submission can complete registration.
- Authenticated sessions expire and renew per security policy.
- Employees and administrators see only role-permitted functions.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Mobile OTP registration | Employee registers with mobile number and completes OTP verification |
| F01-002 | Government identity submission | Employee uploads/submits government ID; system records validation status for booking eligibility |
| F01-003 | Secure login and session management | Registered users authenticate and maintain controlled sessions |
| F01-004 | Role and permission assignment | Administrator assigns employee vs administrative roles and permissions |

---

### 02. Site, Building & Room Configuration

**Purpose:** Maintain the property hierarchy—sites/locations, buildings, floors, and rooms—with attributes needed for browsing, pricing, and availability.

**Functional requirements:**
- Create and manage multiple sites with address and administrative details.
- Configure multiple buildings per site and floor-wise structure per building.
- Define rooms under floors with type, capacity, amenities, pricing, and availability status.
- Support buildings that differ in structure, floor count, and room types.

**Acceptance criteria:**
- Administrators can maintain sites, buildings, floors, and rooms end to end.
- Room attributes required for search and booking are complete and visible to eligible users.
- Structural differences across buildings do not block configuration or booking.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Site and location master | Administrator creates and maintains guest-house sites with address and admin details |
| F02-002 | Building and floor setup | Administrator configures buildings under a site and floors within each building |
| F02-003 | Room catalogue and pricing | Administrator defines rooms with type, capacity, amenities, pricing, and availability status |
| F02-004 | Heterogeneous property structures | System supports differing building layouts and room mixes without forced uniformity |

---

### 03. Booking & Room Allocation

**Purpose:** Enable employees to browse inventory, book by date with conflict prevention, review pricing, and receive automatic room allocation and confirmation after successful payment.

**Functional requirements:**
- Browse sites, buildings, and available rooms.
- Book based on selected dates and availability; prevent double booking.
- Present booking summary including pricing before confirmation/payment.
- Automatically allocate rooms upon successful payment.
- Generate booking confirmation including period, location, and access-credential references.

**Acceptance criteria:**
- Conflicting bookings for the same room and overlapping dates are rejected.
- Confirmation is issued only for payment-successful bookings with allocated rooms.
- Confirmation content includes booking period, location, and credential references.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Inventory browse and availability search | Employee searches sites/buildings/rooms by dates and views availability |
| F03-002 | Booking request with conflict prevention | Employee creates a booking; system validates conflicts and blocks double booking |
| F03-003 | Booking summary and pricing preview | System presents summary and price before payment |
| F03-004 | Automatic room allocation | On payment success, system allocates room(s) to the booking |
| F03-005 | Booking confirmation record | System generates confirmation with period, location, and credential references |

---

### 04. Online Payment Processing

**Purpose:** Collect booking payments through an online payment gateway and gate confirmation on successful payment, with failure and retry handling.

**Functional requirements:**
- Integrate with an online payment gateway.
- Support UPI, net banking, and cards.
- Confirm booking only upon successful payment.
- Handle payment failures and retries.

**Acceptance criteria:**
- Supported methods can complete a successful payment path.
- Failed payments do not confirm or allocate rooms.
- Users can retry payment where policy allows.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Payment checkout initiation | Employee pays pending booking via gateway (UPI, net banking, cards) |
| F04-002 | Payment success handling | Successful payment updates booking and triggers allocation/confirmation |
| F04-003 | Payment failure, retry and status | System records failures, allows retry, and exposes payment status |

---

### 05. Access Credentials & Guest Check-in

**Purpose:** Issue QR / unique booking identifiers, deliver credentials to users, support self check-in and occupancy tracking, and optionally hand off to access hardware while retaining manual key override.

**Functional requirements:**
- Generate QR code or unique booking identifier per confirmed booking.
- Share credentials via SMS or other communication channels.
- Where supported, integrate with access-control hardware for automated door access.
- Retain manual override using physical keys with on-site authorities.
- Allow check-in using provided credentials, including QR scanning where supported.
- Track occupancy including active stays and no-shows.

**Acceptance criteria:**
- Every confirmed booking has a usable credential identifier.
- Credentials are delivered through configured channels.
- Check-in and occupancy states are visible to operations.
- Hardware integration is optional per site; key override remains documented/available operationally.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Access credential generation | System generates QR or unique booking identifier for confirmed bookings |
| F05-002 | Credential delivery | Credentials are sent to the user via SMS or other configured channels |
| F05-003 | Self check-in and occupancy tracking | User checks in with credentials/QR; system tracks active stay and no-show |
| F05-004 | Optional hardware access handoff | Where enabled, credentials are presented to access-control hardware |
| F05-005 | Manual key override recording | On-site authority records manual key/physical override events |

---

### 06. Administration, Monitoring & Reports

**Purpose:** Provide administrative dashboards, master/user controls, exceptional booking overrides, and reports on booking activity, revenue, and utilization.

**Functional requirements:**
- Dashboards for bookings, occupancy, and payments.
- Administrative management of sites, buildings, rooms, and users.
- Booking overrides for exceptional scenarios.
- Reports for booking activity, revenue, and utilization.

**Acceptance criteria:**
- Administrators can monitor operations via dashboards.
- Master and user controls are operable within role permissions.
- Overrides are auditable.
- Standard reports export or display the required operational metrics.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Operations dashboard | Administrator views bookings, occupancy, and payment summaries |
| F06-002 | Administrative master and user controls | Administrator manages sites, buildings, rooms, and users within policy |
| F06-003 | Exceptional booking override | Administrator overrides bookings in exceptional scenarios with reason |
| F06-004 | Activity, revenue and utilization reports | Administrator runs reports on bookings, revenue, and utilization |

---

### 07. Notification Service

**Purpose:** Provide reusable SMS/email (and similar) notification dispatch for OTP, booking confirmation, and access credentials.

**Functional requirements:**
- Maintain templates for registration OTP, booking confirmation, and credential delivery.
- Dispatch messages through provisioned communication services with delivery status tracking.

**Acceptance criteria:**
- Configured notifications are sent for the supported events.
- Delivery outcomes are visible for operational follow-up.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Notification template catalogue | Administrator maintains templates for OTP, confirmation, and credentials |
| F07-002 | Notification dispatch and status | System dispatches messages and records delivery/failure status |

---

### 08. Integration Hub

**Purpose:** Provide managed adapters for the payment gateway, communication providers, and optional access-control hardware.

**Functional requirements:**
- Payment gateway connectivity for checkout and status callbacks.
- Communication service connectivity for SMS/email.
- Optional adapter for access-control hardware where sites support it.

**Acceptance criteria:**
- Payment and communication channels operate for go-live sites.
- Hardware adapter can be enabled per site without blocking sites without hardware.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Payment gateway adapter | System integrates payment initiation, callbacks, and status with the gateway |
| F08-002 | Communication service adapter | System integrates SMS/email providers for outbound notifications |
| F08-003 | Access-control hardware adapter | Optional adapter for automated door access at equipped sites |

---

## 7. End-to-End Workflows

### 7.1 Employee registration

1. Employee opens registration and enters mobile number.  
2. System sends OTP; employee verifies.  
3. Employee submits government identification.  
4. System records identity validation status and activates eligible login.

### 7.2 Booking and payment

1. Employee searches by site/dates and selects available room options.  
2. System shows booking summary and price.  
3. Employee proceeds to payment gateway.  
4. On success, system allocates room, creates confirmation, and issues access credentials.  
5. On failure, booking remains unconfirmed; employee may retry per policy.

### 7.3 Arrival and stay

1. Employee receives credential via SMS/configured channel.  
2. Employee self-checks in using credential/QR (or is assisted on-site).  
3. Occupancy shows active stay; missed arrivals can be marked/tracked as no-show.  
4. Where hardware is enabled, credential may unlock automated access; otherwise physical key override is used.

### 7.4 Administration

1. Administrator maintains property masters and user roles.  
2. Administrator monitors dashboards and acts on exceptions via overrides.  
3. Administrator generates activity, revenue, and utilization reports.

---

## 8. Access Control / RBAC

**Access model:** Direct **User → Role → Permissions** (no post/position hierarchy required by the source).

**Indicative roles (illustrative, final naming during implementation):**

| Role | Typical access |
|------|----------------|
| Employee Guest | Register, book, pay, view own bookings/credentials, self check-in |
| Site / Guest-house Administrator | Site-scoped masters, occupancy, overrides, local reports |
| Platform Administrator | Cross-site configuration, users/roles, dashboards, reports, integrations |
| Auditor (optional) | Read-only history of bookings, payments, overrides, and access events |

Identity documents and booking records are visible only to authorized roles. Administrative overrides require reason capture and audit trail.

---

## 9. Channels

| Channel | Phase 1 |
|---------|---------|
| Employee web portal | In scope |
| Administrative web interface | In scope |
| SMS / email notifications | In scope (via provisioned providers) |
| Native mobile apps | Out of scope (future) |
| Access-control hardware terminals | Optional where deployed |

---

## 10. Integrations

| Integration | Purpose | Phase 1 |
|-------------|---------|---------|
| Payment gateway | UPI, net banking, cards; success/failure callbacks | Required |
| SMS / email provider | OTP, confirmation, credentials | Required |
| Access-control hardware | Automated door access using booking credentials | Optional / site-dependent |
| Central government employee directory | Identity enrichment | Future — out of scope |

Merchant accounts, gateway credentials, and communication service contracts are client-provisioned dependencies.

---

## 11. Audit, Compliance & Security

- Secure handling of user data and identity documents (storage, access control, retention aligned to applicable policy).
- Authentication, session controls, and role-based authorization.
- Audit trail for registration, booking, payment outcomes, allocation, credential issuance, check-in, and administrative overrides.
- Compliance with applicable data-protection and government regulations as identified by the client.
- Payment handling must support reconciliation-friendly status records (without prescribing gateway internals).

---

## 12. Non-Functional Requirements

1. Secure handling of personal and identity data.  
2. Scalability for multiple locations and concurrent users.  
3. Low latency for search and booking operations under expected load.  
4. High availability with minimal planned downtime.  
5. Regulatory compliance as applicable to government employee data and payments.  
6. Graceful degradation at sites without access hardware (manual key path remains usable).

---

## 13. Data Migration

**Out of scope** for Phase 1 unless separately commissioned. No legacy guest-house booking migration is assumed.

---

## 14. Phased Delivery

### Phase 1 — Go-live (this SOW)

Modules 01–08 with payment and communication integrations; access-hardware adapter enabled only for equipped sites.

### Phase 2 — Future considerations (not estimated herein)

- Mobile applications  
- Centralized government employee database integration  
- Advanced analytics  
- Enhanced smart-hardware automation  

---

## 15. Deliverables

1. Web-based guest house booking platform (employee + admin).  
2. Administrative interface for management and monitoring.  
3. Integrated payment processing capability.  
4. Booking confirmation and access credential generation/delivery.  
5. Basic system documentation (admin and user).  
6. Configurable optional hardware access handoff where applicable.

---

## 16. Acceptance Criteria (Program Level)

1. Users can register with OTP and validated government identity submission.  
2. Rooms can be configured and managed across multiple sites and buildings with differing structures.  
3. Booking and payment processes function reliably, including failure/retry paths.  
4. Room allocation and confirmation are accurate after successful payment.  
5. Access credentials are generated, delivered, and usable for check-in (and hardware where enabled).  
6. Administrative controls, dashboards, overrides, and reporting are operational.

---

## 17. Expected Benefits

- Faster, transparent booking for government employees across locations  
- Reduced double-booking and manual coordination effort  
- Payment-linked confirmation with clearer revenue visibility  
- Stronger identity control at registration  
- Better occupancy awareness and utilization reporting  
- Flexible access path (digital credential ± hardware, with key override)

---

## 18. Assumptions & Dependencies

1. All intended end users are authorized government employees.  
2. Payment gateway and communication services will be provisioned separately by the client.  
3. Availability of access-control hardware varies by location; software must not hard-depend on hardware for core booking.  
4. Network connectivity is available at guest-house locations for real-time operations.  
5. Access model is User → Role → Permissions as stated in Section 8.  
6. Document management and approvals are embedded in business processes (no separate DMS/workflow product).  
7. No Phase 1 legacy migration.  
8. Identity “validation” means capture plus configurable administrative/verification status; automated verification against a central government directory is future scope.  
9. “Other communication channels” beyond SMS are limited to email unless the client specifies additional providers.

---

## 19. Vendor Response Expectations

Vendors should:

1. Confirm understanding of modules and feature outline IDs (`F{NN}-{SEQ}`).  
2. Identify any scope clarifications, especially around identity verification depth and hardware brands/protocols.  
3. Propose Phase 1 delivery plan aligned to modules 01–08.  
4. Separate optional hardware-enablement effort from core booking go-live if commercially useful.  
5. List assumptions on gateway, SMS, hosting, and compliance responsibilities.  
6. Avoid prescribing proprietary stack lock-in in the business response unless required by client standards.

---

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User Registration & Authentication | Shared | F01-001 … F01-004 (4) |
| 02 | Site, Building & Room Configuration | Business | F02-001 … F02-004 (4) |
| 03 | Booking & Room Allocation | Business | F03-001 … F03-005 (5) |
| 04 | Online Payment Processing | Business | F04-001 … F04-003 (3) |
| 05 | Access Credentials & Guest Check-in | Business | F05-001 … F05-005 (5) |
| 06 | Administration, Monitoring & Reports | Business | F06-001 … F06-004 (4) |
| 07 | Notification Service | Technical | F07-001 … F07-002 (2) |
| 08 | Integration Hub | Technical | F08-001 … F08-003 (3) |

**Total outline features:** 30

### Appendix B — Module consolidation map (draft → consolidated)

| Draft SOW section | Consolidated module |
|-------------------|---------------------|
| 2.3 User Registration and Validation | 01. User Registration & Authentication |
| 2.1 Site and Location Management | 02. Site, Building & Room Configuration |
| 2.2 Building and Room Structuring | 02. Site, Building & Room Configuration |
| 2.4 Booking Management | 03. Booking & Room Allocation |
| 2.6 Room Allocation and Confirmation | 03. Booking & Room Allocation |
| 2.5 Payment Processing | 04. Online Payment Processing |
| 2.7 Access Control Mechanism | 05. Access Credentials & Guest Check-in |
| 2.8 Check-in and Occupancy Management | 05. Access Credentials & Guest Check-in |
| 2.9 Administration and Monitoring | 06. Administration, Monitoring & Reports |
| SMS/email for OTP & credentials (implied) | 07. Notification Service |
| Payment gateway & optional hardware (implied) | 08. Integration Hub |

### Appendix C — Key business entities (logical)

Site · Building · Floor · Room · User · Role · Booking · Payment · Room Allocation · Access Credential · Check-in / Occupancy · Override · Notification · Integration Endpoint

### Appendix D — Risks and considerations

1. Variability in infrastructure across locations may affect access-control enablement.  
2. Dependence on network availability for real-time booking, payment, and check-in.  
3. Government identity validation may require additional manual verification mechanisms beyond document upload.  
4. Payment reconciliation and failure scenarios require careful operational handling.  
5. Incorrect room master data (pricing/availability) directly impacts booking trust.
