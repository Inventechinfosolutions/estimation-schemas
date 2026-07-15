# Statement of Work (SOW)

# Bangalore Development Authority (BDA)  
# Layout Master & Site Management System (LMS)

**Document Type:** Request for Proposal (RFP) – Statement of Work  
**Version:** 1.0  
**Status:** Draft for RFP  
**Prepared by:** Bangalore Development Authority  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Role-Based Access Control](#8-role-based-access-control)
9. [Channels – BDA Officer Portal & Citizen Portal](#9-channels--bda-officer-portal--citizen-portal)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria (Program Level)](#16-acceptance-criteria-program-level)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)

---

## 1. Introduction

This Statement of Work (SOW) defines the functional and delivery requirements for the design, development, implementation, data migration, training, and support of the **Layout Master & Site Management System (LMS)** for the **Bangalore Development Authority (BDA)**.

The SOW is intended for use in an **RFP**. Responding vendors shall propose a complete solution covering application software, implementation services, legacy data migration, training, documentation, and warranty / AMC, as specified in this document and the RFP package.

LMS shall be the **authoritative master system** for BDA layouts and sites, and shall also cover **site classification, auction, allotment, Civic Amenity (CA) site management, Land Loser site management, GIS/GeoServer synchronization, and citizen-facing services**.

**Document management** and **approval workflows** are not separate product modules. They shall be built into every relevant business process (layout, site, classification, auction, allotment, CA site, Land Loser, and GIS change control) so that documents and approvals travel with the transaction.

---

## 2. Project Overview

BDA intends to implement a centralized digital platform to manage the complete lifecycle of BDA layouts and individual sites, including:

- Creation and maintenance of layout master records  
- Creation and maintenance of site master records under each layout  
- Multi-category site classification with department-wise approvals  
- Auction of eligible sites  
- Allotment of eligible sites  
- Civic Amenity (CA) site lifecycle management  
- Land Loser site identification and management  
- Bidirectional synchronization with BDA GIS / GeoServer  
- Secure access for BDA officials and a public / citizen portal  
- Dashboards, MIS, and search across layouts and sites  
- Migration of existing layout and site data from legacy / manual sources  

The system shall replace fragmented manual registers, spreadsheets, and duplicated departmental records with a **single source of truth** for layout and site information used across BDA departments and downstream processes.

### 2.1 Entities to Be Supported

| Entity | Description |
|---|---|
| Layout | Planned / developed BDA layout with location, survey, area, structure (Block / Sector / Phase / Stage / Section), plans, and status |
| Site | Individual plot / site within a layout, with dimensions, category, reservation, legal status, ownership, and documents |
| Site Classification | One or more categories applied to a site (Residential, Commercial, CA, Auction, Land Loser, Park, Utility, Reserved, etc.) |
| Auction Case | Business case to auction one or more approved sites, through notification, participation, result, and post-auction update |
| Allotment Case | Business case to allot eligible sites through application, scrutiny, approval, allotment order, and possession |
| CA Site Case | Civic Amenity site register, allotment / lease / assignment to eligible institutions or uses, and ongoing status |
| Land Loser Case | Sites marked and approved as Land Loser with supporting references and documents |
| Spatial Record | Layout boundaries and site polygons / attributes synchronized with GIS / GeoServer |

### 2.2 Guiding Principles

1. **Single master repository** — no parallel unofficial site registers for in-scope processes.  
2. **Approval before consumption** — special classifications and process eligibility take effect only after configured approval.  
3. **Process integrity** — Auction, Allotment, and CA processes consume only validated, eligible sites.  
4. **Spatial consistency** — attribute and geometry data remain consistent between LMS and GIS / GeoServer.  
5. **Transparency** — citizen-facing information where BDA permits publication; full audit for official actions.  
6. **Documents with the record** — every key action can attach, store, and retrieve related documents within the same process.  

---

## 3. Project Objectives

1. Digitize all BDA layout and site records into a centralized master repository.  
2. Eliminate manual registers, duplicate site entries, and inconsistent departmental data.  
3. Provide standardized, department-configurable classification and approval workflows.  
4. Enable end-to-end **Auction**, **Allotment**, and **CA Site** processes on top of the layout/site master.  
5. Support **Land Loser** site identification, verification, approval, and publishing.  
6. Achieve full bidirectional integration with **BDA GIS / GeoServer** from Phase 1.  
7. Provide an authenticated **BDA officer portal** and a **citizen / public portal**.  
8. Migrate legacy layout and site data with validation and reconciliation.  
9. Improve transparency, data accuracy, operational efficiency, and inter-department coordination.  
10. Serve as the authoritative property master for other present and future BDA applications.  

---

## 4. In Scope / Out of Scope

### 4.1 In Scope

- Responsive web application for BDA officers, section users, and administrators.  
- Citizen / public portal for permitted search, view, notifications, and process participation (e.g., auction / allotment application where enabled by BDA).  
- Layout master lifecycle management.  
- Site master lifecycle management under layouts.  
- Multi-category site classification with configurable multi-level approval workflows (embedded in classification and process modules).  
- Auction management (from site eligibility through auction conclusion and site status update).  
- Allotment management (from eligibility through application, approval, allotment order, and possession recording).  
- CA Site management (register, eligibility, allotment / assignment, status, and related documents).  
- Land Loser site management.  
- Full GIS / GeoServer integration (read, display, write-back, sync, failure handling, and sync logs) — **Phase 1**.  
- Embedded document management for layouts, sites, classifications, auction, allotment, CA, Land Loser, and GIS reference documents.  
- Master data configuration, users, roles, and department-wise workflow configuration.  
- Dashboards, operational reports, management MIS, advanced search, and export.  
- Notifications (in-app; SMS / email where enabled).  
- Legacy data migration (templates, cleansing support, import, validation, reconciliation).  
- Training, UAT support, go-live support, warranty, and documentation.  

### 4.2 Out of Scope (unless explicitly added via change request)

- Full court case management / litigation case diary beyond **legal status flags, key dates, linked court orders / documents, and remarks**.  
- Full ERP / general ledger / treasury accounting replacement (integration hooks only, if required later).  
- Hardware procurement (servers, scanners, GPS devices, plotters, etc.), unless stated in the RFP commercial section.  
- Physical digitization / scanning of paper archives (BDA responsibility; system shall accept uploaded digital files).  
- Native iOS / Android apps (optional; vendor may propose separately — responsive web is mandatory).  
- Replacement of unrelated BDA systems (HR, payroll, engineering project management, etc.).  

---

## 5. Solution Expectations

Vendors shall propose a solution that meets the following **business and delivery expectations**. Detailed technology stack choices may be proposed by the vendor and finalized with BDA during design, provided functional and non-functional requirements are met.

| Area | Expectation |
|---|---|
| Access channels | Secure BDA officer web portal + public / citizen web portal |
| Usability | Clear, role-based screens; mobile-responsive for field reference and citizen use |
| Hierarchy | Administrative location hierarchy (State → District → Taluk → Village / Hobli → BDA Zone) and Layout → Block / Sector / Phase / Stage / Section → Site |
| Single source of truth | Layout and site codes/status governed in LMS; downstream processes use LMS as master |
| Workflow | Configurable multi-level approvals by process and site category / department |
| Documents | Upload, view, version/replace, and link documents within each business process |
| Spatial | Bidirectional consistency with BDA GIS / GeoServer for layouts and sites |
| Auditability | Complete history of create / edit / classify / approve / publish / allot / auction actions |
| Language | English mandatory at go-live; bilingual-ready (English + Kannada) preferred |
| Hosting | As specified in RFP (government-approved cloud / on-premises / hybrid — BDA decision) |

---

## 6. Consolidated Functional Modules

The solution shall be delivered as **nine consolidated modules**.  
Document attachment / retrieval and approval workflow steps are **embedded** inside Modules 2–8 as applicable — they are not bid as standalone modules.

---

### Module 1: Master Data & System Configuration

**Purpose:** Provide configurable foundation data, organizational structure, users/roles, and workflow configuration used across all modules.

#### 1.1 Functional Requirements

**A. Location & Administrative Masters**

- Country, State, District, Taluk, Village, Hobli, BDA Zone.  
- Section / Division / Department masters used for routing and ownership.  
- Ability to activate / deactivate masters without deleting historical references.  

**B. Layout & Site Masters**

- Layout Status, Site / Property Status.  
- Site Categories (Residential, Commercial, CA, Auction, Land Loser, Corner, Intermediate, Park, Civic Infrastructure, Utility, Public Purpose, Government Reserved, Future Development, and other BDA-defined categories).  
- Reservation Categories, Road Facing, Corner / Intermediate indicators.  
- Block, Sector, Phase, Stage, Section structure codes (as applicable).  
- Document type master (layout plans, survey sketches, GOs, acquisition documents, court orders, khata, site sketches, classification approvals, GIS references, certificates, auction / allotment / CA papers, etc.).  

**C. Process Masters**

- Auction status, allotment status, CA site status, Land Loser status.  
- Eligibility rules parameters (configurable flags / conditions as defined by BDA).  
- Notice / circular templates for auction and allotment (where applicable).  
- Notification templates (in-app / SMS / email).  

**D. User, Role & Workflow Configuration**

- Create and manage users, roles, and permission sets.  
- Map users to departments, zones, and data scopes.  
- Configure multi-level approval workflows by process type (e.g., layout publish, site creation/cancellation, classification for Auction / CA / Land Loser / Reserved / Commercial, auction notification approval, allotment approval, CA allotment approval).  
- Configure workflow levels, approvers / roles, and conditions as defined by BDA (Engineering, Land Acquisition, Auction, Revenue, Legal, CA Site, Town Planning, Commissioner Office, and others).  
- Maker–checker where required by process.  

#### 1.2 Key Capabilities

- Search, filter, and export of masters.  
- Prevention of orphaned references when deactivating masters.  
- Audit of configuration changes to workflows and critical masters.  

#### 1.3 Acceptance Criteria

| ID | Criterion |
|---|---|
| M1-AC1 | Authorized admin can create and configure all listed masters without code change. |
| M1-AC2 | Department-wise approval workflows can be configured per process / category. |
| M1-AC3 | Role permissions restrict module and record visibility as configured. |
| M1-AC4 | Deactivated masters cannot be selected for new transactions but remain visible on historical records. |
| M1-AC5 | Document types and notification templates are configurable by administrators. |

---

### Module 2: Layout Management

**Purpose:** Provide complete lifecycle management of BDA layouts as the parent entity for all sites.

*(Documents and layout-related approvals are embedded in this module.)*

#### 2.1 Functional Requirements

**A. Layout Register**

Authorized officials shall be able to:

- Create new layouts with unique layout code / identity as defined by BDA.  
- Update layout information with full change history.  
- View complete layout details and linked sites summary.  
- Capture location details: State, District, Taluk, Village, Hobli, BDA Zone.  
- Capture / maintain latitude and longitude (and link to GIS geometry where available).  
- Maintain total layout area and survey / boundary details.  
- Maintain Block, Sector, Phase, Stage, and Section information.  
- Maintain layout status (Draft, Active, Archived, and other BDA-defined statuses).  
- Archive layouts where applicable (without losing history or linked site references).  

**B. Layout Documents & Photographs (embedded)**

- Upload approved layout plans and supporting documents.  
- Upload layout photographs.  
- Link Government Orders, acquisition papers, survey sketches, and GIS reference documents to the layout.  
- Retrieve documents from the layout record; control access by role.  

**C. Layout Approval / Publish (embedded workflow)**

- Where required by BDA, layout creation or major amendments shall follow a configurable approval workflow before the layout becomes active for site creation or public display.  
- Each approval step shall capture remarks, user, date, and time.  

**D. Layout–Site Relationship**

- Every site shall belong to exactly one registered layout.  
- Layout view shall show site counts by status and category.  

#### 2.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M2-AC1 | Authorized users can create, update, view, and archive layouts with required location and structure fields. |
| M2-AC2 | Layout plans, photographs, and supporting documents can be uploaded and retrieved from the layout record. |
| M2-AC3 | Where configured, layout activation requires successful workflow approval. |
| M2-AC4 | Sites cannot be created without a valid parent layout. |
| M2-AC5 | Layout search works by name, code, zone, district, taluk, village, and status. |

---

### Module 3: Site Management & Classification

**Purpose:** Maintain the complete site register and master classification system, with embedded classification approval workflows and site documents.

*(Consolidates: Site Management, Site Classification, Classification Approval Workflow, Department-wise Workflow.)*

#### 3.1 Functional Requirements

**A. Site Register**

The system shall support:

- Creation of sites under a layout.  
- Modification of site information with audit trail.  
- Site cancellation / deactivation where applicable (with reason and approval if configured).  
- Viewing complete site details.  
- Site numbering as per BDA conventions.  
- Site dimensions and area calculations / capture.  
- Corner and intermediate site identification.  
- Road facing details.  
- Khata information.  
- Survey numbers.  
- Reservation information.  
- Legal status and litigation information (flags, key dates, remarks, linked documents).  
- Site ownership / possession status as maintained by BDA.  
- Site photographs and supporting documents (embedded document handling).  

**B. Site Classification**

- Each site may be classified into one or more categories based on departmental requirements.  
- Categories shall include at minimum: Residential, Commercial, Civic Amenity (CA), Auction, Land Loser, Corner, Intermediate, Park, Civic Infrastructure, Utility, Public Purpose, Government Reserved, Future Development, and other categories defined by BDA.  
- Classification shall determine which business process (Auction / Allotment / CA / Land Loser / other) may consume the site.  

**C. Classification Approval Workflow (embedded)**

- Classification under special / process-driving categories (e.g., Auction, Land Loser, CA, Commercial, Public Utility, Reserved, or other department-specific categories) shall **not** become effective immediately.  
- The system shall:  
  - Route the request to the concerned department(s).  
  - Allow verification of site details.  
  - Allow approve / reject / return with remarks at each stage.  
  - Maintain complete approval history with date, time, and authority.  
  - Attach classification approval documents.  
- Only after successful approval shall the site become available for the respective business process.  

**D. Search & Retrieval (site/layout)**

Search parameters shall include at minimum:

Layout Name, Layout Code, Site Number, Survey Number, Zone, District, Taluk, Village, Block, Sector, Phase, Stage, Site Category, Auction Status, CA Site Status, Land Loser Status, Allotment Status, Approval Status, GIS Availability, Property / Site Status.

#### 3.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M3-AC1 | Every site is uniquely identifiable and linked to a valid layout. |
| M3-AC2 | Multi-category classification is supported with effective dates / status. |
| M3-AC3 | Special classifications require configured multi-level approval before process eligibility. |
| M3-AC4 | Rejected / returned classifications do not make the site available for the target process. |
| M3-AC5 | Site documents and photographs are available from the site record. |
| M3-AC6 | Advanced search returns correct results for the listed parameters. |

---

### Module 4: Auction Management

**Purpose:** Manage the end-to-end auction of BDA sites that have been approved as auction-eligible in the layout/site master.

*(Documents and auction approval workflows are embedded in this module.)*

#### 4.1 Functional Requirements

**A. Auction Eligibility & Nomination**

- Identify / propose sites for auction only if the site holds an approved Auction (or equivalent) classification / eligibility flag.  
- Route auction nomination through the required departmental approval workflow.  
- Mark site as **Approved for Auction** after successful approval.  
- Sites not approved shall not be available for auction scheduling.  

**B. Auction Case Lifecycle**

- Create auction cases / batches with auction reference, schedule, location / mode (as defined by BDA), and linked sites.  
- Capture auction terms, EMD / participation conditions (as configured), and supporting notifications.  
- Publish auction notices for citizen / applicant visibility on the public portal as permitted by BDA.  
- Record bidder / participant registration details as required by BDA process.  
- Record auction proceedings / results (winning bid, bidder, amount, status).  
- Handle unsuccessful / cancelled / postponed auctions with reason and audit.  
- Update site status after auction confirmation (e.g., Auctioned / Pending Allotment Formalities / Released Back).  

**C. Post-Auction Actions**

- Generate / store auction-related orders and acknowledgements (templates configurable).  
- Link payments / EMD / balance dues recording as per BDA process (integration with payment gateway where mandated in RFP).  
- Handover outcome to allotment / possession steps where required.  
- Ensure any change to auction-approved site attributes remains controlled and visible to downstream views.  

**D. Auction Documents (embedded)**

- Auction notification, proceedings, bid sheets, winner confirmation, challans, and related GOs / approvals attached to the auction case and/or site.  

#### 4.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M4-AC1 | Only sites approved for auction can be included in an auction case. |
| M4-AC2 | Auction nomination and publication follow configured approvals. |
| M4-AC3 | Auction results update site status and retain full history. |
| M4-AC4 | Citizens can view published auction notices/details as configured by BDA. |
| M4-AC5 | Auction documents are retrievable from the auction case and related site. |

---

### Module 5: Allotment Management

**Purpose:** Manage end-to-end allotment of eligible BDA sites (including residential / other categories as defined by BDA), from application through allotment order and possession recording.

*(Documents and allotment approval workflows are embedded in this module.)*

#### 5.1 Functional Requirements

**A. Allotment Eligibility**

- Sites become available for allotment only when status and classification rules defined by BDA are satisfied.  
- Support allotment pools / schemes / notifications as configured.  

**B. Application & Scrutiny**

- Capture allotment applications (officer-assisted and/or citizen portal submission, as enabled).  
- Capture applicant details, eligibility criteria responses, preferences (layout / site / category), and supporting documents.  
- Provide scrutiny checklist, deficiency memo, and re-submission tracking.  
- Support selection methods defined by BDA (e.g., priority rules, lottery / draw recording, committee recommendation — configurable process, not hardcoded to one method).  

**C. Allotment Approval & Order**

- Multi-level approval workflow for recommended allotments.  
- Generate allotment order / intimation from templates.  
- Record acceptance / refusal by allottee within configured timelines.  
- Update site ownership / allotment status and prevent double allotment of the same site.  

**D. Possession / Handover**

- Record possession / handover dates, condition notes, and possession documents.  
- Link subsequent mutations / cancellations / surrender (as applicable) with approval and audit.  

**E. Allotment Documents (embedded)**

- Application form, KYC / identity proofs (as required), eligibility certificates, scrutiny notes, allotment order, possession certificate, and related correspondence.  

#### 5.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M5-AC1 | A site cannot be allotted unless it meets configured eligibility rules. |
| M5-AC2 | The same active site cannot be allotted to two allottees. |
| M5-AC3 | Allotment approval history and allotment order are stored and retrievable. |
| M5-AC4 | Possession recording updates site status and retains documents. |
| M5-AC5 | Citizen portal supports application / status tracking where enabled by BDA. |

---

### Module 6: CA Site Management

**Purpose:** Maintain Civic Amenity (CA) sites as part of the master repository and manage CA-specific allotment / assignment / lease lifecycle as defined by BDA.

*(Documents and CA approval workflows are embedded in this module.)*

#### 6.1 Functional Requirements

**A. CA Site Register**

- Maintain CA sites approved through classification workflow.  
- Capture CA purpose, permitted use, beneficiary type, and status.  
- Ensure only approved CA sites are available for CA processes.  

**B. CA Allotment / Assignment / Lease**

- Receive / register applications or institutional proposals.  
- Scrutiny, committee / department recommendation, and multi-level approval.  
- Capture terms (period, conditions, fees / deposits if applicable).  
- Issue CA allotment / lease / assignment order from templates.  
- Track renewals, cancellations, breaches / notices (status + documents).  
- Update CA site occupancy / availability status.  

**C. CA Documents (embedded)**

- Institutional documents, project purpose notes, approvals, agreements / orders, and compliance certificates linked to the CA case and site.  

**D. Synchronization with Master**

- CA process statuses continuously reflect on the site master for enterprise visibility and reporting.  

#### 6.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M6-AC1 | Only classification-approved CA sites enter the CA process pool. |
| M6-AC2 | CA allotment / assignment requires configured approvals before order generation. |
| M6-AC3 | CA site status updates are visible on the site master and dashboards. |
| M6-AC4 | CA documents and orders are linked to both case and site records. |

---

### Module 7: Land Loser Management

**Purpose:** Identify, verify, approve, and maintain Land Loser sites and related reference information.

*(Documents and Land Loser approval workflows are embedded in this module.)*

#### 7.1 Functional Requirements

- Mark / propose a site as Land Loser.  
- Capture Land Loser reference information (acquisition reference, beneficiary linkage fields as defined by BDA, remarks).  
- Department verification and multi-level approval workflow.  
- Attach supporting documents (acquisition papers, GOs, identity / entitlement proofs as applicable).  
- On approval, publish Land Loser status on the site master for downstream use.  
- Support cancellation / correction of Land Loser marking through controlled workflow.  

#### 7.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M7-AC1 | Land Loser status is effective only after successful approval. |
| M7-AC2 | Supporting documents and references are mandatory as configured. |
| M7-AC3 | Approved Land Loser sites appear correctly in searches and Land Loser dashboards. |
| M7-AC4 | Full approval history is retained for audit. |

---

### Module 8: GIS & GeoServer Synchronization

**Purpose:** Ensure spatial and non-spatial information for layouts and sites remains consistent between LMS and the BDA GIS platform / GeoServer.

**All capabilities in this module are mandatory in Phase 1.**

*(Sync exceptions, approvals for geometry overrides if configured, and GIS reference documents are embedded.)*

#### 8.1 Functional Requirements

**A. GIS Information in LMS**

- Retrieve and display layout boundaries from the GIS server.  
- Retrieve and display site polygons from the GIS server.  
- Retrieve and display spatial attributes.  
- Show GIS availability status on layout and site records.  

**B. Bidirectional Synchronization**

- When a layout or site is created or modified in the GIS platform, corresponding records shall synchronize to LMS.  
- When a layout or site is created or updated in LMS, GIS / GeoServer shall be updated to maintain consistency.  
- Synchronize geometry and attribute changes for layouts and sites.  

**C. GeoServer Operations**

- Fetch layout and site geometry from GeoServer.  
- Push newly created layouts and sites to GeoServer.  
- Update geometry modifications and attribute changes.  
- Handle synchronization failures through retry and exception queues.  
- Maintain synchronization logs for audit and operations monitoring.  

**D. Operational Controls**

- Dashboard indicators for GIS sync health (success / pending / failed).  
- Authorized re-sync / resolution actions for failed items.  
- Clear business status when GIS is unavailable (no silent data loss).  

#### 8.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M8-AC1 | Layout boundary and site polygon can be viewed from the LMS record when available in GIS. |
| M8-AC2 | Create/update in LMS reflects in GIS / GeoServer within agreed sync window. |
| M8-AC3 | Create/update in GIS reflects in LMS within agreed sync window. |
| M8-AC4 | Failed synchronizations are logged, visible, and retriable. |
| M8-AC5 | GIS sync status is available on dashboards and on individual records. |

---

### Module 9: Analytics, Dashboards & Reports

**Purpose:** Provide operational monitoring and management decision-support across layouts, sites, classifications, auction, allotment, CA, Land Loser, and GIS sync.

#### 9.1 Dashboards

Dashboards shall include at minimum:

- Total Layouts  
- Total Sites  
- Layout-wise Site Count  
- Zone-wise Layout Distribution  
- Category-wise Site Distribution  
- Auction Site Summary & Auction Case Pipeline  
- Allotment Pipeline Summary  
- CA Site Summary  
- Land Loser Site Summary  
- Commercial / Residential / Reserved Site Summaries  
- Department-wise Pending Approvals  
- Approval Status Summary  
- GIS Synchronization Status  
- Recently Updated Layouts / Sites  
- Citizen portal activity summary (applications / enquiries — as applicable)  

Role-based dashboard views shall be supported (executive vs operational sections).

#### 9.2 Standard Reports

- Layout master register  
- Site master register (with filters)  
- Classification and approval pendency report  
- Auction schedule / results report  
- Allotment application / order / possession report  
- CA site register and occupancy report  
- Land Loser register  
- GIS sync exception report  
- Audit / activity reports for privileged actions  

Export to PDF and Excel shall be available for registers and standard reports.

#### 9.3 Acceptance Criteria

| ID | Criterion |
|---|---|
| M9-AC1 | Dashboard KPIs reconcile to underlying registers for an agreed sample period. |
| M9-AC2 | Pendency reports show correct department / stage aging. |
| M9-AC3 | Authorized users can export listed reports to PDF/Excel. |
| M9-AC4 | GIS sync and approval pendency widgets reflect near-real-time operational status. |

---

## 7. End-to-End Workflows

Vendors shall implement the following as **configurable workflows** with maker–checker / multi-level approvals where specified by BDA during requirements finalization. Documents may be attached at relevant steps.

### 7.1 Layout-to-Site Master Flow

```text
Layout Creation → (Optional Approval) → Layout Active
→ Site Creation → Site Documents / Attributes → Site Active
→ Classification Proposal → Department Verification → Multi-level Approval
→ Classification Effective → Available to Eligible Process
```

### 7.2 Auction Flow

```text
Eligible Site → Propose for Auction → Department Approval → Approved for Auction
→ Create Auction Case → Publish Notice → Participation / Bidding Process (as defined)
→ Record Result → Confirm Winner → Update Site Status → Post-Auction Formalities / Documents
```

### 7.3 Allotment Flow

```text
Eligible Site → Scheme / Notification → Application (Officer / Citizen)
→ Scrutiny → Deficiency / Resubmission (if any) → Selection Method as Configured
→ Recommendation → Multi-level Approval → Allotment Order
→ Acceptance → Possession / Handover → Site Status Update
```

### 7.4 CA Site Flow

```text
Site Classification as CA → Approval → CA Register
→ Application / Institutional Proposal → Scrutiny → Approval
→ CA Order / Agreement → Occupancy Status → Renewal / Closure (as applicable)
```

### 7.5 Land Loser Flow

```text
Mark Land Loser → Attach References / Documents → Department Verification
→ Approval → Land Loser Effective on Site Master → Available for Downstream Use
```

### 7.6 GIS Synchronization Flow

```text
Change in LMS or GIS → Sync Event → Success (update peer system)
→ Failure → Exception Queue / Log → Retry / Manual Resolution → Audit Entry
```

---

## 8. Role-Based Access Control

### 8.1 Indicative Roles

| Role | Typical Access |
|---|---|
| Super Administrator | Full configuration, users, masters, workflows |
| Commissioner / Senior Authority | Executive dashboards; high-level approvals |
| Town Planning Officer | Layouts, planning attributes, related approvals |
| Engineering Section User | Layout/site engineering attributes; workflow participation |
| Land Acquisition Section User | Acquisition references; Land Loser verification / approvals |
| Auction Section User | Auction nomination, cases, results, auction approvals |
| Revenue / Allotment Section User | Allotment applications, scrutiny, orders, possession |
| CA Site Section User | CA register, CA allotment / assignment processing |
| Legal Section User | Legal status, litigation flags/documents; related approvals |
| GIS Cell User | GIS sync monitoring, exception resolution, spatial validation |
| Zonal Officer | Zone-scoped layout/site operations and approvals |
| Data Entry Operator | Restricted create/update as assigned |
| Auditor | Read-only access to registers, approvals, and audit logs |
| Citizen / Applicant (Portal) | Public search/view; auction/allotment applications and status as enabled |

### 8.2 Access Principles

- Least privilege; module + action + data-scope (zone / layout) controls.  
- Segregation of duties for propose vs approve on classification, auction, allotment, and CA processes.  
- Citizens see only published / permitted information and their own applications.  
- All privileged actions logged.  

Vendors shall provide a **role–permission matrix** as a deliverable for BDA sign-off during design.

---

## 9. Channels – BDA Officer Portal & Citizen Portal

### 9.1 BDA Officer Portal

- Full operational access based on role for masters, layouts, sites, classification, auction, allotment, CA, Land Loser, GIS sync monitoring, dashboards, and reports.  
- Worklists for pending approvals and sync exceptions.  
- Document upload/view within each process.  

### 9.2 Citizen / Public Portal

The public portal shall support, as enabled by BDA configuration:

- Search and view of **published** layout / site information (fields controlled by BDA).  
- View of published auction notices, schedules, and permitted results summaries.  
- Allotment scheme information and online application / document upload (where enabled).  
- Application status tracking for the logged-in citizen / applicant.  
- Download of issued orders / acknowledgements pertaining to the applicant (where enabled).  
- Contact / help information and circulars published by BDA.  

Sensitive legal, litigation, internal remarks, and non-published classifications shall **not** be exposed on the public portal.

---

## 10. Integrations

| Integration | Priority | Notes |
|---|---|---|
| BDA GIS Platform | Mandatory (Phase 1) | Bidirectional sync of layouts/sites and spatial attributes |
| GeoServer | Mandatory (Phase 1) | Geometry fetch/update, attribute sync, retry, logs |
| SMS Gateway | Mandatory | OTPs, workflow alerts, auction/allotment notices |
| Email Service | Mandatory | Notices, acknowledgements, workflow alerts |
| Payment Gateway | Conditional / Mandatory if online fees/EMD enabled | Auction EMD / allotment fees as decided in RFP |
| Other BDA Applications | Mandatory (API/interface readiness) | Provide validated layout/site master data to approved consumers |
| DigiLocker / Aadhaar eKYC | Optional | Subject to BDA / legal approval; quote separately |

Vendors shall describe approach for secure data exchange, failure handling, and reconciliation for each mandatory integration, without locking BDA to a proprietary interface pattern that prevents future system interconnection.

---

## 11. Audit, Compliance & Security

The system shall maintain:

- Complete audit trail of create / update / delete and approval actions  
- User activity logs and login history  
- Approval history per transaction (classification, auction, allotment, CA, Land Loser, layout publish)  
- Document upload / replace history linked to business records  
- GIS synchronization logs  
- Backup and recovery logs  

Security expectations:

- Secure authentication for officers; citizen registration / login for portal services  
- Optional 2FA for privileged officer roles  
- Password policy and session timeout  
- Protection of personal data of applicants / allottees  
- Role-based restriction on sensitive legal and internal fields  
- Secure handling of documents  

---

## 12. Non-Functional Requirements

| Area | Requirement |
|---|---|
| UI | Responsive web application for officer and citizen channels; accessible design |
| Language | English mandatory at go-live; bilingual-ready (English + Kannada) preferred |
| Performance | Key pages respond within agreed time under agreed concurrent load |
| Availability | Target ≥ 99.5% monthly (final SLA in contract) |
| Backup | Daily automated backups; periodic restore drills |
| Scalability | Support growth in layouts, sites, applications, documents, and users |
| Compatibility | Chrome, Edge, Firefox (latest two major versions) |
| Export | PDF / Excel for registers and reports |
| Search | Global and module-level search & filters |
| DR | Disaster recovery strategy and RPO/RTO to be proposed by vendor |

---

## 13. Data Migration

Legacy data migration is **in scope**.

### 13.1 Migration Scope

- Existing layout registers (digital and structured extracts from manual / Excel / legacy systems).  
- Existing site registers and key attributes (numbering, dimensions, category, status, survey/khata references where available).  
- Historical classification / auction / allotment / CA / Land Loser flags **to the extent data is available and validated by BDA**.  
- Document metadata linkage where digital files are provided; bulk linking of scanned files supplied by BDA.  

### 13.2 Migration Expectations

- Vendor shall provide data templates, validation rules, and import tools.  
- BDA shall nominate data owners for cleansing decisions.  
- Trial migration + reconciliation (counts, sample field checks, exception lists) before final cutover.  
- Post-migration exception register with closure tracking.  
- No go-live on empty masters where BDA has provided loadable legacy data for the agreed scope.  

### 13.3 Acceptance Criteria (Migration)

| ID | Criterion |
|---|---|
| MIG-AC1 | Agreed layout and site counts reconcile between source extracts and LMS after final load. |
| MIG-AC2 | Exception list is reviewed and signed off (accepted residual exceptions documented). |
| MIG-AC3 | Sample of migrated records (including documents where provided) passes BDA verification. |

---

## 14. Phased Delivery

All core functional modules, including **full GIS / GeoServer capabilities**, officer portal, citizen portal (MVP as defined below), and migration of agreed datasets, shall be delivered in **Phase 1**.

### Phase 1 – Full Production Go-Live (Mandatory)

- Module 1: Master Data & System Configuration  
- Module 2: Layout Management  
- Module 3: Site Management & Classification (with embedded workflows & documents)  
- Module 4: Auction Management  
- Module 5: Allotment Management  
- Module 6: CA Site Management  
- Module 7: Land Loser Management  
- Module 8: GIS & GeoServer Synchronization (**complete bidirectional scope**)  
- Module 9: Dashboards & Reports  
- BDA officer portal  
- Citizen / public portal MVP: published search/view, auction notices, allotment application & status (as enabled)  
- SMS / email notifications  
- Payment gateway if online EMD/fees are included in RFP commercial scope  
- Legacy data migration for agreed datasets  
- Training, UAT, go-live, hypercare  

### Phase 2 – Enhancements (Optional / Later)

- Advanced analytics / additional MIS packs  
- Optional DigiLocker / eKYC  
- Kannada UI completion (if not fully delivered in Phase 1)  
- Native mobile apps (optional)  
- Additional downstream BDA application connectors beyond Phase 1 readiness  

Vendors shall provide timelines, milestones, and resource plans aligned to this phasing (or a justified alternative that still delivers **all GIS features in Phase 1**).

---

## 15. Deliverables

| # | Deliverable |
|---|---|
| 1 | Project plan, RAID log, weekly status reports |
| 2 | Requirements Specification & Gap Analysis (against this SOW) |
| 3 | Solution design (functional + security + integration approach) |
| 4 | UI/UX wireframes / prototypes for key officer and citizen journeys |
| 5 | Configured application (all Phase 1 modules) |
| 6 | Completed mandatory integrations (GIS/GeoServer, SMS, email; payment if applicable) |
| 7 | Data migration templates, trial load, final load, reconciliation report |
| 8 | Test plans, test cases, UAT support & UAT sign-off pack |
| 9 | Training (admin + officers + train-the-trainer) & user manuals (officer + citizen) |
| 10 | Administration and operations documentation |
| 11 | Go-live support & hypercare |
| 12 | Source code / escrow as per RFP contract terms |
| 13 | Warranty support and AMC proposal |

---

## 16. Acceptance Criteria (Program Level)

The solution shall be accepted when:

1. All Phase 1 modules meet the module acceptance criteria in Section 6.  
2. GIS / GeoServer bidirectional synchronization is demonstrated in UAT/production as agreed, including failure/retry visibility.  
3. Auction, Allotment, CA, and Land Loser processes operate only on approved / eligible sites.  
4. Citizen portal publishes only permitted fields and supports configured application journeys.  
5. Sample / final data migration reconciles for agreed layouts and sites.  
6. UAT sign-off by BDA-designated committee with no open **Critical / High** defects.  
7. Training completed for nominated users.  
8. Dashboards/reports reconcile to registers for an agreed sample period.  
9. Security checklist (authentication, RBAC, audit, document access, backup restore test) signed off.  

---

## 17. Expected Benefits

- Single authoritative digital register of BDA layouts and sites  
- Elimination of duplicate and inconsistent departmental site records  
- Controlled, auditable classification before Auction / Allotment / CA / Land Loser use  
- Digitized end-to-end Auction, Allotment, and CA Site processes  
- Spatial and attribute consistency with BDA GIS / GeoServer from day one  
- Transparent citizen access to published information and eligible applications  
- Faster approvals with department worklists and complete history  
- Better management visibility through dashboards and MIS  
- Reduced manual effort, paperwork, and operational delays  
- Stronger compliance, accountability, and inter-system data quality  

---

## 18. Assumptions & Dependencies

1. BDA will nominate a Product Owner / nodal officer and section SMEs for timely decisions on rules and workflows.  
2. BDA will provide legacy layout/site data in agreed templates and nominate ownership for cleansing decisions.  
3. BDA will provide access to GIS / GeoServer environments, credentials, and technical counterparts for Phase 1 integration.  
4. SMS, email, and (if applicable) payment gateway credentials / approvals will be facilitated by BDA.  
5. Final auction mode (including e-auction mechanics) and allotment selection method will be confirmed during requirements workshops within the functional boundaries of this SOW.  
6. Digitization of physical files remains BDA’s responsibility.  
7. Hosting decision and security clearances will follow the RFP / contract.  
8. Kannada content (if required at go-live) will be reviewed and approved by BDA.  
9. Court processes remain outside the system except status, key dates, and linked documents.  

---

## 19. Vendor Response Expectations

RFP responses shall include at minimum:

1. Understanding of this SOW and proposed module mapping.  
2. Functional compliance matrix (clause-by-clause against Section 6).  
3. Approach for embedded document handling and configurable workflows (not as separate products).  
4. GIS / GeoServer synchronization approach and Phase 1 readiness evidence.  
5. Citizen portal vs officer portal scope and information disclosure controls.  
6. Data migration approach and cutover plan.  
7. Implementation methodology, timeline, team profiles, and milestones.  
8. Commercial proposal aligned to Phase 1 and optional Phase 2 items.  
9. Case studies of similar government land / layout / allotment / auction systems.  
10. Assumptions, exclusions, and dependencies.  
11. Post-go-live support / AMC model and SLAs.  

---

## Appendix A – Module Consolidation Map

| Consolidated Module | Baseline Topics Included |
|---|---|
| 1. Master Data & System Configuration | Master data; users/roles; workflow configuration (not a separate workflow module) |
| 2. Layout Management | Layout lifecycle + layout documents + layout approvals |
| 3. Site Management & Classification | Site lifecycle; multi-category classification; classification approvals; search |
| 4. Auction Management | Auction eligibility, cases, notices, results, post-auction updates + documents/approvals |
| 5. Allotment Management | Applications, scrutiny, selection recording, orders, possession + documents/approvals |
| 6. CA Site Management | CA register; CA allotment/assignment/lease lifecycle + documents/approvals |
| 7. Land Loser Management | Land Loser marking, verification, approval, publishing + documents |
| 8. GIS & GeoServer Synchronization | Full bidirectional GIS/GeoServer scope (Phase 1) |
| 9. Analytics, Dashboards & Reports | Dashboards, MIS, operational and management reports |

**Explicitly not separate modules:** Document Management; Workflow Engine (capabilities embedded across Modules 1–8).

---

## Appendix B – Indicative Data Entities

Layout, Site, Site Classification, Approval Instance, Department, Zone, Location Hierarchy, Document, Photograph, Auction Case, Auction Participant / Bid Result, Allotment Application, Allotment Order, Possession Record, CA Site Case, Land Loser Record, GIS Sync Log, User, Role, Notification, Audit Log.

---

## Appendix C – Document Types (Indicative)

Approved Layout Plans, Survey Sketches, Government Orders, Acquisition Documents, Court Orders, Khata Documents, Site Sketches, Classification Approval Documents, GIS Reference Documents, Supporting Certificates, Auction Notices / Proceedings, Allotment Applications / Orders, Possession Certificates, CA Agreements / Orders, Land Loser Entitlement Documents.

---

*This SOW provides the RFP foundation for a full-scale BDA Layout Master & Site Management System covering layout and site master data, classification controls, Auction, Allotment, CA Site and Land Loser processes, GIS/GeoServer synchronization, citizen and officer channels, migration, and executive reporting.*

**End of Document**
