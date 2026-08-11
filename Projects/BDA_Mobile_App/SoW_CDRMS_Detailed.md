# Statement of Work (SOW)

# Bangalore Development Authority (BDA)

# Correct Dimension Report Management System (CDRMS)

**Document Type:** Statement of Work – Business Requirements  
**Version:** 1.0  
**Status:** Draft  
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
9. [Channels – Mobile App & Web Application](#9-channels--mobile-app--web-application)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Expected Benefits](#16-expected-benefits)
17. [Assumptions & Dependencies](#17-assumptions--dependencies)
18. [Vendor Response Expectations](#18-vendor-response-expectations)

---



## 1. Introduction

This Statement of Work (SOW) states the **business requirements** for the **Correct Dimension Report Management System (CDRMS)** for the **Bangalore Development Authority (BDA)**. It is prepared as a client requirements document for discussion with implementing vendors / partners.

The solution shall cover:

- Native / cross-platform **mobile application** for BDA field engineers  
- Responsive **web application** for Super Admin and CAO users  
- Backend services, security, notifications, reporting, and documentation  
- Implementation, training, warranty / AMC as agreed with BDA

CDRMS shall digitize the **Correct Dimension Report (CDR)** process used by BDA engineers to capture site dimensions and related site information during field visits, which is then verified by the CAO office. The system shall produce verified CDR / site-visit records and downloadable PDF packs for official use.

**Document handling** (photos, video, PDF generation) and **verification workflow** are embedded in the business process and are not separate product modules.

CDRMS covers engineer geo-bound field capture for CDR (site details, dimensions including odd sites, Check Bandi, directions with width, surroundings per direction, photos/video), CAO verification with PDF, and Super Admin masters, users, and KPIs.

---



## 2. Project Overview

BDA currently relies on field engineers to visit proposed / identified sites, record site details, surroundings, approach roads, and supporting media, and submit the same for administrative verification. These processes are fragmented, difficult to enforce by geography, and lack a controlled digital trail from field capture to CAO verification.

BDA intends to implement CDRMS as a single platform that:

- Allows Super Admin to create and manage **users** (Engineers, CAO, Super Admin) with appropriate access  
- Creates **login credentials for engineers**, each bound to **one geo-location**  
- Enforces that an engineer **cannot capture or submit site details for any location other than the assigned geo-location**  
- Enables engineer mobile access as: download app → **OTP-based login on every login** → enable device location → use the application  
- Captures, during the site visit:
  - **Site details** — identification, dimensions/area (**including odd / irregular site dimensions**), geo stamp  
  - **Check Bandi** — site verification / check-bandi record for the visit  
  - **Directions** — narrative directions + mandatory approach / road **width**  
  - **Surroundings** — what is around the site **at each direction**
- Captures up to **10 photographs** (maximum **10 MB** per photo) and **one video** per site-visit application  
- On submission, routes the application to the **CAO** for verification  
- Allows CAO to verify the application and **download a PDF copy** of the submitted application  
- Provides a **web application** with:
  - **Super Admin** login — masters, users, and application KPIs  
  - **CAO** login — all submitted applications, verification actions, PDF download, and KPIs

### 2.1 Business Context


| Aspect                 | Description                                                                    |
| ---------------------- | ------------------------------------------------------------------------------ |
| Primary users (field)  | BDA engineers conducting site visits                                           |
| Primary users (office) | CAO (verification & PDF), Super Admin (masters, users, KPIs)                   |
| Primary outcome        | Verified site-visit application pack (data + media + PDF)                      |
| Geographic control     | One engineer ↔ one geo-location; cross-location data entry blocked             |
| Access foundation      | Users with roles (Engineer / CAO / Super Admin); engineer geo-location binding |




### 2.2 Guiding Principles

1. Field capture requires **OTP login on every session**, is geo-restricted, and identity-verified before use.
2. Site-visit data and media form a single application record.
3. CAO verification is mandatory before the record is treated as verified / complete.
4. Super Admin manages masters, users, and credentials.
5. KPIs provide operational visibility to Super Admin and CAO.
6. The system is the system of record for site-visit applications and verified PDF packs.

---



## 3. Project Objectives

1. Digitize end-to-end site visit capture by BDA engineers on a mobile application.
2. Enforce geo-location based access so engineers operate only within their assigned location.
3. Enable Super Admin to create and manage users and engineer logins with geo-location assignment.
4. Ensure secure mobile access through **mandatory OTP-based login on every login** and mandatory location enablement.
5. Standardize capture of site details (including **odd / irregular site dimensions**), **Check Bandi**, directions (with width), and surroundings.
6. Support structured media capture (up to 10 photos @ 10 MB each, plus one video).
7. Provide CAO with a complete queue of submitted applications for verification and PDF download.
8. Provide Super Admin with master data, user management, and application KPIs on the web.
9. Create a reliable, auditable digital trail from field visit to CAO-verified application pack.
10. Improve data quality, accountability, and turnaround time for site-visit documentation.

---



## 4. In Scope / Out of Scope



### 4.1 In Scope

**Mobile Application (Engineer)**

- Engineer login and session management.
- **OTP-based login mandatory on every login** (no password-only or OTP-once access).
- Mandatory device location (GPS) enablement to use the app.  
- Geo-location enforcement (engineer restricted to assigned location).  
- Create / edit (before submit) / submit site-visit applications.  
- Capture **site details** (including **odd / irregular site dimensions**), **Check Bandi**, **directions with width**, and **surroundings / what is around the site** as detailed in Module 04.  
- Capture up to 10 photographs (max 10 MB each) and one video per application.  
- View own submitted applications and status.  
- **Online-only** operation.

**Web Application — Super Admin**

- Login and administration console.  
- Master data management (geo-locations, site attribute masters, status lists, configurable parameters).  
- User management for Engineers, CAO, and Super Admin.  
- Creation and management of engineer login credentials with geo-location assignment.  
- Application KPIs and operational dashboards.  
- Search, filter, and export of masters and KPI views (Excel / CSV where applicable).

**Web Application — CAO**

- Login and CAO workbench.  
- View all submitted site-visit applications (with filters by location, engineer, date, status).  
- Open application detail including site data, Check Bandi, directions, surroundings, photos, and video.  
- Verify / approve or return / reject with remarks.  
- Download PDF copy of the submitted (and, where applicable, verified) application.  
- Application KPIs relevant to CAO operations.

**Common / Platform**

- Role-based access for Engineer, CAO, and Super Admin as defined in Section 8.  
- SMS OTP for **every** engineer mobile login (mandatory).  
- Secure media storage and retrieval.  
- PDF generation of site-visit application pack.  
- Audit logging of critical actions.  
- Training, UAT support, go-live support, warranty, and documentation.



### 4.2 Out of Scope

- Hardware procurement (mobile devices, servers, etc.).  
- Citizen / public portal.  
- Payment gateway / fee collection.  
- Integration with other applications, unless added later by change request.

---



## 5. Solution Expectations

Vendors shall propose a solution that meets the following business-level expectations (technology stack remains vendor proposal, subject to BDA / MeitY policy):


| Area           | Expectation                                                                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------- |
| Channels       | Android and iOS mobile apps for engineers; responsive web app for Super Admin and CAO                                |
| Deployment     | Secure cloud (MeitY-empaneled / government-approved) or on-premises / hybrid as specified in RFP                     |
| Access         | Users with roles (Engineer / CAO / Super Admin); engineer bound to one geo-location                                  |
| Geo control    | Each engineer credential bound to exactly one geo-location; server-side enforcement mandatory                        |
| Field capture  | Site ID + dimensions (incl. odd), Check Bandi, directions + **width**, surroundings **per direction**, photos, video |
| Media          | Photos: up to 10 per application, max 10 MB each; Video: one per application with agreed max size                    |
| Verification   | CAO verifies submitted applications; PDF download                                                                    |
| Administration | Super Admin manages masters, users, credentials, and **basic** KPIs                                                  |
| Security       | TLS; **OTP login every engineer session**; role-based access; audit of admin and verification actions                |
| Connectivity   | **Online-only**                                                                                                      |
| Usability      | Simple mobile UX; minimal training                                                                                   |


---



## 6. Consolidated Functional Modules

Requirements are grouped into **seven functional areas** below (for clarity). Each area lists purpose, functional requirements, and key capabilities.

**Document management** (photo / video / PDF) and **CAO verification workflow** are embedded within the relevant modules below.

---



### 01. User & Access Management

**Purpose:** Enable Super Admin to create and manage users and login credentials, assign engineer geo-location, and control access for Engineer, CAO, and Super Admin.

**Functional requirements:**

- Create and manage **users** (name, mobile, email, employee / BDA ID, status).  
- Assign each user a **role**: Engineer, CAO, or Super Admin.  
- Create **login credentials** for engineers, CAO, and Super Admin.  
- Bind each **engineer** to **exactly one geo-location**.  
- Activate, deactivate, and reset credentials as needed.  
- Engineers see only their own applications and may write only within assigned geo-location.  
- CAO and Super Admin access their respective web functions as in Section 8.

#### Key capabilities (feature outline)


| Feature ID | Capability                        | Description                                              |
| ---------- | --------------------------------- | -------------------------------------------------------- |
| F01-001    | User Management                   | Create, update, search, activate/deactivate users.       |
| F01-002    | Role Assignment                   | Assign Engineer / CAO / Super Admin role to users.       |
| F01-003    | Engineer Credential & Geo Binding | Provision engineer login bound to one geo-location.      |
| F01-004    | CAO & Super Admin Credentials     | Provision and manage web logins for CAO and Super Admin. |
| F01-005    | Access Deactivation & Reset       | Deactivate users and support secure credential reset.    |




### 02. Master Data & System Configuration

**Purpose:** Provide configurable masters and system parameters used by mobile capture and web administration / KPIs.

**Functional requirements:**

- **Geo-location master** used for engineer assignment and enforcement.  
- Masters needed for capture fields: site category/type, site shape (regular / odd-irregular), road type, surrounding feature types (per direction), and application status.  
- Other coded lists as finalized with BDA during requirement workshops.  
- Application status master (Draft, Submitted, Returned, Verified, Rejected).  
- Configurable parameters: OTP validity, max photo count (default 10), max photo size (default 10 MB), max video size, session timeout, PDF template versioning metadata.  
- Activate / deactivate masters without breaking historical references.  
- Super Admin maintains masters on the web application.



#### Key capabilities (feature outline)


| Feature ID | Capability                       | Description                                                                 |
| ---------- | -------------------------------- | --------------------------------------------------------------------------- |
| F02-001    | Geo-Location Master              | Maintain the location hierarchy/list used for engineer binding and filters. |
| F02-002    | Site Visit Attribute Masters     | Maintain dropdown / coded values for site capture fields.                   |
| F02-003    | Application Status Configuration | Maintain statuses used in the site-visit lifecycle.                         |
| F02-004    | System Parameters & Media Limits | Configure OTP, media limits, timeouts, and related parameters.              |
| F02-005    | Master Search Filter Export      | Search, filter, and export master lists for administration.                 |


---



### 03. Mobile Onboarding & Geo Enforcement

**Purpose:** Ensure only provisioned engineers can access the mobile app via **OTP-based login on every login**, enable location services, and operate only within the assigned geo-location.

**Functional requirements:**

- Engineer downloads / installs the mobile application (Play Store / App Store or enterprise distribution as decided by BDA).  
- **OTP-based login is mandatory on every login** — each session requires successful OTP validation against the engineer’s registered mobile number; password-only or “remembered / OTP-once” login is not permitted.  
- Login flow: engineer identifies using provisioned credential (e.g. employee ID / registered mobile) → system sends OTP to registered mobile → engineer enters OTP → session established only after OTP success.  
- OTP is single-use, time-bound, and subject to resend cooldown / attempt limits as configured.  
- Logout / session expiry requires a fresh OTP login to regain access.  
- User **must enable device location** (GPS / location services); app shall block core capture functions if location is disabled.  
- Continuously / at key actions validate that the engineer’s current / selected site location falls within the **assigned geo-location**; block save/submit for other locations with a clear error message.  
- Server-side validation of geo-location rules (client checks alone are insufficient).  
- Display engineer profile summary: name, role, assigned geo-location.



#### Key capabilities (feature outline)


| Feature ID | Capability                          | Description                                                                     |
| ---------- | ----------------------------------- | ------------------------------------------------------------------------------- |
| F03-001    | Engineer Mobile Login               | Initiate engineer mobile login using provisioned identity (no OTP-free access). |
| F03-002    | Mandatory OTP Login (Every Session) | Require OTP validation on every login before establishing a session.            |
| F03-003    | Mandatory Location Enablement       | Require device location services to access capture features.                    |
| F03-004    | Assigned Geo-Location Enforcement   | Prevent capture/submit outside the engineer’s assigned geo-location.            |
| F03-005    | Engineer Profile & Assignment View  | Show engineer identity and assigned location on mobile.                         |


---



### 04. Field Site Visit Capture

**Purpose:** Enable engineers to capture complete site-visit applications including structured details, Check Bandi, directions with width, surroundings, photographs, and video.

**Functional requirements:**

**A. Site-visit application header**

- System-generated application number.  
- Engineer identity and assigned geo-location (auto-stamped).  
- Check Bandi date/time (auto or entered as part of Check Bandi section).  
- Capture of device lat-long at key events (open form / submit) where available.

**B. Site details**

The engineer shall capture **site identification**, **dimensions** (including odd/irregular), and link to **direction-wise surroundings** (Section E). Baseline fields (mandatory / optional labels finalized in workshops; masters configurable by Super Admin):

**B.1 Identification & location reference**

- Layout / scheme / project name (where applicable).  
- Survey number(s), site / plot number, block / sector / phase (as applicable).  
- Village / hobli / ward / zone and other administrative location references within the engineer’s assigned geo-location.  
- Postal / local address or landmark-based location description.  
- Khata / property reference number (if available / applicable).  
- Site category / proposed use (e.g., residential, commercial, CA, industrial, mixed — from masters).

**B.2 Site shape and dimensions**

- Site shape — **regular** or **odd / irregular** (from masters).  
- **Regular sites:** length and breadth (with unit).  
- **Odd / irregular sites:** variable number of sides with per-side length and unit; optional side label / facing; optional brief geometry note.  
- Area (with unit — sq.ft / sq.m); optional note if measured and record area differ.  
- Corner site / intermediate site indicator (optional).

**B.3 Geo stamp (device)**

- Latitude and longitude captured from device at form open and/or at submit (mandatory where GPS available).  
- Accuracy / timestamp of geo stamp recorded with the application.

**B.4 Additional remarks**

- Optional short free-text remarks (single field).

**C. Check Bandi**

- Check Bandi date.  
- Check Bandi number (system-generated; optional BDA reference if provided).  
- Engineer and geo-location (auto-stamped).  
- Short remarks (optional).  
- Acknowledgement that Check Bandi was done at site (mandatory at submit).

**D. Directions & approach width**

- Narrative **directions** to the site (from a known landmark / layout entrance).  
- Nearest landmark / road name (optional).  
- Approach / road **width** — **mandatory** numeric value with unit (ft / m).  
- Road type (optional, from master).

**E. Surroundings — each direction**

For **each direction** (North, South, East, West — or Front / Rear / Left / Right as configured):

- What is around that side (type from master + short description).

Optional: one short overall note on surroundings.

**F. Media capture**

- Up to **10 photographs** per application, max **10 MB** each.  
- **One video** per application within configured max size.  
- Preview / replace / delete before submit.

**G. Draft & submit**

- Save draft online (within geo rules).  
- Validate mandatory fields before submit.  
- On submit, lock engineer edit (unless returned by CAO) and place in CAO queue.



#### Key capabilities (feature outline)


| Feature ID | Capability                            | Description                                                                                                       |
| ---------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| F04-001    | Site Visit Application Create & Draft | Create and save draft site-visit applications on mobile.                                                          |
| F04-002    | Site Details Capture                  | Capture site identification, shape, and **regular or odd/irregular multi-side dimensions** (plus area/geo stamp). |
| F04-003    | Check Bandi Capture                   | Capture Check Bandi date, number, acknowledgement (optional remarks).                                             |
| F04-004    | Directions & Width Capture            | Capture narrative directions and mandatory approach/road width.                                                   |
| F04-005    | Surroundings Capture                  | Capture what is around the site at each direction (type + short description).                                     |
| F04-006    | Photo Capture (10 × 10 MB)            | Capture/upload up to 10 photos with per-file size enforcement.                                                    |
| F04-007    | Video Capture                         | Capture/upload one video per application within limits.                                                           |
| F04-008    | Application Validation & Submit       | Validate mandatory data/media and submit to CAO queue.                                                            |
| F04-009    | Engineer Application Status View      | Engineer views own applications and statuses.                                                                     |


---



### 05. CAO Verification & PDF Export

**Purpose:** Provide CAO with a complete workbench to review submitted site-visit applications (including media), verify or return them, and download PDF copies.

**Functional requirements:**

- CAO login on web application.  
- Queue / list of all submitted applications with filters: geo-location, engineer, date range, status, application number.  
- Application detail view: full site details (identification & dimensions), Check Bandi, directions/route & width, side-wise and vicinity surroundings, photos gallery, video playback / download.  
- Actions: **Verify / Approve**, **Return for correction**, **Reject** (final labels confirmed in workshops) with mandatory remarks on return/reject.  
- On return, engineer may edit and resubmit within geo rules.  
- **Download PDF** of the application pack including key site data and photo references / embedded thumbnails as designed.  
- Record verifier identity, date/time, and remarks on the application.  
- Prevent unverified applications from being marked as verified (status control).



#### Key capabilities (feature outline)


| Feature ID | Capability                        | Description                                                    |
| ---------- | --------------------------------- | -------------------------------------------------------------- |
| F05-001    | CAO Application Workbench         | List/search/filter all site-visit applications for CAO.        |
| F05-002    | Application Detail & Media Review | Review full application data, photos, and video.               |
| F05-003    | Verify / Return / Reject Workflow | Perform verification decisions with remarks and status update. |
| F05-004    | PDF Generation & Download         | Generate and download PDF copy of the application.             |
| F05-005    | Resubmission Handling             | Allow returned applications to be corrected and resubmitted.   |


---



### 06. Dashboards, KPIs & MIS

**Purpose:** Provide operational count KPIs for Super Admin and CAO.

**Functional requirements:**

- Super Admin: simple counts — active engineers, applications by status, by geo-location / period.  
- CAO: pending verification count; verified / returned / rejected counts.  
- Date-range and geo-location filters.  
- Excel/CSV export of the count tables.



#### Key capabilities (feature outline)


| Feature ID | Capability             | Description                                               |
| ---------- | ---------------------- | --------------------------------------------------------- |
| F06-001    | Super Admin Basic KPIs | Simple count KPIs for users/applications for Super Admin. |
| F06-002    | CAO Basic KPIs         | Pending and outcome count KPIs for CAO.                   |


---



### 07. Notification Service

**Purpose:** SMS OTP for every engineer login.

**Functional requirements:**

- SMS OTP dispatch for **every engineer mobile login**.  
- Configurable OTP length, expiry, resend cooldown, and max validation attempts.  
- OTP delivery logging for support.



#### Key capabilities (feature outline)


| Feature ID | Capability                    | Description                                            |
| ---------- | ----------------------------- | ------------------------------------------------------ |
| F07-001    | SMS OTP Dispatch & Validation | Send and validate OTP for every engineer mobile login. |


---



## 7. End-to-End Workflows



### 7.1 Engineer Provisioning (Web — Super Admin)

1. Super Admin creates the engineer **user** and assigns role **Engineer**.
2. Super Admin creates engineer **login credentials** and assigns **one geo-location**.
3. Engineer is informed of credentials through BDA’s operational process (SMS/email optional).



### 7.2 Mobile Login (OTP on Every Login)

1. Engineer installs the mobile application (first use).
2. On **every login**, engineer enters provisioned identity (e.g. employee ID / registered mobile).
3. System sends **OTP** to registered mobile; engineer verifies OTP — session starts only after OTP success.
4. Engineer enables **device location** (if not already enabled); app confirms location services are on.
5. Engineer may begin site-visit capture within assigned geo-location.
6. On logout or session expiry, steps 2–3 are repeated (fresh OTP required).



### 7.3 Site Visit Capture & Submission

1. Engineer creates a new site-visit application (geo-location auto-bound).
2. Captures **site details** (ID, regular or **odd/irregular multi-side dimensions**, geo stamp), **Check Bandi**, **directions & mandatory approach width**, and **surroundings at each direction**.
3. Captures up to 10 photos (≤ 10 MB each) and one video.
4. Saves draft as needed; validates and **submits**.
5. Application moves to CAO queue with status **Submitted**.



### 7.4 CAO Verification & PDF Download

1. CAO opens workbench and selects an application.
2. Reviews data and media.
3. **Verifies** (or returns / rejects with remarks).
4. Downloads **PDF** copy of the application.
5. If returned, engineer corrects on mobile and resubmits; cycle repeats.



### 7.5 KPI Monitoring

1. Super Admin monitors overall volumes, user readiness, and location-wise activity.
2. CAO monitors pending verifications and outcomes.

---



## 8. Role-Based Access Control

CDRMS shall support three user roles with the following responsibilities. Detailed access design may be refined later; baseline requirements are:


| Role        | Channel | Primary responsibilities                                                                                                         |
| ----------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Super Admin | Web     | Masters, users, engineer credentials & geo assignment, basic KPIs, system parameters                                             |
| CAO         | Web     | View all applications, verify/return/reject, PDF download, CAO KPIs                                                              |
| Engineer    | Mobile  | OTP login on every session + location enablement; capture/submit site visits within assigned geo-location; view own applications |




### 8.1 Data scoping


| Role        | Data scope                                                                         |
| ----------- | ---------------------------------------------------------------------------------- |
| Engineer    | Own applications only; write only within assigned geo-location                     |
| CAO         | All applications across geo-locations (unless BDA later requests location scoping) |
| Super Admin | Full administrative scope; KPI visibility across the system                        |




### 8.2 Access rules

- Engineer must complete OTP login every session; no access without OTP.  
- No cross-location submit for engineers.  
- CAO verification and PDF download restricted to CAO (and Super Admin if permitted).  
- User creation and geo reassignment restricted to Super Admin.  
- Media and PDF accessible only to authorized users for that application.

---



## 9. Channels – Mobile App & Web Application


| Channel                    | Users       | Capabilities                                                                         |
| -------------------------- | ----------- | ------------------------------------------------------------------------------------ |
| Mobile App (Android & iOS) | Engineers   | OTP login every session, geo-enforced site visit capture, media, submit, status view |
| Web Application            | Super Admin | Masters, users, credentials, KPIs                                                    |
| Web Application            | CAO         | Application workbench, verification, PDF download, KPIs                              |


Citizen / public channel is **not** required.

---



## 10. Integrations


| Integration                    | Purpose                                             | Baseline                                              |
| ------------------------------ | --------------------------------------------------- | ----------------------------------------------------- |
| SMS Gateway                    | OTP on every engineer login + optional workflow SMS | **Required**                                          |
| Email Gateway                  | Optional credential / status mailers                | Optional                                              |
| Map / reverse-geocode provider | Display / assist location awareness                 | Optional (lat-long from device is baseline)           |
| Other BDA application APIs     | Direct hand-off of verified applications            | **Out of scope** (PDF download is baseline); optional |
| Object / media storage         | Store photos and video                              | Required (vendor architecture)                        |


Vendors shall describe gateway assumptions, BDA-provided vs vendor-provided SMS accounts, and indicative throughput.

---



## 11. Audit, Compliance & Security

- Audit trail for: credential create/reset/deactivate, geo assignment changes, application submit, CAO verify/return/reject, PDF download, master changes.  
- Audit fields: who, what, when, before/after where applicable, IP / device metadata where available.  
- Secure storage of media; access only via authorized sessions.  
- Password / credential policy aligned to BDA IT policy.  
- OTP single-use with expiry.  
- Protection against replay of submitted applications and tampering of verified records.  
- Compliance with applicable Government of Karnataka / MeitY security guidelines as stated in RFP.

---



## 12. Non-Functional Requirements


| Area          | Requirement                                                                                                                        |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Platforms     | Mobile: latest major Android & iOS versions N and N-1; Web: Chrome, Edge, Firefox current                                          |
| Performance   | Mobile form save/submit usable on typical 4G field networks; list pages responsive for CAO volumes agreed in sizing                |
| Media         | Enforce 10 photos max, 10 MB max per photo; configurable video max size (default assumption: 50 MB unless BDA specifies otherwise) |
| Scalability   | Support growth in engineers, locations, and applications without redesign                                                          |
| Availability  | Working-hours oriented HA; target availability as defined in RFP NFR annex                                                         |
| RPO / RTO     | As defined in RFP (vendor to propose backup/DR approach)                                                                           |
| Usability     | Minimal-training mobile UX; **English** baseline (Kannada optional)                                                                |
| Accessibility | Practical field usability (large tap targets, clear errors)                                                                        |
| Localization  | Date/time in IST; numeric formats as per BDA                                                                                       |


---



## 13. Data Migration


| Item                              | Scope                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Engineer / user lists             | **In scope** — import from BDA-provided Excel/CSV templates                                                    |
| Historical paper site-visit files | **Out of scope** for bulk digitization; new visits captured digitally                                          |
| Geo-location master               | **In scope** — seed from BDA-provided list                                                                     |
| Active applications at go-live    | Cut-over approach agreed in implementation plan (typically start fresh unless BDA provides structured backlog) |


Vendor shall provide templates, validation reports, and trial migration before go-live.

---



## 14. Phased Delivery


| Phase              | Scope                                                                                                                              | Outcome                                            |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Phase 1            | Modules 01–07 baseline: provisioning, mobile capture with geo enforcement, CAO verification + PDF, Super Admin masters & KPIs, OTP | Production go-live for site-visit → CAO → PDF pack |
| Phase 2 (optional) | As agreed with BDA later                                                                                                           | Extended scope                                     |


Baseline RFP price shall cover **Phase 1**. Phase 2 items shall be quoted as optional line items.

---



## 15. Deliverables

1. Mobile applications (Android and iOS) for engineers.
2. Web application for Super Admin and CAO.
3. Backend services, environments (Dev / UAT / Prod as agreed), and deployment scripts / runbooks.
4. Source code / escrow as per RFP commercial terms.
5. SRS / design artefacts agreed in project plan (business-facing).
6. Admin and user manuals; training materials; training sessions for Super Admin, CAO, and engineers.
7. UAT test packs and UAT support.
8. Go-live support and hypercare as defined in RFP.
9. Warranty and AMC terms as defined in RFP.
10. PDF template for site-visit application pack (CAO download).

---



## 16. Expected Benefits

1. Standardized, geo-controlled field capture by BDA engineers.
2. Faster CAO verification with complete digital application packs.
3. Ready PDF artefacts of verified site-visit applications.
4. Clear accountability via user roles and audit trails.
5. Management visibility through Super Admin and CAO KPIs.
6. Reduced dependency on paper / informal channels for site-visit documentation.

---



## 17. Assumptions & Dependencies

1. BDA will provide the engineer / user list and geo-locations for initial load.
2. Each engineer is assigned to **one** geo-location.
3. SMS gateway for OTP will be arranged as agreed with BDA.
4. Default video size limit is **50 MB** unless BDA specifies otherwise.
5. CAO can view applications across geo-locations.
6. Android and iOS are both required.
7. Application is **online-only**.
8. BDA will nominate Super Admin and CAO users for UAT and production.
9. Devices for engineers are BDA’s responsibility.
10. Hosting (cloud / on-prem / hybrid) will follow BDA instructions.

---



## 18. Vendor Response Expectations

Vendors shall include in their proposal:

1. Understanding of scope and proposed solution approach (mobile + web).
2. Compliance matrix against Section 6 capabilities.
3. Geo-enforcement approach (device + server validation).
4. Media handling approach (compression policy without breaching evidentiary needs, storage, retention).
5. PDF sample/mock of site-visit application pack.
6. Implementation plan, milestones, team profiles.
7. Assumptions and optional Phase 2 items with separate commercials.
8. Security, hosting, backup/DR summary.
9. Training and support plan.
10. Indicative sizing (engineers, applications/month, storage for media).

---

---

**End of Statement of Work**
