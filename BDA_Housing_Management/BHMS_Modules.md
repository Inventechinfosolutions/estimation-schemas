# BDA Housing Management System (BHMS) — Module List

Source: `SoW_BHMS_Detailed.md`

| # | Module | Type | Summary |
|---|--------|------|---------|
| 01 | User & Role Management | Shared | Officer/citizen auth, roles, permissions, approval-level mapping |
| 02 | Master Data & System Configuration | Business | Housing masters, templates, parameters, workflow configuration |
| 03 | Housing Project Management | Business | Project create, approve, publish, and project documents |
| 04 | Flats & Villas Inventory & Status | Business | Unit inventory, pricing, documents, status lifecycle |
| 05 | Housing Notification Management | Business | Public booking notification publish/extend/withdraw |
| 06 | Citizen Registration & Portal | Shared | Citizen OTP registration, profile, discovery, self-service shell |
| 07 | Application & First-Come Booking | Business | Online/officer applications and exclusive FCFS booking |
| 08 | Online Payment Management | Business | Gateway payments, dues, reminders, receipts, reconciliation |
| 09 | Allotment, Sale Deed, Registration & Possession | Business | Allotment letter, draft sale deed, offline registration, possession |
| 10 | Cancellation, Refund & Auto-Cancellation | Business | Voluntary cancel, refund, non-payment auto-cancel |
| 11 | Bank / Loan NOC Management | Business | NOC request, approval, issuance, and history |
| 12 | Notification Service | Technical | SMS, email, and portal/in-app notification dispatch |
| 13 | API / Integration Hub | Technical | Payment gateway connector and optional DigiLocker/eKYC |
| 14 | Analytics, Dashboards & Reports | Business | Management/Engineering/Accounts/Citizen MIS and exports |
| 15 | Data Migration | Shared | Legacy project/unit/booking import and reconciliation |

Source notes for each module are in the Module Details sections below.

---

## Module Details

### 01. User & Role Management

- **Type:** Shared
- **Summary:** Provide secure login, roles, permissions, and approval-level user mapping for BDA officers and citizen portal users.
- **Source:** Explicit in document (SOW Module 1.B / Section 8); separated for implementation per schema defaults (Identity & Access).
- **In Scope:**
  - Officer user create/update, activate/deactivate, password reset
  - Roles and permission sets (module + action)
  - Map users to approval levels
  - Secure authentication, password policy, session timeout
  - Citizen credential lifecycle linkage with Module 06
  - Login history and access-related activity logs
  - Segregation-of-duties support for propose vs approve
- **Out of Scope:**
  - External IdP/SSO unless later specified
  - Approval workflow *definition* (Module 02); runtime approvals in business modules
- **Key Actors:** Super Administrator, Auditor, all officer roles, Citizen
- **Dependencies:** None (foundation)
- **Notes:** Citizen profile registration UX lives in Module 06; auth foundation here.

---

### 02. Master Data & System Configuration

- **Type:** Business
- **Summary:** Maintain housing masters, document types, charges, notification templates, system parameters, and configurable multi-level approval definitions.
- **Source:** Explicit in document (SOW Module 1), excluding User & Role (Module 01).
- **In Scope:**
  - Layout, project type, property type, tower, floor, block, BHK, facing, amenities
  - Document type, charges, payment lookup masters
  - Notification templates; parameters (90-day balance, 130-day auto-cancel, 10% refund deduction — configurable)
  - Configure approval processes per process type (any number of levels; rearrange; map users)
  - Activate/deactivate masters; search/export of masters
- **Out of Scope:**
  - Transactional project/unit registers (Modules 03–04)
  - Standalone BPM product beyond configurable approval definitions
  - Separate Document Management product (embedded in business modules)
- **Key Actors:** Super Administrator, section admins
- **Dependencies:** Module 01
- **Notes:** Runtime approvals execute inside Modules 03–11.

---

### 03. Housing Project Management

- **Type:** Business
- **Summary:** Create, approve, publish, and maintain BDA housing projects with embedded documents.
- **Source:** Explicit in document (SOW Module 2)
- **In Scope:**
  - Project attributes, counts, amenities, booking window, completion date, status
  - Project images, brochure, layout plans, supporting documents
  - Publication only after configured approval
  - History of create/modify/approve/publish
- **Out of Scope:**
  - Unit inventory (Module 04)
  - Housing notification content lifecycle (Module 05)
  - Citizen visibility shell (Module 06)
- **Key Actors:** Engineering Section, Approvers
- **Dependencies:** Modules 01–02; Module 12 for alerts
- **Notes:** Only published projects appear on citizen portal.

---

### 04. Flats & Villas Inventory & Status

- **Type:** Business
- **Summary:** Maintain Flat/Villa inventory, pricing, unit documents, and event-driven status lifecycle.
- **Source:** Explicit in document (SOW Module 3)
- **In Scope:**
  - Unit register (type, tower/block/floor, BHK, facing, areas, parking, construction status)
  - Financials per unit (base price, booking amount, GST, charges, total)
  - Unit documents and media
  - Status lifecycle including Available/Booked/Paid/Allotted/Registered/Possession/Cancelled/Refunded
  - Post-publish change approvals where configured
  - Auto-return to available on cancellation
- **Out of Scope:**
  - Booking/payment case processing (Modules 07–08)
  - Lottery/quota engines (SOW out of scope)
- **Key Actors:** Engineering Section, Approvers
- **Dependencies:** Modules 01–03
- **Notes:** Concurrent booking exclusivity enforced with Module 07.

---

### 05. Housing Notification Management

- **Type:** Business
- **Summary:** Publish and manage public housing booking notifications for approved projects.
- **Source:** Explicit in document (SOW Module 4)
- **In Scope:**
  - Notification content (units summary, prices, documents required, window, policies, T&Cs)
  - Active-only citizen visibility
  - Extend / modify / withdraw before booking end with audit and approvals as configured
- **Out of Scope:**
  - SMS/email template dispatch engine (Module 12)
  - Application capture (Module 07)
- **Key Actors:** Housing/Engineering officers, Approvers, Citizens (view)
- **Dependencies:** Modules 01–04
- **Notes:** Distinct from system event notifications (Module 12).

---

### 06. Citizen Registration & Portal

- **Type:** Shared
- **Summary:** Citizen OTP registration, profile, published inventory discovery, and self-service portal shell with ownership isolation.
- **Source:** Explicit in document (SOW Module 5 / Section 9.2)
- **In Scope:**
  - Registration fields + mobile OTP
  - Login, profile update, password change
  - Project/unit search, filter, compare, brochure/photos/floor plans
  - Portal navigation to apply/pay/track/download (process backends in Modules 07–11)
  - Citizen-only access to own records
- **Out of Scope:**
  - Officer operational UI
  - Payment gateway connector implementation (Module 13)
  - Native mobile apps
- **Key Actors:** Citizen; BDA content publishers via officer tools
- **Dependencies:** Modules 01–05; Module 12 for OTP/notices
- **Notes:** Disclosure limited to published inventory and own transactions.

---

### 07. Application & First-Come Booking

- **Type:** Business
- **Summary:** Capture online and officer-assisted applications and confirm exclusive first-come bookings after booking-amount payment.
- **Source:** Explicit in document (SOW Module 6)
- **In Scope:**
  - Online application journey
  - Officer-assisted offline data entry into the same workflow
  - Document uploads and T&Cs acceptance
  - Booking confirmation after successful online booking payment
  - Unit reservation, double-booking prevention, booking confirmation/receipt artefacts
- **Out of Scope:**
  - Lottery/draw
  - Balance payment ledger engine details beyond booking confirmation handoff (Module 08)
  - Allotment letter generation (Module 09)
- **Key Actors:** Citizen, Housing/Estate officers, Approvers
- **Dependencies:** Modules 01–06, 08, 12
- **Notes:** Payment success signal from Module 08/13 required before booking confirm.

---

### 08. Online Payment Management

- **Type:** Business
- **Summary:** Collect and track online payments for booking, balance, and applicable charges with reminders and receipts.
- **Source:** Explicit in document (SOW Module 7)
- **In Scope:**
  - Payment heads and dues against booking
  - Configurable balance due period (default 90 days)
  - Online payment UX and status; receipts; history
  - Automatic due reminders
  - Accounts reconciliation views
- **Out of Scope:**
  - Cash/DD/offline payment modes (baseline excluded)
  - Payment gateway connector internals (Module 13) — this module consumes the hub
  - Refund payout processing mechanics beyond refund case linkage (Module 10)
- **Key Actors:** Citizen, Accounts Section
- **Dependencies:** Modules 01–02, 07, 12–13
- **Notes:** Failed/pending gateway payments must not confirm booking.

---

### 09. Allotment, Sale Deed, Registration & Possession

- **Type:** Business
- **Summary:** Generate allotment letter and draft sale deed; record offline registration; issue possession.
- **Source:** Explicit in document (SOW Module 8)
- **In Scope:**
  - Allotment letter generate/download/reissue with history
  - Draft sale deed generate/review/revise/approve with version history
  - Offline registration capture (SRO particulars) + registered deed upload
  - Possession readiness checks, possession letter, acknowledgement
- **Out of Scope:**
  - Online Sub-Registrar / Kaveri integration (SOW out of baseline)
  - Eligibility/quota engines
- **Key Actors:** Housing officers, Registration Section, Possession Section, Citizen (downloads)
- **Dependencies:** Modules 01–02, 07–08, 12
- **Notes:** Draft deed is in-system; registration ceremony is offline.

---

### 10. Cancellation, Refund & Auto-Cancellation

- **Type:** Business
- **Summary:** Process voluntary cancellation, configurable refunds, and non-payment auto-cancellation returning units to inventory.
- **Source:** Explicit in document (SOW Module 9)
- **In Scope:**
  - Cancellation request and approval workflow
  - Refund calculation (default 10% booking-amount deduction, configurable) and status tracking
  - Auto-cancel at configured non-payment threshold (default 130 days)
  - Free unit inventory and notify citizen
- **Out of Scope:**
  - Court dispute case management
  - Bank settlement rails beyond recorded refund status (payment hub may support payout later)
- **Key Actors:** Citizen, Housing officers, Accounts, Approvers
- **Dependencies:** Modules 01–02, 04, 07–08, 12
- **Notes:** Auto-cancel requires scheduler/job support inside this module’s implementation effort (not a separate platform module).

---

### 11. Bank / Loan NOC Management

- **Type:** Business
- **Summary:** Manage bank/housing-loan NOC requests, approvals, issuance, and history against bookings/allotments.
- **Source:** Explicit in document (SOW Module 10)
- **In Scope:**
  - Citizen/officer NOC request linked to booking/allotment
  - Bank details, supporting documents, scrutiny, multi-level approval
  - NOC generation from template; issue/download; reissue/withdraw as configured
- **Out of Scope:**
  - Bank CBS integration
  - Loan sanction/disbursement processing
- **Key Actors:** Citizen, NOC Desk, Approvers
- **Dependencies:** Modules 01–02, 07–09, 12
- **Notes:** In-scope per BDA confirmation for this RFP.

---

### 12. Notification Service

- **Type:** Technical
- **Summary:** Dispatch SMS, email, and portal/in-app notifications for OTP and process events.
- **Source:** Added for implementation (derived from SOW Sections 10–11 / event list)
- **In Scope:**
  - Event-driven notifications listed in SOW (registration, application, booking, payments, letters, cancellation, refund, auto-cancel, NOC, etc.)
  - Template rendering using Module 02 templates
  - Delivery logging / basic failure visibility
- **Out of Scope:**
  - Marketing campaigns
  - Housing *booking notification* content product (Module 05)
- **Key Actors:** System; Super Administrator (templates via Module 02)
- **Dependencies:** Modules 01–02; SMS/email connectivity via Module 13 patterns/credentials
- **Notes:** Mandatory SMS/email per SOW integrations.

---

### 13. API / Integration Hub

- **Type:** Technical
- **Summary:** Secure connectors for payment gateway and optional DigiLocker/Aadhaar eKYC.
- **Source:** Added for implementation (derived from SOW Section 10)
- **In Scope:**
  - Payment gateway connector (mandatory) with auth, callbacks, failure handling, reconciliation hooks
  - Optional DigiLocker / Aadhaar eKYC placeholders
- **Out of Scope:**
  - Sub-Registrar online integration (baseline out of scope)
  - SMS/email send pipeline (Module 12)
- **Key Actors:** Super Administrator, Accounts (recon consumers), ops
- **Dependencies:** Module 08 for payment business posting; Module 01 for service accounts as applicable
- **Notes:** Keeps external connector complexity out of business payment UX.

---

### 14. Analytics, Dashboards & Reports

- **Type:** Business
- **Summary:** Role-based dashboards and PDF/Excel reports for Management, Engineering, Accounts, and Citizen views.
- **Source:** Explicit in document (SOW Module section Dashboards & Reports / Appendix)
- **In Scope:**
  - Management, Engineering, Accounts, Citizen dashboard KPIs listed in SOW
  - Project/inventory/booking/payment/financial/registration/possession/citizen/admin reports
  - Filters and PDF/Excel export
- **Out of Scope:**
  - Ad-hoc enterprise BI warehouse product beyond packaged dashboards/reports
- **Key Actors:** Commissioner/senior authority, Engineering, Accounts, Auditor, Citizen (own dashboard)
- **Dependencies:** Modules 03–11 for data; Module 01 for role views
- **Notes:** KPIs must reconcile to registers for acceptance sampling.

---

### 15. Data Migration

- **Type:** Shared
- **Summary:** Migrate legacy projects/units and available booking/applicant data with validation and reconciliation.
- **Source:** Explicit in document (SOW Section 13)
- **In Scope:**
  - Templates, validation, import tools
  - Trial/final loads, exception register, cutover support
  - Document metadata bulk link when files supplied
- **Out of Scope:**
  - Physical scanning (BDA)
  - Reconstructing complete history where source data does not exist
- **Key Actors:** Vendor migration team, BDA data owners
- **Dependencies:** Modules 02–11 target structures
- **Notes:** Estimate as its own delivery unit.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|---|---|
| Document Management | **Embedded** in Modules 03–11 per SOW — not a separate module |
| Workflow / Approval Engine | **Config** in Module 02; **runtime** in business modules — not a standalone BPM module |
| Audit & process history | System-wide NFR + domain history in business modules |
| Advanced search | Embedded in module list/search and Module 06 discovery |
| Officer portal shell | Authenticated app experience across modules — not separate |
| Lottery / quota / eligibility engines | Out of scope |
| GIS / GeoServer | Out of baseline (layout master only) |
| Sub-Registrar online API | Out of baseline |

---

## Assumptions

1. Project code is **BHMS**; output root is `BDA_Housing_Management/`.
2. Production SOW `SoW_BHMS_Detailed.md` is the scope source of truth.
3. Booking model is first-come-first-served; payments are online-only in baseline.
4. Documents and workflows are estimated inside owning business features.
5. Payment Gateway Very High connector hours belong in Module 13; Module 08 consumes the hub.
6. DigiLocker/eKYC remain optional commercial line items under Module 13.

---

## Risks

1. Concurrent booking races under high load may expand Module 07 concurrency design effort.
2. Offline registration data quality (SRO fields/deed scans) may delay Module 09 acceptance.
3. Auto-cancellation and refund parameter changes mid-project can rework Modules 02/08/10.
4. Legacy data quality may expand Module 15 exceptions.
5. Bank NOC template/legal content ownership may delay Module 11 UAT.

---

## Review Checklist

- [x] Major SOW sections map to a module or embedded/out-of-scope note
- [x] No separate Document or Workflow modules
- [x] Business / Technical / Shared types assigned
- [x] Dependencies noted
- [x] Module count practical (15) for feature breakdown
