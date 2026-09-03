# SoW BMTC_MMVM — Detailed Statement of Work

## Introduction
Bangalore Metropolitan Transport Corporation (BMTC) invites application software for integrated Material Management and Vehicle Maintenance
as specified in tender BMTC/2025-26/SE1231, as amended by Addendum-1231 and the published replies to pre-bid queries.
The original RFP remains the commercial and compliance baseline; this SOW does not replace tender conditions.

## Project Overview
BMTC Integrated Material Management and Vehicle Maintenance will replace paper job cards and fragmented stores processes with a single staff application covering mechanical maintenance,
tyres, major assemblies, fuel, preventive maintenance, stores receipt and distribution, purchase, reporting and migration from existing BMTC IT.
Users operate across Depots, Zones, Central Workshop, Central Stores, Depot Stores and Central Office. About 600 staff users are indicated in the RFP.

## Project Objectives
- Make the Digital Job Card the single source of truth for fitment, labour and vehicle history.
- Maintain one BMTC Item ID shared across Central Stores, Depot Stores and workshops, with live stock on issue and receipt.
- Track tyres, major assemblies, fuel/KMPL, UGT and preventive maintenance (EOC/docking and 10-day) with due KM/date alerts.
- Support gate entry, inspection, RV, indent/transfer, min/reorder, average-cost valuation, supplier and CPO/LPO/LOI with amendments.
- Provide role-scoped reports and dashboards, AVLS KM where available, SMS/email alerts, and barcode/QR software for stores demonstration and operations.
- Migrate existing electronic data and digitise listed paper records into the same structures, with BMTC validation before Go-Live.

## In Scope / Out of Scope
### In Scope
- Application software for the modules listed in Section 6, including Person–Post–Role access, maker-checker where required, and audit logging.
- Staff web portal and in-application mobile/scan capture where the RFP requires job-card or barcode/QR use.
- Embedded document attachments on transactions (no standalone DMS product).
- Data migration tooling, test/production loads, BMTC validation workflows, and structured digitisation of listed paper records.
- Logical integrations for AVLS (vehicle/KM/fuel), HPCL fuel software (pre-bid), SMS, email, and agreed BMTC IT/MIS APIs.
- Bidder-provided hosting on a MeitY-empaneled cloud in India (pre-bid: hosting infrastructure by the successful bidder), including backup, DR and SLA reporting.
- Application maintenance, updates and on-site/helpdesk support for **12 months from Go-Live** (Addendum-1231; original RFP text of 60 months is superseded).
- Standalone complaint registering and monitoring (pre-bid: not an existing BMTC helpdesk).

### Out of Scope
- Detailed technical architecture, class diagrams and UI wireframes (covered in design stage).
- Purchase of barcode/QR scanners, printers or other hardware (RFP: hardware cost is not paid by BMTC).
- SMS usage charges (borne by BMTC). Citizen/public portal is not in this RFP.

## Solution Expectations (Business-level Only)
- Configuration-driven masters, workflows and approval Posts scoped by unit.
- Real-time stock movement on issue against job card and on receipt/acknowledgement.
- Tamper-evident history of who acted, from which Post, when, with MAC/IP as required by the RFP.
- Excel/PDF exports and live dashboards for CME, COSP, Depot Managers, Accounts and Central Office.

## Consolidated Functional Modules

### 01. Person, Post, Role & Access Governance
**Purpose:** Staff identity as Person mapped to unit Posts (Depot, Workshop, Stores, Central Office) with Roles and 2FA.

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F01-001 | Foundational person directory. | Access Administrator maintains each BMTC official as a unique Person |
| F01-002 | Unit-scoped post catalogue. | Administrator maintains Posts placed on Depot, Zone, Central Workshop, Central Stores, Depot Stores or Central Office, with a supervising Post for approvals |
| F01-003 | Effective-dated occupancy. | Administrator maps a Person to a Post with effective dates; Checker approves before login under that Post |
| F01-004 | Post-level permission matrix. | Administrator assigns Roles (view/create/approve by module) to Posts; permissions are never granted directly to Persons |
| F01-005 | Login, OTP and 2FA. | Person signs in with credentials, completes 2FA using official mobile/email OTP, then selects a current Post |
| F01-006 | Access forensic log. | Auditor searches who did what, when, from which Post, MAC/IP |


### 02. Organisation and Location Masters
**Purpose:** Depots, zones, Central Workshop, Central Stores, Depot Stores and sections used to scope Posts and stock.

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F02-001 | Depot/zone/workshop catalogue. | Administrator maintains BMTC Depots, Zones and Central Workshop as location units used for Post placement, job cards and stock |
| F02-002 | Stores and section catalogues. | Administrator maintains Central Stores, Depot Stores, Scrap Store and mechanical sections (Engine, Transmission, Electrical, Tyre, Body) |


### 03. Item Master and Catalogue
**Purpose:** Single BMTC Item ID shared across Central Stores, Depot Stores and CWS with OEM, ABC, warranty and substitutes (FR-S-05 to 09).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F03-001 | FR-S-05, FR-S-06. | Stores Administrator creates a unique BMTC Item ID and links OEM part numbers |
| F03-002 | FR-S-07 to FR-S-09. | Administrator classifies items under Main/Sub schedule and ABC, captures warranty/batch/expiry where applicable, and links substitutes |


### 04. Vehicle Master, KM and Fleet History
**Purpose:** Vehicle master, depot allocation, daily/AVLS KM, assembly history and lifecycle events (FR-M-19 to 23).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F04-001 | FR-M-19, FR-M-23 allocation. | Fleet Administrator maintains vehicle number, type, model, chassis, engine, induction date and depot allocation |
| F04-002 | FR-M-20 and RFP AVLS KM. | Statistical clerk enters starting progressive KM; later KM is added from AVLS |
| F04-003 | Transfers, scrap alerts, assembly history view. | Fleet Administrator records induction, inter-depot transfer and scrap with auction alert; the vehicle history shows spares, services, transfers, warranty parts and accidents |


### 05. Digital Job Card and Fitment
**Purpose:** Digital job card as single source of truth, supervisor sign-off, stores issue and fitment (FR-M-01 to 13).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F05-001 | Job card create/edit/submit. | Mechanical Clerk or Tech |
| F05-002 | Issue + fitment. | Store Clerk records issue to mechanic (Item ID, vehicle, qty, mechanic); stock reduces |
| F05-003 | Supervisor sign-off and labour. | Supervisor closes the job card only after work is complete, with digital sign-off |


### 06. Component Removal, Lifecycle, Warranty and Scrap
**Purpose:** Removal, transfer between vehicles, reusable/scrap routing and warranty claims (FR-M-14 to 18, FR-X-03, FR-X-04).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F06-001 | Removal and transfer. | Mechanical Clerk records who removed an item, when, reason, condition, source vehicle and destination vehicle if refitted |
| F06-002 | Stock routing. | On approved removal, Reusable items return to Depot Store serviceable stock; Scrap goes to Scrap Store with disposal/auction tracking |
| F06-003 | Warranty tracking. | When condition is Under Warranty, a claim is opened against the supplier and tracked to closure |


### 07. Tyre and Major Assembly Management
**Purpose:** Tyre history card, positions, inflation, life analysis, scrap tyres; new and RC major assemblies (FR-M-24 to 29).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F07-001 | Tyre card. | Tyre Clerk records fitment/removal per tyre with wheel position and cumulative KM across vehicles and retreads; records inflation readings |
| F07-002 | Life analysis and scrap. | System analyses KM run and premature wear; scrap tyres get condition and disposal records |
| F07-003 | Assembly tracking. | Workshop tracks new major assemblies and reconditioned (RC) assemblies with related reports (engine, gearbox, axles, alternator, starter) |


### 08. Fuel Management
**Purpose:** UGT master, fuel GRN, daily issue, fuel register and KMPL at vehicle, driver, depot and model (FR-M-30 to 35).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F08-001 | UGT catalogue. | Depot fuel administrator maintains UGT details and capacity per depot |
| F08-002 | Fuel receipt. | Fuel clerk records supplier GRN; the fuel register shows cumulative receipts, issues and closing balance |
| F08-003 | Issue and KMPL. | Fuel clerk records daily HSD issue per bus with driver; system calculates KMPL and flags underperforming vehicles vs norms; averages by vehicle, driver, depot, model |


### 09. Preventive Maintenance Scheduling
**Purpose:** EOC/Docking and 10-day maintenance due date/KM, statuses and alerts (FR-M-36 to 38, FR-R-02).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F09-001 | PM engine. | System tracks EOC/Docking and 10-Day schedules with auto due date and due KM from last completed maintenance; statuses Upcoming / Due Today / Overdue / Completed; alerts to Tech |


### 10. Stores Receipt and Inspection
**Purpose:** Gate entry, inspection report, receipt voucher linked to PO, stock update (FR-S-01 to 04).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F10-001 | Gate entry. | Central Stores clerk records every incoming consignment: vendor, item, quantity, date |
| F10-002 | IR and RV. | Inspector accepts or rejects goods (IR) |


### 11. Distribution, Stock Visibility and Replenishment
**Purpose:** Indent-based transfers, acknowledgement, live stock, min/reorder alerts, monthly average cost, physical verification (FR-S-10 to 19, FR-X-05).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F11-001 | Distribution flow. | Receiving location raises indent; Central Stores dispatches Stock Transfer; receiver acknowledges to complete the cycle and move stock |
| F11-002 | Live stock views. | Depots, Workshops, Central Stores and Central Office see stock by login scope; Central Stores can see all depot and CWS stock |
| F11-003 | Control and PV. | Alerts at min and reorder; monthly average cost valuation; physical count vs system with discrepancy reconciliation |


### 12. Purchase and Supplier Management
**Purpose:** Supplier master, auto PR, CPO/LPO, LOI, PO amendment workflow, pending PO dashboard (FR-S-20 to 26).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F12-001 | Supplier catalogue. | Purchase Administrator maintains approved suppliers with contacts, item categories and performance history |
| F12-002 | PR. | System raises auto PR as advance alert from reorder/forecast; officer may raise manual PR for Store and Mechanical officers |
| F12-003 | PO lifecycle. | Purchase officer issues Central PO, Local PO or LOI; amendments require reason and approval; pending PO dashboard shows outstanding and overdue |


### 13. Barcode, QR, Notifications and External Integrations
**Purpose:** Barcode/QR at stores, SMS/email, AVLS, and documented APIs for BMTC IT (FR-X-08, RFP technical).

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F13-001 | QR/barcode software only. | Generate and scan QR/barcode for receipt, issue and stock verification at Central Stores and Depot Stores |
| F13-002 | Notifications. | SMS gateway and email for PM alerts, reorder, job-card pending, PO overdue |
| F13-003 | External hooks. | Fetch vehicle master/fuel/KM from AVLS (pre-bid: KM and fuel currently entered in AVLS) |


### 14. Reporting and Dashboards
**Purpose:** Mechanical reports FR-R-01 to 06, RFP report list, role-based dashboards, accounts audit views, Excel/PDF export with unit scope.

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F14-001 | Maintenance MIS. | Pending job cards with ageing bands and pending reason; job card register; vehicle maintenance history; repeated complaint and most items consuming vehicle |
| F14-002 | CME/DC/DME analysis. | Most defective bus; low performing driver and vehicle KMPL with flags; DVP analysis (schedules, vehicles, off-road, spare %) |
| F14-003 | Dashboards. | Role-based dashboards: fleet status, stock alerts, open job cards, procurement, fuel efficiency (FR-X-07) |


### 15. Data Migration and Record Digitisation
**Purpose:** Migrate existing BMTC IT data with cleansing, test, validate; digitise listed paper records into the new structures.

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F15-001 | Migration software effort. | Service Provider plans cleansing, test loads, validation with BMTC, and cutover from existing IT systems before Go-Live |
| F15-002 | Digitisation of paper into masters/transactions. | Existing BMTC paper categories listed in the RFP are captured into the same structures as live transactions (job cards, history cards, registers), mirroring paper information |


### 16. Hosting, Helpdesk and Post Go-Live Maintenance
**Purpose:** Bidder-provided MeitY cloud hosting, standalone helpdesk, SLA/CERT-IN tooling; 12-month AMC after Go-Live per Addendum-1231.

**Functional requirements:**
- Provide the required workflows and unit-scoped processing aligned to BMTC Mechanical, Stores and Purchase practice.
- Enforce security, access controls, and audit-grade traceability.
- Provide reliable outputs for review, reporting and oversight.

**Acceptance criteria:**
- Transactions and approvals are processed through governed workflow states with complete history.
- Role-scoped access prevents unauthorised viewing/acting.
- Reporting and MIS outputs can be generated from controlled operational records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F16-001 | Bidder-provided MeitY hosting setup. | Successful bidder provides MeitY-empaneled cloud hosting in India with required compute, storage, bandwidth, DR/backup and SLA instrumentation |
| F16-002 | Standalone helpdesk. | 24x7 helpdesk as a standalone module (pre-bid: not integrated with an existing BMTC helpdesk) |
| F16-003 | Audit cycle tooling. | Arrange CERT-IN empanelled security audit and safe-to-host before Go-Live, and VAPT after major changes, with reports shared with BMTC |


## End-to-End Workflows
- Person authenticates (including 2FA), selects a current Post, and works only within that Post's unit scope.
- Mechanical: job card → stores issue → fitment → supervisor digital sign-off; removals route reusable/scrap/warranty.
- Stores: gate entry → inspection → RV linked to PO → stock; indent → dispatch → acknowledgement.
- Purchase: reorder/forecast → PR → CPO/LPO/LOI → amendment and pending-PO monitoring.
- Fuel and KM (manual, AVLS or HPCL feed) feed KMPL and PM due KM; PM alerts notify DM, DME, DC and Tech. Supervisor.
- Dashboards and accounts views consume live operational records; barcode/QR supports receipt, issue and verification.
- Helpdesk tickets and hosting SLA packs support monthly payment after Go-Live.

## Access Control / RBAC
Staff access is Person → Post → Role → Permissions. A Person is mapped to a Post placed on Depot, Zone, Central Workshop, Central Stores, Depot Stores or Central Office.
Roles and permissions attach to the Post, not directly to the Person. Data scope follows the Post's unit unless a Central Office / Central Stores Role allows a wider view.
Approval routing uses the supervising Post on the Post master. Institution or public users are not in this RFP. Accounts login (FR-X-09) is a Role on an Accounts Post.
Maker–checker applies to masters and to transactions that require a checker. Every action is logged against the acting Person and Post, including MAC/IP as required.

## Channels
- Staff web portal for Depot, Workshop, Stores, Purchase, Mechanical Section, CME/DC/DME, COSP, Depot Managers and Accounts.
- In-application capture for job-card and barcode/QR scanning where the RFP requires it (not a citizen portal).

## Integrations
- AVLS for vehicle master, fuel and KM (pre-bid: KM and fuel are currently entered in AVLS).
- HPCL fuel software now, and future PSU/vendor fuel systems as BMTC decides (pre-bid).
- SMS gateway and email for configured alerts (SMS charges billed to BMTC).
- Agreed APIs/MIS sharing with BMTC IT and future BMTC projects as required by the RFP.
- Barcode/QR generation and scan validation against stores events (hardware out of this SOW).
- MeitY-empaneled cloud platform provided by the bidder (India residency).

## Audit, Compliance & Security
- Audit trail of actions, approvals and stock movements; 2FA using official mobile and email.
- Permission checks on every screen and operation; recertification of Post mappings.
- Application and transaction logs retained as required (RFP: transaction log minimum one year; application data five years).

## Non-Functional Requirements
- Performance and availability suitable for concurrent depot, workshop and stores operations (~600 users).
- Secure handling of fleet, stores and commercial data.
- Usable job-card and stock screens under depot workshop conditions.

## Data Migration
Migration from existing BMTC IT is in scope: cleansing, mapping, test load, production load and validation sign-off with BMTC before Go-Live.
Pre-bid: migrated volume is about 9 GB in MySQL. Listed paper records are digitised into the same structures as live transactions.

## Phased Delivery
- Phase 1: Person–Post access, organisation/item/vehicle masters, job card and stores receipt/issue.
- Phase 2: Tyre, assemblies, fuel, PM, distribution, purchase and barcode/QR.
- Phase 3: AVLS/HPCL/SMS/email, reporting (English and Kannada), migration, hosting go-live, helpdesk.
- Phase 4: Twelve months AMC from Go-Live (Addendum-1231), including updates and on-site/helpdesk support.

## Deliverables
- Production-grade application modules, features and governed workflows as listed.
- Test-ready build with audit logging, unit-scoped access and integration hooks named above.
- Documentation for configuration, operation and maintenance handover (application software).

## Acceptance Criteria (Program Level)
- Digital job card, stock and purchase cycles complete with history and unit-scoped access.
- Reports and dashboards (English and Kannada) reflect controlled operational records with correct Depot/Zone/Workshop/Stores/CO filters.
- Migration and digitisation batches are signed by BMTC validators; AVLS/HPCL/SMS/email hooks run against agreed mappings.
- Hosting is live on MeitY-empaneled cloud in India with safe-to-host; helpdesk is operational; AMC starts at Go-Live for 12 months.

## Expected Benefits
- Elimination of paper job cards as the system of record.
- Visible stock and faster replenishment; warranty and scrap traceability.
- Fuel/KMPL and PM due visibility for Mechanical and Depot Managers.

## Assumptions & Dependencies
- BMTC confirms the Post catalogue, supervising Posts and which Posts hold CME, COSP, Accounts and Depot Manager Roles.
- AVLS, HPCL and legacy extract formats are provided for mapping; BMTC officers are available for migration validation (pre-bid: about 9 GB MySQL).
- Barcode/QR hardware, classroom training delivery and SMS charges remain outside this SOW. Hosting and 12-month AMC are in scope.
- Optional second AMC year at the same price (original contract-period clause) is not assumed unless BMTC confirms it in writing.

## Vendor Response Expectations
- Provide a production-quality build aligned to the functional scope and acceptance criteria.
- Maintain traceability, validation and security for enterprise governance.

## Appendices
- Appendix A — Module & Feature Index (summary).

| Module | Module Name | Type | Feature IDs (count) |
|---|---|---|---|
| 01 | Person, Post, Role & Access Governance | Shared | F01-001, F01-002, F01-003, F01-004, F01-005, F01-006 (6) |
| 02 | Organisation and Location Masters | Business | F02-001, F02-002 (2) |
| 03 | Item Master and Catalogue | Business | F03-001, F03-002 (2) |
| 04 | Vehicle Master, KM and Fleet History | Business | F04-001, F04-002, F04-003 (3) |
| 05 | Digital Job Card and Fitment | Business | F05-001, F05-002, F05-003 (3) |
| 06 | Component Removal, Lifecycle, Warranty and Scrap | Business | F06-001, F06-002, F06-003 (3) |
| 07 | Tyre and Major Assembly Management | Business | F07-001, F07-002, F07-003 (3) |
| 08 | Fuel Management | Business | F08-001, F08-002, F08-003 (3) |
| 09 | Preventive Maintenance Scheduling | Business | F09-001 (1) |
| 10 | Stores Receipt and Inspection | Business | F10-001, F10-002 (2) |
| 11 | Distribution, Stock Visibility and Replenishment | Business | F11-001, F11-002, F11-003 (3) |
| 12 | Purchase and Supplier Management | Business | F12-001, F12-002, F12-003 (3) |
| 13 | Barcode, QR, Notifications and External Integrations | Technical | F13-001, F13-002, F13-003 (3) |
| 14 | Reporting and Dashboards | Business | F14-001, F14-002, F14-003 (3) |
| 15 | Data Migration and Record Digitisation | Business | F15-001, F15-002 (2) |
| 16 | Hosting, Helpdesk and Post Go-Live Maintenance | Technical | F16-001, F16-002, F16-003 (3) |
