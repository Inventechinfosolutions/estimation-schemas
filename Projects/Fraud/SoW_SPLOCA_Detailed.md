# Statement of Work (SOW)

# SPLOCA Legal Management Application

**Document Type:** Statement of Work – Functional & Delivery Requirements  
**Version:** 1.0  
**Status:** Draft for RFP / Implementation  
**Source:** Annexure-I — `SPLOCA_Legal_Management_Application.md` (from scanned `Scan documents20260811_133355.pdf`)  
**Prepared for:** SPLOCA / Legal Cell (Fraud Prevention & Prosecution context as implied by Annexure organisational units)

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Abbreviations & Expansions](#2-abbreviations--expansions)
3. [Project Overview](#3-project-overview)
4. [Project Objectives](#4-project-objectives)
5. [In Scope / Out of Scope](#5-in-scope--out-of-scope)
6. [Solution Expectations](#6-solution-expectations)
7. [Consolidated Functional Modules](#7-consolidated-functional-modules)
8. [End-to-End Workflows](#8-end-to-end-workflows)
9. [Access Control / RBAC](#9-access-control--rbac)
10. [Channels – Web Portal & Android Mobile](#10-channels--web-portal--android-mobile)
11. [Integrations](#11-integrations)
12. [Audit, Compliance & Security](#12-audit-compliance--security)
13. [Non-Functional Requirements](#13-non-functional-requirements)
14. [Data Migration](#14-data-migration)
15. [Phased Delivery](#15-phased-delivery)
16. [Deliverables](#16-deliverables)
17. [Acceptance Criteria (Program Level)](#17-acceptance-criteria-program-level)
18. [Expected Benefits](#18-expected-benefits)
19. [Assumptions & Dependencies](#19-assumptions--dependencies)
20. [Vendor Response Expectations](#20-vendor-response-expectations)
21. [Appendices](#21-appendices)

---

## 1. Introduction

This Statement of Work (SOW) defines the functional and delivery requirements to **design, develop, test, deploy, and commission** the **SPLOCA Legal Management Application** as specified in **Annexure-I**.

The application shall provide a unified legal work platform for SPLOCA legal and related offices to:

- Maintain a coded, keyword-hyperlinked **Legal Database** (Acts & Rules, research/legal opinions, Special Court and High Court orders, petitions, SOBs, written arguments)
- Search the corpus via **natural language** and **Boolean** search with highlighted, hyperlinked results
- Enable **Client – Legal Section collaboration** (reports, queries, tasks, meetings, document sharing, limited/community access, anytime-anywhere access)
- Support **Legal Team communication & collaboration** (hierarchy / need-to-know access, full task lifecycle, team messaging, calendar, email sync)
- Maintain a **Unified Contact Database** across SPLOCA and related offices and contact categories
- Capture **Court Attendance & Expenses** and submit expense bills
- Provide **Knowledge, Expertise, Tools & Training** repositories and modules
- Deliver **Matter Management** with integrated dashboard and matter-wise reports
- Provide an **Android Mobile Application** for Advocates & Legal Cell covering contacts, matters, tasks, communication, time entry, dashboard, messaging, attendance/expense, and documents
- Meet stated **Security** requirements (instant backup; HTTPS/SSL and AES 256-bit encryption)

**Document handling**, **versioning**, **controlled sharing**, and **task/workflow actions** are **embedded** inside the relevant business modules. They are not bid as a separate Document Management or BPM product unless the purchaser later expands scope.

Abbreviations used in Annexure-I and this SOW are expanded in **Section 2 — Abbreviations & Expansions**.

---

## 2. Abbreviations & Expansions

The following expansions are used for this SOW. Where an Annexure term is organisation-specific, the expansion reflects **SPLOCA / KPIDFE** usage in Karnataka. Any residual ambiguity shall be confirmed by SPLOCA Legal Cell during requirements workshops.

### 2.1 Organisation & statute

| Abbreviation | Expansion | Notes |
| ------------ | --------- | ----- |
| **SPLOCA** | Special Officer & Competent Authority | Government of Karnataka office dealing with IMA & other KPIDFE cases |
| **KPIDFE** | Karnataka Protection of Interest of Depositors in Financial Establishments Act, 2004 | Governing statute for depositor-protection / financial-establishment fraud cases |
| **IMA** | IMA & other company / financial-establishment fraud matters handled by SPLOCA | As named on SPLOCA materials (“IMA & Other KPIDFE cases”) |
| **DFPC** | District Fraud Prevention Cell | Listed in Annexure contact coverage |

### 2.2 Offices, roles & parties

| Abbreviation | Expansion | Notes |
| ------------ | --------- | ----- |
| **CA** | Competent Authority | Statutory / designated authority under KPIDFE / SPLOCA; also keyword and matter/report dimension |
| **FE** | Financial Establishment | Notified / fraudulent financial establishment under KPIDFE; keyword and matter/report dimension |
| **RC** | Regional Commissioner | As in “RC Office” in Annexure contact list |
| **RD** | Revenue Department | Indicative GoK expansion alongside RC/CA; confirm with SPLOCA if a different office is intended |
| **IO** / **IOs** | Investigating Officer(s) | Annexure contact coverage (“IOs”) |
| **AC** | Assistant Commissioner | Annexure example key official (with Tahsildar, Sub Registrar) |
| **OP** | Opposite Party | Party opposing the petitioner in cases/petitions (“Petitioner & OP”) |
| **Legal Cell / Legal Team** | SPLOCA Legal Cell / Legal Team | Internal legal users of the application |

### 2.3 Legal document types & records

| Abbreviation | Expansion | Notes |
| ------------ | --------- | ----- |
| **SOB** | Statement of Objections | Legal pleading / document class in Annexure Legal Database (alongside Petitions and Written Arguments); confirm exact SPLOCA docket label in workshop if different |
| **OM** | Office Memorandum | Knowledge repository document type |
| **GO** | Government Order | Knowledge repository document type |
| **SOP** | Standard Operating Procedure | Manuals, Guidelines and SOP database |
| **Guard File** | Guard File | Official circular / standing-instruction file set maintained with OM/GO |

### 2.4 Technology & delivery terms

| Abbreviation | Expansion |
| ------------ | --------- |
| **HTTPS** | Hypertext Transfer Protocol Secure |
| **SSL** | Secure Sockets Layer (TLS/SSL as denoted in Annexure “Https/SSL”) |
| **AES** | Advanced Encryption Standard (Annexure: AES 256-bit) |
| **SMS** | Short Message Service |
| **UAT** | User Acceptance Testing |
| **RBAC** | Role-Based Access Control |
| **NFR** | Non-Functional Requirement |
| **RFP** | Request for Proposal |
| **SOW** | Statement of Work |

### 2.5 Confirmation rule

If SPLOCA’s internal glossary differs for **SOB**, **RD**, or **IMA** naming, the **SPLOCA-confirmed expansion** shall prevail without changing functional scope.

---

## 3. Project Overview



### 2.1 Business Context


| Aspect                             | Description                                                                                                                                   |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Solution                           | SPLOCA Legal Management Application                                                                                                           |
| Primary users                      | Advocates, Legal Cell / Legal Team, Client-side legal section users, authorised office staff                                                  |
| Organisational coverage (contacts) | SPLOCA Office, RC Office, CA, RD, District Fraud Prevention Cell, IOs, Legal Team                                                             |
| Channels                           | Web browser portal; Android mobile application                                                                                                |
| Access model                       | Hierarchy and **Need To Know** based access and visibility; Limited (selected users) / Community (all users) options for collaboration spaces |
| Primary outcome                    | Single platform for legal knowledge, matter work, collaboration, attendance/expenses, and mobile field/court use                              |




### 2.2 Guiding Principles

1. **Coded & hyperlinked legal knowledge** — Acts, opinions, orders, petitions, SOBs, and written arguments are coded and keyword-hyperlinked with mandatory reference fields as specified.
2. **Searchability** — Natural language and Boolean connector search with result highlighting and document address hyperlinks.
3. **Need-to-know collaboration** — Visibility follows hierarchy and need-to-know; sharing supports limited or community access.
4. **Matter-centric work** — Tasks, documents, communications, hearings, time, and key dates converge on the Matter Dashboard.
5. **Anytime-anywhere** — Web browser and Android access for authorised users.
6. **Secure by design** — HTTPS/SSL, AES 256-bit encryption, and instant backup / server storage for hardware-failure resilience.

---



## 4. Project Objectives

1. Implement the complete **Legal Database** with coding, referencing, and keyword hyperlinking for all document classes in Annexure-I §1.
2. Implement the **Key Words Database** covering FE, CA, Accused, Advocates, Presiding Judge, Act, Rules & Sections, Legal Doctrines.
3. Deliver **Search Facility** with natural language search, search-within-results, Boolean terms and connectors (AND, OR, NOT, /p, /s, /pg, /d, phrase, /#, root expander !, parentheses), and highlighted hyperlinked results.
4. Enable **Client – Legal Section Collaboration** including advocate reporting, client queries/tasks/meetings, document sharing for Information / Response / Correction / Opinion / Drafting / Approval, Limited/Community access, and web/Android access.
5. Enable **Legal Team Communication & Collaboration** with hierarchy/need-to-know rights, full task management lifecycle, and team communication features including email sync, individual/group messaging, calendar, and alerts.
6. Deliver a **Unified Contact Database** for listed offices and categorized contacts, with free-text search and SMS / Email / Team contact actions.
7. Deliver **Court Attendance & Expense Management** including cause-list upload, category-wise expenses with vouchers, search/retrieval, and expense bill submission.
8. Deliver **Knowledge, Expertise, Tools & Training Modules** including manuals/SOPs, forms/templates, key judgements, OM/GO/Guard File, training modules (Legal Research, Legal Writing, MS Word, MS Excel), and knowledge features (share, prevent knowledge leaks, searchable repository, ready reference, rights management).
9. Deliver **Matter Management** with integrated searchable dashboard, seven report dimensions, and all key matter features listed in Annexure-I §8.
10. Deliver **Mobile Application for Advocates & Legal Cell** with all capabilities listed in Annexure-I §9.
11. Meet **Security** requirements for backup and encrypted transmission (Annexure-I §10).

---



## 5. In Scope / Out of Scope



### 4.1 In Scope

**A. Functional (Annexure-I complete)**

- §1 Legal Database — Acts & Rules; Research & Legal Opinions; Special Court & High Court Orders; Petitions; SOBs; Written Arguments; Key Words Database  
- §2 Search Facility — natural language, Boolean connectors, highlight & hyperlink results  
- §3 Client – Legal Section Collaboration — advocate reports, client queries/tasks/meetings, document sharing purposes, Limited/Community access, web/Android anytime-anywhere access  
- §4 Legal Team Communication & Collaboration — hierarchy/need-to-know; Task Management (i–xi); Team Communication (i–vii)  
- §5 Unified Contact Database — creating database (i–v); using contact data (i–ii)  
- §6 Court Attendance & Expense Management — attendance, expenses, search, expense bill  
- §7 Knowledge, Expertise, Tools & Training — (a)–(f) including training modules and key features  
- §8 Matter Management — Matter Dashboard and Key Features  
- §9 Mobile Application for Advocates & Legal Cell — all listed capabilities  
- §10 Security — Backup; Data Transmission & Encryption (HTTPS/SSL, AES 256-bit)

**B. Delivery (implementation baseline)**

- Requirements confirmation workshops against this SOW / Annexure-I  
- Solution design (functional), configuration, development of web and Android applications  
- Unit, system, and integration testing; UAT support  
- Deployment on purchaser-provided / agreed infrastructure  
- User manuals and training for key user groups  
- Go-live support / hypercare as agreed in contract



### 4.2 Out of Scope (unless added by change request)

- Native **iOS** mobile application (Annexure specifies **Android**; iOS only if later authorised)  
- Replacement of court e-filing systems or judiciary case management systems outside SPLOCA control  
- Procurement of SMS gateway / email service commercial accounts (integration is in scope; accounts facilitated by purchaser)  
- Full enterprise ERP / payroll / general ledger replacement  
- Hardware procurement (servers, scanners, devices) unless stated in commercial RFP  
- Bulk physical digitization / scanning of paper archives (system shall accept uploaded/scanned files; scanning labour remains purchaser unless contracted)  
- Legacy data migration of historical case archives **unless** a migration package is separately ordered (Annexure-I does not define migration datasets)

---



## 6. Solution Expectations


| Area                  | Expectation                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------- |
| Channels              | Secure web portal (browser) + Android mobile app for Advocates & Legal Cell              |
| Access                | Hierarchy + Need To Know visibility; Limited vs Community collaboration options          |
| Legal content         | Coded records with keyword hyperlinks and mandatory reference fields per document class  |
| Search                | Natural language + Boolean connector search; highlight and hyperlink to document address |
| Collaboration         | Client–legal and legal-team spaces; tasks, messaging, calendar, document sharing         |
| Matter work           | Matter Dashboard integrating tasks, documents, communications, hearings, time, key dates |
| Contacts              | Unified address book across listed offices and contact categories                        |
| Attendance / expenses | Court attendance with cause list; category-wise expenses with vouchers; expense bills    |
| Knowledge             | SOPs, templates, judgements, OM/GO/Guard File, training modules; rights-managed sharing  |
| Security              | Instant backup to server; HTTPS/SSL; AES 256-bit encryption                              |
| Documents             | Upload, scan-in, version, share with controlled access — embedded in modules             |
| Language              | English UI mandatory at go-live unless purchaser requires additional language            |


---



## 7. Consolidated Functional Modules

The solution shall be delivered as **twelve consolidated modules**. Document upload/version/share and task workflow steps are **embedded** inside Modules 03–11 as applicable.

---



### 01. Access Control & Need-To-Know Security

**Purpose:** Provide user identity, hierarchy and need-to-know based access and visibility rights, and Limited / Community collaboration access options.

**Functional requirements:**

- Create and manage users for Advocates, Legal Cell, Client-side users, and office roles as configured.  
- Enforce **Hierarchy and Need To Know based Access and Visibility Rights**.  
- Support collaboration space access as **Limited (selected users)** or **Community Access (all users)**.  
- Apply rights management for sensitive documents and controlled file sharing (aligned with Module 10 / matter documents).  
- Authenticate web and Android clients for authorised users only.

**Acceptance criteria:**


| ID      | Criterion                                                                              |
| ------- | -------------------------------------------------------------------------------------- |
| M01-AC1 | Users see only matters/documents/messages permitted by hierarchy / need-to-know rules. |
| M01-AC2 | Limited vs Community access options are enforceable on collaboration spaces.           |
| M01-AC3 | Unauthorised users cannot access restricted documents or matters.                      |




#### Key capabilities (feature outline)


| Feature ID | Capability                          | Description                                                           |
| ---------- | ----------------------------------- | --------------------------------------------------------------------- |
| F01-001    | User & identity management          | Create/manage users for advocates, legal cell, clients, offices       |
| F01-002    | Hierarchy & need-to-know visibility | Configure and enforce hierarchical / need-to-know access rights       |
| F01-003    | Limited vs community access         | Apply selected-user vs all-user collaboration access options          |
| F01-004    | Controlled document rights          | Enforce controlled file sharing / access control on sensitive content |
| F01-005    | Web & mobile authentication         | Secure login for web browser and Android app                          |


---



### 02. Keyword & Reference Masters

**Purpose:** Maintain the Key Words Database and reference vocabularies used for coding and hyperlinking legal content.

**Functional requirements:**

- Maintain Key Words Database entities: **FE, CA, Accused, Advocates, Presiding Judge, Act, Rules & Sections, Legal Doctrines**.  
- Support coding of Acts & Rules and linkage of keywords for hyperlinking.  
- Enable administrators to add/update keyword terms used across Legal Database and Search.

**Acceptance criteria:**


| ID      | Criterion                                                                 |
| ------- | ------------------------------------------------------------------------- |
| M02-AC1 | All listed keyword entity types can be maintained without code change.    |
| M02-AC2 | Keywords are available for coding/hyperlinking in Legal Database records. |




#### Key capabilities (feature outline)


| Feature ID | Capability                        | Description                                                                                  |
| ---------- | --------------------------------- | -------------------------------------------------------------------------------------------- |
| F02-001    | Keyword entity masters            | Maintain FE, CA, Accused, Advocates, Presiding Judge, Act, Rules & Sections, Legal Doctrines |
| F02-002    | Act & Rules coding catalogue      | Code relevant Acts and Rules for hyperlinking                                                |
| F02-003    | Keyword–document link maintenance | Maintain keyword associations used for hyperlinks                                            |


---



### 03. Legal Database

**Purpose:** Store, code, reference, and keyword-hyperlink all legal document classes specified in Annexure-I §1.

**Functional requirements:**

- **Acts & Rules:** Relevant Acts and Rules shall be coded and key words hyperlinked.  
- **Research opinions and Legal Opinions:** Referenced to FE, CA, Date, Cases/Petitions (with Petitioner & OP); coded; key words (Case Number / FE / CA / Date of Filing / Date of Order / Act & Section) hyperlinked.  
- **Special Court Orders and High Court Orders:** Referenced to FE, CA, Accused, Advocates, Presiding Judge, Date, Cases/Petitions (with Petitioner & OP); coded; key words (Case Number / FE / CA / Date of Filing / Date of Order / Act & Section) hyperlinked.  
- **Petitions:** Same reference and keyword hyperlink pattern as orders (FE, CA, Accused, Advocates, Presiding Judge, Date, Cases/Petitions with Petitioner & OP; Case Number / FE / CA / Date of Filing / Date of Order / Act & Section).  
- **SOBs:** Same reference and keyword hyperlink pattern as petitions/orders.  
- **Written Arguments:** Same reference and keyword hyperlink pattern as petitions/orders.  
- Upload / attach source documents; navigate via keyword hyperlinks to related records.

**Acceptance criteria:**


| ID      | Criterion                                                                              |
| ------- | -------------------------------------------------------------------------------------- |
| M03-AC1 | Each document class (a–f) can be created with mandatory reference fields as specified. |
| M03-AC2 | Keywords are hyperlinked and resolve to related records / document addresses.          |
| M03-AC3 | Acts & Rules are coded and keyword-hyperlinked.                                        |




#### Key capabilities (feature outline)


| Feature ID | Capability                                 | Description                                                                  |
| ---------- | ------------------------------------------ | ---------------------------------------------------------------------------- |
| F03-001    | Acts & Rules register                      | Code Acts & Rules with keyword hyperlinks                                    |
| F03-002    | Research & legal opinions register         | Capture opinions with FE/CA/Date/Cases-Petitions refs and keyword hyperlinks |
| F03-003    | Special Court & High Court orders register | Capture orders with full reference set and keyword hyperlinks                |
| F03-004    | Petitions register                         | Capture petitions with full reference set and keyword hyperlinks             |
| F03-005    | SOB register                               | Capture SOBs with full reference set and keyword hyperlinks                  |
| F03-006    | Written arguments register                 | Capture written arguments with full reference set and keyword hyperlinks     |
| F03-007    | Keyword hyperlink navigation               | Navigate from keywords to linked legal records/documents                     |


---



### 04. Search Facility

**Purpose:** Provide natural language and Boolean connector search across the legal corpus with highlighted, hyperlinked results.

**Functional requirements:**

- Search box to enter keywords.  
- **Natural language search** (Google-like; e.g. “What are the elements of battery?”).  
- **Search Within Results** using key words.  
- **Boolean Terms and Connector** support: AND, OR, NOT; /p (same paragraph); /s (same sentence); /pg (same page); /d (same document); "" phrase; /# (where # is a number); ! root expander (e.g. Obey! → Obey, Obeys, Obeyed, Obeying); () parenthesis to group terms.  
- Highlight & hyperlink keywords with document address in Results.

**Acceptance criteria:**


| ID      | Criterion                                                                                                |
| ------- | -------------------------------------------------------------------------------------------------------- |
| M04-AC1 | Natural language queries return relevant documents from the indexed corpus.                              |
| M04-AC2 | Boolean operators and proximity connectors (/p, /s, /pg, /d), phrase, /#, !, and () behave as specified. |
| M04-AC3 | Search Within Results narrows the current result set by keywords.                                        |
| M04-AC4 | Results highlight keywords and hyperlink to document address.                                            |




#### Key capabilities (feature outline)


| Feature ID | Capability                      | Description                                                           |
| ---------- | ------------------------------- | --------------------------------------------------------------------- |
| F04-001    | Search box & corpus indexing    | Keyword entry and searchable index over legal/knowledge content       |
| F04-002    | Natural language search         | Google-like NL search including example query patterns                |
| F04-003    | Search within results           | Refine current results using additional keywords                      |
| F04-004    | Boolean & connector search      | AND/OR/NOT, /p, /s, /pg, /d, phrase, /#, root expander !, parentheses |
| F04-005    | Highlighted hyperlinked results | Highlight keywords and link to document address in results            |


---



### 05. Unified Contact Database

**Purpose:** Unify organisational and matter-related contacts into one address database with search and outreach actions.

**Functional requirements:**

**Creating Database:**

- Cover contacts for: SPLOCA Office, RC Office, CA, RD, District Fraud Prevention Cell, IOs, Legal Team.  
- Categorized addition of contacts of Advocates / Accused / Petitioners / Visitors / External Experts / Key Officials like Tahsildar, AC, Sub Registrar.  
- Convert multiple business contact lists into one unified address.  
- Classify contacts or add a new customized category.  
- Update feature to add relevant details to existing contacts.

**Using Contact Data:**

- Free text search to find match from existing database.  
- Seamlessly send number to SMS / Email / Team for contacting (phone / mail).

**Acceptance criteria:**


| ID      | Criterion                                                                     |
| ------- | ----------------------------------------------------------------------------- |
| M05-AC1 | Contacts for all listed offices and categories can be created and classified. |
| M05-AC2 | Multiple lists can be unified into one address book.                          |
| M05-AC3 | Free-text search finds matching contacts.                                     |
| M05-AC4 | User can initiate SMS / Email / Team contact actions from a contact.          |




#### Key capabilities (feature outline)


| Feature ID | Capability                               | Description                                                                |
| ---------- | ---------------------------------------- | -------------------------------------------------------------------------- |
| F05-001    | Office & organisation contact coverage   | Maintain contacts for SPLOCA, RC, CA, RD, DFPC, IOs, Legal Team            |
| F05-002    | Categorized contact types                | Advocates, Accused, Petitioners, Visitors, External Experts, Key Officials |
| F05-003    | Unified address book & custom categories | Merge lists; classify; add custom categories; update details               |
| F05-004    | Contact free-text search                 | Find contacts from the unified database                                    |
| F05-005    | SMS / Email / Team contact actions       | Initiate phone/mail outreach via SMS, Email, or Team                       |


---



### 06. Matter Management

**Purpose:** Create and manage matters with an integrated dashboard, reports, documents, consultations, tasks, and key-date tracking.

**Functional requirements:**

**Matter Dashboard:**

- Integrate Tasks, Documents, Communication & Messages, Activities, Team Members, Client Contacts, Court Hearings, Time Entry, Key Dates.  
- Searchable dashboard.  
- Reports: Case wise; Court wise; Team Member Wise; CA Wise; FE Wise; Key Date Wise; Stage wise.

**Key Features:**

- Create New Matter, Classify, Add Descriptions, FE, CA, Court, Opponents, Date.  
- Capture & edit variables: court details, matter type, matter details, category & issues, Opponent & lawyers detail.  
- Share files with controlled access.  
- Consult Client / External Expert / Research Expert / Other.  
- Create and edit documents and maintain version of documents.  
- Scan and upload matter related documents.  
- Assign Tasks.  
- Track Key Date & Deadline & Alerts.

**Acceptance criteria:**


| ID      | Criterion                                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| M06-AC1 | Matter Dashboard shows integrated tasks, documents, communications, activities, team, client contacts, hearings, time entry, key dates. |
| M06-AC2 | All seven report dimensions are available and filterable.                                                                               |
| M06-AC3 | Matter create/edit captures FE, CA, Court, Opponents, Date and listed variables.                                                        |
| M06-AC4 | Document versioning, scan/upload, controlled share, consultation, task assign, and key-date alerts work on the matter.                  |




#### Key capabilities (feature outline)


| Feature ID | Capability                  | Description                                                                                     |
| ---------- | --------------------------- | ----------------------------------------------------------------------------------------------- |
| F06-001    | Matter create & classify    | Create matter with descriptions, FE, CA, Court, Opponents, Date                                 |
| F06-002    | Matter variable capture     | Court details, type, details, category & issues, opponent & lawyers                             |
| F06-003    | Matter dashboard            | Integrated view of tasks, docs, messages, activities, team, contacts, hearings, time, key dates |
| F06-004    | Matter search               | Searchable matter dashboard / register                                                          |
| F06-005    | Matter reports              | Case, Court, Team Member, CA, FE, Key Date, Stage wise reports                                  |
| F06-006    | Matter documents & versions | Create/edit/version; scan/upload; controlled share                                              |
| F06-007    | Consultations               | Consult Client / External Expert / Research Expert / Other                                      |
| F06-008    | Matter tasks & key dates    | Assign tasks; track key dates/deadlines with alerts                                             |


---



### 07. Client – Legal Section Collaboration

**Purpose:** Enable collaboration between Advocates / Legal Section and Clients as specified in Annexure-I §3.

**Functional requirements:**

- Advocates to report: Court Proceedings / Directions of court, Stay Alerts, Cause Lists, Time Critical Responses, Quick Information, To Do Lists.  
- Clients to Raise Queries, Request Tasks, Schedule Meetings.  
- Document Sharing for Information / Response / Correction / Opinion / Drafting / Approval.  
- Option for Limited (selected users) / Community Access (all users).  
- Anytime-Anywhere Access via web browser / Android.

**Acceptance criteria:**


| ID      | Criterion                                                                      |
| ------- | ------------------------------------------------------------------------------ |
| M07-AC1 | Advocates can submit all listed report/alert/list types to clients.            |
| M07-AC2 | Clients can raise queries, request tasks, and schedule meetings.               |
| M07-AC3 | Document sharing supports the six stated purposes.                             |
| M07-AC4 | Limited and Community access options apply to collaboration content.           |
| M07-AC5 | Collaboration functions are available on web and Android for authorised users. |




#### Key capabilities (feature outline)


| Feature ID | Capability                               | Description                                                                                         |
| ---------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------- |
| F07-001    | Advocate court reporting pack            | Proceedings, directions, stay alerts, cause lists, time-critical responses, quick info, to-do lists |
| F07-002    | Client queries, tasks & meetings         | Clients raise queries, request tasks, schedule meetings                                             |
| F07-003    | Collaboration document sharing           | Share for Information/Response/Correction/Opinion/Drafting/Approval                                 |
| F07-004    | Limited / community collaboration spaces | Selected-user vs all-user access on collaboration content                                           |


---



### 08. Legal Team Communication & Task Management

**Purpose:** Provide legal team task lifecycle and team communication tools per Annexure-I §4.

**Functional requirements:**

**Task Management:**

- Assignment Of Task; Assign Due Date; Status Of Task; Alerts; Accept/Reject Task; Reassign Task; Reminder; Overdue Tasks; Reprimand / Warning; Publish Task Completion Report with Attachment; Publish Team Member Task Schedule & Status.

**Team Communication:**

- Quick tab in the side bar to relay communication to the team.  
- Saving Records of Communication for each matter.  
- Search for Communication briefs and messages (by Person / Date / Case / Key Word).  
- Sync email services.  
- Provision of both individual & group messaging.  
- Calendar for task overview and status of each task with team members.  
- Share files, bills, tasks and calendar with alert.

**Acceptance criteria:**


| ID      | Criterion                                                                                                   |
| ------- | ----------------------------------------------------------------------------------------------------------- |
| M08-AC1 | All eleven task-management actions (i–xi) are available and auditable.                                      |
| M08-AC2 | Overdue, reminder, accept/reject, reassign, reprimand/warning behaviours work as configured.                |
| M08-AC3 | Task completion report can be published with attachment; team schedule & status can be published.           |
| M08-AC4 | Sidebar quick communication, matter-linked message history, and search by Person/Date/Case/Key Word work.   |
| M08-AC5 | Email sync, individual/group messaging, calendar, and share-with-alert for files/bills/tasks/calendar work. |




#### Key capabilities (feature outline)


| Feature ID | Capability                            | Description                                                        |
| ---------- | ------------------------------------- | ------------------------------------------------------------------ |
| F08-001    | Task assignment & due dates           | Assign tasks and due dates                                         |
| F08-002    | Task status, accept/reject, reassign  | Status tracking; accept/reject; reassign                           |
| F08-003    | Task alerts, reminders, overdue       | Alerts, reminders, overdue handling                                |
| F08-004    | Reprimand / warning                   | Issue reprimand/warning on tasks                                   |
| F08-005    | Task completion & schedule publish    | Completion report with attachment; team schedule & status publish  |
| F08-006    | Sidebar team communication            | Quick sidebar relay to the team                                    |
| F08-007    | Matter communication records & search | Save per-matter communications; search by person/date/case/keyword |
| F08-008    | Email sync & messaging                | Sync email; individual & group messaging                           |
| F08-009    | Team calendar & share-with-alert      | Calendar overview; share files/bills/tasks/calendar with alert     |


---



### 09. Court Attendance & Expense Management

**Purpose:** Capture court attendance and category-wise expenses; support search and expense bill submission.

**Functional requirements:**

- **Court Attendance:** Submit Attendance with Name / Code, Date, Court, Location, Entry Time, Presiding Judge, Matter, Brief on Proceedings, Effective / Ineffective, Exit Time, & upload with Cause List.  
- Capture expenses category wise — Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage, Specified Other Expense with attached document / voucher.  
- Quick search and retrieval.  
- Submit Expense Bill.

**Acceptance criteria:**


| ID      | Criterion                                                                |
| ------- | ------------------------------------------------------------------------ |
| M09-AC1 | Attendance captures all listed fields and supports cause-list upload.    |
| M09-AC2 | Expenses support all listed categories with voucher/document attachment. |
| M09-AC3 | Quick search retrieves attendance and expense records.                   |
| M09-AC4 | Expense bill can be submitted from captured expenses.                    |




#### Key capabilities (feature outline)


| Feature ID | Capability                    | Description                                                                         |
| ---------- | ----------------------------- | ----------------------------------------------------------------------------------- |
| F09-001    | Court attendance capture      | Attendance with all Annexure fields + cause list upload                             |
| F09-002    | Category-wise expense capture | Travel, boarding, lodging, local travel, court expenses, clerkage, other + vouchers |
| F09-003    | Attendance & expense search   | Quick search and retrieval                                                          |
| F09-004    | Expense bill submission       | Submit expense bill from captured expenses                                          |


---



### 10. Knowledge, Expertise, Tools & Training

**Purpose:** Provide knowledge repositories, templates, judgements, OM/GO/Guard File, training modules, and knowledge governance features.

**Functional requirements:**

- Manuals, Guidelines and SOP database with key words hyperlinked.  
- Forms & Format Templates.  
- Key Judgement database.  
- OM, GO & Guard File Database.  
- Training Modules: Legal Research; Legal Writing; MS Word; MS Excel.  
- Key Features: Create, share, use and manage knowledge and information assets; Information and knowledge sharing; Prevent ‘knowledge leaks’ (systemized aggregation of an outgoing team member’s proprietary knowledge); Searchable repository (systematically docketed; title and word search); Ready reference (date of file creation and author details); Rights Management (controlled file sharing and access control).

**Acceptance criteria:**


| ID      | Criterion                                                                                                                |
| ------- | ------------------------------------------------------------------------------------------------------------------------ |
| M10-AC1 | SOP/manuals, templates, judgements, OM/GO/Guard File repositories are available with keyword hyperlinks where specified. |
| M10-AC2 | Four training modules are accessible to authorised users.                                                                |
| M10-AC3 | Knowledge assets can be created, shared, searched by title/word, and show creation date/author.                          |
| M10-AC4 | Outgoing member knowledge aggregation (anti-leak) process is supported.                                                  |
| M10-AC5 | Sensitive knowledge is protected by controlled sharing / access control.                                                 |




#### Key capabilities (feature outline)


| Feature ID | Capability                              | Description                                                        |
| ---------- | --------------------------------------- | ------------------------------------------------------------------ |
| F10-001    | Manuals, guidelines & SOP library       | SOP/manuals database with keyword hyperlinks                       |
| F10-002    | Forms & format templates                | Maintain and use forms/format templates                            |
| F10-003    | Key judgement database                  | Store and retrieve key judgements                                  |
| F10-004    | OM, GO & Guard File database            | OM/GO/Guard File repository                                        |
| F10-005    | Training modules                        | Legal Research, Legal Writing, MS Word, MS Excel                   |
| F10-006    | Knowledge share & searchable repository | Create/share/manage; title & word search; ready reference metadata |
| F10-007    | Knowledge-leak prevention               | Aggregate outgoing team member proprietary knowledge               |
| F10-008    | Knowledge rights management             | Controlled file sharing and access control for sensitive knowledge |


---



### 11. Mobile Application (Android) for Advocates & Legal Cell

**Purpose:** Deliver Android mobile capabilities listed in Annexure-I §9 for Advocates and Legal Cell.

**Functional requirements:**

- Add Contact  
- Add Matter  
- Task Management — Create task, Assign, Accept/Reject task, Reassign, Mark status as completed, View Task inbox, Overdue items, Task Outbox  
- Send Communication  
- Make Time Entry  
- View Matter Dashboard — Tasks, Communication, Documents, Court Hearings, Team Members, Client contact related to the matter all in one place  
- Internal Messaging  
- Attendance, Expense recording  
- Documents — View, Download, Create folder, Upload and View shared documents

**Acceptance criteria:**


| ID      | Criterion                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------- |
| M11-AC1 | All listed mobile capabilities are available to authorised Advocates / Legal Cell users on Android.                 |
| M11-AC2 | Matter Dashboard on mobile shows tasks, communication, documents, hearings, team members, client contacts together. |
| M11-AC3 | Task inbox/outbox, overdue, accept/reject, reassign, and completion work on mobile.                                 |
| M11-AC4 | Documents can be viewed, downloaded, folder-created, uploaded, and shared documents viewed on mobile.               |




#### Key capabilities (feature outline)


| Feature ID | Capability                       | Description                                                                   |
| ---------- | -------------------------------- | ----------------------------------------------------------------------------- |
| F11-001    | Mobile add contact & matter      | Add contact and add matter on Android                                         |
| F11-002    | Mobile task management           | Create/assign/accept-reject/reassign/complete; inbox; overdue; outbox         |
| F11-003    | Mobile communication & messaging | Send communication; internal messaging                                        |
| F11-004    | Mobile time entry                | Make time entry against matter/work                                           |
| F11-005    | Mobile matter dashboard          | Tasks, communication, documents, hearings, team, client contacts in one place |
| F11-006    | Mobile attendance & expense      | Attendance and expense recording on mobile                                    |
| F11-007    | Mobile documents                 | View, download, create folder, upload, view shared documents                  |


---



### 12. Platform Security, Backup & Encryption

**Purpose:** Meet Annexure-I §10 security requirements for backup and encrypted transmission.

**Functional requirements:**

- **Backup:** Instant back-up, and storage on server in case of hardware failure.  
- **Data Transmission & Encryption:** Encrypted — HTTPS/SSL and AES 256-bit encryption standard.  
- Ensure web and mobile channels use encrypted transport.

**Acceptance criteria:**


| ID      | Criterion                                                                                                                            |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| M12-AC1 | Instant backup to server storage is demonstrated; restore path documented for hardware-failure scenarios.                            |
| M12-AC2 | Application traffic uses HTTPS/SSL.                                                                                                  |
| M12-AC3 | AES 256-bit encryption standard is applied as designed for protected data at rest / sensitive payloads as agreed in security design. |




#### Key capabilities (feature outline)


| Feature ID | Capability                      | Description                                                        |
| ---------- | ------------------------------- | ------------------------------------------------------------------ |
| F12-001    | Instant backup & server storage | Instant backup with server storage for hardware-failure resilience |
| F12-002    | HTTPS/SSL transport security    | Encrypted data transmission via HTTPS/SSL                          |
| F12-003    | AES 256-bit encryption          | Apply AES 256-bit encryption standard as specified                 |


---



## 8. End-to-End Workflows



### 7.1 Legal Content Coding & Hyperlink Flow

```text
Capture / Upload Legal Artefact (Act/Rule, Opinion, Order, Petition, SOB, Written Argument)
→ Enter mandatory references (FE, CA, dates, parties, etc. as applicable)
→ Code & attach Keywords
→ Hyperlink keywords to related records
→ Available to Search Facility
```



### 7.2 Search Flow

```text
Enter NL or Boolean query → Results (highlight + document address hyperlink)
→ Optional Search Within Results → Open document / related record
```



### 7.3 Matter Lifecycle Flow

```text
Create Matter (classify, FE, CA, Court, Opponents, Date)
→ Capture variables / upload-scan documents / version
→ Assign Tasks / Track Key Dates & Alerts
→ Communications & Consultations
→ Court Hearings / Time Entry
→ Matter Dashboard & Reports (Case/Court/Team/CA/FE/Key Date/Stage)
```



### 7.4 Client–Legal Collaboration Flow

```text
Advocate reports (proceedings, stay, cause list, time-critical, quick info, to-do)
↔ Client queries / task requests / meetings
↔ Document sharing (Information/Response/Correction/Opinion/Drafting/Approval)
→ Access per Limited or Community setting
```



### 7.5 Task Management Flow

```text
Assign Task + Due Date → Accept/Reject → Work / Reassign
→ Reminders / Alerts / Overdue / Reprimand-Warning (as needed)
→ Complete → Publish Completion Report with Attachment
→ Team Schedule & Status publish
```



### 7.6 Attendance & Expense Flow

```text
Submit Court Attendance (+ Cause List)
→ Capture category-wise expenses + vouchers
→ Search / Retrieve
→ Submit Expense Bill
```

---



## 9. Access Control / RBAC



### 8.1 Access Model (from Annexure-I)

- **Hierarchy and Need To Know** based Access and Visibility Rights.  
- Collaboration content may use **Limited (selected users)** or **Community Access (all users)**.  
- Sensitive documents/knowledge protected through **controlled file sharing and access control**.



### 8.2 Indicative Actor Groups


| Actor group                                               | Typical use                                                            |
| --------------------------------------------------------- | ---------------------------------------------------------------------- |
| Advocate                                                  | Court reporting, matters, tasks, mobile court use, attendance/expenses |
| Legal Cell / Legal Team                                   | Matter work, collaboration, knowledge, tasks, messaging                |
| Client (Legal Section)                                    | Queries, task requests, meetings, shared documents                     |
| Office users (SPLOCA / RC / CA / RD / DFPC / IO contexts) | Contacts, need-to-know visibility as configured                        |
| Administrator                                             | Users, access rights, masters, keywords, system configuration          |


Vendor shall deliver a **role–permission–visibility matrix** during design for purchaser sign-off.

---



## 10. Channels – Web Portal & Android Mobile



### 9.1 Web Browser Portal

- Full functional access per role for Legal Database, Search, Collaboration, Team Communication/Tasks, Contacts, Attendance/Expenses, Knowledge, Matter Management, and administration.  
- Anytime-Anywhere access via web browser for authorised users.



### 9.2 Android Mobile Application (Advocates & Legal Cell)

Implements Annexure-I §9 capabilities listed under Module 11 (contacts, matters, tasks, communication, time entry, matter dashboard, internal messaging, attendance/expense, documents).

---



## 11. Integrations


| Integration   | Priority               | Notes                                                              |
| ------------- | ---------------------- | ------------------------------------------------------------------ |
| SMS Gateway   | Mandatory (functional) | Contact outreach; alerts as configured                             |
| Email Service | Mandatory (functional) | Contact outreach; Team Communication email sync                    |
| Email Sync    | Mandatory (functional) | Sync email services for team communication                         |
| Other systems | Conditional            | Only if identified during workshops and approved by change control |


---



## 12. Audit, Compliance & Security

- Audit trail for matter, task, document share, access-rights, and attendance/expense actions  
- Communication records retained per matter  
- Instant backup and server storage for hardware-failure scenarios  
- HTTPS/SSL for data transmission  
- AES 256-bit encryption standard  
- Controlled access to sensitive documents and knowledge assets

---



## 13. Non-Functional Requirements


| Area           | Requirement                                                                               |
| -------------- | ----------------------------------------------------------------------------------------- |
| Platforms      | Web (browser) + Android mobile                                                            |
| Availability   | Fit for operational legal-office use; backup/restore path for hardware failure            |
| Performance    | Search and matter dashboard usable under expected concurrent load (to be sized in design) |
| Security       | HTTPS/SSL; AES 256-bit; need-to-know access                                               |
| Usability      | Role-based screens; mobile usable for court/field advocate workflows                      |
| Search quality | Support NL and Boolean connector semantics as specified                                   |
| Backup         | Instant backup to server storage                                                          |


---



## 14. Data Migration

Annexure-I does **not** specify legacy dataset volumes or cutover rules.

- **Baseline:** Migration of historical archives is **out of scope** unless separately ordered.  
- System shall support **ongoing upload/scan** of matter and legal documents and **unification of contact lists** going forward.  
- If purchaser later provides structured extracts (contacts, matters, judgements), a migration work package may be added by change request.

---



## 15. Phased Delivery



### Phase 1 – Full Annexure-I Go-Live (Mandatory)

All Modules 01–12, web portal, Android mobile app, SMS/Email integrations, UAT, training, go-live.

### Phase 2 – Optional Enhancements (if ordered)

- iOS mobile application  
- Additional connectors beyond SMS/Email  
- Structured legacy archive migration  
- Additional language packs

---



## 16. Deliverables


| #   | Deliverable                                                 |
| --- | ----------------------------------------------------------- |
| 1   | Requirements confirmation / gap note against Annexure-I     |
| 2   | Functional solution design & access-visibility matrix       |
| 3   | Configured web application (Modules 01–10, 12 capabilities) |
| 4   | Android mobile application (Module 11)                      |
| 5   | Search facility meeting Boolean/NL requirements             |
| 6   | SMS and Email integrations (including email sync)           |
| 7   | Test evidence; UAT support & UAT sign-off pack              |
| 8   | Backup/restore demonstration and operations note            |
| 9   | User manuals (web + mobile) and training                    |
| 10  | Go-live support / hypercare as contracted                   |
| 11  | Source code / escrow per contract terms                     |


---



## 17. Acceptance Criteria (Program Level)

1. Every Annexure-I section (§1–§10) is demonstrably covered by Modules 01–12.
2. Legal Database document classes support stated reference fields and keyword hyperlinking.
3. Search supports NL, Search Within Results, all listed Boolean connectors, and highlighted hyperlinked results.
4. Client–Legal and Legal Team collaboration/task/communication features operate per Annexure.
5. Unified Contact Database covers listed offices/categories with search and SMS/Email/Team actions.
6. Court attendance, expenses, search, and expense bill submission work end-to-end.
7. Knowledge repositories, training modules, and knowledge governance features work as specified.
8. Matter Dashboard, seven report types, and matter key features work end-to-end.
9. Android app delivers all §9 capabilities.
10. Instant backup and HTTPS/SSL + AES 256-bit requirements are demonstrated.
11. UAT signed off with no open Critical/High defects.

---



## 18. Expected Benefits

- Single coded, searchable legal knowledge base with hyperlinked keywords  
- Faster retrieval via natural language and Boolean professional search  
- Structured client–legal and internal legal-team collaboration  
- Matter-centric visibility of tasks, documents, hearings, and key dates  
- Unified contacts across SPLOCA and related fraud-prevention offices  
- Mobile enablement for advocates and legal cell at court/field  
- Controlled sharing and knowledge retention when team members leave  
- Security baseline with backup and strong encryption

---



## 19. Assumptions & Dependencies

1. Annexure-I is the authoritative functional scope; this SOW organises it for implementation without dropping items.
2. Abbreviations follow **Section 2**; if SPLOCA’s internal glossary differs (especially SOB / RD / IMA), SPLOCA confirmation prevails. Exact field dictionaries confirmed in workshops.
3. Access model is **Hierarchy + Need To Know** plus Limited/Community options (not a Post/Person model unless purchaser later mandates).
4. Document management and task workflow are **embedded** (not separate products).
5. Mobile scope is **Android** only in Phase 1.
6. Purchaser facilitates SMS gateway and email service credentials/approvals.
7. Infrastructure/hosting for application and backup storage is purchaser-provided or commercially agreed.
8. Legacy archive migration is out of scope unless separately ordered.
9. Training module content for MS Word/Excel/Legal Research/Writing may use purchaser-supplied materials packaged into the app.
10. Project code **SPLOCA**; output root **Projects/Fraud/**; SOW purpose **RFP + implementation**.

---



## 20. Vendor Response Expectations

1. Clause-by-clause compliance matrix against Annexure-I §1–§10 and this SOW Module 01–12.
2. Approach for Legal Database coding/hyperlinking and Search (NL + Boolean connectors).
3. Hierarchy / need-to-know access design approach.
4. Android mobile delivery plan covering every §9 capability.
5. SMS/Email/email-sync integration approach.
6. Backup and encryption approach meeting §10.
7. Implementation plan, team, timeline, and assumptions.
8. Commercial proposal for Phase 1 and optional Phase 2 items.
9. Relevant case studies (legal / case / matter management for government or prosecution offices preferred).

---



## 21. Appendices



### Appendix A — Module & Feature Index


| Module | Module Name                                             | Type      | Feature IDs (count)   |
| ------ | ------------------------------------------------------- | --------- | --------------------- |
| 01     | Access Control & Need-To-Know Security                  | Shared    | F01-001 … F01-005 (5) |
| 02     | Keyword & Reference Masters                             | Shared    | F02-001 … F02-003 (3) |
| 03     | Legal Database                                          | Business  | F03-001 … F03-007 (7) |
| 04     | Search Facility                                         | Business  | F04-001 … F04-005 (5) |
| 05     | Unified Contact Database                                | Business  | F05-001 … F05-005 (5) |
| 06     | Matter Management                                       | Business  | F06-001 … F06-008 (8) |
| 07     | Client – Legal Section Collaboration                    | Business  | F07-001 … F07-004 (4) |
| 08     | Legal Team Communication & Task Management              | Business  | F08-001 … F08-009 (9) |
| 09     | Court Attendance & Expense Management                   | Business  | F09-001 … F09-004 (4) |
| 10     | Knowledge, Expertise, Tools & Training                  | Business  | F10-001 … F10-008 (8) |
| 11     | Mobile Application (Android) for Advocates & Legal Cell | Business  | F11-001 … F11-007 (7) |
| 12     | Platform Security, Backup & Encryption                  | Technical | F12-001 … F12-003 (3) |


**Total provisional features:** 68  

**Explicitly not separate modules:** Standalone Document Management product; standalone BPM/workflow engine (embedded in Modules 06–08, 10–11).

### Appendix B — Annexure-I Traceability


| Annexure section                                  | SOW coverage       |
| ------------------------------------------------- | ------------------ |
| §1 Legal Database (a–g)                           | Modules 02, 03     |
| §2 Search Facility (A–C)                          | Module 04          |
| §3 Client – Legal Section Collaboration (a–e)     | Modules 01, 07, 11 |
| §4 Legal Team Communication & Collaboration (a–c) | Modules 01, 08     |
| §5 Unified Contact Database (a–b)                 | Modules 05, 11     |
| §6 Court Attendance & Expense Management (a–d)    | Modules 09, 11     |
| §7 Knowledge, Expertise, Tools & Training (a–f)   | Module 10          |
| §8 Matter Management (a–b)                        | Module 06          |
| §9 Mobile Application                             | Module 11          |
| §10 Security (a–b)                                | Module 12          |




### Appendix C — Indicative Data Entities

User, Role, Visibility Rule, Keyword, Act/Rule, Legal Opinion, Court Order, Petition, SOB, Written Argument, Contact, Contact Category, Matter, Matter Document Version, Task, Communication Message, Calendar Entry, Court Attendance, Expense Item, Expense Bill, Knowledge Asset, Training Module, Time Entry, Court Hearing, Key Date, Backup Job, Audit Log.

### Appendix D — Document Types (Indicative)

Acts & Rules; Research Opinions; Legal Opinions; Special Court Orders; High Court Orders; Petitions; SOBs; Written Arguments; Cause Lists; Matter Documents (scanned/uploaded); Task Completion Reports; Expense Vouchers; Expense Bills; Manuals/Guidelines/SOPs; Forms & Format Templates; Key Judgements; OM; GO; Guard File documents; Shared collaboration documents.

---

*This SOW implements Annexure-I of the SPLOCA Legal Management Application in full. No Annexure functional item is intentionally omitted; organisational packaging into modules is for delivery and estimation only.*