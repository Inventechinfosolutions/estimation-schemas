# AMT — Feature-wise Estimation Summary (Ultra Detailed)

**Project:** Advertisement Monitoring Tool (AMT)  
**All-in:** **4464** · **Go-live:** **4134** · **Optional:** **330**  
**Artefact line items:** **870**  
**Basis:** Estimation Master — every named UI screen, API operation, data entity, integration, test suite, and doc artefact

## 1. Estimation Master roll-up (all-in)

| Area | Hours | % | Artefact rows |
|------|------:|--:|--------------:|
| UI | 1352 | 30.3% | 252 |
| API | 1338 | 30.0% | 229 |
| Database | 292 | 6.5% | 112 |
| Integration | 320 | 7.2% | 26 |
| Testing | 956 | 21.4% | 160 |
| Documentation | 206 | 4.6% | 91 |
| **Total** | **4464** | 100% | **870** |

## 2. Module-wise summary

| # | Module | Type | Feat | Lines | UI | API | DB | Int | Test | Doc | Total | % go-live |
|---|--------|------|-----:|------:|---:|----:|---:|----:|-----:|----:|------:|----------:|
| 01 | User & Access Management | Shared | 5 | 104 | 126 | 158 | 33 | 24 | 100 | 20 | 461 | 8.7% |
| 02 | Master Data & System Configuration | Business | 5 | 103 | 148 | 138 | 37 | 4 | 74 | 19 | 420 | 10.2% |
| 03 | Campaign Management | Business | 7 | 132 | 232 | 220 | 45 | 0 | 122 | 23 | 642 | 15.5% |
| 04 | Creative Asset Inventory | Business | 5 | 81 | 140 | 114 | 23 | 8 | 72 | 12 | 369 | 8.9% |
| 05 | Proof-of-Display Capture & Verification | Business | 6 | 105 | 198 | 176 | 38 | 16 | 116 | 23 | 567 | 11.2% |
| 06 | Mobile Field Application | Business | 5 | 90 | 122 | 158 | 27 | 76 | 116 | 21 | 520 | 12.6% |
| 07 | Reporting & Analytics | Business | 6 | 79 | 168 | 128 | 30 | 8 | 100 | 24 | 458 | 11.1% |
| 08 | Notifications & Alerts | Shared | 4 | 57 | 76 | 66 | 19 | 48 | 62 | 14 | 285 | 5.2% |
| 09 | Integration Hub | Technical | 4 | 57 | 58 | 86 | 19 | 112 | 80 | 22 | 377 | 7.9% |
| 10 | Platform Security & Compliance Controls | Technical | 5 | 62 | 84 | 94 | 21 | 24 | 114 | 28 | 365 | 8.8% |

## 3. Feature roll-up + full artefact catalogue

### 01 — User & Access Management (Shared)

**Module total:** **461 hours** · **104 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F01-001 | User account lifecycle | 26 | 34 | 7 | 0 | 20 | 4 | 91 | 24 | Go-live |
| F01-002 | Role & permission matrix | 32 | 36 | 9 | 0 | 20 | 4 | 101 | 22 | Go-live |
| F01-003 | Optional SSO integration | 24 | 32 | 3 | 16 | 22 | 4 | 101 | 19 | OPTIONAL · SSO optional; IdP/protocol TBD |
| F01-004 | Multi-factor authentication | 26 | 34 | 8 | 8 | 24 | 5 | 105 | 23 | Go-live |
| F01-005 | Access audit trail | 18 | 22 | 6 | 0 | 14 | 3 | 63 | 16 | Go-live |

#### 3.01B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F01-001 | UI | AMT User register with type/status/role filters | Medium | 6 |
| F01-001 | UI | User create profile form (staff/vendor/field) | Medium | 6 |
| F01-001 | UI | User edit profile with vendor master linkage picker | Medium | 6 |
| F01-001 | UI | Role multi-select panel at save | Easy | 4 |
| F01-001 | UI | Activate/deactivate modal with reason capture | Simple | 2 |
| F01-001 | UI | Local account credential reset initiation dialog | Simple | 2 |
| F01-001 | API | List users with search filters and pagination | Medium | 6 |
| F01-001 | API | Get user profile by identifier | Simple | 2 |
| F01-001 | API | Create user with role assignments | Medium | 6 |
| F01-001 | API | Update user profile and role links | Medium | 6 |
| F01-001 | API | Activate user lifecycle transition | Easy | 4 |
| F01-001 | API | Deactivate user with reason | Easy | 4 |
| F01-001 | API | Initiate password/credential reset | Easy | 4 |
| F01-001 | API | Active email uniqueness validation | Simple | 2 |
| F01-001 | Database | User core entity columns | Easy | 2 |
| F01-001 | Database | User–role junction with FK constraints | Easy | 2 |
| F01-001 | Database | Unique active email index | Easy | 2 |
| F01-001 | Database | Vendor FK for vendor user type | Simple | 1 |
| F01-001 | Testing | Create staff/vendor/field happy paths | Medium | 6 |
| F01-001 | Testing | Validation: missing role, duplicate email | Medium | 6 |
| F01-001 | Testing | Deactivate blocks auth; reactivation restore | Easy | 4 |
| F01-001 | Testing | Administrator-only access for other roles | Easy | 4 |
| F01-001 | Documentation | User administration guide (register/lifecycle) | Easy | 2 |
| F01-001 | Documentation | UAT script: vendor user with master linkage | Easy | 2 |
| F01-002 | UI | Role register list with search | Easy | 4 |
| F01-002 | UI | Role create/edit metadata form | Easy | 4 |
| F01-002 | UI | Module permission matrix grid (CRUD/approve/verify) | Complex | 12 |
| F01-002 | UI | Copy permissions from existing role dialog | Medium | 6 |
| F01-002 | UI | Role deactivate confirmation with assigned-user warning | Simple | 2 |
| F01-002 | UI | Read-only permission preview for auditors | Easy | 4 |
| F01-002 | API | List roles with filters | Simple | 2 |
| F01-002 | API | Create and update role metadata | Easy | 4 |
| F01-002 | API | Get permission matrix for role | Easy | 4 |
| F01-002 | API | Persist bulk permission map replace | Complex | 8 |
| F01-002 | API | Clone role permissions from source role | Medium | 6 |
| F01-002 | API | Deactivate role with dependency check | Medium | 6 |
| F01-002 | API | Resolve effective permissions for session | Medium | 6 |
| F01-002 | Database | Role entity | Simple | 1 |
| F01-002 | Database | Permission catalogue seed storage | Easy | 2 |
| F01-002 | Database | Role–permission assignment storage | Medium | 4 |
| F01-002 | Database | Module-scoped permission uniqueness constraints | Easy | 2 |
| F01-002 | Testing | Matrix: campaign approver vs PoD verifier roles | Complex | 8 |
| F01-002 | Testing | Unauthorized module entry denied | Medium | 6 |
| F01-002 | Testing | Role clone and deactivate with assigned users | Medium | 6 |
| F01-002 | Documentation | RBAC configuration handbook | Easy | 2 |
| F01-002 | Documentation | UAT: approver cannot verify PoD | Easy | 2 |
| F01-003 | UI | SSO IdP configuration screen (metadata, certificates) | Medium | 6 |
| F01-003 | UI | IdP attribute-to-AMT field mapping grid | Medium | 6 |
| F01-003 | UI | Login page SSO entry and federation error states | Easy | 4 |
| F01-003 | UI | SSO link status panel on user profile | Simple | 2 |
| F01-003 | UI | JIT provision dry-run test panel | Medium | 6 |
| F01-003 | API | Initiate federated login (auth request) | Complex | 8 |
| F01-003 | API | Consume IdP callback and issue AMT session | Complex | 8 |
| F01-003 | API | JIT create or link user from IdP attributes | Medium | 6 |
| F01-003 | API | SSO configuration CRUD | Medium | 6 |
| F01-003 | API | Apply default role on first SSO login | Easy | 4 |
| F01-003 | Integration | IdP protocol adapter (auth, mapping, retry) | Medium | 16 |
| F01-003 | Database | SSO external identity link on user | Easy | 2 |
| F01-003 | Database | SSO configuration store | Simple | 1 |
| F01-003 | Testing | SSO happy-path login | Medium | 6 |
| F01-003 | Testing | Certificate expiry and invalid signature | Medium | 6 |
| F01-003 | Testing | Deactivated user blocked at SSO | Easy | 4 |
| F01-003 | Testing | JIT role assignment edge cases | Medium | 6 |
| F01-003 | Documentation | SSO setup runbook for DIPR IT | Easy | 2 |
| F01-003 | Documentation | UAT federation sign-off checklist | Easy | 2 |
| F01-004 | UI | MFA enrollment wizard with TOTP QR | Medium | 6 |
| F01-004 | UI | Login MFA TOTP challenge screen | Easy | 4 |
| F01-004 | UI | Login MFA SMS OTP challenge screen | Easy | 4 |
| F01-004 | UI | Admin MFA policy toggles by role | Medium | 6 |
| F01-004 | UI | Backup codes generate and confirm modal | Simple | 2 |
| F01-004 | UI | Admin force-reset MFA for user dialog | Simple | 2 |
| F01-004 | UI | MFA lockout user messaging panel | Simple | 2 |
| F01-004 | API | Enroll TOTP secret and confirm enrollment | Complex | 8 |
| F01-004 | API | Verify MFA challenge at login | Medium | 6 |
| F01-004 | API | Send and verify SMS OTP | Medium | 6 |
| F01-004 | API | Admin read/update MFA policy by role | Medium | 6 |
| F01-004 | API | Generate and invalidate backup codes | Easy | 4 |
| F01-004 | API | Admin reset MFA enrollment for user | Easy | 4 |
| F01-004 | Integration | SMS gateway OTP dispatch (provision) | Easy | 8 |
| F01-004 | Database | MFA enrollment secrets (encrypted) | Medium | 4 |
| F01-004 | Database | MFA policy flags per role | Easy | 2 |
| F01-004 | Database | Backup codes hash storage | Easy | 2 |
| F01-004 | Testing | MFA policy enforced per role | Complex | 8 |
| F01-004 | Testing | Lockout after failed attempts | Medium | 6 |
| F01-004 | Testing | Backup code one-time use | Medium | 6 |
| F01-004 | Testing | TOTP clock skew tolerance | Easy | 4 |
| F01-004 | Documentation | MFA operations guide for administrators | Medium | 3 |
| F01-004 | Documentation | UAT MFA enrollment and recovery scripts | Easy | 2 |
| F01-005 | UI | Access audit register with actor/action filters | Medium | 6 |
| F01-005 | UI | Audit event detail drawer (before/after snapshot) | Easy | 4 |
| F01-005 | UI | Quick date-range presets (today/7d/30d) | Simple | 2 |
| F01-005 | UI | Export filtered audit slice to CSV dialog | Easy | 4 |
| F01-005 | UI | Login failure spike filter chip | Simple | 2 |
| F01-005 | API | Ingest authentication login/logout/failure events | Medium | 6 |
| F01-005 | API | Ingest privilege change events (users/roles) | Medium | 6 |
| F01-005 | API | Query audit register with filters and pagination | Medium | 6 |
| F01-005 | API | Export filtered audit register | Easy | 4 |
| F01-005 | Database | Append-only access audit event storage | Medium | 4 |
| F01-005 | Database | Time-series indexes on actor and timestamp | Easy | 2 |
| F01-005 | Testing | Events on login and permission matrix change | Medium | 6 |
| F01-005 | Testing | Filter combinations and export correctness | Easy | 4 |
| F01-005 | Testing | Append-only immutability enforcement | Easy | 4 |
| F01-005 | Documentation | Access audit register user guide | Easy | 2 |
| F01-005 | Documentation | UAT: trace administrator role change | Simple | 1 |

**Module area roll-up:** UI 126h · API 158h · Database 33h · Integration 24h · Testing 100h · Documentation 20h

### 02 — Master Data & System Configuration (Business)

**Module total:** **420 hours** · **103 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F02-001 | Media & campaign reference masters | 28 | 28 | 9 | 0 | 14 | 4 | 83 | 23 | Go-live |
| F02-002 | Vendor / agency master | 26 | 30 | 7 | 0 | 16 | 4 | 83 | 21 | Go-live |
| F02-003 | Location & geography masters | 32 | 32 | 8 | 0 | 12 | 3 | 87 | 21 | Go-live |
| F02-004 | Notification templates & system parameters | 32 | 28 | 7 | 4 | 16 | 4 | 91 | 22 | Go-live |
| F02-005 | Master search, filter & change audit | 30 | 20 | 6 | 0 | 16 | 4 | 76 | 16 | Go-live |

#### 3.02B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F02-001 | UI | Media channel type maintenance list | Easy | 4 |
| F02-001 | UI | Media channel create/edit form | Easy | 4 |
| F02-001 | UI | Campaign type maintenance list | Easy | 4 |
| F02-001 | UI | Campaign type bilingual label editor | Medium | 6 |
| F02-001 | UI | Campaign status lifecycle lookup screen | Easy | 4 |
| F02-001 | UI | Budget head / scheme code lookup screen | Easy | 4 |
| F02-001 | UI | Deactivate master in-use warning modal | Simple | 2 |
| F02-001 | API | List media channels with filters | Simple | 2 |
| F02-001 | API | CRUD media channel master | Easy | 4 |
| F02-001 | API | List campaign types | Simple | 2 |
| F02-001 | API | CRUD campaign type with localized labels | Medium | 6 |
| F02-001 | API | List and CRUD campaign status with ordering | Easy | 4 |
| F02-001 | API | List and CRUD budget head master | Easy | 4 |
| F02-001 | API | Referential guard on master deactivate | Medium | 6 |
| F02-001 | Database | Media channel entity | Simple | 1 |
| F02-001 | Database | Campaign type entity with i18n labels | Easy | 2 |
| F02-001 | Database | Campaign status and budget head entities | Easy | 2 |
| F02-001 | Database | Cross-master referential guard indexes | Medium | 4 |
| F02-001 | Testing | Deactivate when referenced by active campaign | Medium | 6 |
| F02-001 | Testing | Multilingual label validation | Easy | 4 |
| F02-001 | Testing | Status ordering and code uniqueness | Easy | 4 |
| F02-001 | Documentation | Reference master seeding checklist | Easy | 2 |
| F02-001 | Documentation | UAT reference master walkthrough | Easy | 2 |
| F02-002 | UI | Vendor/agency register with search and pagination | Easy | 4 |
| F02-002 | UI | Vendor profile form (contacts, GST, channels) | Medium | 6 |
| F02-002 | UI | Outdoor/print/digital capability toggles panel | Medium | 6 |
| F02-002 | UI | Vendor document attachment slot list | Easy | 4 |
| F02-002 | UI | Deactivate vendor confirmation with campaign warning | Simple | 2 |
| F02-002 | UI | Vendor quick-view drawer from register | Easy | 4 |
| F02-002 | API | List vendors with filters and pagination | Medium | 6 |
| F02-002 | API | Get vendor profile by id | Simple | 2 |
| F02-002 | API | Create vendor profile | Medium | 6 |
| F02-002 | API | Update vendor profile | Medium | 6 |
| F02-002 | API | Deactivate vendor with assignment eligibility check | Medium | 6 |
| F02-002 | API | Vendor autocomplete for campaign assignment | Easy | 4 |
| F02-002 | Database | Vendor profile entity | Easy | 2 |
| F02-002 | Database | Vendor channel capability flags | Simple | 1 |
| F02-002 | Database | Vendor contact child records | Easy | 2 |
| F02-002 | Database | Active campaign assignment guard index | Easy | 2 |
| F02-002 | Testing | Inactive vendor blocked on campaign assignment | Medium | 6 |
| F02-002 | Testing | Mandatory fields and GST format validation | Easy | 4 |
| F02-002 | Testing | Deactivate vendor with open campaigns | Medium | 6 |
| F02-002 | Documentation | Vendor master administration notes | Easy | 2 |
| F02-002 | Documentation | UAT vendor onboarding script | Easy | 2 |
| F02-003 | UI | District hierarchy tree browser | Medium | 6 |
| F02-003 | UI | Assembly constituency list under district | Easy | 4 |
| F02-003 | UI | Outdoor site location create/edit form | Medium | 6 |
| F02-003 | UI | Latitude/longitude fields with validation hints | Easy | 4 |
| F02-003 | UI | Location list filter by district and site type | Easy | 4 |
| F02-003 | UI | Location map preview pin (read-only) | Medium | 6 |
| F02-003 | UI | Deactivate location confirmation dialog | Simple | 2 |
| F02-003 | API | Geography tree query (district → locations) | Medium | 6 |
| F02-003 | API | List locations with composite filters | Medium | 6 |
| F02-003 | API | Create location with hierarchy FK | Medium | 6 |
| F02-003 | API | Update location coordinates | Easy | 4 |
| F02-003 | API | Deactivate location with active PoD reference check | Medium | 6 |
| F02-003 | API | Location lookup by code for PoD capture | Easy | 4 |
| F02-003 | Database | District/constituency hierarchy storage | Medium | 4 |
| F02-003 | Database | Outdoor site location entity | Easy | 2 |
| F02-003 | Database | Geospatial index for proximity queries | Easy | 2 |
| F02-003 | Testing | Deactivate location referenced by active PoD | Easy | 4 |
| F02-003 | Testing | Invalid coordinate range validation | Easy | 4 |
| F02-003 | Testing | Hierarchy tree navigation and pagination | Easy | 4 |
| F02-003 | Documentation | Geography master seeding guide | Easy | 2 |
| F02-003 | Documentation | UAT district filter on campaign coverage | Simple | 1 |
| F02-004 | UI | Notification template register by channel | Easy | 4 |
| F02-004 | UI | Email template editor with placeholder help | Medium | 6 |
| F02-004 | UI | SMS template editor with length counter | Easy | 4 |
| F02-004 | UI | In-app notification template editor | Easy | 4 |
| F02-004 | UI | System parameters form (PoD/sync/retention) | Medium | 6 |
| F02-004 | UI | Parameter change confirmation with impact summary | Simple | 2 |
| F02-004 | UI | Template preview render modal | Medium | 6 |
| F02-004 | API | List templates by event type | Easy | 4 |
| F02-004 | API | CRUD email notification template | Medium | 6 |
| F02-004 | API | CRUD SMS notification template | Easy | 4 |
| F02-004 | API | CRUD in-app notification template | Easy | 4 |
| F02-004 | API | CRUD system parameters with bounds validation | Medium | 6 |
| F02-004 | API | Preview template with sample campaign payload | Easy | 4 |
| F02-004 | Integration | SMTP test-send hook for template validation | Simple | 4 |
| F02-004 | Database | Template storage with event key | Medium | 4 |
| F02-004 | Database | System parameter key-value store | Easy | 2 |
| F02-004 | Database | Parameter change audit linkage | Simple | 1 |
| F02-004 | Testing | PoD threshold parameter read by downstream rules | Medium | 6 |
| F02-004 | Testing | Placeholder substitution in preview | Easy | 4 |
| F02-004 | Testing | Invalid parameter bounds rejected | Medium | 6 |
| F02-004 | Documentation | System parameter dictionary for operators | Easy | 2 |
| F02-004 | Documentation | UAT template activation checklist | Easy | 2 |
| F02-005 | UI | Unified master search screen with type-ahead | Medium | 6 |
| F02-005 | UI | Search results grouped by master type | Medium | 6 |
| F02-005 | UI | Master record quick-open drawer | Easy | 4 |
| F02-005 | UI | Master change history timeline panel | Easy | 4 |
| F02-005 | UI | Filter by master type and editor user | Easy | 4 |
| F02-005 | UI | Change diff view (before/after fields) | Medium | 6 |
| F02-005 | API | Cross-master federated search | Complex | 8 |
| F02-005 | API | Retrieve change audit trail for master key | Medium | 6 |
| F02-005 | API | List recent master changes with filters | Medium | 6 |
| F02-005 | Database | Change audit linkage to master records | Medium | 4 |
| F02-005 | Database | Search indexing metadata for masters | Easy | 2 |
| F02-005 | Testing | Audit emitted on vendor and parameter edits | Medium | 6 |
| F02-005 | Testing | Search returns correct master types | Medium | 6 |
| F02-005 | Testing | Unauthorized audit access denied | Easy | 4 |
| F02-005 | Documentation | Master audit investigation guide | Easy | 2 |
| F02-005 | Documentation | UAT trace vendor master edit | Easy | 2 |

**Module area roll-up:** UI 148h · API 138h · Database 37h · Integration 4h · Testing 74h · Documentation 19h

### 03 — Campaign Management (Business)

**Module total:** **642 hours** · **132 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F03-001 | Campaign create & maintain | 42 | 46 | 10 | 0 | 20 | 5 | 123 | 24 | Go-live |
| F03-002 | Campaign approval workflow | 42 | 48 | 7 | 0 | 28 | 5 | 130 | 25 | Go-live |
| F03-003 | Scheduling & milestones | 28 | 24 | 4 | 0 | 14 | 3 | 73 | 19 | Go-live |
| F03-004 | Budget & spend tracking | 36 | 30 | 8 | 0 | 16 | 4 | 94 | 19 | Go-live |
| F03-005 | Vendor assignment | 24 | 26 | 4 | 0 | 16 | 2 | 72 | 16 | Go-live |
| F03-006 | Campaign version control | 32 | 24 | 6 | 0 | 16 | 2 | 80 | 15 | Go-live |
| F03-007 | Campaign–PoD linkage | 28 | 22 | 6 | 0 | 12 | 2 | 70 | 14 | Go-live |

#### 3.03B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F03-001 | UI | Campaign register with channel/status filters | Medium | 6 |
| F03-001 | UI | Campaign create wizard step 1 (identity, dates) | Medium | 6 |
| F03-001 | UI | Wizard step 2 multi-channel attribute panels | Complex | 12 |
| F03-001 | UI | Wizard step 3 district coverage and budget head | Medium | 6 |
| F03-001 | UI | Campaign detail summary tabs (overview, channels) | Easy | 4 |
| F03-001 | UI | Draft save and resume banner | Simple | 2 |
| F03-001 | UI | Duplicate campaign from existing dialog | Medium | 6 |
| F03-001 | API | List campaigns with filters and pagination | Medium | 6 |
| F03-001 | API | Create campaign draft | Medium | 6 |
| F03-001 | API | Update campaign profile and channel attributes | Complex | 8 |
| F03-001 | API | Promote draft to valid pre-approval state | Medium | 6 |
| F03-001 | API | Get campaign detail aggregate | Medium | 6 |
| F03-001 | API | Clone campaign from existing template | Medium | 6 |
| F03-001 | API | Validate print/digital/outdoor mandatory attributes | Complex | 8 |
| F03-001 | Database | Campaign core entity | Easy | 2 |
| F03-001 | Database | Per-channel attribute extension storage | Medium | 4 |
| F03-001 | Database | District coverage junction | Easy | 2 |
| F03-001 | Database | Draft status and version pointer | Easy | 2 |
| F03-001 | Testing | Print/digital/outdoor attribute validation matrix | Medium | 6 |
| F03-001 | Testing | Draft to pre-approval transition rules | Medium | 6 |
| F03-001 | Testing | Duplicate campaign data integrity | Easy | 4 |
| F03-001 | Testing | Register filter and pagination combinations | Easy | 4 |
| F03-001 | Documentation | Campaign setup playbook for DIPR staff | Easy | 2 |
| F03-001 | Documentation | UAT multi-channel campaign creation script | Medium | 3 |
| F03-002 | UI | Campaign approval inbox list with SLA badges | Medium | 6 |
| F03-002 | UI | Inbox filters (stage, district, channel) | Easy | 4 |
| F03-002 | UI | Multi-stage approval action panel | Complex | 12 |
| F03-002 | UI | Reject reason modal with mandatory comment | Simple | 2 |
| F03-002 | UI | Request changes panel for campaign originator | Medium | 6 |
| F03-002 | UI | Approval history timeline on campaign detail | Easy | 4 |
| F03-002 | UI | Delegated approver assignment dialog | Medium | 6 |
| F03-002 | UI | Concurrent approval conflict notification | Simple | 2 |
| F03-002 | API | List pending approvals for current approver | Medium | 6 |
| F03-002 | API | Get workflow instance with stage definitions | Medium | 6 |
| F03-002 | API | Approve stage transition | Complex | 8 |
| F03-002 | API | Reject with reason and rollback stage | Complex | 8 |
| F03-002 | API | Resubmit campaign after rework | Medium | 6 |
| F03-002 | API | Record approval comments per stage | Easy | 4 |
| F03-002 | API | Trigger notification on stage change | Medium | 6 |
| F03-002 | API | Read workflow config by campaign type | Easy | 4 |
| F03-002 | Database | Workflow instance and stage state storage | Medium | 4 |
| F03-002 | Database | Approval comment and decision log | Easy | 2 |
| F03-002 | Database | Stage SLA timestamp fields | Simple | 1 |
| F03-002 | Testing | Multi-stage approve happy path | Complex | 8 |
| F03-002 | Testing | Reject and resubmit loop | Complex | 8 |
| F03-002 | Testing | Wrong role cannot approve stage | Medium | 6 |
| F03-002 | Testing | Concurrent approver safe handling | Medium | 6 |
| F03-002 | Documentation | Campaign approval configuration guide | Medium | 3 |
| F03-002 | Documentation | UAT multi-stage sign-off script | Easy | 2 |
| F03-003 | UI | Campaign flight calendar month view | Medium | 6 |
| F03-003 | UI | Channel-specific run window editor | Medium | 6 |
| F03-003 | UI | Milestone list with due dates | Easy | 4 |
| F03-003 | UI | Milestone completion toggle for coordinators | Easy | 4 |
| F03-003 | UI | Schedule conflict warning dialog | Simple | 2 |
| F03-003 | UI | Milestone overdue indicator chips | Simple | 2 |
| F03-003 | UI | Schedule list view (non-Gantt) | Easy | 4 |
| F03-003 | API | Get campaign schedule aggregate | Easy | 4 |
| F03-003 | API | CRUD flight windows per media channel | Medium | 6 |
| F03-003 | API | CRUD campaign milestones | Easy | 4 |
| F03-003 | API | Detect overlapping run windows | Medium | 6 |
| F03-003 | API | Mark milestone complete with timestamp | Easy | 4 |
| F03-003 | Database | Schedule window entity | Easy | 2 |
| F03-003 | Database | Milestone entity with campaign FK | Easy | 2 |
| F03-003 | Testing | Window validation (end before start) | Easy | 4 |
| F03-003 | Testing | Overlap detection across channels | Medium | 6 |
| F03-003 | Testing | Milestone overdue flag computation | Easy | 4 |
| F03-003 | Documentation | Campaign scheduling operations notes | Easy | 2 |
| F03-003 | Documentation | UAT milestone tracking walkthrough | Simple | 1 |
| F03-004 | UI | Campaign budget header summary panel | Medium | 6 |
| F03-004 | UI | Budget line-item spend entry grid | Complex | 12 |
| F03-004 | UI | Spend vs budget variance summary card | Easy | 4 |
| F03-004 | UI | Vendor-wise spend breakdown chart | Medium | 6 |
| F03-004 | UI | Budget revision request form | Medium | 6 |
| F03-004 | UI | Spend locked after campaign closed banner | Simple | 2 |
| F03-004 | API | Get budget and spend summary for campaign | Medium | 6 |
| F03-004 | API | CRUD budget line items | Medium | 6 |
| F03-004 | API | Record actual spend entry with validation | Complex | 8 |
| F03-004 | API | Calculate variance and burn rate | Medium | 6 |
| F03-004 | API | Enforce spend lock on closed campaign | Easy | 4 |
| F03-004 | Database | Budget header and line-item storage | Medium | 4 |
| F03-004 | Database | Spend transaction log | Easy | 2 |
| F03-004 | Database | Budget revision history | Easy | 2 |
| F03-004 | Testing | Over-budget warning rules | Medium | 6 |
| F03-004 | Testing | Closed campaign spend entry blocked | Easy | 4 |
| F03-004 | Testing | Line-item totals reconciliation | Medium | 6 |
| F03-004 | Documentation | Budget tracking notes for finance liaison | Easy | 2 |
| F03-004 | Documentation | UAT variance spot-check script | Easy | 2 |
| F03-005 | UI | Campaign vendor assignment panel | Medium | 6 |
| F03-005 | UI | Vendor picker with channel capability filter | Medium | 6 |
| F03-005 | UI | Assignment scope matrix (district/channel) | Medium | 6 |
| F03-005 | UI | Remove vendor assignment confirmation | Simple | 2 |
| F03-005 | UI | Vendor assignment change history list | Easy | 4 |
| F03-005 | API | List vendor assignments for campaign | Easy | 4 |
| F03-005 | API | Assign vendor with district/channel scope | Medium | 6 |
| F03-005 | API | Update assignment scope | Medium | 6 |
| F03-005 | API | Remove assignment with active PoD guard | Easy | 4 |
| F03-005 | API | Validate vendor active and channel-capable | Medium | 6 |
| F03-005 | Database | Campaign–vendor assignment junction | Easy | 2 |
| F03-005 | Database | District and channel scope flags | Easy | 2 |
| F03-005 | Testing | Inactive vendor blocked on assign | Medium | 6 |
| F03-005 | Testing | Outdoor capability mismatch rejected | Medium | 6 |
| F03-005 | Testing | Duplicate assignment prevented | Easy | 4 |
| F03-005 | Documentation | Campaign vendor assignment guide | Easy | 2 |
| F03-006 | UI | Campaign version history list | Easy | 4 |
| F03-006 | UI | Compare versions side-by-side diff panel | Complex | 12 |
| F03-006 | UI | Create new version from approved baseline | Medium | 6 |
| F03-006 | UI | Version label and change summary form | Easy | 4 |
| F03-006 | UI | Read-only approved snapshot view | Medium | 6 |
| F03-006 | API | List campaign versions for lineage | Easy | 4 |
| F03-006 | API | Snapshot campaign state as new version | Complex | 8 |
| F03-006 | API | Get version diff metadata | Medium | 6 |
| F03-006 | API | Promote version to current editable draft | Medium | 6 |
| F03-006 | Database | Version snapshot storage | Medium | 4 |
| F03-006 | Database | Version lineage foreign key | Easy | 2 |
| F03-006 | Testing | Snapshot captures channel attributes | Medium | 6 |
| F03-006 | Testing | Compare highlights changed fields | Medium | 6 |
| F03-006 | Testing | Approved version immutability | Easy | 4 |
| F03-006 | Documentation | Campaign version control user notes | Easy | 2 |
| F03-007 | UI | Campaign PoD coverage planner grid | Medium | 6 |
| F03-007 | UI | Link outdoor sites to campaign PoD slots | Medium | 6 |
| F03-007 | UI | Expected PoD count per site indicator | Easy | 4 |
| F03-007 | UI | PoD linkage status dashboard strip | Medium | 6 |
| F03-007 | UI | Bulk link sites from district filter | Medium | 6 |
| F03-007 | API | List PoD plan slots for campaign | Medium | 6 |
| F03-007 | API | Link or unlink site to PoD plan | Medium | 6 |
| F03-007 | API | Compute expected vs submitted PoD counts | Medium | 6 |
| F03-007 | API | Validate outdoor site geotag present | Easy | 4 |
| F03-007 | Database | Campaign–site PoD plan junction | Medium | 4 |
| F03-007 | Database | Expected capture schedule linkage | Easy | 2 |
| F03-007 | Testing | Counts update when PoD submitted | Medium | 6 |
| F03-007 | Testing | Unlink blocked when verified PoD exists | Medium | 6 |
| F03-007 | Documentation | PoD linkage planning guide for coordinators | Easy | 2 |

**Module area roll-up:** UI 232h · API 220h · Database 45h · Integration 0h · Testing 122h · Documentation 23h

### 04 — Creative Asset Inventory (Business)

**Module total:** **369 hours** · **81 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F04-001 | Asset upload & metadata | 28 | 28 | 8 | 0 | 16 | 2 | 82 | 18 | Go-live |
| F04-002 | Asset versioning | 22 | 18 | 3 | 0 | 10 | 2 | 55 | 14 | Go-live |
| F04-003 | Outdoor geotagging | 38 | 22 | 4 | 8 | 16 | 4 | 92 | 18 | Go-live |
| F04-004 | Inventory search & filter | 30 | 24 | 5 | 0 | 16 | 2 | 77 | 16 | Go-live |
| F04-005 | Asset access & preview | 22 | 22 | 3 | 0 | 14 | 2 | 63 | 15 | Go-live |

#### 3.04B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F04-001 | UI | Creative asset upload drop zone with progress | Medium | 6 |
| F04-001 | UI | Asset metadata form (campaign, channel, language) | Medium | 6 |
| F04-001 | UI | File type and size validation messages | Simple | 2 |
| F04-001 | UI | Bulk upload queue panel | Medium | 6 |
| F04-001 | UI | Upload failure retry list | Easy | 4 |
| F04-001 | UI | Asset thumbnail preview strip | Easy | 4 |
| F04-001 | API | Initiate multipart creative upload | Medium | 6 |
| F04-001 | API | Complete upload and persist metadata | Complex | 8 |
| F04-001 | API | List upload job status | Easy | 4 |
| F04-001 | API | Validate MIME type and size limits | Medium | 6 |
| F04-001 | API | Link uploaded asset to campaign | Easy | 4 |
| F04-001 | Database | Asset binary storage pointer | Easy | 2 |
| F04-001 | Database | Asset metadata entity | Medium | 4 |
| F04-001 | Database | Upload job queue record | Easy | 2 |
| F04-001 | Testing | Happy path for image/PDF/video types | Medium | 6 |
| F04-001 | Testing | Oversize and invalid MIME rejected | Medium | 6 |
| F04-001 | Testing | Bulk partial failure recovery | Easy | 4 |
| F04-001 | Documentation | Creative asset upload operator guide | Easy | 2 |
| F04-002 | UI | Asset version history stack panel | Easy | 4 |
| F04-002 | UI | Upload new creative version dialog | Medium | 6 |
| F04-002 | UI | Version compare preview (image/PDF) | Medium | 6 |
| F04-002 | UI | Mark version approved for PoD reference | Easy | 4 |
| F04-002 | UI | Superseded version banner on detail | Simple | 2 |
| F04-002 | API | List asset versions in lineage | Easy | 4 |
| F04-002 | API | Create new version in lineage | Medium | 6 |
| F04-002 | API | Set active approved version for PoD | Easy | 4 |
| F04-002 | API | Stream version binary for preview | Easy | 4 |
| F04-002 | Database | Version chain FK on asset | Easy | 2 |
| F04-002 | Database | Approved-for-PoD version flag | Simple | 1 |
| F04-002 | Testing | Only approved version used in PoD compare | Medium | 6 |
| F04-002 | Testing | Version rollback blocked after PoD link | Easy | 4 |
| F04-002 | Documentation | Creative version policy notes | Easy | 2 |
| F04-003 | UI | Outdoor geotag map picker (site pin drop) | Very High | 16 |
| F04-003 | UI | Manual latitude/longitude fallback form | Medium | 6 |
| F04-003 | UI | District boundary overlay toggle on map | Medium | 6 |
| F04-003 | UI | Geotag accuracy radius slider | Easy | 4 |
| F04-003 | UI | Geotag summary card on asset detail | Easy | 4 |
| F04-003 | UI | Immutable geotag lock indicator after PoD | Simple | 2 |
| F04-003 | API | Save geotag coordinates on outdoor asset | Medium | 6 |
| F04-003 | API | Validate coordinates against district master | Medium | 6 |
| F04-003 | API | Assist reverse geocode for pin placement | Easy | 4 |
| F04-003 | API | Enforce geotag immutability after PoD link | Medium | 6 |
| F04-003 | Integration | Base map tile / GIS provider hook | Easy | 8 |
| F04-003 | Database | Geotag columns on outdoor asset | Easy | 2 |
| F04-003 | Database | District FK validation constraint | Easy | 2 |
| F04-003 | Testing | District mismatch rejection | Medium | 6 |
| F04-003 | Testing | Immutability after PoD submission | Medium | 6 |
| F04-003 | Testing | Map picker pin drag accuracy | Easy | 4 |
| F04-003 | Documentation | Outdoor geotag capture guidelines | Easy | 2 |
| F04-003 | Documentation | UAT outdoor site pin placement script | Easy | 2 |
| F04-004 | UI | Creative asset inventory register with facets | Medium | 6 |
| F04-004 | UI | Advanced filter drawer (campaign, channel, date) | Medium | 6 |
| F04-004 | UI | Saved search preset chips | Easy | 4 |
| F04-004 | UI | Asset quick preview modal | Easy | 4 |
| F04-004 | UI | Export filtered inventory to CSV | Easy | 4 |
| F04-004 | UI | Full-text search box with hit highlights | Medium | 6 |
| F04-004 | API | Search assets with composite filters | Complex | 8 |
| F04-004 | API | Save and load user search preset | Easy | 4 |
| F04-004 | API | Export search result set | Medium | 6 |
| F04-004 | API | Facet counts for filter panels | Medium | 6 |
| F04-004 | Database | Search indexes on asset metadata | Medium | 4 |
| F04-004 | Database | Saved search preset storage | Simple | 1 |
| F04-004 | Testing | Filter combination correctness | Medium | 6 |
| F04-004 | Testing | Export row limit enforcement | Easy | 4 |
| F04-004 | Testing | RBAC hides unauthorized assets | Medium | 6 |
| F04-004 | Documentation | Asset inventory search user tips | Easy | 2 |
| F04-005 | UI | Asset detail preview page (image/PDF/video) | Medium | 6 |
| F04-005 | UI | Role-based download button visibility | Easy | 4 |
| F04-005 | UI | Watermarked preview for vendor users | Medium | 6 |
| F04-005 | UI | Internal share link expiry dialog | Easy | 4 |
| F04-005 | UI | Access denied explanation panel | Simple | 2 |
| F04-005 | API | Get asset with RBAC permission check | Medium | 6 |
| F04-005 | API | Stream preview rendition | Medium | 6 |
| F04-005 | API | Log asset view and download audit | Easy | 4 |
| F04-005 | API | Generate time-limited internal share token | Medium | 6 |
| F04-005 | Database | Asset access audit log | Easy | 2 |
| F04-005 | Database | Share token store | Simple | 1 |
| F04-005 | Testing | Vendor cannot download without entitlement | Medium | 6 |
| F04-005 | Testing | Watermark applied on vendor preview | Easy | 4 |
| F04-005 | Testing | Expired share link denied | Easy | 4 |
| F04-005 | Documentation | Asset access policy summary | Easy | 2 |

**Module area roll-up:** UI 140h · API 114h · Database 23h · Integration 8h · Testing 72h · Documentation 12h

### 05 — Proof-of-Display Capture & Verification (Business)

**Module total:** **567 hours** · **105 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F05-001 | PoD capture & metadata stamp | 28 | 24 | 6 | 0 | 16 | 4 | 78 | 17 | Go-live |
| F05-002 | Batch PoD upload | 34 | 34 | 6 | 0 | 20 | 4 | 98 | 17 | Go-live |
| F05-003 | Manual verification workflow | 42 | 32 | 6 | 0 | 18 | 5 | 103 | 20 | Go-live |
| F05-004 | PoD validation rules engine | 38 | 32 | 8 | 0 | 26 | 5 | 109 | 18 | Go-live |
| F05-005 | Third-party verification provision | 28 | 32 | 6 | 16 | 20 | 3 | 105 | 17 | OPTIONAL · Third-party PoD vendor/APIs/licenses TBD |
| F05-006 | PoD evidence register | 28 | 22 | 6 | 0 | 16 | 2 | 74 | 16 | Go-live |

#### 3.05B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F05-001 | UI | Single PoD capture form (photo + metadata) | Medium | 6 |
| F05-001 | UI | Camera EXIF auto-fill panel | Easy | 4 |
| F05-001 | UI | Campaign and outdoor site cascaded picker | Medium | 6 |
| F05-001 | UI | Capture timestamp and GPS stamp display | Easy | 4 |
| F05-001 | UI | Submit PoD confirmation summary | Simple | 2 |
| F05-001 | UI | PoD draft save for poor connectivity | Medium | 6 |
| F05-001 | API | Create PoD record with media attachment | Complex | 8 |
| F05-001 | API | Extract and validate EXIF/GPS metadata | Medium | 6 |
| F05-001 | API | Resolve campaign–site PoD linkage | Medium | 6 |
| F05-001 | API | Persist metadata stamp fields on evidence | Easy | 4 |
| F05-001 | Database | PoD evidence core entity | Medium | 4 |
| F05-001 | Database | Metadata stamp columns (GPS, time, device) | Easy | 2 |
| F05-001 | Testing | Happy path with valid EXIF/GPS | Medium | 6 |
| F05-001 | Testing | Missing GPS handling per validation rules | Medium | 6 |
| F05-001 | Testing | Wrong campaign–site linkage rejected | Easy | 4 |
| F05-001 | Documentation | PoD capture field guide for field staff | Easy | 2 |
| F05-001 | Documentation | UAT single PoD submission script | Easy | 2 |
| F05-002 | UI | Batch PoD upload wizard — file selection step | Medium | 6 |
| F05-002 | UI | Batch wizard — column mapping grid | Complex | 12 |
| F05-002 | UI | Batch wizard — validation preview with errors | Medium | 6 |
| F05-002 | UI | Batch progress and per-row status table | Medium | 6 |
| F05-002 | UI | Download batch error report CSV | Easy | 4 |
| F05-002 | API | Initiate batch PoD ingest job | Complex | 8 |
| F05-002 | API | Map spreadsheet rows to PoD entities | Complex | 8 |
| F05-002 | API | Row-level validation before commit | Medium | 6 |
| F05-002 | API | Commit batch with partial success policy | Complex | 8 |
| F05-002 | API | Export batch error report | Easy | 4 |
| F05-002 | Database | Batch job header and row status | Medium | 4 |
| F05-002 | Database | Batch ingest staging table | Easy | 2 |
| F05-002 | Testing | All-valid rows commit successfully | Medium | 6 |
| F05-002 | Testing | Partial failure and rollback policy | Complex | 8 |
| F05-002 | Testing | Column mapping errors surfaced pre-commit | Medium | 6 |
| F05-002 | Documentation | Batch PoD upload template specification | Easy | 2 |
| F05-002 | Documentation | UAT batch ingest script | Easy | 2 |
| F05-003 | UI | PoD verifier work queue with priority sort | Medium | 6 |
| F05-003 | UI | Side-by-side creative vs PoD review screen | Complex | 12 |
| F05-003 | UI | Zoom and pan controls on PoD image | Medium | 6 |
| F05-003 | UI | Accept/reject/rework action panel | Medium | 6 |
| F05-003 | UI | Reject reason code picker modal | Simple | 2 |
| F05-003 | UI | Rework instructions comment box | Easy | 4 |
| F05-003 | UI | Verification status history timeline | Easy | 4 |
| F05-003 | UI | Conflict-of-interest self-declare checkbox | Simple | 2 |
| F05-003 | API | List pending PoD verification queue | Medium | 6 |
| F05-003 | API | Get PoD with linked approved creative asset | Medium | 6 |
| F05-003 | API | Record verifier accept decision | Complex | 8 |
| F05-003 | API | Record reject or rework with reason | Complex | 8 |
| F05-003 | API | Reassign queue item to another verifier | Easy | 4 |
| F05-003 | Database | Verification decision and reason codes | Medium | 4 |
| F05-003 | Database | Verifier assignment log | Easy | 2 |
| F05-003 | Testing | Rework loop until accept | Complex | 8 |
| F05-003 | Testing | Verifier cannot verify own submission | Medium | 6 |
| F05-003 | Testing | Reject reason mandatory validation | Easy | 4 |
| F05-003 | Documentation | Verifier desk procedures | Medium | 3 |
| F05-003 | Documentation | UAT manual verification desk script | Easy | 2 |
| F05-004 | UI | PoD validation rules admin register | Medium | 6 |
| F05-004 | UI | Rule condition builder editor | Complex | 12 |
| F05-004 | UI | Rule priority ordering drag list | Medium | 6 |
| F05-004 | UI | Rule outcome badges on PoD detail view | Easy | 4 |
| F05-004 | UI | Test rule against sample PoD panel | Medium | 6 |
| F05-004 | UI | Rule publish/activate toggle | Easy | 4 |
| F05-004 | API | CRUD PoD validation rule definitions | Medium | 6 |
| F05-004 | API | Evaluate rules on PoD ingest | Very High | 16 |
| F05-004 | API | Re-evaluate rules on demand for PoD | Medium | 6 |
| F05-004 | API | List evaluation results for PoD | Easy | 4 |
| F05-004 | Database | Rule definition storage | Medium | 4 |
| F05-004 | Database | Per-PoD per-rule evaluation result | Medium | 4 |
| F05-004 | Testing | GPS drift distance fail rule | Complex | 8 |
| F05-004 | Testing | Capture timestamp conflict fail | Medium | 6 |
| F05-004 | Testing | Mandatory metadata fail paths | Medium | 6 |
| F05-004 | Testing | Rule priority ordering outcomes | Medium | 6 |
| F05-004 | Documentation | Validation rules catalog for DIPR sign-off | Easy | 2 |
| F05-004 | Documentation | UAT rule pack regression set notes | Medium | 3 |
| F05-005 | UI | Third-party verifier organisation register | Medium | 6 |
| F05-005 | UI | API credential issue and revoke panel | Medium | 6 |
| F05-005 | UI | Outbound PoD queue for external verification | Easy | 4 |
| F05-005 | UI | External status webhook monitor dashboard | Medium | 6 |
| F05-005 | UI | Manual reconcile external decision screen | Medium | 6 |
| F05-005 | API | Register third-party verifier client | Medium | 6 |
| F05-005 | API | Push PoD package to external verifier | Complex | 8 |
| F05-005 | API | Receive callback/webhook verification decision | Complex | 8 |
| F05-005 | API | Reconcile conflicting internal/external decisions | Medium | 6 |
| F05-005 | API | Rotate third-party API credentials | Easy | 4 |
| F05-005 | Integration | External verifier REST adapter (auth, mapping) | Medium | 16 |
| F05-005 | Database | External verifier client registry | Easy | 2 |
| F05-005 | Database | Outbound/inbound integration message log | Medium | 4 |
| F05-005 | Testing | Push and callback happy path | Complex | 8 |
| F05-005 | Testing | Auth failure and retry behaviour | Medium | 6 |
| F05-005 | Testing | Reconcile with internal manual verify | Medium | 6 |
| F05-005 | Documentation | Third-party verification integration runbook | Medium | 3 |
| F05-006 | UI | PoD evidence register with status filters | Medium | 6 |
| F05-006 | UI | Evidence detail with metadata stamp panel | Medium | 6 |
| F05-006 | UI | Chain-of-custody timeline on evidence | Easy | 4 |
| F05-006 | UI | Bulk verification status filter chips | Easy | 4 |
| F05-006 | UI | Register export for audit evidence pack | Medium | 6 |
| F05-006 | UI | Tamper/rule-fail indicator column | Simple | 2 |
| F05-006 | API | Search PoD evidence register | Medium | 6 |
| F05-006 | API | Get evidence detail with media references | Medium | 6 |
| F05-006 | API | Export register slice for audit | Medium | 6 |
| F05-006 | API | Append custody event on evidence access | Easy | 4 |
| F05-006 | Database | Evidence register denormalized view | Medium | 4 |
| F05-006 | Database | Custody event append log | Easy | 2 |
| F05-006 | Testing | Filter by campaign and verification status | Medium | 6 |
| F05-006 | Testing | Export cap and field mask by role | Medium | 6 |
| F05-006 | Testing | Custody events recorded on download | Easy | 4 |
| F05-006 | Documentation | PoD evidence register audit guide | Easy | 2 |

**Module area roll-up:** UI 198h · API 176h · Database 38h · Integration 16h · Testing 116h · Documentation 23h

### 06 — Mobile Field Application (Business)

**Module total:** **520 hours** · **90 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F06-001 | Field task & checklist inbox | 40 | 28 | 4 | 0 | 16 | 4 | 92 | 19 | Go-live |
| F06-002 | Mobile PoD capture | 34 | 26 | 6 | 12 | 24 | 5 | 107 | 20 | Go-live |
| F06-003 | Offline mode & local queue | 16 | 40 | 10 | 0 | 32 | 5 | 103 | 17 | Go-live |
| F06-004 | Sync & conflict resolution | 20 | 46 | 6 | 40 | 28 | 5 | 145 | 19 | Go-live |
| F06-005 | Mobile secure session | 12 | 18 | 1 | 24 | 16 | 2 | 73 | 15 | Go-live |

#### 3.06B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F06-001 | UI | AMT Field Home with sync badge and assignment summary | Easy | 4 |
| F06-001 | UI | Field task inbox list with campaign/site/status filters | Complex | 12 |
| F06-001 | UI | Task detail header with due date and campaign context | Medium | 6 |
| F06-001 | UI | Checklist step panel with mandatory item markers | Medium | 6 |
| F06-001 | UI | Checklist item capture (yes/no, notes, optional photo gate) | Medium | 6 |
| F06-001 | UI | PoD launch shortcut from task when configured | Simple | 2 |
| F06-001 | UI | Pull-to-refresh and empty-state offline hint panel | Easy | 4 |
| F06-001 | API | List assigned field tasks with filters | Medium | 6 |
| F06-001 | API | Fetch task detail and checklist definition | Easy | 4 |
| F06-001 | API | Submit checklist item responses batch | Medium | 6 |
| F06-001 | API | Mark task in-progress/completed transitions | Easy | 4 |
| F06-001 | API | Validate mandatory checklist before PoD eligibility | Complex | 8 |
| F06-001 | Database | Checklist response progress store | Easy | 2 |
| F06-001 | Database | Task status transition audit fields | Easy | 2 |
| F06-001 | Testing | Assigned-only visibility and filter scenarios | Medium | 6 |
| F06-001 | Testing | Mandatory checklist negative before PoD | Medium | 6 |
| F06-001 | Testing | Checklist completion happy path | Easy | 4 |
| F06-001 | Documentation | Field inbox operator guide | Easy | 2 |
| F06-001 | Documentation | Checklist completion business rules appendix | Easy | 2 |
| F06-002 | UI | PoD capture launcher from task context | Simple | 2 |
| F06-002 | UI | Camera live preview with capture controls | Complex | 12 |
| F06-002 | UI | Gallery picker when policy enabled | Easy | 4 |
| F06-002 | UI | GPS/timestamp/device metadata read-only panel | Medium | 6 |
| F06-002 | UI | Image preview retake and quality warning dialog | Medium | 6 |
| F06-002 | UI | Submit confirmation with connectivity/queue status | Easy | 4 |
| F06-002 | API | Initiate mobile PoD capture session with context | Easy | 4 |
| F06-002 | API | Upload PoD media multipart with checksum | Complex | 8 |
| F06-002 | API | Attach GPS/timestamp/device attestation metadata | Medium | 6 |
| F06-002 | API | Finalize PoD submit to verification queue | Complex | 8 |
| F06-002 | Database | Mobile PoD staging record | Medium | 4 |
| F06-002 | Database | Capture metadata extension fields | Easy | 2 |
| F06-002 | Integration | Device GPS location service bridge | Simple | 4 |
| F06-002 | Integration | Device camera and gallery capability bridge | Easy | 8 |
| F06-002 | Testing | Happy path camera capture with GPS | Complex | 8 |
| F06-002 | Testing | Gallery disabled policy negative | Easy | 4 |
| F06-002 | Testing | GPS accuracy threshold failure | Medium | 6 |
| F06-002 | Testing | Media size/quality validation | Medium | 6 |
| F06-002 | Documentation | Mobile PoD field capture SOP | Medium | 3 |
| F06-002 | Documentation | Metadata attestation notes for verifiers | Easy | 2 |
| F06-003 | UI | Global offline banner and connectivity badge | Easy | 4 |
| F06-003 | UI | Queued items list with type and retry status | Medium | 6 |
| F06-003 | UI | Queue item detail with error reason dialog | Easy | 4 |
| F06-003 | UI | Storage quota warning dialog | Simple | 2 |
| F06-003 | API | Connectivity state observer hook | Simple | 2 |
| F06-003 | API | Enqueue PoD media and checklist delta operations | Very High | 16 |
| F06-003 | API | Dequeue and mark-in-flight queue operations | Complex | 8 |
| F06-003 | API | Queue deduplication key validation | Medium | 6 |
| F06-003 | API | Encrypted local persistence read/write layer | Complex | 8 |
| F06-003 | Database | On-device queue entity store | Complex | 6 |
| F06-003 | Database | Staged media blob index | Medium | 4 |
| F06-003 | Testing | App restart queue survival | Complex | 8 |
| F06-003 | Testing | Duplicate enqueue prevention | Medium | 6 |
| F06-003 | Testing | Disk quota handling | Medium | 6 |
| F06-003 | Testing | Offline PoD then online drain smoke | Very High | 12 |
| F06-003 | Documentation | Offline operations field runbook | Medium | 3 |
| F06-003 | Documentation | Queue encryption and retention notes | Easy | 2 |
| F06-004 | UI | Sync progress modal with batch counters | Medium | 6 |
| F06-004 | UI | Background sync status chip on field home | Easy | 4 |
| F06-004 | UI | Conflict resolution choice dialog (server/client/manual) | Medium | 6 |
| F06-004 | UI | Sync failure detail with retry action | Easy | 4 |
| F06-004 | API | Start sync batch with auth gate | Medium | 6 |
| F06-004 | API | Upload queued PoD media chunks | Complex | 8 |
| F06-004 | API | Upload checklist/task delta batch | Complex | 8 |
| F06-004 | API | Server version compare for conflict detection | Complex | 8 |
| F06-004 | API | Apply conflict resolution rule outcome | Very High | 16 |
| F06-004 | Integration | Mobile-to-server delta sync orchestration | Complex | 24 |
| F06-004 | Integration | Exponential backoff retry scheduler | Medium | 16 |
| F06-004 | Database | Sync cursor per device | Easy | 2 |
| F06-004 | Database | Conflict audit and resolution log | Medium | 4 |
| F06-004 | Testing | Server-wins conflict scenario | Complex | 8 |
| F06-004 | Testing | Client-wins with notes merge | Complex | 8 |
| F06-004 | Testing | Auth expiry mid-sync recovery | Medium | 6 |
| F06-004 | Testing | Media integrity failure retry | Medium | 6 |
| F06-004 | Documentation | Sync and conflict DIPR rules matrix | Medium | 3 |
| F06-004 | Documentation | Support troubleshooting guide | Easy | 2 |
| F06-005 | UI | Mobile login screen aligned to AMT branding | Easy | 4 |
| F06-005 | UI | Session timeout warning modal | Simple | 2 |
| F06-005 | UI | Re-authentication prompt on policy violation | Easy | 4 |
| F06-005 | UI | Secure logout confirmation clearing cache | Simple | 2 |
| F06-005 | API | Mobile login and token issuance | Medium | 6 |
| F06-005 | API | Token refresh on idle boundary | Easy | 4 |
| F06-005 | API | Device registration label submit | Easy | 4 |
| F06-005 | API | Secure logout and session revoke | Easy | 4 |
| F06-005 | Integration | Module 01 identity and MFA handoff | Medium | 16 |
| F06-005 | Integration | Optional SSO deep-link return handling | Easy | 8 |
| F06-005 | Database | Device session registration record | Simple | 1 |
| F06-005 | Testing | Session expiry and re-auth flow | Medium | 6 |
| F06-005 | Testing | Failed login throttle alignment | Medium | 6 |
| F06-005 | Testing | Logout clears sensitive local cache | Easy | 4 |
| F06-005 | Documentation | Mobile session policy notes | Easy | 2 |

**Module area roll-up:** UI 122h · API 158h · Database 27h · Integration 76h · Testing 116h · Documentation 21h

### 07 — Reporting & Analytics (Business)

**Module total:** **458 hours** · **79 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F07-001 | Campaign KPI dashboards | 46 | 24 | 6 | 0 | 22 | 5 | 103 | 17 | Go-live |
| F07-002 | Channel-wise spend analytics | 32 | 18 | 6 | 0 | 18 | 5 | 79 | 14 | Go-live |
| F07-003 | Compliance & PoD reports | 28 | 20 | 6 | 0 | 20 | 5 | 79 | 13 | Go-live |
| F07-004 | Audit log export | 12 | 16 | 2 | 0 | 10 | 2 | 42 | 10 | Go-live |
| F07-005 | Scheduled & exportable reports | 40 | 34 | 8 | 8 | 22 | 5 | 117 | 16 | Go-live |
| F07-006 | Role-based report views | 10 | 16 | 2 | 0 | 8 | 2 | 38 | 9 | Go-live |

#### 3.07B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F07-001 | UI | Executive KPI dashboard shell with date/campaign filters | Very High | 16 |
| F07-001 | UI | Campaign status KPI card strip | Medium | 6 |
| F07-001 | UI | PoD verification progress KPI cards | Medium | 6 |
| F07-001 | UI | Field completion funnel chart panel | Complex | 12 |
| F07-001 | UI | Drill-down to campaign list from KPI click | Easy | 4 |
| F07-001 | UI | Role-scoped dashboard empty state | Simple | 2 |
| F07-001 | API | Campaign count aggregates by status | Medium | 6 |
| F07-001 | API | PoD submitted/verified/rejected KPI aggregates | Complex | 8 |
| F07-001 | API | Field task completion rate aggregate | Medium | 6 |
| F07-001 | API | Dashboard filter metadata (campaigns, regions) | Easy | 4 |
| F07-001 | Database | KPI aggregate materialized summary support | Medium | 4 |
| F07-001 | Database | Dashboard query indexes on campaign dates | Easy | 2 |
| F07-001 | Testing | Role-scoped KPI visibility | Complex | 8 |
| F07-001 | Testing | Filter combination accuracy | Medium | 6 |
| F07-001 | Testing | KPI numbers vs source module sample | Complex | 8 |
| F07-001 | Documentation | KPI definition dictionary | Medium | 3 |
| F07-001 | Documentation | Dashboard user interpretation guide | Easy | 2 |
| F07-002 | UI | Spend analytics filter bar (channel, period, campaign) | Medium | 6 |
| F07-002 | UI | Channel spend bar/column chart panel | Complex | 12 |
| F07-002 | UI | Drill-down spend detail grid | Complex | 12 |
| F07-002 | UI | Export current view trigger | Simple | 2 |
| F07-002 | API | Channel spend summary aggregation | Complex | 8 |
| F07-002 | API | Spend detail paginated fetch | Medium | 6 |
| F07-002 | API | Channel master join for labels | Easy | 4 |
| F07-002 | Database | Spend roll-up summary store | Medium | 4 |
| F07-002 | Database | Analytics period partition helpers | Easy | 2 |
| F07-002 | Testing | Spend totals reconciliation sample | Complex | 8 |
| F07-002 | Testing | Unknown channel edge handling | Easy | 4 |
| F07-002 | Testing | Drill-down permission bounds | Medium | 6 |
| F07-002 | Documentation | Spend metric definitions | Medium | 3 |
| F07-002 | Documentation | Reconciliation with campaign budget notes | Easy | 2 |
| F07-003 | UI | Compliance report parameter form | Complex | 12 |
| F07-003 | UI | PoD outcome results grid with status badges | Complex | 12 |
| F07-003 | UI | Report run progress indicator | Easy | 4 |
| F07-003 | API | Build compliance report dataset | Complex | 8 |
| F07-003 | API | PoD verification outcome query | Medium | 6 |
| F07-003 | API | Report export file generation trigger | Medium | 6 |
| F07-003 | Database | Compliance report query views support | Medium | 4 |
| F07-003 | Database | Verification outcome indexed lookups | Easy | 2 |
| F07-003 | Testing | Compliance figures vs PoD source UAT | Complex | 8 |
| F07-003 | Testing | Parameter validation negative cases | Medium | 6 |
| F07-003 | Testing | Large result set pagination | Medium | 6 |
| F07-003 | Documentation | Compliance report field dictionary | Medium | 3 |
| F07-003 | Documentation | Auditor usage notes | Easy | 2 |
| F07-004 | UI | Audit log filter panel (actor, entity, date range) | Medium | 6 |
| F07-004 | UI | Export format and column picker dialog | Easy | 4 |
| F07-004 | UI | Export job status toast/list | Simple | 2 |
| F07-004 | API | Audit log search with pagination | Medium | 6 |
| F07-004 | API | Generate audit export file job | Medium | 6 |
| F07-004 | API | Export download entitlement check | Easy | 4 |
| F07-004 | Database | Audit log range query indexes | Easy | 2 |
| F07-004 | Testing | Export completeness vs filter | Medium | 6 |
| F07-004 | Testing | Unauthorized export negative | Easy | 4 |
| F07-004 | Documentation | Audit export usage notes | Easy | 2 |
| F07-005 | UI | Report catalogue picker for export | Medium | 6 |
| F07-005 | UI | On-demand export dialog (format, filters) | Complex | 12 |
| F07-005 | UI | Schedule configuration wizard steps | Very High | 16 |
| F07-005 | UI | Scheduled job list with next-run display | Medium | 6 |
| F07-005 | API | Render report to PDF/Excel job | Very High | 16 |
| F07-005 | API | Create/update report schedule | Complex | 8 |
| F07-005 | API | Cancel/pause scheduled report job | Easy | 4 |
| F07-005 | API | Fetch report job status and download link | Medium | 6 |
| F07-005 | Integration | Scheduled completion email via Module 08 | Easy | 8 |
| F07-005 | Database | Report job queue persistence | Medium | 4 |
| F07-005 | Database | Schedule recurrence rule storage | Medium | 4 |
| F07-005 | Testing | One-off export format validation | Complex | 8 |
| F07-005 | Testing | Scheduled cron fire mock | Complex | 8 |
| F07-005 | Testing | Failed job retry notification | Medium | 6 |
| F07-005 | Documentation | Report scheduling admin guide | Medium | 3 |
| F07-005 | Documentation | Supported formats matrix | Easy | 2 |
| F07-006 | UI | Report catalogue entitlement matrix admin grid | Medium | 6 |
| F07-006 | UI | Preview report as role simulator panel | Easy | 4 |
| F07-006 | API | List reports with effective entitlement | Medium | 6 |
| F07-006 | API | Save role-to-report mapping updates | Easy | 4 |
| F07-006 | API | Enforce entitlement on report render requests | Medium | 6 |
| F07-006 | Database | Role-report mapping table | Easy | 2 |
| F07-006 | Testing | Cross-role visibility negative tests | Easy | 4 |
| F07-006 | Testing | Verifier vs admin catalogue diff | Easy | 4 |
| F07-006 | Documentation | Report RBAC configuration notes | Easy | 2 |

**Module area roll-up:** UI 168h · API 128h · Database 30h · Integration 8h · Testing 100h · Documentation 24h

### 08 — Notifications & Alerts (Shared)

**Module total:** **285 hours** · **57 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F08-001 | In-app notification centre | 28 | 18 | 6 | 0 | 16 | 3 | 71 | 17 | Go-live |
| F08-002 | Email notification dispatch | 10 | 18 | 3 | 24 | 16 | 4 | 75 | 14 | Go-live |
| F08-003 | SMS notification provision | 14 | 14 | 2 | 24 | 14 | 4 | 72 | 14 | OPTIONAL · SMS gateway credentials TBD |
| F08-004 | Notification preference & delivery log | 24 | 16 | 8 | 0 | 16 | 3 | 67 | 12 | Go-live |

#### 3.08B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F08-001 | UI | Web notification bell with unread badge | Easy | 4 |
| F08-001 | UI | Web notification centre drawer with list | Complex | 12 |
| F08-001 | UI | Notification detail/read expand row | Easy | 4 |
| F08-001 | UI | Mobile field in-app notification feed | Medium | 6 |
| F08-001 | UI | Mark all read action bar | Simple | 2 |
| F08-001 | API | Create in-app notification on platform events | Medium | 6 |
| F08-001 | API | List notifications with pagination | Easy | 4 |
| F08-001 | API | Mark single notification read | Simple | 2 |
| F08-001 | API | Mark all read for user | Simple | 2 |
| F08-001 | API | Unread count aggregate | Easy | 4 |
| F08-001 | Database | In-app notification entity store | Medium | 4 |
| F08-001 | Database | Per-user read state index | Easy | 2 |
| F08-001 | Testing | Event-to-in-app delivery mapping | Medium | 6 |
| F08-001 | Testing | Unread badge accuracy | Easy | 4 |
| F08-001 | Testing | Mobile feed parity | Medium | 6 |
| F08-001 | Documentation | In-app notification event catalogue | Easy | 2 |
| F08-001 | Documentation | Badge polling behaviour notes | Simple | 1 |
| F08-002 | UI | Email template preview panel in admin | Medium | 6 |
| F08-002 | UI | Test send dialog with recipient override | Easy | 4 |
| F08-002 | API | Render notification to email body merge | Complex | 8 |
| F08-002 | API | Queue email dispatch attempt | Medium | 6 |
| F08-002 | API | Record delivery status callback handler | Easy | 4 |
| F08-002 | Integration | SMTP/email gateway connector | Easy | 8 |
| F08-002 | Integration | TLS credential vault binding | Medium | 16 |
| F08-002 | Database | Email dispatch attempt log | Easy | 2 |
| F08-002 | Database | Template version reference fields | Simple | 1 |
| F08-002 | Testing | Template merge with sample events | Medium | 6 |
| F08-002 | Testing | Gateway failure retry behaviour | Medium | 6 |
| F08-002 | Testing | Invalid recipient negative | Easy | 4 |
| F08-002 | Documentation | Email dispatch event list | Easy | 2 |
| F08-002 | Documentation | DIPR SMTP setup checklist | Easy | 2 |
| F08-003 | UI | SMS channel enablement toggle admin | Easy | 4 |
| F08-003 | UI | SMS test send panel | Easy | 4 |
| F08-003 | UI | Provider credential masked form | Medium | 6 |
| F08-003 | API | SMS message render from template | Easy | 4 |
| F08-003 | API | SMS dispatch submit operation | Easy | 4 |
| F08-003 | API | Opt-out flag enforcement check | Medium | 6 |
| F08-003 | Integration | SMS gateway REST connector | Medium | 16 |
| F08-003 | Integration | Credential vault and rate limit | Easy | 8 |
| F08-003 | Database | SMS dispatch attempt log | Easy | 2 |
| F08-003 | Testing | Mock gateway send success | Medium | 6 |
| F08-003 | Testing | Opt-out suppression negative | Easy | 4 |
| F08-003 | Testing | Invalid MSISDN validation | Easy | 4 |
| F08-003 | Documentation | SMS provision checklist for DIPR | Easy | 2 |
| F08-003 | Documentation | Template length and encoding notes | Easy | 2 |
| F08-004 | UI | User notification preference settings screen | Complex | 12 |
| F08-004 | UI | Channel opt-in/opt-out per event category | Medium | 6 |
| F08-004 | UI | Delivery log viewer with filters | Medium | 6 |
| F08-004 | API | Fetch user notification preferences | Easy | 4 |
| F08-004 | API | Save preference updates with policy bounds | Medium | 6 |
| F08-004 | API | Query delivery log paginated | Medium | 6 |
| F08-004 | Database | User preference persistence | Medium | 4 |
| F08-004 | Database | Delivery log append-only store | Medium | 4 |
| F08-004 | Testing | Policy bounds on mandatory alerts | Medium | 6 |
| F08-004 | Testing | Delivery log accuracy vs dispatch | Medium | 6 |
| F08-004 | Testing | Preference change audit | Easy | 4 |
| F08-004 | Documentation | Notification preference policy guide | Medium | 3 |

**Module area roll-up:** UI 76h · API 66h · Database 19h · Integration 48h · Testing 62h · Documentation 14h

### 09 — Integration Hub (Technical)

**Module total:** **377 hours** · **57 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F09-001 | Secure REST API gateway | 12 | 30 | 6 | 32 | 22 | 6 | 108 | 16 | Go-live |
| F09-002 | DIPR system connectors | 22 | 22 | 6 | 40 | 26 | 6 | 122 | 15 | Go-live |
| F09-003 | Third-party analytics provision | 8 | 12 | 1 | 16 | 10 | 5 | 52 | 11 | OPTIONAL · Third-party analytics vendor TBD |
| F09-004 | Integration auth, failure & reconciliation | 16 | 22 | 6 | 24 | 22 | 5 | 95 | 15 | Go-live |

#### 3.09B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F09-001 | UI | API client register form | Easy | 4 |
| F09-001 | UI | Client scope assignment matrix | Medium | 6 |
| F09-001 | UI | Client secret rotate confirmation | Simple | 2 |
| F09-001 | API | External campaign read resource handler | Complex | 8 |
| F09-001 | API | External PoD status read resource handler | Complex | 8 |
| F09-001 | API | External vendor assignment read handler | Medium | 6 |
| F09-001 | API | Client credentials token exchange | Complex | 8 |
| F09-001 | Integration | Gateway rate limiting middleware | Medium | 16 |
| F09-001 | Integration | OAuth2/client credential auth middleware | Medium | 16 |
| F09-001 | Database | API client registry | Medium | 4 |
| F09-001 | Database | Issued token metadata | Easy | 2 |
| F09-001 | Testing | AuthZ scope negative tests | Complex | 8 |
| F09-001 | Testing | Rate limit breach response | Medium | 6 |
| F09-001 | Testing | Contract smoke for agreed entities | Complex | 8 |
| F09-001 | Documentation | External API consumer guide | Complex | 4 |
| F09-001 | Documentation | Client onboarding checklist | Easy | 2 |
| F09-002 | UI | Connector list with health status | Medium | 6 |
| F09-002 | UI | Field mapping maintenance grid | Complex | 12 |
| F09-002 | UI | Manual replay trigger dialog | Easy | 4 |
| F09-002 | API | Connector job enqueue from platform events | Complex | 8 |
| F09-002 | API | Transform pipeline apply mapping | Complex | 8 |
| F09-002 | API | Fetch connector run history | Medium | 6 |
| F09-002 | Integration | DIPR primary system adapter (baseline) | Complex | 24 |
| F09-002 | Integration | DIPR secondary reference sync adapter | Medium | 16 |
| F09-002 | Database | Connector mapping configuration store | Medium | 4 |
| F09-002 | Database | Connector run state and last cursor | Easy | 2 |
| F09-002 | Testing | Mock DIPR endpoint happy path | Very High | 12 |
| F09-002 | Testing | Mapping regression on schema drift | Complex | 8 |
| F09-002 | Testing | Partial failure retry | Medium | 6 |
| F09-002 | Documentation | Connector setup workbook | Complex | 4 |
| F09-002 | Documentation | Mapping change control notes | Easy | 2 |
| F09-003 | UI | Analytics connector enablement form | Easy | 4 |
| F09-003 | UI | Export batch status monitor | Easy | 4 |
| F09-003 | API | Build analytics export batch payload | Easy | 4 |
| F09-003 | API | Submit batch to provisioned endpoint | Medium | 6 |
| F09-003 | API | Fetch last export cursor status | Simple | 2 |
| F09-003 | Integration | Third-party analytics vendor adapter shell | Medium | 16 |
| F09-003 | Database | Analytics export batch log | Simple | 1 |
| F09-003 | Testing | Mock analytics endpoint connectivity | Easy | 4 |
| F09-003 | Testing | Batch resume after failure | Medium | 6 |
| F09-003 | Documentation | Third-party analytics provision checklist | Medium | 3 |
| F09-003 | Documentation | Data fields shared with vendor | Easy | 2 |
| F09-004 | UI | Integration failure queue list | Medium | 6 |
| F09-004 | UI | Failure detail with payload redaction view | Easy | 4 |
| F09-004 | UI | Reconciliation report results grid | Medium | 6 |
| F09-004 | API | List failed integration attempts | Medium | 6 |
| F09-004 | API | Retry single failure with backoff | Complex | 8 |
| F09-004 | API | Run reconciliation compare job | Complex | 8 |
| F09-004 | Integration | Shared credential vault refresh helpers | Medium | 16 |
| F09-004 | Integration | Token expiry proactive refresh scheduler | Easy | 8 |
| F09-004 | Database | Failure queue persistence | Medium | 4 |
| F09-004 | Database | Reconciliation run summary store | Easy | 2 |
| F09-004 | Testing | Retry exhaustion to dead letter | Complex | 8 |
| F09-004 | Testing | Reconciliation mismatch surfacing | Complex | 8 |
| F09-004 | Testing | Credential refresh on 401 | Medium | 6 |
| F09-004 | Documentation | Integration failure runbook | Medium | 3 |
| F09-004 | Documentation | Reconciliation sign-off template | Easy | 2 |

**Module area roll-up:** UI 58h · API 86h · Database 19h · Integration 112h · Testing 80h · Documentation 22h

### 10 — Platform Security & Compliance Controls (Technical)

**Module total:** **365 hours** · **62 artefact line items**

#### 3.{s['nn']}A Feature totals by work area

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Lines | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|------:|-------|
| F10-001 | Encryption & secure storage controls | 4 | 18 | 6 | 16 | 20 | 5 | 69 | 13 | Go-live |
| F10-002 | Data retention & archival policy | 22 | 30 | 10 | 0 | 20 | 6 | 88 | 14 | Go-live |
| F10-003 | Security hardening & OWASP controls | 2 | 18 | 2 | 0 | 26 | 6 | 54 | 10 | Go-live |
| F10-004 | Accessibility & multilingual framework | 40 | 10 | 2 | 0 | 26 | 6 | 84 | 12 | Go-live |
| F10-005 | VAPT remediation support | 16 | 18 | 1 | 8 | 22 | 5 | 70 | 13 | Go-live |

#### 3.10B Ultra-detailed artefact line items

| Feature ID | Area | Artefact | Complexity | Hours |
|------------|------|----------|------------|------:|
| F10-001 | UI | Encryption status diagnostics panel (admin) | Easy | 4 |
| F10-001 | API | Application-layer encrypt/decrypt helpers | Complex | 8 |
| F10-001 | API | Key rotation hook orchestration | Medium | 6 |
| F10-001 | API | Sensitive field redaction in logs | Easy | 4 |
| F10-001 | Integration | Database TDE/at-rest configuration alignment | Easy | 8 |
| F10-001 | Integration | Media object store SSE configuration | Easy | 8 |
| F10-001 | Database | Encryption key metadata registry | Medium | 4 |
| F10-001 | Database | Sensitive column classification tags | Easy | 2 |
| F10-001 | Testing | At-rest encryption verification | Complex | 8 |
| F10-001 | Testing | TLS enforcement on endpoints | Medium | 6 |
| F10-001 | Testing | Key rotation smoke on sample entity | Medium | 6 |
| F10-001 | Documentation | Encryption control matrix for DIPR | Medium | 3 |
| F10-001 | Documentation | PoD media storage security notes | Easy | 2 |
| F10-002 | UI | Retention category policy list | Complex | 12 |
| F10-002 | UI | Category retention rule edit form | Medium | 6 |
| F10-002 | UI | Archival job history viewer | Easy | 4 |
| F10-002 | API | Save retention policy category rules | Medium | 6 |
| F10-002 | API | Run retention evaluation scheduler job | Complex | 8 |
| F10-002 | API | Execute archival move to cold store | Complex | 8 |
| F10-002 | API | Disposal purge with approval gate | Complex | 8 |
| F10-002 | Database | Retention policy configuration | Complex | 6 |
| F10-002 | Database | Job run history and legal hold flags | Medium | 4 |
| F10-002 | Testing | Sample data retention elapsed UAT | Complex | 8 |
| F10-002 | Testing | Legal hold blocks disposal | Medium | 6 |
| F10-002 | Testing | Archival restore smoke | Medium | 6 |
| F10-002 | Documentation | Retention administrator guide | Complex | 4 |
| F10-002 | Documentation | DIPR disposal approval workflow notes | Easy | 2 |
| F10-003 | UI | Security headers/cookie diagnostic read-only panel | Simple | 2 |
| F10-003 | API | Central input validation middleware | Complex | 8 |
| F10-003 | API | CSRF and session hardening hooks | Medium | 6 |
| F10-003 | API | Security event capture emitters | Easy | 4 |
| F10-003 | Database | Security event log support fields | Easy | 2 |
| F10-003 | Testing | OWASP Top 10 oriented test pack | Very High | 12 |
| F10-003 | Testing | Scan finding remediation regression | Complex | 8 |
| F10-003 | Testing | Mobile API auth bypass negative | Medium | 6 |
| F10-003 | Documentation | Security hardening checklist for DIPR | Complex | 4 |
| F10-003 | Documentation | Middleware configuration reference | Easy | 2 |
| F10-004 | UI | Global language switcher component | Medium | 6 |
| F10-004 | UI | Accessible form control library baseline | Very High | 16 |
| F10-004 | UI | Accessible data table patterns for reports | Complex | 12 |
| F10-004 | UI | Focus order and skip-link layout shell | Medium | 6 |
| F10-004 | API | Persist user locale preference | Medium | 6 |
| F10-004 | API | Serve localized label bundles | Easy | 4 |
| F10-004 | Database | User locale preference store | Easy | 2 |
| F10-004 | Testing | WCAG checks on campaign dashboard journey | Very High | 12 |
| F10-004 | Testing | WCAG checks on field mobile login journey | Complex | 8 |
| F10-004 | Testing | Kannada/English label coverage sample | Medium | 6 |
| F10-004 | Documentation | Accessibility developer guidelines | Complex | 4 |
| F10-004 | Documentation | i18n string contribution guide | Easy | 2 |
| F10-005 | UI | VAPT finding register list | Medium | 6 |
| F10-005 | UI | Finding detail with severity and CVE refs | Medium | 6 |
| F10-005 | UI | Evidence attachment upload panel | Easy | 4 |
| F10-005 | API | Create/update finding status workflow | Complex | 8 |
| F10-005 | API | Attach remediation evidence metadata | Easy | 4 |
| F10-005 | API | Export finding closure pack | Medium | 6 |
| F10-005 | Integration | VAPT tooling import/handoff file ingest | Easy | 8 |
| F10-005 | Database | VAPT finding register | Simple | 1 |
| F10-005 | Testing | Retest pass on remediated finding | Very High | 12 |
| F10-005 | Testing | Reopen on regression | Medium | 6 |
| F10-005 | Testing | Evidence access RBAC | Easy | 4 |
| F10-005 | Documentation | VAPT closure evidence template | Medium | 3 |
| F10-005 | Documentation | Retest request checklist | Easy | 2 |

**Module area roll-up:** UI 84h · API 94h · Database 21h · Integration 24h · Testing 114h · Documentation 28h

## 4. Optional commercial line items (with nested artefacts)


### F01-003 — Optional SSO integration (101h)

Condition: SSO optional; IdP/protocol TBD

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | SSO IdP configuration screen (metadata, certificates) | Medium | 6 |
| UI | IdP attribute-to-AMT field mapping grid | Medium | 6 |
| UI | Login page SSO entry and federation error states | Easy | 4 |
| UI | SSO link status panel on user profile | Simple | 2 |
| UI | JIT provision dry-run test panel | Medium | 6 |
| API | Initiate federated login (auth request) | Complex | 8 |
| API | Consume IdP callback and issue AMT session | Complex | 8 |
| API | JIT create or link user from IdP attributes | Medium | 6 |
| API | SSO configuration CRUD | Medium | 6 |
| API | Apply default role on first SSO login | Easy | 4 |
| Integration | IdP protocol adapter (auth, mapping, retry) | Medium | 16 |
| Database | SSO external identity link on user | Easy | 2 |
| Database | SSO configuration store | Simple | 1 |
| Testing | SSO happy-path login | Medium | 6 |
| Testing | Certificate expiry and invalid signature | Medium | 6 |
| Testing | Deactivated user blocked at SSO | Easy | 4 |
| Testing | JIT role assignment edge cases | Medium | 6 |
| Documentation | SSO setup runbook for DIPR IT | Easy | 2 |
| Documentation | UAT federation sign-off checklist | Easy | 2 |

### F05-005 — Third-party verification provision (105h)

Condition: Third-party PoD vendor/APIs/licenses TBD

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Third-party verifier organisation register | Medium | 6 |
| UI | API credential issue and revoke panel | Medium | 6 |
| UI | Outbound PoD queue for external verification | Easy | 4 |
| UI | External status webhook monitor dashboard | Medium | 6 |
| UI | Manual reconcile external decision screen | Medium | 6 |
| API | Register third-party verifier client | Medium | 6 |
| API | Push PoD package to external verifier | Complex | 8 |
| API | Receive callback/webhook verification decision | Complex | 8 |
| API | Reconcile conflicting internal/external decisions | Medium | 6 |
| API | Rotate third-party API credentials | Easy | 4 |
| Integration | External verifier REST adapter (auth, mapping) | Medium | 16 |
| Database | External verifier client registry | Easy | 2 |
| Database | Outbound/inbound integration message log | Medium | 4 |
| Testing | Push and callback happy path | Complex | 8 |
| Testing | Auth failure and retry behaviour | Medium | 6 |
| Testing | Reconcile with internal manual verify | Medium | 6 |
| Documentation | Third-party verification integration runbook | Medium | 3 |

### F08-003 — SMS notification provision (72h)

Condition: SMS gateway credentials TBD

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | SMS channel enablement toggle admin | Easy | 4 |
| UI | SMS test send panel | Easy | 4 |
| UI | Provider credential masked form | Medium | 6 |
| API | SMS message render from template | Easy | 4 |
| API | SMS dispatch submit operation | Easy | 4 |
| API | Opt-out flag enforcement check | Medium | 6 |
| Integration | SMS gateway REST connector | Medium | 16 |
| Integration | Credential vault and rate limit | Easy | 8 |
| Database | SMS dispatch attempt log | Easy | 2 |
| Testing | Mock gateway send success | Medium | 6 |
| Testing | Opt-out suppression negative | Easy | 4 |
| Testing | Invalid MSISDN validation | Easy | 4 |
| Documentation | SMS provision checklist for DIPR | Easy | 2 |
| Documentation | Template length and encoding notes | Easy | 2 |

### F09-003 — Third-party analytics provision (52h)

Condition: Third-party analytics vendor TBD

| Area | Artefact | Complexity | Hours |
|------|----------|------------|------:|
| UI | Analytics connector enablement form | Easy | 4 |
| UI | Export batch status monitor | Easy | 4 |
| API | Build analytics export batch payload | Easy | 4 |
| API | Submit batch to provisioned endpoint | Medium | 6 |
| API | Fetch last export cursor status | Simple | 2 |
| Integration | Third-party analytics vendor adapter shell | Medium | 16 |
| Database | Analytics export batch log | Simple | 1 |
| Testing | Mock analytics endpoint connectivity | Easy | 4 |
| Testing | Batch resume after failure | Medium | 6 |
| Documentation | Third-party analytics provision checklist | Medium | 3 |
| Documentation | Data fields shared with vendor | Easy | 2 |

## 5. Effort profile — top 15 features

| Feature ID | Name | Hours | Lines | Module |
|------------|------|------:|------:|--------|
| F06-004 | Sync & conflict resolution | 145 | 19 | 06 |
| F03-002 | Campaign approval workflow | 130 | 25 | 03 |
| F03-001 | Campaign create & maintain | 123 | 24 | 03 |
| F09-002 | DIPR system connectors | 122 | 15 | 09 |
| F07-005 | Scheduled & exportable reports | 117 | 16 | 07 |
| F05-004 | PoD validation rules engine | 109 | 18 | 05 |
| F09-001 | Secure REST API gateway | 108 | 16 | 09 |
| F06-002 | Mobile PoD capture | 107 | 20 | 06 |
| F01-004 | Multi-factor authentication | 105 | 23 | 01 |
| F05-005 | Third-party verification provision | 105 | 17 | 05 |
| F05-003 | Manual verification workflow | 103 | 20 | 05 |
| F06-003 | Offline mode & local queue | 103 | 17 | 06 |
| F07-001 | Campaign KPI dashboards | 103 | 17 | 07 |
| F01-002 | Role & permission matrix | 101 | 22 | 01 |
| F01-003 | Optional SSO integration | 101 | 19 | 01 |

## 6. Hours by module type

| Type | Hours |
|------|------:|
| Business | 2976 |
| Shared | 746 |
| Technical | 742 |

## 7. Indicative phasing (18 weeks)

| Phase | Weeks | Focus |
|-------|-------|-------|
| 1 | 1–3 | Requirements & prototype |
| 2 | 4–10 | Core build & integration |
| 3 | 11–14 | Test & UAT |
| 4 | 15–16 | Deploy & train |
| 5 | 17–18 | Stabilize |

## 8. Exclusions (not in feature hours)

- Government hosting hardware / DC tenancy
- Third-party product licenses (PoD verification, analytics, SMS commercial charges)
- Creative production / media buying
- Large legacy archive migration (unless added)
- Permanent DIPR staffing
- Tender EMD / performance guarantee
- Extended AMC beyond Weeks 17–18 (quote separately)
