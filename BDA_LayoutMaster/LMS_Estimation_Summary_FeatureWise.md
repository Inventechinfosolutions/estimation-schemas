# LMS — Estimation Summary (Feature-Wise)

**Project:** BDA Layout Master & Site Management System (LMS)  
**Source:** `SoW_LMS_Detailed.md`  
**Basis:** Estimation Master in `feature_schema.md` (UI / API / Database / Integration / Testing / Documentation)  
**Status:** Step 4 + Step 5 complete

> High-level rollup: [`LMS_Estimation_Summary.md`](LMS_Estimation_Summary.md)

---

## Module 01 — `01-user-role-management`

**Module total:** **368 hours** · **8 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F01-001 | Officer User Management | 49 | Officer lifecycle and assignments |
| F01-002 | Roles & Permission Sets | 49 | Module/action permissions |
| F01-003 | Department, Zone & Data Scoping | 49 | Data visibility scope |
| F01-004 | Authentication, Password & Session Management | 41 | Local authentication |
| F01-005 | Optional 2FA for Privileged Roles | 45 | Uses Module 11 delivery |
| F01-006 | Citizen & Applicant Registration/Login | 49 | Portal identity foundation |
| F01-007 | Login History & Access Audit | 41 | Application-level audit |
| F01-008 | Segregation of Duties Enforcement | 45 | Maker–checker control |


## Module 02 — `02-master-data-system-configuration`

**Module total:** **354 hours** · **7 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F02-001 | Location & Administrative Masters | 49 | Hierarchy and organisation |
| F02-002 | Layout, Site, Category & Status Masters | 49 | Core reference data |
| F02-003 | Document Type Master | 37 | Embedded-document types |
| F02-004 | Process Status & Eligibility Parameters | 49 | Process eligibility |
| F02-005 | Notice & Notification Templates | 49 | Content configuration |
| F02-006 | Approval Workflow Configuration | 80 | Config only; no standalone engine |
| F02-007 | Master Activate, Deactivate & Export | 41 | Historical integrity |


## Module 03 — `03-layout-management`

**Module total:** **297 hours** · **6 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F03-001 | Layout Register CRUD | 57 | Parent layout lifecycle |
| F03-002 | Layout Structure: Block, Sector & Phase | 45 | Layout addressing hierarchy |
| F03-003 | Layout Documents & Photographs | 49 | Embedded documents |
| F03-004 | Layout Publish Approval Workflow | 66 | Runtime approval |
| F03-005 | Layout Search & Site Summary | 44 | Linked-site aggregates |
| F03-006 | Layout Archive | 36 | Retained historical record |


## Module 04 — `04-site-management-classification`

**Module total:** **398 hours** · **7 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F04-001 | Site Register CRUD | 57 | Authoritative site register |
| F04-002 | Site Attributes, Legal & Reservation | 57 | Legal flags only; no case diary |
| F04-003 | Site Documents & Photographs | 49 | Embedded documents |
| F04-004 | Multi-Category Site Classification | 66 | Effective category control |
| F04-005 | Classification Approval Workflow | 66 | Runtime approval |
| F04-006 | Site Cancellation & Deactivation | 38 | Controlled lifecycle closure |
| F04-007 | Advanced Layout & Site Search | 65 | SOW multi-parameter filters |


## Module 05 — `05-auction-management`

**Module total:** **349 hours** · **6 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F05-001 | Auction Nomination, Eligibility & Approval | 66 | Approved sites only |
| F05-002 | Auction Case Lifecycle | 66 | Mode subject to workshops |
| F05-003 | Auction Notice Publication | 49 | Portal consumes published content |
| F05-004 | Participant Registration & Results | 66 | No bidding-engine assumption |
| F05-005 | Post-Auction Status & Orders | 49 | Handover to Module 06 |
| F05-006 | Auction Documents, EMD & Payment Link | 53 | Module 12 payment stub only |


## Module 06 — `06-allotment-management`

**Module total:** **477 hours** · **7 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F06-001 | Allotment Schemes, Eligibility & Pools | 73 | Approval-gated pool and publication |
| F06-002 | Allotment Application Capture | 73 | Officer and portal-originated intake |
| F06-003 | Scrutiny, Deficiency & Resubmission | 73 | Checklist and applicant response cycle |
| F06-004 | Selection Method Recording | 69 | Priority, draw, or committee evidence |
| F06-005 | Allotment Approval & Order | 66 | Order issuance and acceptance controls |
| F06-006 | Possession & Handover | 49 | Certificate-backed completion |
| F06-007 | Mutation, Cancellation & Surrender | 74 | High-impact controlled changes |


## Module 07 — `07-ca-site-management`

**Module total:** **296 hours** · **5 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F07-001 | CA Site Register | 43 | Approved CA site intake |
| F07-002 | CA Application & Institutional Proposal | 73 | Proposal and scrutiny |
| F07-003 | CA Approval, Order & Agreement | 74 | Terms, approval, execution |
| F07-004 | CA Renewal, Cancellation & Breach | 66 | Ongoing lifecycle controls |
| F07-005 | CA Status Sync to Site Master | 40 | Master reflection/reconciliation |


## Module 08 — `08-land-loser-management`

**Module total:** **177 hours** · **3 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F08-001 | Land Loser Propose & Mark | 45 | Non-effective proposal and evidence |
| F08-002 | Land Loser Verification, Approval & Publish | 66 | Approval-gated site publication |
| F08-003 | Land Loser Correction & Cancellation | 66 | Auditable corrective lifecycle |


## Module 09 — `09-gis-geoserver-synchronization`

**Module total:** **544 hours** · **6 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F09-001 | GIS Layout & Site Spatial Display | 99 | Phase 1 |
| F09-002 | LMS to GIS/GeoServer Outbound Sync | 94 | Phase 1 |
| F09-003 | GIS to LMS Inbound Sync | 94 | Phase 1 |
| F09-004 | Geometry & Attribute Change Synchronization | 102 | Phase 1 |
| F09-005 | Sync Exception & Retry Queue | 102 | Phase 1 |
| F09-006 | Sync Logs & Operational Status | 53 | Phase 1 |


## Module 10 — `10-citizen-public-portal`

**Module total:** **323 hours** · **6 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F10-001 | Citizen Portal Shell & Navigation | 51 | Portal scope |
| F10-002 | Published Layout & Site Search/View | 63 | Portal scope |
| F10-003 | Public Auction Notices View | 42 | Portal scope |
| F10-004 | Citizen Allotment Application | 82 | Portal scope |
| F10-005 | Application Status & Document Download | 42 | Portal scope |
| F10-006 | Circulars, Help & Disclosure Controls | 43 | Portal scope |


## Module 11 — `11-notification-service`

**Module total:** **195 hours** · **6 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F11-001 | In-app Notification Framework | 30 | |
| F11-002 | SMS Dispatch Service | 39 | |
| F11-003 | Email Dispatch Service | 39 | |
| F11-004 | OTP Notification Flow | 26 | |
| F11-005 | Workflow & Process Alert Dispatch | 35 | |
| F11-006 | Notification Delivery Logging | 26 | |


## Module 12 — `12-api-integration-hub`

**Module total:** **270 hours** · **5 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F12-001 | Payment Gateway Connector (Conditional) | 76 | CONDITIONAL — include if online EMD/fees enabled |
| F12-002 | BDA Master Data Publish Interface | 46 |  |
| F12-003 | Integration Authentication, Failure Handling & Reconciliation | 47 |  |
| F12-004 | DigiLocker Connector (Optional) | 43 | OPTIONAL — excluded from base go-live |
| F12-005 | Aadhaar eKYC Connector (Optional) | 58 | OPTIONAL — excluded from base go-live |


## Module 13 — `13-analytics-dashboards-reports`

**Module total:** **343 hours** · **9 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F13-001 | Analytics Shell & Role-Based Views | 33 |  |
| F13-002 | Layout & Site Inventory Dashboard | 39 |  |
| F13-003 | Classification & Approval Pendency Dashboard | 39 |  |
| F13-004 | Auction & Allotment Pipeline Dashboard | 39 |  |
| F13-005 | CA & Land Loser Summary Dashboard | 39 |  |
| F13-006 | GIS Sync Health Dashboard | 39 |  |
| F13-007 | Standard Register Reports | 40 |  |
| F13-008 | Process & Operational Reports | 40 |  |
| F13-009 | PDF & Excel Export Framework | 35 |  |


## Module 14 — `14-data-migration`

**Module total:** **255 hours** · **5 features**

| Feature ID | Feature Name | Total Hours | Notes |
|------------|--------------|-------------|-------|
| Feature ID | Feature Name | Total Hours | Notes |
| F14-001 | Migration Templates & Validation Rules | 32 |  |
| F14-002 | Layout & Site Bulk Import | 54 |  |
| F14-003 | Historical Process Flags Import | 54 |  |
| F14-004 | Document Metadata Bulk Link | 51 |  |
| F14-005 | Trial, Final Reconciliation & Cutover | 64 |  |


---

## Grand totals

| Metric | Value |
|--------|------:|
| Feature count | 86 |
| Grand total (all catalogued) | **4646** |
| Go-live recommended (excl. DigiLocker/eKYC 101h) | **4545** |
| Base (excl. payment 76h + optional 101h) | **4469** |

### Module rollup

| Module | Features | Hours |
|--------|----------|------:|
| 01 User Role Management | 8 | 368 |
| 02 Master Data System Configuration | 7 | 354 |
| 03 Layout Management | 6 | 297 |
| 04 Site Management Classification | 7 | 398 |
| 05 Auction Management | 6 | 349 |
| 06 Allotment Management | 7 | 477 |
| 07 Ca Site Management | 5 | 296 |
| 08 Land Loser Management | 3 | 177 |
| 09 Gis Geoserver Synchronization | 6 | 544 |
| 10 Citizen Public Portal | 6 | 323 |
| 11 Notification Service | 6 | 195 |
| 12 Api Integration Hub | 5 | 270 |
| 13 Analytics Dashboards Reports | 9 | 343 |
| 14 Data Migration | 5 | 255 |
| **Total** | **86** | **4646** |

---

## Exclusions (not in feature hours)

- Training, UAT facilitation, hypercare, warranty/AMC
- Hosting/infra and third-party licenses (SMS, email, payment, GIS platform)
- Physical scanning of legacy paper files
- Native mobile apps
