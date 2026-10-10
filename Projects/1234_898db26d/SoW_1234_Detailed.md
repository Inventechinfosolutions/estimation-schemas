# SoW 1234 — Detailed Statement of Work

**Project name:** test1

## Introduction
The Examination Module provides an end-to-end digital platform for candidate registration, examination scheduling, hall ticket generation,
secure computer-based examination conduct, evaluation, result publication, certificate generation, and online certificate verification.
The system supports Government Department Employees and employees of PSUs, Boards, Corporations, Societies and other eligible organisations.
Examinations shall be accessible only from authorised examination centres configured and approved by the department.

## Project Overview
Project **test1** delivers the Examination Module capabilities described in the source functional specification,
including OTP-based candidate access, KGID-assisted government employee registration, fee management, centre allocation,
question bank management with randomised papers, secure CBT delivery, and QR-enabled certificate verification.

## Project Objectives
- Provide secure candidate login using OTP.
- Enable online examination registration for government and other organisation candidates.
- Integrate with KGID for government employee detail retrieval.
- Support examination fee rules including first-attempt free registration for government employees.
- Facilitate examination scheduling, centre allocation and digital hall tickets.
- Conduct secure computer-based examinations only at authorised centres.
- Generate results and digitally verifiable certificates with QR codes.
- Provide dashboards, reports and audit trails for administration and centres.

## In Scope / Out of Scope
### In Scope
- Functional modules listed in Section 6 (Consolidated Functional Modules).
- Candidate portal, administrator and examination centre user roles.
- KGID integration, payment gateway integration and notification channels as configured.
- Competent authority document template download and upload for non-government candidates.
- Authorised centre access enforcement as agreed with the department.

### Out of Scope
- Detailed API contracts, database schemas and UI wireframes (addressed in design, not in this SOW).
- Hosting infrastructure, hardware procurement and annual maintenance unless separately ordered.
- Classroom training and scanning bureau services unless separately ordered.
- Legacy data migration unless explicitly added to scope.

## Solution Expectations (Business-level Only)
- Configurable examinations, fees, evaluation rules and centre masters.
- Secure examination conduct with activity recording and audit logging.
- Role-scoped dashboards and exportable operational reports.

## Consolidated Functional Modules

### 01. User and Role Management
**Purpose:** Manage examination administrators, centre or invigilator users, roles and permissions.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F01-001 | User register and onboarding for admin and centre roles | Create and maintain staff and centre user accounts used by administration and centre operations |
| F01-002 | Role-to-permission mapping for examination operations | Define roles for Examination Administrator, Centre or Invigilator user and map functional permissions |
| F01-003 | Staff authentication and session handling | Secure login, session timeout and logout for administrator and centre channels |


### 02. Examination Configuration
**Purpose:** Configure examinations, registration windows, fee rules, evaluation rules and examination parameters.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F02-001 | Exam catalogue and open registration control | Maintain examinations open for registration with schedules and descriptive details |
| F02-002 | Fee and attempt eligibility configuration | Configure first-attempt free rules for government employees, subsequent attempt fees and mandatory fees for other categories |
| F02-003 | Evaluation and conduct parameter setup | Configure scoring, negative marking, pass criteria, duration, security options and paper parameters |


### 03. Candidate Access and Registration
**Purpose:** OTP-based candidate login and end-to-end registration for government and other organisation candidates.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F03-001 | Mobile OTP login for candidates | Candidates access the portal using mobile OTP with expiry, retry limits and session timeout |
| F03-002 | KGID-driven government employee registration | Government department employees register using mandatory KGID with retrieved employee details and confirmation |
| F03-003 | Manual registration for other organisation employees | Manual capture of candidate and employment details for PSU, Board, Corporation, Society and other eligible organisations |
| F03-004 | Competent authority template and upload | Download prescribed competent authority format, upload digitally signed confirmation and associate with registration |
| F03-005 | Exam and dual centre preference capture | Select examination and two preferred examination centres during registration |


### 04. Fee and Payment
**Purpose:** Determine applicable fees and collect payments where registration is not free.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F04-001 | Fee presentation and payment initiation | Present applicable fee, initiate payment for paid registrations and confirm successful payment before registration completion |
| F04-002 | Payment reconciliation register | Administrator views fee-paid, free and failed transactions for operational reconciliation |


### 05. Scheduling Allocation and Hall Ticket
**Purpose:** Schedule examinations, allocate centres and issue digital hall tickets.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F05-001 | Examination schedule planning | Plan examination dates, sessions and capacity-linked schedules |
| F05-002 | Centre allocation against preferences | Allocate candidates to examination centres using preferences, capacity and business rules |
| F05-003 | Digital hall ticket issuance | Generate digital hall tickets after scheduling and allocation with candidate and centre details |


### 06. Examination Centre Management and Enforcement
**Purpose:** Manage authorised centres, enforce centre-only access and support invigilator session activation.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F06-001 | Examination centre master data | Maintain authorised examination centres, capacity and centre user mapping |
| F06-002 | Centre-only access validation | Validate candidate, centre, device or network and session before examination access is granted |
| F06-003 | Invigilator session activation | Centre or invigilator user verifies candidate, activates examination session and monitors status |


### 07. Question Bank and Paper Generation
**Purpose:** Maintain question banks and generate randomised papers with multiple versions.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F07-001 | Question bank administration | Create and maintain questions with categories, difficulty and status for examinations |
| F07-002 | Randomised multi-version papers | Generate examination papers with random question selection and multiple versions such as A/B/C/D |
| F07-003 | Order randomisation controls | Randomise question order and answer option order per candidate paper |


### 08. Computer-Based Examination Conduct
**Purpose:** Issue examination credentials, deliver secure CBT interface with timer, record activity and handle submission.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F08-001 | Examination credential lifecycle | Generate system examination credentials and authenticate candidate for the assigned session |
| F08-002 | CBT delivery and timer | Present questions, capture responses and enforce configured examination duration with auto-submit |
| F08-003 | Security logging and submission | Record examination activity, apply security controls and process manual or automatic submission |


### 09. Results Certificates and Verification
**Purpose:** Evaluate responses, publish results, generate QR-enabled certificates and provide public verification.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F09-001 | Evaluation and result views | Score responses per configured rules and publish results to candidate login when allowed |
| F09-002 | Certificate issuance with QR | Generate downloadable certificates for eligible candidates embedding unique QR verification reference |
| F09-003 | Public QR verification | Public verification page validates certificate token from QR scan and shows approved disclosure |


### 10. Dashboards Reports and Audit
**Purpose:** Administrator and centre dashboards, operational reports and audit trail inquiry.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F10-001 | Administrator operational dashboard | Overall view of registrations, schedules, outcomes and certificate status |
| F10-002 | Centre dashboard | Centre-specific view of today's examinations, attendance and session status |
| F10-003 | Standard report catalogue | Candidate, fee, examination, result and certificate reports with export to Excel or PDF |
| F10-004 | Audit log inquiry | Capture and inquire audit logs for critical activities listed in the SOW |


### 11. Integrations and Notifications
**Purpose:** KGID employee lookup, payment gateway and multi-channel notifications to candidates and staff.

**Functional requirements:**
- Deliver the capabilities outlined in the Key capabilities table for this module.
- Enforce role-based access for candidates, administrators and centre users.
- Record critical activities for audit where applicable.

**Acceptance criteria:**
- Module capabilities operate per the Examination Module business rules in the source document.
- Unauthorized users cannot access other centres' or candidates' data.
- Outputs (hall tickets, results, certificates) reflect approved configuration and allocation.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F11-001 | KGID lookup integration | Integrate with KGID to retrieve government employee details during registration |
| F11-002 | Payment gateway adapter | Integrate with configured payment gateway for registration fee collection and callback handling |
| F11-003 | Multi-channel notifications | Send SMS, email and portal notifications for registration, payment, schedule, hall ticket, credentials, results and certificates |


## End-to-End Workflows
- Candidate OTP login → registration (government KGID path or other organisation path) → examination and centre preference → fee (if applicable) → confirmation.
- Scheduling → centre allocation → hall ticket → candidate reports to allotted authorised centre → verification and session activation.
- Examination credentials → secure CBT → submission → evaluation → result → certificate with QR → public verification.

## Access Control / RBAC
Candidate access is via OTP to the candidate portal. Examination Administrator users manage configuration, registrations, scheduling, question banks and results.
Centre or Invigilator users access centre-scoped functions only. Public users access certificate verification without login.
Registration verification or approval applies only where the department requires administrator review of non-government registrations.

## Channels
- Candidate web portal (OTP login).
- Examination Administrator web console.
- Examination centre / invigilator web interface.
- Public certificate verification page (QR landing).

## Integrations
- KGID system for government employee detail retrieval.
- Payment gateway for registration fee collection.
- SMS and email (and portal notifications) for candidate and operational alerts.

## Audit, Compliance & Security
- Audit trail for critical activities listed in the source specification.
- Examination security controls, activity recording and centre-only access enforcement.
- Unique certificate identifiers and QR verification.

## Non-Functional Requirements
- Availability during scheduled examination windows.
- Secure handling of candidate data, responses and certificates.
- Performance suitable for concurrent candidates at multiple centres.

## Data Migration
Legacy data migration is out of scope unless separately agreed.

## Phased Delivery
- Phase 1: Access, examination configuration and candidate registration (Modules 01–03).
- Phase 2: Fees, scheduling, hall tickets and centre management (Modules 04–06).
- Phase 3: Question bank, CBT conduct and results or certificates (Modules 07–09).
- Phase 4: Dashboards, reports, audit and integrations (Modules 10–11).

## Deliverables
- Configured Examination Module application covering in-scope capabilities.
- Administrator, centre and candidate-facing functions per this SOW.
- Operational and user documentation for handover.

## Acceptance Criteria (Program Level)
- End-to-end examination lifecycle operates per business rules in the source document.
- Candidates cannot attempt examinations outside allotted authorised centres and sessions.
- Certificates verify correctly through the public QR verification page.

## Expected Benefits
- Digitised registration and examination conduct with reduced manual processing.
- Improved integrity through randomised papers and centre enforcement.
- Verifiable digital certificates for stakeholders.

## Assumptions & Dependencies
- KGID and payment gateway interfaces are available for integration testing.
- Authorised centre enforcement mechanism is agreed with the department.
- Notification channels (SMS/email) are provisioned by the department or vendor as agreed.

## Vendor Response Expectations
- Deliver the in-scope modules with production-quality validation, security and audit logging.
- Propose centre enforcement approach aligned to department infrastructure.

## Appendices
- Appendix A — Module & Feature Index (summary).

| Module | Module Name | Type | Feature IDs (count) |
|---|---|---|---|
| 01 | User and Role Management | Shared | F01-001, F01-002, F01-003 (3) |
| 02 | Examination Configuration | Business | F02-001, F02-002, F02-003 (3) |
| 03 | Candidate Access and Registration | Business | F03-001, F03-002, F03-003, F03-004, F03-005 (5) |
| 04 | Fee and Payment | Business | F04-001, F04-002 (2) |
| 05 | Scheduling Allocation and Hall Ticket | Business | F05-001, F05-002, F05-003 (3) |
| 06 | Examination Centre Management and Enforcement | Business | F06-001, F06-002, F06-003 (3) |
| 07 | Question Bank and Paper Generation | Business | F07-001, F07-002, F07-003 (3) |
| 08 | Computer-Based Examination Conduct | Business | F08-001, F08-002, F08-003 (3) |
| 09 | Results Certificates and Verification | Business | F09-001, F09-002, F09-003 (3) |
| 10 | Dashboards Reports and Audit | Business | F10-001, F10-002, F10-003, F10-004 (4) |
| 11 | Integrations and Notifications | Technical | F11-001, F11-002, F11-003 (3) |
