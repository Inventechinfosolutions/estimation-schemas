# Scope of Work (Detailed) — Online Computer Literacy Test (CLT) and Digital Certification System

**Client:** Karnataka State Electronics Development Corporation Limited (KEONICS)  
**On behalf of:** Center for E-Governance, Department of Personnel and Administrative Reforms, Government of Karnataka  
**Source:** RFP KEONICS/2026-27/SE0140/Call-3 — Selection of Service Provider for Design, Development, Implementation and Maintenance of Online Computer Literacy Test (CLT) and Digital Certification System  
**Project code:** CLT  
**Prepared:** 2026-10-14

## 1. Introduction

The Government of Karnataka requires every state government employee to pass the Computer Literacy Test (CLT) during probation or within the prescribed period. More than five lakh employees fall under the rule, with about 15,000 new recruits every year. KEONICS, on behalf of the Center for E-Governance (DPAR), is procuring a Service Provider to design, develop, implement and maintain an end-to-end online CLT and digital certification system hosted at the Karnataka State Data Centre (SDC).

This document converts the RFP Terms of Reference, Annexure 1 (technical requirements) and the Special Conditions of Contract into a structured scope of 18 modules and 90 features for estimation and delivery planning.

## 2. Programme Overview

| Item | Detail |
|------|--------|
| Candidates | Government employees (with or without KGID) and prospective candidates (new appointees, board and corporation staff) |
| Volume | About 25,000 registrations in 2026 and 20,000 in 2027; 15,000 new employees per year thereafter |
| Test pattern | Part 1: 60 MCQs across 12 topics (60 marks). Part 2: English and Kannada typing tests (20 marks each). 90 minutes; 50% to qualify |
| Sessions | Four sessions per day with an optional fifth; working Saturdays for employees and Sundays for prospective candidates |
| Concurrency | At least 2,000 concurrent candidates per session |
| Hosting | Karnataka State Data Centre only; no local database at test centres |
| Proctoring | Continuous screen and webcam video recording with automated monitoring and real-time alerts |
| Certificates | Digitally signed, watermarked, QR-verifiable certificates; results updated in HRMS |
| Contract | Development and go-live by T + 3 months, 12-month warranty, then comprehensive AMC for 3 years |

## 3. Objectives

1. Conduct a fair, secure and fully online CLT with registration, booking, testing, evaluation and certification in one system.
2. Validate identity through HRMS (KGID) or Aadhaar eKYC and at the centre through hall ticket, photo and biometric checks.
3. Keep the question bank confidential through maker-checker workflow, component segregation and AES-256 encryption with HSM keys.
4. Deliver unique jumbled papers per candidate with immediate scoring and tamper-proof digital certificates.
5. Give KEONICS and competent authorities real-time monitoring, complete audit trails and MIS.
6. Meet performance (2,000 concurrent, under one second on LAN), availability (99.9%) and Safe-to-Host requirements.

## 4. Scope Summary

### In scope

- Design, development, testing, deployment at SDC and go-live of all modules listed in Section 6
- Web portal at clt.karnataka.gov.in and candidate mobile application (Android and iOS)
- Content Authoring Tool, question bank workflow and question paper generation
- Test centre console, secure exam client, online examination engine with typing tests
- Screen and webcam video proctoring with automated monitoring
- Integrations: HRMS, Aadhaar authentication and eKYC, payment gateway, SMS and e-mail, HSM, DSC / e-Sign
- Porting of legacy CLT data
- Warranty for 12 months after go-live and comprehensive AMC for three years

### Out of scope / provided by others

- SDC infrastructure (servers, storage, network, backup media) — provided by the State Data Centre
- Test centre premises, terminals, webcams, network and seating — arranged by KEONICS and centres
- Licences and transaction charges of third-party services (payment gateway, SMS, Aadhaar, e-Sign)
- Re-evaluation of answer scripts (not permitted under the RFP)

### Service line items (quoted separately from software features)

- Question content creation by Subject Matter Experts (at least 2,000 questions at launch, 5% growth per year)
- Need-based offsite helpdesk with dedicated numbers
- Annual Safe-to-Host audit by a CERT-In empanelled auditor and SSL certificates
- Training, user manuals and how-to videos; exit management and knowledge transfer

## 5. Users and Roles

| Role | Responsibility |
|------|----------------|
| Candidate | Registers, books, pays, takes mock and main tests, downloads results and certificates |
| Registration Centre Operator | Registers prospective candidates at designated centres and captures photographs |
| Scrutiny Officer | Validates registrations and support requests |
| SME Author / Reviewer / Technical Committee | Authors, reviews and approves questions |
| Question Bank Administrator | Manages blueprint, banks and paper generation |
| Proctor / Centre Operator | Runs sessions, validates candidates, handles incidents |
| Examination Monitoring Unit | Monitors all centres live and takes control actions |
| Result Officer / KEONICS Approver | Finalises results and approves certificate issue |
| Finance Officer | Reconciles fees and approves refunds |
| Helpdesk Executive | Logs calls and makes outbound calls |
| KEONICS Administrator / Super Admin | Configures the system and manages users |

## 6. Functional Scope by Module

### 01. Access Control & Staff User Management

**Type:** Shared · **RFP reference:** RFP 4.4.17, 4.6.1.3

**Purpose:** Control access for KEONICS, Center for E-Governance, district, centre, question bank and support users, and restrict each user to the data and actions permitted to the role.

**Functional requirements:**

- Secure staff login with password policy, OTP and session controls
- User management for all staff roles with mapping to district, test centre and question bank function
- Permission matrix configurable without code changes; data scope by district and centre
- Strict separation of question bank roles so that no single person sees all components of a question except its author

**Acceptance criteria:** Each role sees only permitted menus, actions and records; question bank segregation is enforced on every screen, export and API.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F01-001 | Staff Authentication & Session Security | Login for KEONICS, CeG, district, centre and question bank users with password policy, OTP, lockout and secure sessions |
| F01-002 | Staff User, Role & Centre Mapping | Create and maintain staff accounts with roles and district, test centre and question bank function mapping |
| F01-003 | Permission Matrix & Data Scope | Configurable role permissions and district / centre data scope enforced on every screen, report and export |

### 02. Examination Configuration & Masters

**Type:** Business · **RFP reference:** RFP 4.4.3, 4.4.7, 4.4.9–4.4.12

**Purpose:** Allow KEONICS to change the examination pattern, centres, sessions and fees without code changes and preserve the configuration used for each test session.

**Functional requirements:**

- Syllabus, topics, marks and weightage configurable with a snapshot preserved against each test session
- Test centre master with seats, terminals, address, contact person and district
- Session calendar: working Saturdays for employees, Sundays for prospective candidates, 4 sessions per day with an optional 5th, one session per centre at a time
- Minimum batch size per session
- Fee rules: free first attempt for government employees, fees for later attempts and for prospective candidates
- Bilingual templates for hall ticket, certificate, notices and messages
- Reference masters: departments, designations, districts, document types, holidays

**Acceptance criteria:** Changes to syllabus, sessions or fees apply only to sessions created after approval; every session carries its configuration snapshot.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F02-001 | Syllabus, Marks & Weightage Configuration | Configure Part 1 topics, Part 2 typing tests, marks, weightage, duration and qualifying marks with a snapshot per session |
| F02-002 | Test Centre, Seat & Terminal Master | Test centres by district with address, contact, seats, terminals, IP / device registration and status |
| F02-003 | Session Calendar & Batch Rules | Session slots by day and centre, Saturday employee and Sunday prospective batches, 5th session, minimum batch size |
| F02-004 | Fee Rule Configuration | Fee by category and attempt number, first attempt free for government employees, effective-dated with approval |
| F02-005 | Document & Certificate Template Management | Bilingual templates for hall ticket, certificate, score card, notices and reports with approval |
| F02-006 | Reference Masters | Departments, boards and corporations, designations, districts, document types, malpractice categories, holidays |

### 03. CLT Web Portal & Mobile Application

**Type:** Business · **RFP reference:** RFP 4.5.3, 4.5.5.3, 4.3.3.1.6–7

**Purpose:** Provide the public face of the CLT with information, study material and access to registration and booking on web and mobile.

**Functional requirements:**

- Information on test details, schedules, registration and test centre addresses, contact persons and telephone numbers
- Download of study material and notices
- Kannada and English content; device, operating system and browser agnostic
- Mobile application for faster registration and booking
- Published helpdesk numbers

**Acceptance criteria:** Portal and mobile application work on smartphones, tablets, laptops and desktops on current browsers in both languages.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F03-001 | Public Information Portal | clt.karnataka.gov.in with test details, schedules, centres, contacts, helpdesk numbers and links to registration and mock test |
| F03-002 | Portal Content & Study Material Management | Manage pages, announcements, FAQs, notices and downloadable study material with approval |
| F03-003 | Bilingual, Responsive & Device-Agnostic Design | Kannada–English toggle, responsive layouts and compatibility across smartphones, tablets, laptops, desktops, operating systems and browsers |
| F03-004 | Candidate Mobile Application | Android and iOS application for registration, booking, payment, hall ticket, mock test, results and certificates |

### 04. Candidate Registration & eKYC

**Type:** Business · **RFP reference:** RFP 4.4.8, 4.4.15, 4.5.5, 4.2.2.5

**Purpose:** Capture complete and verified candidate details for government employees and prospective candidates.

**Functional requirements:**

- Existing employees: KGID, name, posting, photograph, contact and date of birth, with data fetched from HRMS
- Prospective candidates and employees without KGID: name, parents' names, Aadhaar, address, contact, date of birth, photo, appointment letter, signature and eKYC
- Prospective candidates register through designated centres where the photograph is taken
- Validation of metadata and acceptance or rejection of registrations
- Support for differently abled candidates with scribe, guardian or helper as per the Government Order

**Acceptance criteria:** No registration completes without HRMS validation (KGID) or eKYC (others); duplicate and fake registrations are blocked.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F04-001 | Candidate OTP Login & Account | Candidate account with mobile and e-mail OTP, profile, consent and single account per person |
| F04-002 | Government Employee Registration with KGID & HRMS Validation | KGID-based registration with HRMS fetch of name, posting, date of birth and contact, photo upload and declaration |
| F04-003 | Prospective Candidate & Non-KGID Registration with eKYC | Registration with Aadhaar eKYC for prospective candidates and employees without KGID, with parents' names, address, appointment letter and signature |
| F04-004 | Centre-Assisted Registration & Photo Capture | Registration at designated centres with live webcam photo, document scanning and operator attestation |
| F04-005 | Registration Scrutiny & Metadata Validation | Automatic metadata checks and scrutiny queue to accept, reject or return registrations with reasons |
| F04-006 | Differently-Abled Candidate Support Requests | Requests for scribe, guardian, helper and extra time as per Government Order with certificate verification |

### 05. Online Test Booking, Fees & Hall Ticket

**Type:** Business · **RFP reference:** RFP 4.4.7, 4.4.10–4.4.13, 4.5.3.1, 4.5.5.4–4.5.5.8, 4.6.1.6

**Purpose:** Let candidates book date, session and centre, pay fees where applicable and receive a hall ticket, while managing batch sizes and rescheduling as per rules.

**Functional requirements:**

- Booking by availability of seats, with colour-coded available and full slots
- Fee based on category and attempt number; payment by UPI / UPI-QR, net banking, credit and debit card
- Hall ticket with barcode and payment receipt details, without photograph, sent by e-mail and SMS
- Rescheduling once, at least one week in advance, online self-service only; no cancellation
- Below the minimum batch size, forced rescheduling with e-mail, SMS and helpdesk calls
- No mixing of employees and prospective candidates in a session; Sunday batches can move to Saturday

**Acceptance criteria:** Seats are never over-booked; fees match attempt history; every forced reschedule is communicated and acknowledged.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F05-001 | Online Test Booking & Slot Availability | Book date, session and centre from colour-coded availability with seat locking and category rules |
| F05-002 | Attempt-Based Fee Calculation & Online Payment | Fee from category and attempt history; payment by UPI / UPI-QR, net banking, credit and debit card |
| F05-003 | Payment Receipt, Reconciliation & Exceptions | Receipts, daily settlement reconciliation, exceptions for unmatched or pending payments and refund records |
| F05-004 | Hall Ticket with Barcode & Receipt | Hall ticket with barcode, session, centre, seat, payment receipt details and instructions; no photograph; e-mail and SMS dispatch |
| F05-005 | Candidate Self-Service Rescheduling | One-time online rescheduling at least one week before the test, within category rules, with new hall ticket |
| F05-006 | Minimum Batch Check & Forced Rescheduling | Detect sessions below minimum batch size, move candidates to other sessions and notify by e-mail, SMS and helpdesk calls; Sunday-to-Saturday conversion |

### 06. Question Bank & Content Authoring Tool

**Type:** Business · **RFP reference:** RFP 4.3.2, 4.4.5, 4.5.6

**Purpose:** Create and maintain secure, approved, bilingual question banks that follow the syllabus weightage.

**Functional requirements:**

- Guidelines for question types, pattern and difficulty approved by the Technical Committee
- Content Authoring Tool for SMEs supporting text, image, formula and practical / simulation questions in Kannada and English
- Maker-checker: author creates, reviewer approves; Technical Committee reviews every item
- No single person except the author sees all components of a question
- Field test and difficulty calibration where required
- Import from Excel / CSV without double data entry
- Separate mock and main question banks; at least 2,000 questions at launch, growing 5% a year; quarterly reports
- Typing test passages in English and Kannada

**Acceptance criteria:** Only Technical Committee approved items enter the bank; component segregation and encryption are demonstrable.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F06-001 | Question Paper Guidelines & Blueprint | Guidelines on question types, pattern and difficulty, and the blueprint of questions per topic and difficulty approved by the Technical Committee |
| F06-002 | Bilingual Rich-Content Question Authoring | Content Authoring Tool for text, image, formula and practical / simulation questions in Kannada and English with metadata |
| F06-003 | Maker-Checker & Technical Committee Approval | Reviewer verification of language, accuracy and difficulty, then Technical Committee approval before an item enters the bank |
| F06-004 | Question Component Segregation & Bank Privacy | Separation of stem, options, answer key and media so that no one but the author sees all components; encrypted bank and access logging |
| F06-005 | Field Test & Difficulty Calibration | Pilot of items with sample candidates and statistical calibration of difficulty and discrimination, if required by KEONICS |
| F06-006 | Excel / CSV Question Import | Bulk import of questions and metadata from Excel / CSV with validation and no double data entry |
| F06-007 | Mock & Main Question Bank Management | Separate mock and main banks, item status, usage and exposure control, retirement, bank strength and growth tracking |
| F06-008 | Typing Test Passage Management | English and Kannada typing passages with length, difficulty and keyboard layout, reviewed and approved |

### 07. Question Paper Generation & Mock Test

**Type:** Business · **RFP reference:** RFP 4.5.4, 4.5.6.6.5, 4.5.6.6.7

**Purpose:** Produce secure, unique papers for each session and give candidates realistic practice.

**Functional requirements:**

- 60 questions chosen randomly from the bank by weightage and difficulty; one set per session
- Jumbling of questions and choices so that no two papers share the same sequence
- Paper not viewable by anyone except candidates taking the test
- Mock test of 25 questions, 30 minutes, unlimited attempts, active 7 to 15 days before the test until test start

**Acceptance criteria:** Every candidate paper is unique in sequence; paper content is unreadable before session start; mock tests mirror the real interface.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F07-001 | Weightage & Difficulty-Based Paper Generation | Random selection of 60 questions per session by topic weightage and difficulty mix, with exposure rules and committee lock |
| F07-002 | Question & Option Jumbling per Candidate | Unique question order and option order for every candidate with mapping stored for evaluation |
| F07-003 | Sealed Paper Storage & Session Release | Encrypted paper storage with keys released only at session start for authorised centres and candidates |
| F07-004 | Mock Test Engine | Mock test of 25 questions in 30 minutes from the mock bank, unlimited attempts, open 7–15 days before until test start |

### 08. Test Centre Operations & Candidate Validation

**Type:** Business · **RFP reference:** RFP 4.4.14, 4.4.16, 4.4.17, 4.5.9, 4.6.8

**Purpose:** Run each session at the test centre with verified proctors and candidates and complete records.

**Functional requirements:**

- Proctor designated by the Deputy Commissioner and KEONICS for every session, with authentication and attendance
- Sanity check that all candidates for the centre are available and status to the Central Control Subsystem
- Validation by hall ticket, employee card, certified photograph and HRMS data; digital photograph at the centre
- Biometric data with logs
- Designated seat per candidate; hall ticket number entered before login
- Upload of scanned commission copy of admission certificates and attendance sheets

**Acceptance criteria:** No candidate starts without validation and seat; every session has an authenticated proctor and complete attendance.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F08-001 | Proctor Management, Authentication & Attendance | Proctor register with designation by Deputy Commissioner and KEONICS, session assignment, OTP / biometric authentication and attendance |
| F08-002 | Centre Readiness Check & Session Start | Pre-session sanity check of terminals, network and candidates, status to central control and proctor-initiated session start |
| F08-003 | Candidate Identity Validation & Photo Capture | Hall ticket barcode scan, check against employee card, certified photo and HRMS data, and live photo capture at the centre |
| F08-004 | Biometric & Aadhaar Authentication at Centre | Fingerprint or face authentication with Aadhaar or registered biometric, storing biometric logs |
| F08-005 | Seat Allocation & Hall Ticket Login Control | Random seat allocation to working terminals, seat display, and terminal login only with hall ticket number at the assigned seat |
| F08-006 | Attendance Sheets, Scans & Centre Incident Records | Digital attendance, printable attendance sheet, upload of scanned admission certificates and attendance sheets, and centre incident log |

### 09. Online Examination Engine

**Type:** Business · **RFP reference:** RFP 4.3.3.1.4, 4.4.4, 4.4.6, 4.4.18–4.4.23, 4.5.9

**Purpose:** Deliver the 90-minute test of 60 MCQs and a 40-mark typing test reliably to up to 2,000 candidates per session.

**Functional requirements:**

- Language choice before login; hall ticket number and credentials
- Rendering of text, image, formula and practical / simulation items; answer in any order, revisit and modify
- Clock from SDC server time; no compensation for late entry; compensation for disruptions
- Typing test in English and Kannada for 40 marks after the MCQ section
- All answers stored centrally with integrity protection
- Early exit allowed; score displayed immediately
- Device, operating system and browser agnostic

**Acceptance criteria:** 2,000 concurrent candidates per session without degradation; no answer lost on disruption; score shown at submission.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F09-001 | Secure Test Login & Language Selection | Language choice before login, hall ticket number and password at the assigned terminal, instructions and candidate confirmation |
| F09-002 | Rich MCQ Delivery & Navigation | Rendering of text, image, formula and simulation items with question palette, mark for review, any-order answering and revisit |
| F09-003 | Server-Synchronised Timer & Disruption Compensation | Timer from SDC server time, no compensation for late entry, automatic compensation for disruptions and extra time for supported candidates |
| F09-004 | English & Kannada Typing Test | Part 2 typing tests in English and Kannada with passage display, keystroke capture, speed and accuracy calculation |
| F09-005 | Response Autosave & Answer Integrity | Every answer saved centrally on change with sequence numbers, offline buffer, resume on another terminal and tamper-proof response log |
| F09-006 | Submission, Early Exit & Immediate Score | Submission summary, early exit, auto-submit at time end and immediate display of score and qualifying status |
| F09-007 | Secure Exam Client & Device Compatibility | Lockdown exam browser / kiosk client for Windows, Linux and macOS with web fallback, version control and terminal registration |

### 10. Screen Proctoring & Malpractice Management

**Type:** Business · **RFP reference:** RFP 4.3.3.1.5

**Purpose:** Track and monitor candidate actions throughout the test and produce evidence-based malpractice reports.

**Functional requirements:**

- Continuous screen proctoring with background screen recording
- Automated webcam monitoring
- Browser activity tracking and immediate tab / window switch detection
- Real-time suspicious activity alerts
- Automatic logging of flagged behaviour and comprehensive malpractice reports

**Acceptance criteria:** Every session has screen and webcam recordings for each candidate; flags appear to the proctor in real time; malpractice reports include evidence.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F10-001 | Continuous Screen Recording | Background screen video recording of every candidate terminal for the full session, chunked upload to SDC storage |
| F10-002 | Webcam Recording & Automated Monitoring | Webcam video recording with automated detection of no face, multiple faces, face mismatch, looking away and mobile phone |
| F10-003 | Browser Activity & Tab-Switch Detection | Detection of focus loss, tab / window switch, blocked shortcuts, multiple monitors and external devices, with configurable responses |
| F10-004 | Real-Time Suspicious Activity Alerts | Live alert stream to proctors and the Examination Monitoring Unit with severity, evidence snapshot and acknowledgement |
| F10-005 | Malpractice Case Management & Reports | Malpractice cases from alerts and proctor reports, evidence bundle, committee decision, result withholding and comprehensive reports |
| F10-006 | Recording Storage, Playback & Retention | Indexed storage of screen and webcam recordings, secure playback with event timeline, retention and purge rules |

### 11. Evaluation, Results & Digital Certification

**Type:** Business · **RFP reference:** RFP 4.2.3.7, 4.3.6.3.2, 4.4.19, 4.4.24–4.4.26, 4.5.8.3, 4.6.1.4

**Purpose:** Evaluate tests, finalise results and issue tamper-proof digital certificates to qualifying candidates.

**Functional requirements:**

- Immediate scoring; 50% qualifying marks; negative marking (desirable)
- Candidate challenge of answer keys; re-evaluation not permitted
- Rank list or pass / fail at the end of tests; final scores digitally signed by the Service Provider and submitted to the Client
- Digitally signed qualifying certificate with watermark and anti-duplication features, issued through the portal per approved workflow
- Results and certificates updated in HRMS

**Acceptance criteria:** Scores match the answer key; certificates are signed, verifiable and pushed to HRMS.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F11-001 | Automatic MCQ & Typing Evaluation | Evaluation using answer key mapping, optional negative marking, typing marks and qualifying status at 50% |
| F11-002 | Answer Key Challenge | Candidate challenge of answer keys within a window, SME / committee review, key correction and re-computation; no re-evaluation |
| F11-003 | Result Finalisation & Signed Submission | Session result finalisation, rank list or pass / fail list, digitally signed result file to KEONICS and result publication |
| F11-004 | Digitally Signed Certificate Generation | Bilingual certificate with watermark, QR, unique number and digital signature for qualified candidates |
| F11-005 | Certificate Issue Workflow & Download | Approval-based issue of certificates, portal and app download, and push of results and certificates to HRMS |
| F11-006 | Public Certificate Verification | Public verification by certificate number or QR scan showing validity, holder and issue details |

### 12. Central Monitoring Centre & Examination Monitoring Unit

**Type:** Business · **RFP reference:** RFP 4.2.3.5, 4.4.21, 4.5.8, 4.3.4.2.3–4.3.4.2.4

**Purpose:** Give KEONICS and the Examination Monitoring Unit live control and visibility of every session.

**Functional requirements:**

- Real-time status of all test centres and test progress for KEONICS and competent authorities
- Exam-day control: start, hold, resume, extend time for disruptions, move candidates on venue change
- Reports for start of tests, exceptions and completion
- Post-test wrap-up and archival with status report

**Acceptance criteria:** Status of every centre is visible within seconds; every intervention is recorded with reason.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F12-001 | Real-Time Centre & Session Monitoring | Live wall of all centres and sessions with readiness, attendance, logins, progress, submissions, alerts and recording health |
| F12-002 | Exam-Day Control & Venue Change Handling | Hold, resume, extend time, restart and move candidates across terminals or centres on venue change, with reasons |
| F12-003 | Central Monitoring Reports | Start-of-test, exception, completion and session summary reports for each test day |
| F12-004 | Post-Test Wrap-Up & Archival | Session closure checklist, data completeness checks, archival of responses, logs and recordings and status report |

### 13. MIS, Dashboards & Reports

**Type:** Business · **RFP reference:** RFP 4.3.4.2.3, 4.3.4.3, 4.3.2.5, 4.6.8.2

**Purpose:** Provide reports and data retrieval required by KEONICS, Center for E-Governance and DPAR.

**Functional requirements:**

- Dashboards and MIS on registration, tests conducted, number of candidates and exceptions
- Periodic test registration reports
- Quarterly question bank repository and enhancement reports
- Software for retrieval of examination data through queries and reports

**Acceptance criteria:** Reports reconcile with transaction data and export to Excel and PDF.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F13-001 | Management Dashboard | KEONICS and DPAR dashboard with registrations, bookings, tests conducted, pass rates, revenue and exceptions by district and period |
| F13-002 | Registration, Test & Result MIS Reports | Standard periodic reports on registrations, bookings, attendance, results, fees, rescheduling and malpractice in Excel and PDF |
| F13-003 | Question Bank Quarterly Reports | Quarterly reports on bank repository strength, additions, retirements, exposure and enhancement against the 5% target |
| F13-004 | Data Retrieval & Query Tool | Ad-hoc query and report builder over approved data views for authorised users, with export and saved queries |

### 14. Notifications & Helpdesk

**Type:** Shared · **RFP reference:** RFP 4.4.10–4.4.12, Data Sheet 3.3.2

**Purpose:** Communicate with candidates and staff at every step and support them through a helpdesk.

**Functional requirements:**

- E-mail and SMS for registration, hall ticket, rescheduling and results
- Helpdesk receiving calls from candidates, KEONICS and Center for E-Governance and making outbound calls
- Dedicated helpdesk numbers published on the portal

**Acceptance criteria:** Every candidate-facing event triggers the configured messages; every call is logged as a ticket.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F14-001 | Notification Templates & Event Engine | Bilingual SMS and e-mail templates mapped to events such as registration, booking, payment, hall ticket, reschedule, results and certificates |
| F14-002 | E-mail & SMS Gateway Integration | Connectors to KEONICS / state SMS gateway with DLT and SMTP e-mail, with retries, throttling and delivery receipts |
| F14-003 | Helpdesk Ticketing & Call Logging | Tickets for calls and e-mails from candidates, KEONICS and CeG, outbound call lists, categories, SLA timers and resolution tracking |
| F14-004 | Notification Delivery Log | Searchable log of every SMS and e-mail with status, resend and statistics |

### 15. Integration Hub

**Type:** Technical · **RFP reference:** RFP 4.3.6, 4.3.3.1.3, 4.4.26, 4.6.1.4, 4.6.1.6

**Purpose:** Integrate the CLT system with HRMS, Aadhaar, payment gateway, HSM and signing services securely.

**Functional requirements:**

- HRMS: employee details for validation; push of results and certificates
- Aadhaar authentication and eKYC through an authorised agency
- Payment gateway for UPI / UPI-QR, net banking, credit and debit card
- HSM service of Center for E-Governance for key management
- Digital signature / e-Sign for final scores, documents and certificates

**Acceptance criteria:** All integrations work end to end with retry, logging and reconciliation.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F15-001 | Integration Framework & Monitoring | Common connector framework with credentials vault, retries, circuit breakers, request logs, error queue and integration dashboard |
| F15-002 | HRMS Integration | Fetch employee details by KGID for registration and validation; push results and certificate references back to HRMS |
| F15-003 | Aadhaar Authentication & eKYC Integration | Aadhaar OTP / biometric authentication and eKYC through the authorised AUA / KUA with consent and reference tokens |
| F15-004 | Payment Gateway Integration | Gateway connector for UPI / UPI-QR, net banking and cards with callback, status inquiry, refunds and settlement data |
| F15-005 | HSM Key Management Integration | Integration with the Center for E-Governance HSM for key generation, wrapping and signing operations |
| F15-006 | DSC & e-Sign Integration | Digital signing of result files, certificates and documents using DSC or e-Sign service with signature verification |

### 16. Security, Audit & Compliance

**Type:** Technical · **RFP reference:** RFP 4.3.3.1.3, 4.4.20, 4.4.22, 4.6.1.3, 4.6.1.5, 4.6.4, 4.6.5, Annexure 9

**Purpose:** Protect question banks, responses, results and personal data and keep complete audit trails.

**Functional requirements:**

- Encryption of credentials, question bank, answer keys, candidate responses and results with AES-256; TLS in transit; asymmetric encryption with HSM
- Audit trails test centre-wise, system IP-wise and candidate-wise in the Annexure 9 format
- Safe-to-Host certification annually by a CERT-In empanelled auditor
- DPDP Act compliance; ISO 27001 aligned controls

**Acceptance criteria:** Encrypted data is unreadable without keys; audit trails are complete and tamper-evident; Safe-to-Host certificate obtained before go-live.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F16-001 | Data Encryption & Key Management | AES-256 encryption of credentials, question bank, answer keys, responses and results; TLS in transit; asymmetric encryption with HSM-held keys |
| F16-002 | Tamper-Evident Audit Trail | Annexure 9 format audit events by test centre, system IP and candidate, hash-chained, with viewer and export |
| F16-003 | Application Security & Safe-to-Host Support | OWASP controls, secure headers, WAF rules, vulnerability scanning, remediation and support for annual Safe-to-Host audits |
| F16-004 | DPDP Compliance & Aadhaar Data Vault | Consent records, purpose limitation, data principal requests, masking, retention rules and Aadhaar Data Vault |

### 17. Platform, Performance & Operations

**Type:** Technical · **RFP reference:** RFP 4.3.3.1.2, 4.3.4.2.2, 4.5.7.2–4.5.7.3, 4.6.6, Annexure 4

**Purpose:** Run the system at SDC with the required performance, availability and recoverability.

**Functional requirements:**

- At least 2,000 concurrent candidates per session without degradation; response under 1 second on LAN
- 99.9% availability
- Hardening of SDC servers before each test cycle
- Backup and restore as per KEONICS policy; data kept live for the contract period
- SLA monitoring and reports

**Acceptance criteria:** Load test at 2,000 concurrent candidates passes; backups restore within agreed time; SLA reports produced monthly.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F17-001 | SDC Deployment, Hardening & Release Management | Development, UAT and production environments at SDC, CI/CD pipeline, server hardening before test cycles and release runbooks |
| F17-002 | Scalability & Load Testing for 2,000 Concurrent Candidates | Horizontal scaling, caching and queueing for 2,000 concurrent candidates plus recordings, with load tests and capacity plan |
| F17-003 | Backup, Restore & Data Retention | Database, file and recording backups per KEONICS policy, restore drills and data kept live for the contract period |
| F17-004 | Availability Monitoring & SLA Reporting | Uptime, response time and error monitoring, alerting, incident register and monthly SLA reports per Annexure 4 |

### 18. Legacy CLT Data Porting

**Type:** Technical · **RFP reference:** RFP 4.6.2.2

**Purpose:** Bring the legacy data of previous CLTs into the new system.

**Functional requirements:**

- Port legacy candidates, results and certificates of previous CLTs
- Validation, reconciliation and KEONICS sign-off

**Acceptance criteria:** Ported records reconcile with legacy counts; earlier attempts count for fee rules; earlier certificates are verifiable.

**Key capabilities:**

| Feature ID | Feature | Description |
|------------|---------|-------------|
| F18-001 | Legacy Data Templates & Porting | Templates, staging and porting of previous CLT candidates, attempts, results and certificates |
| F18-002 | Ported Data Validation & Reconciliation | Count and checksum reconciliation, sample verification and KEONICS sign-off of ported data |

## 7. End-to-End Workflows

1. **Employee:** OTP account → KGID registration with HRMS fetch → auto-accept or scrutiny → booking (free first attempt) → hall ticket → mock tests → centre validation → test → immediate score → result finalisation → signed certificate → HRMS update.
2. **Prospective candidate:** registration at designated centre with eKYC and live photo → scrutiny → booking and fee payment → hall ticket → test → result → certificate.
3. **Question bank:** blueprint → authoring → review → Technical Committee approval → bank → paper set per session → sealed → released at session start.
4. **Session:** calendar → bookings → minimum batch check and forced reschedule → proctor assignment → readiness → validation → test with proctoring → wrap-up and archival.
5. **Malpractice:** alert → proctor / EMU review → case → committee decision → result withheld or cancelled.

## 8. Security, Audit and Compliance

- AES-256 encryption of credentials, question bank, answer keys, responses and results; TLS in transit; asymmetric encryption with keys in the CeG HSM
- Question component segregation so that only the author sees all components
- Audit trails test centre-wise, IP-wise and candidate-wise in the Annexure 9 format; tamper-evident
- Safe-to-Host certification before go-live and annually; ISO 27001 aligned controls; IPv6 readiness
- DPDP Act compliance and Aadhaar Data Vault

## 9. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Concurrency | At least 2,000 concurrent candidates per session with screen and webcam recording |
| Response time | Under 1 second on LAN for test interactions |
| Availability | 99.9% |
| Compatibility | Device, operating system and browser agnostic |
| Languages | Kannada and English |
| Data location | SDC only; no data stored at centres after the session |
| Backup | As per KEONICS policy; data live for the contract period |

## 10. Legacy Data Porting

Previous CLT candidates, attempts, results and certificates are ported so that attempt counts drive fee rules and earlier certificates remain verifiable. KEONICS provides data in agreed templates and signs off reconciliation before go-live.

## 11. Delivery Phasing and Milestones

| Milestone | Timeline | Payment |
|-----------|----------|--------:|
| Functional Requirement Specification | T + 1 month | 10% |
| Design: UI/UX, MIS, technology stack, server requirements, data migration document | T + 1.5 months | 25% |
| Development, data porting, UAT deployment, manuals and how-to videos | T + 2 months | — |
| UAT completion | T + 2.5 months | 30% |
| Safe-to-Host certification | T + 3 months | — |
| Go-live (W) with 10 trouble-free sessions and source code handover | T + 3 months | 20% |
| Warranty | W + 12 months | 5% |
| Comprehensive AMC | 3 years after warranty | Quarterly |

## 12. Deliverables

- FRS, design documents, data migration document, test plans and reports
- Application source code, binaries, mobile apps and deployment scripts
- User manuals, operator and proctor manuals, how-to videos
- Load test report, Safe-to-Host certificate, SLA reports

## 13. Service Levels (summary of Annexure 4)

- Availability 99.9% measured monthly; penalties per Annexure 4
- Resolution times for critical, high and medium incidents per Annexure 4
- Liquidated damages of 0.5% per week of delay up to 10%; performance bank guarantee of 5%

## 14. Assumptions

1. SDC provides compute, storage (including video recordings) and bandwidth sized per the capacity plan.
2. HRMS look-up and result update APIs are provided by DPAR / CeG.
3. Aadhaar AUA / KUA access, payment gateway, SMS (DLT) and e-mail accounts are provided by KEONICS / CeG.
4. The CeG HSM partition and signing certificates are made available.
5. Test centres provide terminals with webcams, required network bandwidth and permit installation of the secure exam client.
6. Legacy CLT data is provided in exportable form.

## 15. Appendix — RFP References

- Terms of Reference (Section 4), Annexure 1 technical requirements, Special Conditions of Contract, Annexure 4 SLA, Annexure 9 audit log format
