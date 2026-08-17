# Statement of Work

# SPLOCA Integrated Claims, Legal & Asset Valuation Platform

**Document type:** Production-grade Statement of Work (RFP discussion and internal estimation)  
**Project code:** SPLOCA  
**Client / Authority:** Special Officer & Competent Authority (SPLOCA) — IMA & other KPIDFE cases, Government of Karnataka  
**Version:** 2.4  
**Date:** 13 August 2026  
**Status:** Draft for review  

---

## Document control

| Item | Detail |
|------|--------|
| **Purpose** | External RFP discussion **and** internal estimation baseline |
| **Authority statute** | Karnataka Protection of Interest of Depositors in Financial Establishments (KPIDFE) Act, 2004 and connected rules / notified forms |
| **Source pack (authoritative)** | (1) Proceedings of the meeting dated 10-08-2026; (2) Claim Management System — Business Process Flow; (3) SPLOCA Legal Management Application (Annexure-I); (4) Main Module — Geo Tagging & Valuation of Immovable Assets (eValueI) including eValueM movables |
| **Related context (non-authoritative for new build)** | Existing public portal / demo at sploca.org is **not** the target solution; the Proceedings require a **dedicated role-based** web and Android application for official work |
| **Supersedes** | SoW SPLOCA Detailed v1.2 (Legal Management–centric). v2.0 consolidated the full programme; **v2.1** added Appendix E; **v2.2** expanded module detail; **v2.3** table/list layout; **v2.4** solidifies module wording and places all entity field details in dedicated tables/lists |

---

## 1. Introduction

This Statement of Work defines the functional and business scope for an **integrated, role-based digital platform** supporting SPLOCA’s statutory responsibilities after a Financial Establishment (FE) is brought under the KPIDFE framework. The platform must interconnect **claims processing**, **legal / matter management**, **seized property valuation and asset management**, **grievance and FIR tracking (reference)**, **statutory notice / template generation**, and **administration**, on a **common database**, with secure **web** and **Android** channels for authorised official work.

The solution must be compatible with the existing legacy environment and designated server / cloud arrangements. It must **not** be merely another public-facing portal (a public portal already exists). Generative AI is **prohibited**; any AI-assisted capability is limited to **approved rule-based or agentic automation**, always subject to **human verification** and a **complete audit trail**.

This SOW is written for senior officers, procurement / RFP evaluators, and estimation teams. It does not prescribe APIs, database schemas, UI wireframes, or effort hours.

---

## 2. Project Overview

### 2.1 Business context

Under the KPIDFE Act, after fraud is identified and Government invokes the Act, SPLOCA (as Competent Authority for IMA and other notified cases) must:

- Maintain authoritative records of each **Financial Establishment**, directors / promoters, schemes, FIR / court references, notifications and orders  
- Manage **attached / seized assets** through valuation, title / khata processes, auction coordination and recovery of funds  
- Maintain a **single depositor profile** across FEs, with rigorous identity, address and bank verification  
- Process **claims** through notification, intake, verification, hierarchical approval, equitable settlement calculation, payment and closure  
- Conduct and track **legal proceedings**, matters, tasks, attendance, expenses, collaboration and a searchable legal knowledge base  
- Value **immovable and movable** seized property (including cash / foreign currency handling workflows) with GIS / geotagged field capture  
- Track **depositor complaints / public grievances** and FIR / investigation / charge-sheet **references** (investigation process itself remains outside the application)  
- Issue **statutory notices, letters, freezing orders, warrants and reports** from controlled templates  

### 2.2 Solution character

| Characteristic | Requirement |
|----------------|-------------|
| **Nature** | Dedicated official application (web + Android), role-based, legacy-compatible |
| **Not** | Replacement of confidential market-intelligence / investigation casework systems; not a generative-AI chatbot; not an open citizen self-service portal for in-Karnataka original-document claim filing |
| **Integration style** | Common database across claims, legal, matter, task, attendance/expense, collaboration, static masters, property and valuation modules — authorised linked access without duplicate entry |
| **IP** | For all in-house applications, codes and software delivered under this engagement, intellectual property rights and source code shall **solely lie with SPLOCA**; no re-use, commercial, advertisement or research use without fees as determined by SPLOCA |
| **Data for build/test** | Actual claimant-level equitable-distribution data shall **not** be shared for development or testing; only anonymised or synthetic data |

### 2.3 Primary users (indicative)

Competent Authority and authorised officers; Legal Cell and empaneled / assigned advocates; valuers; contract staff and security guards (credentialed as applicable); admin / IT; other posts authorised by SPLOCA hierarchy. Limited external claim-intake pathways only where this SOW explicitly allows (e.g. out-of-Karnataka claimants under stated constraints).

---

## 3. Project Objectives

1. Digitise end-to-end **claim settlement** operations after FE handover to the Competent Authority, with verifiable identity, bank and document integrity.  
2. Provide a **production-grade Legal Management** capability (library, search, matters, collaboration, tasks, contacts, attendance/expense, knowledge/training, Android for advocates / Legal Cell).  
3. Deliver **Seized Property Valuation & Asset Management** (eValueI immovable + eValueM movable / specialty forms + cash/FX workflows) with Android GIS field capture and CA assessment / billing.  
4. Enforce **hierarchy and need-to-know** access (role **and** post/position), Limited vs Community collaboration spaces, and per-module security, backup awareness, training and FAQ.  
5. Generate **unique FE and property codes**, interconnect modules on a **common database**, and deploy on the **designated server / approved cloud** with clear Android / Play Store licensing where approved.  
6. Support **agentic / rule-based automation** (OCR to searchable text, forgery screening assist, bank/IFSC checks, template notices, settlement calculations) **without generative AI**, with human verify + audit.  
7. Preserve **forensic-quality audit trails** for payments, penny-drop, verification decisions and privileged actions.

---

## 4. In Scope / Out of Scope

### 4.1 In scope

| Area | Included |
|------|----------|
| **Channels** | Secure staff **web** application; **Android** applications for (a) Advocates & Legal Cell and (b) Valuation field work; limited claim-intake channel for **out-of-Karnataka** claimants as constrained below |
| **Claims programme** | FE management; asset attachment & recovery (through auction / deposit); depositor master & document intake (OCR, translation/format conversion, forgery screening of photos/JPEG); investment portfolio; claim notification; claim submission (staff-mediated for in-Karnataka; limited online for out-of-Karnataka); verification & evaluation; approval; recovery & settlement; payment & closure; penny-drop recording; equitable distribution statement / Special Court report **input-driven** preparation |
| **Legal programme** | Legal database (Acts/Rules, opinions, Special/High Court orders, petitions, SOBs, written arguments) with keyword coding/hyperlinks; advanced search (NL + Boolean); client–legal collaboration; team communication & task management; unified contacts; court attendance & expense; knowledge/expertise/training; matter management; Legal Android |
| **Valuation programme** | Asset & valuer masters; assignment; Preliminary Site Inspection with GIS photos/video; method-specific valuation data capture (Cost of Construction, Comparable, Land & Building and related adjustment factors as in source FRS); Forms V-1, V-2, V-3, V-4, V-6, V-7, V-8; eValueM QR coding taxonomy and movable valuation; CA report assessment; valuer billing; digital layout/CAD upload for maintenance/security; cash & foreign currency quantity/value/damage and RBI damaged-note application automation in prescribed format |
| **Cross-cutting** | Unique FE code (FE number + FE type + tri-lateral index) and seized-property code with Google location; RTI third-party information seeker flag/report across FEs; grievance / complaint follow-up with FIR, investigation and charge-sheet **stage tracking**; statutory template generation (notices, freezing orders, warrants, letters, reports); admin credential management; property & inventory module with unique coded inventory and maintenance tickets; common DB; HTTPS/SSL; AES-256; instant server backup; cloud architecture on designated server; Play Store / distribution licensing clarity where approved |
| **AI policy** | Agentic / rule-based tools only (e.g. OCR, screening assist, rule checks); human verification mandatory; full audit trail |
| **Migration** | Structured migration / load of agreed legacy and scanned corpora: Acts/Rules, opinions, orders, petitions/SOBs/arguments as available, contacts, matters, FE/claim/depositor/investment/asset records as released by SPLOCA (using anonymised/synthetic data for non-prod) |
| **Integrations (business-level)** | Existing online Aadhaar verification; PAN verification provision; OTP for phone; SMS; email sync; geocoding / reverse geocoding; Digi pin / pin-code and geo comparison; contracted-bank penny-drop result recording; Karnataka bank/branch/IFSC reference database; interaction with in-use document software / subscriptions as interfaces allow (Idea, Adobe Suite and similar — interface expectations, not product lock-in) |

### 4.2 Out of scope

| Area | Excluded |
|------|----------|
| **Market intelligence & investigation process** | Collection, confidential handling and investigation procedures for market intelligence and investigation casework — **excluded**, except issuance of various notices from form templates and maintenance of investigation **references** (FIR No., Court Case No., Government Notification) |
| **Generative AI** | Any generative AI for drafting free-form legal advice, fabricating content, or unsupervised claimant communications |
| **Public portal rebuild** | Replacing or merely extending the existing public-facing portal as the primary official system |
| **In-Karnataka full online claim filing** | Unrestricted online claim submission for in-Karnataka claimants where original documents and BSA 2023 / socio-economic profile constraints apply; such claims are **staff-mediated / assisted intake** (scanner/OCR into system). Online limited access may continue or be refined only for **out-of-Karnataka** claimants as directed by SPLOCA |
| **Hardware, scanning bureau, physical security** | Devices, scanners, valuers’ testing machines, RBI logistics, auction physical execution |
| **Training delivery as instructor-led programmes** | Content modules and in-app FAQ/training are in scope; classroom delivery and certification programmes are out unless separately commissioned |
| **Hosting AMC / telecom contracts** | Beyond deployment onto the designated server and documented runbooks; ongoing AMC only if separately ordered |
| **Equitable-distribution production data in non-prod** | Real claimant-level equitable distribution datasets for development/test |
| **Form V-5** | Not present in the supplied eValueI PDF; treat as out of scope unless SPLOCA later supplies the form |

### 4.3 Clarifying boundary — Online claims

Per Business Process Flow Phase 4 and Proceedings: the system is a **dedicated role-based official application**. Claim **windows** and notifications are published for eligible investors; **intake** for in-Karnataka claimants emphasises original documents and controlled digitisation (OCR). **Out-of-Karnataka** claimants may use a constrained online submission path. An existing limited online access system may already exist — this SOW requires the new platform to **cover the business outcomes** of Modules 3A–4B without assuming a mass public portal redesign.

---

## 5. Solution Expectations (business-level)

1. **Single programme, common data:** Claims, legal, valuation, grievances and admin share masters (FE, CA, property, contacts, users/posts) with RBAC preventing unauthorised lateral browsing.  
2. **Need-to-know:** Visibility of matters, documents, claims and assets follows hierarchy and explicit Limited / Community rules.  
3. **Source integrity:** OCR and conversion produce searchable/editable text **without altering** source PDF/JPEG binaries; originals remain authoritative.  
4. **Verification depth:** Phone OTP; address via pin / Digi pin / geo vs database with RPAD re-verification on discrepancy; bank particulars vs claim/ID; Karnataka IFSC/branch DB; penny-drop with audit; Aadhaar (existing service) + PAN.  
5. **Human-in-the-loop automation:** Agentic bots may propose extractions, mismatch queries, forgery-risk flags, settlement maths and template fills — officers decide.  
6. **Court-ready outputs:** Equitable distribution statements, Special Court reports, valuation Forms V-1…V-8, notices under notified forms, 5(2) petition templates, 7(1)/8(1) reports, SOB, PWR, Caveat, IA, SLP etc., with approved fonts/spacing where specified.  
7. **Field truth for valuation:** Geotagged photos (minima per FRS), video, valuer real-time location, system date/time; nearby amenities assist; Google Map link & QR.  
8. **Deployability:** Designated server cloud architecture; clear Android licensing; IP vested in SPLOCA.  
9. **Operability:** Each module/sub-module includes access control, security considerations, backup participation, training content hooks and FAQ.

---

## 6. Consolidated Functional Modules

Document handling and workflow are **embedded** inside business modules unless noted. Module numbers and feature IDs below are **authoritative** for downstream estimation.

Each module is presented for readability and solidity as follows:

| Subsection | Format |
|------------|--------|
| Source coverage | Table |
| Functional requirements | Table (`#` / Area / Requirement) with complete requirement sentences |
| Entity field details | Dedicated field tables or lists (no comma-packed field strings) |
| Acceptance criteria | Numbered criteria table |
| Key capabilities | Feature ID table with full descriptions |



### 01. Access Control, Identity & Need-to-Know Security

**Purpose:** Provide a single, attributable identity model for all official users so that access to claims, legal matters, documents, assets and valuation work is controlled by role **and** post/position, hierarchy and need-to-know rules — on both web and Android.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §§3(d) Limited/Community access; 4(a) hierarchy & need-to-know; 10 Security |
| Proceedings dated 10-08-2026 | Items 1 (dedicated role-based app), 3 (OTP), 13 (credential admin), 18 (RBAC on common DB), 23 (per-module access control) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Identity model | The system shall maintain each official user as a Person linked to one or more Posts/Positions and Roles. Access shall never be role-only. Every create, update, approve, share and delete action shall be attributable to a named person acting in a post. |
| 2 | Visibility control | The system shall enforce organisational hierarchy and need-to-know rules so that matters, claims, depositor records, documents, assets and valuation assignments are visible only to authorised posts. |
| 3 | Collaboration spaces | The system shall support Limited spaces (explicit named members only) and Community spaces (all authorised users of that community), consistent with Legal Annexure collaboration rules. |
| 4 | Document rights | The system shall enforce document rights for view, download, share and edit according to classification and policy. Sensitive legal and claim documents shall not be freely redistributable. |
| 5 | Channel authentication | The system shall authenticate staff web and official Android clients against the same identity store and access rules. |
| 6 | OTP verification | Where phone verification is required (claimant and applicable staff flows), the system shall verify the number by OTP and retain verification status, timestamp and channel. |
| 7 | Credential administration | Authorised administrators shall create, update and deactivate credentials for officers, contract staff, security guards and valuers, including related asset/valuer master linkages, with a complete audit trail. |
| 8 | Per-module ACL | Every module and sub-module shall enforce in-built access control consistent with the central identity model (Proceedings item 23). |
| 9 | Credential hygiene | Credential sharing across persons is prohibited by policy. Deactivation shall block future login without deleting historical audit records. |

##### Entity fields — Person / Post / Credential

| Field / attribute | Notes |
|---|---|
| Person name | Legal name of the individual |
| Person unique ID | System identifier |
| Mobile number | Subject to OTP verification where required |
| Email | Official contact where applicable |
| Post / Position | Official post held (e.g. CA desk, Legal Cell, Admin) |
| Role(s) | Functional role(s) attached to the post |
| Organisation unit | SPLOCA / Legal Cell / Valuation / Admin-IT as applicable |
| Credential status | Active / Inactive / Locked |
| User type | Officer / Contract staff / Security guard / Valuer / Other authorised |
| Linked valuer / asset masters | Where user is a valuer or asset custodian |
| Last credential change | Who changed, when, what changed (audit) |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A user without Limited-space membership cannot open that space or its documents. |
| 2 | A user outside hierarchy/need-to-know cannot open restricted claim, matter, depositor or asset records. |
| 3 | Credential create, update and deactivate events record actor, timestamp and before/after status. |
| 4 | OTP success/failure and verified status are stored and retrievable for audit. |
| 5 | The same person-post-role identity governs web and Android sessions. |
| 6 | Disabling a credential immediately blocks new authentication on all channels. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Person, post/position & role identity | Maintain persons mapped to posts/positions and roles so every login and privileged action is attributable to a named official identity. |
| F01-002 | Hierarchy & need-to-know visibility | Restrict visibility of claims, matters, documents, depositor and asset records by organisational hierarchy and need-to-know rules. |
| F01-003 | Limited vs Community access spaces | Configure and enforce Limited (named members) versus Community collaboration and document spaces. |
| F01-004 | Controlled document rights | Enforce view, download, share and edit rights on sensitive documents according to policy. |
| F01-005 | Web & mobile authentication | Provide secure authentication for the staff web application and official Android applications using the same identity model. |
| F01-006 | OTP phone verification | Verify phone numbers by OTP and retain verification status, timestamp and channel for audit. |
| F01-007 | Credential lifecycle (officers, contract, guards, valuers) | Allow authorised admins to create, update and deactivate credentials for officers, contract staff, guards and valuers with full audit trail. |

---

### 02. Reference Masters, Keywords & Unique Coding

**Purpose:** Provide the shared master data, keyword catalogues and unique coding schemes that all claims, legal, property and valuation modules consume, so records are consistently keyed, searchable and reportable without duplicate masters.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §1(g) Keyword database |
| Proceedings dated 10-08-2026 | Items 7–8 (central masters/templates), 18 (common DB), 22 (unique FE and property codes) |
| Business Process Flow | FE unique ID / keyword linking |
| eValueI / eValueM FRS | Movable coding tree — normative detail in Appendix E |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Keyword & entity masters | The system shall maintain shared keyword and entity catalogues used across legal and claims modules, and allow authorised maintenance without breaking existing document links. |
| 2 | Act & Rules coding | The system shall maintain a coding catalogue for Acts, Rules and Sections to support hyperlinked navigation in the legal library. |
| 3 | Keyword–document links | The system shall create, maintain and repair keyword-to-document links for legal registers and seized-document corpora. |
| 4 | Unique FE code | The system shall automatically generate a unique FE code comprising FE number, FE type and the tri-lateral index assigned to that Financial Establishment. |
| 5 | Unique property code | The system shall automatically generate a unique seized-property code associated with Google location, and support 3(2) prepared-code usage when an asset enters the attachment lifecycle. |
| 6 | Central master service | Master, static and dynamic reference data required by claims, legal, matter, task, attendance/expense, collaboration, property and valuation modules shall be maintained centrally and consumed without duplicate local masters. |
| 7 | eValueM taxonomy | The system shall maintain the full movable category / sub-code / object / detail-code taxonomy exactly as specified in Appendix E. |

##### Keyword / entity catalogue (minimum set)

- FE (Financial Establishment)
- CA (Competent Authority)
- Accused
- Advocates
- Presiding Judge
- Act, Rules & Sections
- Legal Doctrines
- Mahazar
- Survey number
- Other domain keywords as notified by SPLOCA

##### Entity fields — Unique FE code

| Component | Rule |
|---|---|
| FE number | Official FE number assigned in SPLOCA records |
| FE type | Type classification of the Financial Establishment |
| Tri-lateral index | Tri-lateral index assigned to that FE |
| Generated code | System concatenates/composes the above into a stable unique FE code |

##### Entity fields — Unique seized-property code

| Component | Rule |
|---|---|
| Property unique code | System-generated stable identifier |
| Google location | Associated map/location reference |
| 3(2) prepared code | Supported when asset enters 3(2) attachment lifecycle |
| Linked FE code | Property remains linked to parent FE |

##### eValueM top-level category codes (full tree in Appendix E)

- AC — Air Conditioners
- PCP — Computers & Peripherals
- EEG — Electrical & Electronic Goods
- FF — Furniture & Fixtures
- MTP — Machinery, Tools & Plant
- TXT — Textiles
- VEH — Vehicles
- ANC — Art Objects & Handicrafts

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Generated FE codes are unique, stable and searchable across modules. |
| 2 | Generated property codes are unique, linked to FE and Google location, and usable in search. |
| 3 | Keyword hyperlinks resolve to the correct current document/register entries. |
| 4 | Changing a central master value is reflected consistently in consuming modules for authorised users. |
| 5 | eValueM tagging only allows codes that exist in the Appendix E taxonomy. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Keyword & entity masters | Maintain shared keyword and entity catalogues (FE, CA, Accused, Advocates, Judge, Act/Rules, doctrines, Mahazar, Survey number, etc.) used across modules. |
| F02-002 | Act & Rules coding catalogue | Maintain coded Acts, Rules and sections for hyperlinked legal navigation. |
| F02-003 | Keyword–document link maintenance | Create, maintain and repair keyword links to legal and seized documents/registers. |
| F02-004 | Unique FE coding | Auto-generate FE code from FE number, FE type and tri-lateral index. |
| F02-005 | Unique seized-property coding | Auto-generate property code with Google location association and 3(2) prepared-code support. |
| F02-006 | Central static / master data service | Provide single maintenance of master/static/dynamic data consumed by all programme modules. |
| F02-007 | eValueM movable coding taxonomy | Maintain the full hierarchical movable coding tree for QR tagging as defined in Appendix E. |

---
### 03. Financial Establishment (FE) Management

**Purpose:** Create and maintain a complete, interlinked digital dossier for every Fraudulent Entity (FE) so officers can store case artefacts, analyse seized materials, cross-verify claims, produce equitable-distribution / Special Court inputs, and run decision dashboards — without embedding confidential market-intelligence casework.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Module 1 — FE / Database Management (all activities) |
| Proceedings dated 10-08-2026 | Items 18, 22; market-intelligence exclusion item 15 |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | FE dossier | The system shall register each FE in separate interlinked folders with a unique ID, key elements and keywords so authorised users can extract raw data, analytical information and decision reports through queries and dashboards on the official web application. |
| 2 | People & schemes | The system shall capture Directors and Promoters and allow configuration of all Investment Schemes operated by the FE. |
| 3 | Case artefacts | The system shall store and link Court Case information, FIR references, Charge Sheets, Accused, Complaint, Government Notifications, Court Orders and KPIDFE Court proceedings. |
| 4 | Working copies | Scanned FIR, charge-sheet and court materials may be transferred into editable Word/Excel-style working copies for analysis without discarding or altering the original scanned source. |
| 5 | Banks, claimants, status | The system shall maintain Company Bank Accounts, Claimant Database linkage and current case status for each FE. |
| 6 | Special situations | The system shall support processes for ineligible depositors, deceased depositors, legal heirs, joint deposits, third-party payments, lost receipts and cash investments as FE/claim-linked workflows. |
| 7 | Post-seizure corpus | The system shall manage post-seizure and ad-interim attachment data, including translation of relevant documents and linking through keywords (for example Mahazar, FE, Survey number) and unique IDs. |
| 8 | Seized analysis | Authorised users shall be able to analyse seized papers, databases and translations linked to the FE. |
| 9 | Claim cross-check | The system shall enable cross-verification of claims against the seized database of the FE. |
| 10 | Special Court outputs | When relevant data is fed into an approved input format, the system shall prepare the equitable distribution statement and the report required for filing before the Special Court. |
| 11 | Audit hooks | The module shall support hooks to penny-drop and excess-payment analysis (with Modules 05–07) under a complete audit trail. |
| 12 | Exclusion | Market-intelligence process/data and social-media investigation casework are out of scope for this module; only BPF references and notice-template hooks via Module 15 are permitted. |

##### Entity fields — FE register (minimum)

| Field | Notes |
|---|---|
| FE unique code | Per Module 02 (number + type + tri-lateral index) |
| FE name / aliases | Including trade names used in schemes |
| Directors | Name and identifying particulars as available |
| Promoters | Name and identifying particulars as available |
| Investment schemes | Scheme master linked to FE |
| Company bank accounts | Account particulars for the FE |
| FIR number(s) | Reference linkage |
| Charge sheet references | Reference linkage |
| Court case number(s) | Including KPIDFE Special Court references |
| Government notifications | Upload + metadata |
| Court orders | Upload + metadata |
| Accused / complaint refs | As available |
| Current case status | Operational status of the FE case |
| Keywords | Mahazar, Survey number, and other coded keywords |
| Claimant database link | Link to depositor/claim records across Modules 05–07 |

##### Special depositor / claim situations to be supported

- Ineligible depositors
- Deceased depositors
- Legal heirs
- Joint deposits
- Third-party payments
- Lost receipts
- Cash investments

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Each FE has one unique dossier and code with linked FIR/court/notification artefacts. |
| 2 | Authorised users can produce equitable-distribution and Special Court report outputs from approved inputs. |
| 3 | Claim records can be cross-checked against seized FE data by authorised roles. |
| 4 | No market-intelligence or social-media investigation casework screens are present in this module. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | FE register & dossier | Register each FE in interlinked folders with unique ID, key elements and keywords for query and dashboard use. |
| F03-002 | Directors, promoters & schemes | Capture directors and promoters and configure all investment schemes under the FE. |
| F03-003 | FIR, court, notification & order linkages | Store and link FIR, charge sheet, court case, government notifications and court orders to the FE dossier. |
| F03-004 | Company bank accounts & case status | Maintain FE bank accounts, claimant-database links and current case status. |
| F03-005 | Seized document corpus & keyword linking | Manage post-seizure/ad-interim documents with translation and keyword/unique-ID links. |
| F03-006 | Special depositor situations | Support ineligible, deceased, legal heir, joint, third-party, lost-receipt and cash-investment processes. |
| F03-007 | Claim vs seized-data cross verification | Cross-verify submitted claims against the seized FE database. |
| F03-008 | Equitable distribution & Special Court inputs | Prepare equitable distribution statement and Special Court filing report from approved input formats. |
| F03-009 | FE analytics & decision dashboards | Provide queries, reports and dashboards for raw and analytical FE decision support. |

---

### 04. Asset Attachment, Recovery & Auction Management

**Purpose:** Maintain the full lifecycle of court-attached assets and recovered funds — from attachment and valuation linkage through title/e-Khata preparation, auction, deposit of proceeds to approved accounts, and release of recovered amounts into claim settlement — including movables, cash and foreign currency.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Module 2 — Asset Attachment & Recovery Management |
| Proceedings dated 10-08-2026 | Items 9 (3(2)→auction/deposit), 12 (CAD/layout), 22 (property codes) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Asset register | The system shall register all court-attached assets linked to FE, location, address, photo and attachment orders, and support categorisation under the 3(2) lifecycle through auction readiness. |
| 2 | Title & e-Khata | The system shall track transfer of title, e-Khata creation, and dues obtained/paid until Khata is created, before auction. |
| 3 | Orders & valuation e-format | The system shall allow upload of attachment orders and recording of valuation particulars in the prescribed e-format based on the valuation manual and/or Module 14 outputs. |
| 4 | Auction & deposit | The system shall track auction milestones and outcomes in consultation with e-Governance, through to deposit of sale proceeds to the approved account/outcome. |
| 5 | Movables | For movable properties, the system shall record location, model, likely date of purchase, likely price, and bank/account details where applicable. |
| 6 | Cash & FX | For cash and foreign currency, the system shall record quantity, value and damage at handover, and automate application to RBI for replacement of damaged notes in the appropriate format. |
| 7 | Search & status | Authorised users shall search properties by FE name, address and keywords, and update records of rights and physical status. |
| 8 | Recovered funds | The system shall maintain recovered amounts available for settlement and feed those figures to Module 07. |
| 9 | CAD coordination | The module shall coordinate with Module 14 for upload/use of digital layout/CAD drawings for maintenance and security. |

##### Entity fields — Attached asset (minimum)

| Field | Notes |
|---|---|
| Asset unique / 3(2) code | Per Module 02 |
| Linked FE | Parent Financial Establishment |
| Asset category | Immovable / Movable / Cash / Foreign currency / Other |
| Location & address | Including map/Google location where applicable |
| Photo(s) | Linked media |
| Attachment order | Upload + metadata |
| Title transfer status | Workflow status |
| e-Khata status | Workflow status |
| Dues paid till Khata | Amounts and dates |
| Valuation e-format link | Link to Module 14 valuation |
| Auction status / milestones | Including e-Governance consultation points |
| Sale proceeds deposit | Approved account/outcome reference |
| Rights record | Ownership/rights updates |
| Physical status | Condition / custody status |

##### Entity fields — Movable operational record

| Field | Notes |
|---|---|
| Location | Where the movable is held/found |
| Model | Model identification |
| Likely date of purchase | As ascertained |
| Likely price | Estimated/likely value |
| Bank / account details | Where applicable |

##### Entity fields — Cash / foreign currency handover

| Field | Notes |
|---|---|
| Currency type | INR / foreign currency denomination |
| Quantity | Count/units |
| Value | Assessed value |
| Damage status | Damage observed during handover |
| RBI replacement application | Auto-generated in prescribed format when damaged notes apply |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Every attached asset is linked to FE, orders, valuation and auction status. |
| 2 | Title, e-Khata and dues path is trackable before auction can be completed. |
| 3 | Auction outcome and deposit-to-approved account/outcome are recorded. |
| 4 | Cash/FX damage and RBI application workflow is completable with audit. |
| 5 | Recovered-fund totals used by settlement match amounts recorded in this module. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Attached asset register | Register court-attached assets linked to FE, location, photo, orders and 3(2) lifecycle. |
| F04-002 | Title, e-Khata & dues tracking | Track title transfer, e-Khata creation and dues paid till Khata before auction. |
| F04-003 | Attachment order & valuation e-format | Upload attachment orders and record valuation particulars in the prescribed e-format. |
| F04-004 | Auction process & deposit to approved | Track auction milestones/outcomes with e-Governance and record deposit of proceeds to the approved account. |
| F04-005 | Movable asset operational record | Record movable location, model, likely purchase date/price and bank/account links. |
| F04-006 | Cash & foreign currency handover | Record quantity, value and damage; automate RBI damaged-note replacement application. |
| F04-007 | Asset search & rights/status updates | Search by FE/address/keywords and update rights and physical status. |
| F04-008 | Recovered funds for settlement | Maintain recovered amounts and make them available to the settlement/payment module. |

---

### 05. Depositor Master, Document Intake & Identity Verification

**Purpose:** Build one trusted depositor profile across all FEs through OCR intake, forgery screening, KYC capture, and rigorous phone, address and bank verification (including penny-drop), so claim processing rests on reliable, auditable identity data.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Module 3 — Claim & Depositor Master |
| Proceedings dated 10-08-2026 | Items 2–5 (OCR, forgery, OTP, address, bank, penny-drop), 20 (no real ED data in test) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Document intake | The system shall support direct recording of soft data from hard copy using searchable OCR, translation and format conversion (for example JPEG→PDF→DOC) into searchable and editable text **without altering the source file content**. |
| 2 | Forgery screening | Claimant photos/JPEG shall be screened through a suitable Python application for forgery or alteration indicators. Flags shall be presented to officers for human decision; auto-rejection without review is not permitted. |
| 3 | Unique profile | The system shall create a unique depositor profile using four parameters of matching, query-friendly with keyword and address identification, maintained as one profile across all FEs. |
| 4 | KYC capture | The system shall capture the depositor KYC and related fields listed in the field table below. |
| 5 | Aadhaar & PAN | Online Aadhaar verification (existing service) shall be used; PAN verification shall be provided. |
| 6 | Phone OTP | Phone numbers shall be verified by OTP with retained verification status. |
| 7 | Address verification | Address shall be verified by Pin code / Digi pin and geographical location comparison from database. On discrepancy, re-verification by RPAD shall be supported. |
| 8 | Bank verification | Deposit and refund bank accounts shall be verified against account-holder name, account number, branch, IFSC and related particulars; name compared to claim/ID; digit-length checked; Karnataka bank/branch/IFSC database comparison enabled. |
| 9 | Physical bank confirm | Where automatic checks are provisional, the system shall support a workflow step for later physical confirmation by the bank of digit-length / account particulars. |
| 10 | Penny-drop | The system shall record penny-drop verification conducted by the contracted bank, verification results, and an audit trail of payments. |
| 11 | Mismatch queries | The system shall auto-generate mismatch queries when Aadhaar/PAN/EPIC details disagree with Bank Pass Book and Claim Form particulars. |
| 12 | Verification notices | Where verification failures require formal notice, the system shall support auto-generation of notices from notified-form templates via Module 15. |

##### Entity fields — Depositor profile / KYC

| Field | Notes |
|---|---|
| Personal information | Name and demographic particulars as per claim/ID |
| Aadhaar | Number + online verification status |
| PAN | Number + verification status |
| EPIC | Where used in mismatch comparison |
| Contact details | Phone (OTP status), email, other contacts |
| Address | Address lines + pin / Digi pin + geo comparison result |
| RPAD re-verification | Status/result when discrepancy arises |
| Deposit bank account | Account-holder name, number, branch, IFSC, other bank particulars |
| Refund bank account | Same structure as deposit account where distinct |
| Nominee details | As applicable |
| Legal heir details | As applicable |
| Four matching parameters | As defined with SPLOCA for unique profile matching |
| Linked FE(s) | All FEs where the depositor appears |

##### Entity fields — Document intake package

| Item | Notes |
|---|---|
| Source PDF / JPEG | Immutable original retained |
| OCR / translated / converted text | Searchable editable working text |
| Forgery screen result | Flag + officer review decision |
| Format conversion path | e.g. JPEG → PDF → DOC |

##### Entity fields — Penny-drop / payment audit

| Field | Notes |
|---|---|
| Penny-drop request reference | As provided by contracted bank process |
| Penny-drop result | Success/fail and returned name/match indicators |
| Verification timestamp | When result recorded |
| Payment audit events | Subsequent payment trail linkage |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | OCR output is searchable/editable while the source binary remains unchanged. |
| 2 | Forgery-screen flags are visible to officers and recorded with review decision. |
| 3 | OTP, address (including RPAD path) and bank verification statuses are stored. |
| 4 | Penny-drop results and payment audit trail are complete and retrievable. |
| 5 | One depositor identity spans multiple FEs under the four-parameter match. |
| 6 | A pending physical bank-confirmation state is supported where required. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | OCR, translation & format conversion intake | Convert every uploaded PDF/JPEG into searchable/editable text without altering the source binary. |
| F05-002 | Photo/JPEG forgery screening | Python-assisted forgery/alteration screening with mandatory officer review of flags. |
| F05-003 | Unique depositor profile (4-parameter match) | Create and maintain one cross-FE depositor identity using four matching parameters. |
| F05-004 | KYC capture (Aadhaar, PAN, nominee, heirs) | Capture personal, contact, bank, nominee and legal-heir data required for claims. |
| F05-005 | Aadhaar & PAN verification services | Use existing Aadhaar online verification and provide PAN verification. |
| F05-006 | Address verification (pin / Digi pin / geo / RPAD) | Verify address via pin/Digi pin and geo comparison; support RPAD re-verification on discrepancy. |
| F05-007 | Bank account & Karnataka IFSC verification | Verify bank particulars against claim/ID, digit-length and Karnataka IFSC/branch DB, with physical bank-confirm step. |
| F05-008 | Penny-drop verification & payment audit | Record contracted-bank penny-drop results and maintain payment audit trail. |
| F05-009 | Auto mismatch query generation | Auto-raise mismatch queries across Aadhaar/PAN/EPIC, passbook and claim form fields. |

---

### 06. Investment Portfolio Management

**Purpose:** Maintain every investment made by a depositor, compute interest and outstanding balances, analyse bank returns, and compare across FE / FIR / seizure data to support claim evaluation and detection of duplication or collusion indicators.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Module 4 — Investment Portfolio Management; Key Aspects on bank/cash transactions and excess payment |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Investment capture | The system shall capture every investment made by a depositor against an FE and scheme using the field table below. |
| 2 | Auto-calculation | The system shall auto-calculate deposits, interest received, maturity-date violations, and promised interest versus actual interest paid. |
| 3 | Outstanding balance | The system shall determine outstanding balance by treating interest paid as principal repaid where the approved business rule requires it. |
| 4 | Role categorisation | The system shall support authorised rule-based categorisation of depositor types, colluders or accused from portfolio analytics. |
| 5 | Bank returns analysis | The system shall analyse bank returns after scan-based transfer and cross-verify them with claims data. |
| 6 | Bank-officer verification | The system shall record bank-officer email addresses to enable auto-verification requests unless data is submitted directly by bank officers. |
| 7 | Cross-database comparison | The system shall compare across FE databases with FIR and seizures asset databases using single and multiple linked parameters to identify duplication, collusion and related legal requirements. |
| 8 | Excess payment | The system shall detail and categorise bank and cash transactions and support excess-payment analysis with audit trail. |
| 9 | Output | Complete investment history shall be available to claim verification and settlement modules. |

##### Entity fields — Investment record

| Field | Notes |
|---|---|
| Fraudulent Entity (FE) | Linked FE |
| Investment Scheme | Linked scheme |
| Customer ID | As per FE records |
| Bond / MOU Number | Where applicable |
| Deposit Receipt | Receipt reference |
| Investment Date | Date of deposit/investment |
| Maturity Date | Contractual maturity |
| Deposit Amount | Principal deposited |
| Interest Promised | Contractual promised interest |
| Amount Already Received | Returns already paid to depositor |
| Outstanding Balance | System-calculated / maintained balance |
| Interest paid treatment | Flag/rule for interest-as-principal-repaid where applicable |
| Maturity violation flag | Where maturity obligations breached |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Complete investment history is available per depositor, FE and scheme. |
| 2 | Outstanding-balance calculations are reproducible and audited. |
| 3 | Cross-FE duplication/collusion queries return explainable results to authorised users. |
| 4 | Excess-payment analysis is available with an audit trail. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Investment record capture | Capture full investment attributes per depositor, FE and scheme. |
| F06-002 | Interest & outstanding auto-calculation | Calculate promised vs paid interest and outstanding balances, including interest-as-principal-repaid rule where applicable. |
| F06-003 | Maturity & violation analytics | Flag maturity-date violations and related analytics. |
| F06-004 | Depositor/colluder/accused categorisation | Apply authorised rules to categorise depositor, colluder or accused roles from portfolio data. |
| F06-005 | Bank returns analysis & claim cross-check | Analyse scanned bank returns and cross-verify against claims. |
| F06-006 | Bank-officer auto-verification requests | Store bank-officer emails and trigger verification requests unless bank submits data directly. |
| F06-007 | Cross-FE / FIR / seizure comparison | Run multi-parameter comparisons across FE, FIR and seizure databases for duplication/collusion indicators. |
| F06-008 | Excess payment analysis | Analyse excess payments and related bank/cash transactions with audit trail. |

---
### 07. Claim Lifecycle Management

**Purpose:** Manage the full claim journey under the KPIDFE framework — notification, intake, verification, hierarchical approval, settlement calculation, payment and closure — with staff-mediated intake for in-Karnataka claimants, constrained online intake for out-of-Karnataka claimants, and agentic assists only under human verification.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Modules 3A–4B (notification, submission, verification, approval, settlement, payment) and Key Aspects |
| Proceedings dated 10-08-2026 | Items 1, 16, 20; Phase 4 online constraint (in-KA staff-mediated; OOK limited online) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Claim notification | The system shall allow creation and publication of claim notifications so that a claim window becomes active for eligible investors. |
| 2 | Claim submission | The system shall capture claim submissions with mandatory validation before acceptance, covering the fields and uploads listed below. |
| 3 | In-Karnataka intake | For in-Karnataka claimants, intake shall be staff-mediated / assisted digitisation of original documents. Unrestricted public online filing is not acceptable under BSA 2023 / socio-economic profile constraints stated in the BPF. |
| 4 | Out-of-Karnataka intake | For out-of-Karnataka claimants, a constrained online submission path shall be provided. If a limited online access system already exists, the new platform shall still achieve the same business outcomes. |
| 5 | Verification | Officers shall verify identity, investment, scheme, customer ID, deposit records, uploads, bank details, previous returns, existing claims and eligibility, and may request additional documents. |
| 6 | Agentic assists | Rule-based / agentic tools may assist extraction and checks. Generative AI is prohibited. No assist may finalise a verification decision without human confirmation and audit. |
| 7 | Approval | The Competent Authority shall review the verification report and record Approved, Partially Approved, Rejected, or Pending Clarification with remarks. |
| 8 | Settlement | The system shall record recovered funds and liabilities and calculate eligible amount, previous returns, previous settlements and net payable. |
| 9 | Payment & closure | The system shall generate payment batches, record NEFT/RTGS references and status, update claim status / investment balance / payment history, and close settled claims. |
| 10 | Forensic audit & lists | The system shall retain forensic audit trails and generate parameterised claimant, accused, colluder and related lists. |
| 11 | Test-data rule | Actual claimant-level equitable-distribution data shall not be used in development or testing. |

##### Entity fields — Claim notification

| Field | Notes |
|---|---|
| Eligible FE | FE(s) covered by the notification |
| Eligible Schemes | Schemes covered |
| Claim Submission Period | Start and end of claim window |
| Eligibility Criteria | Published eligibility rules |
| Required Documents | Document checklist |
| Instructions | Claimant/staff instructions |
| Publication status | Draft / Published / Closed |

##### Entity fields — Claim submission

| Field / upload | Notes |
|---|---|
| Selected FE | Mandatory |
| Investment Scheme | Mandatory |
| Investment Record | Linked portfolio record where available |
| Personal Details | Confirmed/captured |
| Investment Details | Confirmed/captured |
| Refund Bank Account | Confirmed/captured and verified via Module 05 |
| Identity Proof | Upload |
| Investment Proof | Upload |
| Bank Documents | Upload |
| Nominee / Legal Heir Documents | Upload if applicable |
| Affidavit | Upload |
| Statement of Investment | Upload |
| Mandatory validation result | Block submit if incomplete |

##### Entity fields — Verification checklist

| Check item | Notes |
|---|---|
| Identity | Against KYC / Aadhaar / PAN |
| Investment Details | Against portfolio / seized data |
| Scheme | Eligibility and scheme match |
| Customer ID | Against FE records |
| Deposit Records | Against receipts / seized DB |
| Uploaded Documents | Completeness and integrity |
| Bank Details | Against Module 05 verification |
| Previous Returns Received | Against portfolio |
| Existing Claims | Duplicate/overlap check |
| Eligibility | Against notification rules |
| Additional documents requested | Optional loop |

##### Entity fields — Approval / settlement / payment

| Field | Notes |
|---|---|
| CA decision | Approved / Partially Approved / Rejected / Pending Clarification |
| CA remarks | Mandatory for non-simple decisions as policy requires |
| Total Recovered Amount | From Module 04 |
| Total Approved Liability | Aggregate approved claims |
| Available Settlement Fund | Fund available for distribution |
| Eligible Amount | Calculated |
| Previous Returns Received | Calculated/recorded |
| Previous Settlements | Calculated/recorded |
| Net Payable Amount | Calculated |
| Payment batch ID | System batch reference |
| Payment mode | NEFT / RTGS |
| Payment Reference / Txn Number | Bank references |
| Payment Status | Pending / Success / Failed / Reversed as applicable |
| Claim Status after payment | Updated to closed when settled |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Claim windows open and close according to published notification periods and eligibility rules. |
| 2 | In-Karnataka and out-of-Karnataka intake paths behave as specified and enforce mandatory validations. |
| 3 | Verification, approval, settlement and payment statuses are complete, linked and audited. |
| 4 | Settlement calculations reconcile to recovered funds and prior returns/settlements. |
| 5 | Agentic assists never auto-finalise without human confirmation. |
| 6 | No generative AI components are present in the claim package. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Claim notification & window | Create and publish claim notifications and activate claim windows for eligible FE/schemes. |
| F07-002 | Staff-mediated claim intake (in-Karnataka) | Support assisted digitised claim capture from original documents with mandatory validation. |
| F07-003 | Constrained online claim submission (OOK) | Provide limited online claim submission for out-of-Karnataka claimants with the same mandatory validations. |
| F07-004 | Claim verification & additional docs | Enable officer verification of identity, investment, bank and eligibility, including additional document requests. |
| F07-005 | Agentic verification assists (non-generative) | Provide rule/agent assists for checks with mandatory human verification and full audit; no generative AI. |
| F07-006 | Claim approval decisions | Record CA decisions: Approved, Partially Approved, Rejected or Pending Clarification with remarks. |
| F07-007 | Settlement fund & net payable calculation | Calculate settlement from recovered funds, approved liability, prior returns/settlements and net payable. |
| F07-008 | Payment batches (NEFT/RTGS) & closure | Generate payment batches, record NEFT/RTGS references/status, update balances and close claims. |
| F07-009 | Forensic audit trail (claims & payments) | Retain end-to-end forensic audit for all claim and payment actions. |
| F07-010 | Claimant / accused / colluder list outputs | Generate parameterised claimant, accused, colluder and related operational lists. |

---

### 08. Legal Knowledge Library & Search

**Purpose:** Provide a production-grade legal knowledge base of Acts/Rules, opinions, court orders, petitions, SOBs and written arguments — coded and keyword-hyperlinked — with natural-language and Boolean search suitable for daily Legal Cell work.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §§1–2 Legal Database and Search Facility |
| Proceedings dated 10-08-2026 | Item 7 — legal digital library and templates |
| Business Process Flow | Key Aspect on reading/analysing court petitions, orders, IAs, injunctions and notices |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Acts & Rules | Relevant Acts and Rules shall be coded and keywords hyperlinked. |
| 2 | Opinions | Research and Legal Opinions shall be referenced to FE, CA, Date and Cases/Petitions (Petitioner & OP), and coded/hyperlinked by Case Number, FE, CA, Date of Filing, Date of Order, Act & Section. |
| 3 | Court orders | All Special Court Orders and High Court Orders shall use the full referencing scheme including Accused, Advocates and Presiding Judge. |
| 4 | Petitions / SOB / Written Arguments | All Petitions, SOBs and Written Arguments shall use the same referencing and coding scheme. |
| 5 | Keyword database | The keyword database shall include the entities listed below. |
| 6 | Search | The system shall provide a search box, natural-language search, Search Within Results, and Boolean connector search as specified below. |
| 7 | Results | Search results shall highlight and hyperlink keywords with document address. |
| 8 | Corpus analytics | The system shall support reading, recording, analysing and reporting court petitions, orders, IAs, temporary injunctions and legal notices. |
| 9 | Template holdings | The library shall hold legal document templates in court-approved font and spacing; generation also via Module 15. |

##### Entity / reference fields — Legal register records

| Register | Reference field | Notes |
|---|---|---|
| Acts & Rules | Act / Rule / Section codes | Hyperlinked keywords |
| Opinions | FE, CA, Date | Mandatory references |
| Opinions | Case/Petition (Petitioner & OP) | Party references |
| Opinions | Case Number, Dates of Filing/Order, Act & Section | Coding/hyperlink keys |
| Special/HC Orders | FE, CA, Accused, Advocates, Presiding Judge, Date | Full order references |
| Special/HC Orders | Cases/Petitions (Petitioner & OP) | Party references |
| Petitions | Same scheme as orders | Coded + hyperlinked |
| SOBs | Same scheme as orders | Coded + hyperlinked |
| Written Arguments | Same scheme as orders | Coded + hyperlinked |

##### Keyword database entities

- FE
- CA
- Accused
- Advocates
- Presiding Judge
- Act, Rules & Sections
- Legal Doctrines

##### Boolean / search operators to be supported

- AND, OR, NOT
- /p — same paragraph
- /s — same sentence
- /pg — same page
- /d — same document
- "" — exact phrase
- /# — numeric connector where # is a number
- ! — root expander (example: Obey! → Obey, Obeys, Obeyed, Obeying)
- () — grouping
- Natural language (Google-like) search
- Search Within Results

##### Legal templates held in library (generation also Module 15)

- 5(2) petition
- Notices as per rules
- 7(1) report
- 8(1) report
- SOB
- PWR
- Caveat
- IA
- SLP

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Each register type stores the required reference fields and supports keyword hyperlinks. |
| 2 | Natural-language and Boolean searches return highlighted, hyperlinked results. |
| 3 | Search Within Results narrows a prior result set without losing audit of the query path. |
| 4 | Root expander and proximity operators behave as specified in acceptance tests. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Acts & Rules register | Maintain coded, keyword-hyperlinked Acts and Rules. |
| F08-002 | Research & legal opinions register | Register opinions with FE/CA/case/date/Act-Section references and hyperlinks. |
| F08-003 | Special & High Court orders register | Register orders with FE, CA, Accused, Advocates, Judge, dates and case hyperlinks. |
| F08-004 | Petitions register | Register petitions with full coding and keyword hyperlinks. |
| F08-005 | SOB register | Register Statements of Objections with coding and hyperlinks. |
| F08-006 | Written arguments register | Register written arguments with coding and hyperlinks. |
| F08-007 | Keyword hyperlink navigation | Navigate between keywords and linked legal documents. |
| F08-008 | Natural language & search-within-results | Provide Google-like natural language search and refine-within-results. |
| F08-009 | Boolean connector search | Support AND/OR/NOT, proximity operators, phrase, root expander and grouping. |
| F08-010 | Highlighted hyperlinked results | Highlight hits and deep-link to document locations in results. |
| F08-011 | Court document corpus analytics | Read, record and analyse petitions, orders, IAs, temporary injunctions and legal notices. |

---

### 09. Matter Management

**Purpose:** Provide systematic management of each court matter — creation, classification, variable capture, dashboard, search, reporting, documents/versions, consultations, tasks, key dates, filings/hearings/orders/compliance/next action, and time entry.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §8 Matter Management |
| Proceedings dated 10-08-2026 | Items 6–7 (matters, filings, hearings, orders, compliance, next action, tasks) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Matter create | Authorised users shall create and classify matters with descriptions and core references. |
| 2 | Variables | Users shall capture and edit matter variables listed below. |
| 3 | Dashboard | Each matter shall present a unified dashboard of linked work objects. |
| 4 | Search & reports | Matters shall be searchable; reports shall be available across the listed dimensions. |
| 5 | Documents | Users shall create/edit documents with versions, scan/upload matter documents, and share with controlled access. |
| 6 | Consultations | Users shall initiate consultations with Client, External Expert, Research Expert or Other. |
| 7 | Tasks & key dates | Users shall assign tasks and track key dates, deadlines and alerts. |
| 8 | Case progress | Users shall record filings, hearing dates, court orders, compliance status and next action required. |
| 9 | Time entry | Users shall capture matter-related time. |

##### Entity fields — Matter header

| Field | Notes |
|---|---|
| Matter ID | System identifier |
| Classification / matter type | As configured |
| Description | Narrative summary |
| FE | Linked Financial Establishment |
| CA | Competent Authority reference |
| Court | Court name/forum |
| Opponents | Opposite parties |
| Date | Matter open/relevant date |

##### Entity fields — Matter variables

| Field | Notes |
|---|---|
| Court details | Extended court particulars |
| Matter details | Detailed particulars |
| Category & issues | Issue categorisation |
| Opponent details | Party particulars |
| Lawyers details | Counsel particulars |

##### Matter dashboard objects (must appear together)

- Tasks
- Documents
- Communication & Messages
- Activities
- Team Members
- Client Contacts
- Court Hearings
- Time Entry
- Key Dates

##### Matter report dimensions

- Case wise
- Court wise
- Team Member wise
- CA wise
- FE wise
- Key Date wise
- Stage wise

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An authorised user opening a matter sees all linked dashboard objects permitted by ACL. |
| 2 | Reports can be filtered by each listed dimension. |
| 3 | Document version history is retained; controlled share respects rights. |
| 4 | Filings, hearings, orders, compliance and next action are visible on the matter. |
| 5 | Key-date alerts fire according to configured deadlines. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Matter create & classify | Create and classify matters with FE, CA, court, opponents, dates and descriptions. |
| F09-002 | Matter variable capture | Capture and edit court, type, category, issues, opponent and lawyer variables. |
| F09-003 | Matter dashboard | Present a unified dashboard of tasks, documents, communications, hearings, time and key dates. |
| F09-004 | Matter search | Search matters by authorised criteria. |
| F09-005 | Matter reports | Produce case/court/team/CA/FE/key-date/stage-wise reports. |
| F09-006 | Matter documents & versions | Create, edit, scan and upload documents with version history and controlled sharing. |
| F09-007 | Consultations | Initiate consultations with client, external expert, research expert or other. |
| F09-008 | Matter tasks & key dates | Assign tasks and track key dates, deadlines and alerts. |
| F09-009 | Filings, hearings, orders & next action | Record filings, hearing dates, court orders, compliance status and next action required. |
| F09-010 | Matter time entry | Capture time spent against matter and activities. |

---
### 10. Collaboration, Tasks & Team Communication

**Purpose:** Enable secure, hierarchy-aware collaboration between operational units and the Legal Cell — including advocate court reporting, client queries/meetings, document sharing, full task lifecycle, messaging, email sync, calendars and authorised audio-visual channels.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §§3–4 Client–Legal collaboration; Legal Team Communication & Collaboration |
| Proceedings dated 10-08-2026 | Items 7–8 (tasks; real-time collaboration/meetings/AV) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Advocate reporting | Advocates shall be able to report court proceedings/directions, stay alerts, cause lists, time-critical responses, quick information and to-do lists. |
| 2 | Client collaboration | Clients shall be able to raise queries, request tasks and schedule meetings. |
| 3 | Document sharing | Documents may be shared for Information, Response, Correction, Opinion, Drafting or Approval under Limited or Community access. |
| 4 | Anytime access | Collaboration shall be available anytime/anywhere via web browser and Android for authorised users. |
| 5 | Task lifecycle | The system shall support the full task lifecycle listed below for matter-related and other official tasks. |
| 6 | Team communication | The system shall support sidebar relay, matter-linked communication records, search, email sync, individual/group messaging, calendar and share-with-alert. |
| 7 | Real-time channels | Secure channels shall support group meetings, document sharing and authorised audio-visual sharing between operational units and Legal Cell. |
| 8 | Access rules | Communication artefacts shall respect hierarchy and need-to-know visibility. |

##### Advocate reporting pack

- Court Proceedings / Directions of court
- Stay Alerts
- Cause Lists
- Time Critical Responses
- Quick Information
- To Do Lists

##### Document sharing purposes

- Information
- Response
- Correction
- Opinion
- Drafting
- Approval

##### Entity fields / actions — Task

| Field / action | Notes |
|---|---|
| Assignment Of Task | Assign to person/post |
| Assign Due Date | Mandatory due date |
| Status Of Task | Lifecycle status |
| Alerts | Status/due alerts |
| Accept / Reject Task | Assignee decision |
| Reassign Task | Transfer to another assignee |
| Reminder | Reminder notifications |
| Overdue Tasks | Overdue handling/views |
| Reprimand / Warning | Disciplinary record against task performance |
| Publish Task Completion Report | With attachment |
| Publish Team Member Task Schedule & Status | Team visibility |

##### Team communication capabilities

- Quick sidebar tab to relay communication to the team
- Save records of communication for each matter
- Search communication briefs/messages by Person / Date / Case / Keyword
- Sync email services
- Individual messaging
- Group messaging
- Calendar for task overview and status with team members
- Share files, bills, tasks and calendar with alert

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Task accept, reject, reassign, reminder and overdue behaviours work end-to-end with audit. |
| 2 | Matter-linked communications are retained and searchable by Person, Date, Case and Keyword. |
| 3 | Non-members cannot access Limited collaboration spaces. |
| 4 | Advocate reporting pack and client query/meeting flows are available to authorised roles. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | Advocate court reporting pack | Capture proceedings/directions, stay alerts, cause lists, time-critical responses, quick information and to-dos. |
| F10-002 | Client queries, tasks & meetings | Allow clients to raise queries, request tasks and schedule meetings. |
| F10-003 | Collaboration document sharing | Share documents for information, response, correction, opinion, drafting or approval. |
| F10-004 | Limited/Community collaboration spaces | Enforce Limited versus Community access for collaboration spaces. |
| F10-005 | Task assignment & due dates | Assign matter-related and other official tasks with due dates. |
| F10-006 | Task status accept/reject/reassign | Support accept, reject and reassign with status tracking. |
| F10-007 | Task alerts, reminders & overdue | Provide alerts, reminders and overdue handling. |
| F10-008 | Reprimand / warning | Record reprimand or warning against task performance. |
| F10-009 | Task completion & schedule publish | Publish completion reports with attachments and team schedules/status. |
| F10-010 | Sidebar team communication | Provide a quick sidebar relay for team communications. |
| F10-011 | Matter communication records & search | Persist matter communications and search by Person, Date, Case or Keyword. |
| F10-012 | Email sync & messaging | Sync email and support individual and group messaging. |
| F10-013 | Team calendar & share-with-alert | Provide task calendar and share files/bills/tasks/calendar with alerts. |
| F10-014 | Meetings & AV collaboration channels | Support authorised group meetings, document sharing and audio-visual channels. |

---

### 11. Unified Contact Database

**Purpose:** Maintain one unified, searchable address book for SPLOCA and related offices and external parties, with categorisation and direct SMS/email/team contact actions.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §5 Unified Contact Database |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Coverage | The contact database shall cover the organisations and teams listed below. |
| 2 | Categories | Contacts shall be addable under the categories listed below, with custom categories supported. |
| 3 | Unify & update | Multiple business contact lists shall be convertible into one address book; existing contacts shall be updatable. |
| 4 | Search | Free-text search shall find matches across the database. |
| 5 | Actions | From a contact, authorised users shall send to SMS, Email or Team for phone/mail contact. |
| 6 | Migration | Legacy contact lists shall be migratable as released under Section 13. |

##### Organisations / teams to cover

- SPLOCA Office
- RC Office
- CA
- RD (Revenue Department — confirm if different)
- District Fraud Prevention Cell
- Investigating Officers (IOs)
- Legal Team

##### Contact categories

- Advocates
- Accused
- Petitioners
- Visitors
- External Experts
- Key Officials (Tahsildar, AC, Sub Registrar, and similar)
- Custom categories defined by authorised users

##### Entity fields — Contact record (minimum)

| Field | Notes |
|---|---|
| Name | Person or office name |
| Category | From category list / custom |
| Organisation | Office/org affiliation |
| Phone | For SMS/call hand-off |
| Email | For email hand-off |
| Address | Where available |
| Designation / role | Where available |
| Notes / additional details | Updatable |
| Team link | For team contact action |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Contacts for all listed organisations/teams can be maintained and searched. |
| 2 | Custom categories can be added without breaking existing records. |
| 3 | SMS, email and team hand-off actions work for authorised users from a contact record. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F11-001 | Office & organisation contact coverage | Cover SPLOCA, RC, CA, RD, DFPC, IOs and Legal Team contacts. |
| F11-002 | Categorised contact types | Maintain advocate, accused, petitioner, visitor, expert and key-official categories. |
| F11-003 | Unified address book & custom categories | Merge multiple lists into one address book; support custom categories and updates. |
| F11-004 | Contact free-text search | Provide free-text search across the address book. |
| F11-005 | SMS / email / team contact actions | Initiate SMS, email or team contact directly from a contact record. |

---

### 12. Court Attendance & Expense Management

**Purpose:** Record court attendance and authorised category-wise expenses linked to matters, with search and expense-bill submission, on web and Android.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §6 Court Attendance & Expense Management |
| Proceedings dated 10-08-2026 | Item 7 — attendance, authorised expenses, matter linkage |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Attendance | Users shall submit court attendance with all fields listed below, including Cause List upload. |
| 2 | Expenses | Users shall capture authorised expenses by category with vouchers, linked to task/matter. |
| 3 | Search | Quick search and retrieval of attendance and expense records shall be available. |
| 4 | Expense bill | Users shall submit expense bills for processing. |
| 5 | Matter linkage | Attendance and expenses shall be linked to the concerned court matter. |
| 6 | Channels | Functionality shall be available on web and Android (Module 17). |

##### Entity fields — Court attendance

| Field | Notes |
|---|---|
| Name / Code | Attendee identity |
| Date | Attendance date |
| Court | Court name |
| Location | Court location |
| Entry Time | In-time |
| Presiding Judge | Judge name |
| Matter | Linked matter |
| Brief on Proceedings | Short narrative |
| Effective / Ineffective | Hearing effectiveness flag |
| Exit Time | Out-time |
| Cause List | Upload attachment |

##### Entity fields — Expense entry

| Field / category | Notes |
|---|---|
| Task | Linked task if any |
| Assigned By | Who assigned |
| Travel | Amount + voucher |
| Boarding | Amount + voucher |
| Lodging | Amount + voucher |
| Local Travel | Amount + voucher |
| Court Expenses | Amount + voucher |
| Clerkage | Amount + voucher |
| Specified Other Expense | Amount + voucher + description |
| Linked Matter | Mandatory matter link |
| Expense Bill submission | Bill package for processing |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Attendance records capture all listed fields and are matter-linked. |
| 2 | Expense entries support all listed categories with vouchers and matter linkage. |
| 3 | Attendance and expense records are searchable. |
| 4 | Expense bills can be submitted with supporting documents. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F12-001 | Court attendance capture | Capture full attendance fields including Effective/Ineffective and Cause List upload. |
| F12-002 | Category-wise expense capture | Capture categorised authorised expenses with vouchers linked to tasks/matters. |
| F12-003 | Attendance & expense search | Provide quick search and retrieval of attendance and expense records. |
| F12-004 | Expense bill submission | Submit expense bills with supporting documents for processing. |

---

### 13. Knowledge, Expertise, Tools & Training

**Purpose:** Provide a rights-managed knowledge repository for manuals/SOPs, forms, judgements, OM/GO/guard files and training content, including outgoing-member knowledge capture and per-module FAQ/training hooks.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §7 Knowledge, Expertise, Tools & Training Modules |
| Proceedings dated 10-08-2026 | Item 23 — per-module training and FAQ |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Repositories | The system shall maintain the knowledge repositories listed below with keyword hyperlinks where applicable. |
| 2 | Training content | In-app training modules shall cover Legal Research, Legal Writing, MS Word and MS Excel. |
| 3 | Knowledge operations | Users shall create, share, use and manage knowledge assets within rights controls. |
| 4 | Leak prevention | The system shall support systematised aggregation of an outgoing team member’s proprietary knowledge. |
| 5 | Search & metadata | Each document shall be docketed for title/word search and shall record author and date of file creation. |
| 6 | Rights management | Sensitive knowledge shall be protected through controlled file sharing and access control. |
| 7 | Per-module FAQ | Each module/sub-module shall provide training and FAQ entry points. |

##### Knowledge repositories

- Manuals, Guidelines and SOP database (keyword-hyperlinked)
- Forms & Format Templates
- Key Judgement database
- OM, GO & Guard File Database

##### Training module topics

- Legal Research
- Legal Writing
- MS Word
- MS Excel

##### Entity fields — Knowledge document

| Field | Notes |
|---|---|
| Title | Docket title |
| Document type | SOP / Form / Judgement / OM / GO / Guard file / Training / Other |
| Author | Author details |
| Date of file creation | Ready-reference metadata |
| Keywords | Hyperlinkable keywords |
| Access rights | Rights-managed sharing |
| Outgoing-member capture flag | For knowledge-leak prevention workflow |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Knowledge assets are searchable by title and words, with author and creation date visible. |
| 2 | Unauthorised users cannot open rights-restricted knowledge documents. |
| 3 | Outgoing-member knowledge capture workflow can be completed and searched later. |
| 4 | FAQ/training entry points exist for each module/sub-module. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F13-001 | Manuals, guidelines & SOP library | Maintain keyword-hyperlinked manuals, guidelines and SOPs. |
| F13-002 | Forms & format templates | Maintain operational forms and format templates. |
| F13-003 | Key judgement database | Maintain key judgements for ready reference. |
| F13-004 | OM, GO & guard file database | Maintain OM, GO and Guard File repository. |
| F13-005 | Training modules | Deliver in-app training for Legal Research, Legal Writing, MS Word and MS Excel. |
| F13-006 | Knowledge share & searchable repository | Provide a docketed searchable knowledge repository with author and creation date. |
| F13-007 | Knowledge leak prevention | Capture and aggregate outgoing team member proprietary knowledge. |
| F13-008 | Knowledge rights management | Enforce controlled sharing and access for sensitive knowledge. |
| F13-009 | Per-module FAQ & training hooks | Provide FAQ and training entry points in every module/sub-module. |

---
### 14. Seized Property Valuation & Asset Management (eValueI / eValueM)

**Purpose:** Manage seized and attached property valuation from 3(2) through auction readiness: office asset creation, valuer assignment, Android GIS field capture, method-specific valuation, Forms V-1–V-4 and V-6–V-8, CA assessment, valuer billing and CAD/layout upload. **Appendix E is normative for every valuation field, formula, form schedule and eValueM code node.**

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Proceedings dated 10-08-2026 | Items 9–13 |
| Main Module eValueI / eValueM FRS | Full field schedules, methods, forms and coding — Appendix E |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Office asset create | Office users shall create seized asset records on the web with the office and asset fields listed below. |
| 2 | Asset register | The system shall register assets with boundaries, deeds, orders and category fields listed below. |
| 3 | Valuer master & assignment | The system shall maintain approved valuers and assignments with the fields listed below. |
| 4 | 3(2) operations | Users shall apply 3(2) prepared code, categorise assets, link location/address/photo, assign valuers, update rights/physical status, and search by FE name, address and keywords. |
| 5 | Site inspection | Assigned valuers shall complete Preliminary Site Inspection on Android with auto-fetched amenities, GIS media minima and the inspection fields listed below. |
| 6 | Method data | Valuers shall enter method-specific analytical data exactly as specified in Appendix E (Cost of Construction, Comparable, FMV floor weightages, Land & Building factors and depreciation formulas). |
| 7 | MIS & CA assessment | The system shall generate valuation reports for CA assessment on the listed parameters and support Accept / Reject / Order Revaluation / Issue SCN, plus auction photo selection. |
| 8 | Billing | After CA acceptance, the system shall prepare valuer bill and voucher; support online submit and signed hard-copy upload. |
| 9 | CAD | Competent officers shall upload digital layout/CAD drawings for maintenance and security. |
| 10 | eValueM | Movables shall be coded, tabulated, labelled and photographed per Appendix E. |
| 11 | Forms | Forms V-1 (with Sub-Annexure), V-2, V-3, V-4, V-6, V-7 and V-8 shall be completable with every field in Appendix E. |
| 12 | Geocoding | The system shall support geocoding and reverse geocoding (address ↔ coordinates) on web and Android. |

##### Entity fields — Office user asset creation (web)

| Field | Notes |
|---|---|
| Office user ID | Logged-in office user |
| User Name | Office user name |
| Designation | Office user designation |
| Mobile Number | Office user mobile |
| Allotted FE name | Linked FE |
| FE Code | Unique FE code |
| CA name | Competent Authority |
| CA Code | CA code |
| Asset Description | Narrative |
| Asset Location | Location text |
| Latitude & Longitude | Coordinates |
| Date of Attachment | Attachment date |
| Date of Absolute | Absolute date where applicable |
| Court Order | Order reference / upload |
| IO Valuation | IO valuation reference/value |
| Section 7(1) Valuation | Statutory valuation reference/value |
| Guidance / Market Value | Guidance or market value |

##### Entity fields — Asset register

| Field | Notes |
|---|---|
| Asset ID | System ID |
| Asset Name | Name |
| Type / details | Asset type and particulars |
| Address | Full address |
| Boundaries North / South / East / West | As per document |
| Asset Measure | Measurement |
| Asset Registration Date | Registration date |
| Parties and Value | Parties and stated value |
| Stamp Duty Paid | Amount |
| Registration Fee | Amount |
| FE Code / CA Code | Links |
| Court Order number & details | Upload supported |
| Sale deed details | Upload supported |
| Category | Land / Property / Building / Lease Holding / Other |
| 3(2) prepared code | Lifecycle code |
| Photo | Linked media |

##### Entity fields — Approved valuer & assignment

| Field | Notes |
|---|---|
| Approved Valuer name | Valuer identity |
| Valuer Code | Unique code |
| Category | Valuer category |
| Order Number | Approval/order reference |
| Rates of Valuation & Incidental Costs | Fee schedule |
| Assignment Number / Date | Assignment identity |
| Assigned Property Details | Linked asset(s) |
| Date of Visit | Field visit date |
| Stage of Valuation | Workflow stage |
| Valuer mobile / allotted names | Contact and allotment particulars |

##### Entity fields — Preliminary Site Inspection

| Field | Notes |
|---|---|
| Selected Asset | From assignment dropdown |
| Displayed office basics | Name, Details, Address, Measure, Registration number |
| View sale deed / court order | Read-only view of uploads |
| CA identification | CA Name, Designation, Mobile, Office Address |
| FE identification | FE Name & Code |
| Approach road width / type | Location particulars |
| Landmark / surrounding area | Location particulars |
| Boundaries N/S/E/W | As inspected |
| Amenity distances (auto-fetched) | School/College, Hospital, Malls, Places of worship, Police, Bus/Railway/Airport |
| Google Map link & QR | Map reference |
| Photos | Minimum 4, each ≥5MB, GIS tag, date on photo |
| Video | Upload supported |
| Captured Date and Time | System + capture time |
| Valuer real-time GIS | Live location |
| Negative factors | Factors affecting property |
| Overall Observation / Remarks | Valuer remarks |

##### Entity fields — CA assessment & billing

| Field / action | Notes |
|---|---|
| Time Taken | Assessment parameter |
| Asset Category | Assessment parameter |
| Method Adopted | Assessment parameter |
| Adjustment Factors used | Assessment parameter |
| Section 7(1) Valuation | Assessment parameter |
| Guidance Value | Assessment parameter |
| Photos for Auction display | Selected by CA |
| CA action | Accept / Reject / Order Revaluation / Issue SCN to Penalize Valuer |
| Valuer bill & voucher | Prepared only after CA acceptance |
| Online bill submit + signed hard copy upload | Billing completion |

##### Normative detail (do not omit)

- All valuation methods, adjustment-factor tables, depreciation formulas and specification proformas — Appendix E
- Forms V-1 (+ Sub-Annexure), V-2, V-3, V-4, V-6, V-7 (incl. purity testing methods), V-8 — Appendix E
- Full eValueM category/sub/object/detail code tree, tabulation columns, sticker/label and photo rules — Appendix E

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Assigned valuers see only their assignments; office-entered basics display before field entry. |
| 2 | Amenity distances are auto-fetched where GIS/API allows; photos meet ≥4 × ≥5MB GIS-dated minima; system date/time and real-time location are captured. |
| 3 | CA can Accept, Reject, Order Revaluation or Issue SCN; billing is blocked until acceptance. |
| 4 | Forms V-1–V-4 and V-6–V-8 are completable and exportable with all Appendix E fields. |
| 5 | eValueM coding and tagging produce unique labels consistent with the Appendix E tree. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F14-001 | Office asset data creation (web) | Create seized asset records with FE/CA codes and valuation seed fields on the web application. |
| F14-002 | Asset register (boundaries, deeds, orders) | Register assets with boundaries, parties, stamp duty, sale deeds and court order uploads. |
| F14-003 | Approved valuer master & assignment | Maintain approved valuers, rates and property assignments with assignment numbers/dates. |
| F14-004 | Valuer assignment retrieval & secure sources | Allow valuers to retrieve assignments and approved secure reference data. |
| F14-005 | Preliminary site inspection (GIS photos/video) | Capture site inspection with auto amenities, map QR, GIS-dated photos/video, location/time and remarks. |
| F14-006 | Valuation methods & analytical data capture | Capture method-specific analytical data per all Appendix E methods and factors. |
| F14-007 | Specification & depreciation proformas | Capture building specification and depreciation calculation inputs per Appendix E. |
| F14-008 | Valuation MIS reports | Generate valuation reports for CA with photo/video tags. |
| F14-009 | CA valuation assessment & actions | Support CA assessment parameters and Accept/Reject/Revalue/SCN actions with auction photo selection. |
| F14-010 | Valuer bill & voucher | Prepare and submit valuer bill/voucher after CA acceptance, including signed hard-copy upload. |
| F14-011 | CAD / digital layout upload | Upload property layout/CAD for maintenance and security. |
| F14-012 | eValueM movable QR coding & tagging | Code, tabulate, label and photograph movables using the full Appendix E taxonomy. |
| F14-013 | Form V-1 immovable valuation report | Complete Form V-1 and Sub-Annexure with every Appendix E field. |
| F14-014 | Forms V-2 / V-3 / V-4 valuation reports | Complete agricultural, forest/plantation and mines/quarries forms in full. |
| F14-015 | Form V-6 movable valuation report | Complete Form V-6 for equipment, furniture, machinery and plant. |
| F14-016 | Form V-7 jewellery & precious metals | Complete Form V-7 including purity testing method fields and sub-annexures. |
| F14-017 | Form V-8 art & handicrafts | Complete Form V-8 for works of art and handicrafts. |
| F14-018 | Geocoding / reverse geocoding support | Convert address↔coordinates/Place IDs for mapping and verification on web and Android. |

---

### 15. Grievance, FIR Tracking, RTI Flags & Statutory Templates

**Purpose:** Track depositor complaints and public grievances with FIR/investigation/charge-sheet stage references; flag RTI third-party seekers across FEs; and generate statutory notices/orders from controlled templates — without building market-intelligence investigation casework.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Proceedings dated 10-08-2026 | Items 14–15, 17, 21 |
| Business Process Flow | Phase 3 references; Phase 4 notice/freezing/report hooks; Key Aspects draft generation |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Grievance follow-up | The system shall support follow-up of depositor complaints and public grievances with action taken at each stage. |
| 2 | Stage tracking | The system shall track complaint, FIR, investigation and charge-sheet stages as references (investigation process itself remains out of scope). |
| 3 | Investigation references | The system shall maintain FIR Number, Court Case Number and Government Notification references. |
| 4 | RTI flag | The system shall provide a modifiable, searchable flag/report identifying depositors who filed RTI applications seeking third-party information, across different FEs. |
| 5 | Statutory templates | The system shall generate draft letters, reports, notices, freezing orders and warrants to Tahsildar, Banks, Claimants or other competent authority/Government through stored templates. |
| 6 | Notified forms | The system shall auto-generate notices from templates as per notified forms. |
| 7 | Template catalogue | The template library shall cover the document types listed below. |
| 8 | Phase 4 template hooks | Template-only support may include preliminary investigation orders, notices to suspected fraudster, rule-5 freezing orders and report to Government — without MI casework screens. |
| 9 | Exclusion | Market-intelligence process/data and investigation process are excluded except notice issuance from form templates. |

##### Entity fields — Grievance / FIR stage track

| Field | Notes |
|---|---|
| Complaint / grievance ID | System identifier |
| Complainant / depositor link | Where known |
| Linked FE | Where applicable |
| Stage | Complaint / FIR / Investigation / Charge-sheet |
| Action taken | Action at current stage |
| FIR Number | Reference |
| Court Case Number | Reference |
| Government Notification | Reference |
| Status / dates | Stage timestamps |

##### Entity fields — RTI third-party flag

| Field | Notes |
|---|---|
| Depositor link | Flagged depositor |
| FE(s) | Across different FEs |
| RTI application particulars | As recorded |
| Third-party information sought | Flag/report basis |
| Modifiable flag | Editable by authorised roles |
| Searchable report | Cross-FE report output |

##### Statutory / legal template types

- Letters and reports requesting compliance
- Notices under notified forms
- Freezing orders (including rule 5 where applicable)
- Warrants
- 5(2) petition
- 7(1) report / 8(1) report
- SOB, PWR, Caveat, IA, SLP
- Reply to Notices
- Vakalat
- Email replies and queries
- Address lists, vendor list, accused list, colluder list
- Claimant lists on different parameters

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Grievance/FIR stage timelines show actions taken at each stage. |
| 2 | RTI third-party flags are searchable across FEs. |
| 3 | Template-generated drafts are editable before issue and fully audited. |
| 4 | No market-intelligence investigation casework screens are present. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F15-001 | Grievance & complaint follow-up | Track depositor/public grievances with action taken at each stage. |
| F15-002 | FIR / investigation / charge-sheet stage tracking | Track complaint→FIR→investigation→charge-sheet stages as references with actions. |
| F15-003 | Investigation reference register | Maintain FIR Number, Court Case Number and Government Notification references. |
| F15-004 | RTI third-party seeker flag & report | Provide modifiable searchable flag/report of RTI third-party information seekers across FEs. |
| F15-005 | Statutory notice & order templates | Generate notices, freezing orders, warrants and compliance letters from templates. |
| F15-006 | Legal & operational document drafts | Draft replies, Vakalat, Caveat, email replies and operational lists. |
| F15-007 | Notified-form auto notice generation | Auto-generate notices from notified forms, including verification and rule-5 freezing templates. |

---

### 16. Administration, Inventory & Support

**Purpose:** Provide admin/IT inventory control with unique coded items by location, and a maintenance ticketing process for IT hardware, software, web applications and other machinery/equipment.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Proceedings dated 10-08-2026 | Item 13 — property and inventory sub-module; item 23 via Module 13 FAQ hooks |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Inventory register | Admin/IT shall maintain a complete inventory of property/equipment with unique codes and locations. |
| 2 | Ticketing | Users shall raise, assign, track and close maintenance tickets for the categories listed below, with audit. |
| 3 | Related admin | This module operates alongside Module 01 credential administration and Module 14 asset/valuer masters. |

##### Entity fields — Inventory item

| Field | Notes |
|---|---|
| Unique inventory code | Stable identifier |
| Item description | What the item is |
| Category | IT hardware / IT software / Web app / Machinery / Equipment / Other |
| Location | Physical or logical location |
| Status | In use / Under maintenance / Retired as applicable |
| Custodian | Responsible user/post if applicable |

##### Entity fields — Maintenance ticket

| Field | Notes |
|---|---|
| Ticket ID | System identifier |
| Ticket type | IT hardware / IT software / Application web apps / Other machinery and equipment |
| Linked inventory item | Where applicable |
| Raised by / date | Requester audit |
| Assignee | Assigned resolver |
| Status | Raised / Assigned / In progress / Closed |
| Resolution notes | Closure particulars |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Every inventory item has a unique code and location. |
| 2 | Tickets can be raised, assigned, tracked and closed for all listed categories with audit. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F16-001 | Unique coded inventory register | Maintain uniquely coded inventory items with locations. |
| F16-002 | Maintenance ticket management | Raise, assign, track and close tickets for IT HW/SW, web apps and other machinery/equipment. |

---

### 17. Mobile Applications (Legal Cell & Valuation)

**Purpose:** Deliver secure Android applications for Advocates/Legal Cell and for valuation field work, with clear distribution/licensing and the same RBAC model as the web application.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §9 Mobile Application for Advocates & Legal Cell |
| Proceedings dated 10-08-2026 | Items 1, 6–7, 10–11, 19 |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Legal Android scope | The Legal Android app shall provide the capabilities listed below for authorised Advocates and Legal Cell users. |
| 2 | Valuation Android scope | The Valuation Android app shall support assignment retrieval, method-specific data entry, GIS media capture and Module 14 / Appendix E inspection/form workflows. |
| 3 | Distribution | Secure Android distribution and licensing shall be provided; Play Store licensing only where specifically approved; licensing shall be clear and not speculative. |
| 4 | Security | Apps shall use the same identity, hierarchy and need-to-know model as web; they are dedicated official apps, not a public portal. |

##### Legal Android capabilities

- Add Contact
- Add Matter
- Task Management — Create, Assign, Accept/Reject, Reassign, Mark completed, Task inbox, Overdue, Task outbox
- Send Communication
- Internal Messaging
- Make Time Entry
- View Matter Dashboard — Tasks, Communication, Documents, Court Hearings, Team Members, Client contacts
- Attendance recording
- Expense recording
- Documents — View, Download, Create folder, Upload, View shared documents

##### Valuation Android capabilities

- Display office-entered asset particulars and uploaded documents for assigned assets only
- Retrieve assignment data from the web application
- Obtain information from approved secure sources
- Enter remaining valuation particulars through method-specific fields
- Capture photographs with GIS/geotagging (minima per Module 14)
- Capture videos
- Capture valuer real-time location with system-generated date and time
- Complete Preliminary Site Inspection and Form workflows per Module 14 / Appendix E

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Legal and Valuation Android apps authenticate against the same identity model as web. |
| 2 | All Annexure §9 Legal mobile capabilities are present and ACL-enforced. |
| 3 | Valuation field capture preserves geotag and system date/time integrity. |
| 4 | Distribution and licensing artefacts are delivered as approved and documented clearly. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F17-001 | Legal mobile — contacts & matters | Add Contact and Add Matter on Android. |
| F17-002 | Legal mobile — task management | Provide full task inbox/outbox lifecycle on Android. |
| F17-003 | Legal mobile — communication & messaging | Send communications and internal messages on Android. |
| F17-004 | Legal mobile — time entry | Capture matter time entries on Android. |
| F17-005 | Legal mobile — matter dashboard | View consolidated matter dashboard objects on Android. |
| F17-006 | Legal mobile — attendance & expense | Record court attendance and expenses on Android. |
| F17-007 | Legal mobile — documents | View, download, create folder, upload and view shared documents on Android. |
| F17-008 | Valuation mobile — assignment & data entry | Retrieve assignments and enter method-specific valuation data in the field. |
| F17-009 | Valuation mobile — GIS media & location | Capture geotagged photos/videos with real-time location and system date/time. |
| F17-010 | Secure Android distribution & licensing | Provide approved secure distribution and clear licensing (Play Store only if specifically approved). |

---

### 18. Platform Security, Backup, Encryption & Deployment

**Purpose:** Provide the common platform services required by all modules: transport and data encryption, instant backup, common interconnected database, designated-server deployment, forensic audit, legacy/document-suite interoperability, and exclusive SPLOCA IP ownership of source code.

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Management Annexure-I | §10 Security |
| Proceedings dated 10-08-2026 | Items 1, 16, 18–20, 23 |
| Business Process Flow | Key Aspects — legacy integration, forensic audit, document suites |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Backup | The system shall provide instant backup and server storage in case of hardware failure, with per-module backup participation. |
| 2 | Transport security | All client-server data transmission shall use HTTPS/SSL. |
| 3 | Encryption | AES-256-bit encryption standard shall be applied as specified for protected data. |
| 4 | Common database | A common database architecture shall interconnect claims, legal, matter, task, attendance/expense, collaboration, static-data, property-management and valuation modules so authorised users access linked information without duplicate entry, subject to RBAC. |
| 5 | Deployment | All approved services shall be deployed on the existing designated server under the required cloud architecture. |
| 6 | Forensic audit | Platform audit services shall cover payments, verification, privileged admin, template issuance and credential changes. |
| 7 | IP ownership | Intellectual property rights and source codes for in-house applications shall solely lie with SPLOCA; unauthorised re-use/commercial/advertisement/research use is prohibited. |
| 8 | Non-prod data | Only anonymised or synthetic data may be used for development/testing; real equitable-distribution claimant-level data is prohibited. |
| 9 | Legacy compatibility | The solution shall be compatible with the existing legacy system/web app through agreed interfaces. |
| 10 | Document suites | Business-level interchange with in-use document software/subscriptions (for example Idea, Adobe Suite) shall be supported as interfaces allow. |
| 11 | Solution nature | The solution is a dedicated role-based official application — not merely a public-facing portal. |
| 12 | AI policy | Generative AI shall not be used nor accepted. Agentic/rule-based automation only, with human verification and complete audit trail. |
| 13 | Per-module controls | Each module/sub-module shall participate in access control, security, backup, training and FAQ (with Modules 01 and 13). |

##### Modules that must interconnect on the common database

- Claims
- Legal
- Matter management
- Task management
- Court attendance and expense
- Collaboration
- Static / master data
- Property management
- Valuation

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Backup restore drill succeeds against RPO/RTO targets agreed with SPLOCA. |
| 2 | HTTPS/SSL and AES-256 controls are verified in acceptance testing. |
| 3 | Authorised users can navigate linked cross-module records without re-keying masters. |
| 4 | All approved services are deployed on the designated server with runbooks handed over. |
| 5 | Source code and artefacts are handed over under exclusive SPLOCA IP terms. |
| 6 | No generative AI is present; agentic assists require human confirmation. |
| 7 | Non-production environments contain only anonymised/synthetic data. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F18-001 | Instant backup & server storage | Provide instant backup to designated server storage with restore capability and per-module participation. |
| F18-002 | HTTPS/SSL transport security | Enforce encrypted HTTPS/SSL transport for web and service channels. |
| F18-003 | AES-256 encryption | Apply AES-256 encryption to protected data as specified. |
| F18-004 | Common interconnected database | Provide shared architecture linking all programme modules under RBAC without duplicate entry. |
| F18-005 | Designated-server cloud deployment | Deploy all approved services on the existing designated server/cloud architecture. |
| F18-006 | Platform forensic audit services | Provide cross-cutting forensic audit trails for privileged, verification, payment and template actions. |
| F18-007 | Legacy compatibility interfaces | Provide interfaces for compatibility with existing legacy system and web applications. |
| F18-008 | Document-suite interoperability | Support business-level interchange with in-use document tools and subscriptions. |
| F18-009 | IP handover & source-code ownership | Deliver source code and artefacts under exclusive SPLOCA IP ownership with no unauthorised re-use. |

---

## 7. End-to-End Workflows

### 7.1 FE to claim settlement (Claims spine)

1. FE registered / enriched (Module 03) with FIR/court/notification references.  
2. Assets attached; valuation commissioned; auction/recovery updates recovered funds (Modules 04, 14).  
3. Depositors and documents ingested with OCR/verification (Module 05); investments recorded (Module 06).  
4. Claim notification published; claims intake (staff-mediated and/or OOK online) (Module 07).  
5. Verification (human + agentic assists) → CA approval → settlement calculation → NEFT/RTGS payment → closure (Module 07).  
6. Equitable distribution / Special Court inputs prepared from approved data (Module 03).  

### 7.2 Legal matter lifecycle

1. Matter created and classified; variables captured (Module 09).  
2. Library research via NL/Boolean search (Module 08).  
3. Tasks assigned; collaboration Limited/Community; communications retained (Module 10).  
4. Hearings attended; expenses captured (Module 12); Android field use (Module 17).  
5. Orders/petitions/SOBs filed into library and matter dossier (Modules 08–09).  
6. Template notices/drafts issued as needed (Module 15).  

### 7.3 Seized property valuation (3(2) → auction readiness)

1. Office creates asset and assigns approved valuer (Module 14).  
2. Valuer inspects on Android with GIS media (Modules 14, 17).  
3. Method-specific valuation and Forms V-1…V-4 / V-6…V-8 completed.  
4. CA assesses; accept/reject/revalue/SCN; auction photos selected.  
5. Valuer billed; asset status and recovered value flow to Modules 04 and 07.  
6. Movables coded (eValueM); cash/FX damage → RBI application (Modules 04, 14).  

### 7.4 Grievance / FIR reference track

Complaint logged → FIR / investigation / charge-sheet stages updated with actions → linked to FE/depositor as authorised → RTI flags maintained separately (Module 15). Investigation casework remains outside the application.

### 7.5 Identity & bank verification sub-flow

Upload/OCR → forgery screen flags → Aadhaar/PAN → OTP phone → address pin/Digi pin/geo (RPAD if mismatch) → bank/IFSC checks → penny-drop record → mismatch queries to officer (Module 05).

---

## 8. Access Control / RBAC

| Element | Model |
|---------|--------|
| **Identity** | Person ↔ **Post/Position** ↔ Role(s) |
| **Visibility** | Hierarchy + need-to-know |
| **Collaboration** | Limited (named members) vs Community (authorised population of the space) |
| **Documents** | Controlled rights (view/download/share/edit) |
| **Modules** | Each module/sub-module has in-built access control |
| **External** | Valuers see assigned assets only; OOK claimants see only their constrained claim path |
| **Admin** | Credential lifecycle for officers, contract staff, guards, valuers |

No role-only model. Credential sharing is prohibited by policy; the system must support individual attribution.

---

## 9. Channels

| Channel | Audience | Scope |
|---------|----------|-------|
| **Staff Web** | SPLOCA officers, Legal Cell, admin/IT, authorised posts | Full programme modules per RBAC |
| **Android — Legal** | Advocates & Legal Cell | Module 17 legal feature set |
| **Android — Valuation** | Assigned valuers / field officers | Module 14/17 valuation field set |
| **Constrained claim intake (OOK)** | Out-of-Karnataka claimants | Module 07 limited online submission only |
| **Staff-mediated intake** | In-Karnataka claimants (via office) | Digitised claim capture; not open public portal |
| **Public portal (existing)** | General public | **Out of scope** as primary solution; legacy compatibility only |

---

## 10. Integrations

| Integration | Business purpose |
|-------------|------------------|
| Existing **Aadhaar** online verification | Identity verification |
| **PAN** verification provision | Identity verification |
| **OTP** gateway | Phone verification |
| **SMS** | Contact and operational notifications |
| **Email sync** | Team communication / bank-officer verification mail |
| **Geocoding / reverse geocoding** | Address↔coordinates; valuation GIS |
| **Digi pin / pin-code & geo DB** | Address verification |
| **Karnataka bank / branch / IFSC DB** | Bank verification |
| **Contracted bank penny-drop** | Account existence/name match results + audit |
| **Payment rails (NEFT/RTGS)** | Claim payment batches (as operated by authorised banking process) |
| **Legacy SPLOCA systems / existing web** | Compatibility and agreed data exchange |
| **e-Governance auction touchpoints** | Auction process consultation/status |
| **Document suites (Idea, Adobe, etc.)** | Interchange with in-use document tools as interfaces allow |
| **Play Store / enterprise Android distribution** | Where specifically approved |

---

## 11. Audit, Compliance & Security

- Complete audit trail for verification decisions, penny-drop, payments, CA valuation actions, credential changes, template issuances and privileged access.  
- Forensic audit module/capability for claim and financial trails.  
- HTTPS/SSL transport; AES-256 encryption; instant server backup.  
- No generative AI; agentic/rule-based only with human verification.  
- RTI third-party seeker flagging.  
- BSA 2023 and original-document necessities inform in-Karnataka intake design.  
- IP and source code solely with SPLOCA.  
- Non-production environments: anonymised/synthetic data only.  
- Knowledge rights management and controlled sharing for sensitive legal knowledge.

---

## 12. Non-Functional Requirements

| Area | Expectation |
|------|-------------|
| **Security** | Role+post RBAC, encryption, OTP, audit, secure Android distribution |
| **Reliability** | Instant backup; restore drills; designated-server hosting |
| **Performance** | Search and dashboard responsive for operational caseloads (targets to be set with SPLOCA during detailed design) |
| **Usability** | Official bilingual needs if directed later; court-approved fonts/spacing for specified templates |
| **Auditability** | Immutable/append-only audit events for critical actions |
| **Interoperability** | Common DB; legacy compatibility; document-suite interchange |
| **Licensing** | Clear, non-speculative Android/Play Store licensing where approved |
| **Valuation field media** | Photos min. 4 × ≥5MB with GIS and date; video supported |
| **Time-box note (source FRS)** | eValueI source states development + alpha + beta live testing not exceeding **3 months** from contract for that valuation application — treat as a **client-stated target for the valuation track** to be reconciled in the overall programme plan |

---

## 13. Data Migration

**In scope.** Agreed corpora to be migrated/loaded as released by SPLOCA, including as available:

- Acts/Rules, opinions, Special/High Court orders, petitions, SOBs, written arguments  
- Contacts and matter records  
- FE, depositor, investment, claim, asset and valuation seed data  
- Keyword catalogues and template masters  

**Constraints:** No real equitable-distribution claimant-level datasets in development/test; use anonymised/synthetic data. Migration mapping and acceptance samples to be jointly agreed.

---

## 14. Phased Delivery

**Programme posture:** Single integrated programme delivery on the common platform (per Proceedings interconnection requirement), with internal workstreams that may complete at different times:

| Workstream | Modules (primary) |
|------------|-------------------|
| Foundation | 01, 02, 18 |
| Claims & FE | 03, 04, 05, 06, 07 |
| Legal | 08–13, 17 (legal) |
| Valuation | 14, 17 (valuation), touches 04 |
| Governance & admin | 15, 16 |

Detailed sprint/release plan is outside this SOW; valuation’s 3-month source note must be explicitly planned against the wider programme without dropping mandatory Proceedings items.

---

## 15. Deliverables

1. Production-grade web application on designated server covering in-scope modules.  
2. Android applications (Legal; Valuation) with approved distribution/licensing.  
3. Configured masters, templates, keyword catalogues and unique coding schemes.  
4. Migration scripts/loads for agreed datasets.  
5. Integration configuration for Aadhaar, OTP/SMS, email, geocoding, bank/penny-drop interfaces as authorised.  
6. Security, backup and encryption implementation with restore demonstration.  
7. Training content / FAQ per module (in-app).  
8. Complete **source code**, build artefacts and documentation under **exclusive SPLOCA IP**.  
9. User, admin and operations runbooks (no speculative third-party licence claims).  
10. Test evidence using anonymised/synthetic data only.

---

## 16. Acceptance Criteria (programme level)

1. All Modules 01–18 Key capabilities demonstrable per RBAC.  
2. End-to-end claim path (notification→payment/closure) completes with audit.  
3. Legal library search (NL + Boolean) and matter dashboard accepted by Legal Cell SMEs.  
4. Valuation path (office create→field GIS→form→CA action→bill) accepted by valuation SMEs.  
5. Unique FE and property codes generated and used in search.  
6. OTP, address and bank/penny-drop verification recorded.  
7. RTI flag and grievance/FIR stage tracking operational.  
8. Template notices/orders generable and auditable.  
9. HTTPS, AES-256 and backup restore demonstrated.  
10. Common DB cross-links work without duplicate entry for authorised users.  
11. No generative AI present; agentic assists require human confirm.  
12. Source code and IP handover completed to SPLOCA.  
13. Android licensing documentation clear and as approved.

---

## 17. Expected Benefits

- Single official platform for claims, legal and valuation instead of fragmented tools/portals.  
- Higher integrity of claimant identity, bank and document verification.  
- Faster, auditable claim settlement against recovered funds.  
- Court-ready legal research and matter operations for advocates and Legal Cell.  
- Field-verified, GIS-backed valuation with CA oversight and billing.  
- Traceable grievances/FIR references and RTI third-party visibility.  
- SPLOCA ownership of IP and deployment on controlled infrastructure.

---

## 18. Assumptions & Dependencies

1. SPLOCA designates server/cloud and provides timely access for deployment.  
2. Existing Aadhaar verification service remains available for integration.  
3. Contracted bank supports penny-drop result exchange as agreed.  
4. Karnataka IFSC/branch reference data is supplied or licensed for use.  
5. Geocoding provider/API will be approved by SPLOCA (secure).  
6. Legacy system interface points and credentials will be provided.  
7. Court-approved fonts/spacing specimens will be supplied for templates that require them.  
8. Valuation manuals, adjustment factor tables and Form specimens in the eValueI FRS are authoritative for Module 14.  
9. In-Karnataka claim intake remains staff-mediated unless SPLOCA later expands online policy.  
10. Market intelligence and investigation casework stay outside this application.  
11. Form V-5 remains out of scope unless supplied.  
12. Hardware, scanning bureau and physical auction execution remain SPLOCA/other agency responsibilities.  
13. Prior demo findings on the public portal are treated as context only; this SOW specifies the dedicated official platform.  
14. “RD” means Revenue Department unless SPLOCA confirms otherwise; “SOB” means Statement of Objections unless a different docket label is confirmed.

---

## 19. Vendor Response Expectations

Vendors / implementing partners should respond with:

1. Module-wise compliance matrix against Modules 01–18 and each `Fxx-xxx` capability (Comply / Partially comply / Not comply) with notes.  
2. Proposed workstream plan reconciling valuation time-box with full programme scope.  
3. Approach to agentic (non-generative) automation, human verification and audit.  
4. Android distribution and licensing proposal (enterprise and/or Play Store).  
5. Migration approach using only anonymised/synthetic non-prod data.  
6. Security, backup, encryption and designated-server deployment approach.  
7. Explicit affirmation of **SPLOCA-exclusive IP and source-code ownership**.  
8. Assumptions, dependencies and exclusions — especially online claim channel boundaries and MI/investigation exclusions.  
9. Team profiles for claims, legal-tech, GIS/valuation and government security delivery.  
10. No generative-AI components in the commercial or technical proposal.

---

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Access Control, Identity & Need-to-Know Security | Shared | F01-001 … F01-007 (7) |
| 02 | Reference Masters, Keywords & Unique Coding | Shared | F02-001 … F02-007 (7) |
| 03 | Financial Establishment (FE) Management | Business | F03-001 … F03-009 (9) |
| 04 | Asset Attachment, Recovery & Auction Management | Business | F04-001 … F04-008 (8) |
| 05 | Depositor Master, Document Intake & Identity Verification | Business | F05-001 … F05-009 (9) |
| 06 | Investment Portfolio Management | Business | F06-001 … F06-008 (8) |
| 07 | Claim Lifecycle Management | Business | F07-001 … F07-010 (10) |
| 08 | Legal Knowledge Library & Search | Business | F08-001 … F08-011 (11) |
| 09 | Matter Management | Business | F09-001 … F09-010 (10) |
| 10 | Collaboration, Tasks & Team Communication | Business | F10-001 … F10-014 (14) |
| 11 | Unified Contact Database | Business | F11-001 … F11-005 (5) |
| 12 | Court Attendance & Expense Management | Business | F12-001 … F12-004 (4) |
| 13 | Knowledge, Expertise, Tools & Training | Business | F13-001 … F13-009 (9) |
| 14 | Seized Property Valuation & Asset Management (eValueI / eValueM) | Business | F14-001 … F14-018 (18) |
| 15 | Grievance, FIR Tracking, RTI Flags & Statutory Templates | Business | F15-001 … F15-007 (7) |
| 16 | Administration, Inventory & Support | Shared | F16-001 … F16-002 (2) |
| 17 | Mobile Applications (Legal Cell & Valuation) | Technical | F17-001 … F17-010 (10) |
| 18 | Platform Security, Backup, Encryption & Deployment | Technical | F18-001 … F18-009 (9) |
| | **Total** | | **157 features** |

### Appendix B — Source Traceability Map

| Source | Primary SOW coverage |
|--------|----------------------|
| Proceedings 10-08-2026 (items 1–23) | Channels; OCR/forgery; OTP/address/bank/penny-drop; Legal web+Android; tasks/attendance/library; collaboration; Valuation web+Android; CA assessment/CAD; admin credentials & inventory tickets; grievances/FIR; MI exclusion; no generative AI; RTI flag; common DB; designated server & IP; synthetic test data; templates; unique FE/property codes; per-module ACL/backup/training/FAQ |
| Business Process Flow | Phases context; Modules FE, Asset, Depositor, Portfolio, Notification, Submission, Verification, Approval, Settlement, Payment; key aspects (legacy, agentic AI, forensic audit, document suites, court docs, penny-drop/excess, draft generation) |
| Legal Management Annexure-I | Modules 08–13, 17 (legal), parts of 01, 18 |
| eValueI / eValueM FRS | Module 14, 17 (valuation); **full field schedules in Appendix E** (methods, factors, proforma, Forms V-1–V-4 & V-6–V-8, eValueM tree, 3-month note) |

### Appendix C — Abbreviations

| Abbreviation | Expansion |
| ------------ | --------- |
| SPLOCA | Special Officer & Competent Authority (Government of Karnataka) |
| KPIDFE | Karnataka Protection of Interest of Depositors in Financial Establishments Act, 2004 |
| IMA | IMA & other KPIDFE / company fraud matters handled by SPLOCA |
| FE | Financial Establishment |
| CA | Competent Authority |
| RC | Regional Commissioner (RC Office) |
| RD | Revenue Department *(confirm if different)* |
| IO / IOs | Investigating Officer(s) |
| AC | Assistant Commissioner |
| OP | Opposite Party |
| SOB | Statement of Objections *(confirm docket label if different)* |
| OM / GO / SOP | Office Memorandum / Government Order / Standard Operating Procedure |
| DFPC | District Fraud Prevention Cell |
| OOK | Out of Karnataka |
| BSA | Bharatiya Sakshya Adhiniyam, 2023 |
| eValueI | Geo tagging & valuation of immovable assets |
| eValueM | QR coding and valuation of movables |
| HTTPS / SSL / AES | Transport security / AES-256 encryption as specified |

### Appendix D — Explicit exclusions reminder

1. Generative AI — prohibited.  
2. Market intelligence process/data and investigation process — excluded (notices/templates and references only).  
3. Public portal as primary official system — excluded.  
4. Real equitable-distribution data in dev/test — prohibited.  
5. Form V-5 — not in source PDF.  
6. Hardware / scanning bureau / physical auction execution — excluded.


### Appendix E — eValueI / eValueM Full Field Schedules, Forms & Coding (normative)

**Authority:** This Appendix is **normative** for Module 14 (Seized Property Valuation & Asset Management) and related Valuation Android capabilities (Module 17). It reproduces, without omission of field schedules, the valuation methods, adjustment-factor tables, property-specification proforma, Forms **V-1, V-2, V-3, V-4, V-6, V-7, V-8**, eValueM movable coding tree, and related FRS rows from `Projects/Fraud/originals/Main_Module_1_eValueI_FRS.md` (source PDF: *Main module 1.pdf*).

**Binding rule:** Implementation of Module 14 / Valuation Android **shall support every field, table column, formula, adjustment factor, declaration clause, and code node** listed below. Form **V-5** is absent from the source and remains out of scope unless SPLOCA supplies it.

**Cross-reference:** Module 14 Key capabilities F14-001 … F14-018 are summaries only; detailed data capture is defined exclusively by this Appendix.

**Source path:** `originals/Main_Module_1_eValueI_FRS.md`

---

## Functional Requirement Specification

| Sl.no | Module Name | Features | Requirements |
|------:|-------------|----------|--------------|
| 1 | User – Admin | Provision to create an Assets data by the office user through Web Application | The system should allow office user to login with User name and password. The Application should allow the office user to enter basic details (Office user ID, User Name, Designation, Mobile Number, Allotted FE name, FE Code, CA name and CA Code, Asset Description, Asset Location, Latitude & Longitude, Date of Attachment, Date of Absolute, Court Order, IO Valuation, Section 7(1) Valuation, Guidance / Market Value) |
| 2 | Valuer Details | Provision to create Approved Valuer data through Web Application | **1.** The Application should allow the office user to enter basic details (Office user ID, User Name, Designation, Mobile Number, Approved Valuer name, Valuer Code, Category, Order Number, Rates of Valuation & Incidental Costs, Assignment Number, Assignment Date, Assigned Property Details)<br>**2.** The Application should allow the Valuer user to enter basic details (User ID, User Name, Designation, Mobile Number, Valuer Code, Assignment Number, Valuer Names Allotted, Mobile Numbers, Date of Visit, Stage of Valuation) |
| 3 | Asset Details | The System make provision to register of Assets and valuers’ details using web application from office user login. | The system should allow office user to create Assets basic details (ID, Asset Name, Type, Asset details, Address, Boundaries (As per Document – North, South, East, West), Asset Measure, Asset Registration Date, Parties and Value Stamp Duty Paid & Registration Fee, FE Code, CA Code, Court Order number, Court Order details (provision to upload), Sale deeds Details (provision to upload), Category of Asset (Land, Property, Building, Lease Holding, Other) |
| 3 / Data Capturing – I | Data Capturing – I (Mined Data) | The App makes provisions to VALUER to mine data from web application, down load data from secure sources, enter the asset valuation details with Photo with GIS tagging, and video upload on a real-time basis. While selecting the asset by the valuer, the basic details about the asset entered by office user must be displayed on the page; later, the remaining valued data will be entered by the assigned valuer in another API based on the Valuation Method adopted. Make provisions to capture the valuer real-time GIS data with system date and time. | The App should allow Asset valuer to select the Assets which is already created and assigned by the office user using drop down.<br><br>**Preliminary Site Inspection Report**<br>**a.** First, Selecting the Asset name from drop down.<br>**b.** Once selected, basic details like **Asset Name, Details, Address, Asset Measure, Asset Registration number** are displayed.<br>&nbsp;&nbsp;&nbsp;&nbsp;**i.** The Sale deeds and court order uploaded file has to see when valuer click view button.<br>**c.** Asset is identified along with CA Name, Designation, Mobile Number and Office Address and FE Name & Code.<br>**d.** Location of Asset (Asset no, Address, width of approach road, type of road, landmark, surrounding area, **Boundaries (North, South, East and West)**)<br>**e.** School/ College, Hospital, Malls, Temples/ Mosque /Church, Police station, and Transportation facilities (Bus stand, Railway station, Airport) near location distance needs to be fetched automatically in the application.<br>**f.** Google Map link & QR Code of the link<br>**g.** Enable mobile app to capture photos (minimum 4 each at least 5mb) with GIS tag (API Geocoding). *(Handwritten note: with date on the photo)*<br>**h.** Upload Photo / Video<br>**i.** Captured Date and Time<br>**j.** Any negative factors which affect the property<br>**k.** Overall Observation by Valuer (Remarks) |
| 4 | Data Capturing – II (Analytical Data) | APIs of Valuation Methods | **a.** Select and Open Application<br>**b.** Select Valuation Format<br>**c.** Select Valuation Method<br>**d.** Enter Code to populate basic data of asset in the application<br>**e.** Enter data<br>**f.** Upload Pictures / Videos into Library |
| 5 | MIS reports and Admin | The system shall make provision to generate the report based on the valuation details entered by valuer. Make provision to create, update or delete the valuer/asset/officer user login credentials in the web application. | **a.** Select and Open Application<br>**b.** Select Valuation Report Format<br>**c.** Enter Code to populate basic data of asset in the application<br>**d.** Enter report<br>**e.** Tag Videos & Photos |
| 6 | CA Report on Valuation Report & Valuer Assessment | The system shall make provision to evaluate the Valuer Report on key parameters – Time Taken, Asset Category, Method Adopted, Adjustment Factors used, Section 7(1) Valuation, Guidance Value | **a.** Select and Open Application<br>**b.** Select Valuation Report<br>**c.** Enter CA Code to populate basic data of asset in the application<br>**d.** Enter report<br>**e.** Select Photos for display in Auction<br>**f.** Accept / Reject / Order Revaluation / Issue SCN to Penalize Valuer |
| 7 | Valuer Billing | The System shall prepare bill and voucher | **a.** Select and Open Application<br>**b.** Enter Valuer Code to populate basic data of Valuer<br>**c.** Select Valuation Report<br>**d.** Open CA Report<br>**e.** Open Billing Window (If CA has accepted)<br>**f.** Enter details<br>**g.** Submit Bill online & upload signed hard copy |

---

## Software

*Note (SOW clarification): The following stack wording is reproduced from the source eValueI FRS for completeness of Appendix E. Geocoding / reverse-geocoding capability is mandatory. Final implementation language and return formats are subject to SPLOCA technical approval and do not override the vendor-neutral stance of the main SOW body.*

Shall use **PHP** and a secure **Geocoding API** with:

1. **Geocoding** — Converts addresses into latitude and longitude coordinates or Place IDs that can be used to place markers on a map  
2. **Reverse geocoding** — Converts latitude/longitude coordinates or a Place ID into a human-readable address  

The return should be in **XML** or another compatible format in host PC / Android.

---

## Valuation Formats

### I. Cost of Construction Method

#### A. Accounts Method

1. Report of Materials Costs  
2. Report of Labour Costs  
3. Date of Construction Start & Completion  
4. Depreciation (Using Certified CLASSIFICATION OF STRUCTURES BASED ON SPECIFICATION WITH EXPECTED ECONOMIC LIFE AND RESIDUAL OR RESERVE VALUE OR SCRAP VALUE)  
5. Likely Market Value  
6. Certificate of all Accounts & Vouchers produced  

#### B. Comparable method – For built up properties

**(a) (Flats/Shops/Offices) In Apartments And Multi Storied Buildings:**

| Sr. No. | Description of property | Built up Area in Sqm. | Date of Sale / Transfer | Area of the Plot | FSI/FAR of the plot | Land appurtenant to Flat | Apparent consideration | Name of seller / purchaser | Register No. |
|--------:|-------------------------|-----------------------|-------------------------|------------------|---------------------|--------------------------|------------------------|----------------------------|--------------|
| | | | | | | | | | |

**(b) Sale Instances For Built Up Properties: Adjustment factors –**

1. Location  
2. Situation  
3. Area  
4. Floor Difference  
5. Specifications  
6. Facilities / Services  
7. Time-gap  
8. Status (Lease or Freehold)  
9. Area of the Building  
10. Floor disposition  

**(c) Floor Disposition**

### II. Fair Market Value of Residential flat / commercial premises

**Weightage for floor disposition:**

| Floor | Weightage |
|-------|-----------|
| **a) Basement** – Used for storage purpose | 0.50A |
| **a) Basement** – Used otherwise | 0.75A to 0.90A |
| **b) Ground floor / 1st & Mezzanine floors** | A |
| **c) 2nd to 5th floor** | 0.95A |
| **d) 6th to 9th floor** | 0.90A |
| **e) 9th floor and above** | 0.85A |

**A** is the average unit cost of a flat.

*Note: In metropolitan cities like Mumbai/ Bangalore, the position is quite reverse in case of flats and multistoried buildings as the rates of upper floors go on increasing as compared to rate of G.F. and F.F. rates. The floors above G. floor and Pent houses fetch the most. Hence above factor should be carefully decided keeping in view the local trends and situations.*

### A. Land and Building Method

Applicable where:

**(a)** Self-occupied property.  
**(b)** Partly self-occupied (i.e., more than 60%) and balance tenanted.  
**(c)** Not possible to obtain fair and maintainable rent.  
**(d)** No direct evidence of rent such as schools and hospitals etc.  
**(e)** Property is not fully developed, or the return from the property is not commercial.

#### i. Land Value: (Derived)

#### ii. Identification of Comparable Sales

**1. Order of preference:**

**(a)** Sale of the adjacent land.  
**(b)** Sale of the land in the same locality.  
**(c)** Sale of the land in the neighborhood or adjoining localities.  
**(d)** Guideline rates issued by Local Authorities for land & construction.

**2. Factors affecting the land value:**

i) Size, ii) Shape, iii) Frontage, iv) Locality and surroundings, v) Amenities and facilities, vi) FAR or FSI, vii) Connectivity, viii) Road width.

**3. Number of sale instances:** Min 3

#### iii. Factors of Adjustment / Influence

**(a) Location & Situation:**

1. Development and the situation of the property in commercial or residential zones – **+/- 5%**  
2. Nearness to roads / proximity to civic amenities & transport facilities: **+/- 5%**  
3. Corner plots: **+/- 5%**

**(b) Time-gap: NPV of Past Sale Instances**

If no such sale instances are available then the price rise should be considered **18 to 24% P.A.**

**(c) Shape:** Adjustment factor **+/- 5%** depending upon the irregularity in shape and frontage of the plot & Vaastu

**(d) Size:** For large size plots **+/- 0.5% per 100 Sqm.**

**(e) FAR:** In case if sale instances of same or next above/below FAR are not available the adjustment in rates for FAR/ FSI should be made as under:

| FAR/FSI | Rate |
|---------|------|
| Additional 0.5 | 40% of basic rate |
| Next 0.5 | 35% |
| Next 0.5 | 30% |
| Next 0.5 | 25% |
| Next 0.1 | 45% |

**(f) Side Open:** Adjustment of **+5%** for each additional open side or vice-versa

**(g) Co-ownership Undivided Share, Rights & Interest:** Discount **5% to 12.5%** depending upon the Number of Co-owners and their relationship can be given.

**(h) Land Tenure:** Adjustment factor of **+/- 0.25%** for working out the land rate of free hold plot from the sale instance of lease hold plot and vice-versa.

**(i) Encumbrance / Civil Dispute / Lack of Approved Layout Plan / Encroachment:** Land value for the portion encumbered may be deferred for reasonable period to allow for depressing effect to the extent of **30%**.

**(j) Unearned increase:** If the property under valuation happens to be a lease hold plot then a certain percentage, as specified in the lease deed of unearned increase (current market rate less premium paid) is also to be deducted from the land value.

#### iv. Other Factors

Other factors effecting the price of property such as defect in title, mode of payment etc. (**Depressing Effect of 10%**)

#### v. Cost of Building

**FMV – Valuation Date – Cost of Reproduction minus the depreciation from the Date of Completion to Date of Valuation.**

#### vi. Depreciation

##### Calculation of Future life of a Building (Lf)

**i) Factors determining future life**

1. Date of commencement of construction  
2. Date of completion of construction  
3. Type and technique of construction  
4. Type and quality of construction materials  
5. Quality of workmanship  
6. Environment in which a building is situated  
7. Climatic conditions of the place  
8. Nature of past use and likely nature of future use  
9. Extent and quality of repair and maintenance  
10. Present physical condition, especially structural components and future repairability  
11. Obsolescence / Dilapidation  

**ii) Formula for Equivalent spent life (Le)**

The equivalent spent life (**Le**) of a building is the total life of the building (**L**) minus the assessed future life of the building (**Lf**).

**Le = L − Lf**

##### A. Straight Line Method

**Depreciation per annum = (Cost of reproduction − Salvage value) / Life of the building**

Assumption: Salvage value is typically taken as **10%** of the cost of reproduction.

**Depreciation per annum = 0.90 × Cost of reproduction / Life of the building**

##### Value of a property by the Land and Building Method

1. **Value of land** = A  
2. **Value of building:**  
   - 2.1 Reproduction cost of the building based on PWD-PAR = **B**  
   - 2.2 Amount of depreciation = (−) **C**  
   - 2.3 Builder’s efforts @ **3%** of B = **D**  
   - 2.4 Value of building **(B − C + D)** = **E**  
3. **Value of the property** = **A + E**

##### Quantum of Depreciation Formula

The Straight Line Method is often adopted for its simplicity in estimating depreciation.

**Q = (1 − p) × R × Le / I**

Where:

- **Q** = Quantum of depreciation  
- **R** = Reproduction cost of the building in Rupees  
- **p** = Percentage considered for estimating salvage value  
- **Le** = Equivalent spent life of the building in years  
- **I** = Life of the building in years  

With **p = 10%**: **Q = 0.9 × R × Le / I**

---

## Reporting Formats

### PROFORMA FOR RECORDING DETAILS OF SPECIFICATIONS OF THE PROPERTY

| Sl. No. | Details of Specification | Non Residential | Residential |
|--------:|--------------------------|-----------------|-------------|
| **1** | **FOUNDATION** | | |
| 1.1 | Type spread foundation/isolated/raft foundation / pile foundation (in case of pile foundation number of diameter and depth of pile be given). | | |
| 1.2 | Depth | | |
| **2** | **SUPERSTRUCTURE** | | |
| 2.1 | RCC framed construction / Load bearing | | |
| 2.2 | No. of Storeys | | |
| 2.3 | Internal & External Walls | | |
| 2.4 | Plinth height | | |
| 2.5 | Floor Height | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| | Door & Windows | | |
| **3** | **FITTINGS & FIXTURES** | | |
| 3.1 | Frames : Doors/Windows | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.2 | Shutters : Doors/Windows | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.3 | M.S. Grills Plain/Ornamental | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 3.4 | Fitting | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **4** | **FLOORING** | | |
| 4.1 | Types of Flooring : | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 4.2 | Dado | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **5** | **ROOFING** | | |
| **6** | **FINISHING** | | |
| 6.1 | Internal Walls | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| 6.2 | External walls | | |
| **7** | **Sanitary & Water Supply installation (Details as per measurement recorded)** | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **8** | **Electrical Installation (Details as per measurement recorded)** | | |
| | a) Basement | | |
| | b) Ground Floor | | |
| | c) First Floor | | |
| | d) Second Floor | | |
| | e) Third Floor | | |
| | f) Forth Floor | | |
| | g) Fifth Floor | | |
| | h) Sixth Floor | | |
| | i) Seventh Floor | | |
| | j) Eighth Floor | | |
| **9** | **External Services** | | |
| 9.1 | Sewer connected to municipal sewer line/septic tank | | |
| 9.2 | Water Supply independent arrangement with tube well / mpl. Supply. | | |
| 9.3 | Overhead Tank | | |
| 9.4 | Underground sump well | | |
| 9.5 | No. of pumps | | |
| 9.6 | Storm water drain | | |
| 9.7 | Horticulture | | |
| 9.8 | Compound lighting | | |
| **10** | **FACILITIES** | | |
| 10.1 a) | Passenger lift …………….. No. for …………….. person | | |
| 10.1 b) | Service Lift …………….. No. for …………….. Kg. | | |
| 10.2 | Generator …………….. No. of ……….. KVA | | |
| 10.3 | Pavement / Road & Path | | |
| 10.4 | Compound wall & gate | | |
| **11** | **Special Items** | | |
| 11.1 | Dry/Wet Riser | | |
| 11.2 | Fire protection system | | |
| 11.3 | Central air conditioning | | |
| 11.4 | Sound System | | |
| 11.5 | T.V. Antenna/ Dish / DTH | | |
| 11.6 | Lightning Conductor | | |
| 11.7 | Telephone Connection | | |

---

## SPLOCA VALUATION FORM V-1

**Report of Valuation of immovable property (other than agricultural lands, plantations, forests,) mines and quarries**

| Field | Value |
|-------|-------|
| Name of registered valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

### General

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner/owners  
4. If under joint ownership/co-ownership, share of each such owner. Divided / undivided?  
5. Brief description of the property  
6. Location, Street, Ward No.  
7. Survey/Plot No. of land  
8. Zone: Green Belt / Residential / Commercial / Mixed area / Industrial?  
9. Classification of locality: HIG / MIG / LIG  

10. **Proximity to civic amenities:**

| Amenity | Schools / Colleges | Hospitals | Offices | Markets | Cinemas / Malls |
|---------|--------------------|-----------|---------|---------|-----------------|
| Proximate (KM) | | | | | |

11. **Means and proximity to surface transport by which the locality is served:**

| Means of Transport | Public Transport | Auto / Taxi | Rail Station | Metro |
|--------------------|------------------|-------------|--------------|-------|
| Proximate (KM) | | | | |

### Land

12. **Area of land, shape, dimensions and physical features with documentary proof**

| Land Document | Shape | Side 1 (Mtr) | Side 2 (Mtr) | Side 3 (Mtr) | Side 4 (Mtr) | Area (Sq Mtr) | Surface |
|---------------|-------|--------------|--------------|--------------|--------------|---------------|---------|
| | | | | | | | |

13. **Roads, streets or lanes on which the land is abutting**

| Abutting Road | Major | Minor | Cross Road | Lane |
|---------------|-------|-------|------------|------|
| Name | | | | |
| Length | | | | |

14. Freehold or Leasehold?  

15. If leasehold, the name of lessor/lessee, nature of lease, dates of commencement and termination of lease and terms of renewal of lease:  
   - (i) Initial premium  
   - (ii) Ground rent payable per annum  
   - (iii) Unearned increase payable to the lessor in the event of sale or transfer  

16. Any restrictive covenant to use of land? If so, upload copy.  

17. Any agreements of easements? If so, upload Copies  

18. Approved Town Planning Scheme or any Development Plan of Government or any statutory body? If so, upload Particulars  

19. Any contribution towards development or is any demand for contribution outstanding?  

20. Whole or part of the land notified for acquisition by Government or any statutory body? Give date and number of the notification  

21. Upload a dimensioned site plan  

### Building Particulars

21. *(Duplicate numbering in source)* Any plans and elevations of structures standing or lay-out plan? Upload  

23. Technical details of the building: **[Use Annexure to this Form]**  

24. (i) Owner-occupied / tenanted / both?  
    (ii) Specify portion and extent under owner-occupation  

25. What is the Floor Space Index permissible and percentage actually utilized?

| FSI Permissible | FSI Utilized | Violation |
|-----------------|--------------|-----------|
| | | |

26. **Rents**

| Sl No | (i) Names of tenants/ lessees/ licensees | (ii) Portions in their occupation | (iii) Monthly or annual rent/ compensation / license fee / Maintenance | (iv) Payment for Furniture / Fittings | Relationship to Owner | Total Receipts from Property |
|------:|------------------------------------------|-----------------------------------|------------------------------------------------------------------------|---------------------------------------|-----------------------|------------------------------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

27. Occupants related to, or close business associates of, the owner:  

28. **Water and electricity charges borne by:**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Water Charges Monthly | | |
| Electricity Charges Monthly | | |

29. **Cost of repairs and maintenance borne by:**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Annual Repairs | | |
| Common Area Maintenance & Security (including Lift, Pump) | | |

30. **Statutory Dues**

| | Owner Share | Lessee Share |
|--|-------------|--------------|
| Property Tax Annual | | |
| Insurance | | |

31. Any dispute between landlord and tenant pending in a court of law:  

### Sales

32. **Sales instances in the locality**

| Sl No | Name & Address of Property | Registration Number | Date of Sale | Area Sold | Sale Price |
|------:|----------------------------|---------------------|--------------|-----------|------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

33. Land rate adopted in this valuation:  

34. Basis of arriving at the land rate in absence of Sale Instances  

### Cost of Construction

35. **Construction Period**

| Commencement of construction | Completion of Construction |
|------------------------------|----------------------------|
| | |

36. Method of construction — by contract/by employing labour directly/both?  

37. Upload Contract, Agreements if available  

38. For items of work done by engaging labour directly, give basic rates of materials and labour supported by documentary proof  

### Part II – Valuation

Approach to valuation of the property and indicate how the value has been arrived at, supported by necessary calculations.

### Part III – Declaration

I hereby declare that —

**(a)** the information furnished in Part I is true and correct to the best of my knowledge and belief;  
**(b)** I have no direct or indirect interest in the property valued;  
**(c)** I have personally inspected the property on ________  

| | |
|--|--|
| Date: | Place: |
| Name & Digital Signature of Registered Valuer: | |
| Name & Digital Signature of Expert Valuer (if any): | |

---

### SUB-ANNEXURE TO FORM V-1

| Sl. No. | Technical details | Main building | Annexe | Servants' quarters | Garages | Pump house |
|--------:|-------------------|---------------|--------|--------------------|---------|------------|
| 1. | No. of floors and height of each floor | | | | | |
| 2. | Plinth area floor-wise (As per IS : 3861-1966) | | | | | |
| 3 | Year of construction | | | | | |
| 4 | Estimated future life | | | | | |
| 5 | Type of construction load bearing walls/RCC frame/steel frame | | | | | |
| 6 | Type of foundations | | | | | |
| 7 | **Walls** | | | | | |
| | (a) Basement and plinth | | | | | |
| | (b) Ground floor | | | | | |
| | (c) Superstructure above ground floor | | | | | |
| 8 | **Partitions** | | | | | |
| | Doors and windows (Floor-wise). | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc. | | | | | |
| 10 | **Flooring (Floor-wise).** *(Sl. No. 9 not present in source)* | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc | | | | | |
| 11 | **Finishing (Floor-wise).** | | | | | |
| | (a) Ground floor | | | | | |
| | (b) 1st floor | | | | | |
| | (c) 2nd floor, etc. | | | | | |
| 12 | Roofing and terracing | | | | | |
| 13 | Special architectural or decorative features, if any | | | | | |
| 14 | (i) Internal wiring surface or conduit | | | | | |
| | (ii) Class of fittings : Superior/ordinary/poor | | | | | |
| 15 | **Sanitary installations.** | | | | | |
| | (a) (i) No. of water closets | | | | | |
| | (ii) No. of lavatory basins | | | | | |
| | (iii) No. of urinals | | | | | |
| | (iv) No. of sinks | | | | | |
| | (v) No. of bath tubs | | | | | |
| | (vi) No. of bidets | | | | | |
| | (vii) No. of geysers | | | | | |
| | (b) Class of fittings : Superior Coloured /superior white/ ordinary | | | | | |
| 16 | **Compound wall.** | | | | | |
| | (i) Height and length | | | | | |
| | (ii) Type of construction | | | | | |
| 17 | No. of lifts and capacity | | | | | |
| 18 | Underground Pump – Capacity and type of construction | | | | | |
| 19 | **Overhead tank :** | | | | | |
| | (i) Where located | | | | | |
| | (ii) Capacity | | | | | |
| | (iii) Type of construction | | | | | |
| 20 | Pumps – No. and their horse power | | | | | |
| 21 | Roads and pavings within the compound, approximate area and type of paving | | | | | |
| 22 | Sewage disposal whether connected to public sewers. If septic tanks provided, No. and capacity | | | | | |

---

## SPLOCA VALUATION FORM V-2

**Report of valuation for agricultural lands other than forests & commercial plantations**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose for which valuation is made  
2. Date as on which valuation is made  
3. Name of the owner/owners of agricultural land  
4. If the agricultural land is under joint ownership/co-ownership, share of each owner: Are the share undivided?  
5. Particulars of agricultural land :

| Sl. No. | Survey No.(s) of land(s) | Village, tehsil and district in which situated | Area of the land (in hectares) | Classification of land(s) as given in the land revenue records etc. | Crops grown during the year | Annual land revenue, if any |
|--------:|--------------------------|------------------------------------------------|--------------------------------|-----------------------------------------------------------------|-----------------------------|-----------------------------|
| | | | | | | |

6. Does the land fall in an area included in any Town Planning Scheme or any Development Plan of Government or any statutory body? If so, upload order  

7. **Special features of the land**

| Soil Type | Quality and fertility | Mode of Irrigation (i.e., whether by wells, electric tube-wells or tube-wells or canal) | Distance from village/ town /markets | Approach roads | Means of transportation | Cultivated by self or tenants. Any other features |
|-----------|----------------------|------------------------------------------------------------------------------------------|--------------------------------------|----------------|-------------------------|---------------------------------------------------|
| | | | | | | |

8. **Comparable case of the sale relied upon :**  
   - **(a)** Type of Property  
   - **(b)** Distance of Locality of Sale  
   - **(c)** Date of Transaction  
   - **(d)** Sale Price and Unit value  

9. **Unit value adopted :** Valuer should discuss in details his approach to valuation of the land and indicate how the value has been arrived at  

10. Value of land(s)  

11. **Declaration:** I hereby declare that—  
    - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
    - **(b)** I have no direct or indirect interest in the land valued;  
    - **(c)** I have personally inspected the land(s) and I have examined the revenue records of village/tehsil  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## SPLOCA VALUATION FORM V-3

**Report of valuation of forests & plantations**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the forest / plantation  
4. If the forest is under joint ownership/co-ownership, share of each owner: Are the share undivided?  
5. Location of the forest / plantation  
6. Area of forest/ plantation (in hectares)  
7. **Valuation of the forest** *(the valuation should be made indicating in detail the different factors which have been taken into account, such as the kind of timber the density of the forest mode of transportation of timber, etc.)*

| Land Location | Area in Hectares | Sale Instance Locality | Sale Instance Outside Locality | Sale Value | Market Value of Land |
|---------------|------------------|------------------------|--------------------------------|------------|----------------------|
| | | | | | |

| Tree Type | Number | Average Age | Value | Availability of Transportation Route | Commercial Value of Trees |
|-----------|--------|-------------|-------|--------------------------------------|---------------------------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

8. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the forest valued;  
   - **(c)** I have personally inspected the forest and I have examined the revenue records of village/tehsil/district  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## SPLOCA VALUATION FORM V-4

**Report of valuation of mines and quarries**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner/owner(s)/Lease holder of the mine(s)/quarry(ies)  
4. If joint ownership/co-ownership / joint lease, share of each: Are the share undivided?

| | Joint Owner / Lessee 1 | Joint Owner / Lessee 2 | ADD Joint Owner / Lessee 3 |
|--|------------------------|------------------------|----------------------------|
| Share | | | |
| Divided / Undivided | | | |

5. The name and location of the mine(s)/quarry(ies)  
6. Area of mine(s)/quarry(ies)  
7. **Valuation of the mine(s)/quarry(ies) excluding machinery, plant, buildings and furniture and fittings** *(the valuer should discuss in details the factors which have been taken into account including the average annual output during the past three years, the extractable reserves, the area available for extraction, the thickness of the seam, the stage of development, depillaring, Geological disturbances, etc.)*  

8. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in mine(s)/quarry(ies) valued;  
   - **(c)** I have personally inspected the mine(s)/quarry(ies) and I have examined the revenue records of village/ tehsil /district  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer | |
| Name & Signature of Expert Valuer (if any) | |

---

## Additional Module: QR Coding and Valuation of Movables (eValueM)

### Categorization and Tagging of Movables

#### 1. Coding

| Sl | Item Category | Code & Sub Code | Object Code | Detail Code |
|----|---------------|-----------------|-------------|-------------|
| i. | **Air Conditioners:** | **AC** | | |
| | - Split | -SPL | | |
| | - Window | -WIN | | |
| ii. | **Computers & Peripherals:** | **PCP** | | |
| | - Desktop | -DT | | |
| | - Laptop | -LT | | |
| | - IPAD | -IPD | | |
| | -- Peripherals | | --P | |
| | --- Keyboard | | | ---KB |
| | --- Mouse | | | ---MUS |
| | - Printer | -PR | | |
| | -- Multifunction | | --MF | |
| | -- Large Format | | --LF | |
| | - Copier | -CP | | |
| | - Scanner | -SCN | | |
| | - Storage Drive | -STR | | |
| iii. | **Electrical & Electronic Goods:** | **EEG** | | |
| | - TV | -TV | | |
| | -- LCD | | --LCD | |
| | -- LED | | --LED | |
| | - CD/ DVD Player | -PLR | --CD/--DVD | |
| | - Mobile Phone | -MBL | | |
| | -- Android | | --AND | |
| | -- Apple | | --APL | |
| | - Domestic | -DOM | | |
| | -- Refrigerator | | --FRG | |
| | -- Microwave | | --MWV | |
| | -- Heater | | --HTR | |
| | -- Washing Machine | | --WSH | |
| | -- Vacuum Cleaner | | --VCM | |
| | -- UPS | | --UPS | |
| | -- Light Fittings | | --LGT | |
| | -- Fan Fittings | | --FAN | |
| | - Commercial | -COMM | | |
| | -- Calculator | | --CAL | |
| | -- POS Terminal | | --POS | |
| | -- Testing Equipment | | --TST | |
| iv. | **Furniture & Fixtures:** | **FF** | | |
| | - Sofa | -SF | | |
| | - Chair | -CHR | | |
| | - Table | -TBL | | |
| | - Storage | -STR | | |
| v. | **Machinery, Tools & Plant:** | **MTP** | | |
| | - Kitchen | -KCN | | |
| | -- Stove | | --STV | |
| | -- Utensils (Preparation) | | --UTPR | |
| | -- Utensils (Cooking) | | --UTCK | |
| | -- Utensils (Serving) | | --UTSRV | |
| | - Living | -LIV | | |
| | -- Gym | | --GYM | |
| | -- Other(Specify) | | --OTH | |
| | - Garden | -GDN | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| | - Factory | -FCT | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| | - Maintenance | -MNT | | |
| | -- Tools | | --TL | |
| | -- Machinery | | --MCN | |
| vi. | **Textiles including Sarees, Dress Materials, Men’s & Children’s Wear:** | **TXT** | | |
| | - Male | -ML | | |
| | -- Clothing | | --CLTH | |
| | -- Dress Materials | | --DRM | |
| | -- Undergarments | | --UGM | |
| | - Female | -FML | | |
| | -- Saree | | --SRI | |
| | -- Dress | | --DRS | |
| | -- Dress Materials | | --DRM | |
| | -- Undergarments | | --UGM | |
| | - Child | -CHD | | |
| | -- Dress | | --DRS | |
| | -- Dress Materials | | --DRM | |
| | - Drapery | -DRP | | |
| vii. | **Vehicles:** | **VEH** | | |
| | - Car | -CR | | |
| | -- Sedan | | --SDN | |
| | -- Hatchback | | --HTC | |
| | -- SUV | | --SUV | |
| | -- MUV | | --MUV | |
| | - Truck | -TRK | | |
| | - Bus | -BUS | | |
| | - Utility | -UTL | | |
| | -- Tractor | | --TRT | |
| | -- Harvester | | --HVR | |
| | -- Cultivator | | --CLT | |
| | -- Ambulance | | --AMB | |
| | -- Earth Mover | | --ERM | |
| | -- Fire Engine | | --FRE | |
| | - Two/ Three Wheeler | -BIK | | |
| | -- Bicycle | | --BCL | |
| | -- Scooter | | --SCT | |
| | -- Motorbike | | --MBK | |
| | -- Auto | | --AUT | |
| viii. | **Art Objects & Handicrafts:** | **ANC** | | |
| | - Art | -ART | | |
| | -- Modern | | --MOD | |
| | -- Antique | | --ANQ | |
| | --- Original | | | ---ORG |
| | --- Copy | | | ---CPY |
| | -- Rare | | --RARE | |
| | --- Original | | | ---ORG |
| | --- Copy | | | ---CPY |
| | - Handicraft | -CFT | | |
| | -- Handmade | | --HND | |
| | --- Traditional | | | ---TDN |
| | --- Antique | | | ---ANQ |
| | -- Machine Made | | --MCN | |

### Valuation & Recording

#### A. Tabulation

| Code of Category | Serial No of Group | Name of Item | Serial No of Item, Description including Material & Colour (in order) | Make / Brand if available | Rating if Available (Exclusive / High / Average / Low) | Condition (New / Unused / Working / Damaged (Details) / Scrap / Obsolete) | Appreciating / Depreciating |
|------------------|--------------------|--------------|-----------------------------------------------------------------------|---------------------------|--------------------------------------------------------|---------------------------------------------------------------------------|----------------------------|
| | | | | | | | |

#### B. Prepare Tagging Sticker / Label with Category, Name, Serial No, Condition

#### C. Upload Photo of Group of Similar Items Placed together & individual sample photos

---

## SPLOCA VALUATION FORM V-6

**Report of valuation of equipment, furniture, machinery and plant**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the machinery/plant, under valuation  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description of the machinery/plant and the purpose for which it is utilised  
6. Valuation of the machinery/plant  

| Item | Code | Description, Colour, Material | Make / Manufacturer | Model Number / Year of Production | Original Price, Present Market Price | Depreciation on Year of Valuation | Market Value |
|------|------|-------------------------------|---------------------|-----------------------------------|--------------------------------------|-----------------------------------|--------------|
| | | | | | | | |

7. **Declaration:** I hereby declare that—  
   - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the machinery/plant valued;  
   - **(c)** I have personally inspected the machinery/plant.  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer: | |
| Name & Signature of Expert Valuer (if any): | |

---

## SPLOCA VALUATION FORM V-7

**Report of valuation of Gemstones, Precious Metals & Jewellery**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the Gemstones, Precious Metals & Jewellery  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description & Valuation of each item of Gemstones, Precious Metals & Jewellery  

| Precious Item | Description | Unit | Gross Weight | Net Weight | Value of Stone | Value of Precious Metal | Total Value of Item |
|---------------|-------------|------|--------------|------------|----------------|-------------------------|---------------------|
| | | | | | | | |
| | | | | | | | |

6. **Special Value Enhancement:** (The valuer should discuss the special features, if any, of the jewellery, such as its antique value, aesthetic value, etc.)  

13. **Explanation of Rates Adopted.** *(Numbering as in source — skips from 6 to 13)*  

14. **Purity Testing Methods Adopted.**

**Testing Methods:**

1. **Digital Weighing Scale** (Sartorius & Wensar brand) with high sensitivity. Weights are reported in Grams and for Gemstones in Carats.  
2. **Gold Purity:** XRF Testing Machine (Maxsell)/ traditional touchstone method with Nitric Acid (HNO₃).  
3. **Silver Purity:** XRF Testing Machine (Maxsell)/ traditional method – Nitric Acid (HNO₃) and Salt Solution (NaCl).  
4. **Diamond:** A 10x, 14x & 20x triplet loupe for visual characteristics and CVD Test both random and continuous testing by Solitaire Diamond Institute, Bangalore / IGI & GTL.  
5. **Precious Gemstones:** 10x loupe for visual characteristics.  

### Sub-Annexure I to Form V – 7

| SL NO | PCS (IO No) | Item | Gross WT (Container no) | Net Weight | Purity (TREASURY NO.) | StoneWT | Stone Qty | RATE | C/s | C/s qty | C/s rate | Pure Metal | VALUE |
|------:|-------------|------|-------------------------|------------|-----------------------|---------|-----------|------|-----|---------|----------|------------|-------|
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | | | | | | | | | | | | | |
| | 0 | TOTALS | 0.00 | 0.00 | | 0.00 | 0 | | 0.00 | 0 | | 0.00 | 0 |

### Sub-Annexure II to Form V – 7

| Precious Item | Description | Unit | Gross Weight | Net Weight | Value of Stone | Value of Precious Metal | Total Value of Item |
|---------------|-------------|------|--------------|------------|----------------|-------------------------|---------------------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

15. **Declaration:** I hereby declare that—  
    - **(a)** the information furnished above is true and correct to the best of my knowledge and belief;  
    - **(b)** I have no direct or indirect interest in the jewellery valued;  
    - **(c)** I have personally inspected the jewellery.  

| | |
|--|--|
| Date: | Place: |
| Name & Signature of Registered Valuer: | |
| Name & Signature of Expert Valuer (if any): | |

---

## SPLOCA VALUATION FORM V-8

**Report of valuation of works of Art & Handicrafts**

| Field | Value |
|-------|-------|
| Name of Registered Valuer | |
| Registration No. | |
| Reference Number & Date | |
| CA | |
| Accused / FE | |

1. Purpose of valuation  
2. Date of valuation  
3. Name of the owner(s) of the Handicraft / Art Object  
4. If the asset is under joint ownership/co-ownership, share of each owner:  
5. Description & Valuation of each item of Handicraft / Art Object  

| Handicraft / Art Object | Description | Material | Dimensions & Weight | Value | Value Added for Hand Crafted | Value added for Antiquity | Value added for Rarity | Total Value of Item |
|-------------------------|-------------|----------|---------------------|-------|------------------------------|---------------------------|------------------------|---------------------|
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

7. **I hereby declare that—**  
   - **(a)** The information furnished above is true and correct to the best of my knowledge and belief;  
   - **(b)** I have no direct or indirect interest in the work(s) of Art & Handicrafts valued;  
   - **(c)** I have personally inspected the work(s) of Art & Handicrafts.  

| | |
|--|--|
| Date: | Place: |

---

**Note: Time period of Application development, alpha testing and beta live testing shall be not exceeding 3 months from date of contract.**

---

---

---

*End of Statement of Work — SPLOCA Integrated Claims, Legal & Asset Valuation Platform (v2.4)*
