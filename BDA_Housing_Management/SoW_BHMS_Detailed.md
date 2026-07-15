# Statement of Work (SOW)

# Bangalore Development Authority (BDA)  
# BDA Housing Management System (BHMS)

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
9. [Channels – Officer Portal & Citizen Portal](#9-channels--officer-portal--citizen-portal)
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

This Statement of Work (SOW) defines the functional and delivery requirements for the design, development, implementation, data migration support, training, and support of the **BDA Housing Management System (BHMS)** for the **Bangalore Development Authority (BDA)**.

The SOW is intended for use in an **RFP**. Responding vendors shall propose a complete solution covering application software, implementation services, training, documentation, and warranty / AMC, as specified in this document and the RFP package.

BHMS shall digitally manage the end-to-end lifecycle of BDA **Flats and Villas** — from project and inventory publication through citizen application, first-come-first-served booking, online payment, allotment, sale deed generation, offline registration recording, possession, cancellation/refund, and bank/loan NOC — with complete process history for officers and citizens.

**Document management** and **approval workflows** are not separate product modules. They shall be built into every relevant business process so that documents and approvals travel with the transaction.

---

## 2. Project Overview

BDA intends to implement a centralized web-based platform to manage housing projects (Flats and Villas), including:

- Housing project creation, approval, and publication  
- Flat and Villa inventory with pricing, status, and documents  
- Housing notifications for public booking windows  
- Citizen registration and self-service portal  
- Online and officer-assisted (offline-entry) applications under the **same** process  
- **First-come-first-served** booking (no lottery / draw in baseline scope)  
- Online payment of booking amount, balance, and applicable charges  
- Allotment letter, draft sale deed generation, offline registration capture, and possession  
- Cancellation, refund, and automatic cancellation for non-payment  
- Bank / loan NOC processing  
- Dashboards, MIS, notifications (SMS / email / portal), and audit  

The system shall provide transparency across the housing allotment process and real-time visibility to authorized BDA officials and to each citizen for their own transactions.

### 2.1 Property Types

| Type | Description |
|---|---|
| Flat | Apartment unit under a tower/block/floor within a housing project |
| Villa | Individual villa unit (including plot area where applicable) under a housing project |

### 2.2 Booking Model

| Rule | Baseline decision |
|---|---|
| Selection method | **First-come-first-served** — a unit may be booked by only one applicant at a time |
| Lottery / draw / category quota | **Out of scope** for this RFP baseline |
| Eligibility / income quota engine | **Not required** in baseline |

### 2.3 Guiding Principles

1. Single platform for project, inventory, application, payment, and handover.  
2. Same business workflow for online and officer-entered applications.  
3. Booking confirmed only after successful online payment of booking amount.  
4. Configurable multi-level approvals without application code change.  
5. Sale deed draft generated in-system; registration completed **offline**, then recorded in BHMS.  
6. Documents and approvals embedded with each business record.  

---

## 3. Project Objectives

1. Digitize end-to-end management of BDA Flats and Villas.  
2. Provide a transparent first-come booking and allotment process.  
3. Enable citizens to discover, apply, pay online, and track status.  
4. Enable BDA sections (Engineering, Accounts, Registration, Possession, Administration) to operate on one system of record.  
5. Enforce payment timelines, auto-cancellation, and refund policy as configurable business rules.  
6. Generate allotment letter, draft sale deed, possession letter, and related artefacts from templates.  
7. Support bank/loan NOC requests with approvals and issued NOC documents.  
8. Deliver dashboards, MIS, notifications, and non-editable audit trails.  
9. Improve operational efficiency, accountability, and citizen service.  

---

## 4. In Scope / Out of Scope

### 4.1 In Scope

- Responsive web application for BDA officers and administrators.  
- Citizen self-service portal.  
- User, role, permission, and configurable multi-level approval setup.  
- Configurable masters (layout, project, property attributes, charges, templates, parameters).  
- Housing project lifecycle with publish control.  
- Flats & Villas inventory, pricing, documents, and status lifecycle.  
- Housing notification publish / extend / modify / withdraw.  
- Citizen registration with OTP-verified mobile.  
- Online applications and officer-assisted offline data entry of applications.  
- First-come booking with exclusive reservation of a unit.  
- **Online payments** (booking, balance, and applicable charges) via payment gateway.  
- Allotment letter management.  
- Draft sale deed generation, review, revision, and approval in system.  
- Offline registration capture (registration particulars + upload of registered sale deed).  
- Possession letter and handover recording.  
- Cancellation, refund calculation/processing, and automatic cancellation for non-payment.  
- Bank / loan NOC request, scrutiny, approval, and NOC issuance.  
- Embedded document management for projects, units, applicants, and transactions.  
- SMS, email, and in-app/portal notifications.  
- Management, Engineering, Accounts, and Citizen dashboards; PDF/Excel reports.  
- Process history and audit trail.  
- Data migration support for agreed legacy extracts (templates, validation, reconciliation).  
- Training, UAT support, go-live support, warranty, and documentation.  

### 4.2 Out of Scope (unless added by change request)

- Lottery / draw / randomisation engine for allotment.  
- Category quota / income-eligibility determination engine (not required in baseline).  
- Online integration with Sub-Registrar / Kaveri for deed registration (registration is offline; BHMS records outcomes).  
- Full GIS / GeoServer spatial platform (layout may be selected from master data; map pin optional if provided).  
- Full court-case / litigation CMS beyond status flags and linked documents where needed.  
- Native iOS/Android apps (responsive web is mandatory; native apps optional/separate).  
- Hardware procurement; physical scanning of paper archives (BDA responsibility).  
- Full ERP / general ledger replacement (hooks only if later required).  

---

## 5. Solution Expectations

| Area | Expectation |
|---|---|
| Access channels | Secure BDA officer portal + citizen portal |
| Usability | Role-based screens; mobile-responsive for citizen and field reference |
| Booking integrity | One active booking per unit; prevent double booking |
| Payments | Online payment gateway for citizen payments; reconciliation visibility for Accounts |
| Workflow | Configurable multi-level approvals by process type |
| Documents | Upload, generate, version/replace, and retrieve within each process |
| Language | English mandatory at go-live; bilingual-ready (English + Kannada) preferred |
| Hosting | As specified in RFP (government-approved cloud / on-premises / hybrid) |
| Auditability | Complete history of create/edit/approve/pay/cancel/NOC actions |

---

## 6. Consolidated Functional Modules

The solution shall be delivered as **ten consolidated modules**.  
Document attachment/retrieval and approval workflow steps are **embedded** inside Modules 2–9 as applicable.

---

### Module 1: Master Data & System Configuration

**Purpose:** Provide configurable masters, users/roles, templates, system parameters, and approval workflow configuration used across BHMS.

#### 1.1 Functional Requirements

**A. Location & Housing Masters**

- Layout Master, Housing Project Type, Property Type (Flat/Villa), Tower, Floor, Block, BHK Type, Facing, Amenities.  
- Document types, Charges Master, Payment-related lookup masters.  
- Notification templates and system parameters (including configurable payment timelines and refund deduction %).  

**B. User, Role & Workflow Configuration**

- Create/manage users; activate/deactivate; reset passwords; assign roles/permissions.  
- Map users to approval levels.  
- Configure multi-level approval processes per module/process (any number of levels; rearrange; map one or more users per level) without code change.  
- Approver actions: Approve, Reject, Send Back, Hold, Reassign, Delegate, Request Clarification — with user, level, date/time, remarks, status.  

#### 1.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M1-AC1 | Administrators can maintain listed masters without code change. |
| M1-AC2 | Approval hierarchies can be created and changed per process type without redeployment. |
| M1-AC3 | Role permissions restrict screens and actions as configured. |
| M1-AC4 | Payment due days and refund deduction % are configurable parameters. |

---

### Module 2: Housing Project Management

**Purpose:** Create, approve, publish, and maintain BDA housing projects.

#### 2.1 Functional Requirements

- Capture project name, code, type, location, layout, phase, zone, description.  
- Towers / villas / flats counts, amenities, images, brochure, booking window dates, expected completion, status.  
- Upload photographs, brochures, layout plans, and supporting documents (embedded).  
- Project create/major change follows configured approval before publish.  
- Only approved/published projects are visible on the Citizen Portal.  
- Full history of creation, modification, approval, and publication.  

#### 2.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M2-AC1 | Unpublished projects are not visible to citizens. |
| M2-AC2 | Project publication requires successful configured approval. |
| M2-AC3 | Project documents are retrievable from the project record. |

---

### Module 3: Flats & Villas Inventory and Status

**Purpose:** Maintain unit inventory and lifecycle status for every Flat and Villa.

#### 3.1 Functional Requirements

**A. Unit Register**

- Unit number, property type, tower/block/floor, BHK, facing, unit status.  
- Areas (super built-up, carpet, balcony; plot area for villas), parking, floor plan, description, construction status.  
- Financials: base price, booking amount, GST, registration charges, maintenance and other charges, total cost.  
- Unit documents: floor plan, images, drawings, brochure, supporting files.  
- Modifications before publish allowed to Engineering; after publish, changes follow approval where configured.  

**B. Status Lifecycle (indicative)**

Draft, Under Approval, Approved, Available for Booking, Booked, Payment Pending, Fully Paid, Allotment Letter Issued, Draft Sale Deed Generated, Registration Completed, Possession Issued, Cancelled, Refunded, Vacant / Available.

- Status updates shall follow business events automatically where defined.  
- On cancellation (manual or auto), unit returns to available inventory.  

#### 3.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M3-AC1 | Every unit is uniquely identifiable under a project. |
| M3-AC2 | A booked unit cannot be booked by another applicant while booking is active. |
| M3-AC3 | Status reflects the latest completed business event. |

---

### Module 4: Housing Notification Management

**Purpose:** Publish booking notifications for approved projects.

#### 4.1 Functional Requirements

- Notification content: project details, available units summary, prices, booking amount, documents required, booking window, payment schedule, cancellation/refund policy, terms.  
- Only active notifications shown to citizens.  
- Extend, modify, or withdraw before booking end (with controls/approvals as configured).  

#### 4.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M4-AC1 | Citizens see only active notifications for published projects. |
| M4-AC2 | Withdrawal/extension is auditable and updates citizen visibility. |

---

### Module 5: Citizen Registration & Portal Services

**Purpose:** Citizen identity, profile, and self-service portal capabilities.

#### 5.1 Functional Requirements

- Registration: name, DOB, gender, Aadhaar, PAN, mobile, email, address, photograph, signature.  
- Mobile OTP verification before registration completion.  
- Login; update profile; change password; view own applications, payments, downloads, notifications.  
- Portal discovery: view projects, search/filter units (location, project, BHK, area, price, availability), photos/floor plans, brochure download, compare units.  
- Submit application, upload documents, pay online, track status, download allotment/sale deed drafts/registered deed (when uploaded)/possession letter/receipts.  
- Citizen sees **only** their own data.  

#### 5.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M5-AC1 | Registration cannot complete without successful mobile OTP. |
| M5-AC2 | Citizen cannot view another citizen’s applications or documents. |
| M5-AC3 | Search/filter returns only published available inventory as configured. |

---

### Module 6: Application & First-Come Booking

**Purpose:** Capture applications (online/officer-assisted) and confirm first-come bookings after payment.

#### 6.1 Functional Requirements

**A. Online Application**

- Select project and unit; view details; upload required documents; accept T&Cs; pay booking amount online; submit.  
- System generates Application Number and acknowledgement.  

**B. Officer-Assisted (Offline Entry) Application**

- Register/select applicant; enter application; upload scanned documents; initiate/link **online** payment for booking amount; submit into the same workflow.  

**C. Booking**

- After verification and successful booking-amount payment, reserve unit, set status Booked, block others, generate booking confirmation and receipt, notify via SMS/email/portal.  
- Booking details: booking number/date, applicant, property, amounts, due date, status.  
- Booking remains active until due date, completion, or cancellation.  

#### 6.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M6-AC1 | Online and officer-entered applications follow the same approval/processing path. |
| M6-AC2 | Booking is confirmed only after successful online booking-amount payment. |
| M6-AC3 | Concurrent booking attempts on the same unit allow only one success. |

---

### Module 7: Online Payment Management

**Purpose:** Collect and track all housing-related payments online.

#### 7.1 Functional Requirements

- Payment heads: booking amount, balance payment, registration charges, GST, maintenance, other applicable charges.  
- Default rule: balance payment due within **90 days** of booking (configurable).  
- Online gateway methods as enabled (e.g. UPI, net banking, cards, NEFT/RTGS where gateway supports).  
- Display total cost, paid, balance, age, due date, status.  
- Automatic reminders before due dates.  
- Payment verification, receipts, history, and Accounts visibility.  
- **Baseline payment channel: online only** (no cash/DD as system payment modes in baseline).  

#### 7.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M7-AC1 | Successful gateway payment updates ledgers and property/payment status. |
| M7-AC2 | Failed/pending gateway payments do not confirm booking. |
| M7-AC3 | Citizens and Accounts can view reconciled payment history for a booking. |

---

### Module 8: Allotment, Sale Deed, Registration & Possession

**Purpose:** Post-booking formalities through possession.

#### 8.1 Functional Requirements

**A. Allotment Letter**

- Generate after successful booking and required approvals.  
- Contents: allotment number/date, applicant, project/unit details, costs, amounts, due date, T&Cs, cancellation policy, signatory.  
- Citizen download; officer regenerate/reissue with history.  

**B. Draft Sale Deed**

- Generate after full payment.  
- Contents: deed number, parties, project/unit, measurements, consideration, payment details, schedule, T&Cs.  
- Review/revise before approval; version history; approved draft is the document package for offline registration.  

**C. Registration (Offline execution, system recording)**

- After draft approval, registration is completed **outside** the system (Sub-Registrar).  
- Registration Section records: registration number/date, document/book numbers, SRO, stamp duty, registration charges.  
- Upload registered sale deed; citizen download; status → Registration Completed.  

**D. Possession**

- After registration recorded, generate Possession Letter; verify full payment, registration, documents, readiness.  
- Issue letter; capture acknowledgement; status → Possession Issued; retain history.  

#### 8.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M8-AC1 | Allotment letter cannot be issued without confirmed booking and required approvals. |
| M8-AC2 | Draft sale deed generates only after full payment. |
| M8-AC3 | Possession cannot be issued unless registration details and registered deed upload are present (as configured). |
| M8-AC4 | Draft sale deed version history is retained. |

---

### Module 9: Cancellation, Refund & Auto-Cancellation

**Purpose:** Handle voluntary cancellation, refunds, and non-payment auto-cancellation.

#### 9.1 Functional Requirements

- Applicant may request cancellation before sale deed execution; workflow approval required.  
- On approval: cancel booking, free unit, retain history and reason.  
- Refund initiation after approval; deduction default **10% of booking amount (configurable)**; remaining eligible amount refunded; track request/amounts/dates/status; citizen status view.  
- If balance payment not completed within **130 days** of booking (configurable), auto-cancel: free unit, reason Auto Cancellation – Non-payment, notify citizen, update history — no manual step required.  

#### 9.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M9-AC1 | Approved cancellation returns unit to available inventory. |
| M9-AC2 | Refund amount applies configured deduction percentage. |
| M9-AC3 | Auto-cancellation runs when configured non-payment threshold is crossed. |

---

### Module 10: Bank / Loan NOC Management

**Purpose:** Process NOC requests for bank/housing loan against allotted/booked properties.

#### 10.1 Functional Requirements

- Citizen and/or officer can raise NOC request linked to booking/allotment.  
- Capture bank name, loan reference (as applicable), applicant and property particulars, supporting documents.  
- Scrutiny and multi-level approval.  
- Generate Bank/Loan NOC from template; issue/download; status tracking.  
- Maintain history of NOC requests, reissues, and cancellations/withdrawals as configured.  

#### 10.2 Acceptance Criteria

| ID | Criterion |
|---|---|
| M10-AC1 | NOC cannot be issued without required booking/allotment linkage and approvals. |
| M10-AC2 | Issued NOC is downloadable by authorized citizen and officers. |
| M10-AC3 | Full NOC process history is retained. |

---

### Cross-cutting capabilities (embedded / included above)

The following are delivered as embedded capabilities rather than separate bid modules:

| Capability | Where covered |
|---|---|
| Document Management | Modules 2–10 |
| Configurable Approvals runtime | Modules 2–10 using Module 1 configuration |
| SMS / Email / Portal notifications | Event-driven across processes (see Section 10) |
| Dashboards & Reports | Section 6 complementary requirements below |
| Search | Global/advanced search across projects, units, bookings, applicants, deeds |
| Process History & Audit | Sections 11–12 |

#### Dashboards (required)

- **Management:** projects, flats/villas, available/booked/sold/vacant, cancellations, registrations pending, possessions, revenue collected/pending, refunds, auto-cancellations, project-wise and area-wise sales, monthly collection.  
- **Engineering:** projects under development/pending/approved, inventory readiness, construction progress indicators as captured.  
- **Accounts:** booking/balance collections, pending payments, refunds pending/completed, daily/monthly collection, revenue summary.  
- **Citizen:** my applications, booking/payment status, balance, allotment/deed/possession artefacts, notifications, downloads.  

#### Reports (PDF/Excel, filterable)

Project, inventory, booking, payment, financial (revenue/refund/cancellation/outstanding), registration/possession registers, citizen application (online/offline), administrative (activity, workflow pendency, audit).

---

## 7. End-to-End Workflows

### 7.1 Core Housing Allotment Flow (First-Come)

```text
Housing Project Created → Project Approved → Housing Notification Published
→ Citizen Registration → Online / Officer-Entered Application
→ Online Booking Amount Payment → Booking Confirmation
→ Allotment Letter → Balance Payment (within configured days)
→ Draft Sale Deed → Offline Registration (record + upload)
→ Possession Letter → Handover
```

### 7.2 Non-Payment Path

```text
Booking → Payment Reminders → (No full payment by configured day)
→ Auto Cancellation → Unit Available → Notifications
```

### 7.3 Voluntary Cancellation & Refund

```text
Cancellation Request → Approval → Booking Cancelled → Unit Available
→ Refund Calculation (configurable deduction) → Refund Processing → Closed
```

### 7.4 Bank / Loan NOC

```text
NOC Request → Document Scrutiny → Multi-level Approval → NOC Issued → Download / Archive
```

---

## 8. Role-Based Access Control

### 8.1 Indicative Roles

| Role | Typical Access |
|---|---|
| Super Administrator | Users, masters, workflows, parameters |
| Commissioner / Senior Authority | Executive dashboards; high-level approvals |
| Engineering Section | Projects, inventory, technical documents |
| Accounts Section | Payments, refunds, revenue dashboards |
| Registration Section | Registration capture and registered deed upload |
| Possession Section | Possession verification and handover |
| Housing / Estate Officer | Applications, booking ops, allotment follow-up |
| NOC Desk | Bank/loan NOC processing |
| Auditor | Read-only registers, approvals, audit |
| Data Entry Operator | Restricted create/update as assigned |
| Citizen | Own portal data and transactions only |

### 8.2 Access Principles

- Least privilege; module + action controls.  
- Segregation of duties for propose vs approve.  
- Citizens restricted to own records.  
- Privileged actions logged.  

Vendors shall provide a role–permission matrix for BDA sign-off during design.

---

## 9. Channels – Officer Portal & Citizen Portal

### 9.1 Officer Portal

Full operational access by role for masters, projects, inventory, notifications, applications, bookings, payments, allotment/deed/registration/possession, cancellation/refund, NOC, dashboards, and reports.

### 9.2 Citizen Portal

Published projects/units, application, online payment, status tracking, downloads, NOC request (where enabled), and personal notifications — only for the logged-in citizen.

---

## 10. Integrations

| Integration | Priority | Notes |
|---|---|---|
| Payment Gateway | Mandatory | Online booking, balance, and charge payments |
| SMS Gateway | Mandatory | OTP, booking, payment, cancellation, NOC alerts |
| Email Service | Mandatory | Acknowledgements and notices |
| DigiLocker / Aadhaar eKYC | Optional | Subject to BDA/legal approval |
| Sub-Registrar / Kaveri e-registration | Out of baseline | Offline registration; system records results |

---

## 11. Audit, Compliance & Security

The system shall maintain:

- Complete process history (user, time, action, previous/current status, remarks, documents) for projects, units, applications, bookings, payments, refunds, cancellations, letters, deeds, registrations, possession, and NOC.  
- Non-editable audit trail: login/logout, activity, data changes, approvals, status changes, uploads, report downloads, configuration changes.  

Security expectations:

- Secure login; OTP for citizens; password policy; session timeout  
- RBAC; secure document storage; HTTPS  
- Encryption of sensitive information as applicable  
- Backup and recovery  

---

## 12. Non-Functional Requirements

| Area | Requirement |
|---|---|
| UI | Responsive web for officer and citizen channels |
| Language | English mandatory; bilingual-ready preferred |
| Performance | Key pages within agreed time under agreed load |
| Availability | Target ≥ 99.5% monthly (final SLA in contract) |
| Backup | Daily backups; periodic restore drills |
| Scalability | Growth in projects, units, applications, payments, documents |
| Compatibility | Chrome, Edge, Firefox (latest two major versions) |
| Export | PDF / Excel for registers and reports |
| Concurrency | Safe handling of concurrent booking attempts on the same unit |

---

## 13. Data Migration

Legacy data migration support is in scope where BDA provides extracts.

- Templates and validation for projects, units, and (where available) bookings/applicants.  
- Trial load, reconciliation, exception register, final cutover support.  
- Document bulk linking when digital files are supplied.  
- Physical scanning remains BDA responsibility.  

---

## 14. Phased Delivery

### Phase 1 – Production Go-Live (Mandatory)

- Modules 1–10 (including online payments, first-come booking, sale deed draft, offline registration recording, possession, cancellation/refund/auto-cancel, bank/loan NOC)  
- Officer and citizen portals  
- SMS/email notifications  
- Dashboards and core reports  
- Migration of agreed datasets  
- Training, UAT, go-live, hypercare  

### Phase 2 – Optional Enhancements

- DigiLocker / Aadhaar eKYC  
- Kannada UI completion (if not fully delivered in Phase 1)  
- Native mobile apps (optional)  
- Future Sub-Registrar online integration (if later mandated)  

---

## 15. Deliverables

| # | Deliverable |
|---|---|
| 1 | Project plan, RAID log, weekly status |
| 2 | Requirements Specification & Gap Analysis (against this SOW) |
| 3 | Solution design (functional, security, integration approach) |
| 4 | UI/UX prototypes for key officer and citizen journeys |
| 5 | Configured application (Phase 1 scope) |
| 6 | Mandatory integrations (payment, SMS, email) |
| 7 | Migration templates, trial/final load, reconciliation report |
| 8 | Test plans, UAT support, UAT sign-off pack |
| 9 | Training and user manuals (officer + citizen) |
| 10 | Administration and operations documentation |
| 11 | Go-live support & hypercare |
| 12 | Source code / escrow as per contract |
| 13 | Warranty and AMC proposal |

---

## 16. Acceptance Criteria (Program Level)

1. Phase 1 modules meet module acceptance criteria in Section 6.  
2. First-come booking prevents double allocation of the same active unit.  
3. Online payment confirms booking only on success; Accounts can reconcile.  
4. Draft sale deed generates after full payment; registration offline path records SRO details and registered deed upload.  
5. Auto-cancellation and refund deduction honour configured parameters.  
6. Bank/loan NOC can be requested, approved, issued, and downloaded.  
7. Citizen portal enforces ownership isolation.  
8. UAT signed off with no open Critical/High defects.  
9. Training completed for nominated users.  
10. Security checklist (auth, RBAC, audit, backup restore) signed off.  

---

## 17. Expected Benefits

- Single digital system for BDA housing stock and allotment lifecycle  
- Transparent first-come booking with reduced disputes over double booking  
- Faster citizen service through online apply/pay/track/download  
- Configurable approvals with full accountability  
- Controlled sale deed drafting and possession readiness checks  
- Structured bank/loan NOC processing  
- Better revenue and refund visibility for Accounts and management  
- Complete auditability for statutory and internal review  

---

## 18. Assumptions & Dependencies

1. BDA will nominate a nodal officer and section SMEs for timely rule/workflow decisions.  
2. Payment gateway, SMS, and email credentials/approvals will be facilitated by BDA.  
3. Baseline allotment model is first-come-first-served; lottery/quota engines are excluded.  
4. Eligibility/income category engines are not required in baseline.  
5. Sale deed registration is offline; BHMS generates draft and records post-registration artefacts.  
6. Offline application entry remains supported; payment confirmation is via online gateway.  
7. Digitization of paper files is BDA’s responsibility.  
8. Hosting and security clearances follow the RFP/contract.  
9. Default timelines (90-day balance; 130-day auto-cancel; 10% refund deduction) are starting parameters and remain configurable.  

---

## 19. Vendor Response Expectations

RFP responses shall include at minimum:

1. Understanding of this SOW and module mapping.  
2. Functional compliance matrix against Section 6.  
3. Approach for concurrent booking integrity and online payment reconciliation.  
4. Approach for draft sale deed templates and offline registration recording.  
5. Bank/loan NOC process design aligned to this SOW.  
6. Data migration approach and cutover plan.  
7. Implementation methodology, timeline, and team profiles.  
8. Commercial proposal for Phase 1 and optional Phase 2 items.  
9. Relevant government / housing / allotment case studies.  
10. Assumptions, exclusions, dependencies, and AMC/SLA model.  

---

## Appendix A – Module Consolidation Map

| Consolidated Module | Baseline Topics Included |
|---|---|
| 1. Master Data & System Configuration | Masters; users/roles; approval configuration; parameters |
| 2. Housing Project Management | Project lifecycle + project documents + publish approval |
| 3. Flats & Villas Inventory and Status | Unit register, pricing, documents, status automation |
| 4. Housing Notification Management | Public booking notification lifecycle |
| 5. Citizen Registration & Portal Services | Registration, OTP, citizen self-service |
| 6. Application & First-Come Booking | Online/offline entry applications; booking confirmation |
| 7. Online Payment Management | Gateway payments, reminders, receipts, ledgers |
| 8. Allotment, Sale Deed, Registration & Possession | Letters, draft deed, offline registration record, possession |
| 9. Cancellation, Refund & Auto-Cancellation | Voluntary cancel, refund, auto-cancel |
| 10. Bank / Loan NOC Management | NOC request through issuance |

**Not separate modules:** Document Management; Workflow Engine; standalone Notification product (event notifications included across processes).

---

## Appendix B – Indicative Data Entities

Project, Flat/Villa Unit, Housing Notification, Citizen, Application, Booking, Payment, Allotment Letter, Draft Sale Deed, Registration Record, Possession Letter, Cancellation, Refund, Bank/Loan NOC, Document, Approval Instance, Notification Log, User, Role, Audit Log.

---

## Appendix C – Key Configurable Business Parameters (Baseline Defaults)

| Parameter | Baseline default | Notes |
|---|---|---|
| Balance payment period | 90 days from booking | Configurable |
| Auto-cancellation for non-payment | 130 days from booking | Configurable |
| Refund deduction on voluntary cancel | 10% of booking amount | Configurable |
| Booking model | First-come-first-served | Fixed for baseline |
| Payment channel | Online gateway | Fixed for baseline |

---

*This SOW provides the RFP foundation for a full-scale BDA Housing Management System covering project and inventory publication, first-come booking, online payments, allotment and sale-deed drafting, offline registration recording, possession, cancellation/refund, bank/loan NOC, citizen and officer channels, and executive reporting.*

**End of Document**
