# Statement of Work (SOW)

# Bangalore Development Authority (BDA)  
# Commercial Property Management System (CPMS)

**Document Type:** Request for Proposal (RFP) – Statement of Work  
**Version:** 1.0  
**Status:** Draft for RFP  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Architecture Expectations](#5-solution-architecture-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Role-Based Access Control](#8-role-based-access-control)
9. [Integrations](#9-integrations)
10. [Audit, Compliance & Security](#10-audit-compliance--security)
11. [Non-Functional Requirements](#11-non-functional-requirements)
12. [Phased Delivery](#12-phased-delivery)
13. [Deliverables](#13-deliverables)
14. [Acceptance Criteria (Program Level)](#14-acceptance-criteria-program-level)
15. [Expected Benefits](#15-expected-benefits)
16. [Assumptions & Dependencies](#16-assumptions--dependencies)
17. [Vendor Response Expectations](#17-vendor-response-expectations)

---

## 1. Introduction

This Statement of Work (SOW) defines the functional, technical, and delivery requirements for the design, development, implementation, and support of a **Commercial Property Management System (CPMS)** for the **Bangalore Development Authority (BDA)**.

The SOW is intended for use in an **RFP**. Responding vendors shall propose a complete solution covering application software, implementation services, data migration support, training, documentation, and warranty/AMC, as specified in this document and the RFP package.

Related modules from the baseline requirements have been **consolidated** into eight logical modules to reduce overlap, clarify ownership of capabilities, and simplify estimation and delivery.

---

## 2. Project Overview

BDA intends to implement a centralized digital platform to manage the complete lifecycle of BDA-owned commercial properties, including:

- Commercial complexes and shopping complexes  
- Individual shops and office spaces  
- Commercial buildings and open commercial sites  
- Parking areas and vacant spaces  
- Rental / lease agreements and tenant management  
- Revenue collection, expenditure, maintenance, and statutory compliance  
- Financial reporting, dashboards, and MIS  

The system shall replace fragmented manual and spreadsheet-driven processes with a single source of truth for property inventory, occupancy, leases, billing, collections, utilities, taxes, maintenance, vendors, documents, and executive reporting.

### 2.1 Property Types to Be Supported

| Category | Examples |
|---|---|
| Built commercial assets | Complexes, buildings, shops, offices |
| Open / site assets | Open commercial sites, vacant plots (commercial) |
| Ancillary assets | Parking bays, common areas (as rentable / allocatable units) |
| Operational states | Vacant, occupied, under maintenance, reserved, auctioned, under litigation, blocked |

---

## 3. Project Objectives

1. Digitize and centralize all commercial property records and inventory.  
2. Maintain a single, authoritative property and unit register with occupancy status.  
3. Digitize tenant onboarding, KYC, and lease lifecycle management.  
4. Automate rent demand generation, collections, arrears, penalties, and GST handling.  
5. Track security deposits, utilities, property tax, and related statutory payments.  
6. Manage maintenance complaints, work orders, vendors, and property expenditures.  
7. Provide configurable approval workflows with full audit trails.  
8. Deliver real-time dashboards and statutory / management reports.  
9. Improve transparency, accountability, revenue realization, and citizen (tenant) service.  

---

## 4. In Scope / Out of Scope

### 4.1 In Scope

- Responsive web application for BDA officers and administrators.  
- Tenant self-service portal (view dues, pay rent/utilities where enabled, raise complaints, download receipts/notices, view lease summary).  
- Field/mobile-friendly web screens for inspections and complaint updates (responsive; native mobile app may be proposed as optional/phase 2).  
- Master data, property inventory, lease lifecycle, billing & collections, utilities, property tax, expenditure, maintenance, vendors, documents, notices, vacancy tracking, dashboards, and reports.  
- Configurable masters, rent revision / penalty / deposit rules, and multi-level approval workflows.  
- Integrations listed in Section 9 (payment gateway, SMS, email, GIS/maps; others as optional/approved).  
- Role-based access control, audit logging, document repository, PDF/Excel export.  
- Data migration support from existing Excel/manual registers (templates + import + validation).  
- Training, UAT support, go-live support, warranty, and documentation.  

### 4.2 Out of Scope (unless explicitly added via change request)

- Full court case / legal case management system beyond **status flags, key dates, linked documents, and notices**.  
- Public auction portal / e-auction engine (allocation may support “auctioned” status and post-allotment lease capture; auction bidding platform is out of scope).  
- Full ERP / accounting general ledger replacement (integration hooks only).  
- DigiLocker and Aadhaar eKYC (optional; subject to BDA/legal approval — vendors shall quote as optional line items).  
- Native iOS/Android apps (optional; vendor may propose separately).  
- Hardware procurement (servers, biometric devices, POS, etc.), unless stated in RFP commercial section.  
- Digitization / scanning of legacy physical files (BDA responsibility; system shall accept uploaded scans).  

---

## 5. Solution Architecture Expectations

Vendors shall propose an architecture that meets the following expectations:

| Area | Expectation |
|---|---|
| Deployment | Secure cloud (MeitY-empaneled / government-approved) or on-premises / hybrid as specified in RFP; BDA to decide |
| Access | Browser-based (Chrome, Edge, Firefox); responsive for tablet/mobile |
| Multi-tenancy of data | Single BDA organization with hierarchical location (Zone → Division → Circle → Ward → Layout) and property hierarchy |
| Scalability | Support growth in properties, tenants, transactions, and concurrent users without redesign |
| Availability | High availability design; RPO/RTO as defined in NFR |
| Security | SSL/TLS, RBAC, optional 2FA, encryption at rest for sensitive documents/PII where applicable |
| APIs | Well-documented REST APIs for integrations and future extensions |
| Auditability | Immutable-style audit trail for financial and approval actions |

---

## 6. Consolidated Functional Modules

The solution shall be delivered as **eight consolidated modules**. Each module below includes purpose, functional requirements, key entities, and acceptance criteria.

---

### Module 1: Master Data & System Configuration

**Purpose:** Provide configurable foundation data, business rules, users/roles, and approval workflow configuration used across all other modules.

#### 1.1 Functional Requirements

**A. Property & Location Masters**

- Commercial Complex, Building, Floor, Shop/Unit, Parking Area, Open Space masters.  
- Utility Meter Master and Asset Master (linked to property/unit).  
- Location hierarchy: Zone, Division, Circle, Ward, Layout, Survey Number.  
- Ability to activate/deactivate masters without deleting historical references.  

**B. Rental & Financial Masters**

- Property Category, Property Type, Lease Type.  
- Rent Revision Rules (periodic %, slab-based, or fixed schedule).  
- Penalty Rules (grace period, daily/monthly interest or flat penalty).  
- Deposit Rules (multiples of rent, interest applicability, forfeiture conditions — configurable).  
- GST Configuration (HSN/SAC if applicable, tax rates, taxability by charge type).  
- Expense Category, Income Category, Utility Types, Tax Types.  
- Payment Modes, Bank Masters.  

**C. User, Role & Workflow Configuration**

- Create/manage users, roles, and permission sets.  
- Map users to organizational units / properties (data scoping).  
- Configure multi-level approval workflows (property creation, lease, refunds, write-offs, expenditure above threshold, vacancy marketing status changes, etc.).  
- Configurable notice templates (SMS/email/PDF).  
- System parameters (financial year, billing cycle cut-off, receipt series, etc.).  

#### 1.2 Key Capabilities

- Search, filter, export of masters.  
- Versioning or effective-date support for rules that change over time (rent revision, GST, penalty).  
- Prevention of orphaned references when deactivating masters.  

#### 1.3 Acceptance Criteria

| ID | Criterion |
|---|---|
| M1-AC1 | Authorized admin can create and configure all listed masters without code change. |
| M1-AC2 | Rent revision, penalty, deposit, and GST rules can be changed with effective dates and applied to new bill runs correctly. |
| M1-AC3 | Approval workflows are configurable by transaction type and amount threshold. |
| M1-AC4 | Role permissions restrict module and record visibility as configured. |
| M1-AC5 | Deactivated masters cannot be selected for new transactions but remain visible on historical records. |

---

### Module 2: Property & Asset Inventory

**Purpose:** Maintain complete inventory of commercial properties, buildings, units, parking, and vacancy status as the system of record.

*(Consolidates: Commercial Property Management, Building Management, Parking Inventory, Vacancy Management)*

#### 2.1 Functional Requirements

**A. Property & Building Register**

- Capture and maintain property details: Property Code (system-generated and/or BDA code), Name, Complex, Type, Address, Geo-location (lat/long + map pin), Floor/Shop attributes, Carpet / Built-up / Rentable area, photographs, documents, current status.  
- Building information: floors, total shops/offices, parking capacity, lifts, utility connections, fire safety details, building age, computed occupancy %.  
- Hierarchical navigation: Complex → Building → Floor → Unit / Shop / Parking bay / Open space.  

**B. Property Status Lifecycle**

Statuses shall include at minimum:

| Status | Description |
|---|---|
| Vacant | Available / not leased |
| Occupied | Active lease |
| Under Maintenance | Temporarily not allocatable |
| Reserved | Soft hold pending allotment |
| Auctioned | Allotted via auction (post-process capture) |
| Under Litigation | Legal hold |
| Blocked | Administrative block |

Status changes shall be audited and may require approval based on configuration.

**C. Parking Inventory (as asset/units)**

- Parking inventory by complex/building.  
- Allocation linkage to tenant/lease (detailed commercial parking rent handled with lease/billing).  
- Occupancy and visitor/reserved parking classification.  

**D. Vacancy Management**

- Vacant since date, expected revenue loss (system-calculated from last/proposed rent × vacant days).  
- Marketing status, inspection readiness, proposed rent, ready-for-allocation flag.  
- Vacancy pipeline views for Estate/Property managers.  

#### 2.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M2-AC1 | Every rentable unit has a unique identifier and current status. |
| M2-AC2 | Occupancy % for a building updates automatically from unit statuses. |
| M2-AC3 | Vacancy report shows vacant units with duration and estimated revenue loss. |
| M2-AC4 | Geo-location can be captured and viewed on map (via GIS/map integration). |
| M2-AC5 | Status transitions follow configured approval rules and are fully audited. |

---

### Module 3: Tenant & Lease Lifecycle

**Purpose:** Manage tenants, allotment/lease creation, handover, renewals/termination, security deposits, and lease-related notices.

*(Consolidates: Tenant Management, Property Allocation / Lease Management, Security Deposit Management, lease-related Notice Management)*

#### 3.1 Functional Requirements

**A. Tenant Registration**

- Tenant types: Individual, Partnership, Company, Trust, Society.  
- Tenant profile: Tenant ID, Aadhaar/PAN (as applicable), GSTIN, contacts, business type, emergency contact, bank details, KYC documents.  
- Duplicate detection on PAN/GSTIN/Aadhaar (configurable).  
- Tenant portal credentials issuance and reset (for portal users).  

**B. Allocation / Lease Process**

Supported process (configurable approvals at each gate):

1. Property availability check  
2. Application capture  
3. Verification  
4. Approval  
5. Lease agreement generation / upload  
6. Security deposit collection  
7. Property handover checklist & possession certificate  
8. Rent billing commencement  
9. Renewal or termination / vacating  

**C. Lease Information**

- Lease number, period, monthly rent, escalation schedule, grace period, penalty rule linkage, renewal/expiry dates, special conditions.  
- Link lease to one or more units/parking bays.  
- Amendment history (rent change, area change, party change) with approvals.  

**D. Security Deposit**

- Collection, adjustment against dues, refund, forfeiture.  
- Interest calculation if configured.  
- Refund workflow with approvals and payment processing status.  

**E. Notices (Lease & Dues Related)**

Auto and manual generation of:

- Rent due / overdue  
- Lease expiry / renewal reminder  
- Eviction / legal notice (template-based; legal process remains offline)  
- Deposit-related notices  

Delivery channels: in-app, email, SMS, downloadable PDF. Delivery status logged.

#### 3.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M3-AC1 | A lease cannot be activated without required KYC, approved application, and deposit collection (or approved waiver). |
| M3-AC2 | Handover records possession date and checklist; unit status becomes Occupied. |
| M3-AC3 | System generates renewal/expiry alerts based on configurable lead time. |
| M3-AC4 | Deposit refund/forfeiture follows approval workflow and updates tenant ledger. |
| M3-AC5 | All lease amendments retain previous version history and audit trail. |

---

### Module 4: Revenue Billing & Collections

**Purpose:** Automate demand generation, multi-mode collections, receipts, arrears, penalties, GST, and revenue ledgers.

*(Consolidates: Rent Billing & Collection; deposit adjustments impacting dues; payment-facing parts of notices)*

#### 4.1 Functional Requirements

**A. Billing / Demand Generation**

- Automatic monthly (or configured cycle) rent demand.  
- Charge components: Monthly Rent, Advance Rent, Arrears, Penalties, GST, Interest, Miscellaneous charges, Parking rent, CAM/other lease-linked charges.  
- Bulk bill run by complex / property group / billing cycle with exception report.  
- Manual ad-hoc demand with approval (where configured).  
- Credit notes / demand cancellation with maker-checker.  

**B. Collections & Payment Modes**

- Online payment (payment gateway), UPI, Bank Transfer, NEFT/RTGS, DD, Cheque, Cash (as enabled).  
- Reconciliation aids for offline instruments (cheque bounce handling, realization dates).  
- Partial payments and allocation rules (configurable priority: penalty → interest → arrears → current, or as configured).  
- Auto-receipt generation (digital PDF) and payment history.  
- Outstanding statement per tenant/lease/property.  

**C. Tenant Portal Payments**

- View current dues and history.  
- Pay selected outstanding demands online.  
- Download receipts and statements.  

**D. Arrears & Defaulters**

- Ageing buckets (e.g., 0–30, 31–60, 61–90, 90+).  
- Defaulter lists for notices and escalation.  

#### 4.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M4-AC1 | Scheduled bill run generates correct demands for all active leases for the cycle. |
| M4-AC2 | GST and penalty calculations match configured rules for sample test cases provided by BDA. |
| M4-AC3 | Online payment updates demand status and generates receipt without manual intervention. |
| M4-AC4 | Partial payment allocation follows configured priority rules. |
| M4-AC5 | Outstanding, collection %, and ageing reports reconcile to transaction ledgers. |

---

### Module 5: Utilities & Statutory Payments

**Purpose:** Track utility consumption/billing and property tax assessments/payments at property or unit level.

*(Consolidates: Utility Management, Property Tax Management)*

#### 5.1 Functional Requirements

**A. Utility Management**

- Utilities: Electricity, Water, DG charges, Common Area Maintenance, Sewage, and configurable other types.  
- Meter master linkage; previous/current reading; units consumed; bill amount; due date; payment status.  
- Support both: (i) BDA-paid utilities recovered from tenants, and (ii) informational tracking of property-level utility bills.  
- Upload of utility bills/receipts.  
- Alerts for overdue utility payments.  

**B. Property Tax Management**

- Tax assessment records: assessment details, tax amount, due date, payment status.  
- Challan and receipt upload.  
- Outstanding tax and tax payment history by property.  
- Link tax payments to expenditure where BDA pays tax (cross-module reference).  

#### 5.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M5-AC1 | Meter reading entry validates current ≥ previous (with override + reason where allowed). |
| M5-AC2 | Utility dues can be billed to tenant lease account when recovery is enabled. |
| M5-AC3 | Property tax register shows assessment, due, paid, and outstanding per property. |
| M5-AC4 | Overdue utility/tax items appear on dashboards and notice candidates. |

---

### Module 6: Operations, Maintenance & Expenditure

**Purpose:** Manage complaints, inspections, work orders, vendors/contractors, and all property-related expenditures.

*(Consolidates: Maintenance Management, Vendor & Contractor Management, Inspection Management, Expenditure Management)*

#### 6.1 Functional Requirements

**A. Complaint & Maintenance Workflow**

Categories: Electrical, Plumbing, Civil, Cleaning, Lift, Parking, Security, Others (configurable).

Workflow:

1. Complaint registration (officer or tenant portal)  
2. Assign engineer / agency  
3. Inspection  
4. Work order  
5. Completion  
6. Verification  
7. Closure  

- SLA timers and escalation (configurable).  
- Photo/document attachment at each stage.  
- Link to vendor and expenditure/payment.  

**B. Inspection Management**

- Periodic and ad-hoc inspection schedules.  
- Checklist templates by property type.  
- Observations, photo upload, recommendations, closure.  
- Findings may spawn maintenance work orders.  

**C. Vendor & Contractor Management**

- Vendor registration: GST, PAN, bank details, agreements, AMC contracts.  
- Performance history and rating (basic).  
- Work assignment, cost estimate, completion certificate, payment processing linkage.  
- Blacklist / inactive status.  

**D. Expenditure Management**

Expense categories including (configurable): Civil, Painting, Plumbing, Electrical, Lift, Housekeeping, Security, Generator, Landscaping, Pest Control, Water, Electricity, Property Tax, Insurance, Miscellaneous.

For each expense:

- Property/unit linkage, vendor, invoice no./date, amount, GST, payment status, documents.  
- Approval workflow by amount threshold.  
- Budget vs actual views (if budgets are maintained; optional simple annual budget by category/property).  

#### 6.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M6-AC1 | Tenant/officer can raise a complaint; status is trackable end-to-end. |
| M6-AC2 | Work order cannot close without verification when configured. |
| M6-AC3 | Inspection schedule generates due inspections and records checklist completion. |
| M6-AC4 | Vendor payments are linkable to work orders/invoices and require configured approvals. |
| M6-AC5 | Property-wise expense reports match posted expenditure transactions. |

---

### Module 7: Documents & Compliance

**Purpose:** Centralized document repository, notice generation framework, and compliance artefacts linked to properties, tenants, and leases.

*(Consolidates: Document Management, Notice Management [cross-cutting], compliance artefacts)*

#### 7.1 Functional Requirements

**A. Document Management**

Store and classify documents such as:

- Lease agreement, possession certificate, building plan  
- Property tax receipts, utility bills, insurance, NOC  
- Photographs, KYC, vendor agreements, completion certificates  
- Legal/litigation related uploads (supporting docs only)  

Capabilities:

- Upload, versioning, tag/category, link to entity (property/tenant/lease/vendor/complaint).  
- Preview (common formats), download, access control by role.  
- Retention flags / archival status (configurable).  

**B. Notice Framework**

- Template management (merge fields from tenant/lease/dues data).  
- Batch notice generation for overdue rent, lease expiry, utility due, property tax due, legal/eviction templates.  
- Channel dispatch (SMS/email) + PDF archive in DMS.  
- Delivery and acknowledgement logs (acknowledgement where available).  

#### 7.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M7-AC1 | Every lease and property can store multiple categorized documents with version history. |
| M7-AC2 | Unauthorized roles cannot download restricted document categories. |
| M7-AC3 | Batch overdue notices generate correctly for a selected ageing cohort and are archived. |
| M7-AC4 | Document search returns results by property, tenant, lease, and document type. |

---

### Module 8: Analytics, Dashboards & Reports

**Purpose:** Provide operational MIS, executive dashboards, and exportable statutory/management reports.

*(Consolidates: Dashboard & MIS, Reports)*

#### 8.1 Dashboards

**Property Dashboard**

- Total / Occupied / Vacant / Under Maintenance / Under Litigation counts  
- Parking utilization  

**Revenue Dashboard**

- Rent demand, collected, pending, collection %  
- Security deposit position  
- Utility & tax collections (where applicable)  

**Expenditure Dashboard**

- Total expenses by category; maintenance; repairs; tax; vendor payments  

**Financial Dashboard**

- Revenue → Expenses → Net Income → Outstanding → Receivables → Cash flow (period filters)  

**Property Health Dashboard**

- High expense / low revenue properties  
- Vacancy trend  
- Lease expiry pipeline  
- Utility consumption trend  

Drill-down from KPI tiles to underlying registers shall be supported.

#### 8.2 Standard Reports

| Group | Reports |
|---|---|
| Property | Property Register, Vacancy, Occupancy, Property-wise Revenue, Property-wise Expense |
| Tenant / Lease | Tenant Register, Lease Expiry, Rent Collection, Outstanding, Security Deposit |
| Financial | Income, Expense, P&L Summary, Cash Collection, Tax, Utility Expense |
| Maintenance | Complaint, Work Order, Vendor Performance, AMC |

All reports: filterable, role-scoped, exportable to **PDF and Excel**.

#### 8.3 Acceptance Criteria

| ID | Criterion |
|---|---|
| M8-AC1 | Dashboard KPIs reconcile to transactional data for a closed test period. |
| M8-AC2 | All listed standard reports are available with filters and Excel/PDF export. |
| M8-AC3 | Users only see dashboard/report data within their authorized property scope. |
| M8-AC4 | Lease expiry and vacancy trend widgets update based on live status/dates. |

---

## 7. End-to-End Workflows

### 7.1 Core Property-to-Revenue Flow

```text
Property Creation → Property Approval → Tenant Registration → Lease Creation
→ Security Deposit Collection → Property Handover → Monthly Rent Billing
→ Rent Collection → Utility & Maintenance Tracking → Expenditure Recording
→ Renewal / Vacating → Dashboard & Reports
```

### 7.2 Maintenance Flow

```text
Complaint → Assign Engineer → Inspection → Work Order → Completion
→ Verification → Closure → (Optional) Vendor Payment / Expenditure Posting
```

### 7.3 Inspection Flow

```text
Inspection Schedule → Checklist → Observation → Photo Upload
→ Recommendations → Closure → (Optional) Spawn Work Order
```

### 7.4 Vacancy-to-Allocation Flow

```text
Mark Vacant → Inspection / Make-ready → Proposed Rent → Ready for Allocation
→ Application → Verification → Approval → Lease → Deposit → Handover
```

Vendors shall implement these as configurable workflows with maker-checker / multi-level approvals where specified by BDA during requirements finalization.

---

## 8. Role-Based Access Control

### 8.1 Indicative Roles

| Role | Typical Access |
|---|---|
| Super Administrator | Full configuration, users, workflows |
| Commissioner | Executive dashboards, approvals (high value) |
| Chief Engineer | Maintenance/works oversight, approvals |
| Estate Officer | Property, lease, vacancy, allotment |
| Property Manager | Day-to-day property & tenant operations |
| Accounts Officer | Billing, collections, deposits, refunds |
| Revenue Officer | Demand, arrears, notices, collection follow-up |
| Maintenance Officer | Complaints, work orders, inspections |
| Tax Officer | Property tax register & payments |
| Utility Officer | Utility meters, readings, bills |
| Auditor | Read-only financial & audit logs |
| Data Entry Operator | Restricted create/update as assigned |
| Tenant (Portal) | Own lease, dues, payments, complaints, documents |

### 8.2 Access Principles

- Least privilege; module + action + data-scope (location/property) controls.  
- Segregation of duties for demand creation vs collection vs refund approval.  
- All privileged actions logged.  

Vendors shall provide a **role–permission matrix** as a deliverable for BDA sign-off during design.

---

## 9. Integrations

| Integration | Priority | Notes |
|---|---|---|
| Payment Gateway (Razorpay / SBI / other govt-approved) | Mandatory | Online rent & other dues |
| SMS Gateway | Mandatory | OTPs, notices, reminders |
| Email Service | Mandatory | Notices, receipts, workflow alerts |
| GIS / Map Services | Mandatory | Property geo-tagging & map views |
| Accounting / ERP | Optional / Phase | Push collections & expenses via API |
| Karnataka Government Treasury | Optional | If applicable and approved |
| DigiLocker | Optional | Subject to approval |
| Aadhaar eKYC | Optional | Subject to legal/BDA approval |

Vendors shall describe API approach, failure handling, reconciliation, and security for each mandatory integration.

---

## 10. Audit, Compliance & Security

The system shall maintain:

- Complete audit trail of create/update/delete and approval actions  
- User activity logs and login history  
- Approval history per transaction  
- Document version history  
- Digital receipts and transaction logs  
- Backup & recovery logs  

Security expectations:

- Secure authentication; optional 2FA  
- Password policy; session timeout  
- Encryption in transit (TLS); encryption at rest for sensitive content as applicable  
- Protection of PII (Aadhaar/PAN masking in UI where required)  
- Regular vulnerability management process during warranty/AMC  

---

## 11. Non-Functional Requirements

| Area | Requirement |
|---|---|
| UI | Responsive web application; accessible, bilingual-ready (English + Kannada UI labels preferred; English mandatory at go-live) |
| Performance | Key pages < 3s under agreed concurrent user load; bill run performance sized to BDA data volume |
| Availability | Target ≥ 99.5% monthly (final SLA in contract) |
| Backup | Daily automated backups; periodic restore drills |
| Scalability | Horizontal scale for app; growth in properties/transactions |
| Compatibility | Chrome, Edge, Firefox (latest 2 major versions) |
| Export | PDF / Excel for registers and reports |
| Search | Global and module-level search & filters |
| Monitoring | Application performance & error monitoring |
| DR | DR strategy and RPO/RTO to be proposed by vendor |

---

## 12. Phased Delivery

Recommended phasing for RFP responses (vendors may propose equivalent with justification):

### Phase 1 – Foundation & Core Revenue (Priority)

- Module 1: Masters & Configuration  
- Module 2: Property & Asset Inventory (including vacancy views)  
- Module 3: Tenant & Lease Lifecycle (including deposits & core notices)  
- Module 4: Revenue Billing & Collections (+ payment gateway, SMS, email)  
- Module 7: Core DMS for lease/KYC/receipts  
- Module 8: Core dashboards & revenue/property reports  
- Tenant portal: view dues, pay, download receipts  

### Phase 2 – Operations & Statutory

- Module 5: Utilities & Property Tax  
- Module 6: Maintenance, Inspections, Vendors, Expenditure  
- Extended notices, property health dashboards, maintenance reports  
- Tenant portal: complaints  

### Phase 3 – Optimization & Optional Integrations

- ERP/Treasury connectors  
- Optional DigiLocker / eKYC  
- Advanced analytics, Kannada UI completion, optional native mobile  

Vendors shall provide timelines, milestones, and resource plans aligned to this phasing (or justified alternative).

---

## 13. Deliverables

| # | Deliverable |
|---|---|
| 1 | Project plan, RAID log, weekly status reports |
| 2 | Requirements Specification & Gap Analysis (against this SOW) |
| 3 | Solution Architecture & Security Design |
| 4 | UI/UX wireframes / prototypes for key journeys |
| 5 | Configured application (all in-scope modules per phase) |
| 6 | Integration design & completed mandatory integrations |
| 7 | Data migration templates, cleaned import, reconciliation report |
| 8 | Test plans, test cases, UAT support & UAT sign-off pack |
| 9 | Training (admin + officer + train-the-trainer) & user manuals |
| 10 | Admin & technical documentation, API docs |
| 11 | Go-live support & hypercare |
| 12 | Source code / escrow as per RFP contract terms |
| 13 | Warranty support and AMC proposal |

---

## 14. Acceptance Criteria (Program Level)

The solution shall be accepted when:

1. All Phase-wise modules meet module acceptance criteria in Section 6.  
2. Mandatory integrations are live in the UAT/production environments as agreed.  
3. Sample data migration for agreed properties/leases reconciles (counts + financial totals).  
4. UAT sign-off by BDA-designated committee with no open **Critical/High** defects.  
5. Training completed for nominated users.  
6. Dashboards/reports reconcile to ledgers for an agreed closed period.  
7. Security checklist (auth, RBAC, audit, TLS, backup restore test) signed off.  

---

## 15. Expected Benefits

- 100% digital management of BDA commercial properties in scope  
- Improved rental revenue through automated billing, reminders, and arrears visibility  
- Real-time occupancy and vacancy visibility  
- Better control of maintenance and utility expenditures  
- Centralized lease and property document repository  
- Timely tracking of electricity, water, property tax, and other statutory payments  
- Transparent approvals with complete audit trails  
- Accurate financial reporting and decision-support dashboards  
- Reduced manual effort, paperwork, and operational delays  
- Improved compliance, accountability, and tenant service  

---

## 16. Assumptions & Dependencies

1. BDA will nominate a Product Owner / nodal officer and module SMEs for timely decisions.  
2. BDA will provide existing property/tenant/lease/financial data in agreed templates.  
3. Payment gateway, SMS, and email service credentials/approvals will be facilitated by BDA.  
4. DigiLocker / Aadhaar eKYC remain optional pending statutory approval.  
5. Legal eviction and court processes remain outside the system except status/docs/notices.  
6. Hosting decision (cloud/on-prem) and security clearances will follow RFP/contract.  
7. Kannada translation content (if required at go-live) will be reviewed/approved by BDA.  

---

## 17. Vendor Response Expectations

RFP responses shall include at minimum:

1. Understanding of this SOW and proposed consolidated module mapping.  
2. Functional compliance matrix (clause-by-clause against Section 6).  
3. Technical architecture, security, hosting, and DR approach.  
4. Implementation methodology, phasing, timeline, and team CVs.  
5. Integration approach for mandatory items.  
6. Data migration approach and sample cutover plan.  
7. Commercial proposal aligned to phases and optional items.  
8. Case studies of similar government / large property or estate management systems.  
9. Assumptions, exclusions, and dependencies.  
10. Post-go-live support / AMC model and SLAs.  

---

## Appendix A – Module Consolidation Map

| Consolidated Module | Baseline Topics Merged |
|---|---|
| 1. Master Data & System Configuration | Master Management + User & Role Management + workflow/config |
| 2. Property & Asset Inventory | Commercial Property + Building + Parking inventory + Vacancy |
| 3. Tenant & Lease Lifecycle | Tenant + Allocation/Lease + Security Deposit + lease notices |
| 4. Revenue Billing & Collections | Rent Billing & Collection (+ payment/receipts) |
| 5. Utilities & Statutory Payments | Utility Management + Property Tax Management |
| 6. Operations, Maintenance & Expenditure | Maintenance + Vendor/Contractor + Inspection + Expenditure |
| 7. Documents & Compliance | Document Management + Notice framework |
| 8. Analytics, Dashboards & Reports | Dashboard & MIS + Reports |

---

## Appendix B – Indicative Data Entities

Property, Building, Floor, Unit/Shop, Parking Bay, Open Space, Meter, Asset, Tenant, Lease, Lease Amendment, Security Deposit, Demand/Invoice, Payment/Receipt, Utility Bill, Property Tax Assessment, Complaint, Work Order, Inspection, Vendor, Contract/AMC, Expense, Document, Notice, User, Role, Approval Instance, Audit Log.

---

*This SOW provides the RFP foundation for a full-scale BDA Commercial Property Management System covering the end-to-end lifecycle of commercial assets—from inventory and tenant onboarding to lease administration, revenue collection, operations, compliance, and executive reporting.*

**End of Document**
