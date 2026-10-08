# Statement of Work (SOW)

# Department of Information & Public Relations (DIPR), Government of Karnataka

# Advertisement Monitoring Tool (AMT)

**Document Type:** Statement of Work – Design, Development, Deployment & Maintenance  
**Version:** 1.0  
**Status:** RFP-ready (estimation / proposal alignment)  
**Source:** E-Tender DIPR/DD(P)/E-Tender/AMT/2026-27/ dated 28-08-2026; Pre-bid queries (Inventech) on RFP Ref. DIPR/2026-27/SE0027  
**Issuing Authority:** Commissioner, Department of Information & Public Relations, Government of Karnataka  
**Office:** “Vartha Soudha”, No. 17, Bhagvan Mahaveer Road (Infantry Road), Bengaluru 560 001  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control / RBAC](#8-access-control--rbac)
9. [Channels](#9-channels)
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
20. [Appendices](#20-appendices)

---

## 1. Introduction

This Statement of Work (SOW) defines the functional and delivery scope for design, development, deployment, and maintenance of an **Advertisement Monitoring Tool (AMT)** for the **Department of Information & Public Relations (DIPR), Government of Karnataka**.

The engagement is floated through e-procurement as:

> **E-Tender for Advertisement design, development, deployment, and maintenance of an Advertisement Monitoring Tool through e-procurement**  
> Tender Ref.: **DIPR/DD(P)/E-Tender/AMT/2026-27/** (also referenced in pre-bid correspondence as **DIPR/2026-27/SE0027**)

The successful bidder shall deliver a **hosted web application** and a **companion mobile application** (native Android and iOS **or** Progressive Web App) to manage advertising campaign activities across **print, digital, and outdoor** media, including campaign lifecycle, asset inventory, proof-of-display (PoD) verification, reporting, analytics, secure access, and integrations.

**Document handling** and **approval workflows** are **embedded** inside campaign, asset, and PoD processes and are not separate bid modules.

This SOW consolidates tender Section I–II functional/technical requirements into estimable modules and feature outlines for RFP response and internal estimation. Commercial, eligibility, EMD, and legal annexure content from the tender remains governed by the official bidding documents; this SOW does not replace KTPP-governed tender terms.

---

## 2. Project Overview

| Aspect | Description |
| ------ | ----------- |
| Client | Department of Information & Public Relations (DIPR), Government of Karnataka |
| Solution | Advertisement Monitoring Tool (AMT) — web + companion mobile |
| Media domains | Print, digital, outdoor |
| Core outcomes | End-to-end campaign management; centralized creative/outdoor asset inventory with geotagging & versioning; PoD capture & verification; KPI/compliance reporting; RBAC with secure authentication |
| Hosting | Hosted web application; Government hosting preferred for data residency / sovereignty (handover for Government hosting where applicable) |
| Delivery window | **18 weeks** from work-order acceptance to production readiness (phased — see Section 14) |
| Maintenance | Minimum maintenance and support period as contracted; SLAs per tender Section V |
| Accessibility | WCAG 2.1 Level AA; multilingual user interfaces |
| Portal | Bids via http://kppp.karnataka.gov.in |

### 2.1 Business context

DIPR manages Government advertising across multiple channels. Today’s monitoring of campaign approvals, creative versions, outdoor placements, and proof-of-display is fragmented. AMT provides a single platform for officials, vendors, and field personnel to plan campaigns, store assets, capture geotagged PoD evidence, verify compliance, and produce audit-ready reports.

### 2.2 Guiding principles

1. **Campaign-first operations** — approvals, schedule, budget, and vendor assignment drive downstream PoD and reporting.
2. **Evidence-backed compliance** — PoD images/videos carry timestamp, GPS, and device metadata; verification is workflow-controlled.
3. **Field enablement** — mobile app supports assigned tasks, checklists, and offline capture with later sync.
4. **Secure Government use** — RBAC, optional SSO, MFA, encryption, OWASP-aligned coding, and DIPR data ownership.
5. **Transparent analytics** — role-based dashboards, channel-wise spend, compliance reports, and exportable MIS.

---

## 3. Project Objectives

1. Deliver end-to-end **campaign management** (creation, approvals, scheduling, budgeting, vendor assignment, version control).
2. Maintain a **centralized asset inventory** for print, digital, and outdoor creatives with metadata, versioning, geotagging (outdoor), and search/filter.
3. Provide **proof-of-display verification** via image/video capture with timestamps, GPS, device metadata, batch upload, manual verification, and provision for third-party verification services.
4. Generate **dashboards and reports** for campaign KPIs, channel-wise spend, compliance, audit logs, scheduled PDF/CSV exports, and role-based views.
5. Implement **user & access management** with RBAC, optional SSO, MFA, and access audit trails.
6. Expose **secure RESTful APIs** for data exchange, DIPR system integration, and third-party analytics provisions.
7. Deliver a **secure mobile application** for field PoD capture, task management, checklists, and offline synchronization.
8. Complete **testing, documentation, training, deployment**, and knowledge transfer within the mandatory 18-week timeline.
9. Meet **security, accessibility (WCAG 2.1 AA), multilingual UI**, and Government compliance expectations stated in the tender.

---

## 4. In Scope / Out of Scope

### 4.1 In Scope

**A. Design & Prototype**

- Requirements analysis and finalization with DIPR  
- System / solution design (business-level architecture description in proposal)  
- UI/UX design and working prototype / PoC for major modules  
- Mapping of modules to tender technical requirements  

**B. Build & Integrate**

- Full-stack development of web application  
- Companion mobile application (Android & iOS native **or** PWA, as accepted by DIPR)  
- Secure RESTful APIs; integration with existing DIPR systems (as identified during requirements)  
- Provisions for third-party analytics and PoD verification services  
- Database implementation supporting campaign, asset, PoD, and audit data  

**C. Functional platform (modules in Section 6)**

- Campaign Management  
- Creative Asset Inventory  
- Proof-of-Display Capture & Verification  
- Reporting & Analytics  
- User & Access Management  
- Mobile Field Operations  
- Notifications supporting approvals, assignments, and PoD outcomes  
- Integration Hub for DIPR / third-party connectors  

**D. Testing & Quality**

- Test plans, test cases, defect tracking  
- Unit, integration, system, beta, and UAT support with sign-off procedures  

**E. Security & Compliance**

- Secure coding; OWASP Top 10 mitigations  
- Encryption at rest and in transit  
- Data retention policies; role-wise access logs  
- Compliance with applicable Government security guidelines  
- WCAG 2.1 Level AA; multilingual interfaces  

**F. Documentation, Training & Knowledge Transfer**

- Architecture documents, user manuals, administrator guides  
- Training sessions for DIPR staff  
- Knowledge transfer for operations handover  

**G. Deployment & Support**

- Deployment to production (or handover for Government hosting)  
- Post-deployment stabilization (Weeks 17–18)  
- Maintenance and support for the contracted period with SLA commitments  

### 4.2 Out of Scope (unless added by change / amendment)

- Procurement of Government data-centre hardware, network, or cloud tenancy (bidder may host temporarily only if DIPR so directs; preferred model is Government hosting)  
- Permanent DIPR operational staffing beyond training, handholding, and contracted support  
- Creative design / media buying of advertisements themselves (platform monitors and manages campaigns; it does not replace media agencies’ creative production unless separately contracted)  
- Unnamed third-party verification or analytics product licenses until DIPR identifies vendors and license ownership  
- Historical bulk migration of legacy campaign archives unless DIPR provides structured data and adds migration to scope during requirements  
- Physical outdoor site construction, media agency field labour, or non-software PoD logistics  

---

## 5. Solution Expectations

| Area | Expectation |
| ---- | ----------- |
| Channels | Staff web portal; field mobile app (Android/iOS or PWA); API consumers |
| Media | Print, digital, outdoor campaign and asset support |
| Access | RBAC; optional SSO; MFA; audit of privileged actions |
| Campaign lifecycle | Create → approve → schedule → assign vendors → track versions → close |
| Assets | Central repository with metadata, versions, outdoor geotags, search/filter |
| PoD | Capture/upload with timestamp, GPS, device metadata; batch; verify; optional third-party |
| Offline | Field capture of PoD / tasks offline with sync and conflict handling when online |
| Reporting | KPI dashboards, channel spend, compliance, audit exports (PDF/CSV), schedules, role views |
| Integrations | REST APIs; DIPR systems; third-party analytics / verification provisions |
| UX | Multilingual UI; WCAG 2.1 AA |
| Availability | Minimum **99.5%** uptime excluding scheduled maintenance (tender Section V) |
| Support SLAs | Critical 4h response; High 8 business hours; Medium 2 business days; Low 5 business days |

---

## 6. Consolidated Functional Modules

Modules are numbered for implementation and estimation. Feature IDs in each **Key capabilities** table are the official IDs for downstream estimation.

### 01. User & Access Management

**Type:** Shared  
**Slug:** `user-access-management`  
**Purpose:** Authenticate users and enforce role-based permissions across web, mobile, and APIs, with optional SSO, MFA, and access audit trails.

**Functional requirements:**

- Maintain users, roles, and permission assignments for DIPR staff, vendors (as applicable), and field personnel  
- Support Role-Based Access Control for all modules  
- Provide optional Single Sign-On integration with DIPR identity provider (protocol finalized with DIPR)  
- Enforce multi-factor authentication as configured  
- Maintain login/session and privilege-change audit trails  
- Support activation, deactivation, and password / credential lifecycle policies  

**Acceptance criteria:**

- Users only see modules and actions permitted by role  
- MFA and optional SSO behave as configured in UAT  
- Access changes are auditable  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | User account lifecycle | Create, update, activate/deactivate staff, vendor, and field user accounts |
| F01-002 | Role & permission matrix | Define roles and map create/read/update/approve/verify permissions by module |
| F01-003 | Optional SSO integration | Integrate with DIPR IdP (SAML/OIDC/LDAP as confirmed) when enabled |
| F01-004 | Multi-factor authentication | Enforce MFA for configured roles / channels |
| F01-005 | Access audit trail | Record authentication events and permission changes for compliance review |

---

### 02. Master Data & System Configuration

**Type:** Business  
**Slug:** `master-data-system-configuration`  
**Purpose:** Provide controlled reference data and system parameters that campaign, asset, PoD, and reporting modules depend on.

**Functional requirements:**

- Maintain masters for media channels (print / digital / outdoor), campaign types, statuses, vendors/agencies, districts/locations, budget heads (as applicable), and PoD verification outcomes  
- Configure notification templates and system parameters (retention, sync windows, GPS accuracy thresholds once finalized)  
- Support search, filter, and controlled edit of masters with audit of changes  
- Multilingual labels for key reference values where required for UI  

**Acceptance criteria:**

- Campaigns, assets, and PoD cannot be created without valid master references  
- Parameter changes apply without code redeploy where designed as configuration  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Media & campaign reference masters | Maintain media types, campaign types, statuses, and related lookups |
| F02-002 | Vendor / agency master | Maintain vendor/agency profiles used in campaign assignment |
| F02-003 | Location & geography masters | Maintain districts / locations used for outdoor geotagging and filters |
| F02-004 | Notification templates & system parameters | Configure email/SMS/in-app templates and operational parameters |
| F02-005 | Master search, filter & change audit | Search/filter masters and retain change history |

---

### 03. Campaign Management

**Type:** Business  
**Slug:** `campaign-management`  
**Purpose:** Manage advertising campaigns end-to-end including creation, workflows, approvals, scheduling, budget tracking, vendor assignment, and version control.

**Functional requirements:**

- Create and maintain campaigns across print, digital, and outdoor  
- Embedded approval workflow with configurable stages and roles  
- Schedule campaign windows and milestones  
- Track budgets / spend against campaign (channel-wise attribution where data exists)  
- Assign vendors/agencies and track assignment history  
- Version-control campaign briefs / creative packages linked to assets  
- Link campaigns to PoD tasks and compliance status  

**Acceptance criteria:**

- A campaign cannot proceed past approval gates without authorized action  
- Schedule, budget, vendor, and version history are visible to entitled roles  
- Campaign status drives field task eligibility  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Campaign create & maintain | Create/edit campaign profiles across print, digital, outdoor with media attributes |
| F03-002 | Campaign approval workflow | Embedded multi-stage approval with comments, reject/resubmit, and status trail |
| F03-003 | Scheduling & milestones | Define campaign calendar windows and key milestones |
| F03-004 | Budget & spend tracking | Record planned budget and track channel-wise spend against campaign |
| F03-005 | Vendor assignment | Assign vendors/agencies to campaigns and maintain assignment history |
| F03-006 | Campaign version control | Version campaign packages/briefs and link to asset versions |
| F03-007 | Campaign–PoD linkage | Link campaigns to field PoD tasks and roll up verification status |

---

### 04. Creative Asset Inventory

**Type:** Business  
**Slug:** `creative-asset-inventory`  
**Purpose:** Central repository for creative and outdoor assets with metadata, versioning, geotagging, and search.

**Functional requirements:**

- Upload and store creatives (images, videos, documents as applicable) linked to campaigns  
- Capture metadata (channel, format, language, validity dates, ownership)  
- Version assets and retain prior versions  
- Geotag outdoor assets / sites  
- Search, filter, and browse inventory with role-based access  
- Support controlled download / preview for entitled users  

**Acceptance criteria:**

- Assets are findable by campaign, channel, location, and version  
- Outdoor assets show geotag where required  
- Unauthorized users cannot access restricted assets  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Asset upload & metadata | Upload creatives and capture channel, format, language, validity, and ownership metadata |
| F04-002 | Asset versioning | Maintain version history and current-version designation |
| F04-003 | Outdoor geotagging | Capture and display geotags for outdoor assets / sites |
| F04-004 | Inventory search & filter | Search/filter assets by campaign, channel, location, status, and metadata |
| F04-005 | Asset access & preview | Role-based preview/download of assets with access logging |

---

### 05. Proof-of-Display Capture & Verification

**Type:** Business  
**Slug:** `proof-of-display-verification`  
**Purpose:** Capture, store, and verify proof-of-display evidence with timestamps, GPS, device metadata, batch handling, and optional third-party verification.

**Functional requirements:**

- Capture/upload images and videos as PoD against campaign / site / task  
- Stamp timestamp, GPS coordinates, and device metadata  
- Support batch upload and bulk association to campaigns/sites  
- Manual verification workflow (accept / reject / rework) with comments  
- Provision connectors for third-party verification services (when DIPR names the service)  
- Retain verification history for audit and compliance reports  

**Acceptance criteria:**

- PoD records without mandatory metadata (as finalized in requirements) are flagged or rejected  
- Verification decisions are role-controlled and auditable  
- Third-party verification path is available when credentials/APIs are provided  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | PoD capture & metadata stamp | Capture/upload image/video with timestamp, GPS, and device metadata |
| F05-002 | Batch PoD upload | Upload and associate multiple PoD items to campaigns/sites in batch |
| F05-003 | Manual verification workflow | Accept/reject/rework PoD with comments and status history |
| F05-004 | PoD validation rules engine | Apply DIPR-confirmed GPS accuracy, timestamp source, and tamper/validation rules |
| F05-005 | Third-party verification provision | Integrate optional third-party verification when DIPR provides APIs/credentials |
| F05-006 | PoD evidence register | Searchable register of PoD evidence with campaign, site, and verification status |

---

### 06. Mobile Field Application

**Type:** Business  
**Slug:** `mobile-field-application`  
**Purpose:** Secure mobile experience for field personnel to manage assigned tasks/checklists and capture PoD, including offline mode with synchronization.

**Functional requirements:**

- Authenticated mobile access for field roles  
- View assigned campaigns/tasks and checklists  
- Capture PoD (camera/gallery as allowed) with metadata while on site  
- Operate offline for designated capture and task-update functions  
- Synchronize queued data when connectivity returns, with conflict resolution  
- Notify field users of new assignments and verification outcomes (via notification module)  

**Acceptance criteria:**

- Field users can complete assigned PoD capture without continuous connectivity  
- Synced data appears correctly on web for verification  
- Conflicts are resolved per defined rules without silent data loss  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Field task & checklist inbox | View and update assigned field tasks and checklists on mobile |
| F06-002 | Mobile PoD capture | Capture PoD from mobile with GPS/timestamp/device metadata |
| F06-003 | Offline mode & local queue | Queue PoD and task updates while offline |
| F06-004 | Sync & conflict resolution | Synchronize queued items when online and resolve conflicts per rules |
| F06-005 | Mobile secure session | Secure login/session handling for field devices aligned to access policy |

---

### 07. Reporting & Analytics

**Type:** Business  
**Slug:** `reporting-analytics`  
**Purpose:** Provide dashboards, KPI views, compliance and spend reports, audit exports, scheduling, and role-based report access.

**Functional requirements:**

- Dashboards for campaign KPIs (definitions finalized with DIPR)  
- Channel-wise spend views  
- Compliance reports based on PoD verification outcomes  
- Audit log reports / exports  
- Export to PDF/CSV; schedule recurring reports  
- Role-based dashboard and report visibility  

**Acceptance criteria:**

- Entitled roles see only authorized views  
- Scheduled reports deliver to configured recipients  
- Figures reconcile to campaign/PoD source data for UAT sample sets  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Campaign KPI dashboards | Role-based dashboards for campaign progress, PoD completion, and status KPIs |
| F07-002 | Channel-wise spend analytics | Views and reports of spend by print/digital/outdoor and campaign |
| F07-003 | Compliance & PoD reports | Reports of verification outcomes, exceptions, and compliance posture |
| F07-004 | Audit log export | Exportable audit reports for access and key operational events |
| F07-005 | Scheduled & exportable reports | PDF/CSV export and scheduled delivery of standard reports |
| F07-006 | Role-based report views | Restrict dashboards/reports by role and organisational scope |

---

### 08. Notifications & Alerts

**Type:** Shared  
**Slug:** `notifications-alerts`  
**Purpose:** Deliver in-app, email, and (where integrated) SMS alerts for approvals, assignments, PoD outcomes, and operational reminders.

**Functional requirements:**

- Trigger notifications on campaign approval actions, vendor/field assignments, PoD verification outcomes, and SLA-style reminders where configured  
- Support in-app notification centre on web; push/in-app on mobile where platform supports  
- Use configurable templates from masters  
- Respect user/role notification preferences within policy  

**Acceptance criteria:**

- Key workflow events generate notifications to correct recipients in UAT  
- Failed deliveries are logged for support  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | In-app notification centre | Web/mobile in-app notifications for workflow and assignment events |
| F08-002 | Email notification dispatch | Email alerts using templates for approvals, assignments, and PoD outcomes |
| F08-003 | SMS notification provision | Optional SMS alerts when gateway credentials are provided by DIPR |
| F08-004 | Notification preference & delivery log | User/role preferences within policy and delivery/failure logs |

---

### 09. Integration Hub

**Type:** Technical  
**Slug:** `integration-hub`  
**Purpose:** Provide secure RESTful APIs and connector framework for DIPR systems, third-party analytics, and verification services.

**Functional requirements:**

- Publish secure REST APIs for authorized data exchange (campaigns, assets, PoD status, masters as agreed)  
- Integrate with existing DIPR systems identified during requirements (list pending DIPR clarification)  
- Provide connector stubs/provisions for third-party analytics and PoD verification  
- Authentication, authorization, retry, and reconciliation for integrations  
- Sandbox/test support when DIPR provides environments  

**Acceptance criteria:**

- Documented APIs authenticate and authorize correctly  
- At least one DIPR or mock integration path demonstrable in UAT  
- Failures are logged and recoverable per retry policy  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Secure REST API gateway | Authenticated REST APIs for agreed AMT data exchange |
| F09-002 | DIPR system connectors | Connectors for DIPR systems identified in requirements (mapping + auth + retry) |
| F09-003 | Third-party analytics provision | Provisioned connector for third-party analytics when named by DIPR |
| F09-004 | Integration auth, failure & reconciliation | Auth handling, failure queues, retries, and reconciliation reports |

---

### 10. Platform Security & Compliance Controls

**Type:** Technical  
**Slug:** `platform-security-compliance`  
**Purpose:** Implement cross-cutting security, retention, encryption, and compliance controls required by the tender beyond module-local features.

**Functional requirements:**

- Apply secure coding practices and OWASP Top 10 mitigations across the platform  
- Encryption in transit and at rest for sensitive data and media stores  
- Data retention, archival, and disposal policies configurable to DIPR rules  
- Support Government security guideline controls as specified by DIPR  
- Accessibility (WCAG 2.1 AA) and multilingual UI framework support  
- Facilitate VAPT / security testing remediation within engagement  

**Acceptance criteria:**

- Security checklist items agreed in UAT are closed or risk-accepted by DIPR  
- Retention policy behaves as configured on sample data  
- Critical accessibility defects for agreed journeys are remediated  

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | Encryption & secure storage controls | Enforce encryption in transit/at rest for application data and media |
| F10-002 | Data retention & archival policy | Configure and enforce retention/archival/disposal for AMT data |
| F10-003 | Security hardening & OWASP controls | Platform hardening aligned to OWASP Top 10 and DIPR security guidelines |
| F10-004 | Accessibility & multilingual framework | WCAG 2.1 AA enablement and multilingual UI framework for AMT screens |
| F10-005 | VAPT remediation support | Remediate findings from agreed VAPT / security assessment cycles |

---

## 7. End-to-End Workflows

### 7.1 Campaign launch

1. Authorized user creates campaign (media type, schedule, budget, vendors).  
2. Campaign enters embedded approval workflow.  
3. On approval, creatives are uploaded/versioned in asset inventory.  
4. Outdoor sites geotagged as required.  
5. Field PoD tasks generated / assigned to field personnel.  

### 7.2 Field PoD capture

1. Field user receives assignment on mobile.  
2. Captures PoD on site (online or offline).  
3. Data syncs to platform with metadata.  
4. Verifier reviews PoD; accepts, rejects, or requests rework.  
5. Optional third-party verification invoked when configured.  
6. Campaign compliance status updates; reports refresh.  

### 7.3 Reporting & audit

1. Managers open role-based dashboards.  
2. Compliance / spend / KPI reports exported or scheduled.  
3. Audit logs exported for internal review.  

---

## 8. Access Control / RBAC

**Access model (from tender):** **User → Role → Permissions** (RBAC), with optional **SSO** and **MFA**.

Indicative roles (final list confirmed during requirements):

| Role | Typical responsibilities |
| ---- | ------------------------ |
| DIPR Administrator | Users, roles, masters, system parameters |
| Campaign Officer | Create/edit campaigns, submit for approval |
| Approver / Manager | Approve/reject campaigns and escalations |
| Asset Manager | Upload/version assets, geotag outdoor inventory |
| PoD Verifier | Verify PoD evidence; request rework |
| Field Personnel | Mobile tasks, checklists, PoD capture |
| Vendor User (optional) | Limited campaign/assignment visibility if DIPR enables |
| Auditor / Viewer | Read-only dashboards and audit exports |

Org-unit or district scoping may be applied for location-sensitive outdoor campaigns if DIPR requires it during FRS finalization.

---

## 9. Channels

| Channel | Users | Primary functions |
| ------- | ----- | ----------------- |
| Web application | DIPR staff, verifiers, managers, admins | Campaigns, assets, verification, reports, masters, access admin |
| Mobile application (Android/iOS or PWA) | Field personnel | Tasks, checklists, PoD capture, offline sync |
| APIs | DIPR / authorized systems | Data exchange, analytics, verification hooks |

Citizen/public portal is **not** in scope unless DIPR later expands scope.

---

## 10. Integrations

| Integration | Purpose | Status |
| ----------- | ------- | ------ |
| Existing DIPR systems | Data exchange with department systems | List, APIs, auth, formats, and sandbox to be provided by DIPR (pre-bid open item) |
| Identity provider (SSO) | Optional SSO | IdP and protocol (SAML/OIDC/LDAP etc.) to be confirmed |
| Third-party PoD verification | External verification services | Vendor, APIs, credentials, licensing ownership TBD by DIPR |
| Third-party analytics | Analytics interchange | Provisioned; vendor TBD |
| Email gateway | Transactional email notifications | DIPR-provided or approved gateway |
| SMS gateway (optional) | SMS alerts | If DIPR provides gateway/credentials |
| Government hosting / infra | Deployment target | Preferred; specs from DIPR when Government hosting applies |

---

## 11. Audit, Compliance & Security

- Role-wise access logs and operational audit trails  
- OWASP Top 10 mitigations; secure coding  
- Encryption at rest and in transit  
- Data ownership and sovereignty with DIPR; Government hosting preferred  
- DIPR right to audit systems, processes, and records  
- Compliance with applicable Government security guidelines (exact standards to be named by DIPR)  
- NDA / confidentiality obligations per contract  
- IPR: DIPR owns deliverables and data; third-party components declared with valid Government-use licenses  

---

## 12. Non-Functional Requirements

| Area | Requirement |
| ---- | ----------- |
| Availability | ≥ **99.5%** uptime excluding scheduled maintenance |
| Performance | Interactive web/mobile journeys responsive under agreed UAT load (thresholds finalized in test plan) |
| Scalability | Support concurrent DIPR users and field sync bursts for campaign peaks |
| Accessibility | WCAG 2.1 Level AA |
| Language | Multilingual user interfaces |
| Security | MFA, optional SSO, encryption, OWASP controls, VAPT remediation as agreed |
| Offline | Mobile offline capture with reliable sync |
| Support | Critical ≤4h response; High ≤8 business hours; Medium ≤2 business days; Low ≤5 business days |
| Penalty | Technical issues not resolved timely may attract ₹1,000/day as per tender Article 12 (contractual) |

---

## 13. Data Migration

**Default:** Structured **legacy bulk migration is out of scope** unless DIPR provides data extracts and formally includes migration during requirements.

**In scope as baseline:**

- Seed masters (channels, statuses, vendors, locations)  
- Create initial admin users and roles  
- Optional one-time import of limited campaign/asset lists if DIPR supplies clean templates during Week 1–3  

---

## 14. Phased Delivery

Mandatory end-to-end completion within **18 weeks** from work-order acceptance:

| Phase | Weeks | Focus |
| ----- | ----- | ----- |
| Phase 1 | 1–3 | Requirement finalization and prototype delivery |
| Phase 2 | 4–10 | Development of core modules and integration |
| Phase 3 | 11–14 | System testing, bug fixes, UAT |
| Phase 4 | 15–16 | Production deployment (or Government hosting handover) and training |
| Phase 5 | 17–18 | Post-deployment support and stabilization |

Timeline depends on timely DIPR availability of APIs, infrastructure, credentials, test data, decisions, and UAT participation (see Assumptions).

---

## 15. Deliverables

1. Requirements / design documentation and working prototype  
2. Web application (production-ready)  
3. Companion mobile application (Android & iOS or accepted PWA)  
4. Source code, deployment artefacts, and configuration guides (per contract)  
5. Secure APIs and integration connectors as scoped  
6. Test plans, test cases, defect logs, UAT evidence  
7. Security compliance evidence / VAPT remediation records as agreed  
8. User manuals, administrator guides, training sessions, knowledge transfer  
9. Deployment on agreed environment / handover for Government hosting  
10. Post-go-live stabilization support (Weeks 17–18) and contracted maintenance  

---

## 16. Acceptance Criteria (Program Level)

1. Prototype covering major modules demonstrated and accepted in Phase 1.  
2. All Section 6 modules delivered to UAT with traceability to tender technical requirements.  
3. UAT sign-off on functional, performance (agreed thresholds), and security checklist items.  
4. Web + mobile (or accepted PWA) deployed to agreed environment.  
5. Training completed for nominated DIPR users; manuals handed over.  
6. SLA monitoring approach agreed for 99.5% availability measurement.  
7. Open critical/high defects closed or waived in writing by DIPR.  

---

## 17. Expected Benefits

- Single system of record for Government advertisement campaigns across print, digital, and outdoor  
- Faster approvals and clearer vendor/field accountability  
- Geotagged, time-stamped PoD evidence for compliance and audit  
- Management visibility via KPI, spend, and compliance dashboards  
- Secure, role-based, multilingual, accessible platform aligned to Government expectations  

---

## 18. Assumptions & Dependencies

1. **Project code / naming:** Project code **AMT**; output under `Projects/DIPR_AMT/`.  
2. **SOW purpose:** RFP-ready business SOW for estimation and proposal alignment.  
3. **Mobile form factor:** Tender allows Android & iOS **or** PWA; estimate assumes **cross-platform / PWA-capable field app** unless DIPR mandates fully native separate codebases (delta via change request).  
4. **Hosting:** Government hosting preferred; bidder prepares deployment packages and supports handover. Infra sizing and environment access are DIPR dependencies.  
5. **DIPR system list:** Complete list of systems, API specs, auth, formats, and sandbox are pending DIPR clarification; Integration Hub estimated with configurable connector capacity for identified systems.  
6. **SSO:** Optional; IdP/protocol TBD — feature included as optional enablement.  
7. **PoD rules:** GPS accuracy, timestamp source, device metadata, and tamper detection rules finalized in Phase 1; validation engine parameterized accordingly.  
8. **Third-party verification/analytics:** Estimated as provisioned connectors; product licenses and sandbox supplied by DIPR or called out as optional commercial lines.  
9. **KPI definitions:** Mandatory KPIs and calculation rules finalized with DIPR in Phase 1.  
10. **SMS:** Optional pending gateway; email notifications assumed available.  
11. **Access model:** User → Role → Permissions; district/org scoping only if DIPR confirms.  
12. **Document/workflow:** Embedded in Campaign, Asset, and PoD modules — not separate modules.  
13. **Data migration:** No large legacy migration unless added; masters seeded.  
14. **Security standards:** Exact Government guideline names (CERT-In, MeitY, state circulars) to be confirmed by DIPR; OWASP + encryption baseline assumed.  
15. **Availability metric:** Tender states **99.5%** (pre-bid text referenced 99.9% — SOW follows tender 99.5% unless corrigendum).  
16. **18-week plan:** Contingent on DIPR readiness; delay handling per contract / KTPP.  
17. **Tech stack:** Bidder-proposed, subject to tender compliance and DIPR acceptance.  
18. **Pre-bid answers:** Where DIPR has not yet answered Inventech pre-bid queries, this SOW records open items as assumptions rather than inventing DIPR policy.  

---

## 19. Vendor Response Expectations

Vendors should provide (aligned to Annexure-I / II of the tender):

1. Company profile and legal status  
2. Solution architecture, technology stack, data approach, APIs, and integration approach (proposal-level; not a substitute for this SOW’s business scope)  
3. Module-wise functional mapping to this SOW / tender Section II  
4. Prototype / PoC evidence and demonstration schedule  
5. Implementation plan mapped to the 18-week phases  
6. Testing & QA plan; security & compliance approach  
7. Training & documentation plan; team CVs  
8. Commercial proposal: lump-sum development, prototype, hosting/licensing/support (if any), training/KT, optional third-party lines, taxes separated  
9. Eligibility proofs, WCC, financials, Annexure-III / IV declarations as required on e-portal  

---

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User & Access Management | Shared | F01-001 … F01-005 (5) |
| 02 | Master Data & System Configuration | Business | F02-001 … F02-005 (5) |
| 03 | Campaign Management | Business | F03-001 … F03-007 (7) |
| 04 | Creative Asset Inventory | Business | F04-001 … F04-005 (5) |
| 05 | Proof-of-Display Capture & Verification | Business | F05-001 … F05-006 (6) |
| 06 | Mobile Field Application | Business | F06-001 … F06-005 (5) |
| 07 | Reporting & Analytics | Business | F07-001 … F07-006 (6) |
| 08 | Notifications & Alerts | Shared | F08-001 … F08-004 (4) |
| 09 | Integration Hub | Technical | F09-001 … F09-004 (4) |
| 10 | Platform Security & Compliance Controls | Technical | F10-001 … F10-005 (5) |

**Total outline features:** 52

### Appendix B — Tender requirement consolidation map

| Tender Section II item | SOW module(s) |
| ---------------------- | ------------- |
| Campaign Management | 03 |
| Asset Inventory | 04 |
| Proof-of-Display (PoD) | 05, 06 |
| Reporting & Analytics | 07 |
| User & Access Management | 01 |
| APIs & Integrations | 09 |
| Mobile Application | 06 |
| Testing & QA | Delivery process (Section 15–16), not a software module |
| Documentation & Training | Deliverables (Section 15) |
| Security & Compliance | 10 (+ cross-cutting in 01) |

### Appendix C — Source artefacts

| Artefact | Location |
| -------- | -------- |
| Tender PDF | `Projects/DIPR_AMT/Advertisment Monitoring Tool Tender.pdf` |
| Pre-bid queries (Inventech) | `Projects/DIPR_AMT/pre_bid_queries_DIPR_inventech 1.docx` |

### Appendix D — Open clarifications (from pre-bid; pending DIPR)

1. Complete DIPR systems integration list and API/sandbox details  
2. Mandatory PoD validation rules and tamper-detection expectation  
3. Named third-party verification services and license ownership  
4. Offline function set and conflict-resolution rules (baseline assumed in Module 06)  
5. SSO IdP and MFA mechanism specifics  
6. Mandatory KPI dictionary  
7. Exact Government security standards list; VAPT certification expectations  
8. Native vs PWA final preference  
9. Government hosting inventory and constraints  
10. UAT defect-closure thresholds; availability measurement methodology  
11. Data residency, DR, backup, retention specifics beyond DIPR ownership principle  
