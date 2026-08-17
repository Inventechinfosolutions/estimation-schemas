# Statement of Work

# GIS Field Valuation — eValueI / eValueM (KPID / SPLOCA)

**Document type:** Production-grade Statement of Work (RFP discussion and internal estimation)  
**Project code:** EVAL  
**Client / Authority:** Special Officer & Competent Authority (SPLOCA) — IMA and other KPIDFE cases, Government of Karnataka  
**Version:** 1.1  
**Date:** 14 August 2026  
**Status:** Draft for review  

---

## Document control

| Item | Detail |
|------|--------|
| **Purpose** | External RFP discussion **and** internal estimation baseline |
| **Authority statute** | Karnataka Protection of Interest of Depositors in Financial Establishments (KPIDFE) Act, 2004 and connected rules |
| **Source (authoritative)** | (1) Annexure-01 — Main Module: SPLOCA Geo Tagging & Valuation of Immovable Assets (eValueI), including Additional Module QR Coding and Valuation of Movables (eValueM); (2) Proceedings of the meeting dated 10 August 2026 (seized-property valuation, Android field capture, CA assessment, valuer billing, common database, designated server, IP and licensing) |
| **Related SOWs (same programme)** | **Claim Management** and **Legal Management Application** are specified in separate SOWs. This document covers **GIS field valuation (eValueI / eValueM)** only. |
| **Shared component** | **User management / Person–Post–Role access, official identity, OTP before activation, 2FA, joiner–mover–leaver, and forensic/login audit** are already specified in the **Claim Management SOW, Module 01 (F01-001 to F01-007 and F01-010)**. This valuation application **consumes that shared component**. It does **not** rebuild user management. |
| **Existing FE application** | FE dossiers are not rebuilt here. FE / CA identity used on asset and valuer records is consumed as a reference (imported FE identity as used by Claim Management). |
| **Claim-side assets** | Claim Management Module 03 records attached assets, title/e-Khata, valuation e-format summary, auction tracking and recovered funds for **settlement**. This SOW produces the **field GIS valuation** (3(2) through valuer report, CA assessment and valuer bill) and **releases** the accepted pack (F07-007). Auction sale and deposit of proceeds remain in the Claim SOW. |

---

## 1. Introduction

This Statement of Work defines the functional and business scope for a **dedicated GIS field-valuation application** for SPLOCA: a role-based official **web** application for office users and the Competent Authority, and an **Android** application for assigned **Approved Valuers**.

It comprises:

- **eValueI** — geo-tagging and valuation of **immovable** assets (land, building, agricultural land, forests/plantations, mines and quarries), using the Authority’s valuation methods and Forms **V-1 to V-4**.  
- **eValueM** — QR coding, tagging and valuation of **movables** (equipment, furniture, machinery, gemstones/jewellery, art and handicrafts), using Forms **V-6 to V-8**, plus cash and foreign-currency handover recording as directed in the 10 August 2026 proceedings.

It is **not** an extension of the existing public website. It is **not** a rebuild of Claim Management, Legal Management, or the existing FE application.

**Person, Post, Role, official identity, OTP, 2FA and credential lifecycle are not specified again in this SOW.** Office users, approved valuers, contract staff used on valuation work, and other valuation users are provisioned on the **shared user-management component** already defined in the Claim Management SOW, Module 01. This SOW adds only valuation-specific access (assignment of assets to a valuer Person, need-to-know on asset photographs and reports, Android authentication against that same identity).

This SOW does not prescribe APIs, database schemas, UI wireframes, or effort hours.

---

## 2. Project Overview

### 2.1 Business context

After KPIDFE invocation, SPLOCA must value seized and attached property so the Competent Authority can assess reports, select photographs for auction display, and pay approved valuers. Annexure-01 and the 10 August 2026 proceedings require a production web application plus a valuation Android application: office users create the 3(2) asset record, code and categorise it, link location, address and photograph; approved valuers are registered and assigned; valuers inspect in the field with GIS-tagged photographs, video and live location; method-specific valuation is entered; the CA assesses the report; a bill and voucher follow only after CA acceptance.

### 2.2 Solution character

| Characteristic | Requirement |
|----------------|-------------|
| **Nature** | Dedicated official valuation **web** + **Android** (valuers) for geo-tagged immovable and QR-tagged movable valuation |
| **Not** | A public portal; a rebuild of Claim Management, Legal Management or user management; a generative-AI valuation product |
| **Access** | **Shared** Person–Post–Role identity from Claim Management Module 01 |
| **AI policy** | Generative AI shall **not** be used. Agentic / rule-based assists only, with human verification and audit |
| **Common data** | Claims, legal, property/valuation, static masters interconnect so authorised users open linked FE / asset / valuation information without duplicate entry, subject to RBAC |
| **IP** | For in-house applications and software delivered under this engagement, intellectual property and source code shall **solely lie with SPLOCA** |
| **Hosting** | Designated server / approved cloud; Android distribution and Play Store licensing where specifically approved — licensing shall be clear, not speculative |
| **FRS platform note** | Annexure-01 names **PHP** and a **secure geocoding** capability (address ↔ coordinates / Place ID; reverse geocoding to a readable address) available on host PC and Android. This SOW treats that as a **source constraint**, not a licence to design interfaces |

### 2.3 Primary users (indicative)

| User | Typical work |
|------|----------------|
| **Office user / Officer** | Create 3(2) asset; enter office-side particulars; upload court order and sale deeds; assign valuer; search and update rights / physical status; upload CAD / layout |
| **Approved Valuer** | Receive assignment; inspect site; capture GIS photos/video/location; complete method-specific valuation and statutory form; declare personal inspection and no interest |
| **Competent Authority** | Assess valuer report on key parameters; accept / reject / order revaluation / issue SCN; select auction-display photos |
| **Administrators** | Consume shared Person/Post provisioning; maintain valuer **master** (rates, category, order — not a second login directory); Android enrolment against shared identity |
| **Billing officer** | Prepare valuer bill and voucher after CA acceptance; submit online; upload signed hard copy |

---

## 3. Project Objectives

1. Deliver a **dedicated valuation web application** (not a public portal) for seized and attached property.
   - Begin with the **3(2)** asset record; code and categorise; link location, address and photograph; maintain rights and physical status through field valuation.

2. Consume **shared user management** from Claim Management Module 01.
   - Person, Post, Role-to-Post, Post-to-Person, official identity, OTP before activation, 2FA, no credential sharing, forensic/login audit — **refer to Claim Management SOW; do not rebuild**.
   - Add valuation-specific Posts (Office user, Approved Valuer, CA as used here) **configured on** that component, plus Android authentication on that identity.

3. Register **approved valuers** (professional master: category, order, rates, incidental costs) and **assign** assets for valuation.

4. Enable the **assigned valuer** to retrieve office-entered asset data, view uploaded sale deeds and court orders, obtain remaining particulars from **approved secure sources**, and complete field capture.
   - Photographs (minimum four, each at least 5 MB) with GIS tag and **date on the photo**; video; valuer real-time location; system date and time.

5. Support **immovable valuation methods** and statutory Forms **V-1 to V-4** (cost of construction, comparable sales, floor weightage, land-and-building with adjustment factors and depreciation).

6. Support **eValueM** movable coding, QR / sticker tagging, tabulation, Forms **V-6 to V-8**, and **cash / foreign currency** handover (quantity, value, damage) with the damaged-note replacement application to RBI as specified in the proceedings.

7. Provide **CA assessment** of the valuer report (time taken, asset category, method, adjustment factors, Section 7(1) valuation, guidance value), including accept / reject / revaluation / SCN, and selection of photographs for auction display.

8. Prepare the **valuer’s bill and voucher** only after CA acceptance; submit online and file the signed hard copy.

9. Deliver the **Valuation Android application** for assigned valuers, with clear distribution / Play Store licensing where approved, and IP vested in SPLOCA.

10. Deploy on the **designated server**, with HTTPS/SSL, AES-256, instant backup, and a **common database** with claims and other programme modules.

---

## 4. In Scope / Out of Scope

### 4.1 In scope

| Area | Included |
|------|----------|
| **Channels** | Secure **staff web**; **Android** for assigned Approved Valuers; anytime-anywhere official access via browser / Android |
| **Shared access (consumed)** | Claim Management SOW Module 01 (F01-001 to F01-007, F01-010): Person, Post, Role mapping, official identity, OTP, 2FA, joiner–mover–leaver, forensic/login audit. Valuation users (office, valuer, CA) are Persons/Posts on that component |
| **Valuation-specific access** | Asset-to-valuer assignment; need-to-know on photographs, sale deeds, court orders and reports; Android login against the same identity |
| **eValueI — immovable** | 3(2) asset register; office-entered particulars; GIS field inspection; valuation methods; Forms V-1, V-2, V-3, V-4; specification proforma; CAD / layout upload |
| **eValueM — movable** | Category/sub-code catalogue; QR / sticker tagging; tabulation; group and sample photographs; Forms V-6, V-7, V-8 |
| **Cash / FCY** | Quantity, value, damage at handover; application to replace damaged notes to RBI in the appropriate format |
| **CA assessment & MIS** | Reports from valuer-entered data; key-parameter assessment; auction-display photo selection; accept / reject / revaluation / SCN |
| **Valuer billing** | Bill and voucher from approved particulars after CA acceptance |
| **Geocoding (business)** | Convert address to coordinates / Place ID for map markers; reverse geocoding to a readable address; nearby civic-amenity distances; Map link and QR of the link |
| **Cross-cutting** | Common database with claims and other programme modules; unique seized-property code with Google location; central static/master data; geocoding/reverse geocoding; per-module access, security, backup awareness, **in-app training/FAQ (F01-005)**; designated server |
| **Document handling & workflow** | **Embedded** in valuation processes (not a separate DMS product) |

### 4.2 Out of scope

| Area | Excluded |
|------|----------|
| **User management rebuild** | Re-specifying or re-building Person, Post, Role, 2FA, OTP-before-activation, official identity or credential lifecycle. **Use Claim Management SOW Module 01**. Proceedings item 13 credentials for officers, contract staff, security guards and valuers are **that shared component**, not a second directory in this application |
| **Claim settlement** | Notification, intake, verification, approval, settlement, payment, **auction sale and recovered-fund deposit** — Claim Management SOW (this SOW supplies accepted valuation and auction-display photographs) |
| **Legal Management** | Matters, library, templates, advocate Android — separate SOW |
| **FE Management dossier** | Already in the existing FE application; not rebuilt here. Unique **FE** code (FE number, type, tri-lateral index) is not created in this SOW; unique **seized-property** code with Google location **is** in this SOW |
| **Office IT inventory / maintenance tickets** | Proceedings item 13 sub-module for IT hardware, software, web apps and other office machinery is **not** in Annexure-01 and is **not** this product |
| **Form V-5** | Not present in the source FRS; excluded unless the Authority supplies the form |
| **Generative AI** | Any generative AI for unsupervised valuation, comparable-sale invention or report drafting |
| **Public portal rebuild** | Existing public website is not the target |
| **Market intelligence and investigation process** | Excluded |
| **Hardware / hosting AMC** | Beyond designated-server deployment and runbooks, unless separately ordered |

### 4.3 Clarifying boundary — Shared user management

Office users, approved valuers and other valuation users **log in as Persons mapped to Posts** created in the shared component. An Administrator does **not** maintain a second user directory inside eValueI / eValueM.

This SOW estimates only:

- wiring valuation web and Android to that shared identity;  
- asset-to-valuer assignment and need-to-know on valuation documents;  
- Valuation-specific Posts/Roles **configured on** the shared component (for example Office user, Approved Valuer, Competent Authority as used here), not a second identity product;  
- the **Approved Valuer professional master** (category, order number, rates of valuation and incidental costs) as **business master data**, distinct from login credentials.

### 4.4 Clarifying boundary — Claim Module 03 vs this SOW

| Claim Management Module 03 | This SOW |
|----------------------------|----------|
| Attached-asset register for **settlement** | 3(2) / GIS valuation asset record for **field valuation** |
| Valuation **e-format summary** from the valuation manual | Full method-specific valuation and statutory Forms V-1–V-4 / V-6–V-8 |
| **Auction tracking** and recovered amount | CA selects photographs **for auction display** and **releases** the accepted pack (F07-007); does not run the auction |
| Title / e-Khata / dues for recovery | Rights and physical status as needed for valuation; not the Khata/dues workflow |

Authorised users shall open the linked record through the **common database**, without re-keying FE identity.

---

## 5. Solution Expectations (business-level)

1. **One identity:** Valuation, Claims and Legal share Person–Post–Role; no second login directory.  
2. **Office first, valuer second:** The valuer cannot invent the asset. Selecting an assigned asset **displays** office-entered basics; the valuer completes the remainder.  
3. **Field truth:** Photographs carry GIS tag and date; video and the valuer’s real-time location are stored with system date and time.  
4. **Method then form:** The valuer selects format and method; statutory Form V-1–V-4 or V-6–V-8 is completed from that work; the valuer declares personal inspection and no interest.  
5. **CA gate:** Billing opens only after CA acceptance. Reject / revaluation / SCN are recorded on the same report.  
6. **No generative AI:** Comparables, adjustment factors and narrative are entered or selected by the valuer, then human-verified.  
7. **Common data:** FE / CA / asset identity is not typed twice across programme applications.

---

## 6. Consolidated Functional Modules

Document handling and workflow are **embedded**. Module numbers and feature IDs are **authoritative** for downstream estimation.

---

### 01. Shared User & Access Control (consumed)

**Purpose:** Use the Person–Post–Role, official identity, OTP, 2FA, joiner–mover–leaver and forensic/login audit **already specified in the Claim Management SOW, Module 01 (F01-001 to F01-007 and F01-010)**. Add only valuation-specific assignment visibility, document rights and Android authentication.

**Type:** Shared  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Claim Management SOW | Module 01 F01-001–F01-007, F01-010 (shared component — **do not rebuild**) |
| Annexure-01 | User–Admin login; MIS Admin “create/update/delete valuer/asset/**officer user login**” — **login** portion is the shared component; asset/valuer **masters** are Modules 02–03 |
| Proceedings 10-08-2026 | Items 1 (role-based web+Android), 13 (credentials on shared component), 18 (RBAC on common DB), 23 (per-module access, training and FAQ) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Shared identity | Valuation web and Android shall authenticate against the **same Person–Post–Role store** as Claim Management. Person create/update, Post, Role-to-Post, Post-to-Person, official identity, OTP before activation, 2FA and deactivation **shall not be re-implemented** here. |
| 2 | Valuation Posts | Office user, Approved Valuer, Competent Authority (and other Posts the Authority names, including contract staff / security guards **as Persons**) shall be configured **on the shared component**. |
| 3 | Assignment visibility | A valuer shall see only assets **assigned** to that Person (plus any CA/office override the Authority defines). |
| 4 | Valuation document rights | View / download of sale deeds, court orders, photographs, CAD and valuation reports shall follow Post and assignment. |
| 5 | Android session | Valuation Android shall use the same identity; disabling a Person shall block new web and Android sessions. |
| 6 | Training / FAQ | Each valuation module shall expose in-application training and FAQ for the Posts that use it (Proceedings item 23). |

##### Entity fields — Valuation access (additional to shared Person/Post)

| Field | Notes |
|-------|-------|
| Valuation Post | Office user / Approved Valuer / CA / other as configured on shared component |
| Assigned assets | Assets this valuer Person may open |
| Document rights | View / download of valuation pack |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A valuation user logs in with the shared Person account; there is no second user master in eValueI / eValueM. |
| 2 | A valuer cannot open an asset that is not assigned to that Person (unless a CA/office override applies). |
| 3 | Disabling the Person on the shared component blocks valuation web and Android immediately. |
| 4 | Claim Management F01-001–F01-007 and F01-010 are not duplicated as new valuation features except the valuation-specific items below. |
| 5 | An authorised user can open in-app training/FAQ for the valuation module they are using. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Consume shared Person–Post–Role identity | An Administrator provisions office users and approved valuers **in the shared user-management component** (Claim Management SOW Module 01: F01-001 Person, F01-002 Post/Role mapping, F01-004 official identity, F01-005 OTP before activation, F01-006 2FA, F01-007 joiner–mover–leaver, F01-010 audit). The Valuation Administrator does **not** create a parallel user directory. A valuer then logs into valuation web with that Person. If the Person is deactivated on the shared component, valuation login fails. |
| F01-002 | Valuation Posts on the shared component | An Administrator configures Posts such as Office user, Approved Valuer and Competent Authority **on the shared component** and maps Persons. A contract staff or security-guard Person used on a valuation site is likewise a shared Person, not a local account. Changing the Post mapping changes which valuation menus the Person sees on next login. |
| F01-003 | Assignment and need-to-know on valuation documents | An Officer assigns an asset to a valuer Person. That valuer opens sale deeds, court orders, photographs and the report for **that** asset. Another valuer not assigned cannot open those files. The system records who viewed or downloaded which valuation document and when. |
| F01-004 | Valuation web and Android on shared identity | An Office user or Approved Valuer signs in on web or Android with the same Person credentials and 2FA as the shared component. After login they see only valuation menus allowed for their Post. Signing out or deactivation ends both channels. |
| F01-005 | In-app training and FAQ for valuation | An Office user, Approved Valuer or CA opens Help / FAQ on the valuation web or Android and reads the topic for the module they are in (for example assignment, GIS capture, Form V-1, billing). The Administrator maintains those topics. This is not a second identity product and not classroom scheduling unless separately ordered. |

---

### 02. Valuation Masters, Property Coding & References

**Purpose:** Maintain approved-valuer **professional** masters (not logins), asset and movable category catalogues, unique seized-property codes with Google location, and FE/CA references consumed from the programme — plus central static/master data for valuation modules.

**Type:** Shared  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Valuer Details (name, code, category, order, rates, incidental costs); asset categories; eValueM category/sub-codes; Software (geocoding / reverse geocoding / map markers); certified classification of structures for depreciation |
| Proceedings 10-08-2026 | Items 7–8 (central master/static data), 9 (register approved valuers; code and categorise), 22 (unique code per seized property with Google location — **not** FE coding), 23 (per-module masters) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Valuer professional master | Office user shall maintain Approved Valuer name, Valuer Code, Category, Order Number, Rates of Valuation and Incidental Costs. This is **not** the login record. |
| 2 | Link to Person | Each active valuer master shall be linked to the shared Person who will log in as that valuer. |
| 3 | Immovable categories | Land, Property, Building, Lease Holding, Other (as in the FRS), extendable by the Authority. |
| 4 | Movable codes | Category, sub-code, object code and detail code as in Annexure-01 (AC, PCP, EEG, FF, MTP, TXT, VEH, ANC and listed children). |
| 5 | Unique property code | Each seized property shall receive a unique code **with Google location**, distinct from the FE unique code which remains in the existing FE application. |
| 6 | FE / CA reference | FE name/code and CA name/code on asset and valuer records shall be selected from programme references (Claim import / existing FE application), not re-typed as a new dossier. |
| 7 | Structure classification | Maintain the certified classification of structures (specification, expected economic life, residual/scrap) used in cost-of-construction depreciation. |
| 8 | Geocoding | Convert address to coordinates / Place ID for map markers; reverse geocode coordinates / Place ID to a readable address; available on web and Android. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An Officer can register an approved valuer’s rates and order without creating a second login; login remains the linked shared Person. |
| 2 | A new seized property receives a unique code that includes / is bound to its Google location. |
| 3 | Movable items can be classified using the Annexure-01 code tree. |
| 4 | FE/CA on an asset is a selection from the shared programme reference, not a free duplicate dossier. |
| 5 | Depreciation in F05-002 / F05-005 uses a structure class from the maintained master (F02-007). |
| 6 | Entering an address yields coordinates (or Place ID) and a map marker; capturing coordinates yields a readable address. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Approved valuer professional master | An Office user opens Valuer master and records Approved Valuer name, Valuer Code, Category, Order Number, Rates of Valuation and Incidental Costs. The user links that master to the shared Person who will log in. Another Officer can later search by Valuer Code and see current rates. Deactivating the master stops new assignments; it does not invent a second password store. |
| F02-002 | Immovable asset category master | An Administrator maintains categories Land, Property, Building, Lease Holding and Other. An Officer creating an asset must select a category from this list. Adding a category the Authority names makes it available on the next asset create, without a code change request for that list alone. |
| F02-003 | Unique seized-property code with Google location | When an Officer saves a new seized property, the system issues a unique property code bound to that property’s Google location. A later search by that code opens the same asset. This code is not the FE unique code (FE number, type, tri-lateral index), which stays in the existing FE application. |
| F02-004 | Movable category and sub-code catalogue | An Administrator (or seeded catalogue) maintains the eValueM tree (for example AC-SPL, PCP-DT, VEH-CR-SUV). An Officer or valuer classifying a movable must pick from that tree so QR/sticker codes stay consistent across seizures. |
| F02-005 | FE and CA identity reference | On an asset or assignment, the Officer selects FE name/code and CA name/code from the programme reference used by Claim Management (imported FE identity). The Officer cannot create a new FE dossier here. Later valuation reports show the same FE/CA labels as claims. |
| F02-006 | Central static masters for valuation | An Administrator maintains static lists used across valuation (for example locality classification HIG/MIG/LIG, zone types, condition grades New/Unused/Working/Damaged/Scrap/Obsolete). Office and valuer screens consume those lists so spelling does not fragment reports. |
| F02-007 | Certified structure-classification master | An Administrator maintains the certified classification of structures: specification class, expected economic life, and residual/scrap (typically 10% unless the Authority records otherwise). When a Valuer runs cost-of-construction or land-and-building depreciation (F05-002, F05-005), the valuer **selects a class from this master**; they do not type a one-off life unless an override with reason is recorded. |
| F02-008 | Geocoding, reverse geocoding and map markers | An Office user entering an asset address (F03-001) obtains latitude/longitude or a Place ID and sees a marker on the map. A Valuer capturing live GIS (F04-007) obtains a human-readable address stored beside those coordinates. The same behaviour is available on web and Android. This SOW does not specify interface contracts. |

---

### 03. Immovable Asset Register (3(2) & Office Capture)

**Purpose:** Let the office user create the seized/attached **immovable** asset on the web, enter basic and document particulars, prepare 3(2), attach court order and sale deeds, record IO / 7(1) / guidance values as known to the office, search and update rights and physical status, and upload CAD / layout — before any valuer field work.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | User–Admin asset create; Asset Details (boundaries, measure, registration, parties, stamp duty, category, uploads) |
| Proceedings 10-08-2026 | Item 9 (create asset, 3(2), code, categorise, location/address/photo, search by FE/address/keywords, update rights and physical status); item 12 (digital layout/CAD) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Office create | Office user shall enter: Office user ID/Name/Designation/Mobile (from shared Person), allotted FE name and code, CA name and code, Asset Description, Asset Location, Latitude & Longitude, Date of Attachment, Date of Absolute, Court Order, IO Valuation, Section 7(1) Valuation, Guidance / Market Value. |
| 2 | Asset details | ID, Asset Name, Type, details, Address, Boundaries (N/S/E/W as per document), Asset Measure, Asset Registration Date, Parties, Stamp Duty Paid & Registration Fee, category. |
| 3 | Uploads | Court order (number and details with file); sale deeds (with file). |
| 4 | 3(2) and coding | 3(2) prepared; property coded (Module 02) and categorised; location, address and photograph linked. |
| 5 | Search and status | Search by FE name, address and other keywords; update records of rights and physical status. |
| 6 | CAD / layout | Authorised officers shall upload a digital layout / CAD drawing for maintenance and security use. |
| 7 | Allotted FE | An Office user shall create and search immovable assets only for FEs **allotted** to that Person/Post, unless a CA/admin override applies. |
| 8 | Asset deactivate | Authorised admin/office shall deactivate or delete an asset record with history; login delete remains on the shared component. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An Officer can create an immovable asset with FE/CA, location and attachment dates and save a 3(2)-ready record. |
| 2 | Court order and sale deeds uploaded by the office are the files the valuer later opens with View. |
| 3 | Search by FE name or address returns the same asset. |
| 4 | CAD/layout is stored on the asset and available to authorised officers. |
| 5 | An Office user without allotment to an FE cannot create an asset for that FE. |
| 6 | A deactivated asset is not offered for new valuer assignment. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Create immovable asset (office web) | An Office user logs in, opens Asset create, selects an **allotted** FE (F03-008) and CA from programme references, and enters asset description, location, latitude and longitude (or obtains them from the address via F02-008), dates of attachment and absolute, court-order reference, IO valuation, Section 7(1) valuation and guidance/market value as known to the office. The user saves. Another Officer allotted to that FE can open the same asset by identification and see those office-entered fields. |
| F03-002 | Asset particulars, boundaries and registration | On that asset, the Officer records name, type, address, document boundaries (North, South, East, West), measure, registration date, parties, stamp duty paid and registration fee, and category (Land, Property, Building, Lease Holding, Other). Saving updates the record the valuer will later see as “basic details”. |
| F03-003 | Upload court order and sale deeds | The Officer uploads the court-order file and sale-deed files against the asset, with court-order number and details. A later valuer uses View (F04-003) to open **these** files; replacing a file is an auditable office action. |
| F03-004 | 3(2) preparation, photograph and office location link | The Officer marks 3(2) prepared, confirms the unique property code (F02-003), links the office photograph and address/location, and saves. The asset is then eligible for valuer assignment. An asset without 3(2) prepared is not offered in the valuer assignment list unless the Authority defines an exception. |
| F03-005 | Search and update rights / physical status | An Officer searches by FE name, address or keyword **within allotted FEs**, opens the asset, and updates rights and physical status. The system appends history (who, when, previous status, new status). A later CA assessment still shows the current physical status. |
| F03-006 | CAD / layout upload for maintenance and security | An authorised Officer uploads a dimensioned site plan or CAD / digital layout to the asset. Another authorised officer opens it for maintenance and security. The file remains with the asset for CA and field use; this is not a separate drawing product. |
| F03-007 | Link to Claim attached-asset record | Where the common database already has a Claim Module 03 attached-asset row for the same property, the Officer links this valuation asset to that row (select existing, do not re-type). Claim settlement continues to own auction tracking and recovered funds; this record owns GIS field valuation. |
| F03-008 | Allotted-FE scope for the office user | An Administrator (on the shared component / valuation allotment) maps which FEs an Office user Person may work. That Officer’s Asset create and search list only those FEs. Attempting to save an asset against a non-allotted FE is refused. A CA or named admin override can open any FE. |
| F03-009 | Deactivate or delete asset | An authorised Office user or Administrator opens an asset and deactivates it (or deletes if the Authority permits hard delete), with reason. The action is history-logged. A deactivated asset cannot be newly assigned (F04-001). Officer **login** create/update/delete remains Claim Management Module 01, not this feature. |

---

### 04. Valuer Assignment & GIS Field Capture (Data Capturing – I)

**Purpose:** Assign an approved valuer to a property; on selection, display office-entered basics; let the valuer complete the **Preliminary Site Inspection Report** with GIS-tagged media, nearby amenities, Map link/QR, live location and remarks — mining remaining data from the web application and approved secure sources.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Valuer Details assignment **and valuer-entered visit/stage/allotted names**; Data Capturing – I (mined data) Preliminary Site Inspection Report (a–k); Form V-1 proximity tables |
| Proceedings 10-08-2026 | Items 9 (assign assets), 10 (retrieve assigned data; approved secure sources; method-specific remaining particulars), 11 (GIS photos, video, real-time location, system date/time) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Assignment | Office user shall record Assignment Number, Assignment Date and Assigned Property Details against the valuer master / Person. |
| 2 | Select assigned asset | Valuer shall select from a dropdown of assets **already created and assigned**; unassigned assets shall not appear. |
| 3 | Display basics | On select: Asset Name, Details, Address, Asset Measure, Asset Registration number; CA Name, Designation, Mobile, Office Address; FE Name & Code. |
| 4 | View deeds/orders | Sale deeds and court order shall open when the valuer clicks View. |
| 5 | Location pack | Asset no, address, width of approach road, type of road, landmark, surrounding area, boundaries N/S/E/W. |
| 6 | Amenities | Distances to school/college, hospital, malls, temples/mosque/church, police station, bus stand, railway station, airport, **and Form V-1 rows: offices, markets, cinemas/malls, auto/taxi, metro** shall be **fetched automatically**. |
| 7 | Map | Google Map link and QR code of the link; map marker from geocoding (F02-008). |
| 8 | Media | Minimum **four** photographs, each at least **5 MB**, with GIS tag (geocoding) and **date on the photo**; photo/video upload; captured date and time. |
| 9 | Valuer GIS | Capture the valuer’s real-time GIS with system date and time; reverse-geocode to a readable address (F02-008). |
| 10 | Remarks | Negative factors affecting the property; overall observation by valuer. |
| 11 | Visit / stage / team | Valuer (or office) shall record Date of Visit, Stage of Valuation, Valuer Names Allotted and their mobile numbers. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A valuer dropdown lists only assets assigned to that valuer Person. |
| 2 | Selecting an asset shows office-entered basics without re-entry. |
| 3 | View opens the office-uploaded sale deed / court order. |
| 4 | Four GIS-tagged, dated photographs of at least 5 MB each can be stored with captured date/time and valuer live location. |
| 5 | Nearby amenity distances (including V-1 civic/transport rows) and Map link/QR are present on the inspection report. |
| 6 | Date of Visit, Stage of Valuation and allotted valuer names/mobiles are stored on the assignment. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Assign asset to approved valuer | An Office user opens an eligible 3(2) asset, selects an Approved Valuer from the professional master, and records Assignment Number, Assignment Date and assigned property details. Additional allotted names/mobiles are recorded in F04-008. The linked valuer Person then sees that asset in their assigned list. The Officer can reassign; the previous valuer loses the asset on the next open unless the Authority keeps a read-only history copy. |
| F04-002 | Display office-entered basics to the assigned valuer | The Valuer opens the application, selects the assigned asset from the dropdown. The page shows Asset Name, Details, Address, Asset Measure, Asset Registration number, CA Name, Designation, Mobile, Office Address, and FE Name & Code **as entered by the office**. The valuer cannot blank those office fields; remaining valuation fields are entered later (Module 05). |
| F04-003 | View sale deeds and court order | On the selected asset, the Valuer clicks View on sale deeds or court order and sees the files the office uploaded (F03-003). If no file was uploaded, View states that and the valuer records the gap in remarks rather than inventing a document. |
| F04-004 | Preliminary site inspection — location and boundaries | The Valuer records or confirms location of asset (asset no, address, width and type of approach road, landmark, surrounding area) and boundaries North, South, East and West. Saving stores this as the Preliminary Site Inspection location pack with the valuer’s identity and time. |
| F04-005 | Nearby amenities, Map link and QR | When the Valuer is on the inspection page, the application fetches distances for that location to: school/college, hospital, malls, places of worship, police station, bus stand, railway station, airport, **offices, markets, cinemas, auto/taxi and metro** (Form V-1 items 10–11 plus Data Capturing – I). It shows a Map link, a QR code of that link, and a map marker (F02-008). The valuer can proceed only when those auto-fetched fields are populated or an authorised exception (fetch failed) is recorded. |
| F04-006 | GIS-tagged photographs and video | The Valuer captures at least four photographs, each at least 5 MB, with GIS tag and the **date printed on the photograph**, and may upload video. Each item stores captured date and time. A submission with fewer than four qualifying photographs is rejected until the valuer adds them. |
| F04-007 | Valuer live location, negative factors, remarks and approved sources | While inspecting, the application captures the valuer’s real-time GIS with system date and time and **reverse-geocodes it to a readable address** stored beside the coordinates (F02-008). The Valuer enters negative factors affecting the property and overall observation. The Valuer may retrieve remaining particulars from **approved secure sources** named by the Authority; the system records which source was used. Generative AI shall not invent site remarks. |
| F04-008 | Visit date, allotted valuer team and stage of valuation | The assigned Valuer (or Office user) records **Date of Visit**, **Valuer Names Allotted** with mobile numbers (team on this assignment, not a second login directory), and **Stage of Valuation** (for example assigned / visited / inspection complete / analytical in progress / submitted to CA / revaluation). Changing stage appends history (who, when, previous, new). CA Time Taken (F07-006) uses visit date and later submit time from this record. |

---

### 05. Immovable Valuation Methods & Statutory Forms (Data Capturing – II)

**Purpose:** Let the assigned valuer select valuation format and method, populate the asset by its code, enter analytical data (cost of construction, comparables, floor weightage, land-and-building with adjustment factors and depreciation), complete the specification proforma, and issue Forms **V-1 to V-4** with declaration — tagging photos/videos into the report library.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Data Capturing – II; Valuation Formats I–II and Land and Building Method; Reporting Formats / specification proforma; Forms V-1, V-2, V-3, V-4 |
| Proceedings 10-08-2026 | Item 10 (method-specific remaining particulars); item 16 (no generative AI) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Method entry | Valuer shall select valuation format and method, enter the asset code to populate basics, enter method data, and upload pictures/videos into the library. |
| 2 | Cost of construction | Accounts method (materials, labour, start/completion, depreciation by certified structure classification, likely market value, certificate of accounts) and comparable method for built-up properties (flats/shops/offices table; adjustment factors including location, situation, area, floor, specifications, facilities, time-gap, status, building area, floor disposition). |
| 3 | Floor weightage | Apply the FRS floor-disposition table for FMV of residential flat / commercial premises, with the metropolitan reverse-trend note for Bangalore as a **careful local decision**, not a hidden default. |
| 4 | Land and building | Applicability tests; derived land value; comparable sales (min. 3; order of preference); adjustment/influence factors as tabulated in the FRS (location, time-gap/NPV, shape, size, FAR, side open, co-ownership, tenure, encumbrance, unearned increase, other depressing effects); building reproduction minus depreciation; builder’s efforts @ 3% of B; formulae for Le, straight-line depreciation and Q as in the FRS. |
| 5 | Specification proforma | Foundation through facilities as in the FRS reporting format (residential / non-residential). |
| 6 | Form V-1 | Full immovable (other than agri/plantations/forests/mines) report including general, land, building, rents, sales, cost of construction, Part II approach, Part III declaration and sub-annexure technical details. |
| 7 | Forms V-2, V-3, V-4 | Agricultural land; forests & plantations; mines and quarries — fields as in the FRS, with declaration of personal inspection and no interest. |
| 8 | Expert Valuer and digital sign | Optional Expert Valuer on the assignment; Registered Valuer (and Expert if any) digitally sign the declaration on V-1 to V-8. |

**Business rule:** Adjustment percentages and depreciation formulae in the FRS are **default calculation rules** the valuer applies or overrides with recorded reason. They are not unsupervised AI.

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Entering the asset code populates office-entered basics into the chosen valuation format. |
| 2 | A land-and-building valuation can be completed with at least three sale instances or a recorded basis where instances are absent (Form V-1 item 34). |
| 3 | Form V-1 (or V-2/V-3/V-4 as applicable) can be generated with valuer declaration (true information, no interest, personal inspection date). |
| 4 | Photos/videos from field capture can be tagged into the valuation report library. |
| 5 | Where an Expert Valuer is appointed, both declarations/digital signatures are present before CA review. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Select format and method; populate by asset code | The Valuer opens Data Capturing – II, selects valuation format and method, and enters the asset code. Basics of that assigned asset populate the working form. The valuer then enters method-specific fields. A code that is not assigned to this valuer does not populate. |
| F05-002 | Cost of construction — Accounts method | For a building where accounts are used, the Valuer enters materials-cost report, labour-cost report, construction start and completion dates, depreciation using a class from the **certified structure-classification master (F02-007)** (economic life and residual/scrap), likely market value, and the certificate that accounts and vouchers were produced. Saving stores the working for the statutory form. |
| F05-003 | Comparable method for built-up properties | The Valuer records comparable sales for flats/shops/offices (built-up area, date of sale, plot area, FSI/FAR, land appurtenant, consideration, parties, register no.) and applies adjustment factors (location, situation, area, floor difference, specifications, facilities, time-gap, lease/freehold, building area, floor disposition). Fewer than the Authority’s minimum comparables requires a recorded reason. |
| F05-004 | Floor-disposition weightage for FMV | For a residential flat or commercial premises, the Valuer selects floor (basement storage / other basement / GF–1st–mezzanine / 2nd–5th / 6th–9th / 9th+) and applies the FRS weightage to average unit cost A. For Bangalore metropolitan reverse-trend, the valuer **explicitly** confirms or replaces the factor with local-trend justification; the system does not silently invert the table. |
| F05-005 | Land and Building method with adjustments and depreciation | Where the FRS applicability tests hold, the Valuer derives land value from comparables (order of preference; minimum three), applies tabulated adjustment factors (location ±5% bands, time-gap/NPV or 18–24% p.a. if no instances, shape, size, FAR steps, side open, co-ownership 5–12.5%, tenure, encumbrance deferment up to 30%, unearned increase, 10% depressing effect), computes building as PWD-PAR reproduction minus depreciation (structure class from F02-007) plus builder’s efforts at 3% of B, using Le = L − Lf and Q = 0.9 × R × Le / I when p = 10%. Each override is reasoned. Property value is A + E. |
| F05-006 | Property specification proforma | The Valuer completes the specification sheet (foundation, superstructure, fittings, flooring, roofing, finishing, sanitary, electrical, external services, facilities, special items) for residential and/or non-residential as applicable, floor by floor as in the FRS. Empty mandatory blocks block form issue. |
| F05-007 | Form V-1 immovable report and declaration | The Valuer completes Form V-1 (purpose, date, owners, location, amenities, land, roads, tenure, restrictions, building, FSI, rents, disputes, sales, construction, Part II calculations, sub-annexure technical details). The Registered Valuer (and Expert Valuer if appointed — F05-010) declares information true, no direct/indirect interest, and personal inspection date, and **digitally signs**. The form is then available to the CA. |
| F05-008 | Forms V-2, V-3 and V-4 | For agricultural land the Valuer completes V-2 (survey, classification, crops, revenue, special features, comparables, unit value, declaration). For forests/plantations, V-3 (area, timber/density/transport, tree schedule). For mines/quarries, V-4 (output, reserves, seam, development, excluding plant/buildings). Each requires personal inspection and no-interest declaration **and digital signature (F05-010)**. Form V-5 is not in the source and is not offered. |
| F05-009 | Tag photos and videos into the valuation library | On the valuation working, the Valuer tags field photographs and videos (Module 04) into the report library so the CA report and auction-display selection (Module 07) use the same media set. Untagged media remain on the inspection pack but do not appear in the CA photo-picker until tagged. |
| F05-010 | Expert Valuer assignment and digital declaration | An Office user or Registered Valuer appoints an **Expert Valuer** on the assignment (linked shared Person / professional master — not a second login directory). On Forms V-1 to V-8 the Registered Valuer, and the Expert Valuer if appointed, complete the no-interest and personal-inspection declaration and apply a **digital signature**. A form without the Registered Valuer’s digital declaration cannot be submitted to the CA. |

---

### 06. Movables QR Coding & Valuation (eValueM)

**Purpose:** Categorise and QR/tag movables, tabulate condition and value, photograph groups and samples, complete Forms **V-6, V-7 and V-8**, and record **cash and foreign currency** at handover including damaged-note replacement applications to RBI.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Additional Module eValueM; Forms V-6, V-7, V-8 |
| Proceedings 10-08-2026 | Item 9 (movables: location, model, likely purchase date, likely price, bank/account; cash/FCY quantity, value, damage; RBI damaged-note application) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Coding | Apply Module 02 movable code tree. |
| 2 | Tabulation | Category code, group serial, item name, description (material & colour), make/brand, rating, condition, appreciating/depreciating. |
| 3 | Tagging | Prepare sticker/label with category, name, serial no, condition. |
| 4 | Photos | Group of similar items together and individual sample photos. |
| 5 | Proceedings extras | Location, model, likely date of purchase, likely price; bank, account and other details where applicable. |
| 6 | V-6 | Equipment, furniture, machinery and plant. |
| 7 | V-7 | Gemstones, precious metals and jewellery, including recorded purity-testing methods and sub-annexures. |
| 8 | V-8 | Works of art and handicrafts (craft, antiquity, rarity additions). |
| 9 | Cash / FCY | Quantity, value, damage at handover; automate application to replace damaged notes to RBI in the appropriate format. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A movable item carries a code from the eValueM tree and a sticker/label dataset. |
| 2 | Group and sample photographs are stored against the group. |
| 3 | V-6 / V-7 / V-8 can be completed with valuer declaration. |
| 4 | A damaged-currency handover can generate the RBI replacement application from stored particulars. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Classify and register a movable | An Office user or assigned Valuer selects the seized lot, picks the eValueM code (category / sub-code / object / detail), and records location, model, likely purchase date, likely price, and bank/account details where the proceedings require them. Saving creates the movable row under the parent seizure/FE. |
| F06-002 | Tabulate condition and value attributes | On that item the user completes serials, description (material and colour in order), make/brand if available, rating (Exclusive / High / Average / Low), condition (New / Unused / Working / Damaged with details / Scrap / Obsolete) and whether the item is appreciating or depreciating. A later Form V-6/V-7/V-8 reads these fields rather than asking them again. |
| F06-003 | Tagging sticker / label | The user generates the tagging sticker/label dataset: category, name, serial number, condition. The user confirms the printed/attached tag matches the on-screen row. An item without a tag dataset cannot be marked inspection-complete. |
| F06-004 | Group and sample photographs | The user uploads a photograph of the **group of similar items placed together** and individual **sample** photographs. Photos inherit GIS/date rules where capture is on Android (Module 09). The CA can later open the group photo without opening every sample. |
| F06-005 | Form V-6 — equipment, furniture, machinery and plant | The Valuer completes V-6 (purpose, date, owners, description and purpose of plant, line-wise code, description, make, model/year, original and present market price, depreciation, market value) and declares personal inspection and no interest **with digital signature (F05-010)**. |
| F06-006 | Form V-7 — gemstones, precious metals and jewellery | The Valuer completes V-7 (item description, unit, gross/net weight, stone and metal values, special enhancement, explanation of rates, **purity-testing methods actually adopted** from the FRS list: digital weighing, XRF/touchstone, diamond loupe/CVD, gemstone loupe) and Sub-Annexures I and II. Declaration of personal inspection and no interest **with digital signature (F05-010)** is required. |
| F06-007 | Form V-8 — art and handicrafts | The Valuer completes V-8 (description, material, dimensions and weight, base value, additions for hand-crafted, antiquity and rarity, total) and declares personal inspection and no interest **with digital signature (F05-010)**. |
| F06-008 | Cash and foreign currency handover; RBI damaged-note application | An Officer or assigned Valuer records cash/FCY quantity, value and damage observed at handover. Where notes are damaged, the user generates the application to RBI to replace damaged notes in the **appropriate stored format**, from those particulars, and files it against the seizure. Generative AI shall not draft the application text. |

---

### 07. CA Assessment, MIS Reports & Auction-Display Photos

**Purpose:** Generate MIS / valuation reports from valuer-entered data; let the Competent Authority assess the report on specified key parameters (including **computed** Time Taken); select photographs for auction display; accept, reject, order revaluation or issue SCN; **release** the accepted pack to Claim Management for auction.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | MIS reports and Admin (report generation); CA Report on Valuation Report & Valuer Assessment |
| Proceedings 10-08-2026 | Item 12 (CA reports; time taken, category, method, adjustment factors, 7(1), guidance value; CAD already in Module 03) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | MIS | Generate the report from valuation details entered by the valuer; select format; enter code to populate asset basics; tag videos and photos. |
| 2 | CA report | CA enters CA Code to populate asset; reviews valuer report; assesses Time Taken (**computed** from assignment / visit / submit, with CA comment), Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation, Guidance Value. |
| 3 | Auction photos | CA selects photos for display in auction (display selection only — auction execution is Claim Management). |
| 4 | Decision | Accept / Reject / Order Revaluation / Issue SCN to Penalize Valuer. |
| 5 | Handoff | After Accept, authorised user releases the accepted valuation pack (report, unique property code, selected photos) to Claim Module 03. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A CA can open a completed valuer report by asset/CA code without re-entering asset basics. |
| 2 | Assessment records the six key parameters. |
| 3 | Accept is a prerequisite to billing (Module 08). |
| 4 | Selected auction-display photos are identifiable for the Claim auction process. |
| 5 | Time Taken on the CA form is computed from stored dates, not typed from memory as the only source. |
| 6 | After Accept, an authorised user can release the pack to Claim; Claim can open it without re-keying the property code. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Valuation MIS report from valuer data | An authorised Office user or CA selects a valuation report format, enters the asset code, and generates the report from data the valuer entered (not a blank). Photos and videos tagged in F05-009 appear on the report. The user can re-generate after a valuer correction; prior versions remain in history. |
| F07-002 | CA assessment on key parameters | The Competent Authority opens the valuer report, confirms asset basics via CA Code, and records assessment of Time Taken (**shown as computed by F07-006**, with optional CA comment), Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation and Guidance Value. Saving stores the CA report against that valuation. |
| F07-003 | Select photographs for auction display | On the CA report, the CA selects which tagged photographs may be shown at auction. Unselected photos remain in the valuation file but are not marked for auction display. Claim Management uses this selection after release (F07-007); this application does not run the auction. |
| F07-004 | Accept, reject, revaluation or SCN | The CA chooses Accept, Reject, Order Revaluation, or Issue SCN to penalise the valuer, with remarks. Accept unlocks billing (Module 08) and makes the pack eligible for Claim release (F07-007). Revaluation returns the asset to assignment (F04-001) with the CA remarks visible to the valuer and resets stage (F04-008). SCN is stored on the valuer master and the report. |
| F07-005 | CAD / layout available during CA review | While assessing, the CA (or authorised officer) opens the CAD/layout uploaded in F03-006 for maintenance and security context. Absence of a drawing is visible; it does not by itself block Accept unless the Authority marks CAD mandatory for that category. |
| F07-006 | Compute Time Taken from assignment, visit and submit | The system computes elapsed time from Assignment Date (F04-001), Date of Visit (F04-008) and valuer submit timestamp (web or Android F09-005) to CA open/decision. The CA sees those intervals on the assessment form (F07-002) and may add a comment; the CA cannot silently overwrite the computed figures. Missing visit date is flagged. |
| F07-007 | Release accepted valuation pack to Claim for auction | After CA Accept, an authorised Officer or CA releases the pack to Claim Management Module 03: unique seized-property code, accepted report, selected auction-display photographs, and the linked attached-asset row (F03-007) if present. Claim uses this for auction tracking and recovered funds. This feature does **not** record auction sale or deposit. A pack that is not Accepted cannot be released. |

---

### 08. Valuer Billing

**Purpose:** Prepare the valuer’s bill and voucher from approved particulars **only after CA acceptance**; submit online and upload the signed hard copy.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Valuer Billing |
| Proceedings 10-08-2026 | Item 13 (valuer bill and voucher from approved particulars) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Gate | Billing window opens only if CA has accepted. |
| 2 | Populate | Enter Valuer Code to populate valuer basics; select valuation report; open CA report. |
| 3 | Bill | Enter details using rates/incidental costs from the valuer master; submit bill online; upload signed hard copy. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Billing cannot be opened for a report that is not CA-accepted. |
| 2 | Bill uses the valuer master’s rates unless an authorised override is recorded. |
| 3 | Online submit and signed-copy upload are both stored against the assignment. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Open billing only after CA acceptance | A Billing officer (or Office user so authorised) enters Valuer Code, selects the valuation report and opens the CA report. If the CA decision is not Accept, the billing window does not open and the user sees the current decision (Reject / Revaluation / SCN). |
| F08-002 | Prepare bill and voucher from approved particulars | In the billing window the officer reviews populated valuer basics and assignment, applies Rates of Valuation and Incidental Costs from F02-001, enters bill details, and generates the bill and voucher. Changing a rate on the bill requires a recorded reason; it does not silently rewrite the valuer master. |
| F08-003 | Submit bill online and file signed hard copy | The officer submits the bill online against the assignment and uploads the signed hard-copy scan. Either missing item leaves the bill in incomplete status. The valuer and CA can see submitted status; payment execution remains outside this SOW unless the Authority later orders it. |

---

### 09. Valuation Android Application (Approved Valuers)

**Purpose:** Deliver the official Android application on which the assigned valuer retrieves office-entered data, captures GIS media and live location, completes method-specific remaining fields, and submits the field package — authenticating with the **shared** Person identity.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Annexure-01 | Data Capturing – I “the App”; geocoding on Android; eValueM photos |
| Proceedings 10-08-2026 | Items 1, 9–11 (valuation Android); 19 (Play Store licensing where approved; IP with SPLOCA) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Identity | Android login is the shared Person (Module 01); 2FA as on the shared component. |
| 2 | Assigned work | Valuer retrieves assigned asset particulars and documents already entered/uploaded by the office. |
| 3 | Field capture | GIS/geotagged photographs, videos, real-time location, system date and time (Modules 04–06 behaviour on device). |
| 4 | Method fields | Remaining valuation particulars through method-specific data-entry fields (Module 05/06), including approved-source retrieval. |
| 5 | Licensing | Secure Android distribution; Play Store licensing where specifically approved; licensing clear, not speculative. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A valuer logs into Android with the same Person as web; deactivation blocks the app. |
| 2 | Assigned assets and office uploads are available on the device without re-keying. |
| 3 | A field package with GIS photos, video and live location can be submitted from Android and appears on web for CA review. |
| 4 | Distribution/licensing is documented in non-speculative terms. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Android login on shared identity | An Approved Valuer installs the official app and signs in with the same Person credentials and 2FA as Claim Module 01. After login the valuer sees only assigned valuation work. A deactivated Person cannot start a new session. |
| F09-002 | Retrieve assigned assets and office documents | The Valuer opens an assigned asset on Android and sees office-entered basics plus View of sale deeds and court orders already uploaded on web. The valuer does not re-type FE/CA/asset identity. |
| F09-003 | Device GIS photo, video and live location | On site the Valuer captures the Module 04 media set (minimum four photographs, each at least 5 MB, GIS tag, date on photo, video, captured date/time) and the valuer’s real-time location with system date and time, using the device. The live GIS is reverse-geocoded to a readable address (F02-008 / F04-007). Submission without that set is refused. |
| F09-004 | Method-specific remaining entry on Android | The Valuer selects the valuation method/format on the device and completes remaining fields (including eValueM tabulation where the assignment is movable). Approved secure sources may be queried as on web. Generative AI is not offered. |
| F09-005 | Submit field package to web for CA | The Valuer submits the inspection and valuation working from Android. An Office user or CA then opens the same package on web (Modules 05–07). A failed submit leaves a clear retry state; partial drafts are attributable to the valuer Person. |
| F09-006 | Distribution and Play Store licensing | The vendor delivers a secure distribution path. Where SPLOCA specifically approves Play Store licensing, that licensing is stated in clear terms (not a speculative placeholder). IP and source of the app lie with SPLOCA. |

---

## 7. End-to-End Workflows

### 7.1 Identity (shared — not rebuilt)

```text
Administrator provisions Person + Post + Role on shared component (Claim Management Module 01)
        → OTP before activation; 2FA
        → Office user / Approved Valuer / CA logs into valuation web or Android with that Person
        → Assignment and valuation document rights apply
```

### 7.2 Immovable valuation (eValueI)

```text
Office creates 3(2) asset (allotted FE, location/geocode, court order, sale deeds, CAD)
        → Unique property code with Google location
        → Assign approved valuer; record visit date, team, stage
        → Valuer retrieves basics; GIS inspection (photos, video, live location + reverse-geocode, amenities including V-1 rows, Map/QR/marker)
        → Method-specific valuation (accounts / comparable / land-and-building / V-1–V-4); Expert Valuer and digital declaration
        → Tag media into report library
        → CA sees computed Time Taken; assesses other key parameters; select auction-display photos
        → Accept / Reject / Revaluation / SCN
        → If Accept: release pack to Claim for auction; bill and voucher; online submit; signed hard copy
```

### 7.3 Movable valuation (eValueM)

```text
Office/valuer codes movable (eValueM tree)
        → Location, model, likely purchase date/price, bank/account as required
        → Tabulation; sticker/label; group and sample photos
        → Form V-6 / V-7 / V-8 (or cash/FCY + RBI damaged-note application)
        → CA assessment and billing as 7.2
```

---

## 8. Access Control / RBAC

**User management is the shared component in the Claim Management SOW, Module 01.** This application does not define a second Person master.

| Element | Where specified |
|---------|-----------------|
| Person, Post, Role-to-Post, Post-to-Person, mapping history | Claim Management SOW F01-001, F01-002 |
| Official identity, OTP before activation, 2FA, joiner–mover–leaver | Claim Management SOW F01-004 to F01-007 |
| Forensic and login audit | Claim Management SOW F01-010 |
| Valuation Posts on that component | This SOW F01-002 |
| Assignment and valuation document rights | This SOW F01-003 |
| Valuation web and Android on that identity | This SOW F01-004 |
| In-app training and FAQ | This SOW F01-005 |
| Allotted-FE scope for office users | This SOW F03-008 |

Valuation Posts (Office user, Approved Valuer, Competent Authority, and others named by SPLOCA) are **configured on** the shared component. The **Approved Valuer professional master** (rates, order, category) is Module 02, not a login store.

---

## 9. Channels

| Channel | Who | Use |
|---------|-----|-----|
| **Staff web** | Office users, CA, Administrators, billing officers | Full eValueI / eValueM office, CA and billing |
| **Android** | Assigned Approved Valuers | Field retrieve, GIS capture, method remaining entry, submit |
| **Public website** | — | **Not** the valuation application |

---

## 10. Integrations

| Integration | Purpose |
|-------------|---------|
| **Shared user-management component** | Claim Management Module 01 identity for all valuation web and Android users |
| **Common database with Claim Management** | Linked FE / attached-asset / accepted valuation / auction-display photos, subject to RBAC |
| **Existing FE application (via programme references)** | FE/CA names and codes on asset and assignment; no FE dossier rebuild |
| **Geocoding / reverse geocoding** | Address ↔ coordinates / Place ID; readable address; map markers — F02-008 (FRS) |
| **Nearby amenities / map link** | Auto distances including Form V-1 civic/transport rows; Map link, QR and marker |
| **Claim Module 03 handoff** | Accepted valuation pack and auction-display photos (F07-007); auction sale stays in Claim |
| **Approved secure sources (as Authority names)** | Remaining field particulars the valuer is permitted to retrieve |
| **RBI damaged-note application format** | Generated from stored cash/FCY handover particulars |
| **Play Store / Android distribution** | Where specifically approved |

This SOW does not specify interface contracts, payloads or schemas.

---

## 11. Audit, Compliance & Security

1. Privileged valuation actions (assign, submit report, CA decision, bill submit) are attributable to the shared Person.  
2. Instant backup and server storage in case of hardware failure.  
3. HTTPS/SSL and AES-256 for data transmission and encryption.  
4. No generative AI.  
5. IP and source code solely with SPLOCA.  
6. Login/2FA audit remains on the shared component (Claim Management F01-010).  
7. GIS photographs, valuer live location and system date/time are retained with the inspection pack.

---

## 12. Non-Functional Requirements

| Area | Expectation |
|------|-------------|
| **Security** | HTTPS/SSL; AES-256; shared 2FA |
| **Backup** | Instant backup to server |
| **Availability** | Suitable for office create/assign and valuer field days (SLA to be agreed) |
| **Media** | Minimum four photographs per immovable inspection, each at least 5 MB, GIS-tagged, date on photo |
| **Interoperability** | Shared identity; common DB with claims; geocoding on web and Android |
| **Android** | Official valuer work; clear licensing |
| **AI** | Agentic / rule-based only; human verify |
| **Operability** | Per-module access, security awareness, backup participation, training/FAQ |
| **FRS platform note** | PHP named in Annexure-01 as the stated platform, with geocoding available on host PC and Android |

This SOW does not size infrastructure beyond the designated-server requirement.

---

## 13. Data Migration

**In scope** as structured load the Authority releases: existing asset lists, valuer professional masters (not passwords), prior valuation reports and photographs, as available.

**Out of scope unless separately ordered:** scanning bureau; reconstruction of missing physical files; claim or legal-matter migration (those SOWs).

---

## 14. Phased Delivery

| Phase | Focus | Modules (primary) |
|-------|--------|-------------------|
| **P1 — Identity and masters** | Consume shared access; valuer professional master; categories; property codes; structure class; geocoding | 01, 02 |
| **P2 — Office asset register** | 3(2), uploads, search, CAD, Claim-asset link, allotted FE, deactivate | 03 |
| **P3 — Field capture and methods** | Assignment, visit/stage, GIS inspection, V-1–V-4, Expert Valuer | 04, 05 |
| **P4 — Movables and cash** | eValueM, V-6–V-8, cash/FCY / RBI | 06 |
| **P5 — CA, billing, Android** | Assessment, computed Time Taken, Claim release, bills, valuer app | 07, 08, 09 |

P1 is a prerequisite. Exact go-live grouping is a commercial / Authority decision after estimation.

**Source-stated target (Annexure-01 note):** time period of application development, alpha testing and beta live testing shall be **not exceeding 3 months from date of contract**. The vendor shall confirm feasibility against the confirmed module set; this SOW does not convert that target into effort hours.

---

## 15. Deliverables

| Deliverable | Description |
|-------------|-------------|
| Valuation staff web application | Modules 01–08 as specified (eValueI and eValueM) |
| Valuation Android application | Module 09 |
| Consumption of shared user management | Claim Management Module 01 — not a second IAM product |
| Statutory form pack | V-1, V-2, V-3, V-4, V-6, V-7, V-8; RBI damaged-note application format |
| Documentation | Role guide, Android/field guide, CA assessment guide, billing guide, interface notes |
| Training/FAQ hooks | In-application; classroom optional |

---

## 16. Acceptance Criteria (programme level)

1. Valuation users log in only via the shared Person–Post–Role component; there is no second user master.  
2. A valuer sees only assigned assets.  
3. Selecting an assigned asset displays office-entered basics; court order and sale deeds open via View.  
4. An immovable inspection stores at least four GIS-tagged, dated photographs of at least 5 MB each, plus valuer live location and system date/time.  
5. Forms V-1–V-4 or V-6–V-8 (as applicable) can be completed with personal-inspection and no-interest declarations.  
6. CA can assess Time Taken, Category, Method, Adjustment Factors, 7(1) and Guidance Value, and Accept / Reject / Revalue / SCN.  
7. Billing is impossible before CA Accept; bill and signed hard copy can be stored after Accept.  
8. Auction-display photo selection can be **released** to Claim (F07-007); this application does not run the auction.  
9. Android supports retrieve, GIS capture (including reverse-geocoded address), remaining method entry and submit on the same identity as web.  
10. Time Taken on the CA form is computed from assignment, visit and submit dates.  
11. Generative AI is absent. IP of delivered software lies with SPLOCA.  
12. In-app training/FAQ is available per valuation module.

---

## 17. Expected Benefits

- Office-created 3(2) asset is the single starting point for field valuation  
- One identity with Claims and Legal (no duplicate logins)  
- GIS-evidenced inspection (photo, video, live location, date/time)  
- Method-faithful statutory forms without unsupervised generative drafting  
- CA gate before valuer payment  
- Movable QR/tag discipline and cash/FCY handover trail  

---

## 18. Assumptions & Dependencies

### 18.1 Assumptions

1. Project code is EVAL; display name is **GIS Field Valuation — eValueI / eValueM (KPID / SPLOCA)**.  
2. Purpose is RFP discussion and internal estimation.  
3. **User management is the shared Claim Management Module 01**; this SOW does not re-estimate that full identity product.  
4. Document management and workflow are embedded.  
5. FE identity comes from the existing FE application / Claim import, not a new FE dossier.  
6. Claim settlement (including auction sale and recovered funds) and Legal Management remain separate SOWs.  
7. Form V-5 is out of scope unless the Authority supplies it.  
8. Office IT inventory / maintenance tickets (proceedings item 13 last sentence) are out of scope.  
9. Android / Play Store licensing is used only where SPLOCA specifically approves.  
10. Generative AI is prohibited.  
11. Hosting is the designated server; this SOW does not size hardware.  
12. PHP and secure geocoding are **FRS-stated** platform constraints; this SOW does not design those interfaces.  
13. Nearby amenity auto-fetch depends on an Authority-approved map/places capability being available at runtime.  
14. The 3-month development/alpha/beta note in Annexure-01 is an Authority-stated target, not an hours estimate.  
15. Actual claimant-level equitable-distribution data shall not be used for development or testing; only anonymized or synthetic data (Proceedings item 20).

### 18.2 Dependencies

1. Shared user-management component (Claim Management Module 01) available to valuation web and Android.  
2. Access to designated server and approved Android distribution path.  
3. Supply of valuer professional lists, existing asset lists and form templates by SPLOCA.  
4. Common-database linkage rules with Claim Management Module 03 (RBAC).  
5. Confirmation of Valuation Posts (Office user, Approved Valuer, CA, others).  
6. Named list of **approved secure sources** valuers may retrieve from.  
7. RBI damaged-note application format as used by the Authority.  
8. Confirmation of Bangalore floor-weightage practice (FRS metropolitan reverse-trend note).

---

## 19. Vendor Response Expectations

1. Confirm **consumption of Claim Management Module 01** for identity; do not propose a second user directory.  
2. Map the solution to **modules 01–09 and feature IDs F{NN}-{SEQ}** without renumbering.  
3. Describe Android distribution and licensing in clear, non-speculative terms.  
4. Exclude generative AI; describe any agentic assist with human verify.  
5. Do not include Claim settlement (auction sale, recovered-fund deposit) or Legal Management scope in the response to this SOW.  
6. Treat Form V-5 and office IT inventory as out of scope unless the Authority adds them.  
7. Identify assumptions that differ from §18.  
8. Do not include effort hours in a rewritten SOW.

---

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Shared User & Access Control (consumed) | Shared | F01-001 … F01-005 (5) |
| 02 | Valuation Masters, Property Coding & References | Shared | F02-001 … F02-008 (8) |
| 03 | Immovable Asset Register (3(2) & Office Capture) | Business | F03-001 … F03-009 (9) |
| 04 | Valuer Assignment & GIS Field Capture (Data Capturing – I) | Business | F04-001 … F04-008 (8) |
| 05 | Immovable Valuation Methods & Statutory Forms (Data Capturing – II) | Business | F05-001 … F05-010 (10) |
| 06 | Movables QR Coding & Valuation (eValueM) | Business | F06-001 … F06-008 (8) |
| 07 | CA Assessment, MIS Reports & Auction-Display Photos | Business | F07-001 … F07-007 (7) |
| 08 | Valuer Billing | Business | F08-001 … F08-003 (3) |
| 09 | Valuation Android Application (Approved Valuers) | Business | F09-001 … F09-006 (6) |

**Total modules:** 9  
**Total feature outlines:** 64  

Module 01 F01-001 **consumes** Claim Management F01-001–F01-007 and F01-010; it is not a second identity build.

### Appendix B — Source consolidation map

| Source | This SOW |
|--------|----------|
| Claim Management SOW Module 01 (user management) | Module 01 — consumed shared component |
| Claim Management SOW Module 03 | Boundary §4.4; F03-007 link; F07-007 release; auction execution stays in Claim |
| Annexure-01 User–Admin / Valuer Details / Asset Details | Modules 02–03; login → Module 01; visit/stage/team → F04-008; allotted FE → F03-008; asset deactivate → F03-009 |
| Annexure-01 Data Capturing – I | Module 04; Android Module 09 |
| Annexure-01 Data Capturing – II and Valuation Formats | Module 05; structure class F02-007; Expert Valuer / digital sign F05-010 |
| Annexure-01 MIS / CA Report / Valuer Billing | Modules 07–08; Time Taken F07-006 |
| Annexure-01 Forms V-1 to V-4 | Module 05 |
| Annexure-01 eValueM and Forms V-6 to V-8 | Module 06 |
| Annexure-01 PHP / geocoding | F02-008; §10, §12 |
| Annexure-01 3-month note | §14 |
| Form V-5 (absent in PDF) | Out of scope |
| Proceedings item 1 | Dedicated role-based web + Android; not public portal |
| Proceedings items 9–12 | 3(2) through GIS field, CA assessment, CAD; F07-007 handoff (not auction sale) |
| Proceedings item 13 | Credentials → shared Module 01; valuer bill → Module 08; office IT inventory **excluded** |
| Proceedings item 16 | No generative AI |
| Proceedings item 18 | Common DB with claims |
| Proceedings item 19 | Designated server; Android licensing; IP with SPLOCA |
| Proceedings item 20 | Assumption 15 — anonymized/synthetic test data |
| Proceedings item 22 | Unique **seized-property** code with Google location (Module 02); FE coding **not** this SOW |
| Proceedings item 23 | Per-module access, backup, training/FAQ (F01-005) |
| Proceedings items 2–8, 14–15, 17, 21 | Claim / Legal — **not this SOW** |

### Appendix C — Key entities

| Entity | Meaning |
|--------|---------|
| **Shared user component** | Claim Management SOW Module 01 Person–Post–Role |
| **Approved Valuer master** | Professional record (code, category, order, rates) linked to a Person |
| **3(2) asset** | Office-created seized/attached immovable record before field valuation |
| **Assignment** | Binding of an asset to a valuer Person |
| **eValueI** | Geo-tagged immovable valuation |
| **eValueM** | QR-coded movable valuation |
| **CA Accept** | Gate that unlocks valuer billing and Claim release (F07-007) |
| **Expert Valuer** | Optional second signatory on statutory forms (F05-010) |
| **Stage of valuation** | Assignment lifecycle status (F04-008) |

### Appendix D — Abbreviations

SPLOCA, KPIDFE, FE, CA, IO, 3(2), 7(1), FSI/FAR, PWD-PAR, FMV, GIS, QR, SCN, RBI, FCY. Forms V-1 to V-4 and V-6 to V-8 as in Annexure-01. Form V-5 is not used.

### Appendix E — Statutory forms in this SOW

| Form | Subject |
|------|---------|
| V-1 | Immovable property other than agricultural lands, plantations, forests, mines and quarries |
| V-2 | Agricultural lands other than forests and commercial plantations |
| V-3 | Forests and plantations |
| V-4 | Mines and quarries |
| V-6 | Equipment, furniture, machinery and plant |
| V-7 | Gemstones, precious metals and jewellery |
| V-8 | Works of art and handicrafts |

---

**End of Statement of Work — GIS Field Valuation (eValueI / eValueM) (KPID / SPLOCA)**
