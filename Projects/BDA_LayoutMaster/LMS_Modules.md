# BDA Layout Master & Site Management System (LMS) - Module List

Source: `SoW_LMS_Detailed.md`

| # | Module | Type | Summary |
|---|--------|------|---------|
| 01 | User & Role Management | Shared | Auth, roles, permissions, zone/department scope |
| 02 | Master Data & System Configuration | Business | Masters, templates, eligibility, workflow config |
| 03 | Layout Management | Business | Layout lifecycle, docs, publish approval |
| 04 | Site Management & Classification | Business | Site register, classification, approvals, search |
| 05 | Auction Management | Business | Auction cases, notices, results, post-auction |
| 06 | Allotment Management | Business | Application, scrutiny, order, possession |
| 07 | CA Site Management | Business | CA register and allotment/assignment/lease |
| 08 | Land Loser Management | Business | Mark, verify, approve, publish Land Loser |
| 09 | GIS & GeoServer Synchronization | Technical | Bidirectional geometry/attribute sync (Phase 1) |
| 10 | Citizen & Public Portal | Shared | Public search, auction notices, applications |
| 11 | Notification Service | Technical | In-app, SMS, email notifications |
| 12 | API / Integration Hub | Technical | Payment gateway and BDA app integrations |
| 13 | Analytics, Dashboards & Reports | Business | Dashboards, MIS, PDF/Excel export |
| 14 | Data Migration | Shared | Legacy import, validation, reconciliation |

Source notes for each module are in the Module Details sections below.

---

## Module Details

### 01. User & Role Management

- **Type:** Shared
- **Summary:** Provide secure login, role-based access, permission sets, and department/zone data scoping for BDA officers and citizen/applicant portal users.
- **Source:** Explicit in document (bundled under SOW Module 1.D and Sec. 8); extracted as a Shared module per schema defaults (Identity & Access).
- **In Scope:**
  - User create/update, activate/deactivate
  - Roles (indicative list in SOW Sec. 8.1) and permission sets (module + action)
  - Map users to departments, zones, and data scopes
  - Secure authentication; password policy; session timeout; optional 2FA for privileged officer roles
  - Citizen / applicant registration and login for portal services
  - Login history and access-related activity logs
  - Segregation-of-duties support for propose vs approve on classification, auction, allotment, and CA processes
- **Out of Scope:**
  - External IdP / SSO federation unless later specified
  - Full SIEM product; application-level activity logs only
  - Approval workflow *definition* (Module 02); runtime approvals inside business modules
- **Key Actors:** Super Administrator, Auditor, all officer roles (consumers), Citizen / Applicant
- **Dependencies:** None (foundation). Consumed by all modules.
- **Notes:** Workflow configuration remains in Module 02; runtime approvals execute inside Modules 03-08 using roles from this module.

---

### 02. Master Data & System Configuration

- **Type:** Business
- **Summary:** Maintain configurable location, layout/site, and process masters; document types; notice/notification templates; eligibility parameters; and multi-level approval workflow definitions.
- **Source:** Explicit in document (SOW Sec. 6 Module 1), excluding User & Role (moved to Module 01).
- **In Scope:**
  - Location & administrative masters: Country, State, District, Taluk, Village, Hobli, BDA Zone; Section / Division / Department
  - Layout & site masters: Layout Status, Site/Property Status, Site Categories, Reservation Categories, Road Facing, Corner/Intermediate indicators, Block/Sector/Phase/Stage/Section structure codes
  - Document type master
  - Process masters: Auction / Allotment / CA / Land Loser statuses; eligibility rule parameters
  - Notice / circular templates for auction and allotment; notification templates (in-app / SMS / email definitions)
  - Configure multi-level approval workflows by process/category/department (layout publish, site cancellation, special classifications, auction, allotment, CA, Land Loser)
  - Activate/deactivate masters without breaking historical references
  - Search, filter, export of masters; audit of critical configuration changes
- **Out of Scope:**
  - Transactional layout/site registers (Modules 03-04)
  - User/role administration (Module 01)
  - Standalone generic workflow product beyond configurable approval definitions used by business modules
  - Standalone Document Management product (documents embedded in business modules)
- **Key Actors:** Super Administrator, Town Planning / section admins, Data Entry Operator (read for transactional use)
- **Dependencies:** Module 01
- **Notes:** Individual CRUD masters are grouped here intentionally as in the SOW.

---

### 03. Layout Management

- **Type:** Business
- **Summary:** Complete lifecycle of BDA layouts as the parent entity for sites, including structure, status, embedded documents/photos, and optional publish approval.
- **Source:** Explicit in document (SOW Sec. 6 Module 2)
- **In Scope:**
  - Create/update/view/archive layouts with unique layout identity
  - Location capture (State -> District -> Taluk -> Village/Hobli -> BDA Zone), lat/long, survey/boundary details, total area
  - Block, Sector, Phase, Stage, Section information
  - Layout status lifecycle (Draft, Active, Archived, and other BDA-defined statuses)
  - Embedded layout documents and photographs (plans, GOs, acquisition papers, survey sketches, GIS references)
  - Configurable layout create/major-amendment / publish approval workflow
  - Layout view of linked site counts by status and category
  - Layout search by name, code, zone, district, taluk, village, status
- **Out of Scope:**
  - Site create/classify (Module 04)
  - GIS sync engine (Module 09) - layout record may display GIS linkage/status
  - Citizen published view shell (Module 10) - consumes published layout fields
- **Key Actors:** Town Planning Officer, Engineering Section, Zonal Officer, Data Entry Operator, Approvers
- **Dependencies:** Modules 01-02; Module 09 for spatial sync/display; Module 11 for workflow alerts
- **Notes:** Document handling and approvals are embedded; do not split into a Document or Workflow module.

---

### 04. Site Management & Classification

- **Type:** Business
- **Summary:** Site register under layouts, multi-category classification, embedded department-wise classification approvals, site documents, and advanced search.
- **Source:** Explicit in document (SOW Sec. 6 Module 3)
- **In Scope:**
  - Site create/update/view/cancel under a valid layout
  - Numbering, dimensions/area, corner/intermediate, road facing, khata, survey numbers, reservation
  - Legal/litigation flags, key dates, remarks, linked documents (not full case management)
  - Ownership/possession status fields as maintained by BDA
  - Site photographs and supporting documents (embedded)
  - Multi-category classification with effective status
  - Special classification approval workflow before process eligibility (Auction, Land Loser, CA, Commercial, Utility, Reserved, etc.)
  - Advanced multi-parameter search and retrieval
- **Out of Scope:**
  - End-to-end Auction / Allotment / CA / Land Loser case processing (Modules 05-08)
  - Full court case diary beyond flags/dates/documents
  - GIS sync engine (Module 09)
- **Key Actors:** Town Planning, Engineering, Legal, Revenue, Auction, CA, Land Acquisition sections; Approvers; Data Entry Operator
- **Dependencies:** Modules 01-03; Module 09 for GIS availability/display; Module 11 for alerts
- **Notes:** Classification effectiveness gates Modules 05-08. Citizen public search of permitted fields is delivered via Module 10.

---

### 05. Auction Management

- **Type:** Business
- **Summary:** End-to-end auction of classification-approved auction-eligible sites, including cases, notices, participation/results, post-auction updates, and embedded documents/approvals.
- **Source:** Explicit in document (SOW Sec. 6 Module 4)
- **In Scope:**
  - Nomination of eligible sites; departmental approval; **Approved for Auction** status
  - Auction case/batch creation, schedule, mode/terms, EMD/participation conditions
  - Publish notices for citizen visibility (content consumed by Module 10)
  - Participant/bidder registration recording as required by BDA process
  - Proceedings/results recording; cancel/postpone/unsuccessful handling
  - Post-auction site status updates; orders/acknowledgements from templates
  - Link payment/EMD/balance dues recording (payment execution via Module 12 when enabled)
  - Handover outcome signals toward allotment/possession where required
  - Embedded auction documents
- **Out of Scope:**
  - Making non-approved sites auctionable
  - Full accounting/GL (payment recording/integration only)
  - Citizen portal shell (Module 10)
- **Key Actors:** Auction Section, Approvers, Commissioner (as configured), GIS Cell (indirect), Citizen (view/participate via portal)
- **Dependencies:** Modules 01-04; Module 10 for public publication/participation UX; Module 11; Module 12 if online EMD/fees; Module 06 if post-auction allotment formalities
- **Notes:** Exact auction mode (including e-auction mechanics) finalized in requirements workshops within SOW boundaries.

---

### 06. Allotment Management

- **Type:** Business
- **Summary:** End-to-end allotment from eligibility and schemes through application, scrutiny, selection recording, order, acceptance, and possession.
- **Source:** Explicit in document (SOW Sec. 6 Module 5)
- **In Scope:**
  - Eligibility pools/schemes/notifications
  - Officer-assisted and citizen-submitted applications (portal UX via Module 10)
  - Applicant details, preferences, supporting documents, scrutiny, deficiency/resubmission
  - Configurable selection method recording (priority, lottery/draw, committee recommendation)
  - Multi-level allotment approval; allotment order/intimation templates
  - Acceptance/refusal within timelines; prevent double allotment
  - Possession/handover recording; mutations/cancellations/surrender with approval
  - Embedded allotment documents
- **Out of Scope:**
  - Auction bidding/results (Module 05)
  - CA-specific allotment/lease lifecycle (Module 07)
  - Full court eviction process
- **Key Actors:** Revenue / Allotment Section, Approvers, Citizen/Applicant, Data Entry Operator
- **Dependencies:** Modules 01-04; Module 10; Module 11; Module 12 if online fees
- **Notes:** Post-auction allotment formalities may be initiated from Module 05 outcomes.

---

### 07. CA Site Management

- **Type:** Business
- **Summary:** CA site register and CA allotment/assignment/lease lifecycle with approvals, terms, renewals/closures, and master status reflection.
- **Source:** Explicit in document (SOW Sec. 6 Module 6)
- **In Scope:**
  - Maintain CA sites approved via classification
  - Purpose, permitted use, beneficiary type, status
  - Applications/institutional proposals; scrutiny; recommendations; multi-level approval
  - Terms (period, conditions, fees/deposits if applicable); CA orders/agreements from templates
  - Renewals, cancellations, breach/notice status + documents
  - Reflect CA occupancy/availability on site master
  - Embedded CA documents
- **Out of Scope:**
  - General residential allotment (Module 06)
  - Classification approval itself (Module 04)
- **Key Actors:** CA Site Section, Approvers, institutional applicants (via officer and/or portal as enabled)
- **Dependencies:** Modules 01-04; Module 11; Module 10 if citizen/institutional portal paths enabled
- **Notes:** Only classification-approved CA sites enter the CA process pool.

---

### 08. Land Loser Management

- **Type:** Business
- **Summary:** Identify, verify, approve, publish, and correct Land Loser markings with references and supporting documents.
- **Source:** Explicit in document (SOW Sec. 6 Module 7)
- **In Scope:**
  - Propose/mark Land Loser on a site
  - Capture acquisition/beneficiary reference fields as defined by BDA
  - Department verification and multi-level approval
  - Mandatory supporting documents as configured
  - Publish effective Land Loser status on site master
  - Controlled cancellation/correction workflow
- **Out of Scope:**
  - Full land acquisition project management system
  - Downstream compensation payment engine unless later added
- **Key Actors:** Land Acquisition Section, Legal (as configured), Approvers
- **Dependencies:** Modules 01-04; Module 11
- **Notes:** Closely related to classification but retained as a dedicated process module per SOW.

---

### 09. GIS & GeoServer Synchronization

- **Type:** Technical
- **Summary:** Bidirectional synchronization and display of layout/site spatial data with BDA GIS platform and GeoServer, including failure handling and sync audit.
- **Source:** Explicit in document (SOW Sec. 6 Module 8) - **all capabilities mandatory in Phase 1**
- **In Scope:**
  - Retrieve/display layout boundaries, site polygons, and spatial attributes in LMS
  - GIS availability status on layout/site records
  - LMS -> GIS/GeoServer update on create/modify
  - GIS -> LMS sync on create/modify
  - Geometry and attribute change synchronization
  - Retry and exception queues; synchronization logs
  - Operational re-sync/resolution actions; no silent data loss when GIS unavailable
  - Inputs to GIS sync health dashboards (Module 13)
- **Out of Scope:**
  - Replacing the enterprise GIS authoring platform itself
  - General non-GIS integrations (Module 12)
- Hardware/GPS devices
- **Key Actors:** GIS Cell, Super Administrator, Layout/Site officers (consumers of map view)
- **Dependencies:** Modules 03-04 for business records; Module 01 for access; Module 13 for KPI display
- **Notes:** Kept separate from API/Integration Hub because sync scope, exception handling, and Phase 1 criticality warrant an independent implementation unit.

---

### 10. Citizen & Public Portal

- **Type:** Shared
- **Summary:** Public/citizen web channel for permitted published information, auction notices, allotment (and related) applications, and applicant status tracking.
- **Source:** Explicit in document (SOW Sec. 9); separated for implementation as a dual-channel delivery unit.
- **In Scope:**
  - Citizen portal shell, registration/login integration with Module 01
  - Search/view of **published** layout/site fields only (disclosure controls)
  - Published auction notices/schedules/permitted result summaries (data from Module 05)
  - Allotment scheme info, online application/document upload, status tracking (process backend Module 06)
  - Download of applicant-owned orders/acknowledgements where enabled
  - Published circulars/help/contact information
  - Ensure sensitive legal/internal fields are not exposed
- **Out of Scope:**
  - Full officer operational UI (officer portal across business modules)
  - Changing classification/auction business rules (backend modules)
  - Native mobile apps (optional Phase 2)
- **Key Actors:** Citizen / Applicant; BDA content publishers (via officer tools)
- **Dependencies:** Modules 01, 03-07 (as enabled); Module 11 for OTP/notices; Module 12 if portal payments enabled
- **Notes:** Business validations and case state machines remain owned by Modules 05-07; this module owns the public experience and disclosure boundary.

---

### 11. Notification Service

- **Type:** Technical
- **Summary:** Dispatch in-app, SMS, and email notifications for OTPs, workflow alerts, and auction/allotment notices.
- **Source:** Added for implementation (derived from SOW Sec. 4.1, Sec. 10, Module 1 templates)
- **In Scope:**
  - Notification event handling from business modules
  - SMS gateway and email service integration points
  - In-app alerts/worklist notifications
  - Template rendering using Module 02 templates
  - Delivery attempt logging / basic failure visibility
- **Out of Scope:**
  - Marketing campaign platform
  - Template master administration (Module 02)
- **Key Actors:** System (automated); Super Administrator (config); all users (recipients)
- **Dependencies:** Module 02 (templates); Module 01 (recipient identities); Module 12 may share gateway credentials/patterns
- **Notes:** Mandatory SMS/email per SOW integrations table.

---

### 12. API / Integration Hub

- **Type:** Technical
- **Summary:** Secure integration layer for payment gateway (if enabled), publishing validated layout/site master data to other BDA applications, and optional future connectors.
- **Source:** Added for implementation (derived from SOW Sec. 10)
- **In Scope:**
  - Payment gateway connector for auction EMD / allotment fees when mandated
  - Interfaces for other BDA departmental applications to consume approved/validated layout and site data
  - Integration readiness patterns: auth, failure handling, reconciliation hooks as required by RFP response
  - Optional DigiLocker / Aadhaar eKYC placeholders (optional commercial line items)
- **Out of Scope:**
  - GIS/GeoServer bidirectional sync implementation (Module 09)
  - SMS/email send pipeline (Module 11)
  - Full ERP/GL/treasury replacement
- **Key Actors:** Super Administrator, integration/ops counterparts at BDA, consuming system owners
- **Dependencies:** Modules 03-06 for publishable master/process outcomes; Module 01 for API consumers/service accounts as applicable
- **Notes:** Ensures LMS remains authoritative master without embedding foreign systems’ logic.

---

### 13. Analytics, Dashboards & Reports

- **Type:** Business
- **Summary:** Role-based dashboards and exportable MIS/operational reports across layouts, sites, processes, approvals, and GIS sync.
- **Source:** Explicit in document (SOW Sec. 6 Module 9)
- **In Scope:**
  - KPIs listed in SOW Sec. 6.9.1 (totals, distributions, auction/allotment/CA/Land Loser summaries, pendency, GIS sync, recent updates, citizen activity summary)
  - Standard reports listed in SOW Sec. 6.9.2
  - PDF/Excel export
  - Executive vs operational role-based views
- **Out of Scope:**
  - Ad-hoc BI warehouse / self-serve cube product beyond packaged dashboards/reports
  - Replacing statutory external reporting systems unless specified later
- **Key Actors:** Commissioner / senior authority, section officers, Auditor (read), GIS Cell (sync widgets)
- **Dependencies:** Modules 03-10 for underlying data; Module 01 for role views
- **Notes:** KPIs must reconcile to registers for acceptance sampling.

---

### 14. Data Migration

- **Type:** Shared
- **Summary:** Migrate legacy layout/site (and related available process flags/documents metadata) into LMS with templates, validation, trial/final loads, and reconciliation.
- **Source:** Explicit in document (SOW Sec. 13)
- **In Scope:**
  - Data templates and validation rules
  - Import tools for layouts, sites, and key attributes
  - Historical classification / auction / allotment / CA / Land Loser flags to the extent available and BDA-validated
  - Document metadata linkage and bulk linking of BDA-supplied digital files
  - Trial migration, reconciliation (counts + sample checks), exception register and closure tracking
  - Final cutover load support
- **Out of Scope:**
  - Physical scanning/digitization of paper archives (BDA)
  - Guaranteeing complete historical process reconstruction where source data does not exist
- **Key Actors:** Vendor migration team, BDA data owners / SMEs, Super Administrator
- **Dependencies:** Modules 02-08 (target structures); Module 01 for user mapping if required
- **Notes:** Delivery workstream with explicit acceptance criteria (MIG-AC1-AC3); estimate as its own unit, not as free effort inside business modules.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|---|---|
| Document Management | **Embedded** in Modules 03-08 (and published downloads via Module 10) per SOW - not a separate module |
| Workflow / Approval Engine | **Embedded** runtime in business modules; **configuration** in Module 02 - not a standalone workflow product module |
| Audit & Compliance logging | **System-wide NFR** (SOW Sec. 11); access logs in Module 01; domain approval history in business modules; GIS sync logs in Module 09 |
| Advanced search/filter | **Embedded** in Modules 03-04 list/search; public search UX in Module 10 |
| Officer Portal shell | Delivered as the authenticated application experience across Modules 01-09 and 13 (not a separate module) |
| Payment Gateway | Connector under Module 12; business posting under Modules 05-06 |
| DigiLocker / Aadhaar eKYC | Optional via Module 12; not mandatory Phase 1 business modules |
| Native mobile apps | Out of scope / optional Phase 2 (SOW) |
| Full court case management | Out of scope; legal flags/docs only in Module 04 |
| File storage / job scheduler / search engine products | Not separate modules; supporting platform concerns inside owning modules |

---

## Assumptions

1. Project code is **LMS**; output root is `BDA_LayoutMaster/`.
2. SOW’s nine consolidated functional modules remain the business backbone; User & Role, Citizen Portal, Notification, Integration Hub, and Data Migration are added only where schema/implementation separability requires it.
3. Document management and workflow are estimated inside owning business features, not as standalone modules (per BDA direction and SOW).
4. All GIS/GeoServer features are Phase 1 and estimated under Module 09 in full.
5. Auction mode details (including any e-auction mechanics) will be refined in workshops but remain inside Module 05 boundaries.
6. Payment gateway is conditional on RFP commercial inclusion; Module 12 includes connector capability, feature estimates may mark payment features as conditional.
7. Citizen portal exposes only BDA-configured published fields; officer portal holds full operational data.
8. Legacy migration completeness is limited to data BDA can supply in agreed templates.

---

## Risks

1. **Auction scope ambiguity** - e-auction depth vs record-results-only will swing Module 05 (and Module 10) effort significantly.
2. **GIS bidirectional sync complexity** - external GIS/GeoServer readiness, data quality, and latency can expand Module 09 beyond attribute CRUD.
3. **Classification multi-department workflows** - highly variable approval graphs may increase Module 02 configuration and Module 04 runtime complexity.
4. **Legacy data quality** - incomplete site numbering/categories/documents may expand Module 14 exceptions and delay go-live readiness.
5. **Dual-channel disclosure controls** - mistakes in public field filtering (Module 10) are compliance-sensitive and need careful acceptance tests.
6. **Overlap between Allotment and post-auction formalities** - unclear ownership between Modules 05 and 06 could cause double-counting or gaps unless clarified at feature time.
7. **CA vs Allotment similarity** - parallel case patterns may tempt over-merging; SOW keeps them separate - feature reuse should be noted without collapsing modules.

---

## Review Checklist

- [x] Every major SOW section maps to a module or is explicitly embedded/out of scope
- [x] No duplicate Document or Workflow modules
- [x] Business vs Technical vs Shared types assigned
- [x] Dependencies noted for estimation order
- [x] Out-of-scope items documented
- [x] Module count practical (14) for feature breakdown
