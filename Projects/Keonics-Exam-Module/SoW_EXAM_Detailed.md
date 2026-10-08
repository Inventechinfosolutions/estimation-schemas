# Statement of Work (SOW)

# Karnataka State Electronics Development Corporation Limited (KEONICS)

# Examination Module

**Document Type:** Statement of Work – Business Requirements  
**Version:** 1.0  
**Status:** Draft  
**Source:** Exam Module.docx (functional outline)  
**Prepared for:** KEONICS / Client Department  

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control](#8-access-control)
9. [Channels](#9-channels)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria](#16-acceptance-criteria)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)
20. [Appendix A — Module & Feature Index](#20-appendix-a--module--feature-index)
21. [Appendix B — Key Business Rules](#21-appendix-b--key-business-rules)
22. [Appendix C — Key Entities](#22-appendix-c--key-entities)
23. [Appendix D — Mapping from Source Outline](#23-appendix-d--mapping-from-source-outline)

---

## 1. Introduction

This Statement of Work states the **business requirements** for an **Examination Module** that provides an end-to-end digital platform for **candidate registration**, **examination scheduling**, **hall ticket generation**, **secure computer-based examination**, **evaluation**, **result publication**, **certificate generation**, and **public certificate verification**.

The system shall support two candidate categories:

1. **Government Department Employees**  
2. **Employees of PSUs, Boards, Corporations, Societies and other eligible organisations**

Candidates shall take examinations **only from authorised examination centres** configured and approved by the Department. Examination from home, personal devices, or unauthorised locations is **not permitted**.

Document upload (competent-authority confirmation) and operational workflows (registration approval, centre activation, evaluation) are **embedded** in the business processes. They are not separate document-management or workflow products.

This document is prepared for RFP discussion and internal estimation. It does not prescribe technology stack, APIs, database design, or screen layouts.

---

## 2. Project Overview

The Examination Module digitises the full lifecycle from candidate login through certificate verification. Government employees register using a mandatory **KGID number**, with employee details retrieved through KGID integration where available. Other organisation employees register manually and upload a **digitally signed competent-authority confirmation**. Fee rules differ by category and attempt history. After scheduling and centre allocation, candidates receive a digital hall ticket and system-generated examination credentials, report to the allotted centre, and sit a randomised computer-based paper under centre and invigilator control. Objective papers are auto-evaluated; eligible candidates receive a certificate with a unique **QR code** that any third party may verify online.

### 2.1 Business Context

| Aspect | Description |
| ------ | ----------- |
| Organisation | KEONICS / Client Department (examination authority) |
| Primary candidates | Government department employees; PSU / Board / Corporation / Society / other eligible organisation employees |
| Primary staff | Examination Administrator; Examination Centre / Invigilator users |
| Public users | Certificate verifiers (QR / verification page) |
| Primary outcomes | Secure centre-only CBT; digital hall tickets; results; QR-verifiable certificates |
| Critical control | Examination access only from authorised centres for allotted candidates and sessions |

### 2.2 Guiding Principles

1. OTP-based candidate portal login; separate system-generated credentials for the examination itself.  
2. KGID-driven registration for government employees; manual + competent-authority document for other organisations.  
3. Fee rules: first government attempt free; subsequent government attempts and all other-organisation registrations payable as configured.  
4. Candidates select **two preferred centres**; final allocation is by administrator / system rules.  
5. Question bank with random selection, multiple versions (A/B/C/D), randomised question and option order, without breaking the answer key.  
6. Centre + network/device + session + invigilator activation before a candidate can start.  
7. Full audit of registration, payment, paper generation, exam activity, results and certificates.

---

## 3. Project Objectives

1. Provide secure candidate login using mobile OTP.  
2. Enable online examination registration for both candidate categories.  
3. Integrate with KGID for government department employees and retrieve available employee information.  
4. Support configurable examination fee management and payment confirmation.  
5. Allow centre preference selection and controlled centre allocation.  
6. Generate and publish digital hall tickets after scheduling and allocation.  
7. Conduct secure computer-based examinations only at authorised centres.  
8. Generate multiple randomised question-paper versions from a managed question bank.  
9. Record examination activity for audit and monitoring.  
10. Evaluate objective papers and publish results per configured rules.  
11. Issue digitally verifiable certificates with unique QR codes.  
12. Allow third parties to verify certificate authenticity online.

---

## 4. In Scope / Out of Scope

### In Scope

- Candidate portal: OTP login, registration (both types), centre preferences, fee payment where applicable, registration status, hall ticket download, result view, certificate download.  
- Examination Administrator functions: examinations, schedules, centres, registrations, question bank, examination parameters, paper versions, session monitoring, results, certificates, reports and dashboards.  
- Examination Centre / Invigilator functions: centre dashboard, candidate verification, session activation, attendance and status monitoring.  
- Public certificate verification page (QR / token).  
- KGID integration (subject to API / data availability).  
- Payment initiation, status, receipt and failed-payment handling where fee applies.  
- Competent-authority document template download and upload (configured formats and sizes).  
- Secure CBT interface with timer, auto-save, navigation, submit and auto-submit.  
- Automatic evaluation for objective-type examinations.  
- SMS / email / portal notifications as finally configured.  
- Audit trail for critical activities listed in the source.  
- Embedded document handling and workflows (not separate DMS/workflow products).

### Out of Scope

- Examination from home, personal laptop/mobile, or any unauthorised location or centre.  
- Subjective / descriptive answer evaluation (source describes objective auto-evaluation; subjective marking is out unless later added).  
- Rebuild of the KGID system itself (integration only).  
- Physical centre infrastructure, hardware, networking and seating (client / centre responsibility).  
- Final technical choice of IP whitelist vs device whitelist vs secure browser (to be finalised with Department infrastructure; business requirement is centre-only access).  
- Generative AI question authoring or unsupervised certificate content.  
- Legacy bulk migration of prior examination history (not stated in source; out of scope unless later ordered).  
- Native mobile examination app (source describes centre computers; not a candidate mobile exam app).  
- Detailed technical architecture, API contracts, database schemas and UI wireframes (design stage).

---

## 5. Solution Expectations

- Candidates use a portal on mobile number + OTP for registration and post-exam services.  
- At the centre, candidates use **system-generated examination Login ID and Password** on an authorised machine after invigilator verification and session activation.  
- Registration is complete only after successful payment where payment is mandatory.  
- Hall ticket appears only after examination scheduling and centre allocation.  
- The examination starts only when registration, fee compliance, schedule, centre mapping, authorised environment and invigilator activation all succeed.  
- Randomisation never changes the underlying correct-answer mapping.  
- Results and certificates follow administrator-configured publication and eligibility rules.  
- Public verification shows only information approved for disclosure; cancelled certificates return the appropriate status.

---

## 6. Consolidated Functional Modules

### 01. Access Control and Staff User Management

**Purpose:** Create and control Examination Administrator and Centre / Invigilator users, and enforce role-based menus for staff functions.

**Type:** Shared

**Functional requirements:**

- Maintain staff users for Examination Administrator and Examination Centre / Invigilator roles.  
- Map centre users only to their authorised centre(s).  
- Role-based access to administration, centre dashboard, question bank, scheduling, results and certificates.  
- Activate / deactivate staff accounts.

**Acceptance criteria:**

- A centre user cannot see examinations or candidates of another centre.  
- An inactive staff account cannot log in.  
- Administrator functions are available only to authorised Administrator users.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Administrator Accounts and Privileges | Create and manage Examination Administrator users and privileges. |
| F01-002 | Centre and Invigilator User Mapping | Create centre users, map them to authorised centres, and restrict access to that centre’s work. |

---

### 02. Candidate Portal Access (OTP Login)

**Purpose:** Let candidates securely enter the examination portal using mobile OTP before registration or post-registration services.

**Type:** Shared

**Functional requirements:**

- Candidate enters mobile number; system validates, sends OTP, validates OTP, and opens the portal session.  
- OTP security controls: expiry, retry limits, resend control, failed-attempt tracking, session timeout.

**Acceptance criteria:**

- Login succeeds only after a valid OTP within expiry and retry limits.  
- Excess failed attempts are blocked per configured policy.  
- Idle / expired sessions require a fresh OTP login.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Mobile OTP Login | Candidate portal login via registered mobile number and OTP. |
| F02-002 | OTP Security Controls | Expiry, retry, resend, failed-attempt tracking and session timeout for candidate OTP login. |

---

### 03. Examination, Centre and Fee Masters

**Purpose:** Hold examinations open for registration, authorised centres, fee rules and examination configuration parameters.

**Type:** Business

**Functional requirements:**

- Create and manage examinations open for registration and their display details.  
- Examination centre master: add/edit, activate/deactivate, capacity, infrastructure details, map sessions, configure centre users, view allocations.  
- Fee rules: first government attempt free; subsequent government attempts payable; other-organisation fee mandatory; amounts configurable.  
- Examination configuration: name, duration, question counts, marks, passing criteria, negative marking if applicable, randomisation flags, versions, instructions, result and certificate eligibility rules.

**Acceptance criteria:**

- Only active authorised centres are available for preference selection and scheduling.  
- Fee calculation uses category and attempt history correctly.  
- Examination parameters are configurable without code change for approved rule sets.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Examination Catalogue | Create and manage examinations open for registration and their published details. |
| F03-002 | Authorised Examination Centre Master | Maintain centre identity, capacity, activation, session mapping and allocation visibility. |
| F03-003 | Fee Rules and Attempt History Basis | Configure fee rules by category and attempt; use attempt history for first vs subsequent government registration. |
| F03-004 | Examination Parameter Configuration | Configure duration, marks, pass rules, randomisation, versions, instructions, result and certificate rules. |

---

### 04. Candidate Registration and Fee Payment

**Purpose:** Complete registration for both candidate types, including KGID path, other-organisation documents, centre preferences, payment and confirmation.

**Type:** Business

**Functional requirements:**

- **Type 1 — Government:** mandatory KGID; retrieve available employee details via integration; candidate confirms; enter additional fields (father’s name, mobile, email, other required).  
- **Type 2 — Other organisations:** manual entry of name, father’s name, mobile, email, employee ID, organisation, date of joining, designation and other configurable fields; download competent-authority format; upload digitally signed confirmation (configured formats/sizes); associate document with registration for admin verification.  
- Select examination currently open for registration; select **two preferred centres**.  
- Fee path: calculate; initiate payment; track status; confirm success; handle failure; store transaction/reference; issue receipt; complete registration only after successful payment where mandatory.  
- After success: unique registration/application number; store application, examination, preferences, documents, payment; show confirmation; allow status view from login.  
- Administrator management of candidate registrations, including verification/approval where applicable.

**Acceptance criteria:**

- Government registration cannot proceed without KGID and candidate confirmation of retrieved details (subject to integration availability).  
- Other-organisation registration cannot complete without the uploaded competent-authority document and mandatory fee payment.  
- Two centre preferences are captured and used later in allocation.  
- Unique registration number is issued and visible in the candidate login.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Government Employee Registration with KGID | KGID capture, integration retrieval, confirmation and additional details. |
| F04-002 | Other Organisation Registration and Competent Authority Document | Manual registration fields, template download and digitally signed document upload. |
| F04-003 | Examination Selection and Centre Preferences | Select open examination and two preferred centres. |
| F04-004 | Fee Calculation and Payment | Fee calculation, payment initiation, success/failure handling, receipt and registration completion gate. |
| F04-005 | Registration Confirmation and Status | Unique registration number, stored application pack, confirmation and candidate status view. |
| F04-006 | Administrator Registration Verification | Admin review/verification/approval of registrations where configured. |

---

### 05. Scheduling, Allocation, Hall Tickets and Examination Credentials

**Purpose:** Schedule sessions, allocate candidates to centres, publish hall tickets and issue examination login credentials.

**Type:** Business

**Functional requirements:**

- Create schedules: examination name, date, time, duration, reporting time, centre, seats/capacity, instructions.  
- Allocate candidates using preferences, availability, capacity, schedule, category and other department rules; show final centre on hall ticket.  
- Hall ticket in candidate login after schedule + allocation: name, registration number, examination, date/time, reporting time, centre and address, photograph/details if applicable, instructions, credential information if applicable; download/print.  
- Generate examination Login ID and Password; share securely by approved communication mechanism.

**Acceptance criteria:**

- Hall ticket is unavailable before scheduling and allocation.  
- Allocated centre matches the session the candidate may attend.  
- Examination credentials are generated for scheduled candidates and usable only in the authorised session path.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Examination Schedule Management | Create and manage examination date, time, duration, centres and capacity. |
| F05-002 | Centre Allocation | Allocate candidates using preferences, capacity and department rules. |
| F05-003 | Hall Ticket Generation and Download | Publish and allow download/print of hall tickets after allocation. |
| F05-004 | Examination Credential Generation | Generate and securely communicate examination Login ID and Password. |

---

### 06. Question Bank and Paper Versions

**Purpose:** Maintain the question bank and generate randomised multi-version papers without breaking answer keys.

**Type:** Business

**Functional requirements:**

- Create/edit/deactivate questions; categorise; configure type, marks, correct answers, difficulty, subject/topic; import if required.  
- Random selection of required count from eligible pool by examination configuration (including per-category counts if required).  
- Multiple versions (A/B/C/D) with randomised question order and answer-option order; correct-answer mapping preserved.

**Acceptance criteria:**

- A generated paper has the configured number of questions and marks.  
- Different versions present different orders while preserving scoring correctness.  
- Deactivated questions are not selected for new papers.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Question Bank Maintenance | Create, edit, categorise, score and activate/deactivate questions; import if required. |
| F06-002 | Random Paper Generation and Versions | Random selection and A/B/C/D versions with randomised question and option order. |

---

### 07. Secure Centre-Based Examination Conduct

**Purpose:** Enforce authorised-centre-only CBT, invigilator activation, secure exam interface, timer, submission and activity recording.

**Type:** Business

**Functional requirements:**

- Centre-only access: deny home, personal device, other network/city, wrong centre, unauthorised computer; allow only authorised computer at allotted centre during scheduled session after validations.  
- Validations before start: registered and eligible; allotted to centre; scheduled date/time; authorised system/network/device; centre and session active; invigilator-validated/activated; not already completed.  
- Centre dashboard: today’s/upcoming exams; candidate counts; present/absent; started/completed; active/submitted; status; centre reports; centre-scoped only.  
- Invigilator: view schedule and list; verify attendance; activate eligible sessions; monitor status.  
- Exam login at centre with system credentials; validate candidate, centre, session and timing.  
- Secure interface: question text/options, next/previous, navigation, answered/unanswered status, remaining time, submit; auto-save responses.  
- Central timer; auto-stop and auto-submit on expiry.  
- Manual submit with answered/unanswered summary and confirmation; lock responses; start evaluation.  
- Record login/start/submit times, responses, version/sequence, centre, device/system, IP/network where available, session events, abnormal events, auto-submit.  
- Prevent multiple simultaneous sessions; browser/session controls as finally approved with infrastructure.

**Acceptance criteria:**

- Access from unauthorised location/device/network/centre is denied.  
- Examination cannot start without invigilator activation for that candidate/session.  
- Timer expiry auto-submits saved responses and blocks further answers.  
- Centre users see only their centre’s candidates and sessions.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Authorised Centre Access Enforcement | Validate centre, session, allocation and authorised environment before allowing exam start. |
| F07-002 | Centre Dashboard and Invigilator Activation | Centre-scoped dashboard, candidate verification, attendance and session activation. |
| F07-003 | Examination Login at Centre | Candidate login with system-generated credentials under centre and session validation. |
| F07-004 | Secure Examination Interface and Timer | CBT UI, navigation, auto-save, central timer and auto-submit on expiry. |
| F07-005 | Examination Submission and Response Lock | Candidate submit with confirmation; lock responses; initiate evaluation. |
| F07-006 | Examination Activity Recording | Capture session, timing, responses, version, centre and environment audit data. |

---

### 08. Evaluation, Results and Certificates

**Purpose:** Auto-evaluate objective papers, publish results, issue QR-coded certificates and support public verification.

**Type:** Business

**Functional requirements:**

- Auto-evaluate against answer key: correct/incorrect/unanswered, marks, negative marks if any, total, percentage, pass/fail per configurable rules.  
- Publish result to candidate login per publication rules (name, registration, examination, date, marks, percentage, pass/fail, other approved fields).  
- Generate certificate for eligible/pass candidates; candidate download from portal.  
- Unique certificate number and QR linked to verification token/URL.  
- Maintain certificate number, candidate and examination references, dates, result status, issue date, certificate status, verification token.  
- Public verification page: valid/genuine, invalid/not found, cancelled/revoked if cancellation is enabled; display only approved public fields.  
- Certificate cancellation/revocation if required by Department.

**Acceptance criteria:**

- Objective scoring matches the configured key and rules.  
- Ineligible candidates do not receive a certificate.  
- QR verification returns the correct status for valid and cancelled certificates.  
- Public page does not disclose non-approved personal data.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Automatic Objective Evaluation | Score responses against the answer key with configurable pass and negative-marking rules. |
| F08-002 | Result Publication | Publish results to candidate login per configured publication rules. |
| F08-003 | Certificate Generation and Download | Issue certificates for eligible candidates and allow portal download. |
| F08-004 | QR Code and Public Certificate Verification | Unique QR/token and public page for authenticity verification including cancelled status. |

---

### 09. Dashboards, Reports, Notifications and Audit

**Purpose:** Give administrators operational visibility, exportable reports, stage notifications and a complete audit trail.

**Type:** Shared

**Functional requirements:**

- Administrator dashboard: registrations by type, pending, fee-paid, examination-wise and centre-wise counts, scheduled/completed exams, pass/fail statistics, certificate generation status.  
- Reports: candidate, fee, examination and certificate report families as listed in the source; export Excel/PDF as finally approved.  
- Notifications (SMS / email / portal as configured): registration, payment, status, schedule, allocation, hall ticket, reminders, credentials, result, certificate.  
- Audit logs for registration, data change, KGID verification, document upload, fees, allocation, scheduling, questions, paper generation, exam login/start/submit, results, certificates, cancellations and administrative actions — with user, date/time and activity.

**Acceptance criteria:**

- Dashboard figures reconcile to underlying registration and examination records for a chosen period.  
- Named reports export in approved formats.  
- Critical actions listed in the source appear in the audit trail with actor and timestamp.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Administrator Operational Dashboard | Overall registration, schedule, result and certificate monitoring views. |
| F09-002 | Operational and Statutory Reports | Candidate, fee, examination and certificate reports with approved exports. |
| F09-003 | Candidate and Staff Notifications | Configured SMS, email and portal notifications across the examination lifecycle. |
| F09-004 | System Audit Trail | Audit logging of critical registration, examination, result and certificate activities. |

---

## 7. End-to-End Workflows

### 7.1 Government employee registration

Candidate OTP login → select government type → enter KGID → retrieve and confirm details → additional fields → select examination → select two centre preferences → attempt/eligibility check → fee free or payable → payment if applicable → registration confirmation.

### 7.2 Other organisation registration

Candidate OTP login → select other-organisation type → enter details → download competent-authority format → obtain digital signature → upload document → select examination → select two centre preferences → mandatory fee payment → registration confirmation.

### 7.3 Schedule to hall ticket

Admin verifies/approves registration if applicable → create schedule → allocate centre → generate hall ticket and examination credentials → candidate downloads hall ticket.

### 7.4 Centre examination day

Candidate reports to allotted centre → invigilator verifies identity → authorised environment validated → session activated → candidate logs in with exam credentials → randomised paper (version + order) → exam with timer → submit or auto-submit → responses locked → automatic evaluation → result → certificate (if eligible) → QR verification by third parties.

---

## 8. Access Control

| Principal | Access |
| --------- | ------ |
| Candidate | Own registration, hall ticket, result, certificate via OTP portal; examination only with exam credentials at allotted centre |
| Examination Administrator | Examinations, centres, schedules, registrations, question bank, parameters, monitoring, results, certificates, reports |
| Examination Centre / Invigilator | Only mapped centre’s candidates, sessions, activation and monitoring |
| Public verifier | Certificate verification page only (approved fields) |

Staff access is **role- and centre-scoped**. Candidate portal identity is **mobile OTP**. Examination identity is **system-generated Login ID / Password** for the scheduled session.

---

## 9. Channels

| Channel | Users | Use |
| ------- | ----- | --- |
| Candidate web portal | Candidates | OTP login, registration, payment, hall ticket, result, certificate |
| Administrator web | Examination Administrators | Masters, scheduling, question bank, monitoring, reports |
| Centre web dashboard | Centre / Invigilator users | Verification, activation, attendance, centre monitoring |
| Examination CBT interface | Candidates at centre | Sit the computer-based examination |
| Public verification page | Anyone with QR / token | Certificate authenticity check |
| SMS / Email | Candidates (and staff as configured) | OTP and lifecycle notifications |

No candidate mobile app for sitting the examination is in scope.

---

## 10. Integrations

| Integration | Purpose | Notes |
| ----------- | ------- | ----- |
| KGID system / API | Retrieve government employee details | Subject to API and data availability |
| Payment gateway | Examination fee collection | Success, failure, reference, receipt |
| SMS gateway | OTP and notifications | Channels finalised at confirmation |
| Email | Notifications and credential communication | As configured |
| Digital signature on competent-authority document | Candidate-side signing before upload | Template provided by system; signing outside or as Department directs |

No interface contracts are prescribed in this SOW.

---

## 11. Audit, Compliance & Security

- Audit trail for all critical activities listed in Appendix B and Module 09.  
- Centre-only examination access with session and invigilator controls.  
- OTP controls for portal login; separate exam credentials for CBT.  
- Prevention of multiple simultaneous examination sessions.  
- Certificate uniqueness and revocation-aware public verification.  
- Activity recording of examination environment details where available (device, IP/network, session).

Exact IP/device/secure-browser mechanisms follow Department infrastructure approval while meeting the centre-only business rule.

---

## 12. Non-Functional Requirements

| Area | Expectation |
| ---- | ----------- |
| Availability | Portal and admin available for registration windows; CBT available for scheduled sessions at centres |
| Integrity | Responses locked after submit; answer-key mapping preserved under randomisation |
| Security | Centre-only CBT; OTP and credential controls; role and centre scoping |
| Usability | Clear candidate and centre flows suitable for examination-day operations |
| Export | Reports in Excel/PDF as finally approved |
| Auditability | User, date/time and activity on critical events |

Hosting and capacity sizing are outside this business SOW unless separately ordered.

---

## 13. Data Migration

Legacy migration of prior examination or candidate history is **out of scope** unless the Department later supplies extracts and rules. Attempt history for fee logic may begin from registrations created in this system, unless historical attempt data is formally provided.

---

## 14. Phased Delivery

Indicative single delivery for go-live of the full module, sequenced internally as:

| Phase | Content |
| ----- | ------- |
| Phase A | Access, masters, candidate OTP portal, registration (both types), fee payment, admin verification |
| Phase B | Scheduling, allocation, hall tickets, credentials, question bank and paper versions |
| Phase C | Centre dashboard, authorised-centre CBT, evaluation, results, certificates, QR verification |
| Phase D | Dashboards, reports, notifications hardening, UAT and go-live |

The Department may compress or split phases at contracting; scope remains the modules in Section 6.

---

## 15. Deliverables

1. Configured Examination Module covering Modules 01–09.  
2. Candidate portal, administrator application, centre dashboard and public verification page.  
3. KGID and payment integrations as facilitated.  
4. Competent-authority document template facility.  
5. Question bank and randomised multi-version paper generation.  
6. Centre-only CBT with invigilator activation and activity recording.  
7. Result and QR-certificate issuance with public verification.  
8. Operational dashboards, reports and audit trail.  
9. User documentation and training for administrators and centre users.  
10. UAT support and defect closure for accepted scope.

---

## 16. Acceptance Criteria

1. Government and other-organisation registration paths complete per fee and document rules.  
2. KGID retrieval works for available fields; graceful handling when API fields are missing.  
3. Two preferences captured; allocation and hall ticket show the final centre.  
4. Unauthorised location/device/network access to CBT is denied in agreed test scenarios.  
5. Invigilator activation is required before exam start.  
6. Randomised versions score correctly against the key.  
7. Timer expiry auto-submits; manual submit locks responses.  
8. Pass candidates receive downloadable certificates; QR verification returns valid status.  
9. Cancelled certificate (if enabled) returns cancelled/revoked on verification.  
10. Audit entries exist for registration, payment, exam start/submit, result and certificate events.

---

## 17. Expected Benefits

- End-to-end digital examination lifecycle with less manual paper handling.  
- Correct fee treatment for first vs subsequent government attempts.  
- Stronger integrity through centre-only CBT and randomised papers.  
- Faster objective results and digitally verifiable certificates.  
- Clear operational visibility for administrators and centres.  
- Public trust through QR authenticity checks.

---

## 18. Assumptions & Dependencies

1. **Project code** `EXAM`; display name **Examination Module**; output folder `Projects/Keonics-Exam-Module/`.  
2. Client organisation is **KEONICS / Client Department** as examination authority; exact branding confirmed at contracting.  
3. KGID API access and field catalogue will be provided by the Department / KGID owner.  
4. Payment gateway merchant credentials and settlement account will be provided by the Department.  
5. Authorised centres will provide computers, network and invigilators; software enforces rules against that infrastructure.  
6. Final centre-access technical mechanism (IP, device, secure browser, or combination) will be chosen with the Department without reducing the centre-only business rule.  
7. Examinations in this phase are **objective / auto-evaluable** unless later extended.  
8. Notification channels (SMS / email / portal) finalised during requirement confirmation.  
9. Certificate cancellation is included if the Department requires it; public verification must honour cancelled status.  
10. Document Management and workflow remain **embedded**.  
11. No legacy attempt-history migration unless separately ordered.  
12. Competent-authority digital signing is performed by the candidate’s organisation using the prescribed format; the system stores the uploaded signed file.

---

## 19. Vendor Response Expectations

Vendors should:

1. Confirm coverage of all feature IDs in Appendix A.  
2. Describe the government vs other-organisation registration and fee paths in business terms.  
3. Describe how **centre-only examination access** will be enforced at a business-control level (without prescribing a single technology).  
4. Describe randomisation and multi-version scoring integrity.  
5. Describe QR certificate verification including cancelled status.  
6. List dependencies on KGID, payment and SMS/email gateways.  
7. Not substitute database schemas, API path designs or UI wireframes for the business confirmation above.

This SOW does not contain effort hours.

---

## 20. Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | Access Control and Staff User Management | Shared | F01-001 … F01-002 (2) |
| 02 | Candidate Portal Access (OTP Login) | Shared | F02-001 … F02-002 (2) |
| 03 | Examination, Centre and Fee Masters | Business | F03-001 … F03-004 (4) |
| 04 | Candidate Registration and Fee Payment | Business | F04-001 … F04-006 (6) |
| 05 | Scheduling, Allocation, Hall Tickets and Examination Credentials | Business | F05-001 … F05-004 (4) |
| 06 | Question Bank and Paper Versions | Business | F06-001 … F06-002 (2) |
| 07 | Secure Centre-Based Examination Conduct | Business | F07-001 … F07-006 (6) |
| 08 | Evaluation, Results and Certificates | Business | F08-001 … F08-004 (4) |
| 09 | Dashboards, Reports, Notifications and Audit | Shared | F09-001 … F09-004 (4) |

**Total: 9 modules, 34 feature outlines.**

---

## 21. Appendix B — Key Business Rules

| # | Business Rule |
| - | ------------- |
| 1 | Candidate portal login shall be through OTP. |
| 2 | KGID Number shall be mandatory for Government Department Employees. |
| 3 | KGID details shall be retrieved through integration, subject to API/data availability. |
| 4 | Candidate shall confirm retrieved KGID information before proceeding. |
| 5 | Government employees shall receive free registration for the first attempt. |
| 6 | Fee shall be applicable for subsequent attempts by Government employees. |
| 7 | Fee shall be mandatory for eligible non-government organisation candidates. |
| 8 | Non-government organisation candidates shall upload digitally signed competent-authority confirmation. |
| 9 | Candidates shall select two preferred examination centres. |
| 10 | Final centre allocation shall be controlled by the examination administrator/system. |
| 11 | Hall ticket shall be available only after examination scheduling/allocation. |
| 12 | Examination shall be accessible only from authorised examination centres. |
| 13 | Candidate shall be allowed to take the examination only in the assigned examination session/centre. |
| 14 | Question selection shall be randomised from the question bank. |
| 15 | Multiple question paper versions shall be supported. |
| 16 | Question order shall be randomised. |
| 17 | Answer option order shall also be randomised. |
| 18 | Candidate responses shall be recorded and securely stored. |
| 19 | Examination shall automatically submit after the configured duration. |
| 20 | Results shall be generated based on configured evaluation rules. |
| 21 | Eligible candidates shall receive certificates through their login. |
| 22 | Certificates shall contain a unique QR code. |
| 23 | QR code shall enable online certificate authenticity verification. |
| 24 | All critical examination activities shall be audit logged. |

---

## 22. Appendix C — Key Entities

| Entity | Meaning |
| ------ | ------- |
| Candidate | Person registering and appearing for an examination |
| KGID | Government employee identity used for Type 1 registration |
| Examination | Named exam open for registration and later scheduling |
| Examination centre | Authorised venue with capacity and centre users |
| Registration / application | Candidate’s application for a specific examination |
| Centre preference | Candidate’s first and second preferred centres |
| Hall ticket | Digital admit card after schedule and allocation |
| Examination credentials | System-generated Login ID and Password for CBT |
| Question bank | Pool of questions used to build papers |
| Paper version | Randomised instance (e.g. A/B/C/D) of a paper |
| Examination session | Scheduled sitting at a centre |
| Result | Scored outcome and pass/fail |
| Certificate | Issued credential with unique number and QR |

---

## 23. Appendix D — Mapping from Source Outline

| Source sections (indicative) | This SOW module |
| ---------------------------- | --------------- |
| 3.2–3.3 Staff users | 01 |
| 4 Candidate OTP login | 02 |
| 15–17, 9, 26 Masters, centres, fees, configuration | 03 |
| 5–14 Registration, document, payment, confirmation | 04 |
| 15–16, 21 Scheduling, hall ticket, credentials | 05 |
| 23–25 Question bank and versions | 06 |
| 18–22, 27–31, 38, 45 Centre CBT and security | 07 |
| 32–37 Evaluation, results, certificates, QR | 08 |
| 39–42 Dashboards, reports, notifications, audit | 09 |
| 43–44 End-to-end flow and business rules | Sections 7 and Appendix B |

---

**End of Statement of Work**
