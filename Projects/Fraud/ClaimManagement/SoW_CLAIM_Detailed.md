# Statement of Work

# Claim Management System (KPID / SPLOCA)

**Document type:** Production-grade Statement of Work (RFP discussion and internal estimation)  
**Project code:** CLAIM  
**Client / Authority:** Special Officer & Competent Authority (SPLOCA) — IMA and other KPIDFE cases, Government of Karnataka  
**Version:** 1.7  
**Date:** 14 August 2026  
**Status:** Draft for review  

---

## Document control


| Item                                    | Detail                                                                                                                                                                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                             | External RFP discussion **and** internal estimation baseline                                                                                                                                                        |
| **Authority statute**                   | Karnataka Protection of Interest of Depositors in Financial Establishments (KPID / KPIDFE) Act and connected rules                                                                                                  |
| **Source (authoritative)**              | (1) Claim Management System — Business Process Flow; (2) Proceedings of Meeting — Review of Existing SPLOCA Website, 12 August 2026 (client demo report) |
| **Related SOWs (same programme)** | **Legal Management Application** and **GIS field valuation (eValueI / eValueM)** are specified in separate SOWs. **Module 01 (Person–Post–Role access)** in this Claim SOW is the **shared user-management component** consumed by Legal Management and by GIS field valuation. |
| **Existing FE application** | **FE Management / Database Management** (Business Process Flow Module 1) is **already implemented** in the existing application and is **not rebuilt** here. This application imports FE details, Directors and Promoters, and Investment Schemes. |
| **Process start**                       | The application is used **after** a Financial Establishment (FE) is declared fraudulent and claim-settlement responsibility is handed to the Competent Authority                                                    |


---



## 1. Introduction

This Statement of Work defines the functional and business scope for a **separate Claim Management application** that digitises claim settlement carried out by the Competent Authority under the KPID Act.

The process begins only after a Financial Establishment is declared fraudulent and investor-claim settlement is handed to the Competent Authority. **FE Management is already implemented in the existing application** and is not rebuilt here; this application **imports** FE details, Directors and Promoters, and Investment Schemes, then supports officers through notification, intake, verification, approval, equitable settlement against recovered funds, payment and closure — with a single depositor identity across entities, auditable bank and document checks, and court-ready distribution outputs.

This application is a **dedicated official Claim Management system**. It is **not** an enhancement of the existing public website ([sploca.org](https://sploca.org/)), which the 12 August 2026 review found to be primarily a PDF / content publishing portal without usable staff modules, Person–Post–Role access, 2FA, or structured FE / depositor / asset / claim data.

---



## 2. Project Overview



### 2.1 Business context

A Financial Establishment may collect money from the public through multiple investment schemes (examples in source: IMA Jewels, Lancer Finance, Innovative Business Centre, and any other entity notified under the KPID Act). A single investor may invest in multiple schemes, make multiple investments under the same scheme, invest in different branches, and invest in multiple Fraudulent Entities.

Typical failure patterns include maturity amounts not paid, interest payments stopped, deposits not returned, offices closed, and directors unavailable. Investors complain to Police and Government. Police investigation (FIR, evidence, seizure, charge sheet) is **outside** this application. FIR number, Court Case Number and Government Notification remain in the **existing FE application** (not duplicated as an FE dossier here).

Government then invokes the KPID Act, appoints the Competent Authority, and issues ad-interim attachment of FE assets (including preliminary investigation orders, notices to suspected fraudsters, freezing orders under rule 5, and report to Government). **From this stage the claim-settlement system is in play.**

### 2.2 Solution character


| Characteristic        | Requirement                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nature**            | Dedicated official claim-settlement application (staff web), role- and post-based, with a **constrained** claimant path only where this SOW allows. Not a rebuild of the public `.org` content portal. |
| **Not**               | A rebuild of the existing FE Management application; a mass public self-service portal for in-Karnataka original-document filing; a replacement of police investigation systems; a generative-AI chatbot |
| **Online constraint** | Unrestricted online filing is **not acceptable** for in-Karnataka claimants because of age and socio-economic profile and the need for original documents under BSA, 2023. Online filing is allowed **only for out-of-Karnataka claimants**. An existing limited online access system is noted in the source; this SOW requires the **business outcomes** of claim submission, not a duplicate public portal |
| **AI policy**         | AI shall **not** be generative. Agentic / rule-based agents and bots may be built and deployed to assist extraction, matching, mismatch queries and calculations, always under **human verification** and a complete audit trail                                                                                                                                                                             |
| **Existing FE application** | FE Management is already live in the existing application. This claim application **imports only the minimal FE details** other modules need (FE details, Directors and Promoters, Investment Schemes). It does **not** re-implement the FE dossier. |




### 2.3 Primary users (indicative)


| User                           | Typical work                                                                                                                                      |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Competent Authority**        | Review verification reports; record claim decisions; oversee settlement and payment release                                                       |
| **IMA / SPLOCA officers**      | Use imported FE / director / scheme references; maintain depositor and investment records; run claim windows; staff-mediated intake; verify and evaluate claims; request additional documents |
| **Administrators**             | Credentials, reference catalogues, publication of notifications                                                                                   |
| **Out-of-Karnataka claimants** | Constrained online claim submission during an open claim window                                                                                   |
| **In-Karnataka claimants**     | Present original documents for **staff-mediated / assisted** digitisation (not unrestricted self-service filing)                                  |
| **Bank officers**              | Supply or confirm bank-return / account data (email-triggered verification unless data is submitted directly)                                     |


---



## 3. Project Objectives

1. Digitise end-to-end **claim settlement** after FE handover to the Competent Authority.
   - Depositor master, claim window, intake, verification, approval, settlement against recovered funds, payment and closure in this application, using imported FE / scheme references.

2. **Import minimal FE details** from the existing FE Management application (not rebuilt here).
   - **FE details** (unique ID, name / aliases).
   - **Directors and Promoters**.
   - **Investment Schemes**.
   - Full FE dossier (FIR, court, notifications, orders, company bank accounts, seized corpus, case status, dashboards) remains in the existing application.

3. Maintain **court-attached assets and recovered funds** as the settlement pool.
   - Asset register; attachment orders; valuation in e-format (valuation manual).
   - Title transfer, e-Khata, dues till Khata, auction tracking with e-Governance.
   - Supporting documents, status, history, ownership / association; depositor-to-asset link where applicable.
   - Recovered amount available for settlement.

4. Create a **single depositor profile** across all FEs.
   - **OCR intake:** searchable OCR, translation, format conversion (JPEG → PDF → DOC); original file unchanged.
   - **Four-parameter matching:** unique profile per depositor; four match parameters (to be confirmed by the Authority).
   - **KYC:** personal information, Aadhaar (verified — not unverified capture as proof), PAN, contact details, bank accounts, nominee, legal heir.
   - Depositor status, history and documents; depositor-wise tracking.
   - **Address / name tally:** pin code to actual areas; Aadhaar / PAN / EPIC vs bank passbook vs claim form.
   - **Mismatch queries:** auto-generated when those sources disagree.
   - One profile used across all Fraudulent Entities, schemes and branches.

5. Maintain every **investment** with calculated outstanding and collusion indicators.
   - Capture FE, scheme, customer ID, bond/MOU, receipt, dates, deposit amount, promised interest, amount already received.
   - Auto-calculate deposits, interest received, maturity violations, promised vs paid interest.
   - Outstanding balance (interest paid treated as principal repaid where the approved rule requires).
   - Depositor / colluder / accused categorisation; bank-returns analysis; bank-officer verification requests.
   - Cross-FE / FIR / seizure comparison; excess-payment analysis.

6. Operate the claim journey: **notification → intake → verification → approval → settlement → payment → closure**.
   - Notification: eligible FE, schemes, period, eligibility, required documents, instructions; window active.
   - Intake: staff-mediated original documents for in-Karnataka (BSA, 2023); constrained online only for out-of-Karnataka; existing limited online access covered as outcomes.
   - Verification: identity, investment, scheme, customer ID, deposits, uploads, bank, previous returns, existing claims, eligibility; additional-document loop.
   - Approval: Competent Authority — Approved / Partially Approved / Rejected / Pending Clarification, with remarks.
   - Settlement and payment: recovered funds, approved liability, previous returns/settlements, net payable; NEFT/RTGS batches; status, history, closure.

7. Produce **equitable distribution statements**, Special Court filing reports (from approved input formats), and automated operational reports from structured data (not PDF-only publishing).
   - Claimant, accused, colluder, address and vendor lists.
   - FE-wise (imported FE), depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, user/activity and Role/Post mapping reports; management dashboards.

8. Preserve **forensic-quality audit trails**.
   - Verification, penny-drop, excess-payment analysis, approval, payment and closure.
   - Person–Post–Role mapping history; login and security logs.
   - Agentic / rule-based assists only, with human verification; no generative AI.

9. Integrate with the **existing FE Management application**, legacy / web application, and in-use document software.
   - FE details, Directors and Promoters, and Investment Schemes imported for use by claim modules.
   - Idea, Adobe Suite and similar as interfaces allow; bank penny-drop recording; bank-officer email verification.

10. Enforce **Person–Post–Role access and staff identity** as required by the 12 August 2026 website review.
    - Unique Person per official; Post catalogue; Role-to-Post and Post-to-Person mapping with full history.
    - Official / administered staff identity (not personal email as the primary department path).
    - Email and mobile OTP **before** account activation; **2FA** for staff login.
    - No credential sharing; unique account per joiner; deactivate relieved staff.
    - Unverified Aadhaar attributes shall not be treated as identity proof.

---



## 4. In Scope / Out of Scope



### 4.1 In scope


| Area                                   | Included                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Channels**                           | Secure **staff web** application for official claim work; **constrained online** claim submission for **out-of-Karnataka** claimants during published windows; staff-mediated intake for **in-Karnataka** claimants. This is **not** an upgrade of the public `.org` PDF portal. |
| **Access, identity and 2FA**           | Unique **Person** per official; **Post** catalogue; **Role-to-Post** and **Post-to-Person** mapping with full history; role-based menus; official / administered staff identity; OTP **before** activation; **2FA** for staff; no credential sharing; joiner–mover–leaver |
| **FE details (imported)**              | **Import only** from the existing FE Management application: FE details, Directors and Promoters, Investment Schemes. The public website’s FE-name-only gap is not solved by rebuilding FE here. |
| **Assets & recovery (claim-enabling)** | Register attached assets; documents; status and history; ownership / association including depositor-to-asset where applicable; attachment orders; valuation e-format; title / e-Khata / dues; auction tracking; recovered amount for settlement |
| **Depositor master**                   | Structured depositor registration (not PDF-only); OCR / translation / format conversion; unique 4-parameter profile across FEs; verified Aadhaar and PAN (unverified Aadhaar shall not be treated as proof); contact, bank, nominee, legal heir; pin-code/address tally; mismatch queries; penny-drop; status, history and documents |
| **Claim lifecycle**                    | Claim registration and window; staff-mediated and constrained OOK submission; document upload; verification; processing workflow with stage audit (role, action, status, remarks, date/time, documents); approval/rejection; status tracking; history; settlement; NEFT/RTGS; closure |
| **Outputs**                            | Equitable distribution and Special Court report from approved inputs; automated reports and dashboards from structured data (FE-wise imported, depositor, asset, claim, verification, status, historical, user/activity, Role/Post mapping) |
| **Platform**                           | Approved Government of Karnataka domain / hosting identity (not `.org` as the primary official domain); staff UX with searchable dropdowns, filters and task-oriented screens; evidence-based UAT against employee roles |
| **Investment portfolio**               | Full investment history; auto-calculation of deposits, interest promised vs paid, maturity violations, outstanding balance (interest paid treated as principal repaid where the approved rule requires); categorisation of depositor / colluder / accused; bank-returns analysis; bank-officer verification requests; cross-FE / FIR / seizure comparison; excess-payment analysis |
| **Special claim situations**           | Ineligible depositors, deceased depositors, legal heirs, joint deposits, third-party payments, lost receipts, cash investments                                                                                                                                                                                                                                                     |
| **AI**                                 | Agentic / rule-based assists only; human verification mandatory; full audit                                                                                                                                                                                                                                                                                                        |
| **Integrations (business-level)**      | Existing **FE Management application** (import FE details, Directors and Promoters, Investment Schemes); legacy / existing web application; existing limited online access system (outcomes); in-use document software / subscriptions (for example Idea, Adobe Suite) as interfaces allow; bank penny-drop result recording; email for bank-officer verification |
| **Document handling & workflow**       | **Embedded** in the business modules (not a separate DMS or workflow product)                                                                                                                                                                                                                                                                                                      |




### 4.2 Out of scope


| Area                                                          | Excluded                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **FE Management / Database Management (BPF Module 1)** | **Not rebuilt.** Already implemented in the existing application. This claim application does not register FE dossiers, store FIR / charge sheet / court / government notification / court order artefacts, maintain FE company bank accounts or current case status, or hold the seized-document / market-intelligence / social-media corpus. Only FE details, Directors and Promoters, and Investment Schemes are **imported**. |
| **Criminal investigation process** | FIR registration, evidence collection, director identification, seizure operations, account freezing **as investigation work**, and charge-sheet filing remain outside this application (and, where already captured, in the existing FE application). |
| **Market intelligence & social-media investigation casework** | Remains in the existing FE application. Not implemented in this claim application. |
| **Generative AI**                                             | Any generative AI for unsupervised claimant communications, fabricated content, or free-form legal advice                                                                                                                                                          |
| **In-Karnataka unrestricted online filing**                   | Mass public self-service claim filing for in-Karnataka claimants where original documents and BSA, 2023 apply                                                                                                                                                      |
| **Personal-email primary registration for department users** | Department / staff users shall not register using personal consumer email as the primary identity path. |
| **Unverified Aadhaar as identity proof** | Capturing “Name as in Aadhaar” or Aadhaar-linked mobile **without verification** is not accepted as identity proof. |
| **Credential sharing** | Sharing an old employee’s login with a new joiner is prohibited. |
| **Public `.org` portal as the official application** | Extending [sploca.org](https://sploca.org/) as a PDF publishing site is not the delivery model. This SOW is a dedicated official application on an approved government domain / hosting identity. |
| **Hardware / scanning bureau / auction physical execution**   | Devices, scanners, physical auction conduct, RBI logistics                                                                                                                                                                                                         |
| **Hosting AMC / telecom**                                     | Beyond deployment onto the designated environment and documented runbooks, unless separately ordered                                                                                                                                                               |




### 4.3 Clarifying boundary — Online claims

Per Phase 4 of the Business Process Flow: from invocation of the KPID Act onwards, a full online system is **not acceptable** for in-Karnataka claimants (age / socio-economic profile and original documents under BSA, 2023). Online is allowed **only for out-of-Karnataka claimants**.

The source notes that a **limited online access system already exists** and that a new unrestricted online submission module is “not required” in that sense. This SOW still requires the **business outcomes** of Module 3B (validated claim pack, linked FE/scheme/investment, uploads) via:

- staff-mediated intake for in-Karnataka claimants; and  
- a constrained OOK path and/or integration with the existing limited online access system.

### 4.4 Clarifying boundary — Fraudulent Entity (existing application)

The Authority’s **existing application already implements** Business Process Flow Module 1 (FE Management / Database Management). This SOW is for a **separate Claim Management application**.

Other claim modules cannot run without an FE identity and schemes. Therefore this application **imports**, via integration, only:

| Imported from existing FE application | Used by |
|---------------------------------------|---------|
| **FE details** (unique ID, name / aliases) | Depositor (cross-FE profile), investment, assets, claim notification, intake, verification, settlement, lists |
| **Directors and Promoters** | Accused / colluder related checks and operational lists |
| **Investment Schemes** | Investment capture, claim notification (eligible schemes), intake (scheme selection), verification (scheme match) |

The following Module 1 items are **not** implemented in this application (they remain in the existing FE application):

- Store Court Case information  
- Store FIR references  
- Upload Government Notifications  
- Upload Court Orders  
- Maintain Company Bank Accounts  
- Maintain Claimant Database (claimant / depositor master is **built in this application**, Module 04)  
- Maintain current case status  
- Interlinked FE folders, keyword dashboards, seized-paper corpus, market intelligence, social-media investigation casework  

If investment analytics must compare against FIR or seized-FE databases, that comparison is a **lookup to the existing application**, not a local copy of those databases.

---



## 5. Solution Expectations (business-level)

1. **Dedicated official application, not the public PDF portal:** Officials run windows, intake, verification, approval and payment in this application. The existing website’s PDF publishing model is not the target solution.
10. **Person–Post–Role accountability:** Every privileged action is attributable to a named Person acting in a Post with mapped Roles. Mapping history is retained.
11. **Staff security baseline:** Official identity; OTP before activation; 2FA; no credential sharing.
12. **Structured data, not PDFs alone:** Depositor, asset, claim and payment records are captured as structured data so reports and verification can be automated.
13. **Usable staff UX and official domain:** Searchable dropdowns and filters; approved government domain / hosting identity.
2. **One depositor, many FEs:** A unique profile (four matching parameters) is maintained across all Fraudulent Entities.
3. **FIR / seized-FE data stays in the existing application:** Investment or claim checks that need FIR or seized-FE data look up that application. This application does not store the FE dossier.
4. **Source integrity:** OCR, translation and format conversion produce searchable working text **without altering** the original scanned file.
5. **Human-in-the-loop automation:** Agentic bots may propose extractions, mismatch queries, eligibility flags and settlement maths — officers and the Competent Authority decide.
6. **Settlement follows recovery:** Net payable is calculated from recovered funds, approved liability, previous returns and previous settlements.
7. **Court-ready outputs:** Equitable distribution statement and Special Court report are prepared from approved input formats.
8. **Forensic audit:** Penny-drop, excess-payment, verification decisions and payments leave a complete trail.
9. **Existing FE application is the FE master:** FE details, Directors and Promoters, and Investment Schemes are imported; they are not registered afresh here. Legacy / web application and document software are integrated at interface level.

---



## 6. Consolidated Functional Modules

Document handling and workflow are **embedded** inside business modules. Module numbers and feature IDs below are **authoritative** for downstream estimation.

Each module is presented as: purpose, source coverage, functional requirements, entity field details, acceptance criteria, and key capabilities.

---



### 01. Access Control, Person–Post–Role & Forensic Audit

**Purpose:** Provide a unique Person identity, Post catalogue, Role-to-Post and Post-to-Person mapping (with history), RBAC, official staff identity, OTP-before-activation, 2FA, and a forensic audit trail — so every claim action is authorised and attributable. Corrects the access, login and credential gaps recorded in the 12 August 2026 website review.

**Type:** Shared  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Officer and Competent Authority actions throughout Modules 3A–4B; Key Aspect 3 (forensic audit); Module 3B constrained claimant path |
| Website review 12-08-2026 | Items 1–7 and Section 3: RBAC; 2FA; Person / Post / Role–Post / Post–Person / Permission; official identity; OTP before activation; no credential sharing |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Person | The system shall maintain each official as a unique **Person**. Every create, update, verify, approve, publish, pay and close action shall be attributable to a named Person acting in a Post. |
| 2 | Post and Role | The system shall maintain a **Post** catalogue and **Roles**. Roles shall be assigned to Posts (**Role-to-Post**). Posts shall be mapped to Persons (**Post-to-Person**) with effective dates. Complete mapping history shall be retained for audit. |
| 3 | RBAC | Users shall access only the modules and functions assigned to their Post/Role. Claim, depositor, FE, investment, asset and payment records shall be visible only to authorised Posts. |
| 4 | Official identity | Department / staff users shall be provisioned through **official or administered staff identity**. Personal consumer email shall not be the primary registration path for department users. |
| 5 | OTP before activation | Email and mobile OTP verification shall be completed **before** account activation. OTP after a already-successful registration is not acceptable. |
| 6 | 2FA | Two-Factor Authentication shall be required for **all staff** access. |
| 7 | Joiner–mover–leaver | Credential sharing is prohibited. Each Person has a unique account. Relieved staff shall be deactivated. New joiners receive **new** accounts mapped to the correct Post/Role. Deactivation shall not delete historical audit records. |
| 8 | Claimant channel | Out-of-Karnataka claimants shall authenticate only to the constrained submission path during an open claim window, and only for their own pack. In-Karnataka claimants shall not receive unrestricted self-service filing accounts. |
| 9 | Document rights | Identity proofs, investment proofs, bank documents, affidavits and related claim documents shall be subject to view / download rules. |
| 10 | Audit | The system shall retain a forensic audit trail of privileged actions and **login / security** events (who, when, what before/after, channel), covering verification, penny-drop, excess-payment, approval, payment, closure, credential and mapping changes. |

##### Entity fields — Person / Post / mapping

| Field | Notes |
|-------|-------|
| Person name | Legal name of the official |
| Person unique ID | System identifier |
| Official email / mobile | Administered staff contact; OTP status |
| Post | Official post (for example CA desk, Officer, Admin) |
| Role(s) attached to Post | Functional permissions |
| Post–Person effective from / to | Mapping period |
| Mapping history | Who changed, when, before/after |
| Credential status | Active / Inactive / Locked |
| 2FA status | Enrolled / not enrolled |
| Last credential change | Actor, timestamp, before/after (audit) |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A Person without the mapped Post/Role cannot open restricted claim packs or menus. |
| 2 | Role-to-Post and Post-to-Person changes record actor, timestamp and before/after. |
| 3 | Department users cannot complete primary registration on personal consumer email. |
| 4 | Account activation is blocked until required OTP succeeds. |
| 5 | Staff login requires 2FA. |
| 6 | Sharing a deactivated or previous occupant’s credentials with a new joiner is not possible as a supported process. |
| 7 | An OOK claimant can submit only within an open window and only for their own pack. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Person master | An Administrator opens Person administration, creates a new Person with legal name and unique ID, or searches an existing Person and updates particulars. The Administrator cannot create a second Person for the same official. Every later claim action (verify, approve, pay) is stored against this Person, not against a shared login. |
| F01-002 | Post, Role-to-Post and Post-to-Person mapping | An Administrator creates a Post (for example Officer or Competent Authority desk), assigns one or more Roles to that Post, then maps a Person to the Post with an effective-from date. When the mapping changes, the Administrator records effective-to, and the system keeps the previous mapping in history (who changed it, when, before/after). Staff see only the Posts currently mapped to them. |
| F01-003 | RBAC menus and need-to-know visibility | After login, the staff member sees only menus and screens allowed for their current Post and Roles. If they try to open another officer’s restricted claim pack, depositor KYC, asset or payment record, the system refuses access and writes an audit event. |
| F01-004 | Official staff identity | An Administrator provisions a department user on an official or administered email and staff identity. The sign-up / login path does not accept a personal consumer email as the primary department identity. The user cannot complete staff provisioning until that official identity is recorded. |
| F01-005 | OTP before account activation | The staff member (or Administrator triggering provisioning) enters official email and mobile. The system sends OTP to both. The user enters the OTPs. Only after both succeed does the Administrator (or the system) mark the account Active. The user cannot log in as Active if OTP is skipped or done after a “registration successful” message. |
| F01-006 | Two-Factor Authentication (staff) | A staff member enters user ID and password, then completes the second factor (for example OTP on the enrolled device/channel) before the session opens. Staff access without the second factor is refused. Claimants on the constrained OOK path are not given this staff 2FA enrolment. |
| F01-007 | Joiner–mover–leaver; no credential sharing | When an official leaves, the Administrator deactivates that Person’s account; the old password cannot be reused. When a new official joins, the Administrator creates a new Person, maps the correct Post, and issues new credentials. The Administrator has no supported action to copy or share the previous occupant’s login with the joiner. Historical audit rows remain after deactivation. |
| F01-008 | Constrained OOK claimant access | An out-of-Karnataka claimant logs in only to the constrained submission path, only while a claim window is open, and only sees their own pack. They cannot open staff menus, other claimants’ packs, or file after the window closes. In-Karnataka claimants are not given this self-service account. |
| F01-009 | Claim-pack document rights | An authorised Officer or Competent Authority opens a claim pack and views or downloads identity proof, investment proof, bank documents, affidavit or heir papers according to their Post rights. A user without download right can view but not download. The system records who viewed or downloaded which document and when. |
| F01-010 | Forensic and login/security audit | An authorised Administrator or auditor opens the audit register, filters by Person, Post, claim, date or action type, and retrieves who did what, when, on which record, before/after values, and channel (staff web, OOK path). This covers verification, penny-drop, excess-payment, approval, payment, closure, mapping changes, login success/failure and 2FA events. |


---



### 02. FE Master Import (from existing application)

**Purpose:** Obtain, by integration, the **minimal FE reference data** that claim modules need — FE details, Directors and Promoters, and Investment Schemes — from the existing FE Management application. This module does **not** create or maintain an FE dossier.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Business Process Flow | Module 1 activities: Register FE details; Capture Directors and Promoters; Configure Investment Schemes — **consumed via import only**. Remainder of Module 1 stays in the existing application. |
| Client direction | FE Management already implemented; this is a separate Claim Management application |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Import FE details | The system shall import FE details required by claim modules, including unique ID and name / aliases, from the existing FE Management application. Officers shall **not** register a new FE dossier in this application. |
| 2 | Import Directors and Promoters | The system shall import Director and Promoter particulars linked to each FE, for use in accused / colluder related checks and lists. |
| 3 | Import Investment Schemes | The system shall import Investment Schemes configured against each FE. Claim notification, intake, investment capture and verification shall use **only** these imported schemes. |
| 4 | Reference use | Imported FE, director/promoter and scheme records shall be available as selectable / linkable references across depositor, investment, asset, claim, settlement and list modules. |
| 5 | No local FE dossier | The system shall not provide screens to create or edit FIR, court case, government notification, court order, FE company bank account, current case status, seized-document corpus, market intelligence or social-media investigation artefacts. Those remain in the existing application. |
| 6 | Sync / refresh | Authorised users shall be able to refresh imported FE, director/promoter and scheme data from the existing application so claim work uses current references. |

##### Entity fields — Imported FE reference (only)

| Field | Notes |
|-------|-------|
| FE unique ID | As issued / held in the existing FE application |
| FE name / aliases | Including trade names used in schemes |
| Directors | Name and identifying particulars as supplied by the existing application |
| Promoters | Name and identifying particulars as supplied by the existing application |
| Investment schemes | Scheme master linked to FE, as configured in the existing application |
| Import / last-sync timestamp | When this application last received the record |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Claim modules can select an FE and scheme only from imported records. |
| 2 | Directors and Promoters imported for an FE are available to authorised lists and checks. |
| 3 | This application has no FE-dossier create/edit for FIR, court, notifications, orders, company banks, case status or seized corpus. |
| 4 | A refresh from the existing application updates the three imported sets without duplicate FE identities. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Import FE details | An authorised Officer or Administrator starts an FE import (or initial load) from the existing FE Management application. The system brings unique ID, name and aliases into this application as read-only references. The Officer then selects that FE on depositor, investment, asset, notification, intake and settlement screens. The Officer has no “Create FE dossier” action in this application. |
| F02-002 | Import Directors and Promoters | After FE details are imported, the Officer or Administrator imports Director and Promoter names and identifying particulars linked to that FE. An Officer later uses those names when running accused or colluder lists and related checks, without re-typing the FE people master. |
| F02-003 | Import Investment Schemes | The Officer or Administrator imports the schemes configured on each FE in the existing application. When creating a claim notification, capturing an investment, or taking in a claim, the Officer (or OOK claimant) can select only those imported schemes, not free-text scheme names. |
| F02-004 | Refresh imported FE reference data | An authorised Officer or Administrator triggers a refresh from the existing FE application. The system updates FE details, Directors, Promoters and schemes already imported, without creating duplicate FE identities. Claim screens then show the refreshed name, scheme list and people references. |


---



### 03. Asset Attachment & Recovered Funds

**Purpose:** Maintain court-attached assets and recovered funds, and make the recovered amount available for claim settlement. This module records attachment, e-format valuation particulars, title/Khata, auction tracking and recovered totals. GIS field valuation (eValueI / eValueM) is specified in a **separate SOW**.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                         |
| --------------------- | -------------------------------------------------------------------------------- |
| Business Process Flow | Module 2 — Asset Attachment & Recovery Management; Phase 4 ad-interim attachment |
| Website review 12-08-2026 | Items 11, 5 (Section 5): structured asset data, documents, status, history, depositor/FE association |




#### Functional requirements


| #   | Area               | Requirement                                                                                                                                                              |
| --- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Asset register     | The system shall register attached assets, support transfer of title, create e-Khata tracking, and record dues obtained and paid until Khata is created, before auction. |
| 2   | Orders             | The system shall allow upload of attachment orders.                                                                                                                      |
| 3   | Valuation e-format | The system shall record valuation details in e-format based on the valuation manual.                                                                                     |
| 4   | Auction            | The system shall track the auction process in consultation with e-Governance.                                                                                            |
| 5   | Recovered funds    | The recovered amount available for settlement shall be maintained and consumed by settlement (Module 08).                                                                |
| 6   | Documents, status, history | The system shall maintain supporting documents, asset status, lifecycle history and ownership / association information. |
| 7   | Depositor / FE association | Where applicable, the system shall associate an asset with the imported FE and with a depositor profile. |




##### Entity fields — Attached asset (minimum)


| Field                       | Notes                                      |
| --------------------------- | ------------------------------------------ |
| Linked FE                   | Parent Financial Establishment             |
| Asset identification        | Description / location as recorded         |
| Attachment order            | Upload + metadata                          |
| Title transfer status       | Workflow status                            |
| e-Khata status              | Workflow status                            |
| Dues paid till Khata        | Amounts and dates                          |
| Valuation e-format          | Particulars per valuation manual           |
| Auction status / milestones | Including e-Governance consultation points |
| Recovered amount            | Amount available for settlement            |
| Supporting documents        | Uploads and metadata                       |
| Asset status / history      | Lifecycle status and change history        |
| Associated depositor        | Where applicable                           |




#### Acceptance criteria


| #   | Criterion                                                                              |
| --- | -------------------------------------------------------------------------------------- |
| 1   | Every attached asset is linked to an FE, attachment order and auction/recovery status. |
| 2   | Title, e-Khata and dues path is trackable before auction completion.                   |
| 3   | Recovered-fund totals used by settlement match amounts recorded in this module.        |
| 4   | Asset documents, status history and depositor/FE association are retrievable.          |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F03-001 | Attached asset register | An Officer selects an imported FE, opens Asset registration, and records the attached asset (identification, location). The Officer saves the record in the recovery lifecycle. Another Officer can later search the same asset by FE or identification and open its current status. |
| F03-002 | Title, e-Khata and dues tracking | On an existing asset, the Officer updates title-transfer status, records e-Khata creation progress, and enters dues obtained and paid with dates, until Khata is created. The Officer cannot mark auction complete unless this path is recorded as required. |
| F03-003 | Attachment order and valuation e-format | The Officer uploads the attachment order against the asset and enters valuation particulars in the prescribed e-format based on the valuation manual, then saves. The order file remains available on the asset record for later settlement and audit. |
| F03-004 | Auction tracking and recovered funds | The Officer records auction milestones (including e-Governance consultation points) and the recovered amount. A settlement Officer later uses that recovered total when calculating available settlement fund; the two figures must match. |
| F03-005 | Asset documents, status and history | The Officer uploads supporting documents, changes asset status, and saves. The system appends a history row (who, when, previous status, new status). An authorised user can open the asset and replay document and status history. |
| F03-006 | Depositor and FE asset association | On the asset record, the Officer links the imported FE (mandatory) and, where applicable, searches and selects a depositor profile. Later reports and claim checks can show that asset against that FE and depositor. |


---



### 04. Depositor Master & Identity Verification

**Purpose:** Build one trusted depositor profile across all FEs through OCR intake, four-parameter matching, KYC capture, address and identity tally, mismatch queries and penny-drop recording, so claim processing rests on reliable, auditable identity data.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| Business Process Flow | Module 3 — Claim & Depositor Master; Module 1 (penny-drop, ineligible/deceased/heir processes); Key Aspect 6 |
| Website review 12-08-2026 | Items 5, 10 and Section 5: structured depositor data; no unverified Aadhaar as proof; status, history, documents |




#### Functional requirements


| #   | Area                   | Requirement                                                                                                                                                                                                              |
| --- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Document intake        | The system shall support direct recording of soft data from hard copy in a specified format using searchable OCR, translation, and format conversion (for example JPEG to PDF to DOC).                                   |
| 2   | Unique profile         | The system shall create a unique profile with **four parameters of matching** for every depositor, query-friendly with keyword and address identification, maintained as **one profile across all Fraudulent Entities**. |
| 3   | Address identification | The system shall tally pin code to actual areas and verify address particulars.                                                                                                                                          |
| 4   | Identity tally         | The system shall tally addresses and name details given in Aadhaar / PAN / EPIC with Bank Pass Book and Claim Forms.                                                                                                     |
| 5   | Mismatch queries       | The system shall auto-generate mismatch queries when those sources disagree.                                                                                                                                             |
| 6   | KYC capture            | The system shall capture personal information, Aadhaar, PAN, contact details, bank accounts, nominee details and legal-heir details. Unverified Aadhaar name or Aadhaar-linked mobile shall **not** be treated as identity proof. |
| 9   | Aadhaar and PAN verification | Aadhaar shall be verified through the Authority’s existing online verification service before it is relied on. PAN verification shall be provided. |
| 10  | Status, history, documents | The system shall maintain depositor documents, verification status, tracking status and history (structured records, not PDF publishing alone). |
| 7   | Penny-drop             | The system shall record penny-drop verification and retain an audit trail (with Module 01 and Module 08).                                                                                                                |
| 8   | Special situations     | The system shall support processes for ineligible depositors, deceased depositors, legal heirs, joint deposits, third-party payments, lost receipts and cash investments (claim/depositor workflows; not part of the existing FE dossier). |




##### Entity fields — Depositor profile / KYC


| Field                    | Notes                                                             |
| ------------------------ | ----------------------------------------------------------------- |
| Personal information     | Name and demographic particulars as per claim / ID                |
| Aadhaar                  | Number **and verification status**; unverified value is not identity proof |
| PAN                      | Number and verification status as available              |
| EPIC                     | Where used in mismatch comparison                                 |
| Contact details          | Phone, email, other contacts                                      |
| Address                  | Address lines + pin-code / area tally result                      |
| Deposit bank account     | Account-holder name, number, branch, IFSC and related particulars |
| Refund bank account      | Same structure where distinct                                     |
| Nominee details          | As applicable                                                     |
| Legal heir details       | As applicable                                                     |
| Four matching parameters | As defined with the Authority for unique profile matching         |
| Linked FE(s)             | All FEs where the depositor appears                               |




##### Entity fields — Document intake package


| Item                              | Notes                        |
| --------------------------------- | ---------------------------- |
| Source JPEG / PDF                 | Immutable original retained  |
| OCR / translated / converted text | Searchable working text      |
| Format conversion path            | For example JPEG → PDF → DOC |




##### Entity fields — Penny-drop


| Field                  | Notes                               |
| ---------------------- | ----------------------------------- |
| Penny-drop reference   | As provided by the bank process     |
| Penny-drop result      | Success / fail and match indicators |
| Verification timestamp | When result recorded                |




#### Acceptance criteria


| #   | Criterion                                                                                 |
| --- | ----------------------------------------------------------------------------------------- |
| 1   | OCR / converted output is searchable while the source file remains unchanged.             |
| 2   | One depositor identity spans multiple FEs under the four-parameter match.                 |
| 3   | Pin-code / address tally and Aadhaar-PAN-EPIC vs passbook vs claim-form tally are stored. |
| 4   | Mismatch queries are auto-generated when sources disagree.                                |
| 5   | Penny-drop results are recorded with an audit trail.                                      |
| 6   | Unverified Aadhaar is not accepted as identity proof.                                     |
| 7   | Depositor documents, status and history are stored as structured records.                 |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F04-001 | OCR, translation and format conversion | An Officer (or assisting staff) uploads a hard-copy scan or photo (JPEG/PDF). The system produces searchable OCR text, optional translation, and format conversion (for example JPEG to PDF to DOC). The Officer works on the text copy. The original file stays unchanged and remains the source. |
| F04-002 | Unique depositor profile (four-parameter match) | When the Officer saves a new depositor or claim identity, the system matches on the four Authority-defined parameters. If a match exists, the Officer is shown the existing profile and continues on that record (including additional FEs). If not, the Officer confirms creation of a new unique profile used across all FEs. |
| F04-003 | KYC capture | The Officer opens the depositor profile and enters personal information, Aadhaar, PAN, contacts, deposit and refund bank accounts, nominee and legal-heir details, then saves. These fields are the ones later used in claim intake and verification. |
| F04-004 | Address and pin-code verification | The Officer enters address and pin code. The system tallies the pin code to actual areas and shows the verification result. On discrepancy the Officer records the outcome (including RPAD re-verification when that step is used) and saves. |
| F04-005 | Name and address tally across ID sources | The Officer (or the system on save) compares name and address on Aadhaar, PAN and EPIC with the bank passbook and the claim form. The Officer sees each source side by side and the tally result (match or differ) before proceeding. |
| F04-006 | Auto mismatch query generation | When tally finds disagreement (for example Aadhaar spelling versus passbook name), the system creates a mismatch query on the depositor/claim. The Officer opens the query, records resolution or sends it for claimant/staff response, and cannot treat the identity as clean until it is closed per policy. |
| F04-007 | Penny-drop verification recording | The Officer records a penny-drop request/result from the contracted bank against the refund account (success/fail, match indicators, timestamp). An auditor later opens the same depositor or payment trail and sees that penny-drop event. |
| F04-008 | Special depositor and claim situations | The Officer flags the depositor/claim as ineligible, deceased, legal heir, joint deposit, third-party payment, lost receipt or cash investment, attaches the supporting papers, and routes the case on that workflow until it is resolved per Authority policy. |
| F04-009 | Aadhaar and PAN verification | The Officer triggers Aadhaar verification through the existing online service and records PAN verification. Until Aadhaar verification succeeds, the Officer cannot treat Aadhaar name or Aadhaar-linked mobile as identity proof. Unverified capture remains visible as unverified only. |
| F04-010 | Depositor documents, status and history | The Officer uploads depositor documents, sets verification/tracking status, and saves. The system stores structured fields and a history of status changes (who, when). The Officer can reopen the profile and see documents and history without relying on a PDF published on a home page. |


---



### 05. Investment Portfolio Management

**Purpose:** Maintain every investment made by a depositor, auto-calculate interest and outstanding balances, analyse bank returns, and compare across FE / FIR / seizure data to support claim evaluation and detection of duplication or collusion indicators.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| Business Process Flow | Module 4 — Investment Portfolio Management; Key Aspect 6 (bank/cash transactions, excess payment) |




#### Functional requirements


| #   | Area                      | Requirement                                                                                                                                                                                               |
| --- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Investment capture        | The system shall capture every investment made by a depositor against an FE and scheme using the field table below.                                                                                       |
| 2   | Auto-calculation          | The system shall auto-calculate deposits, interest received, maturity dates and violations of those dates, and promised interest versus actual interest paid.                                             |
| 3   | Outstanding balance       | The system shall determine outstanding balance by treating interest paid as principal repaid where the approved business rule requires it.                                                                |
| 4   | Role categorisation       | The system shall support identification of depositor types, colluders or the accused based on authorised data analytics.                                                                                  |
| 5   | Bank returns              | The system shall analyse bank returns after scan-based transfer and cross-verify them with claims data.                                                                                                   |
| 6   | Bank-officer verification | The system shall record bank-officer email addresses to enable auto-verification requests unless the data is submitted directly by bank officers.                                                         |
| 7   | Cross-database comparison | The system shall compare across imported FEs and local investment / claim / attached-asset data using single and multiple linked parameters to identify duplication and collusion. Comparison with FIR or seized-FE databases, where required, shall be a **lookup to the existing FE application**, not a local copy of those databases. |
| 8   | Excess payment            | The system shall detail and categorise bank and cash transactions and support excess-payment analysis with audit trail.                                                                                   |
| 9   | Output                    | Complete investment history shall be available to claim verification and settlement modules.                                                                                                              |




##### Entity fields — Investment record


| Field                   | Notes                                                         |
| ----------------------- | ------------------------------------------------------------- |
| Fraudulent Entity       | Linked FE                                                     |
| Investment Scheme       | Linked scheme                                                 |
| Customer ID             | As per FE records                                             |
| Bond / MOU Number       | Where applicable                                              |
| Deposit Receipt         | Receipt reference                                             |
| Investment Date         | Date of deposit / investment                                  |
| Maturity Date           | Contractual maturity                                          |
| Deposit Amount          | Principal deposited                                           |
| Interest Promised       | Contractual promised interest                                 |
| Amount Already Received | Returns already paid to depositor                             |
| Outstanding Balance     | System-calculated / maintained balance                        |
| Interest-paid treatment | Flag / rule for interest-as-principal-repaid where applicable |
| Maturity violation flag | Where maturity obligations were breached                      |




#### Acceptance criteria


| #   | Criterion                                                                                |
| --- | ---------------------------------------------------------------------------------------- |
| 1   | Complete investment history is available per depositor, FE and scheme.                   |
| 2   | Outstanding-balance calculations are reproducible and audited.                           |
| 3   | Cross-FE duplication / collusion queries return explainable results to authorised users. |
| 4   | Excess-payment analysis is available with an audit trail.                                |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F05-001 | Investment record capture | An Officer opens a depositor, selects imported FE and scheme, and enters customer ID, bond/MOU, deposit receipt, dates, deposit amount, promised interest and amount already received, then saves. The same Officer can reopen the record and see the full investment history for that depositor, FE and scheme. |
| F05-002 | Interest and outstanding auto-calculation | After the Officer saves amounts and dates, the system calculates interest received, promised versus paid interest, and outstanding balance (treating interest paid as principal repaid where the Authority’s rule applies). The Officer views the calculated figures, can re-run after a correction, and the calculation is stored for audit. |
| F05-003 | Maturity and violation analytics | The Officer opens portfolio analytics for a depositor or FE. The system flags investments whose maturity date is violated. The Officer reviews the flag list and uses it in verification or categorisation. |
| F05-004 | Depositor / colluder / accused categorisation | An authorised Officer runs the categorisation action on portfolio data (using imported Director/Promoter names where relevant). The system proposes depositor, colluder or accused under approved rules. The Officer accepts or overrides with remarks; the category is stored on the profile for lists and verification. |
| F05-005 | Bank returns analysis and claim cross-check | The Officer uploads or opens scanned bank-return data after transfer, runs analysis, and compares it with claim and investment records. The Officer sees matches and exceptions and records the cross-check outcome on the claim or investment. |
| F05-006 | Bank-officer verification requests | The Officer records the bank officer’s email on the investment or return. Unless the bank has already submitted the data, the Officer triggers a verification request to that email and later records the reply or timeout against the same record. |
| F05-007 | Cross-FE comparison (FIR / seized-FE via existing app) | The Officer selects one or more imported FEs and runs a duplication or collusion comparison across local investments, claims and attached assets. Where FIR or seized-FE data is needed, the Officer initiates a lookup to the existing FE application and reviews the returned indicators without storing a local FE dossier. |
| F05-008 | Excess payment analysis | The Officer opens bank and cash transactions for a depositor or FE, runs excess-payment analysis, and reviews flagged excesses. The Officer records the outcome; the system keeps an audit trail of the analysis and the Officer’s decision. |


---



### 06. Claim Notification & Intake

**Purpose:** Invite eligible investors to submit claims, open and close claim windows, and capture complete claim packs — staff-mediated for in-Karnataka claimants and constrained online for out-of-Karnataka claimants — with mandatory validation before acceptance.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Business Process Flow | 3A Claim Notification; Module 3B Online Claim Submission (including note that a limited online access system exists); Phase 4 online constraint |




#### Functional requirements


| #   | Area                    | Requirement                                                                                                                                                                                                                                              |
| --- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Notification            | The system shall allow creation of a claim notification containing eligible FE and eligible schemes **selected from imported FE / scheme records**, plus claim submission period, eligibility criteria, required documents and instructions. |
| 2   | Publication             | The system shall publish the notification through the official application / portal used for this programme so that the claim window becomes active.                                                                                                     |
| 3   | Window control          | Claim submission shall be accepted only within the published period and only for the eligible FE / schemes.                                                                                                                                              |
| 4   | In-Karnataka intake     | For in-Karnataka claimants, intake shall be **staff-mediated / assisted digitisation of original documents**. The Officer shall **Submit** only when the full mandatory document pack (identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable) and mandatory fields are present. Unrestricted public online filing is not acceptable under BSA, 2023. |
| 5   | Out-of-Karnataka intake | For out-of-Karnataka claimants, a **constrained online** submission path shall be provided. **Submit** shall require the **same** mandatory document pack and fields as in-Karnataka staff-mediated intake. If a limited online access system already exists, the new platform shall still achieve those validated-pack outcomes. |
| 6   | Claimant confirmations  | The investor (or assisting officer) shall select FE, investment scheme and investment record, and confirm personal details, investment details and refund bank account.                                                                                  |
| 7   | Uploads                 | The pack shall include identity proof, investment proof, bank documents, nominee / legal-heir documents (if applicable), affidavit and statement of investment.                                                                                          |
| 8   | Mandatory validation    | At Submit (Officer or OOK claimant), the system shall block the claim if any mandatory field or mandatory document is missing, and shall list the gaps. Incomplete packs shall not be stored as submitted claims. Extra documents requested during verification (Module 07) come after this first Submit. |




##### Entity fields — Claim notification


| Field                   | Notes                             |
| ----------------------- | --------------------------------- |
| Eligible FE             | Imported FE(s) covered by the notification |
| Eligible Schemes        | Imported schemes covered                   |
| Claim Submission Period | Start and end of claim window     |
| Eligibility Criteria    | Published eligibility rules       |
| Required Documents      | Document checklist                |
| Instructions            | Claimant / staff instructions     |
| Publication status      | Draft / Published / Closed        |




##### Entity fields — Claim submission pack


| Field / upload                 | Notes                                             |
| ------------------------------ | ------------------------------------------------- |
| Selected FE                    | Mandatory                                         |
| Investment Scheme              | Mandatory                                         |
| Investment Record              | Linked portfolio record where available           |
| Personal Details               | Confirmed / captured                              |
| Investment Details             | Confirmed / captured                              |
| Refund Bank Account            | Confirmed / captured                              |
| Identity Proof                 | Upload                                            |
| Investment Proof               | Upload                                            |
| Bank Documents                 | Upload                                            |
| Nominee / Legal Heir Documents | Upload if applicable                              |
| Affidavit                      | Upload                                            |
| Statement of Investment        | Upload                                            |
| Intake channel                 | Staff-mediated (in-KA) / Constrained online (OOK) |
| Mandatory validation result    | Block submit if incomplete                        |




#### Acceptance criteria


| #   | Criterion                                                                                              |
| --- | ------------------------------------------------------------------------------------------------------ |
| 1   | Claim windows open and close according to published notification periods and eligibility rules.        |
| 2   | In-Karnataka staff-mediated Submit is refused unless the full mandatory document pack and fields are present. |
| 3   | OOK constrained Submit uses the same mandatory document pack and the same block-if-incomplete rule. |
| 4   | A claim cannot be marked submitted if mandatory fields or documents are missing.                       |
| 5   | Submitted claims are linked to FE, scheme, depositor and investment records where those records exist. |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F06-001 | Claim notification and window | An authorised Officer or Administrator creates a notification, selects imported eligible FE and schemes, enters submission period, eligibility, required documents and instructions, and publishes it. The claim window becomes Active for that period. The same user can close the window; intake is then refused. |
| F06-002 | Staff-mediated claim intake (in-Karnataka) | An in-Karnataka claimant presents original documents at the counter. The Officer selects imported FE, scheme and investment record, confirms personal, investment and refund-bank details, and uploads the pack from the originals. **At Submit, the Officer must have all mandatory documents:** identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable — plus all mandatory fields. If any of these is missing, the Officer cannot submit; the system blocks submission and lists the gaps. The claimant does not self-file online. |
| F06-003 | Constrained online claim submission (OOK) | An out-of-Karnataka claimant logs into the constrained path during an open window, selects imported FE, scheme and investment, confirms personal, investment and refund-bank details, and uploads the **same mandatory document pack** as F06-002 (identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers if applicable). **Submit is allowed only when that full pack and the mandatory fields are present.** The system applies the same block-and-list-gaps behaviour as staff-mediated intake. |
| F06-004 | Claim pack validation and document uploads | Shared Submit rule for **both** F06-002 (Officer) and F06-003 (OOK claimant): the claim is accepted as submitted only when identity proof, investment proof, bank documents, affidavit, statement of investment, and nominee/heir papers (if applicable) are present, together with mandatory fields (FE, scheme, personal, investment, refund bank). If any mandatory item is missing, the system blocks submission and lists the gaps. Only a complete pack is stored as a submitted claim. Additional documents requested later (F07-002) are after this first Submit, not a substitute for it. |
| F06-005 | Existing limited online access outcomes | If the Authority’s limited online access system already captures an OOK pack, the Officer retrieves or receives that outcome into this application so the claim still has linked FE, scheme, investment, validated fields and uploads. The Officer does not send the claimant to a new mass public portal. |


---



### 07. Claim Verification, Evaluation & Approval

**Purpose:** Verify submitted claims against identity, investment, seized data and eligibility; request additional documents where needed; and record the Competent Authority’s decision with remarks.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                   |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Business Process Flow | 3C Claim Verification & Evaluation; Claim Approval; Key Aspect 2 (agentic, not generative) |




#### Functional requirements


| #   | Area                 | Requirement                                                                                                                                                                                          |
| --- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Officer verification | An authorised officer shall verify identity, investment details, scheme, customer ID, deposit records, uploaded documents, bank details, previous returns received, existing claims and eligibility. |
| 2   | Additional documents | If required, the officer shall request additional documents through the application. The claimant (or assisting staff for in-KA) shall upload them. The officer shall continue evaluation.           |
| 3   | Agentic assists      | Rule-based / agentic tools may assist extraction and checks. Generative AI is prohibited. No assist may finalise a verification decision without human confirmation and audit.                       |
| 4   | Verification output  | A verified claim (or a documented exception) shall be ready for Competent Authority review.                                                                                                          |
| 5   | Approval             | The Competent Authority shall review the verification report. Decision may be Approved, Partially Approved, Rejected, or Pending Clarification. Remarks shall be recorded.                           |
| 6   | Decision output      | The claim decision shall be finalised and available to settlement (except where pending clarification).                                                                                              |




##### Entity fields — Verification checklist


| Check item                     | Notes                                 |
| ------------------------------ | ------------------------------------- |
| Identity                       | Against KYC / Aadhaar / PAN           |
| Investment Details             | Against portfolio / seized data       |
| Scheme                         | Eligibility and scheme match          |
| Customer ID                    | Against FE records                    |
| Deposit Records                | Against receipts / seized database    |
| Uploaded Documents             | Completeness and integrity            |
| Bank Details                   | Against depositor-master verification |
| Previous Returns Received      | Against portfolio                     |
| Existing Claims                | Duplicate / overlap check             |
| Eligibility                    | Against notification rules            |
| Additional documents requested | Optional loop                         |




##### Entity fields — Approval


| Field                    | Notes                                                            |
| ------------------------ | ---------------------------------------------------------------- |
| CA decision              | Approved / Partially Approved / Rejected / Pending Clarification |
| CA remarks               | Recorded with the decision                                       |
| Verification report link | Report reviewed by the Competent Authority                       |
| Workflow stage audit     | Role/Post, action, status, remarks, date and time, supporting documents — each stage |




#### Acceptance criteria


| #   | Criterion                                                                                          |
| --- | -------------------------------------------------------------------------------------------------- |
| 1   | Every submitted claim can be verified against the checklist items and the result stored.           |
| 2   | Additional-document request and subsequent upload re-enter evaluation without losing prior checks. |
| 3   | Agentic assists never auto-finalise verification or approval.                                      |
| 4   | CA decisions and remarks are complete, attributable and audited.                                   |
| 5   | No generative AI components are present in verification or approval.                               |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F07-001 | Officer verification checklist | An Officer opens a submitted claim and works through identity, investment details, scheme, customer ID, deposit records, uploads, bank details, previous returns, existing claims and eligibility, recording pass/fail or remarks on each item, then saves the checklist. |
| F07-002 | Additional document request loop | If a document is missing or unclear, the Officer raises an additional-document request on the claim. The claimant (OOK) or assisting staff (in-KA) uploads the papers. The Officer reopens the claim, continues the checklist from where it stopped, and saves; prior ticks are not lost. |
| F07-003 | Agentic verification assists (non-generative) | While the Officer is on the checklist, rule-based or agentic assists may highlight mismatches or extracted values. The Officer must confirm or reject each suggestion. The Officer cannot skip human confirmation. No generative-AI compose action is available. Assists and Officer decisions are audited. |
| F07-004 | Verification report for Competent Authority | When the Officer completes evaluation, the Officer generates the verification report from the checklist and remarks and marks the claim ready for CA review. The Competent Authority opens that report (not a blank claim) as the basis for decision. |
| F07-005 | Claim approval decisions | The Competent Authority opens the verification report, selects Approved, Partially Approved, Rejected or Pending Clarification, enters remarks, and saves. The decision, Person, Post, date/time and remarks are stored on the claim and visible to settlement. Pending Clarification returns the claim for further Officer work. |


---



### 08. Settlement, Payment & Closure

**Purpose:** Calculate settlement from recovered funds and approved liability, generate payment batches, record NEFT/RTGS outcomes, update balances and close settled claims.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                                                            |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Business Process Flow | Module 4A Recovery & Settlement Management; Module 4B Payment & Claim Closure; Module 1 (penny-drop / excess-payment / audit trail) |




#### Functional requirements


| #   | Area                   | Requirement                                                                                                         |
| --- | ---------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1   | Settlement inputs      | The system shall record Total Recovered Amount, Total Approved Liability and Available Settlement Fund.             |
| 2   | Settlement calculation | The system shall calculate Eligible Amount, Previous Returns Received, Previous Settlements and Net Payable Amount. |
| 3   | Payment batches        | The system shall generate payment batches.                                                                          |
| 4   | Transfer               | Payment shall be transferable through NEFT and RTGS.                                                                |
| 5   | Payment recording      | The system shall record Payment Reference, Transaction Number and Payment Status.                                   |
| 6   | Updates                | The system shall update Claim Status, Investment Balance and Payment History.                                       |
| 7   | Closure                | When payment succeeds as policy requires, the claim shall be marked successfully settled and closed.                |
| 8   | Payment audit          | Payment events shall participate in the forensic audit trail (Module 01).                                           |




##### Entity fields — Settlement and payment


| Field                                  | Notes                                               |
| -------------------------------------- | --------------------------------------------------- |
| Total Recovered Amount                 | From Module 03                                      |
| Total Approved Liability               | Aggregate approved claims                           |
| Available Settlement Fund              | Fund available for distribution                     |
| Eligible Amount                        | Calculated                                          |
| Previous Returns Received              | Calculated / recorded                               |
| Previous Settlements                   | Calculated / recorded                               |
| Net Payable Amount                     | Calculated                                          |
| Payment batch ID                       | System batch reference                              |
| Payment mode                           | NEFT / RTGS                                         |
| Payment Reference / Transaction Number | Bank references                                     |
| Payment Status                         | Pending / Success / Failed / Reversed as applicable |
| Claim Status after payment             | Updated to closed when settled                      |
| Investment Balance after payment       | Updated                                             |
| Payment History                        | Append-only history                                 |




#### Acceptance criteria


| #   | Criterion                                                                                                |
| --- | -------------------------------------------------------------------------------------------------------- |
| 1   | Settlement calculations reconcile to recovered funds and prior returns / settlements.                    |
| 2   | Payment batches can be generated and tracked for NEFT and RTGS.                                          |
| 3   | Payment reference, transaction number and status are stored for every payment.                           |
| 4   | Successful settlement updates claim status, investment balance and payment history and closes the claim. |
| 5   | Failed or reversed payments do not close the claim.                                                      |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F08-001 | Settlement fund and net payable calculation | An Officer records total recovered amount (from assets), total approved liability and available settlement fund. The system calculates eligible amount, previous returns, previous settlements and net payable. The Officer reviews the figures, saves, and uses net payable for payment. |
| F08-002 | Payment batch generation (NEFT / RTGS) | The Officer selects approved claims with a net payable, chooses NEFT or RTGS, and generates a payment batch. The system creates a batch ID and lists the included claims and amounts for the Officer to confirm before transfer. |
| F08-003 | Payment reference and status recording | After transfer, the Officer (or returning bank status) records payment reference, transaction number and status (pending, success, failed, reversed) against each claim in the batch. The Officer can reopen a claim and see the latest payment status. |
| F08-004 | Claim closure and balance update | When payment status is success as policy requires, the Officer (or the system on that status) updates claim status to closed, updates investment balance and appends payment history. A failed or reversed payment leaves the claim open; the Officer cannot close it as settled. |
| F08-005 | Payment forensic audit | An authorised auditor or Administrator opens a claim or batch and retrieves who generated the batch, who recorded bank references, each status change, and closure — with Person, Post, timestamp and channel. |


---



### 09. Operational Reports, Lists & Special Court Outputs

**Purpose:** Produce the operational and court-facing outputs of the claim programme — equitable distribution and Special Court reports from approved input formats, parameterised lists, and decision dashboards — and provide business-level hooks to the legacy web application and in-use document software.

**Type:** Business  

#### Source coverage


| Source document       | Coverage                                                                                                                                      |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Business Process Flow | Module 1 (equitable distribution statement, Special Court report, dashboards); Key Aspects 1, 4, 7 |
| Website review 12-08-2026 | Items 13, 8 and Sections 6G–6H: automated reports from structured data; not PDF-only; Role/Post mapping and activity reports |




#### Functional requirements


| #   | Area                   | Requirement                                                                                                                                                                   |
| --- | ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Equitable distribution | When relevant data is fed into an approved input format, the system shall prepare the equitable distribution statement required for filing before the Special Court.          |
| 2   | Special Court report   | The system shall prepare the report required for filing before the Special Court from the same class of approved inputs.                                                      |
| 3   | Dashboards             | Authorised users shall extract raw data, analytical information and decision reports through queries and dashboards.                                                          |
| 4   | Lists                  | The system shall generate parameterised lists including claimants (on different parameters), accused, colluders, address lists and vendor lists as required for operations.   |
| 5   | Legacy / web app       | The claim programme shall integrate with the legacy system and existing web application at a business-interface level (no duplicate island of claim data).                    |
| 6   | Document software      | The system shall interact with in-use document software and online subscriptions (for example Idea, Adobe Suite) as interfaces allow, for working copies and published packs. |
| 7   | Structured operational reports | From captured structured data the system shall produce depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, user/activity and Role/Post mapping reports, in addition to FE-wise views on imported FE references. PDF publishing alone is not sufficient. |




##### Entity fields — Special Court / distribution inputs (conceptual)


| Item                             | Notes                                                         |
| -------------------------------- | ------------------------------------------------------------- |
| Approved input format            | Authority-specified fields fed for ED / court report          |
| Equitable distribution statement | Generated output                                              |
| Special Court report             | Generated output                                              |
| List parameters                  | Filters such as FE, scheme, status, depositor type, geography |




#### Acceptance criteria


| #   | Criterion                                                                                                     |
| --- | ------------------------------------------------------------------------------------------------------------- |
| 1   | Equitable distribution statement and Special Court report can be produced from approved inputs.               |
| 2   | Parameterised claimant, accused, colluder, address and vendor lists can be generated by authorised roles.     |
| 3   | Dashboard / query outputs are restricted by Module 01 visibility rules.                                       |
| 4   | Legacy / web-application integration expectations are documented as interfaces, not as a second claim ledger. |




#### Key capabilities (feature outline)


| Feature ID | Capability | Description |
| ---------- | ---------- | ----------- |
| F09-001 | Equitable distribution statement | An authorised Officer enters or loads the approved input format (recovered funds, approved claims and related fields) and generates the equitable distribution statement. The Officer downloads or files the output for Special Court use. |
| F09-002 | Special Court filing report | Using the same class of approved inputs, the Officer generates the Special Court filing report, reviews it on screen, and produces the filing copy. The Officer does not re-key the settlement figures by hand into an unrelated template. |
| F09-003 | Parameterised operational lists | The Officer selects parameters (FE, scheme, status, depositor type, geography or similar) and generates claimant, accused, colluder, address or vendor lists. The Officer views or exports only lists allowed for their Post. |
| F09-004 | Claim decision dashboards | The Officer or Competent Authority opens dashboards, filters by imported FE, scheme, window or status, and views claim and settlement counts and exceptions. Menu access follows Module 01; another Post does not see restricted slices. |
| F09-005 | Legacy web app and document-software hooks | An authorised Officer or Administrator sends or retrieves agreed claim outcomes to the legacy / existing web application, and opens working copies in in-use document software (for example Idea or Adobe Suite) where that interface exists, without creating a second unofficial claim ledger. |
| F09-006 | Structured operational reports | The Officer chooses a report type (depositor-wise, asset-wise, claim-wise, verification, status-wise, historical, user/activity), sets filters, and generates it from structured records. Publishing a PDF on a home page is not the way these reports are produced. |
| F09-007 | Role / Post mapping reports | An Administrator or auditor generates Role-to-Post and Post-to-Person mapping reports (current and history: who was mapped, effective dates, who changed the mapping). The report is used for access audit, not for granting access. |


---



## 7. End-to-End Workflows



### 7.1 Statutory prelude (outside the application, except references)

```text
Fraud occurs (multiple schemes / branches / FEs)
        → FE fails to repay; complaints to Police / Government
        → Criminal investigation (FIR, seizure, charge sheet)     [OUT OF SCOPE — remains outside this app / in existing FE application]
        → Government invokes KPID Act; appoints Competent Authority
        → Ad-interim attachment of FE assets
        → Claim-settlement system in use (imports FE, directors/promoters, schemes)
```

**Another route (references only):** Complaint; suo-motu action on advertisement; inputs from RBI / SLCC / Ombudsman; direct information to DC / AC / Fraud cell / SPLOCA / Regional Commissioner, Bengaluru (Secretary Economic Offences).

### 7.2 Claim settlement (in application)

```text
Import FE details, Directors and Promoters, Investment Schemes (from existing FE application)
        → Record attached assets and recovered funds
        → Build depositor master (OCR, 4-parameter match, KYC, tally, penny-drop)
        → Capture investment portfolio (interest, outstanding, bank returns)
        → Publish claim notification → claim window active
        → Intake: staff-mediated (in-KA) or constrained online (OOK)
        → Officer verification (+ additional documents if required)
        → Competent Authority decision (Approve / Partial / Reject / Pending)
        → Settlement calculation against recovered funds
        → NEFT / RTGS payment batches → status, history, closure
        → Equitable distribution statement / Special Court report as required
```



### 7.3 Additional-document loop

Officer requests documents → claimant or assisting staff uploads → officer continues evaluation → verification report updated → CA review when ready.

### 7.4 Mismatch and special situations

Auto mismatch queries (Aadhaar / PAN / EPIC vs passbook vs claim form) and special situations (ineligible, deceased, heirs, joint, third-party, lost receipts, cash investments) remain linked to the depositor and claim until resolved per Authority policy.

---



## 8. Access Control / RBAC

Access follows the **Person–Post–Role** model required by the 12 August 2026 website review (not role-only logins).


| Element | Rule |
|---------|------|
| **Person** | Unique official identity; no shared credentials |
| **Post** | Catalogue of posts (for example Officer, Competent Authority desk, Administrator) |
| **Role-to-Post** | Permissions attach to the Post |
| **Post-to-Person** | A Person occupies a Post for an effective period; full mapping history is kept |
| **Administrator** | Person/Post/Role administration, credentials, 2FA enrolment support, notification publication support |
| **Officer (via Post)** | Imported FE / director / scheme references; depositor / investment maintenance; staff-mediated intake; verification; additional-document requests; operational lists as authorised |
| **Competent Authority (via Post)** | Review verification reports; record Approved / Partially Approved / Rejected / Pending Clarification; oversee settlement and payment release |
| **OOK claimant** | Constrained submission of own pack during an open window only — not a department Person/Post |
| **In-KA claimant** | No unrestricted self-service filing account; originals presented for staff-mediated intake |
| **Bank officer** | Not an application Person by default; participates via email verification / direct data submission |

Staff login requires **2FA**. OTP is completed **before** activation. Department users use **official / administered identity**. Every privileged action is attributable (Module 01).

---



## 9. Channels


| Channel                                            | Who                                           | Use                                                                                       |
| -------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Staff web application**                          | Officers, Competent Authority, Administrators | All official claim work                                                                   |
| **Constrained online path**                        | Out-of-Karnataka claimants                    | Claim submission during published windows only                                            |
| **Staff-mediated counter / assisted digitisation** | In-Karnataka claimants via officers           | Original-document intake (BSA, 2023)                                                      |
| **Existing limited online access system**          | As already in use                             | Business outcomes must be covered; may be integrated rather than rebuilt as a mass portal |
| **Email**                                          | Bank officers                                 | Auto-verification requests unless data is submitted directly                              |
| **Mobile / Android official apps**                 | —                                             | **Not in this SOW** (not specified in the Claim Management Business Process Flow)         |


---



## 10. Integrations

Business-level integrations only (no API contracts).


| Integration                                    | Purpose                                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Existing FE Management application** | **Authoritative FE master.** Import FE details, Directors and Promoters, and Investment Schemes for use by all claim modules |
| **Legacy system and existing web application** | Avoid a duplicate claim ledger; authorised linked access                                                         |
| **Existing limited online access system**      | Cover OOK / limited-access claim submission outcomes                                                             |
| **In-use document software**                   | Idea, Adobe Suite and similar subscriptions — working copies, conversion and published packs as interfaces allow |
| **Bank penny-drop process**                    | Record verification results and payment audit                                                                    |
| **Bank-officer email**                         | Trigger verification requests                                                                                    |
| **Payment rails**                              | NEFT and RTGS batching and status recording (through the Authority’s approved banking arrangements)              |
| **Aadhaar online verification**                | Existing service — required before Aadhaar is relied on as identity proof                                        |
| **PAN verification**                           | To be provided                                                                                                   |


Aadhaar shall be **verified** through the Authority’s existing online verification service before it is relied on as identity proof (website review item 5; unverified Aadhaar capture is not accepted). PAN verification shall be provided. Capture of Aadhaar and PAN without verification is not sufficient.

---



## 11. Audit, Compliance & Security

1. Forensic audit trail for verification, penny-drop, excess-payment analysis, approval, payment and closure.
2. Original scans / JPEGs / PDFs retained unaltered; OCR and conversions are working copies.
3. BSA, 2023 original-document requirement for in-Karnataka claim verification.
4. Need-to-know visibility of claim packs and depositor KYC.
5. No generative AI in claimant communications or decisioning.
6. Investigation process and the FE dossier remain outside this application (existing FE application / police process).
7. Payment and settlement figures used in court outputs must reconcile to recovered funds and approved claims.
8. Person–Post–Role mapping history and login / 2FA / credential events are auditable.
9. Unverified Aadhaar is not treated as identity proof.

---



## 12. Non-Functional Requirements


| Area                  | Expectation                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------ |
| **Integrity**         | Source files immutable; working copies separately identifiable                             |
| **Auditability**      | Privileged actions attributable and retrievable                                            |
| **Availability**      | Suitable for official claim-window operations (exact SLA to be agreed)                     |
| **Usability**         | Searchable / type-ahead dropdowns, practical filters, clearer navigation and task-oriented staff screens (website review item 16). Staff-mediated intake usable with original physical documents; OOK path limited and simple |
| **Official domain**   | Approved Government of Karnataka domain / hosting identity. `.org` (including sploca.org) shall not be the primary official domain for this application |
| **UAT evidence**      | Module completion is accepted only after employee-role demonstration with evidence, not on unsubstantiated “module working” claims |
| **Search**            | Keyword, unique ID, address / pin-code and depositor-parameter queries                     |
| **Interoperability**  | Existing FE Management application (FE / director / scheme import); legacy web application and document-software hooks |
| **Language / script** | Translation of claim documents as required for analysis                                    |
| **AI**                | Agentic / rule-based only; human verify; no generative models                              |


This SOW does not prescribe hosting stack, encryption algorithms, or infrastructure sizing.

---



## 13. Data Migration

**In scope** as a structured load of records the Authority releases for the claim programme, including as available:

- FE details, Directors and Promoters, and Investment Schemes **via integration / initial load from the existing FE Management application** (not a separate FE-dossier migration)  
- Depositor / claimant identity packs and scanned corpora  
- Investment / deposit records and bank-return scans  
- Attached-asset and recovered-fund figures required for settlement  
- Open or historical claim packs the Authority designates

**Out of scope unless separately ordered:** back-file scanning bureau operations; reconstruction of missing physical receipts. Migration of legal-matter and GIS-valuation records belongs to those separate SOWs.

Non-production environments should use anonymised or synthetic claimant data where live equitable-distribution datasets are sensitive (recommended control; confirm with the Authority).

---



## 14. Phased Delivery

Indicative phasing aligned to the Business Process Flow (not a commercial bid schedule):


| Phase                         | Focus                                                                                   | Modules (primary) |
| ----------------------------- | --------------------------------------------------------------------------------------- | ----------------- |
| **P1 — Foundations**          | Person–Post–Role, 2FA, official identity; import FE details / directors / promoters / schemes; depositor master; investment portfolio | 01, 02, 04, 05    |
| **P2 — Recovery feed**        | Attached assets, valuation e-format, auction tracking, recovered funds                  | 03                |
| **P3 — Claim window**         | Notification, staff-mediated intake, constrained OOK / existing limited-access outcomes | 06                |
| **P4 — Decide and pay**       | Verification, approval, settlement, NEFT/RTGS, closure                                  | 07, 08            |
| **P5 — Court and operations** | Equitable distribution, Special Court report, structured operational reports, dashboards | 09                |


P1 is a prerequisite for P3–P5. P2 may run in parallel with P1 once imported FE references are available. Exact go-live grouping is a commercial / Authority decision after estimation.

---



## 15. Deliverables


| Deliverable                                                                            | Description                                                                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Staff web application for claim settlement                                             | Modules 01–09 as specified                                                                                                             |
| Constrained OOK submission path and/or integration with existing limited online access | Module 06 outcomes                                                                                                                     |
| Role and credential administration                                                     | Module 01 — Person, Post, Role mapping, 2FA, official identity                                                     |
| Equitable distribution and Special Court output formats                                | Module 09                                                                                                                              |
| Operational reports and dashboards from structured data                                | Module 09                                                                                                                              |
| Integration with existing FE Management application (FE / director / scheme import)    | Module 02 / §10                                                                                                                        |
| Integration with legacy / existing web application (agreed interfaces)                 | Module 09 / §10                                                                                                                        |
| Documentation                                                                          | Functional overview, role guide, audit/retrieval guide, interface notes                                                                |
| Training content hooks                                                                 | In-application guidance for officers on intake, verification and payment — classroom programmes out of scope unless separately ordered |


---



## 16. Acceptance Criteria (programme level)

1. FE details, Directors and Promoters, and Investment Schemes are available in this application **by import** from the existing FE Management application; claim modules can select only imported FE and scheme records.
2. A single depositor profile exists across FEs using four matching parameters; mismatch queries fire when Aadhaar/PAN/EPIC, passbook and claim form disagree.
3. Complete investment history supports verification and settlement calculations.
4. Claim windows open and close per published notifications.
5. In-Karnataka intake is staff-mediated; OOK uses a constrained path; mandatory packs cannot be submitted incomplete.
6. Officers complete the verification checklist and additional-document loop; CA records one of the four decisions with remarks.
7. Settlement net payable reconciles to recovered funds, approved liability, previous returns and previous settlements.
8. NEFT/RTGS batches record reference, transaction number and status; successful payment closes the claim and updates balances.
9. Equitable distribution statement and Special Court report can be produced from approved inputs.
10. Generative AI is absent; agentic assists never auto-finalise decisions.
11. Forensic audit is retrievable for verification, penny-drop, excess-payment, approval and payment.
12. This application does not implement FE Management screens (FIR, court dossier, seized corpus, company banks, case status).
13. Staff access uses Person–Post–Role mapping with history; 2FA is required; OTP completes before activation; personal email is not the primary department registration path.
14. Unverified Aadhaar is not accepted as identity proof.
15. Structured depositor, asset and claim data support automated reports (not PDF publishing alone).
16. Searchable dropdowns / filters are available on staff screens; primary official domain is not `.org`.

---



## 17. Expected Benefits

- Digitised, auditable claim settlement after KPID invocation  
- One depositor identity across multiple FEs, schemes, branches and investments  
- Reduced duplicate / collusive claims through portfolio comparison and imported FE / scheme / director references  
- Transparent settlement against recovered funds  
- Court-ready equitable distribution and Special Court outputs  
- Clear channel split: original documents for in-Karnataka; limited online for out-of-Karnataka  
- Unique Person–Post–Role access with 2FA and official identity  
- Structured depositor, asset and claim data (not a PDF publishing portal)  
- Approved government domain / hosting identity; usable staff screens

---



## 18. Assumptions & Dependencies



### 18.1 Assumptions (defaults taken for this draft)

1. **Project code** is CLAIM; display name is **Claim Management System (KPID / SPLOCA)**.
2. **SOW purpose** is both RFP discussion and internal estimation.
3. **Document management and workflow are embedded** in business modules.
4. **Access model** is **Person–Post–Role** with mapping history, official staff identity, OTP before activation, 2FA, and no credential sharing, as required by the 12 August 2026 website review.
5. This SOW is a **separate Claim Management application**. FE Management (BPF Module 1) is already implemented in the existing application and is not rebuilt. Only FE details, Directors and Promoters, and Investment Schemes are imported.
6. **Aadhaar online verification** (existing) is used; PAN verification is provided. Unverified Aadhaar capture is not treated as proof.
7. **Existing limited online access system** will be integrated or its outcomes re-implemented in the constrained OOK path — not rebuilt as a mass public portal.
8. **Four matching parameters** for unique depositor profile will be confirmed by the Authority during implementation (the source requires four parameters but does not name them).
9. **Interest-paid-as-principal-repaid** is applied where the Authority’s approved business rule requires it.
10. **Android / mobile official apps** are out of this SOW unless later added.
11. Hosting is on the Authority’s designated environment; this SOW does not size infrastructure.
12. Agentic bots are limited to assistive extraction, matching, mismatch flags and calculations.
13. Imported FE / director / scheme records are **read-as-reference** in this application; the existing application remains the system of record for the FE dossier.
14. Primary official hosting identity will be an approved government domain, not `.org`.



### 18.2 Dependencies

1. Government notification / KPID invocation and appointment of Competent Authority for each FE brought onto the system.
2. Working integration (and access) to the existing FE Management application for FE details, Directors and Promoters, and Investment Schemes.
3. Supply of bank returns, attachment orders and recovered-fund figures by the Authority for modules built in this application.
4. Approved input format for equitable distribution and Special Court reports.
5. Banking arrangements for penny-drop, NEFT and RTGS.
6. e-Governance consultation path for auction tracking.
7. Access to legacy system and existing web application interface points.
8. Clarification of the four depositor-matching parameters.
9. Policy for ineligible / deceased / heir / joint / third-party / lost-receipt / cash-investment cases.

---



## 19. Vendor Response Expectations

Vendors (or internal estimation teams) shall:

1. Confirm understanding of the **in-Karnataka vs out-of-Karnataka** intake split and the existing limited online access system.
2. Map their solution to **modules 01–09 and feature IDs F{NN}-{SEQ}** without renumbering.
3. Describe agentic / rule-based assists and explicitly **exclude generative AI**.
4. Describe forensic audit coverage for verification, penny-drop, excess-payment, approval and payment.
5. Describe the **FE import integration** (FE details, Directors and Promoters, Investment Schemes) and legacy / web-application / document-software interface approach at business level.
6. Identify assumptions that differ from §18.
7. Not treat FE Management (BPF Module 1) or police investigation as part of this Claim Management SOW. Legal Management and GIS field valuation (eValueI / eValueM) are in the same programme and will be covered in **separate SOWs** — do not duplicate that scope in the response to this document.
8. Not include effort hours in a rewritten SOW; hours belong in a later estimation artefact.

---



## 20. Appendices



### Appendix A — Module & Feature Index


| Module | Module Name                                        | Type     | Feature IDs (count)   |
| ------ | -------------------------------------------------- | -------- | --------------------- |
| 01     | Access Control, Person–Post–Role & Forensic Audit  | Shared   | F01-001 … F01-010 (10) |
| 02     | FE Master Import (from existing application)       | Business | F02-001 … F02-004 (4) |
| 03     | Asset Attachment & Recovered Funds                 | Business | F03-001 … F03-006 (6) |
| 04     | Depositor Master & Identity Verification           | Business | F04-001 … F04-010 (10) |
| 05     | Investment Portfolio Management                    | Business | F05-001 … F05-008 (8) |
| 06     | Claim Notification & Intake                        | Business | F06-001 … F06-005 (5) |
| 07     | Claim Verification, Evaluation & Approval          | Business | F07-001 … F07-005 (5) |
| 08     | Settlement, Payment & Closure                      | Business | F08-001 … F08-005 (5) |
| 09     | Operational Reports, Lists & Special Court Outputs | Business | F09-001 … F09-007 (7) |


**Total modules:** 9  
**Total feature outlines:** 60  

### Appendix B — Source module consolidation map


| Source (Business Process Flow)                             | This SOW                                                                                                         |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Phase 1–4 (business prelude)                               | §2, §7.1; investigation process out of scope                                                                     |
| Module 1 — FE Management                                   | **Not rebuilt.** Module 02 imports only FE details, Directors and Promoters, Investment Schemes. Remainder of Module 1 stays in the existing application. ED / court report / dashboards (claim-side) in Module 09; penny-drop and special situations in Module 04 |
| Module 2 — Asset Attachment & Recovery                     | Module 03                                                                                                        |
| Module 3 — Claim & Depositor Master                        | Module 04                                                                                                        |
| Module 4 — Investment Portfolio                            | Module 05                                                                                                        |
| 3A — Claim Notification                                    | Module 06                                                                                                        |
| 3B — Online Claim Submission                               | Module 06 (staff-mediated + constrained OOK)                                                                     |
| 3C — Claim Verification & Evaluation                       | Module 07                                                                                                        |
| Claim Approval                                             | Module 07                                                                                                        |
| 4A — Recovery & Settlement                                 | Module 08                                                                                                        |
| 4B — Payment & Claim Closure                               | Module 08                                                                                                        |
| Key Aspect 1 — Legacy / web app                            | Module 02 (FE import) and Module 09 / §10                                                                        |
| Key Aspect 2 — Agentic, not generative                     | Modules 07, 05, 04 and §5                                                                                        |
| Key Aspect 3 — Forensic audit                              | Module 01, 08                                                                                                    |
| Key Aspect 4 — Document software                           | Module 09 / §10                                                                                                  |
| Key Aspect 5 — Court petitions/orders                      | Legal Management Application (separate SOW); not duplicated in this Claim Management SOW                         |
| Key Aspect 6 — Bank/cash, penny-drop, excess payment       | Modules 04, 05, 08                                                                                               |
| Key Aspect 7 — Lists (claimants, accused, colluders, etc.) | Module 09; Vakalat / Caveat and similar legal drafts belong to the Legal Management SOW                          |
| Website review 12-08-2026 — access / 2FA / Person–Post     | Module 01 and §8                                                                                                 |
| Website review — structured depositor / asset / claim / reports | Modules 03, 04, 06–09                                                                                        |
| Website review — domain and UX                             | §9, §12                                                                                                          |




### Appendix C — Key entities


| Entity                   | Meaning                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------- |
| **FE**                   | Fraudulent Entity / Financial Establishment. **Master record lives in the existing FE application**; this claim application imports unique ID, name, directors/promoters and schemes |
| **Competent Authority**  | Authority appointed to settle investor claims (SPLOCA for IMA and other assigned cases) |
| **Depositor / Claimant** | Person with a unique cross-FE profile who may file a claim                              |
| **Claim window**         | Period during which submissions are accepted for named FE/schemes                       |
| **Recovered amount**     | Funds from attached-asset recovery available for settlement                             |
| **Net payable**          | Eligible amount minus previous returns and previous settlements                         |




### Appendix D — Document types (indicative)

Identity proof; investment proof / deposit receipt; bank documents / pass book; nominee or legal-heir documents; affidavit; statement of investment; attachment orders; bank returns; additional documents requested during verification.

FIR / charge sheet / court order / government notification / seized papers remain in the **existing FE application** and are not stored as an FE dossier in this application.

---

**End of Statement of Work — Claim Management System (KPID / SPLOCA)**