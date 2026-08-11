# Correct Dimension Report Management System (CDRMS) — Module List

Source: `SoW_CDRMS_Detailed.md`

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User & Access Management | Shared | Users, roles (Engineer / CAO / Super Admin), credentials, engineer geo binding | Explicit in SOW |
| 02 | Master Data & System Configuration | Business | Geo-locations, capture masters, statuses, OTP/media parameters | Explicit in SOW |
| 03 | Mobile Onboarding & Geo Enforcement | Business | OTP login every session, location enablement, geo restriction | Explicit in SOW |
| 04 | Field Site Visit Capture | Business | CDR field capture: site details, dimensions, Check Bandi, directions/width, surroundings, media, submit | Explicit in SOW |
| 05 | CAO Verification & PDF Export | Business | Application review, verify/return/reject, PDF download | Explicit in SOW |
| 06 | Dashboards, KPIs & MIS | Business | Count KPIs for Super Admin and CAO | Explicit in SOW |
| 07 | Notification Service | Technical | SMS OTP for every engineer login | Explicit in SOW |

---

## Module Details

### 01. User & Access Management

- **Type:** Shared
- **Summary:** Enable Super Admin to create and manage users and login credentials, assign engineer geo-location, and control access for Engineer, CAO, and Super Admin.
- **Source:** Explicit in document (SOW §6 Module 01; Section 8)
- **In Scope:**
  - User create/update/search/activate/deactivate
  - Role assignment: Engineer, CAO, Super Admin
  - Engineer credentials bound to exactly one geo-location
  - CAO and Super Admin web credentials
  - Credential reset and access deactivation
  - Data scoping: engineer own applications / assigned geo only
- **Out of Scope:**
  - Post/Person organisational hierarchy (deferred per SOW)
  - External IdP / SSO unless later specified
- **Key Actors:** Super Admin; (affects Engineer, CAO)
- **Dependencies:** None (foundation); uses Geo-Location master from Module 02 for binding
- **Notes:** Access model is user → role (Engineer / CAO / Super Admin) with engineer geo binding.

---

### 02. Master Data & System Configuration

- **Type:** Business
- **Summary:** Provide configurable masters and system parameters used by mobile capture and web administration / KPIs.
- **Source:** Explicit in document (SOW §6 Module 02)
- **In Scope:**
  - Geo-location master for engineer assignment and filters
  - Site visit attribute masters (category/type, shape regular/odd-irregular, road type, surrounding feature types)
  - Application status master (Draft, Submitted, Returned, Verified, Rejected)
  - System parameters: OTP validity, max photo count/size, max video size, session timeout, PDF template metadata
  - Activate/deactivate masters; search/filter/export
- **Out of Scope:**
  - Transactional CDR / site-visit applications (Module 04)
  - Standalone Document Management product
- **Key Actors:** Super Admin
- **Dependencies:** Module 01 (admin access)
- **Notes:** Masters support Modules 03–06 capture and verification.

---

### 03. Mobile Onboarding & Geo Enforcement

- **Type:** Business
- **Summary:** Ensure provisioned engineers access the mobile app via OTP on every login, enable location services, and operate only within assigned geo-location.
- **Source:** Explicit in document (SOW §6 Module 03; workflows 7.2)
- **In Scope:**
  - Engineer mobile login (no OTP-free access)
  - Mandatory OTP validation every session; fresh OTP after logout/expiry
  - Mandatory device location enablement for capture
  - Assigned geo-location enforcement (client + server)
  - Engineer profile view (identity, assigned location)
- **Out of Scope:**
  - Offline sync / offline capture (online-only per SOW)
  - Field capture forms (Module 04)
  - SMS gateway implementation details beyond consuming OTP (Module 07)
- **Key Actors:** Engineer
- **Dependencies:** Modules 01, 02, 07
- **Notes:** OTP delivery is Module 07; enforcement rules live here.

---

### 04. Field Site Visit Capture

- **Type:** Business
- **Summary:** Enable engineers to capture CDR-related site-visit applications: site details, dimensions (including odd/irregular), Check Bandi, directions with width, surroundings per direction, photos/video, and submit.
- **Source:** Explicit in document (SOW §6 Module 04)
- **In Scope:**
  - Create/draft/submit site-visit (CDR) applications online
  - Site identification and shape/dimensions (regular L×B and odd multi-side)
  - Geo stamp; Check Bandi; directions & mandatory approach width; surroundings per direction
  - Up to 10 photos (max 10 MB each) and one video
  - Validation and submit to CAO queue; engineer status view of own applications
  - Embedded media handling for capture
- **Out of Scope:**
  - CAO verification and PDF generation (Module 05)
  - Offline queue/sync
- **Key Actors:** Engineer
- **Dependencies:** Modules 01, 02, 03
- **Notes:** Photos/video/PDF document handling is embedded (not a separate DMS module).

---

### 05. CAO Verification & PDF Export

- **Type:** Business
- **Summary:** Provide CAO workbench to review submitted applications (including media), verify/return/reject, and download PDF.
- **Source:** Explicit in document (SOW §6 Module 05; workflow 7.4)
- **In Scope:**
  - Application list/search/filter
  - Detail and media review
  - Verify / return / reject with remarks
  - PDF generation and download
  - Resubmission handling after return
  - Embedded verification workflow
- **Out of Scope:**
  - Engineer field capture (Module 04)
  - Advanced MIS / custom report builder
- **Key Actors:** CAO; Engineer (resubmit after return)
- **Dependencies:** Modules 01, 02, 04
- **Notes:** Verification workflow embedded in this module.

---

### 06. Dashboards, KPIs & MIS

- **Type:** Business
- **Summary:** Provide operational count KPIs for Super Admin and CAO.
- **Source:** Explicit in document (SOW §6 Module 06)
- **In Scope:**
  - Super Admin counts: active engineers, applications by status / geo / period
  - CAO counts: pending, verified, returned, rejected
  - Date-range and geo-location filters
  - Excel/CSV export of count tables
- **Out of Scope:**
  - Custom report builder / BI suite
- Drill-down product beyond filtered lists where already in Module 05
- **Key Actors:** Super Admin, CAO
- **Dependencies:** Modules 01, 04, 05
- **Notes:** Keep to simple counts per SOW minimal scope.

---

### 07. Notification Service

- **Type:** Technical
- **Summary:** SMS OTP dispatch and validation support for every engineer mobile login.
- **Source:** Explicit in document (SOW §6 Module 07; Integrations)
- **In Scope:**
  - SMS OTP send for every engineer login
  - OTP length, expiry, resend cooldown, max attempts (parameters from Module 02)
  - OTP delivery logging
- **Out of Scope:**
  - Status SMS workflows (not in baseline SOW)
  - Email gateway product (optional in SOW integrations)
- **Key Actors:** System; Engineer (receives OTP)
- **Dependencies:** Module 02 (parameters); SMS gateway (external)
- **Notes:** Consumed by Module 03 login flow.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Document / media storage | Embedded in Modules 04 and 05 (photos, video, PDF) |
| CAO verification workflow | Embedded in Module 05 |
| Audit logging | System-wide NFR (SOW §11); not a separate module |
| Search/filter on lists | Standard within Modules 02, 05, 06 |
| API / Integration Hub | Not a standalone module; SMS gateway consumed by Module 07; other integrations out of scope / optional |
| Offline sync | Explicitly out of scope (online-only) |
| Post/Person org model | Deferred; not in baseline SOW |
| Citizen / public portal | Out of scope |
| Payment gateway | Out of scope |

---

## Assumptions

1. Production SOW `SoW_CDRMS_Detailed.md` is the scope source of truth for module `{NN}` and feature IDs `F{NN}-{SEQ}`.
2. Access model remains user → role (Engineer / CAO / Super Admin) with engineer geo binding.
3. Document management and verification workflow stay embedded (no separate DMS / BPM modules).
4. Notification baseline is OTP SMS only.
5. Phase 1 = Modules 01–07 as listed; Phase 2 only if BDA agrees later.

---

## Risks

1. Geo-enforcement accuracy depends on device GPS quality and master geo definitions — may affect Module 03/04 acceptance.
2. Media volume (10 photos + video per application) may drive storage/performance cost under Module 04/05.
3. SMS OTP reliability (gateway SLAs) affects Module 03 login UX.
4. If BDA later requires Post/Person structures, Module 01 boundaries will need expansion.
5. Online-only constraint may limit field use in poor-connectivity sites — operational risk, not a module gap.

---

**Module slugs (for folders)**

| # | Slug |
|---|------|
| 01 | `user-access-management` |
| 02 | `master-data-system-configuration` |
| 03 | `mobile-onboarding-geo-enforcement` |
| 04 | `field-site-visit-capture` |
| 05 | `cao-verification-pdf-export` |
| 06 | `dashboards-kpis-mis` |
| 07 | `notification-service` |
