# Legal Management Application (KPID / SPLOCA) — Module List

Source: `SoW_LEGAL_Detailed.md` (v1.0)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Shared User & Access Control (consumed) | Shared | Consume Claim Module 01 identity; Legal Posts, Limited/Community, legal document rights, web+Android session | Explicit in SOW |
| 02 | Legal Masters, Keywords & Templates | Shared | Keyword catalogues, Act/section coding, court-approved statutory templates, central masters | Explicit in SOW |
| 03 | Legal Knowledge Library & Search | Business | Acts/Rules, opinions, orders, petitions/SOB/arguments; NL and Boolean search | Explicit in SOW |
| 04 | Matter Management | Business | Matter create/classify, dashboard, documents, consultations, key dates, matter reports | Explicit in SOW |
| 05 | Tasks, Collaboration & Communication | Business | Task lifecycle, court alerts, queries/meetings, Limited/Community share, email/messages | Explicit in SOW |
| 06 | Unified Contact Database | Business | Office, agency and categorised contacts; search; SMS/email/team hand-off | Explicit in SOW |
| 07 | Court Attendance & Expense Management | Business | Court attendance with cause list; category expenses; bills linked to matter | Explicit in SOW |
| 08 | Knowledge, SOP, Training & Retention | Business | SOP/forms/judgements/OM-GO, training/FAQ, outgoing-member knowledge capture | Explicit in SOW |
| 09 | Legal Android Application (Advocates & Legal Cell) | Business | Android contact/matter/task/comms/time/dashboard/attendance/docs; licensing | Explicit in SOW |

---

## Module Details

### 01. Shared User & Access Control (consumed)

- **Type:** Shared
- **Slug:** `shared-user-access-control`
- **Summary:** Wire Legal web and Android to Claim Management Module 01; add Legal-specific spaces and document rights only.
- **Source:** Explicit in SOW §6 Module 01; Claim SOW F01-001–F01-007, F01-010.
- **In Scope:** F01-001 … F01-004 — consume shared Person–Post–Role; Limited vs Community; legal document rights; Legal web and Android on that identity. Configure Legal Cell / Advocate Posts **on** the shared component.
- **Out of Scope:** Rebuilding Person, Post, Role, OTP, 2FA, official identity or forensic login audit as a second product.
- **Key Actors:** Administrator (shared IAM), Legal Cell, Advocate, Competent Authority.
- **Dependencies:** Claim Management Module 01 must be available.
- **Notes:** No second user master. Feature generation estimates only the Legal-specific wiring and spaces.

### 02. Legal Masters, Keywords & Templates

- **Type:** Shared
- **Slug:** `legal-masters-keywords-templates`
- **Summary:** Keyword/entity catalogues, Act/Rules coding, stored court-approved templates (5(2), notices, 7(1)/8(1), SOB, PWR, Caveat, IA, SLP, letters, freezing orders, warrants), central static masters.
- **Source:** Explicit in SOW §6 Module 02; Annexure-I; Proceedings items 7, 8, 21.
- **In Scope:** F02-001 … F02-006.
- **Out of Scope:** Generative-AI drafting; Claim settlement notices that belong to Claim SOW except template generation here.
- **Key Actors:** Administrator, Legal Cell, Advocate.
- **Dependencies:** 01 Shared access.
- **Notes:** Human verification before issue.

### 03. Legal Knowledge Library & Search

- **Type:** Business
- **Slug:** `legal-knowledge-library-search`
- **Summary:** Coded library of Acts/Rules, opinions, Special/High Court orders, petitions, SOBs and written arguments with NL search, search-within-results and Boolean connectors.
- **Source:** Explicit in SOW §6 Module 03; Annexure-I §1–2.
- **In Scope:** F03-001 … F03-007.
- **Out of Scope:** Public website search; standalone search product.
- **Key Actors:** Legal Cell, Advocate.
- **Dependencies:** 01 Access; 02 Keywords.
- **Notes:** Originals unchanged; highlights/hyperlinks in results.

### 04. Matter Management

- **Type:** Business
- **Slug:** `matter-management`
- **Summary:** Matter as hub — create/classify, dashboard, variables, versioned documents, consultations, key dates/compliance, reports.
- **Source:** Explicit in SOW §6 Module 04; Annexure-I §8.
- **In Scope:** F04-001 … F04-007.
- **Out of Scope:** Standalone DMS/BPM; citizen matter portal.
- **Key Actors:** Legal Cell, Advocate, Competent Authority.
- **Dependencies:** 01 Access; 02 Keywords/templates; 03 Library; 06 Contacts.
- **Notes:** FE/CA from programme references, not a new FE dossier.

### 05. Tasks, Collaboration & Communication

- **Type:** Business
- **Slug:** `tasks-collaboration-communication`
- **Summary:** Matter and official tasks; court/stay/cause-list alerts; queries and meetings; Limited/Community sharing; matter messages; email sync and operational-unit coordination.
- **Source:** Explicit in SOW §6 Module 05; Annexure-I §3–4; Proceedings items 6–8.
- **In Scope:** F05-001 … F05-009.
- **Out of Scope:** Public collaboration portal; market-intelligence investigation rooms.
- **Key Actors:** Legal Cell, Advocate, authorised operational-unit users.
- **Dependencies:** 01 Access (Limited/Community); 04 Matter.
- **Notes:** Need-to-know still applies to AV/group meetings.

### 06. Unified Contact Database

- **Type:** Business
- **Slug:** `unified-contact-database`
- **Summary:** Unified office/agency and categorised external contacts with search and SMS/email/team actions.
- **Source:** Explicit in SOW §6 Module 06; Annexure-I §5.
- **In Scope:** F06-001 … F06-005.
- **Out of Scope:** Marketing CRM; payment contacts.
- **Key Actors:** Legal Cell, Advocate, Administrator.
- **Dependencies:** 01 Access; SMS/email services.
- **Notes:** Unify/merge without confirmed duplicates.

### 07. Court Attendance & Expense Management

- **Type:** Business
- **Slug:** `court-attendance-expense-management`
- **Summary:** Court attendance (including cause list) and category-wise expenses/bills always linked to the matter.
- **Source:** Explicit in SOW §6 Module 07; Annexure-I §6; Proceedings item 7.
- **In Scope:** F07-001 … F07-005.
- **Out of Scope:** Payroll; valuer billing (EVAL); reimbursement gateway.
- **Key Actors:** Advocate, Legal Cell, Competent Authority / supervisor.
- **Dependencies:** 01 Access; 04 Matter.
- **Notes:** Unlinked personal notes are not allowed.

### 08. Knowledge, SOP, Training & Retention

- **Type:** Business
- **Slug:** `knowledge-sop-training-retention`
- **Summary:** Manuals/SOP, forms, key judgements, OM/GO/guard file, in-app training/FAQ, outgoing-member knowledge capture and rights.
- **Source:** Explicit in SOW §6 Module 08; Annexure-I §7; Proceedings item 23.
- **In Scope:** F08-001 … F08-006.
- **Out of Scope:** Classroom/instructor-led training unless separately ordered; LMS vendor product.
- **Key Actors:** Legal Cell, Administrator, knowledge owners.
- **Dependencies:** 01 Access; 02 Keywords.
- **Notes:** Knowledge remains after Person deactivation on shared IAM.

### 09. Legal Android Application (Advocates & Legal Cell)

- **Type:** Business
- **Slug:** `legal-android-application`
- **Summary:** Official Android app on shared identity for contacts, matters, tasks, communication, time, dashboard, attendance/expense and documents.
- **Source:** Explicit in SOW §6 Module 09; Annexure-I §9; Proceedings items 1, 19.
- **In Scope:** F09-001 … F09-008 including Play Store licensing where specifically approved.
- **Out of Scope:** iOS; public Play Store consumer app; second login directory.
- **Key Actors:** Advocate, Legal Cell.
- **Dependencies:** 01 Shared identity; 04–07 backend capabilities.
- **Notes:** IP with SPLOCA; licensing must be non-speculative.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| User management / IAM | Consumed from Claim Module 01 — not rebuilt |
| Document Management | Embedded in library, matter, collaboration |
| Workflow engine | Embedded in tasks and matter |
| Notifications (email sync, SMS from contacts, alerts) | Embedded in Modules 05–06; no standalone Notification Service |
| Platform backup / HTTPS / AES-256 | NFR (SOW §11–12); not a separate module |
| Claim settlement | Claim SOW |
| GIS field valuation | Valuation SOW |
| FE dossier | Existing FE application |
| Market intelligence / investigation | Out of scope except template notices (Module 02) |
| Generative AI | Prohibited |
| Office IT inventory | Out of scope |

---

## Assumptions

1. Module `{NN}` and feature IDs match `SoW_LEGAL_Detailed.md`.
2. Shared IAM is Claim Module 01; this list does not re-estimate that full identity product except F01-001–F01-004 wiring/spaces.
3. Document handling and workflow remain embedded.
4. No hours in this step.

---

## Risks

1. Shared IAM not ready delays Legal web and Android.
2. Court-approved font/spacing for templates must be supplied by SPLOCA.
3. Email sync and AV meeting policy may tighten Limited/Community rules.
4. Play Store licensing depends on a specific SPLOCA approval.
