# Statement of Work (SOW)

# Karnataka Building and Other Construction Workers Welfare Board (KBOCWWB)

# Labour CESS Tracking & Monitoring System

**Document Type:** Statement of Work – Business Requirements  
**Version:** 1.0  
**Status:** Draft  
**Source:** Request for Proposal No. KBOCWWB/2026-27/SE0157 dated 29-06-2026  
**Prepared for:** Joint Secretary, Karnataka Building and Other Construction Workers Welfare Board, Bengaluru  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control](#8-access-control)
9. [Channels](#9-channels)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria](#16-acceptance-criteria)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)
20. [Appendix A — Module & Feature Index](#20-appendix-a--module--feature-index)
21. [Appendix B — Mapping to RFP Software Modules](#21-appendix-b--mapping-to-rfp-software-modules)
22. [Appendix C — CESS Collection Agency Groups](#22-appendix-c--cess-collection-agency-groups)
23. [Appendix D — Key Entities](#23-appendix-d--key-entities)
24. [Appendix E — Named KSK Integration Operations](#24-appendix-e--named-ksk-integration-operations)

---

## 1. Introduction

This Statement of Work states the **business requirements** for **Design, Development, Implementation, Operation and Maintenance** of a **Labour CESS Tracking & Monitoring System** for the **Karnataka Building and Other Construction Workers Welfare Board (KBOCWWB)**, Labour Department, Government of Karnataka.

The Board is mandated to collect **1% labour cess** on building and other construction activities under the Building and Other Construction Workers’ Welfare Cess Act, 1996 and the Rules of 1998. Cess deducted by government undertakings, Urban Local Bodies and other agencies must be remitted to the Board **within 30 days**. Those funds support welfare of registered construction workers.

The RFP requires a **custom-built** application (not a licensed or COTS product). The **software, latest source code and cess/project data** shall be **owned by KBOCWWB**. The application shall be **hosted at the Karnataka State Data Centre (KSDC / SDC)** with a disaster-recovery site.

**Document handling** (scan, OCR search, digital files) and **workflow** (inward, e-office inbox, approvals, notices, appeals) are **in scope as business capabilities**. They are grouped for implementation under one correspondence module in this SOW; they remain the same scope as RFP Modules 4, 5 and 6.

This document is prepared for RFP discussion and internal estimation. It does not prescribe technology stack, interface contracts, database design, or screen layouts.

---

## 2. Project Overview

KBOCWWB estimates that only about **30–40% of eligible cess** is collected today. Causes stated in the RFP include: no reliable demand assessment; stakeholders using their own systems (some digital, some manual); weak information sharing; delayed and lump-sum remittances without project-wise breakup; unmonitored construction especially in peri-urban and rural areas; and non-standard submission formats. The Board often learns of fund status only through AG or other audit.

The solution shall automate the **full lifecycle of cess**: project registration, cess calculation (1% of eligible cost), assessment in the field, demand and notice, collection and remittance (including **LCDRS — Labour Cess Deductions / Collection and Remittance at Source**), reconciliation, appeal and grievance, and compliance follow-up when remittance exceeds 30 days.

Stakeholders include:

| Stakeholder | Role in this system |
| ----------- | ------------------- |
| Labour Department | Oversight, coordination for data sharing, enforcement policy |
| KBOCWWB | Fund management, business rules, compliance, approvals for agency integrations, awareness of CESS API self-service |
| CESS collection agencies | Project data, deduction at source, automated exchange via connectors **or** periodic update on the Labour Cess Portal |
| Implementing agency | Design, build, integrate (including Karmika Seva Kendra and listed agencies), operate connectors, technical support |

### 2.1 Business Context

| Aspect | Description |
| ------ | ----------- |
| Organisation | Karnataka Building and Other Construction Workers Welfare Board (KBOCWWB) |
| Legal basis | BOCW Act 1996; Cess Act 1996; Cess Rules 1998; 1% cess; remittance within 30 days |
| Existing platform | KBOCWWB **Karmika Seva Kendra (KSK)** — this project **integrates** with KSK; it does not replace KSK welfare functions |
| Hosting | Karnataka State Data Centre with DR |
| Selection | Quality- and Cost-Based Selection (QCBS), 75% technical / 25% financial |
| Indicative project value (RFP) | Rs. 1505 lakh including GST |
| Development window (performance security) | 9 months software development, then 24 months AMC |

### 2.2 Guiding Principles

1. One **central cess system of record** for demand, collection, remittance and outstanding dues.
2. **Real-time or periodic** intelligence from e-procurement, building-plan, treasury and other agency systems; **manual capture** where the agency has no IT system.
3. **Compel timely demand** and follow up remittance beyond 30 days with alerts and escalation.
4. **Project-wise, department-wise and region-wise** tracking — not lump-sum only.
5. **Custom-built** application owned by the Board; no product licence lock-in.
6. **Plug-and-play connectors** so listed collection agencies can onboard without a unique build per agency.
7. Access follows **organisation, designation, territory and assigned work** — not a two-role toy model.

---

## 3. Project Objectives

1. Register construction projects and compute **1% cess** from tender, permit and departmental data (and from field assessment where needed).
2. Give KBOCWWB a **single view** of deducted vs remitted cess, outstanding dues and leakage.
3. Enable **LCDRS** so collection at cash counter (and equivalent channels) remits to the Board’s cess account with project and demand detail.
4. Let Labour Inspectors **assess on site** (web and GPS-enabled mobile), calculate cess for new work and partial violation, and issue **demand notices on the spot**.
5. Provide a **Labour Cess Portal** for government departments and private agencies: login, demand update, payment/remittance, DCB, appeal, grievance and notices.
6. Integrate with **KSK** for builder/contractor profile, officer lists (ALC/LO), officer review and **online payment collection through the Board’s payment interface**.
7. Provide a **CESS API / Connector Self-Service Portal** for Annexure A and B agencies (REST and SOAP as needed).
8. Support **audit-ready** reconciliation, CAG/AG reports, interest-loss on delay, and encrypted sharing for treasury/audit.
9. Host at **KSDC** with DR, security audit support, training and two years of AMC after the stated integration milestone.

---

## 4. In Scope / Out of Scope

### In Scope

- Custom web application, inspector/staff mobile application, and GIS analytical views covering the modules in Section 6.
- Super-administration: territory and organisation masters, RBAC, logs, backups, version logs, middleware control.
- Construction **project (infra) registry** and cess masters (categories, departments, private agencies, building and project types).
- Digital inward/outward, document repository (scan, OCR search), and e-office style inbox processing of files, linked to cess and appeal work.
- GPS-enabled field assessment, survey calculation, on-the-spot demand notice (print and email soft copy).
- Labour Cess Portal for government and private agencies, including two-factor login, cash counter and multi-mode collection, LCDRS, scheduled demand update, self DCB, remittance to Board bank/treasury, grievance and appeal.
- Accounts: DCB, notices/reminders, reconciliation of collections and refunds, interest-loss on delayed remittance.
- Meetings (internal and with external agencies), minutes, task delegation.
- Alerts, notification templates, event and periodic reminders, escalation matrix.
- Smart middleware: KSK; e-procurement; building-plan / town-planning (including NIRMANA and similar); Khajane 2.0 / treasury; GST; other state/central/department systems as facilitated by the Board; data pool for analytics.
- CESS API / Connector Self-Service Portal (pre-configured connectors, onboarding, health, versioning, sandbox, REST and SOAP, audit, Board approval of access).
- GIS layers, line segments, polygons and superimposition for buildings and projects.
- MIS, KPI and predictive decision-support reports (not a separate licensed BI product requirement).
- SRS, design, development, deployment at KSDC, security-audit support, train-the-trainer capacity building, helpdesk during implementation, source-code handover, and **24 months AMC** as in the RFP.
- Manual data entry path for agencies **without** IT systems.

### Out of Scope

- Replacement or rewrite of **Karmika Seva Kendra** welfare-scheme, worker-registration or benefit-disbursement functions (integration only).
- **Command and control centre** integration (RFP: future enhancement).
- Licensed COTS cess product or per-user software licence model.
- Construction of KSDC halls, racks or Board office civil works.
- Unique custom connector **codebase per agency** where a standardised connector template applies (agencies onboard through the self-service portal).
- Legal drafting of Government Orders that mandate departmental reporting (Board / Labour Department action; the software shall support mandated reporting once issued).
- Procurement of satellite imagery (RFP risk note: Board/client facilitation if used).
- Citizen generic grievance portal unrelated to cess, or public social-media channels.
- Detailed technical architecture, interface contracts, database schemas, class diagrams and UI wireframes (design stage after award).

---

## 5. Solution Expectations

- The Board and Labour Department work primarily in the **back-office**. Collection agencies and private payers work on the **Labour Cess Portal** and/or **connectors**.
- Inspectors work **in the field on mobile** with GPS-stamped photo/video and can issue demand on the spot.
- Cess is **1%** of the applicable construction cost, including **partial violation** against sanctioned estimates where the RFP requires it.
- Remittance clock is **30 days** from deduction; the system tracks, reminds and escalates.
- Online cess **payment collection** for Board accounting is through the **KSK / Board payment interface** named in the RFP — not a parallel ungoverned gateway.
- Agencies that cannot integrate still **create a portal account** and update records on the schedule the Board defines.
- Predictive analytics support demand assessment and leakage detection; they do not replace statutory demand.
- Language of the RFP deliverables is **English**; operational labels should remain usable by field officers.

---

## 6. Consolidated Functional Modules

RFP software modules 1–17 are retained in full as scope. They are **grouped** below for implementation and later estimation. Appendix B maps each RFP module to this structure.

### 01. User, Role and Organisation Governance

**Purpose:** Give KBOCWWB a super-administrator function to hold organisation, designation and user structure and to control who may do what.

**Type:** Shared

**Functional requirements:**

- Maintain main masters needed for territory linkage and organisation structure (detailed territory GIS is Module 02).
- Create and maintain **role-based access**, user privileges, and mapping of **department, territory, designation and user**.
- Create staff/user profiles; map services, sub-services and **stage-wise actions**.
- Control smart-middleware access at an operational level (who may approve a connector or integration).
- Retain operational logs, system logs, version logs and database-backup administration.

**Acceptance criteria:**

- A user without a role and mapping cannot reach back-office functions.
- Privilege changes take effect on subsequent sessions and are logged.
- Super-administrator can produce operational, system and version logs for a chosen period.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Super Administrator and System Configuration | Create and maintain foundation masters and system settings used across the cess application. |
| F01-002 | Role-Based Access and Privileges | Define roles, privileges and service/stage action mapping for Board and departmental users. |
| F01-003 | Organisation Structure and User Mapping | Departments, sub-departments, hierarchical designations, user profiles, and department–territory–designation–user mapping. |
| F01-004 | Logs, Version History and Backup Administration | Operational logs, system logs, version logs and database backup administration for Board operations. |

---

### 02. Territory and GIS Foundation

**Purpose:** Represent Karnataka administrative geography for MIS, GIS and assignment of work.

**Type:** Shared

**Functional requirements:**

- Create territories with required details.
- Maintain **hierarchical mapping** of territories (state / division / district / taluk / ULB / other levels used by the Board).
- Support MIS and GIS use of the same territory master (plotting of projects is Module 13).

**Acceptance criteria:**

- Every assessable location used in assessment or DCB can be tied to a territory in the hierarchy.
- Territory changes do not orphan historical project records (history remains attributable).

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Territory Master and Hierarchy | Create and maintain territories and parent–child hierarchy for cess administration. |
| F02-002 | Territory for MIS and GIS | Expose territory structure to dashboards and GIS so projects and assessments plot in the correct geography. |

---

### 03. Labour Cess Masters and Project Registry

**Purpose:** Hold cess reference data and the **infra registry** of construction projects from which demand is derived.

**Type:** Business

**Functional requirements:**

- Maintain labour cess category and labour cess master.
- Maintain government department master and private agency master.
- Maintain building categories and project categories.
- Register **all new construction projects** department-wise: name, location, type, estimated cost, developer/contractor, timelines and other details needed to compute and track cess.
- Use project inputs from integrations and from departmental entry (Module 11).

**Acceptance criteria:**

- A project cannot be saved without the minimum identity, location, cost and responsible agency fields the Board defines.
- Cess computation at 1% can be run from registered project cost (and from assessment where cost is revised).

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Cess, Building and Project Category Masters | Labour cess category, cess master, building categories and project categories. |
| F03-002 | Government Department and Private Agency Master | Masters of remitting departments and private agencies that collect or owe cess. |
| F03-003 | Construction Project Infra Registry | Department-wise registration of construction projects with cost, parties, location and timelines. |

---

### 04. Correspondence, Document Management and E-office

**Purpose:** Digitise inward/outward, store project and cess documents, and process files in an inbox — as required by RFP Modules 4, 5 and 6 — without treating them as a generic standalone product outside cess work.

**Type:** Shared

**Functional requirements:**

- Digital **inward acknowledgement**; auto-forward to the correct inbox using the **service mapping matrix**.
- Digital **outward acknowledgement**.
- Integration of inward with the Labour Cess Portal and the Appeal module.
- Scan letters, files and ledgers; **OCR search**; store against the file/project.
- E-office: inbox processing, comment section and document section, tied to territory and organisation.
- On defined actions, update cess data through middleware (automation, not a separate product).

**Acceptance criteria:**

- An inward item produces a digital acknowledgement and lands in the mapped officer inbox.
- A user can find a stored document by OCR/text search within authorised files.
- Appeal and portal submissions can be processed as files without re-keying the inward number.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Digital Inward and Outward | Acknowledgements, service-matrix auto-forward, and linkage to portal and appeal. |
| F04-002 | Document Repository, Scan and OCR Search | Scan/upload of letters, files and ledgers with searchable retrieval. |
| F04-003 | E-office Inbox and Digital File Processing | Inbox-based file processing with comments and documents, using organisation and territory. |
| F04-004 | Action-Triggered Cess Update | On configured file actions, update cess records through the integration layer. |

---

### 05. Field Assessment and Demand

**Purpose:** Let the Board **create assessment worklists** and let Labour Inspectors **survey, calculate cess and issue demand** in the field.

**Type:** Business

**Functional requirements:**

- Back-office creation of lists of buildings/projects to assess; district officers may self-create lists; state may impose lists.
- Mobile application for inspectors to fetch/update estimation details.
- **GPS-enabled** image and video capture with timestamp.
- Survey and calculation for **entire new construction** and **partial violation** against sanctioned estimates.
- Generate **demand notice on the spot** (print and email soft copy).
- Territory-wise tasks, notifications and real-time dashboards for assessment work.

**Acceptance criteria:**

- An inspector in the field can complete an assessment against an assigned item and store GPS media.
- Demand notice can be generated immediately after calculation, without a separate back-office wait, where policy allows.
- Partial-violation calculation is distinguishable from full-new-construction calculation.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Assessment Worklists | State-imposed and district self-created lists of buildings and projects to assess. |
| F05-002 | Inspector Mobile Assessment with GPS Media | Fetch/update estimates on mobile with GPS image/video and timestamp. |
| F05-003 | Cess Survey Calculation | Calculate cess for new construction and partial violation against sanctioned estimates. |
| F05-004 | On-the-Spot Demand Notice | Generate, print and email demand/assessment notice in the field. |

---

### 06. Labour Cess Portal, LCDRS and Collections

**Purpose:** Give government departments and private agencies a **secured portal** to see demand, collect/remit cess and stay aligned with Board books.

**Type:** Business

**Functional requirements:**

- Accounts for departments and private agencies are **created in back-office**; credentials sent to registered email; **two-factor authentication** on login.
- Content management for agency-facing information as required.
- **Cash counter** collecting cess by cash, debit/credit card, dynamic QR, net banking and other stated modes; **QR acknowledgement receipt**.
- **LCDRS:** remittance into the labour cess bank account **at the time of collection** through the cash-counter path, with accountability and project/demand detail.
- **Scheduled demand update** — mandatory periodic update of demand/collection.
- Push of MIS and GIS intelligence from back-office so agencies see leakage and related signals (for example unauthorised construction).
- Pay/remit collected cess to the Board (bank accounts and/or Treasury) against demand, with paying-stakeholder and periodic demand detail.
- Self **real-time DCB** and discrepancy/leakage information for the logged-in agency.
- View of assessment/demand notices issued against the agency.
- Alerts and notifications on the portal.

**Acceptance criteria:**

- An agency cannot use the portal until the Board has created the account and the user completes two-factor login.
- A cash-counter collection produces a QR acknowledgement and, under LCDRS, a remittance trail to the Board cess account with demand reference.
- Agency DCB matches Board-visible demand, collection and remittance for that account holder (within timing of posted transactions).

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Agency Portal Access and Two-Factor Login | Board-created agency accounts, email credentials, CMS access and two-factor login. |
| F06-002 | Cash Counter and Multi-Mode Collection | Collect cess by the stated modes and issue QR acknowledgement receipts. |
| F06-003 | LCDRS Remittance at Source | Remit to the Board cess account at collection, with project and demand detail. |
| F06-004 | Scheduled Demand Update | Mandatory periodic interface for agencies to update demand and collection. |
| F06-005 | Agency DCB, Notices and Intelligence | Self DCB, leakage/discrepancy view, assessment notices, and MIS/GIS intelligence pushed from back-office. |
| F06-006 | Remittance to Board Bank or Treasury | Transfer of collected cess to Board accounts or Treasury against demand. |

---

### 07. Appeals and Grievances

**Purpose:** Let cess payees **appeal** demand (including alleged discrimination and refunds) and **raise grievances**, and let the Board process them through inward and e-office.

**Type:** Business

**Functional requirements:**

- Portal: appeal for demand assessment, refunds and similar; grievance/complaints on cess matters; status visibility for the payee.
- Back-office: process appeals/grievances with inward and e-office.
- Staff mobile (as listed under RFP accounts/staff app): process appeal/grievance where the Board so configures.

**Acceptance criteria:**

- A portal user can file an appeal or grievance and see status without telephoning the Board.
- Every appeal/grievance has an inward trail and a processing file.
- Outcome (accept, reject, refund instruction) is visible to the applicant and to accounts.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Portal Appeal and Refund Request | Payee login to appeal demand assessment, refunds and related discrimination claims. |
| F07-002 | Grievance Registration and Tracking | Register and track cess-related complaints from the portal. |
| F07-003 | Back-office Appeal and Grievance Processing | Inward and e-office processing of appeals and grievances, including staff-mobile action where used. |

---

### 08. Accounts, DCB, Notices and Reconciliation

**Purpose:** Give Board accounts a **demand–collection–balance** picture, notices, reconciliation, refunds and **interest-loss** on delayed remittance.

**Type:** Business

**Functional requirements:**

- DCB reports; generate notices and reminders; reconcile cess collections and refunds.
- Automatic **interest-loss** calculation when remittance exceeds 30 days (RFP financial optimisation).
- Staff-exclusive mobile: territory/designation DCB dashboards, assessment actions already in Module 05, appeal processing, meetings, alerts, GPS updates — **accounts-facing DCB and notice actions** are in this module; overlapping channels are listed in Section 9 rather than duplicated as extra products.
- Audit-ready deducted vs remitted views for CAG/AG.

**Acceptance criteria:**

- Board accounts can produce DCB for a department, region and project for a chosen period.
- A remittance later than 30 days shows computed interest-loss using Board-supplied rates/rules.
- Notices/reminders can be generated from outstanding DCB and are logged.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Demand, Collection and Balance Registers | Project-, department- and region-wise DCB for Board staff. |
| F08-002 | Notices and Reminders | Generate statutory/operational notices and reminders for non-remittance and related dues. |
| F08-003 | Reconciliation of Collections and Refunds | Match deducted vs remitted cess and process refunds against appeals or corrections. |
| F08-004 | Interest Loss on Delayed Remittance | Calculate and report interest loss when remittance exceeds 30 days. |
| F08-005 | Staff Mobile DCB and Account Actions | Territory/designation real-time DCB and related account actions on the staff mobile application. |

---

### 09. Meetings and Task Tracking

**Purpose:** Plan and record **cess-related meetings** with department staff, other government departments and private agencies, and track resulting tasks.

**Type:** Business

**Functional requirements:**

- Create meetings, agendas; record minutes of physical meetings; delegate tasks; track tasks; integrate with alerts.

**Acceptance criteria:**

- A meeting record can hold agenda, attendees, minutes and delegated tasks.
- Overdue tasks raise alerts per Module 10 configuration.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Meetings, Agenda and Minutes | Create cess meetings (internal and external) and record minutes. |
| F09-002 | Task Delegation and Tracking | Assign, track and close tasks arising from meetings. |

---

### 10. Alerts, Notifications and Escalation

**Purpose:** Standardise **reminders and escalations** for delayed remittance, missed demand updates and other configured events.

**Type:** Shared

**Functional requirements:**

- Define message templates; periodic auto alerts; trigger-based alerts; track responses; **escalation matrix** if delay persists.
- Push to department staff, portal users, external departments and private agencies as configured.
- Digital correspondence/reminders to remitting agencies for non-payment beyond 30 days.

**Acceptance criteria:**

- Non-remittance beyond 30 days produces the configured reminder and, if still unpaid, the next escalation step.
- Each alert has a response/acknowledgement trail where the Board requires one.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | Templates, Periodic and Event Alerts | Configure templates, schedules and event triggers for cess alerts and notifications. |
| F10-002 | Escalation Matrix and Response Tracking | Escalate persistent delay and track responses to individual alerts. |

---

### 11. Integrations, Smart Middleware and KSK

**Purpose:** Exchange cess-relevant data with **KSK** and with **state, central and departmental systems**, and hold a **data pool** for analytics. Where a system cannot connect, provide **manual or semi-automated** capture.

**Type:** Technical

**Functional requirements:**

- Intra-integration with **Karmika Seva Kendra** as in Appendix E (profile sync, payment collection, officer review, ALC/LO dropdown alignment).
- Integrations named in the RFP: building-plan / town planning (state and local, **NIRMANA** cited), **Karnataka e-procurement**, **treasury / Khajane 2.0** and other financial applications, **GST**, and further state/central/department applications as the Board facilitates.
- Automated or semi-automated pull of permits, tenders, utility or other construction signals; **periodic updates**.
- Manual entry by the department when IT integration is not feasible.
- Data pool: mirror of integrated data for predictive reports.
- KBOCWWB facilitates departmental introductions and alternate sources (for example tender systems); the implementing agency performs technical integration.

**Acceptance criteria:**

- Builder/contractor cess registration can be pre-filled from KSK Aadhaar-verified profile where KSK returns data.
- Online payment of cess through the Board path posts into Board accounting as specified in the RFP payment milestone.
- An agency without an API can still submit project/cess data through portal or Board-assisted manual capture.
- Officer list used as Registering Officer in cess matches the ALC/LO list used in KSK builder/contractor modules.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F11-001 | Karmika Seva Kendra Integration | Profile sync, officer RBAC alignment, officer review actions, and cess payment collection through the Board/KSK payment interface. |
| F11-002 | Automated Departmental Data Ingestion | Ingest from e-procurement, building-plan/NIRMANA-class systems, treasury/Khajane 2.0, GST and other facilitated systems. |
| F11-003 | Manual and Semi-Automated Capture | Forms and processes for agencies or departments that cannot expose a live interface. |
| F11-004 | Integration Data Pool | Maintain a mirrored pool of integrated data to feed MIS and predictive analytics. |

---

### 12. CESS API Connector Self-Service Portal

**Purpose:** Let listed **collection agencies** onboard **standard connectors** without a bespoke build per agency, under Board governance.

**Type:** Technical

**Functional requirements:**

- Dedicated self-service portal for CESS API and connector management.
- Pre-defined, ready-to-use connectors for agencies in **Annexure A and Annexure B** of the RFP.
- Standard templates: authentication, data exchange formats, error handling, **REST and SOAP**.
- Agency self-service: register, configure, activate without routine Board technical labour.
- Health monitoring (status, uptime, data flow) and alerts on failure or discrepancy.
- Version management, update and rollback.
- Testing **sandbox** before go-live.
- Usage logs and audit trails per agency.
- Board administrators approve, revoke or reconfigure connector access.

**Acceptance criteria:**

- A new listed agency can complete sandbox validation and go live using a template connector without a unique development ticket, subject to Board approval.
- Board admin can revoke a connector and halt data flow.
- REST-oriented and SOAP-oriented agencies can both complete an exchange using the published templates.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F12-001 | Connector Catalogue and Agency Onboarding | Pre-configured connectors, templates and self-service registration/activation with Board approval. |
| F12-002 | Connector Health, Versioning and Sandbox | Monitor uptime and flow; manage versions and rollback; sandbox testing before production. |
| F12-003 | Connector Audit and Protocol Coverage | Usage logs, audit trails, and support for REST and SOAP agency landscapes. |

---

### 13. GIS Analytical Platform

**Purpose:** Give back-office users a **GIS view of buildings and projects** for monitoring and leakage intelligence.

**Type:** Business

**Functional requirements:**

- Superimpose GIS layers; display line segments and polygons.
- Show projects/assessments on map in concert with Module 02 territory and Module 14 analytics.
- Support GIS intelligence pushed to portal users (Module 06).

**Acceptance criteria:**

- A Board user can locate a registered project on the map using authorised layers.
- Layer superimposition does not require a separate desktop GIS licence as a user prerequisite (browser/back-office GIS as delivered).

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F13-001 | GIS Layers, Lines and Polygons | Maintain and display layers, line segments and polygons for buildings and projects. |
| F13-002 | Layer Superimposition and Project Display | Superimpose layers and display cess projects/assessments for review. |

---

### 14. MIS, Analytics and Decision Support

**Purpose:** Provide **real-time dashboards and predictive reports** for demand, collection, leakage and policy.

**Type:** Business

**Functional requirements:**

- Department-wise cess collection, project status, cost/time overruns, pending actions, KPIs and trends.
- Interactive dashboard: registered vs unregistered construction signals, compliance rate, revenue leakage, regional distribution.
- Analytical and **predictive** reports for decision support.
- Provision to integrate with a **command and control centre later** (interface readiness only; CCC itself is out of scope).
- Push of selected intelligence to staff and to external agencies (with Module 10).

**Acceptance criteria:**

- Authorised officers can filter DCB and project KPIs by department, territory and period.
- Outstanding dues older than 30 days are visible on the monitoring dashboard.
- Predictive/analytical outputs are reproducible from stored data for a stated as-on date.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F14-001 | Operational MIS Dashboards | Real-time department, territory and project dashboards for cess monitoring. |
| F14-002 | KPI, Leakage and Trend Reporting | KPIs for collection, compliance, leakage and regional distribution, with drill-down. |
| F14-003 | Predictive Decision Support | Analytical and predictive reports for demand assessment and policy; CCC hook reserved for later. |

---

## 7. End-to-End Workflows

### 7.1 Project appears and cess is computed

1. Project data arrives by connector, e-procurement/building-plan/treasury feed, portal entry, or Board/manual capture.
2. Infra registry record is created or updated (Module 03).
3. System computes **1% cess** (and later revisions from assessment).
4. Demand is visible to Board accounts and to the responsible agency on the portal.

### 7.2 Field assessment and on-the-spot demand

1. State or district creates an assessment worklist.
2. Inspector opens the item on mobile, captures GPS media, surveys new work or partial violation.
3. Cess is calculated; demand notice is issued on the spot and also stored for the agency on the portal.
4. DCB and dashboards update.

### 7.3 Collection, LCDRS and remittance (30-day clock)

1. Agency collects at cash counter or equivalent; QR acknowledgement is issued.
2. LCDRS posts remittance to the Board cess account with demand/project detail.
3. Alternatively, agency remits through bank/Treasury interface against demand.
4. If remittance is not completed within 30 days, alerts fire; escalation matrix applies; interest-loss is computed.

### 7.4 Appeal or grievance

1. Payee files appeal or grievance on the portal.
2. Inward acknowledgement is generated; file lands in mapped e-office inbox.
3. Board processes; accounts post refund or uphold demand; payee sees status.

### 7.5 Agency technical onboarding

1. Agency registers on the Connector Self-Service Portal.
2. Configures a template connector; tests in sandbox.
3. Board approves; production data flows; health dashboard monitors the connector.

---

## 8. Access Control

Access is **role-based**, constrained by **organisation, designation, territory and assigned work**. It is **not** a simple User/Admin-only model.

| Principal | Typical access |
| --------- | -------------- |
| Super administrator | Masters, RBAC, logs, backups, middleware/connector governance |
| Board / Labour Department officers | Back-office cess, accounts, e-office, MIS/GIS per mapping |
| Registering Officer (ALC/LO) | Same officer universe as KSK builder/contractor modules |
| Labour Inspector | Assigned assessment work, field mobile, own territory |
| Government department / private agency user | Own portal account, own DCB, own appeals/grievances, own connector (if any) |
| Agency technical contact | Connector portal within Board-approved scope |

**Two-factor authentication** is required for Labour Cess Portal logins as specified in the RFP.

Inspector (and similar field roles) **see only assigned projects**, as stated under Data Governance in the RFP.

---

## 9. Channels

| Channel | Users | Use |
| ------- | ----- | --- |
| Back-office web | Board and Labour Department staff | Masters, registry, accounts, e-office, MIS, GIS, worklists |
| Labour Cess Portal (web) | Government departments and private agencies | Demand, collection, remittance, DCB, appeal, grievance, notices |
| Connector Self-Service Portal (web) | Agency integrators and Board admins | Connector onboarding, sandbox, health |
| Inspector mobile | Labour Inspectors | Assessment, GPS media, on-the-spot notice |
| Staff mobile | Labour Department / Board staff | DCB dashboards, assessment support, appeals, meetings, alerts, GPS timestamped updates |
| GIS analytical views | Authorised back-office users | Layers, polygons, project display |

There is **no** general public citizen app in this phase beyond cess payee/agency access.

---

## 10. Integrations

| Integration | Purpose | Notes |
| ----------- | ------- | ----- |
| Karmika Seva Kendra (KSK) | Profile, officers, review, **online payment collection** | Mandatory; RFP payment milestone |
| Khajane 2.0 / treasury | Financial posting and remittance intelligence | Named in Annexure A and architecture |
| Karnataka e-procurement (eProc / KPPP as applicable) | Tender/project cost and award signals | Named |
| Building plan / town planning (NIRMANA and local) | Permits and construction intelligence | State and individual planning authorities |
| GST applications | Complementary financial/construction signals | Named |
| CESS connectors (Annexure A, B and listed central agencies) | Project and cess data exchange | REST and SOAP templates |
| SMS / email / in-app | Alerts and credential mail | Templates in Module 10 |
| Bank accounts | Cess collection and remittance | LCDRS and Board accounts |
| Command and control centre | Future | Interface provision only |

The Board facilitates introductions and policy; the implementing agency performs technical integration.

---

## 11. Audit, Compliance & Security

- All actions, entries and edits **logged and timestamped**.
- Role-based visibility; encrypted storage; SSL for hosted access; API authentication for integrations.
- Conformance with the **IT Act** as stated in the RFP hosting/security plan.
- External data sharing (audit, treasury) **approved and encrypted**.
- Connector usage logs for compliance verification.
- Security audit support as part of KSDC hosting obligations.
- Audit-ready deducted vs remitted reports for **CAG/AG**.

---

## 12. Non-Functional Requirements

| Area | Expectation (from RFP) |
| ---- | ---------------------- |
| Hosting | Karnataka State Data Centre; **DR site**; regular backups |
| Performance | Load-balanced, scalable data store; admin health monitoring and alert thresholds |
| Availability | DR and monitoring to mitigate downtime (exact SLA to be confirmed at contracting) |
| Security | RBAC, encryption, audit trails, two-factor on agency portal |
| Ownership | Board owns application, latest source code (including ready-to-use modules) and all cess/project metadata |
| Build model | Custom-built only; not licence-based; not COTS |
| Language | English for contractual reports; operational usability for field officers |
| Training | Train-the-trainer; in-person clusters; videos/manuals; sandbox (RFP data sheet also marks training “No” as a scoring feature — delivery Phase 4 still requires the capacity-building programme in the ToR) |
| Helpdesk | Handholding during adoption (stated under risk mitigation) |

---

## 13. Data Migration

The RFP does not specify a historical cess-ledger migration from a named legacy cess application. **Structured migration of prior-year cess ledgers is out of scope unless the Board later supplies extracts and rules.**

**In scope:** ongoing capture from KSK and other systems from go-live of each integration; preservation of history created **in this system**; historical trend analysis on data stored after go-live.

If the Board later mandates load of past remittances, that shall be a change to this SOW.

---

## 14. Phased Delivery

Aligned to RFP Section 13. Calendar days are **as in the RFP** (aggressive); contracting may restated them, but this SOW does not change the RFP sequence.

| Phase | Content | Timing (RFP) |
| ----- | ------- | ------------ |
| Phase 1 — SRS | Study existing KBOCWWB applications; SRS | 30 days |
| Phase 2 — Milestone 1 | RFP Modules 1–6 (super admin, territory, organisation, inward/outward, DMS, e-office) | 30 days from Purchase Order |
| Phase 2 — Milestone 2 | RFP Modules 7–9 (meetings, back-office cess, GPS assessment) | 30 days from successful Milestone 1 |
| Phase 2 — Milestone 3 | RFP Modules 10–16 (appeal, middleware, accounts, GIS analytics, alerts, DSS, **Labour Cess Portal go-live**) | 60 days from successful Milestone 2 |
| Phase 3.1 | KSK integration and online payment via Board/KSK payment interface | 90 days from successful Milestone 3 |
| Phase 3.2 | RFP Module 17 — CESS API / Connector Self-Service Portal for listed agencies | 30 days from successful Phase 3.1 |
| Phase 4 | Training and capacity building | 30 days after Phase 3 |
| Phase 5.1 | AMC year 1 | 12 months from completion of Phase 3.1 |
| Phase 5.2 | AMC year 2 | 12 months after AMC year 1 |

Performance security in the RFP is sized for **9 months development** plus **24 months AMC**.

Indicative RFP payment weights (for vendor awareness, not an estimate of effort): Milestones 1–3 and KSK integration **10% each**; Connector portal **45%**; AMC **7.5% + 7.5%**.

---

## 15. Deliverables

1. Software Requirements Specification and subsequent design artefacts agreed with the Board.
2. Custom application covering all Section 6 modules (RFP 1–17 scope).
3. Inspector mobile and staff mobile applications as specified.
4. Labour Cess Portal and Connector Self-Service Portal.
5. Integrations in Section 10, including KSK and connector templates for Annexure A/B agencies.
6. Deployment on KSDC with DR, backups and monitoring.
7. Security-audit cooperation and closure of audit observations required for go-live.
8. Training (master trainers, materials, sandbox) and implementation helpdesk.
9. Source code (latest version) and operational documentation handed to KBOCWWB.
10. MIS/GIS dashboards and audit-ready DCB/reconciliation outputs.
11. Two years AMC from the RFP start point (completion of Phase 3.1).

---

## 16. Acceptance Criteria

**Program level** (in addition to module-level criteria):

1. SRS accepted before Milestone 1 build is treated as complete.
2. Each Phase 2 milestone is accepted when the listed RFP modules are deployed and demonstrated on Board-approved scenarios.
3. Labour Cess Portal go-live (Milestone 3) includes two-factor agency login, cash counter/LCDRS path, scheduled demand update and agency DCB.
4. Phase 3.1 accepted when KSK profile, officer mapping, officer review and **online payment collection via the Board/KSK interface** work on agreed test cases.
5. Phase 3.2 accepted when the Connector Self-Service Portal supports sandbox-to-production onboarding for the agreed first set of Annexure A/B connector templates.
6. Training completion certificates / attendance as Phase 4.
7. AMC service levels as contracted; source code escrow/handover complete.

---

## 17. Expected Benefits

- Higher share of **eligible 1% cess** actually demanded and remitted.
- **Project-wise** transparency instead of delayed lump-sum transfers.
- Fewer **interest losses** from remittance beyond 30 days.
- Faster **field demand** through GPS assessment and on-the-spot notices.
- Fewer **audit objections** through reconciliation and logs.
- Agencies can comply via **integration or portal**, including those still on manual processes.
- Better **welfare funding** predictability for construction workers (outcome of timely cess, not a new welfare product in this SOW).

---

## 18. Assumptions & Dependencies

1. **Project code** for this SOW set is `CESS`; display name **Labour CESS Tracking & Monitoring System**; output folder `Projects/CESS/`.
2. Document management and e-office remain **in scope**; they are grouped under Module 04 for this SOW and still map to RFP Modules 4–6 for delivery/payment.
3. KSK remains the system of record for **worker welfare operations**; this application is the system of record for **cess tracking**.
4. **1%** cess and **30-day** remittance rule apply unless the Board issues a changed business rule.
5. Interest-loss formula, notice templates and escalation steps will be supplied by KBOCWWB during SRS.
6. KSDC hosting, DR, SSL certificates and security-audit slotting are **Board / SDC responsibilities** to provision; the implementing agency deploys and hardens the application.
7. Departmental integrations depend on **Board-facilitated access** to counterpart systems; delay in counterpart APIs is not a reduction of functional scope.
8. Annexure lists of ULBs, panchayats, planning authorities and CPSUs are **onboarding volume**, not separate software products.
9. Command and control centre is **future**; only a provision to integrate later is in scope.
10. No full historical cess-ledger migration unless the Board later authorises it.
11. Two-factor authentication applies to the **Labour Cess Portal** as specified; back-office MFA to follow Board security policy at SRS if not restated.
12. RFP data sheet marks training as “No” for one evaluation clause; **ToR Phase 4 and Section 12.5 still require** train-the-trainer capacity building — that ToR requirement is in scope.
13. Payment collection online is **only** through the Board/KSK interface named for Phase 3.1 (not an uncontrolled third-party checkout).
14. Custom-built ownership includes handover of source even for “ready-to-use” components the vendor employs.

---

## 19. Vendor Response Expectations

Vendors should:

1. Confirm coverage of **all RFP Modules 1–17** against the feature IDs in this SOW (Appendix A and B).
2. Describe how **LCDRS**, **30-day** alerts and **interest-loss** will work in business terms.
3. Describe **KSK** integration and **connector self-service** (including REST and SOAP templates and sandbox).
4. Describe **manual capture** for non-IT agencies and for 7000+ Gram Panchayats where live integration is not ready.
5. Propose a **KSDC** deployment and DR approach without prescribing a proprietary lock-in.
6. Provide the **methodology, work plan, risks and a demo of a similar application** as required for technical presentation.
7. Confirm **source-code handover** and Board ownership.
8. Price in line with RFP financial forms; this SOW does **not** contain effort hours.

Do not respond with database schemas, interface path designs, or UI wireframes as a substitute for the business confirmation above.

---

## 20. Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User, Role and Organisation Governance | Shared | F01-001 … F01-004 (4) |
| 02 | Territory and GIS Foundation | Shared | F02-001 … F02-002 (2) |
| 03 | Labour Cess Masters and Project Registry | Business | F03-001 … F03-003 (3) |
| 04 | Correspondence, Document Management and E-office | Shared | F04-001 … F04-004 (4) |
| 05 | Field Assessment and Demand | Business | F05-001 … F05-004 (4) |
| 06 | Labour Cess Portal, LCDRS and Collections | Business | F06-001 … F06-006 (6) |
| 07 | Appeals and Grievances | Business | F07-001 … F07-003 (3) |
| 08 | Accounts, DCB, Notices and Reconciliation | Business | F08-001 … F08-005 (5) |
| 09 | Meetings and Task Tracking | Business | F09-001 … F09-002 (2) |
| 10 | Alerts, Notifications and Escalation | Shared | F10-001 … F10-002 (2) |
| 11 | Integrations, Smart Middleware and KSK | Technical | F11-001 … F11-004 (4) |
| 12 | CESS API Connector Self-Service Portal | Technical | F12-001 … F12-003 (3) |
| 13 | GIS Analytical Platform | Business | F13-001 … F13-002 (2) |
| 14 | MIS, Analytics and Decision Support | Business | F14-001 … F14-003 (3) |

**Total: 14 modules, 47 feature outlines.**

---

## 21. Appendix B — Mapping to RFP Software Modules

| RFP Module | RFP name | This SOW |
| ---------- | -------- | -------- |
| 1 | Super administrator | 01 |
| 2 | Territory (MIS and GIS based) | 02 |
| 3 | Organisation structure | 01 |
| 4 | Inward/outward | 04 |
| 5 | Document management system (DMS) | 04 |
| 6 | E-office | 04 |
| 7 | Meetings | 09 |
| 8 | Back-office Labour cess application | 03 |
| 9 | GPS enabled Assessment (web and mobile) | 05 |
| 10 | Appeal module | 07 |
| 11 | Smart middleware (SI) | 11 |
| 12 | Accounts (including staff mobile bundle) | 08 (mobile channel also serves 05, 07, 09, 10) |
| 13 | Back-office GIS based analytical platform | 13 |
| 14 | Auto alerts and notifications | 10 |
| 15 | Analytical reports with decision support | 14 |
| 16 | Labour cess portal | 06 |
| 17 | CESS API/Connector Self Service Portal | 12 |

Delivery milestones in Section 14 continue to use **RFP module numbers 1–17** so they stay aligned with the tender payment table.

---

## 22. Appendix C — CESS Collection Agency Groups

The implementing agency shall support information flow from the groups listed in the RFP (full proper names remain in the tender annexures). Groups include:

- **Annexure A (indicative):** Khajane 2.0, Karnataka e-procurement, BBMP, BDA, BMRDA, BWSSB, KUIDFC, KSIIDC, KSIDC, BMRCL, CREDAI, RERA, BMTC, KSRTC, KHB, KSDB, KSTDC, KIADB, PWD, KSHIP, SHDP, KRDCL, and others listed in the RFP.
- **Annexure B (indicative):** City Corporations, Municipal Councils, Town Municipal Councils, Town Panchayats, Urban Development bodies, Planning Authorities, ESCOMs, KPTCL, KPCL, RDPR, South Western Railway, housing and irrigation corporations, Smart Cities, line departments, **over 7000 Gram Panchayats**, and listed **Central PSUs** (for example HAL, BHEL, IOCL, NTPC, as in the RFP list).

Connectors and/or portal/manual capture cover these agencies; each name is not a separate software module.

---

## 23. Appendix D — Key Entities

| Entity | Meaning |
| ------ | ------- |
| Construction project (infra registry) | Building or other construction work against which 1% cess is computed |
| CESS collection agency | Department, ULB, PSU, private body that deducts or collects cess |
| Demand | Amount payable as cess, including assessment revisions |
| Remittance | Transfer to KBOCWWB cess account / treasury, due within 30 days of deduction |
| LCDRS | Labour cess deductions/collection and remittance at source at the time of collection |
| Assessment | Field or back-office survey of work, including partial violation |
| Appeal / grievance | Payee challenge or complaint on cess matters |
| Connector | Standardised data exchange configuration for an agency |
| Territory | Administrative geography used for assignment, MIS and GIS |
| KSK | Existing Karmika Seva Kendra platform of KBOCWWB |

---

## 24. Appendix E — Named KSK Integration Operations

As stated in RFP Section 7 (described here as business operations, not interface designs):

| Operation | Business purpose |
| --------- | ---------------- |
| Builder/Contractor Profile Sync | Fetch Aadhaar-verified details and mobile numbers of registered builders/contractors to pre-fill cess registration |
| Cess Payment Collection | Secure online payment (net banking, UPI, cards) linked to Board accounting — **this is the mandated online collection path** |
| Officer Review Action | Labour Department officers view project, documents and payment in one place |
| Officer Mapping (RBAC) | Registering Officer in cess is limited to the same ALC/LO list as KSK builder/contractor modules |

---
