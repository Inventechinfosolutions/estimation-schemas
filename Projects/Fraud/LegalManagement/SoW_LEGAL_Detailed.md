# Statement of Work

# Legal Management Application (KPID / SPLOCA)

**Document type:** Production-grade Statement of Work (RFP discussion and internal estimation)  
**Project code:** LEGAL  
**Client / Authority:** Special Officer & Competent Authority (SPLOCA) — IMA and other KPIDFE cases, Government of Karnataka  
**Version:** 1.0  
**Date:** 14 August 2026  
**Status:** Draft for review  

---

## Document control

| Item | Detail |
|------|--------|
| **Purpose** | External RFP discussion **and** internal estimation baseline |
| **Authority statute** | Karnataka Protection of Interest of Depositors in Financial Establishments (KPIDFE) Act, 2004 and connected rules |
| **Source (authoritative)** | (1) SPLOCA Legal Management Application — Annexure-I; (2) Proceedings of the meeting dated 10 August 2026 (legal, task, library, Android, templates, collaboration, security and common-database points) |
| **Related SOWs (same programme)** | **Claim Management** and **GIS field valuation (eValueI / eValueM)** are specified in separate SOWs. This document covers **Legal Management** only. |
| **Shared component** | **User management / Person–Post–Role access, official identity, OTP before activation, 2FA, joiner–mover–leaver, and forensic/login audit** are already specified in the **Claim Management SOW, Module 01 (F01-001 to F01-007 and F01-010)**. This Legal application **consumes that shared component**. It does **not** rebuild user management. |
| **Existing FE application** | FE dossiers are not rebuilt here. FE / CA names used as legal keywords and matter fields are consumed as references (imported FE identity as used by Claim Management). |

---

## 1. Introduction

This Statement of Work defines the functional and business scope for a **dedicated Legal Management Application** for SPLOCA — a role-based official **web** application and an **Android** application for Advocates and the Legal Cell.

It is **not** an extension of the existing public website. It supports systematic management of court matters: case particulars, filings, hearings, attendance, orders, compliance and next action; a coded legal library with search; tasks; collaboration; contacts; expenses; knowledge and training; and court-approved document templates.

**Person, Post, Role, official identity, OTP, 2FA and credential lifecycle are not specified again in this SOW.** Legal Cell officers, empaneled advocates and other legal users are provisioned on the **shared user-management component** already defined in the Claim Management SOW, Module 01. This SOW adds only Legal-specific access (Limited / Community spaces, legal document rights, Android authentication against that same identity).

This SOW does not prescribe APIs, database schemas, UI wireframes, or effort hours.

---

## 2. Project Overview

### 2.1 Business context

After KPIDFE invocation, SPLOCA’s Legal Cell and assigned advocates must manage Special Court and High Court work: petitions, SOBs, written arguments, orders, hearings, attendance, expenses, opinions and statutory notices. Annexure-I and the 10 August 2026 proceedings require a production legal web application with integrated task management, a digital library, templates in court-approved font and spacing, and Android for advocates and Legal Cell.

### 2.2 Solution character

| Characteristic | Requirement |
|----------------|-------------|
| **Nature** | Dedicated official Legal web + Android application for Advocates and Legal Cell |
| **Not** | A public portal; a rebuild of Claim Management or GIS valuation; a rebuild of user management; a generative-AI drafting product |
| **Access** | **Shared** Person–Post–Role identity from Claim Management Module 01, plus Legal Limited / Community spaces and need-to-know visibility |
| **AI policy** | Generative AI shall **not** be used. Agentic / rule-based assists only, with human verification and audit |
| **Common data** | Claims, legal, matter, task, attendance/expense, collaboration and static masters interconnect so authorised users open linked information without duplicate entry, subject to RBAC |
| **IP** | For in-house applications and software delivered under this engagement, intellectual property and source code shall **solely lie with SPLOCA** |
| **Hosting** | Designated server / approved cloud; Android distribution and Play Store licensing where specifically approved — licensing shall be clear, not speculative |

### 2.3 Primary users (indicative)

| User | Typical work |
|------|----------------|
| **Competent Authority** | Review matter dashboards, key dates, attendance/expense, template outputs |
| **Legal Cell officers** | Library, matters, tasks, collaboration, contacts, attendance, expenses, templates |
| **Empaneled / assigned advocates** | Same on web and Android: matters, tasks, communication, time, attendance, expense, documents |
| **Administrators** | Consume shared Person/Post provisioning; maintain legal keywords, templates, FAQ; Android enrolment against shared identity |
| **Operational units (authorised)** | Coordinated document sharing and meetings with Legal Cell under Limited / Community rules |

---

## 3. Project Objectives

1. Deliver a **dedicated Legal web application** (not a public portal) for court-matter work.
   - Case particulars, filings, hearing dates, court orders, compliance status and next action.

2. Consume **shared user management** from Claim Management Module 01.
   - Person, Post, Role-to-Post, Post-to-Person, official identity, OTP before activation, 2FA, no credential sharing, forensic/login audit — **refer to Claim Management SOW; do not rebuild**.
   - Add Legal-specific Limited / Community spaces, legal document rights, and Android authentication on that identity.

3. Provide a **coded legal digital library** with keyword hyperlinks and search.
   - Acts and Rules; research and legal opinions; Special Court and High Court orders; petitions; SOBs; written arguments.
   - Natural-language search, search-within-results, and Boolean terms and connectors.

4. Operate **matter management** with a single dashboard per matter.
   - Tasks, documents, communication, activities, team, contacts, hearings, time entry, key dates; reports by case, court, team member, CA, FE, key date and stage.

5. Operate **integrated task management** and **client–legal / team collaboration**.
   - Assign, due date, status, alerts, accept/reject, reassign, reminder, overdue, reprimand, completion report, team schedule.
   - Court proceedings / stay alerts / cause lists; queries; meetings; document sharing; Limited vs Community; email sync; individual and group messaging; calendar.

6. Maintain a **unified contact database** and **court attendance & expense** linked to the matter.

7. Provide **knowledge, SOP, templates, training and knowledge-retention** (including outgoing-member capture).

8. Deliver the **Android application for Advocates and Legal Cell** (contacts, matters, tasks, communication, time, dashboard, attendance, expense, documents).

9. Generate **statutory drafts from stored templates** (5(2) petition, notices as per rules, 7(1) / 8(1) reports, SOB, PWR, Caveat, IA, SLP, letters, freezing orders, warrants) in court-approved font and spacing, with human verification — no generative AI.

10. Deploy on the **designated server**, with HTTPS/SSL, AES-256, instant backup, clear Android licensing, and IP vested in SPLOCA.

---

## 4. In Scope / Out of Scope

### 4.1 In scope

| Area | Included |
|------|----------|
| **Channels** | Secure **staff web**; **Android** for Advocates and Legal Cell; anytime-anywhere official access via browser / Android |
| **Shared access (consumed)** | Claim Management SOW Module 01 (F01-001 to F01-007, F01-010): Person, Post, Role mapping, official identity, OTP, 2FA, joiner–mover–leaver, forensic/login audit. Legal users (Legal Cell, advocates) are Persons/Posts on that component |
| **Legal-specific access** | Hierarchy / need-to-know; Limited (named members) vs Community spaces; legal document view/download/share/edit; Android login against the same identity |
| **Library and search** | Acts/Rules, opinions, Special/High Court orders, petitions, SOBs, written arguments — coded and keyword-hyperlinked; NL search; Boolean connectors; highlight/hyperlink in results |
| **Matters, tasks, collaboration** | Matter create/classify/dashboard; task lifecycle; client–legal and team communication; email sync; authorised AV / group meetings between operational units and Legal Cell |
| **Contacts, attendance, expense** | Unified contacts; court attendance with cause list; category-wise expenses and bills linked to the matter |
| **Knowledge and training** | Manuals/SOP, forms, key judgements, OM/GO/guard file, training modules, FAQ, knowledge-leak prevention, rights management |
| **Templates** | 5(2), notices as per rules, 7(1), 8(1), SOB, PWR, Caveat, IA, SLP, letters, freezing orders, warrants — stored templates; human-verified fill |
| **Android** | Annexure-I §9 functions; Play Store / distribution licensing where approved |
| **Cross-cutting** | Common database with claims and other programme modules; central static/master data; per-module access, security, backup awareness, training/FAQ; designated server |
| **Document handling & workflow** | **Embedded** in legal processes (not a separate DMS product) |

### 4.2 Out of scope

| Area | Excluded |
|------|----------|
| **User management rebuild** | Re-specifying or re-building Person, Post, Role, 2FA, OTP-before-activation, official identity or credential lifecycle. **Use Claim Management SOW Module 01** |
| **Claim settlement** | Notification, intake, verification, approval, settlement, payment — Claim Management SOW |
| **GIS field valuation (eValueI / eValueM)** | Separate SOW |
| **FE Management dossier** | Already in the existing FE application; not rebuilt here |
| **Market intelligence and investigation process** | Excluded except issue of notices from form templates |
| **Generative AI** | Any generative AI for unsupervised legal drafting or advice |
| **Public portal rebuild** | Existing public website is not the target |
| **Hardware / hosting AMC** | Beyond designated-server deployment and runbooks, unless separately ordered |

### 4.3 Clarifying boundary — Shared user management

Legal Cell officers, empaneled advocates and other legal users **log in as Persons mapped to Posts** created in the shared component. An Administrator does **not** maintain a second user directory inside Legal Management.

This SOW estimates only:

- wiring Legal web and Android to that shared identity;  
- Limited vs Community legal spaces;  
- legal document rights;  
- Legal-specific Posts/Roles **configured on** the shared component (for example Legal Cell, Advocate), not a second identity product.

---

## 5. Solution Expectations (business-level)

1. **One identity:** Legal and Claims share Person–Post–Role; no second login directory.  
2. **Need-to-know:** Matter, document and communication visibility follows hierarchy and Limited / Community rules.  
3. **Coded library:** Opinions, orders, petitions, SOBs and arguments carry FE, CA, accused, advocates, judge, dates and Act/section keywords.  
4. **Matter is the hub:** Tasks, documents, messages, hearings, time and expenses hang off the matter.  
5. **Templates, not generative AI:** Drafts come from stored templates; an officer or advocate verifies before issue.  
6. **Android = official work:** Same identity and matter data as web, for Advocates and Legal Cell.  
7. **Common data:** Authorised users open linked claim/FE/matter information without re-keying, subject to RBAC.  
8. **IP and hosting:** Source and IP with SPLOCA; designated server; clear Android licensing.

---

## 6. Consolidated Functional Modules

Document handling and workflow are **embedded**. Module numbers and feature IDs are **authoritative** for downstream estimation.

---

### 01. Shared User & Access Control (consumed)

**Purpose:** Use the Person–Post–Role, official identity, OTP, 2FA, joiner–mover–leaver and forensic/login audit **already specified in the Claim Management SOW, Module 01 (F01-001 to F01-007 and F01-010)**. Add only Legal-specific spaces, document rights and Android authentication.

**Type:** Shared  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Claim Management SOW | Module 01 F01-001–F01-007, F01-010 (shared component — **do not rebuild**) |
| Legal Annexure-I | §§3(d) Limited/Community; 4(a) hierarchy and need-to-know; 9 Android; 10 Security |
| Proceedings 10-08-2026 | Items 1 (role-based web+Android), 18 (RBAC on common DB), 23 (per-module access) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Shared identity | Legal web and Android shall authenticate against the **same Person–Post–Role store** as Claim Management. Person create/update, Post, Role-to-Post, Post-to-Person, official identity, OTP before activation, 2FA and deactivation **shall not be re-implemented** here. |
| 2 | Legal Posts | Legal Cell and Advocate (and other legal Posts the Authority names) shall be configured **on the shared component**. |
| 3 | Limited / Community | The system shall support Limited spaces (explicit named members only) and Community spaces (all authorised users of that community) for legal collaboration and documents. |
| 4 | Legal document rights | View, download, share and edit of legal documents shall follow classification and Post rights. Sensitive legal documents shall not be freely redistributable. |
| 5 | Android session | Legal Android shall use the same identity; disabling a Person shall block new web and Android sessions. |

##### Entity fields — Legal access (additional to shared Person/Post)

| Field | Notes |
|-------|-------|
| Legal Post | Legal Cell / Advocate / other as configured on shared component |
| Space type | Limited / Community |
| Named members (Limited) | Persons explicitly added |
| Document rights | View / download / share / edit |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A Legal user logs in with the shared Person account; there is no second user master in Legal. |
| 2 | A user outside a Limited space cannot open that space or its documents. |
| 3 | Disabling the Person on the shared component blocks Legal web and Android immediately. |
| 4 | Claim Management F01-001–F01-007 and F01-010 are not duplicated as new Legal features except the Legal-specific items below. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Consume shared Person–Post–Role identity | An Administrator provisions Legal Cell officers and advocates **in the shared user-management component** (Claim Management SOW Module 01: F01-001 Person, F01-002 Post/Role mapping, F01-004 official identity, F01-005 OTP before activation, F01-006 2FA, F01-007 joiner–mover–leaver, F01-010 audit). The Legal Administrator does **not** create a parallel user directory. A Legal user then logs into Legal web with that Person. If the Person is deactivated on the shared component, Legal login fails. |
| F01-002 | Limited vs Community legal spaces | An authorised Legal Cell user creates a Limited space, adds named Persons, and shares a matter folder only with them. A Person not named cannot open that folder. For Community, the user publishes to all authorised Legal community members. Hierarchy / need-to-know from the shared RBAC still applies. |
| F01-003 | Legal document rights | An Advocate or Legal Cell user opens a petition, order or opinion and can view, download, share or edit only as their Post and the document classification allow. A user without download right can view but not download. The system records who viewed or downloaded which legal document and when. |
| F01-004 | Legal web and Android on shared identity | An Advocate or Legal Cell user signs in on web or Android with the same Person credentials and 2FA as the shared component. After login they see only Legal menus allowed for their Post. Signing out or deactivation ends both channels. |

---

### 02. Legal Masters, Keywords & Templates

**Purpose:** Maintain the keyword catalogues, Act/section coding and stored legal templates (court-approved font and spacing) that the library, matters and notice generation consume — including central static/master data for legal modules.

**Type:** Shared  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §1(g) Key Words Database |
| Proceedings 10-08-2026 | Items 7 (templates and central master/static/dynamic data), 8 (static/master data), 21 (draft letters, notices, freezing orders, warrants) |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Keywords | The system shall maintain catalogues: FE, CA, Accused, Advocates, Presiding Judge, Act, Rules and Sections, Legal Doctrines, and other coded keywords used in the library. |
| 2 | Act coding | Acts and Rules shall be coded so keywords can be hyperlinked in library documents. |
| 3 | Templates | Stored templates shall include 5(2) petition, notices as per rules, 7(1) report, 8(1) report, SOB, PWR, Caveat, IA, SLP, letters, freezing orders and warrants, in font and spacing approved by courts. |
| 4 | Draft generation | Authorised users shall generate drafts from those templates to Tahsildar, Banks, Claimants, Competent Authority or Government. Generative AI shall not compose the text. |
| 5 | Central masters | Master, static and dynamic reference data required by legal, matter, task, attendance/expense and collaboration shall be maintained centrally and consumed without duplicate local masters. |
| 6 | Link maintenance | Authorised users shall create and repair keyword links to library and matter documents. |

##### Entity fields — Template (minimum)

| Field | Notes |
|-------|-------|
| Template type | 5(2) / notice / 7(1) / 8(1) / SOB / PWR / Caveat / IA / SLP / letter / freezing order / warrant / other |
| Court font and spacing | As approved |
| Linked FE / CA / matter | Where the draft is matter-specific |
| Human verification status | Required before issue |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A library document can be hyperlinked to current keyword catalogue entries. |
| 2 | An officer can produce a 5(2) / notice / 7(1) / 8(1) / Caveat (and listed types) from a stored template without generative AI. |
| 3 | Changing a central keyword does not silently break existing document links; repair is available. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Keyword and entity catalogues | An Administrator or authorised Legal Cell user opens the keyword catalogue, adds or updates FE, CA, Accused, Advocate, Presiding Judge, Act/Rules/section or doctrine entries, and saves. Library and matter screens then offer those values for coding and search. |
| F02-002 | Act and Rules coding | The user codes an Act or Rule and sections so that a library document can hyperlink those codes. Another user opens the Act in the library and follows the keyword to the coded section. |
| F02-003 | Court-approved legal templates | An authorised user uploads or maintains a template (5(2), notice as per rules, 7(1), 8(1), SOB, PWR, Caveat, IA, SLP, letter, freezing order, warrant) with the court-approved font and spacing, and marks it available for drafting. |
| F02-004 | Generate draft from template | A Legal Cell user or Advocate opens a matter, selects a template type, fills the matter/FE/CA/addressee fields, generates the draft, reviews it on screen, and only then marks it ready to issue. There is no generative-AI compose action. |
| F02-005 | Central static and master data | An Administrator maintains static/master values used by matters, tasks, attendance and collaboration in one place. Matter and Android screens consume those values; a second local master is not created in those modules. |
| F02-006 | Keyword–document link maintenance | The user links a keyword to a library or matter document, or repairs a broken link after a catalogue change, then saves. Search and hyperlink navigation use the repaired link. |

---

### 03. Legal Knowledge Library & Search

**Purpose:** Store Acts/Rules, opinions, court orders, petitions, SOBs and written arguments — referenced and keyword-hyperlinked — with natural-language and Boolean search for daily Legal Cell work.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §§1–2 Legal Database and Search Facility |
| Proceedings 10-08-2026 | Item 7 — legal digital library |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Acts & Rules | Relevant Acts and Rules shall be coded and keywords hyperlinked. |
| 2 | Opinions | Research and Legal Opinions shall be referenced to FE, CA, Date and Cases/Petitions (Petitioner & OP), and coded/hyperlinked by Case Number, FE, CA, Date of Filing, Date of Order, Act & Section. |
| 3 | Court orders | Special Court Orders and High Court Orders shall use the full referencing scheme including Accused, Advocates and Presiding Judge. |
| 4 | Petitions / SOB / Written Arguments | All Petitions, SOBs and Written Arguments shall use the same referencing and coding scheme. |
| 5 | Search | Search box; natural-language search; Search Within Results; Boolean connectors (AND, OR, NOT, /p, /s, /pg, /d, quoted phrase, /#, !, parentheses). |
| 6 | Results | Keywords in results shall be highlighted and hyperlinked with document address. |

##### Entity fields — Library document (minimum)

| Field | Notes |
|-------|-------|
| Document type | Act/Rule / Opinion / Special Court order / High Court order / Petition / SOB / Written arguments |
| FE, CA | References |
| Case number; Petitioner & OP | As applicable |
| Accused, Advocates, Presiding Judge | As applicable |
| Date of filing / order | As applicable |
| Act & Section keywords | Hyperlinked |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An opinion or order can be retrieved by FE, case number, Act/section or other coded keyword. |
| 2 | Natural-language and Boolean searches return highlighted, hyperlinked hits. |
| 3 | Search Within Results narrows the current hit list. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Acts and Rules library | A Legal Cell user uploads or records an Act/Rule, applies coded keywords, and saves. Another user searches or follows a hyperlink and opens that Act/Rule without altering the stored original. |
| F03-002 | Research and legal opinions | The user files an opinion against FE, CA, date, case/petition (Petitioner and OP), and codes Case Number, FE, CA, filing/order dates, Act and section. Another user retrieves it by those fields or keywords. |
| F03-003 | Special Court and High Court orders | The user files an order with FE, CA, Accused, Advocates, Presiding Judge, date, case/petition and Act/section codes, then saves. A later search by judge, accused or case number opens that order. |
| F03-004 | Petitions, SOBs and written arguments | The user files a petition, SOB or written argument with the same referencing scheme as orders, scans/uploads the document, and saves. Team members with rights open the current version from the library or the matter. |
| F03-005 | Natural-language search and search-within-results | The user types a plain-language query (for example an elements-style question) in the search box, reviews hits, then enters further keywords to Search Within Results. Hits show highlighted terms and a link to the document. |
| F03-006 | Boolean terms and connectors | The user enters AND, OR, NOT, /p, /s, /pg, /d, a quoted phrase, /#, ! root expander or parentheses, runs search, and opens a hit. The system applies those connectors as specified in Annexure-I. |
| F03-007 | Highlight and hyperlink in results | In the result list the user sees matched keywords highlighted and hyperlinked to the document address, then clicks through to the passage. |

---

### 04. Matter Management

**Purpose:** Create and run each court matter as a single hub — classification, parties, documents and versions, tasks, key dates, consultations and reports.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §8 Matter Management |
| Proceedings 10-08-2026 | Item 6 — court matters, filings, hearings, orders, compliance, next action |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Create | The user shall create a matter: classify, description, FE, CA, Court, opponents, date. |
| 2 | Variables | Capture and edit court details, matter type, details, category and issues, opponent and lawyers. |
| 3 | Dashboard | Integrate tasks, documents, communication, activities, team members, client contacts, court hearings, time entry and key dates; searchable. |
| 4 | Documents | Scan/upload; create and edit with versions; share with controlled access. |
| 5 | Consult | Consult Client / External Expert / Research Expert / Other. |
| 6 | Key dates | Track key dates, deadlines and alerts; next action and compliance status. |
| 7 | Reports | Case wise, Court wise, Team Member wise, CA wise, FE wise, Key Date wise, Stage wise. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | Opening a matter shows tasks, documents, messages, hearings, team, contacts, time and key dates in one dashboard. |
| 2 | Document versions are retrievable; controlled share does not expose the file to non-members. |
| 3 | Listed report types can be produced from matter data by an authorised Post. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Create and classify matter | A Legal Cell user or Advocate selects Create Matter, enters classification, description, imported FE, CA, court, opponents and date, and saves. The matter appears in search and on that user’s dashboard. |
| F04-002 | Matter dashboard | The user opens the matter and sees in one place: tasks, documents, communication and messages, activities, team members, client contacts, court hearings, time entries and key dates, and can search within that matter. |
| F04-003 | Capture and edit matter variables | The user edits court details, matter type, details, category and issues, opponent and lawyers, and saves. The dashboard and reports use the updated values. |
| F04-004 | Matter documents, versions and controlled share | The user scans or uploads a document, or creates/edits text and saves a new version. The user shares the file only with Posts/Persons allowed. A person without access cannot open it. Previous versions remain available. |
| F04-005 | Consult client or expert | The user raises a consultation to Client, External Expert, Research Expert or Other on the matter, attaches context, and records the response against the matter. |
| F04-006 | Key dates, deadlines, compliance and next action | The user records a key date or deadline, sets an alert, and updates compliance status and next action. Assigned users receive the alert; overdue dates show on the dashboard. |
| F04-007 | Matter reports | An authorised user selects a report type (case, court, team member, CA, FE, key date or stage), sets filters, and generates the report from matter records. |

---

### 05. Tasks, Collaboration & Communication

**Purpose:** Assign and track legal and official tasks; enable client–legal and team communication (including Limited/Community sharing, email sync, and authorised coordination with operational units).

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §§3–4 Client–Legal collaboration; Legal Team Communication & Collaboration (task management) |
| Proceedings 10-08-2026 | Items 6–8 — task management; real-time collaboration; operational units and Legal Cell |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Task lifecycle | Assignment, due date, status, alerts, accept/reject, reassign, reminder, overdue, reprimand/warning, completion report with attachment, team member task schedule and status. |
| 2 | Advocate / Legal Cell reporting | Report court proceedings/directions, stay alerts, cause lists, time-critical responses, quick information, to-do lists. |
| 3 | Client actions | Raise queries, request tasks, schedule meetings. |
| 4 | Document sharing | Information / Response / Correction / Opinion / Drafting / Approval, with Limited or Community access. |
| 5 | Team communication | Sidebar relay; save records per matter; search by Person / Date / Case / Key Word; email sync; individual and group messaging; calendar; share files, bills, tasks and calendar with alert. |
| 6 | Cross-unit | Authorised real-time channels for group meetings, document sharing and audio-visual sharing between operational units and Legal Cell. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A task can be assigned, accepted or rejected, reassigned, completed with attachment, and shown on the team schedule. |
| 2 | Communication on a matter is searchable by person, date, case and keyword. |
| 3 | Limited-space shares are not visible to non-members. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Assign task with due date and status | An authorised user opens a matter (or the task inbox), assigns a task to a Person/Post, sets due date and initial status, and saves. The assignee sees it in the task inbox with an alert. |
| F05-002 | Accept, reject, reassign, reminder, overdue, reprimand | The assignee accepts or rejects the task. The assigner may reassign, send a reminder, view overdue items, or record a reprimand/warning. Each action is stored on the task with Person and timestamp. |
| F05-003 | Task completion report and team schedule | The assignee marks the task complete, attaches the completion report, and publishes. A supervisor opens the team member task schedule and status view for the period. |
| F05-004 | Court proceedings, stay alerts and cause lists | An Advocate or Legal Cell user records court proceedings or directions, a stay alert, cause list, time-critical response or to-do against the matter. Assigned members receive the alert and see it on the matter dashboard. |
| F05-005 | Queries, task requests and meetings | A client-side authorised user (or Legal Cell on their behalf) raises a query, requests a task, or schedules a meeting on the matter. Legal Cell responds or accepts the slot; the thread stays on the matter. |
| F05-006 | Limited/Community document sharing for legal work | The user shares a document for Information, Response, Correction, Opinion, Drafting or Approval, choosing Limited (named Persons) or Community. Only those members can open it. |
| F05-007 | Team messages saved and searchable per matter | The user sends a sidebar or matter message. The system saves it against the matter. Another user searches communications by Person, Date, Case or Key Word and opens the brief. |
| F05-008 | Email sync, messaging, calendar and file alerts | The user sends individual or group messages, syncs authorised email, uses the calendar for task overview, and shares files, bills, tasks or calendar with an alert to members. |
| F05-009 | Operational unit and Legal Cell coordination | An authorised operational-unit user and a Legal Cell user join an authorised group meeting or share documents / audio-visual as permitted. Unauthorised users cannot join. Need-to-know still applies. |

---

### 06. Unified Contact Database

**Purpose:** One classified contact directory for SPLOCA and related offices, advocates, accused, petitioners, visitors, experts and field officers, with search and SMS/email/team hand-off.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §5 Unified Contact Database |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Office contacts | SPLOCA Office, RC Office, CA, RD, District Fraud Prevention Cell, IOs, Legal Team. |
| 2 | Categorised contacts | Advocates, Accused, Petitioners, Visitors, External Experts, Tahsildar, AC, Sub Registrar; custom categories. |
| 3 | Unify and update | Convert multiple lists into one address book; update existing contacts. |
| 4 | Search | Free-text search. |
| 5 | Use | Send number to SMS / Email / Team for contacting. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | A contact can be found by free text and opened with category and details. |
| 2 | The user can pass the number/email to SMS, email or team from the contact record. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Office and agency contacts | An authorised user adds or updates a contact for SPLOCA, RC Office, CA, RD, DFPC, IO or Legal Team, sets category, and saves. Another user searches and opens that contact. |
| F06-002 | Categorised external contacts | The user adds an Advocate, Accused, Petitioner, Visitor, External Expert, Tahsildar, AC or Sub Registrar (or a custom category), fills details, and saves. |
| F06-003 | Unify lists and update existing | The user imports or merges another business contact list into the unified directory, or opens an existing contact and adds details, then saves without creating a duplicate where a match is confirmed. |
| F06-004 | Free-text contact search | The user types a name, office, category or fragment; the system shows matches; the user opens the contact. |
| F06-005 | Send to SMS, email or team | From the contact, the user chooses SMS, email or team, and sends the number or address for contacting. The action is recorded against the contact or matter where linked. |

---

### 07. Court Attendance & Expense Management

**Purpose:** Record court attendance (with cause list) and category-wise authorised expenses linked to the matter, and submit bills.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §6 Court Attendance & Expense Management |
| Proceedings 10-08-2026 | Item 7 — attendance, authorised expenses, linkage to court matter |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Attendance | Submit Name/Code, Date, Court, Location, Entry Time, Presiding Judge, Matter, Brief on Proceedings, Effective/Ineffective, Exit Time, upload with Cause List. |
| 2 | Expenses | Category-wise: Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage, Specified Other, with document/voucher. |
| 3 | Search | Quick search and retrieval. |
| 4 | Bill | Submit expense bill. |
| 5 | Link | Attendance and authorised expenses shall link to the concerned court matter. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An attendance row is retrievable by date, court, matter or person and shows cause-list upload. |
| 2 | An expense bill is linked to the matter and shows vouchers. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Submit court attendance | An Advocate or Legal Cell user opens Attendance, selects the matter, enters name/code, date, court, location, entry/exit time, judge, brief on proceedings, Effective/Ineffective, uploads the cause list, and submits. The row appears on the matter dashboard. |
| F07-002 | Capture category-wise expenses | The user records Task, Assigned By, Travel, Boarding, Lodging, Local Travel, Court Expenses, Clerkage or Specified Other against the matter, attaches voucher/document, and saves. |
| F07-003 | Search attendance and expense | The user searches by date, court, matter, person or category and opens the matching attendance or expense record. |
| F07-004 | Submit expense bill | The user compiles authorised expenses for the period, submits the expense bill, and the bill remains linked to the matter for CA or supervisor review. |
| F07-005 | Link attendance and expense to matter | When saving attendance or expense, the user must select the court matter. Opening the matter shows those attendance and expense rows; they are not stored as unlinked personal notes. |

---

### 08. Knowledge, SOP, Training & Retention

**Purpose:** Manuals, SOP, forms, key judgements, OM/GO/guard files, training (research, writing, Word, Excel), FAQ, outgoing-member knowledge capture, and rights-managed sharing.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §7 Knowledge, Expertise, Tools & Training |
| Proceedings 10-08-2026 | Item 23 — training and FAQ per module |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | SOP library | Manuals, Guidelines and SOP with keywords hyperlinked. |
| 2 | Forms | Forms and format templates. |
| 3 | Judgements / OM / GO | Key judgement database; OM, GO and Guard File database. |
| 4 | Training | Legal Research, Legal Writing, MS Word, MS Excel; in-app FAQ. |
| 5 | Retention | Systemized aggregation of an outgoing member’s proprietary knowledge; docket with title, word search, date of creation and author; controlled file sharing. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | SOP and OM/GO can be found by title or keyword. |
| 2 | An outgoing member’s captured knowledge remains searchable after deactivation of their login. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Manuals, guidelines and SOP | An authorised user uploads a manual, guideline or SOP, applies keywords, and saves. Another user searches by keyword or title and opens the document. |
| F08-002 | Forms and format templates | The user adds a form or format template to the knowledge base. A Legal Cell user opens it from the matter or knowledge menu and uses it for drafting (separate from statutory templates in Module 02 where those are court forms). |
| F08-003 | Key judgement database | The user files a key judgement with title, date, author/court and keywords. Another user searches and opens it. |
| F08-004 | OM, GO and guard-file database | The user files an OM, GO or guard-file item with docket title, date and author. Another user locates it by title or word search. |
| F08-005 | Training modules and FAQ | An Administrator publishes training content for Legal Research, Legal Writing, MS Word or MS Excel, and FAQ for the legal modules. A user opens the module or FAQ from the application. Classroom delivery is out of scope unless separately ordered. |
| F08-006 | Outgoing-member knowledge capture and rights | Before or when a member leaves, an authorised user captures that member’s designated knowledge assets into the repository (title, author, date). After the Person is deactivated on the shared component, those documents remain searchable. Sensitive items stay under controlled sharing. |

---

### 09. Legal Android Application (Advocates & Legal Cell)

**Purpose:** Official Android channel for the same identity and matter data — contacts, matters, tasks, communication, time, dashboard, attendance, expense and documents.

**Type:** Business  

#### Source coverage

| Source document | Coverage |
|-----------------|----------|
| Legal Annexure-I | §9 Mobile Application for Advocates & Legal Cell |
| Proceedings 10-08-2026 | Items 1, 6, 19 — Android for official work; Play Store licensing where approved |

#### Functional requirements

| # | Area | Requirement |
|---|------|-------------|
| 1 | Contacts / matters | Add Contact; Add Matter. |
| 2 | Tasks | Create, assign, accept/reject, reassign, mark completed, inbox, overdue, outbox. |
| 3 | Communication | Send communication; internal messaging. |
| 4 | Time | Make time entry. |
| 5 | Dashboard | View matter dashboard: tasks, communication, documents, hearings, team, client contact. |
| 6 | Attendance / expense | Record attendance and expense. |
| 7 | Documents | View, download, create folder, upload, view shared documents. |
| 8 | Distribution | Secure Android distribution; Play Store licensing where specifically approved; licensing clear. |

#### Acceptance criteria

| # | Criterion |
|---|-----------|
| 1 | An Advocate completes task accept/complete, attendance and a document upload on Android against the same matter as web. |
| 2 | The same Person credentials and 2FA (as configured on the shared component) govern Android. |
| 3 | Licensing/distribution approach is documented and not left speculative. |

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Add contact and matter on Android | An Advocate or Legal Cell user opens the Android app, adds a contact or a matter (with required fields including FE/CA/court as on web), and saves. The record appears on web for authorised Posts. |
| F09-002 | Android task inbox and lifecycle | The user opens Task inbox, creates or is assigned a task, accepts or rejects, reassigns, marks completed, views overdue and outbox. Status matches the web task on the same matter. |
| F09-003 | Android communication and messaging | The user sends a matter communication or internal message from the phone. Recipients see it on web and Android; it is stored on the matter. |
| F09-004 | Time entry on Android | The user records a time entry against the matter (date, duration, activity) and saves. The matter dashboard shows the entry. |
| F09-005 | Matter dashboard on device | The user opens a matter and sees tasks, communication, documents, court hearings, team members and client contact in one place, then drills into an item. |
| F09-006 | Attendance and expense on Android | The user submits court attendance or an expense line with voucher photo/upload from the device, linked to the matter, as on web. |
| F09-007 | Android documents | The user views or downloads a document, creates a folder, uploads a file, or opens a shared document, subject to the same rights as web. |
| F09-008 | Android distribution and licensing | The delivery includes a clear, non-speculative distribution method (including Play Store licensing where SPLOCA specifically approves). IP remains with SPLOCA. |

---

## 7. End-to-End Workflows

### 7.1 Identity (shared — not rebuilt)

```text
Administrator provisions Person + Post + Role on shared component (Claim Management Module 01)
        → OTP before activation; 2FA
        → Legal Cell / Advocate logs into Legal web or Android with that Person
        → Limited / Community and legal document rights apply
```

### 7.2 Matter lifecycle

```text
Create matter (FE, CA, court, parties)
        → File / link library documents (petition, SOB, orders)
        → Assign tasks; collaborate; hearings and key dates
        → Attendance and expenses against the matter
        → Template drafts (notices, 5(2), 7(1)/8(1), Caveat, etc.) with human verify
        → Compliance and next action on dashboard
        → Reports (case / court / team / CA / FE / stage)
```

---

## 8. Access Control / RBAC

**User management is the shared component in the Claim Management SOW, Module 01.** This application does not define a second Person master.

| Element | Where specified |
|---------|-----------------|
| Person, Post, Role-to-Post, Post-to-Person, mapping history | Claim Management SOW F01-001, F01-002 |
| Official identity, OTP before activation, 2FA, joiner–mover–leaver | Claim Management SOW F01-004 to F01-007 |
| Forensic and login audit | Claim Management SOW F01-010 |
| Legal Limited vs Community spaces | This SOW F01-002 |
| Legal document rights | This SOW F01-003 |
| Legal web and Android on that identity | This SOW F01-004 |

Legal Posts (Legal Cell, Advocate, and others named by SPLOCA) are **configured on** the shared component.

---

## 9. Channels

| Channel | Who | Use |
|---------|-----|-----|
| **Staff web** | Legal Cell, CA, Administrators, authorised operational users | Full Legal Management |
| **Android** | Advocates and Legal Cell | Annexure-I §9 functions |
| **Email (sync)** | Legal team | Authorised mail sync for matter communication |
| **SMS** | From contacts | Hand-off of numbers for contacting |
| **Public website** | — | **Not** the Legal application |

---

## 10. Integrations

| Integration | Purpose |
|-------------|---------|
| **Shared user-management component** | Claim Management Module 01 identity for all Legal web and Android users |
| **Common database with Claim Management** | Authorised linked FE/matter/claim access without duplicate entry, subject to RBAC |
| **Existing FE application (via programme references)** | FE/CA names as keywords and matter fields; no FE dossier rebuild |
| **Email services** | Sync as specified in Annexure-I |
| **SMS** | Send contact numbers |
| **Document software** | Working copies as interfaces allow |
| **Play Store / Android distribution** | Where specifically approved |

---

## 11. Audit, Compliance & Security

1. Privileged legal actions (share, download, task complete, template issue) are attributable to the shared Person.  
2. Instant backup and server storage in case of hardware failure.  
3. HTTPS/SSL and AES-256 for data transmission and encryption.  
4. No generative AI.  
5. Market intelligence / investigation process excluded except template notices.  
6. IP and source code solely with SPLOCA.  
7. Login/2FA audit remains on the shared component (Claim Management F01-010).

---

## 12. Non-Functional Requirements

| Area | Expectation |
|------|-------------|
| **Security** | HTTPS/SSL; AES-256; shared 2FA |
| **Backup** | Instant backup to server |
| **Availability** | Suitable for court-day Legal Cell and advocate field use (SLA to be agreed) |
| **Search** | Library Boolean/NL; matter and communication search |
| **Interoperability** | Shared identity; common DB with claims; email sync |
| **Android** | Official work; clear licensing |
| **AI** | Agentic / rule-based only; human verify |
| **Operability** | Per-module access, security awareness, backup participation, training/FAQ |

This SOW does not size infrastructure beyond the designated-server requirement.

---

## 13. Data Migration

**In scope** as structured load the Authority releases: Acts/Rules, opinions, orders, petitions/SOBs/written arguments, contacts, matters, templates, as available.

**Out of scope unless separately ordered:** scanning bureau; reconstruction of missing physical files; claim or GIS-valuation migration (those SOWs).

---

## 14. Phased Delivery

| Phase | Focus | Modules (primary) |
|-------|--------|-------------------|
| **P1 — Identity and masters** | Consume shared access; keywords, templates, central masters | 01, 02 |
| **P2 — Library and search** | Acts, opinions, orders, petitions, SOB, arguments, search | 03 |
| **P3 — Matters and work** | Matters, tasks, collaboration, contacts, attendance/expense | 04, 05, 06, 07 |
| **P4 — Knowledge** | SOP, OM/GO, training, retention | 08 |
| **P5 — Android** | Advocate / Legal Cell app and distribution | 09 |

P1 is a prerequisite. Exact go-live grouping is a commercial / Authority decision after estimation.

---

## 15. Deliverables

| Deliverable | Description |
|-------------|-------------|
| Legal staff web application | Modules 01–08 as specified |
| Legal Android application | Module 09 |
| Consumption of shared user management | Claim Management Module 01 — not a second IAM product |
| Template pack | Types listed in Module 02 |
| Documentation | Role guide, Android guide, template/issue guide, interface notes |
| Training/FAQ hooks | In-application; classroom optional |

---

## 16. Acceptance Criteria (programme level)

1. Legal users log in only via the shared Person–Post–Role component; there is no second user master.  
2. Limited spaces are closed to non-members.  
3. Library documents are coded and retrievable by NL and Boolean search.  
4. A matter dashboard shows tasks, documents, communication, hearings, team, contacts, time and key dates.  
5. Tasks can be assigned, accepted/rejected, reassigned and completed with attachment.  
6. Attendance and expenses link to the matter.  
7. A statutory draft can be generated from a stored template and issued only after human verification; no generative AI.  
8. Android supports the Annexure-I §9 actions on the same matter and identity as web.  
9. Market-intelligence investigation screens are absent.  
10. IP of delivered software lies with SPLOCA.

---

## 17. Expected Benefits

- Single official Legal workbench for library, matters, tasks and court days  
- One identity with Claims (no duplicate logins)  
- Court-ready templates without unsupervised generative drafting  
- Advocate mobility on Android with the same matter file  
- Searchable institutional memory (including after staff leave)  

---

## 18. Assumptions & Dependencies

### 18.1 Assumptions

1. Project code is LEGAL; display name is **Legal Management Application (KPID / SPLOCA)**.  
2. Purpose is RFP discussion and internal estimation.  
3. **User management is the shared Claim Management Module 01**; this SOW does not re-estimate that full identity product.  
4. Document management and workflow are embedded.  
5. FE identity used in legal keywords/matters comes from the existing FE application / Claim import, not a new FE dossier.  
6. GIS valuation and Claim settlement remain separate SOWs.  
7. Android / Play Store licensing is used only where SPLOCA specifically approves.  
8. Generative AI is prohibited.  
9. Hosting is the designated server; this SOW does not size hardware.  
10. SOB means Statement of Objections unless SPLOCA names a different docket label.

### 18.2 Dependencies

1. Shared user-management component (Claim Management Module 01) available to Legal web and Android.  
2. Access to designated server and approved Android distribution path.  
3. Supply of library corpora, templates and contact lists by SPLOCA.  
4. Court-approved font/spacing for templates.  
5. Common-database linkage rules with Claim Management (RBAC).  
6. Confirmation of Legal Posts (Legal Cell, Advocate, others).

---

## 19. Vendor Response Expectations

1. Confirm **consumption of Claim Management Module 01** for identity; do not propose a second user directory.  
2. Map the solution to **modules 01–09 and feature IDs F{NN}-{SEQ}** without renumbering.  
3. Describe Android distribution and licensing in clear, non-speculative terms.  
4. Exclude generative AI; describe any agentic assist with human verify.  
5. Do not include Claim settlement or eValueI/eValueM scope in the response to this SOW.  
6. Identify assumptions that differ from §18.  
7. Do not include effort hours in a rewritten SOW.

---

## 20. Appendices

### Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Shared User & Access Control (consumed) | Shared | F01-001 … F01-004 (4) |
| 02 | Legal Masters, Keywords & Templates | Shared | F02-001 … F02-006 (6) |
| 03 | Legal Knowledge Library & Search | Business | F03-001 … F03-007 (7) |
| 04 | Matter Management | Business | F04-001 … F04-007 (7) |
| 05 | Tasks, Collaboration & Communication | Business | F05-001 … F05-009 (9) |
| 06 | Unified Contact Database | Business | F06-001 … F06-005 (5) |
| 07 | Court Attendance & Expense Management | Business | F07-001 … F07-005 (5) |
| 08 | Knowledge, SOP, Training & Retention | Business | F08-001 … F08-006 (6) |
| 09 | Legal Android Application (Advocates & Legal Cell) | Business | F09-001 … F09-008 (8) |

**Total modules:** 9  
**Total feature outlines:** 57  

Module 01 F01-001 **consumes** Claim Management F01-001–F01-007 and F01-010; it is not a second identity build.

### Appendix B — Source consolidation map

| Source | This SOW |
|--------|----------|
| Claim Management SOW Module 01 (user management) | Module 01 — consumed shared component |
| Annexure-I §1–2 Library and Search | Module 03; keywords in Module 02 |
| Annexure-I §3 Client–Legal collaboration | Module 05 |
| Annexure-I §4 Team communication and tasks | Module 05 |
| Annexure-I §5 Contacts | Module 06 |
| Annexure-I §6 Attendance and expense | Module 07 |
| Annexure-I §7 Knowledge and training | Module 08 |
| Annexure-I §8 Matter management | Module 04 |
| Annexure-I §9 Android | Module 09 |
| Annexure-I §10 Security | §11–12; shared 2FA from Claim Module 01 |
| Proceedings item 1 | Dedicated role-based web + Android; not public portal |
| Proceedings items 6–8 | Matters, tasks, attendance/expense, library, templates, collaboration |
| Proceedings item 15 | Market intelligence excluded except template notices |
| Proceedings item 16 | No generative AI |
| Proceedings item 18 | Common DB with claims |
| Proceedings item 19 | Designated server; Android licensing; IP with SPLOCA |
| Proceedings item 21 | Template letters, notices, freezing orders, warrants — Module 02 |
| Proceedings item 23 | Per-module access, backup, training, FAQ |
| Proceedings items 2–5, 9–14, 17, 22 | Claim / valuation / FE coding — **not this SOW** |

### Appendix C — Key entities

| Entity | Meaning |
|--------|---------|
| **Shared user component** | Claim Management SOW Module 01 Person–Post–Role |
| **Matter** | A court case / legal file hub |
| **Limited space** | Named members only |
| **Community space** | All authorised users of that legal community |
| **FE / CA** | References on matters and library documents |

### Appendix D — Abbreviations

As in Annexure-I (SPLOCA, KPIDFE, FE, CA, RC, RD, IO, AC, OP, SOB, OM, GO, SOP, DFPC). SOB is treated as Statement of Objections unless SPLOCA directs otherwise.

---

**End of Statement of Work — Legal Management Application (KPID / SPLOCA)**
