# Examination Module — Module List

Source: SoW_EXAM_Detailed.md

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Access Control and Staff User Management | Shared | Administrator and centre/invigilator accounts with role- and centre-scoped access. | Explicit in SOW |
| 02 | Candidate Portal Access (OTP Login) | Shared | Candidate portal entry via mobile OTP with security controls. | Explicit in SOW |
| 03 | Examination, Centre and Fee Masters | Business | Examinations, authorised centres, fee rules and examination parameters. | Explicit in SOW |
| 04 | Candidate Registration and Fee Payment | Business | Government KGID and other-organisation registration, preferences, payment and confirmation. | Explicit in SOW |
| 05 | Scheduling, Allocation, Hall Tickets and Examination Credentials | Business | Schedules, centre allocation, hall tickets and exam login credentials. | Explicit in SOW |
| 06 | Question Bank and Paper Versions | Business | Question bank maintenance and randomised multi-version papers. | Explicit in SOW |
| 07 | Secure Centre-Based Examination Conduct | Business | Centre-only CBT, invigilator activation, exam UI, timer, submit and activity recording. | Explicit in SOW |
| 08 | Evaluation, Results and Certificates | Business | Auto-evaluation, results, QR certificates and public verification. | Explicit in SOW |
| 09 | Dashboards, Reports, Notifications and Audit | Shared | Admin dashboard, MIS reports, lifecycle notifications and system audit trail. | Explicit in SOW |

***Module Details***

### 01. Access Control and Staff User Management

- **Type:** Shared
- **Summary:** Administrator and centre/invigilator accounts with role- and centre-scoped access.
- **Source:** Explicit in SOW
- **In Scope:** Examination Administrator accounts and privileges; Centre/Invigilator users mapped to authorised centres only; activate/deactivate; role-based menus for admin and centre functions.
- **Out of Scope:** Candidate OTP login (Module 02); examination-day credentials (Module 05); public verifier identity beyond verification page (Module 08).
- **Key Actors:** Examination Administrator; Centre/Invigilator users.
- **Dependencies:** None (foundation for staff work).
- **Notes:** Access model is user → role, with centre scope for invigilators.

### 02. Candidate Portal Access (OTP Login)

- **Type:** Shared
- **Summary:** Candidate portal entry via mobile OTP with security controls.
- **Source:** Explicit in SOW
- **In Scope:** Mobile number entry, OTP send/validate, session; expiry, retry, resend, failed-attempt tracking, session timeout.
- **Out of Scope:** Staff login (Module 01); CBT exam credentials (Module 05/07).
- **Key Actors:** Candidate.
- **Dependencies:** SMS gateway (integration).
- **Notes:** Separate from examination Login ID/Password used at the centre.

### 03. Examination, Centre and Fee Masters

- **Type:** Business
- **Summary:** Examinations, authorised centres, fee rules and examination parameters.
- **Source:** Explicit in SOW
- **In Scope:** Examination catalogue; centre master (capacity, activate/deactivate, session mapping, allocation visibility); fee rules by category/attempt; examination parameters (duration, marks, pass, randomisation, versions, result/certificate rules).
- **Out of Scope:** Live CBT conduct (Module 07); registration transactions (Module 04).
- **Key Actors:** Examination Administrator.
- **Dependencies:** Module 01.
- **Notes:** Only active authorised centres are selectable for preferences and scheduling.

### 04. Candidate Registration and Fee Payment

- **Type:** Business
- **Summary:** Government KGID and other-organisation registration, preferences, payment and confirmation.
- **Source:** Explicit in SOW
- **In Scope:** Type 1 KGID path; Type 2 manual + competent-authority document; exam selection; two centre preferences; fee calculation and payment; unique registration number; status view; admin verification where configured.
- **Out of Scope:** Rebuild of KGID; payment gateway product itself (integration only).
- **Key Actors:** Candidate; Examination Administrator (verification).
- **Dependencies:** Modules 02, 03; KGID and payment integrations.
- **Notes:** Document upload and verification workflow are embedded.

### 05. Scheduling, Allocation, Hall Tickets and Examination Credentials

- **Type:** Business
- **Summary:** Schedules, centre allocation, hall tickets and exam login credentials.
- **Source:** Explicit in SOW
- **In Scope:** Schedule creation; allocation by preferences/capacity/rules; hall ticket download/print; generate and communicate examination Login ID/Password.
- **Out of Scope:** Centre-day activation (Module 07).
- **Key Actors:** Examination Administrator; Candidate (download hall ticket).
- **Dependencies:** Modules 03, 04.
- **Notes:** Hall ticket only after schedule and allocation.

### 06. Question Bank and Paper Versions

- **Type:** Business
- **Summary:** Question bank maintenance and randomised multi-version papers.
- **Source:** Explicit in SOW
- **In Scope:** Question CRUD/import; categories, marks, keys; random selection; versions A/B/C/D with randomised question and option order; answer-key integrity.
- **Out of Scope:** Live paper delivery UI (Module 07 consumes generated paper).
- **Key Actors:** Examination Administrator.
- **Dependencies:** Module 03 (examination parameters).
- **Notes:** Randomisation must not break correct-answer mapping.

### 07. Secure Centre-Based Examination Conduct

- **Type:** Business
- **Summary:** Centre-only CBT, invigilator activation, exam UI, timer, submit and activity recording.
- **Source:** Explicit in SOW
- **In Scope:** Authorised-centre enforcement; centre dashboard; verification and session activation; exam login; secure interface; timer and auto-submit; response lock; activity recording.
- **Out of Scope:** Home/personal-device exam; subjective marking.
- **Key Actors:** Centre/Invigilator; Candidate at centre.
- **Dependencies:** Modules 01, 03, 05, 06.
- **Notes:** Exact IP/device/browser mechanism finalised with Department; business rule is centre-only.

### 08. Evaluation, Results and Certificates

- **Type:** Business
- **Summary:** Auto-evaluation, results, QR certificates and public verification.
- **Source:** Explicit in SOW
- **In Scope:** Objective auto-score; result publication; certificate issue/download; QR and public verification; cancellation/revocation if required.
- **Out of Scope:** Subjective evaluation; generative certificate content.
- **Key Actors:** Examination Administrator; Candidate; Public verifier.
- **Dependencies:** Modules 02, 06, 07.
- **Notes:** Public page shows only approved disclosure fields.

### 09. Dashboards, Reports, Notifications and Audit

- **Type:** Shared
- **Summary:** Admin dashboard, MIS reports, lifecycle notifications and system audit trail.
- **Source:** Explicit in SOW
- **In Scope:** Administrator operational dashboard; candidate/fee/examination/certificate reports with export; SMS/email/portal notifications; audit of critical activities.
- **Out of Scope:** Separate reporting-engine product; CCC integration.
- **Key Actors:** Examination Administrator; Candidate (notifications/inbox).
- **Dependencies:** Modules 01–08 as data sources.
- **Notes:** Notification channels finalised at confirmation; audit is a first-class feature here.

***Excluded / Embedded Capabilities***

| Capability | Treatment |
|------------|-----------|
| Document management | Embedded (competent-authority upload in Module 04) |
| Workflow engine | Embedded (registration verification, invigilator activation, evaluation) |
| Integration hub | KGID/payment/SMS estimated as Integration rows on owning features; not a separate module per SOW consolidation |
| Public verifier role | Certificate verification page in Module 08; no staff account required |
| Seat/computer assignment | Covered under centre allocation / hall ticket / centre conduct as applicable; not a separate SOW feature ID |

***Assumptions***

1. SOW module numbers and feature IDs are reused without renumbering.
2. Objective CBT only in this phase.
3. Centre access technical mechanism chosen later without shrinking centre-only scope.
4. Integrations estimated on features that own the channel (KGID, payment, SMS/email).

***Risks***

1. KGID API field gaps force manual override paths in registration.
2. Weak centre network controls undermine centre-only CBT.
3. Thin question pools break multi-version randomisation.
4. Payment failure handling must not leave half-registered candidates.
