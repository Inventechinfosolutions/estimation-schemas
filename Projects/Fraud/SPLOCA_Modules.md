# SPLOCA Legal Management Application — Module List

Source: `SoW_SPLOCA_Detailed.md` (v1.2)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Access Control & Need-To-Know Security | Shared | Users, roles, post/position, hierarchy NTK, Limited/Community, document rights, web/Android auth | Explicit in SOW |
| 02 | Keyword & Reference Masters | Shared | FE/CA/Accused/Advocates/Judge/Act/Doctrine masters and keyword–document links | Explicit in SOW |
| 03 | Legal Database | Business | Acts/Rules, opinions, orders, petitions, SOB, written arguments, hyperlinks, corpus migration | Explicit in SOW |
| 04 | Search Facility | Business | Corpus indexing, natural language, search-within-results, Boolean/connectors, highlighted results | Explicit in SOW |
| 05 | Unified Contact Database | Business | Office and categorised contacts, search, SMS/email/team actions, contact migration | Explicit in SOW |
| 06 | Matter Management | Business | Matter lifecycle, dashboard, reports, documents, consultations, tasks/key dates, time entry, migration | Explicit in SOW |
| 07 | Client – Legal Section Collaboration | Business | Advocate reporting pack, queries/tasks/meetings, document share, Limited/Community spaces | Explicit in SOW |
| 08 | Legal Team Communication & Task Management | Business | Task lifecycle, sidebar/comms, email sync, messaging, calendar, share-with-alert | Explicit in SOW |
| 09 | Court Attendance & Expense Management | Business | Attendance, category expenses, search, expense bill submission | Explicit in SOW |
| 10 | Knowledge, Expertise, Tools & Training | Business | SOPs/templates/judgements/OM-GO, training content, searchable knowledge, leak prevention, rights | Explicit in SOW |
| 11 | Mobile Application (Android) for Advocates & Legal Cell | Business | Android contact/matter/task/comms/time/dashboard/attendance/docs | Explicit in SOW |
| 12 | Platform Security, Backup & Encryption | Technical | Instant backup, HTTPS/SSL, AES-256 | Explicit in SOW |

---

## Module Details

### 01. Access Control & Need-To-Know Security

- **Type:** Shared
- **Slug:** `access-control-need-to-know-security`
- **Summary:** Establish identity via users, roles, and post/position so hierarchy, need-to-know, Limited/Community, and document rights apply on web and Android.
- **Source:** Explicit in SOW §6 Module 01; access model confirmed as role + post/position.
- **In Scope:** User CRUD/deactivate; role permission sets; post/position catalogue and posting; hierarchy NTK visibility; Limited vs Community; document rights (View/Download/Comment/Edit/Approve); web & Android authentication and session handling.
- **Out of Scope:** Citizen identity; SSO/AD (unless later change); separate org-hierarchy product module.
- **Key Actors:** Administrator, Legal Cell Officer, Advocate, Reviewer, other authorised staff.
- **Dependencies:** None (foundational).
- **Notes:** Features F01-001 … F01-005.

### 02. Keyword & Reference Masters

- **Type:** Shared
- **Slug:** `keyword-reference-masters`
- **Summary:** Maintain keyword/entity and Act/Rules coding catalogues and keyword–document links for the legal and knowledge corpus.
- **Source:** Explicit in SOW §6 Module 02 (from Annexure Key Words Database).
- **In Scope:** FE, CA, Accused, Advocates, Presiding Judge, Act, Rules & Sections, Legal Doctrines; Act→Rules→Sections catalogue; bidirectional keyword–document links; admin governance.
- **Out of Scope:** Full-text search engine (Module 04); register content itself (Module 03).
- **Key Actors:** Administrator, Legal Cell content managers.
- **Dependencies:** 01 Access Control.
- **Notes:** Features F02-001 … F02-003.

### 03. Legal Database

- **Type:** Business
- **Slug:** `legal-database`
- **Summary:** Registers for Acts/Rules, opinions, Special/High Court orders, petitions, SOB, written arguments with coding, hyperlink navigation, and corpus migration.
- **Source:** Explicit in SOW §6 Module 03.
- **In Scope:** Six register types + Acts/Rules; common CRUD/archive/attachments; keyword hyperlink navigation; migration of Acts/Rules, opinions, orders (F03-008).
- **Out of Scope:** Migration of petitions/SOB/written arguments (not in confirmed migration scope); standalone DMS.
- **Key Actors:** Legal Cell, Advocates, Administrators.
- **Dependencies:** 01 Access; 02 Keyword Masters.
- **Notes:** Features F03-001 … F03-008.

### 04. Search Facility

- **Type:** Business
- **Slug:** `search-facility`
- **Summary:** Search box and corpus indexing with natural language, search-within-results, Boolean/connectors, and highlighted hyperlinked results.
- **Source:** Explicit in SOW §6 Module 04.
- **In Scope:** Indexing of legal/knowledge/matter corpus; NL search; within-results; AND/OR/NOT, /p /s /pg /d, phrases, /#, !, (); highlight + document address links; access-filtered results.
- **Out of Scope:** Separate search product; citizen search portal.
- **Key Actors:** All authorised staff users.
- **Dependencies:** 01 Access; 02/03/06/10 content sources.
- **Notes:** Features F04-001 … F04-005.

### 05. Unified Contact Database

- **Type:** Business
- **Slug:** `unified-contact-database`
- **Summary:** Unified address book for office and categorised contacts with search, SMS/email/team actions, and contact migration.
- **Source:** Explicit in SOW §6 Module 05.
- **In Scope:** SPLOCA/RC/CA/RD/DFPC/IO/Legal Team; Advocates/Accused/Petitioners/Visitors/Experts/Key Officials; custom categories; free-text search; SMS/Email/Team actions; F05-006 migration.
- **Out of Scope:** Marketing CRM; payment contacts.
- **Key Actors:** Legal Cell, Advocates, Administrators.
- **Dependencies:** 01 Access; SMS/email integrations.
- **Notes:** Features F05-001 … F05-006.

### 06. Matter Management

- **Type:** Business
- **Slug:** `matter-management`
- **Summary:** Matter create/classify, variables, dashboard, search, reports, documents/versions, consultations, tasks/key dates, web time entry, matter migration.
- **Source:** Explicit in SOW §6 Module 06.
- **In Scope:** Full matter lifecycle; embedded documents; reports (case/court/team/CA/FE/key date/stage); F06-010 time entry; F06-009 migration.
- **Out of Scope:** Standalone DMS/BPM; citizen matter portal.
- **Key Actors:** Legal Cell, Advocates, Administrators.
- **Dependencies:** 01 Access; 02 Keywords; 05 Contacts; 08 Tasks (coordination).
- **Notes:** Features F06-001 … F06-010.

### 07. Client – Legal Section Collaboration

- **Type:** Business
- **Slug:** `client-legal-section-collaboration`
- **Summary:** Advocate court reporting pack, client queries/tasks/meetings, purpose-tagged document sharing, Limited/Community spaces.
- **Source:** Explicit in SOW §6 Module 07.
- **In Scope:** Proceedings, stay alerts, cause lists, time-critical, quick info, to-dos; queries/tasks/meetings; share purposes including Approval; Limited/Community.
- **Out of Scope:** Citizen/client public portal (“client” = legal section / internal requesting side).
- **Key Actors:** Advocates, Legal Section staff.
- **Dependencies:** 01 Access; 06 Matter; 08 Tasks (where task requests route).
- **Notes:** Features F07-001 … F07-004.

### 08. Legal Team Communication & Task Management

- **Type:** Business
- **Slug:** `legal-team-communication-task-management`
- **Summary:** Team task lifecycle, sidebar communication, matter-linked comms search, email sync, messaging, calendar, share-with-alert.
- **Source:** Explicit in SOW §6 Module 08.
- **In Scope:** Assign/due/status/accept-reject/reassign/alerts/reminders/overdue/reprimand; completion & schedule publish; sidebar; matter comms search; email sync; individual/group messaging; calendar; share files/bills/tasks/calendar with alert.
- **Out of Scope:** External public messaging; separate BPM engine.
- **Key Actors:** Legal Cell, Advocates, Supervisors.
- **Dependencies:** 01 Access; 06 Matter; email service.
- **Notes:** Features F08-001 … F08-009.

### 09. Court Attendance & Expense Management

- **Type:** Business
- **Slug:** `court-attendance-expense-management`
- **Summary:** Court attendance capture, category-wise expenses with vouchers, search, expense bill submission.
- **Source:** Explicit in SOW §6 Module 09.
- **In Scope:** Full attendance field set including Cause List; expense categories; search; bill submit draft vs submitted.
- **Out of Scope:** Payroll; payment gateway reimbursement.
- **Key Actors:** Advocates, Legal Cell, Supervisors.
- **Dependencies:** 01 Access; 06 Matter.
- **Notes:** Features F09-001 … F09-004.

### 10. Knowledge, Expertise, Tools & Training

- **Type:** Business
- **Slug:** `knowledge-expertise-tools-training`
- **Summary:** Manuals/SOPs, forms, judgements, OM/GO/guard files, training content, searchable repository, leak prevention, rights.
- **Source:** Explicit in SOW §6 Module 10.
- **In Scope:** Libraries listed; training modules Legal Research/Writing/MS Word/MS Excel as content; docketing; knowledge-leak offboarding capture; rights via Module 01.
- **Out of Scope:** Instructor-led training delivery; LMS vendor product.
- **Key Actors:** Legal Cell, Knowledge owners, Trainees.
- **Dependencies:** 01 Access; 02 Keywords.
- **Notes:** Features F10-001 … F10-008.

### 11. Mobile Application (Android) for Advocates & Legal Cell

- **Type:** Business
- **Slug:** `mobile-application-android-advocates-legal-cell`
- **Summary:** Android app for contact/matter add, tasks, communication, time entry, matter dashboard, attendance/expense, documents.
- **Source:** Explicit in SOW §6 Module 11.
- **In Scope:** Android capabilities F11-001 … F11-007 with same access rules as web; sync parity.
- **Out of Scope:** iOS; citizen app; offline-first unless agreed in design without expanding scope.
- **Key Actors:** Advocates, Legal Cell.
- **Dependencies:** 01 Access; 05–09 backend capabilities.
- **Notes:** Features F11-001 … F11-007.

### 12. Platform Security, Backup & Encryption

- **Type:** Technical
- **Slug:** `platform-security-backup-encryption`
- **Summary:** Instant/scheduled backup to server storage, HTTPS/SSL transport, AES-256 encryption.
- **Source:** Explicit in SOW §6 Module 12.
- **In Scope:** Backup trigger/status/alerts and UAT restore demo; HTTPS enforcement; AES-256 for agreed sensitive data; key handling without embedding keys in mobile.
- **Out of Scope:** Hardware; hosting/AMC; certificate procurement (SPLOCA/hosting).
- **Key Actors:** Administrator, SPLOCA IT.
- **Dependencies:** Hosting provided by SPLOCA.
- **Notes:** Features F12-001 … F12-003.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Document Management | Embedded in Matter, Collaboration, Knowledge, Attendance vouchers |
| Workflow / tasking engine | Embedded in Modules 06, 07, 08 (no standalone BPM) |
| Notifications (SMS/email/in-app alerts) | Embedded in Contacts, Tasks, Collaboration, Security backup alerts; no separate Notification Service module (integrations remain SMS + email sync) |
| Audit logging | NFR / Access — embedded across modules |
| Reporting engine | Matter reports inside Module 06; not a separate MIS product |
| Citizen portal | Out of scope |
| Hardware, scanning bureau, training delivery, hosting/AMC | Out of scope per SOW |

---

## Assumptions

1. SOW v1.2 is the scope source of truth; feature IDs F01-001 … F12-003 (72 features including F06-010) are preserved.
2. Access model is role + post/position only (no citizen identity).
3. “Client” in collaboration means authorised legal-section users.
4. Migration limited to Acts/Rules, opinions, orders, contacts, matters.
5. Single-phase delivery; modules ordered for implementation dependency.

---

## Risks

1. Boolean/connector search (/p /s /pg /d, root expander) may be higher complexity than typical enterprise search — watch F04-004 estimates.
2. Email sync (F08-008) depends on SPLOCA mailbox/provider readiness.
3. Migration data quality for legal corpus and matters may extend F03-008 / F06-009 effort without changing feature IDs.
4. Android parity with web access rules (Module 11) can surface defects late if access rules change after mobile build starts.
