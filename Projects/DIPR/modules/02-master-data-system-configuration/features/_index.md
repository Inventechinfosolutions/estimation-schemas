# Feature Index — Ultra Detailed
## 02 — Master Data & System Configuration

| Feature ID | Feature Name | UI | API | DB | Int | Test | Doc | Total | Line items | Notes |
|------------|--------------|---:|----:|---:|----:|-----:|----:|------:|-----------:|-------|
| F02-001 | Media & campaign reference masters | 28 | 28 | 9 | 0 | 14 | 4 | 83 | 23 |  |
| F02-002 | Vendor / agency master | 26 | 30 | 7 | 0 | 16 | 4 | 83 | 21 |  |
| F02-003 | Location & geography masters | 32 | 32 | 8 | 0 | 12 | 3 | 87 | 21 |  |
| F02-004 | Notification templates & system parameters | 32 | 28 | 7 | 4 | 16 | 4 | 91 | 22 |  |
| F02-005 | Master search, filter & change audit | 30 | 20 | 6 | 0 | 16 | 4 | 76 | 16 |  |

**Module Total:** **420 hours** · **103 artefact line items**

### Module estimation line-item roll-up

| Area | Hours |
|------|------:|
| UI | 148 |
| API | 138 |
| Database | 37 |
| Integration | 4 |
| Testing | 74 |
| Documentation | 19 |

### Ultra-detailed artefact catalogue

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
