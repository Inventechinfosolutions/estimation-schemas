# LEGAL — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 4,149 hours · **Go-live:** 4,149 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Shared User & Access Control (consumed) | Shared | 4 | 292 | 7.0% |
| 02 | Legal Masters, Keywords & Templates | Shared | 6 | 403 | 9.7% |
| 03 | Legal Knowledge Library & Search | Business | 7 | 523 | 12.6% |
| 04 | Matter Management | Business | 7 | 507 | 12.2% |
| 05 | Tasks, Collaboration & Communication | Business | 9 | 727 | 17.5% |
| 06 | Unified Contact Database | Business | 5 | 324 | 7.8% |
| 07 | Court Attendance & Expense Management | Business | 5 | 296 | 7.1% |
| 08 | Knowledge, SOP, Training & Retention | Business | 6 | 368 | 8.9% |
| 09 | Legal Android Application (Advocates & Legal Cell) | Business | 8 | 709 | 17.1% |
| | **Total** | | **57** | **4,149** | **100%** |

## 01 — Shared User & Access Control (consumed) (292 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Consume shared Person–Post–Role identity | 76 | Wiring to Claim Module 01; no second Person master |
| F01-002 | Limited vs Community legal spaces | 67 | Named Limited members vs Community publish; need-to-know still applies |
| F01-003 | Legal document rights | 64 | View/download/share/edit by Post and classification; access log |
| F01-004 | Legal web and Android on shared identity | 85 | Same Person/2FA on web and Android; deactivation ends both |

## 02 — Legal Masters, Keywords & Templates (403 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Keyword and entity catalogues | 68 | FE/CA/Accused/Advocate/Judge/Act/doctrine catalogues for coding |
| F02-002 | Act and Rules coding | 64 | Code Acts/Rules/sections for library hyperlinks |
| F02-003 | Court-approved legal templates | 71 | Stored 5(2)/notice/7(1)/8(1)/SOB/PWR/Caveat/IA/SLP/letter/freezing/warrant |
| F02-004 | Generate draft from template | 94 | Human-verified merge from stored templates; no generative AI |
| F02-005 | Central static and master data | 52 | One central master; matter/Android consume, do not fork |
| F02-006 | Keyword–document link maintenance | 54 | Create/repair keyword links after catalogue change |

## 03 — Legal Knowledge Library & Search (523 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Acts and Rules library | 62 | Upload/code Acts/Rules; originals unchanged on open |
| F03-002 | Research and legal opinions | 64 | File opinions with FE/CA/case/Act coding |
| F03-003 | Special Court and High Court orders | 65 | File orders with accused/advocates/judge coding |
| F03-004 | Petitions, SOBs and written arguments | 64 | Same referencing as orders; versioned petitions/SOB/arguments |
| F03-005 | Natural-language search and search-within-results | 102 | Plain-language query plus Search Within Results |
| F03-006 | Boolean terms and connectors | 104 | AND OR NOT /p /s /pg /d quoted phrase /# ! parentheses |
| F03-007 | Highlight and hyperlink in results | 62 | Highlighted, hyperlinked hits to document passage |

## 04 — Matter Management (507 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Create and classify matter | 68 | Create matter with classification, FE, CA, court, opponents, date |
| F04-002 | Matter dashboard | 96 | Single hub: tasks, docs, comms, team, hearings, time, key dates |
| F04-003 | Capture and edit matter variables | 62 | Edit court, type, issues, opponent and lawyers |
| F04-004 | Matter documents, versions and controlled share | 83 | Scan/upload, versions, share only to allowed Posts/Persons |
| F04-005 | Consult client or expert | 54 | Consult Client / External / Research Expert / Other on the matter |
| F04-006 | Key dates, deadlines, compliance and next action | 69 | Key dates, alerts, compliance status, next action, overdue on dashboard |
| F04-007 | Matter reports | 75 | Case/court/team/CA/FE/key date/stage reports from matter records |

## 05 — Tasks, Collaboration & Communication (727 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Assign task with due date and status | 122 | Assign Person/Post, due date, status; inbox alert |
| F05-002 | Accept, reject, reassign, reminder, overdue, reprimand | 67 | Accept/reject, reassign, reminder, overdue, reprimand with Person/timestamp |
| F05-003 | Task completion report and team schedule | 64 | Completion report attachment; team member schedule/status |
| F05-004 | Court proceedings, stay alerts and cause lists | 69 | Proceedings, stay alerts, cause lists, time-critical to-dos |
| F05-005 | Queries, task requests and meetings | 64 | Queries, task requests, meeting slots on the matter |
| F05-006 | Limited/Community document sharing for legal work | 64 | Purpose-based share; Limited named vs Community |
| F05-007 | Team messages saved and searchable per matter | 70 | Sidebar/matter messages saved; search by Person/Date/Case/Key Word |
| F05-008 | Email sync, messaging, calendar and file alerts | 122 | Authorised email sync, group messaging, task calendar, file/bill alerts |
| F05-009 | Operational unit and Legal Cell coordination | 85 | Authorised group meeting/AV/docs; unauthorised cannot join |

## 06 — Unified Contact Database (324 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Office and agency contacts | 60 | SPLOCA, RC, CA, RD, DFPC, IO, Legal Team contacts |
| F06-002 | Categorised external contacts | 58 | Advocate, Accused, Petitioner, Visitor, Expert, Tahsildar, AC, Sub Registrar, custom |
| F06-003 | Unify lists and update existing | 89 | Import/merge lists; no duplicate where match confirmed |
| F06-004 | Free-text contact search | 53 | Free-text by name, office, category or fragment |
| F06-005 | Send to SMS, email or team | 64 | From contact, send number/address to SMS, email or team; log it |

## 07 — Court Attendance & Expense Management (296 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Submit court attendance | 65 | Attendance with cause list, times, Effective/Ineffective, matter |
| F07-002 | Capture category-wise expenses | 62 | Category-wise expenses with voucher against the matter |
| F07-003 | Search attendance and expense | 52 | Search by date, court, matter, person or category |
| F07-004 | Submit expense bill | 65 | Compile/submit bill; linked to matter for CA/supervisor review |
| F07-005 | Link attendance and expense to matter | 52 | Mandatory matter on save; no unlinked personal notes |

## 08 — Knowledge, SOP, Training & Retention (368 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Manuals, guidelines and SOP | 60 | Upload SOP/manuals/guidelines; search by keyword or title |
| F08-002 | Forms and format templates | 52 | Knowledge forms; distinct from Module 02 court templates |
| F08-003 | Key judgement database | 60 | Key judgements with title, date, court, keywords |
| F08-004 | OM, GO and guard-file database | 54 | OM/GO/guard file with docket title, date, author; title/word search |
| F08-005 | Training modules and FAQ | 63 | In-app Legal Research/Writing/Word/Excel training and module FAQ |
| F08-006 | Outgoing-member knowledge capture and rights | 79 | Capture leaver knowledge; remains searchable after shared IAM deactivation |

## 09 — Legal Android Application (Advocates & Legal Cell) (709 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Add contact and matter on Android | 89 | Android add contact/matter; appears on web |
| F09-002 | Android task inbox and lifecycle | 152 | Android inbox: create, accept/reject, reassign, complete, overdue, outbox |
| F09-003 | Android communication and messaging | 79 | Matter/internal messages from Android; stored on matter; web+Android |
| F09-004 | Time entry on Android | 62 | Time entry (date, duration, activity) on matter from Android |
| F09-005 | Matter dashboard on device | 89 | Android hub: tasks, comms, docs, hearings, team, client contact |
| F09-006 | Attendance and expense on Android | 85 | Android attendance/expense with voucher photo, linked to matter |
| F09-007 | Android documents | 85 | View, download, folder, upload, shared docs; same rights as web |
| F09-008 | Android distribution and licensing | 68 | Non-speculative distribution; Play Store only if SPLOCA approves; IP with SPLOCA |

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
