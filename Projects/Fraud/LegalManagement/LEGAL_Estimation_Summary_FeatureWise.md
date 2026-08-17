# LEGAL — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 2,769 hours · **Go-live:** 2,769 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Shared User & Access Control (consumed) | Shared | 4 | 200 | 7.2% |
| 02 | Legal Masters, Keywords & Templates | Shared | 6 | 269 | 9.7% |
| 03 | Legal Knowledge Library & Search | Business | 7 | 375 | 13.5% |
| 04 | Matter Management | Business | 7 | 357 | 12.9% |
| 05 | Tasks, Collaboration & Communication | Business | 9 | 473 | 17.1% |
| 06 | Unified Contact Database | Business | 5 | 210 | 7.6% |
| 07 | Court Attendance & Expense Management | Business | 5 | 182 | 6.6% |
| 08 | Knowledge, SOP, Training & Retention | Business | 6 | 234 | 8.5% |
| 09 | Legal Android Application (Advocates & Legal Cell) | Business | 8 | 469 | 16.9% |
| | **Total** | | **57** | **2,769** | **100%** |

## 01 — Shared User & Access Control (consumed) (200 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Consume shared Person–Post–Role identity | 52 | Wiring to Claim Module 01; no second Person master |
| F01-002 | Limited vs Community legal spaces | 45 | Named Limited members vs Community publish; need-to-know still applies |
| F01-003 | Legal document rights | 42 | View/download/share/edit by Post and classification; access log |
| F01-004 | Legal web and Android on shared identity | 61 | Same Person/2FA on web and Android; deactivation ends both |

## 02 — Legal Masters, Keywords & Templates (269 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Keyword and entity catalogues | 46 | FE/CA/Accused/Advocate/Judge/Act/doctrine catalogues for coding |
| F02-002 | Act and Rules coding | 42 | Code Acts/Rules/sections for library hyperlinks |
| F02-003 | Court-approved legal templates | 49 | Stored 5(2)/notice/7(1)/8(1)/SOB/PWR/Caveat/IA/SLP/letter/freezing/warrant |
| F02-004 | Generate draft from template | 72 | Human-verified merge from stored templates; no generative AI |
| F02-005 | Central static and master data | 30 | One central master; matter/Android consume, do not fork |
| F02-006 | Keyword–document link maintenance | 30 | Create/repair keyword links after catalogue change |

## 03 — Legal Knowledge Library & Search (375 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Acts and Rules library | 40 | Upload/code Acts/Rules; originals unchanged on open |
| F03-002 | Research and legal opinions | 42 | File opinions with FE/CA/case/Act coding |
| F03-003 | Special Court and High Court orders | 43 | File orders with accused/advocates/judge coding |
| F03-004 | Petitions, SOBs and written arguments | 42 | Same referencing as orders; versioned petitions/SOB/arguments |
| F03-005 | Natural-language search and search-within-results | 82 | Plain-language query plus Search Within Results |
| F03-006 | Boolean terms and connectors | 88 | AND OR NOT /p /s /pg /d quoted phrase /# ! parentheses |
| F03-007 | Highlight and hyperlink in results | 38 | Highlighted, hyperlinked hits to document passage |

## 04 — Matter Management (357 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Create and classify matter | 46 | Create matter with classification, FE, CA, court, opponents, date |
| F04-002 | Matter dashboard | 76 | Single hub: tasks, docs, comms, team, hearings, time, key dates |
| F04-003 | Capture and edit matter variables | 40 | Edit court, type, issues, opponent and lawyers |
| F04-004 | Matter documents, versions and controlled share | 63 | Scan/upload, versions, share only to allowed Posts/Persons |
| F04-005 | Consult client or expert | 30 | Consult Client / External / Research Expert / Other on the matter |
| F04-006 | Key dates, deadlines, compliance and next action | 47 | Key dates, alerts, compliance status, next action, overdue on dashboard |
| F04-007 | Matter reports | 55 | Case/court/team/CA/FE/key date/stage reports from matter records |

## 05 — Tasks, Collaboration & Communication (473 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Assign task with due date and status | 42 | Assign Person/Post, due date, status; inbox alert |
| F05-002 | Accept, reject, reassign, reminder, overdue, reprimand | 45 | Accept/reject, reassign, reminder, overdue, reprimand with Person/timestamp |
| F05-003 | Task completion report and team schedule | 42 | Completion report attachment; team member schedule/status |
| F05-004 | Court proceedings, stay alerts and cause lists | 47 | Proceedings, stay alerts, cause lists, time-critical to-dos |
| F05-005 | Queries, task requests and meetings | 42 | Queries, task requests, meeting slots on the matter |
| F05-006 | Limited/Community document sharing for legal work | 42 | Purpose-based share; Limited named vs Community |
| F05-007 | Team messages saved and searchable per matter | 48 | Sidebar/matter messages saved; search by Person/Date/Case/Key Word |
| F05-008 | Email sync, messaging, calendar and file alerts | 102 | Authorised email sync, group messaging, task calendar, file/bill alerts |
| F05-009 | Operational unit and Legal Cell coordination | 63 | Authorised group meeting/AV/docs; unauthorised cannot join |

## 06 — Unified Contact Database (210 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Office and agency contacts | 38 | SPLOCA, RC, CA, RD, DFPC, IO, Legal Team contacts |
| F06-002 | Categorised external contacts | 36 | Advocate, Accused, Petitioner, Visitor, Expert, Tahsildar, AC, Sub Registrar, custom |
| F06-003 | Unify lists and update existing | 67 | Import/merge lists; no duplicate where match confirmed |
| F06-004 | Free-text contact search | 29 | Free-text by name, office, category or fragment |
| F06-005 | Send to SMS, email or team | 40 | From contact, send number/address to SMS, email or team; log it |

## 07 — Court Attendance & Expense Management (182 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Submit court attendance | 43 | Attendance with cause list, times, Effective/Ineffective, matter |
| F07-002 | Capture category-wise expenses | 40 | Category-wise expenses with voucher against the matter |
| F07-003 | Search attendance and expense | 28 | Search by date, court, matter, person or category |
| F07-004 | Submit expense bill | 43 | Compile/submit bill; linked to matter for CA/supervisor review |
| F07-005 | Link attendance and expense to matter | 28 | Mandatory matter on save; no unlinked personal notes |

## 08 — Knowledge, SOP, Training & Retention (234 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Manuals, guidelines and SOP | 38 | Upload SOP/manuals/guidelines; search by keyword or title |
| F08-002 | Forms and format templates | 28 | Knowledge forms; distinct from Module 02 court templates |
| F08-003 | Key judgement database | 38 | Key judgements with title, date, court, keywords |
| F08-004 | OM, GO and guard-file database | 32 | OM/GO/guard file with docket title, date, author; title/word search |
| F08-005 | Training modules and FAQ | 41 | In-app Legal Research/Writing/Word/Excel training and module FAQ |
| F08-006 | Outgoing-member knowledge capture and rights | 57 | Capture leaver knowledge; remains searchable after shared IAM deactivation |

## 09 — Legal Android Application (Advocates & Legal Cell) (469 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Add contact and matter on Android | 67 | Android add contact/matter; appears on web |
| F09-002 | Android task inbox and lifecycle | 72 | Android inbox: create, accept/reject, reassign, complete, overdue, outbox |
| F09-003 | Android communication and messaging | 55 | Matter/internal messages from Android; stored on matter; web+Android |
| F09-004 | Time entry on Android | 38 | Time entry (date, duration, activity) on matter from Android |
| F09-005 | Matter dashboard on device | 67 | Android hub: tasks, comms, docs, hearings, team, client contact |
| F09-006 | Attendance and expense on Android | 63 | Android attendance/expense with voucher photo, linked to matter |
| F09-007 | Android documents | 63 | View, download, folder, upload, shared docs; same rights as web |
| F09-008 | Android distribution and licensing | 44 | Non-speculative distribution; Play Store only if SPLOCA approves; IP with SPLOCA |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Identity and masters | 01, 02 |
| P2 — Library and search | 03 |
| P3 — Matters and work | 04, 05, 06, 07 |
| P4 — Knowledge | 08 |
| P5 — Android | 09 |

## Exclusions (not in feature hours)

- Rebuild of user management (Claim Management Module 01)
- Claim settlement
- GIS field valuation (eValueI / eValueM)
- FE Management dossier
- Market intelligence and investigation process
- Generative AI
- Hardware and hosting AMC
