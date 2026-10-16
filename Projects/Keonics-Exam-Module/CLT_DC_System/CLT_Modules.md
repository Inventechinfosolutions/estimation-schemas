# Online Computer Literacy Test (CLT) and Digital Certification System — Module List

Source: `SoW_CLT_Detailed.md` (derived from `261013-Call 3-RFP-CLT DC System-v1-0.pdf`, Section 6)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Access Control & Staff User Management | Shared | Staff login with OTP, user and role management with centre and district mapping, configurable permission matrix and data scope | Derived |
| 02 | Examination Configuration & Masters | Business | Syllabus, marks and weightage with session snapshot, test centres and seats, session calendar and batch rules, fee rules, document templates, reference masters | Explicit |
| 03 | CLT Web Portal & Mobile Application | Business | Public portal at clt.karnataka.gov.in with test information, centres and study material, content management, responsive bilingual design and a candidate mobile application | Explicit |
| 04 | Candidate Registration & eKYC | Business | Candidate OTP account, KGID registration with HRMS validation, eKYC registration for prospective candidates and employees without KGID, centre-assisted registration, scrutiny, scribe requests | Explicit |
| 05 | Online Test Booking, Fees & Hall Ticket | Business | Online Test Booking System with colour-coded slots, attempt-based fees and payment, receipts and reconciliation, barcode hall ticket, one-time self-service rescheduling, minimum batch and forced rescheduling | Explicit |
| 06 | Question Bank & Content Authoring Tool | Business | Question paper guidelines and blueprint, bilingual rich-content authoring, maker-checker and Technical Committee approval, component segregation, calibration, bulk import, mock and main banks, typing passages | Explicit |
| 07 | Question Paper Generation & Mock Test | Business | Weightage and difficulty based random paper set per session, question and option jumbling per candidate, sealed paper release, mock test engine | Explicit |
| 08 | Test Centre Operations & Candidate Validation | Business | Proctor management and attendance, centre sanity check and session start, candidate identity validation and photo, biometric / Aadhaar authentication, seat allocation, attendance sheets and scans | Explicit |
| 09 | Online Examination Engine | Business | Secure login and language choice, rich MCQ interface, server-synchronised timer with compensation, English and Kannada typing test, autosave and integrity, submission with immediate score, device-agnostic secure client | Explicit |
| 10 | Screen Proctoring & Malpractice Management | Business | Continuous screen video recording, webcam video recording with automated monitoring, browser activity and tab-switch detection, real-time alerts, malpractice cases and reports, recording storage and playback | Explicit |
| 11 | Evaluation, Results & Digital Certification | Business | Automatic MCQ and typing evaluation with optional negative marking, answer key challenge, result finalisation with signed submission, digitally signed certificate, certificate issue workflow, public verification | Explicit |
| 12 | Central Monitoring Centre & Examination Monitoring Unit | Business | Real-time monitoring of all centres and sessions, exam-day control actions and venue change handling, central monitoring reports, post-test wrap-up and archival | Explicit |
| 13 | MIS, Dashboards & Reports | Business | Management dashboard, registration, test and result MIS, question bank quarterly and enhancement reports, data retrieval and query tool | Explicit |
| 14 | Notifications & Helpdesk | Shared | Bilingual notification templates and event engine, e-mail and SMS gateways, helpdesk ticketing with call logging, delivery log | Explicit |
| 15 | Integration Hub | Technical | Integration framework and monitoring, HRMS fetch and result push, Aadhaar authentication and eKYC, payment gateway, HSM, DSC / e-Sign | Explicit |
| 16 | Security, Audit & Compliance | Technical | AES-256 and asymmetric encryption with HSM keys, tamper-evident audit trail per Annexure 9, application security and Safe-to-Host support, DPDP compliance | Explicit |
| 17 | Platform, Performance & Operations | Technical | SDC deployment and hardening, scalability for 2,000 concurrent candidates and load testing, backup and retention, availability monitoring and SLA reporting | Explicit |
| 18 | Legacy CLT Data Porting | Technical | Templates and porting of previous CLT data, validation and reconciliation with sign-off | Explicit |

---

## Module Details

### 01. Access Control & Staff User Management

- **Type:** Shared
- **Summary:** Staff login with OTP, user and role management with centre and district mapping, configurable permission matrix and data scope.
- **Source:** Derived (RFP 4.4.17, 4.6.1.3)
- **In Scope:** Staff authentication; users, roles, district / centre mapping; permission matrix and data scope
- **Out of Scope:** Candidate login (Module 04); proctor onboarding (Module 08)
- **Key Actors:** Super Admin; KEONICS Administrator; all staff roles
- **Dependencies:** F14-002 (OTP delivery); F16-002 (audit)
- **Notes:** Access model User → Role → Permissions with district / centre data scope; candidates use a separate OTP login
- **Features:** F01-001 Staff Authentication & Session Security, F01-002 Staff User, Role & Centre Mapping, F01-003 Permission Matrix & Data Scope

### 02. Examination Configuration & Masters

- **Type:** Business
- **Summary:** Syllabus, marks and weightage with session snapshot, test centres and seats, session calendar and batch rules, fee rules, document templates, reference masters.
- **Source:** Explicit (RFP 4.4.3, 4.4.7, 4.4.9–4.4.12)
- **In Scope:** Configuration and masters used by all business modules
- **Out of Scope:** Question content (Module 06)
- **Key Actors:** KEONICS Administrator; Approving Authority
- **Dependencies:** Used by Modules 04–11
- **Notes:** No code change needed for syllabus, weightage, sessions or fee revisions
- **Features:** F02-001 Syllabus, Marks & Weightage Configuration, F02-002 Test Centre, Seat & Terminal Master, F02-003 Session Calendar & Batch Rules, F02-004 Fee Rule Configuration, F02-005 Document & Certificate Template Management, F02-006 Reference Masters

### 03. CLT Web Portal & Mobile Application

- **Type:** Business
- **Summary:** Public portal at clt.karnataka.gov.in with test information, centres and study material, content management, responsive bilingual design and a candidate mobile application.
- **Source:** Explicit (RFP 4.5.3, 4.5.5.3, 4.3.3.1.6–7)
- **In Scope:** Public portal pages, content management, mobile application shell and store publication
- **Out of Scope:** Registration and booking logic (Modules 04–05, reused by the mobile application)
- **Key Actors:** Public; candidates; KEONICS Content Administrator
- **Dependencies:** Modules 04, 05, 07
- **Notes:** —
- **Features:** F03-001 Public Information Portal, F03-002 Portal Content & Study Material Management, F03-003 Bilingual, Responsive & Device-Agnostic Design, F03-004 Candidate Mobile Application

### 04. Candidate Registration & eKYC

- **Type:** Business
- **Summary:** Candidate OTP account, KGID registration with HRMS validation, eKYC registration for prospective candidates and employees without KGID, centre-assisted registration, scrutiny, scribe requests.
- **Source:** Explicit (RFP 4.4.8, 4.4.15, 4.5.5, 4.2.2.5)
- **In Scope:** Candidate account, registration paths, document capture, scrutiny, scribe requests
- **Out of Scope:** Booking and fees (Module 05)
- **Key Actors:** Candidate; Registration Centre Operator; Scrutiny Officer
- **Dependencies:** F15-002 (HRMS); F15-003 (Aadhaar eKYC); F14-002
- **Notes:** eKYC and HRMS connectors are in Module 15
- **Features:** F04-001 Candidate OTP Login & Account, F04-002 Government Employee Registration with KGID & HRMS Validation, F04-003 Prospective Candidate & Non-KGID Registration with eKYC, F04-004 Centre-Assisted Registration & Photo Capture, F04-005 Registration Scrutiny & Metadata Validation, F04-006 Differently-Abled Candidate Support Requests

### 05. Online Test Booking, Fees & Hall Ticket

- **Type:** Business
- **Summary:** Online Test Booking System with colour-coded slots, attempt-based fees and payment, receipts and reconciliation, barcode hall ticket, one-time self-service rescheduling, minimum batch and forced rescheduling.
- **Source:** Explicit (RFP 4.4.7, 4.4.10–4.4.13, 4.5.3.1, 4.5.5.4–4.5.5.8, 4.6.1.6)
- **In Scope:** Booking, payment, receipts, hall ticket, rescheduling, batch management
- **Out of Scope:** Payment gateway charges
- **Key Actors:** Candidate; KEONICS Administrator; Finance Officer; Helpdesk
- **Dependencies:** Module 02; F15-004 (payment gateway); Module 14
- **Notes:** —
- **Features:** F05-001 Online Test Booking & Slot Availability, F05-002 Attempt-Based Fee Calculation & Online Payment, F05-003 Payment Receipt, Reconciliation & Exceptions, F05-004 Hall Ticket with Barcode & Receipt, F05-005 Candidate Self-Service Rescheduling, F05-006 Minimum Batch Check & Forced Rescheduling

### 06. Question Bank & Content Authoring Tool

- **Type:** Business
- **Summary:** Question paper guidelines and blueprint, bilingual rich-content authoring, maker-checker and Technical Committee approval, component segregation, calibration, bulk import, mock and main banks, typing passages.
- **Source:** Explicit (RFP 4.3.2, 4.4.5, 4.5.6)
- **In Scope:** Authoring tool, workflow, bank management, reports
- **Out of Scope:** Writing of question content by SMEs (service, quoted separately)
- **Key Actors:** SME Author; Reviewer; Technical Committee Member; Question Bank Administrator
- **Dependencies:** F16-001 (encryption); F02-001 (syllabus)
- **Notes:** Question content creation is a service line item, not feature hours
- **Features:** F06-001 Question Paper Guidelines & Blueprint, F06-002 Bilingual Rich-Content Question Authoring, F06-003 Maker-Checker & Technical Committee Approval, F06-004 Question Component Segregation & Bank Privacy, F06-005 Field Test & Difficulty Calibration, F06-006 Excel / CSV Question Import, F06-007 Mock & Main Question Bank Management, F06-008 Typing Test Passage Management

### 07. Question Paper Generation & Mock Test

- **Type:** Business
- **Summary:** Weightage and difficulty based random paper set per session, question and option jumbling per candidate, sealed paper release, mock test engine.
- **Source:** Explicit (RFP 4.5.4, 4.5.6.6.5, 4.5.6.6.7)
- **In Scope:** Paper sets, jumbling, release control, mock test
- **Out of Scope:** Exam delivery (Module 09)
- **Key Actors:** System; Question Bank Administrator; Candidate
- **Dependencies:** Module 06; F16-001; F15-005 (HSM)
- **Notes:** —
- **Features:** F07-001 Weightage & Difficulty-Based Paper Generation, F07-002 Question & Option Jumbling per Candidate, F07-003 Sealed Paper Storage & Session Release, F07-004 Mock Test Engine

### 08. Test Centre Operations & Candidate Validation

- **Type:** Business
- **Summary:** Proctor management and attendance, centre sanity check and session start, candidate identity validation and photo, biometric / Aadhaar authentication, seat allocation, attendance sheets and scans.
- **Source:** Explicit (RFP 4.4.14, 4.4.16, 4.4.17, 4.5.9, 4.6.8)
- **In Scope:** Centre console for proctors and centre staff
- **Out of Scope:** Centre hardware, network and seating (KEONICS / centres)
- **Key Actors:** Proctor; Centre Operator; Candidate
- **Dependencies:** Module 05; F15-003; F12-001
- **Notes:** No local database; all data is stored centrally
- **Features:** F08-001 Proctor Management, Authentication & Attendance, F08-002 Centre Readiness Check & Session Start, F08-003 Candidate Identity Validation & Photo Capture, F08-004 Biometric & Aadhaar Authentication at Centre, F08-005 Seat Allocation & Hall Ticket Login Control, F08-006 Attendance Sheets, Scans & Centre Incident Records

### 09. Online Examination Engine

- **Type:** Business
- **Summary:** Secure login and language choice, rich MCQ interface, server-synchronised timer with compensation, English and Kannada typing test, autosave and integrity, submission with immediate score, device-agnostic secure client.
- **Source:** Explicit (RFP 4.3.3.1.4, 4.4.4, 4.4.6, 4.4.18–4.4.23, 4.5.9)
- **In Scope:** Candidate test client and test services
- **Out of Scope:** Proctoring (Module 10)
- **Key Actors:** Candidate; System
- **Dependencies:** Modules 07, 08; F16-001
- **Notes:** —
- **Features:** F09-001 Secure Test Login & Language Selection, F09-002 Rich MCQ Delivery & Navigation, F09-003 Server-Synchronised Timer & Disruption Compensation, F09-004 English & Kannada Typing Test, F09-005 Response Autosave & Answer Integrity, F09-006 Submission, Early Exit & Immediate Score, F09-007 Secure Exam Client & Device Compatibility

### 10. Screen Proctoring & Malpractice Management

- **Type:** Business
- **Summary:** Continuous screen video recording, webcam video recording with automated monitoring, browser activity and tab-switch detection, real-time alerts, malpractice cases and reports, recording storage and playback.
- **Source:** Explicit (RFP 4.3.3.1.5)
- **In Scope:** Recording, detection, alerts, cases, storage and playback
- **Out of Scope:** Storage hardware (provided by State Data Center)
- **Key Actors:** Candidate; Proctor; Examination Monitoring Unit; Malpractice Committee
- **Dependencies:** Module 09; F17-002 (capacity)
- **Notes:** Full video recording is in go-live scope; storage sized with SDC
- **Features:** F10-001 Continuous Screen Recording, F10-002 Webcam Recording & Automated Monitoring, F10-003 Browser Activity & Tab-Switch Detection, F10-004 Real-Time Suspicious Activity Alerts, F10-005 Malpractice Case Management & Reports, F10-006 Recording Storage, Playback & Retention

### 11. Evaluation, Results & Digital Certification

- **Type:** Business
- **Summary:** Automatic MCQ and typing evaluation with optional negative marking, answer key challenge, result finalisation with signed submission, digitally signed certificate, certificate issue workflow, public verification.
- **Source:** Explicit (RFP 4.2.3.7, 4.3.6.3.2, 4.4.19, 4.4.24–4.4.26, 4.5.8.3, 4.6.1.4)
- **In Scope:** Evaluation, challenge, results, certificates, verification
- **Out of Scope:** Re-evaluation (not permitted)
- **Key Actors:** System; Result Officer; KEONICS Approver; Candidate; Public verifier
- **Dependencies:** Modules 06, 09; F15-002; F15-006
- **Notes:** —
- **Features:** F11-001 Automatic MCQ & Typing Evaluation, F11-002 Answer Key Challenge, F11-003 Result Finalisation & Signed Submission, F11-004 Digitally Signed Certificate Generation, F11-005 Certificate Issue Workflow & Download, F11-006 Public Certificate Verification

### 12. Central Monitoring Centre & Examination Monitoring Unit

- **Type:** Business
- **Summary:** Real-time monitoring of all centres and sessions, exam-day control actions and venue change handling, central monitoring reports, post-test wrap-up and archival.
- **Source:** Explicit (RFP 4.2.3.5, 4.4.21, 4.5.8, 4.3.4.2.3–4.3.4.2.4)
- **In Scope:** Central dashboard and control console
- **Out of Scope:** Monitoring hardware
- **Key Actors:** Examination Monitoring Unit; KEONICS; Competent Authority
- **Dependencies:** Modules 08–10
- **Notes:** —
- **Features:** F12-001 Real-Time Centre & Session Monitoring, F12-002 Exam-Day Control & Venue Change Handling, F12-003 Central Monitoring Reports, F12-004 Post-Test Wrap-Up & Archival

### 13. MIS, Dashboards & Reports

- **Type:** Business
- **Summary:** Management dashboard, registration, test and result MIS, question bank quarterly and enhancement reports, data retrieval and query tool.
- **Source:** Explicit (RFP 4.3.4.2.3, 4.3.4.3, 4.3.2.5, 4.6.8.2)
- **In Scope:** Dashboards, standard reports, query tool
- **Out of Scope:** External BI tools
- **Key Actors:** KEONICS; Center for E-Governance; DPAR; Administrators
- **Dependencies:** All business modules
- **Notes:** —
- **Features:** F13-001 Management Dashboard, F13-002 Registration, Test & Result MIS Reports, F13-003 Question Bank Quarterly Reports, F13-004 Data Retrieval & Query Tool

### 14. Notifications & Helpdesk

- **Type:** Shared
- **Summary:** Bilingual notification templates and event engine, e-mail and SMS gateways, helpdesk ticketing with call logging, delivery log.
- **Source:** Explicit (RFP 4.4.10–4.4.12, Data Sheet 3.3.2)
- **In Scope:** Templates, engine, gateways, ticketing, logs
- **Out of Scope:** Helpdesk staffing (service)
- **Key Actors:** System; Helpdesk Executive; Candidate
- **Dependencies:** F15-001
- **Notes:** —
- **Features:** F14-001 Notification Templates & Event Engine, F14-002 E-mail & SMS Gateway Integration, F14-003 Helpdesk Ticketing & Call Logging, F14-004 Notification Delivery Log

### 15. Integration Hub

- **Type:** Technical
- **Summary:** Integration framework and monitoring, HRMS fetch and result push, Aadhaar authentication and eKYC, payment gateway, HSM, DSC / e-Sign.
- **Source:** Explicit (RFP 4.3.6, 4.3.3.1.3, 4.4.26, 4.6.1.4, 4.6.1.6)
- **In Scope:** Connectors and integration operations
- **Out of Scope:** Licences and transaction charges of third-party services
- **Key Actors:** System; Super Admin
- **Dependencies:** External system access from Center for E-Governance / KEONICS
- **Notes:** —
- **Features:** F15-001 Integration Framework & Monitoring, F15-002 HRMS Integration, F15-003 Aadhaar Authentication & eKYC Integration, F15-004 Payment Gateway Integration, F15-005 HSM Key Management Integration, F15-006 DSC & e-Sign Integration

### 16. Security, Audit & Compliance

- **Type:** Technical
- **Summary:** AES-256 and asymmetric encryption with HSM keys, tamper-evident audit trail per Annexure 9, application security and Safe-to-Host support, DPDP compliance.
- **Source:** Explicit (RFP 4.3.3.1.3, 4.4.20, 4.4.22, 4.6.1.3, 4.6.1.5, 4.6.4, 4.6.5, Annexure 9)
- **In Scope:** Security controls, audit, compliance features
- **Out of Scope:** Audit fee (commercial line item)
- **Key Actors:** System; Super Admin; Auditor
- **Dependencies:** F15-005 (HSM)
- **Notes:** —
- **Features:** F16-001 Data Encryption & Key Management, F16-002 Tamper-Evident Audit Trail, F16-003 Application Security & Safe-to-Host Support, F16-004 DPDP Compliance & Aadhaar Data Vault

### 17. Platform, Performance & Operations

- **Type:** Technical
- **Summary:** SDC deployment and hardening, scalability for 2,000 concurrent candidates and load testing, backup and retention, availability monitoring and SLA reporting.
- **Source:** Explicit (RFP 4.3.3.1.2, 4.3.4.2.2, 4.5.7.2–4.5.7.3, 4.6.6, Annexure 4)
- **In Scope:** Environments, pipelines, performance engineering, backups, monitoring
- **Out of Scope:** SDC infrastructure
- **Key Actors:** Service Provider operations; KEONICS; SDC
- **Dependencies:** SDC
- **Notes:** —
- **Features:** F17-001 SDC Deployment, Hardening & Release Management, F17-002 Scalability & Load Testing for 2,000 Concurrent Candidates, F17-003 Backup, Restore & Data Retention, F17-004 Availability Monitoring & SLA Reporting

### 18. Legacy CLT Data Porting

- **Type:** Technical
- **Summary:** Templates and porting of previous CLT data, validation and reconciliation with sign-off.
- **Source:** Explicit (RFP 4.6.2.2)
- **In Scope:** Porting utilities and validation
- **Out of Scope:** Cleansing of legacy data at source
- **Key Actors:** Service Provider; KEONICS
- **Dependencies:** Modules 04, 11
- **Notes:** —
- **Features:** F18-001 Legacy Data Templates & Porting, F18-002 Ported Data Validation & Reconciliation

## Excluded / Embedded Capabilities

- **Workflow / approvals:** embedded in registration scrutiny (F04-005), question review (F06-003), forced rescheduling (F05-006), malpractice (F10-005), results (F11-003) and certificate issue (F11-005); no separate workflow engine module.
- **Document management:** embedded — photos and documents (F04-002 to F04-004), media (F06-002), hall tickets (F05-004), scans (F08-006), recordings (F10-006), certificates (F11-004).
- **Scheduler / background jobs:** embedded in seat hold expiry (F05-001), minimum batch check (F05-006), paper generation (F07-001), reminders (F14-001), retention purge (F10-006), reconciliation (F05-003).
- **Question content creation by SMEs:** service line item; the Content Authoring Tool and workflow are in Module 06.
- **Helpdesk staffing, Safe-to-Host audit fee, SSL certificate, training and how-to videos, CAMC and exit management:** service or commercial line items outside feature hours.
- **Re-evaluation:** not permitted under the RFP.

## Assumptions

1. Access model is User → Role → Permissions with district / centre data scope; candidates use a separate OTP login.
2. HRMS, Aadhaar, payment gateway, HSM and DSC / e-Sign connectors are built in Module 15; business features call them.
3. Full screen and webcam video recording is in go-live scope; storage and bandwidth are provided by SDC per the capacity plan.
4. Field test and difficulty calibration (F06-005) is conditional on KEONICS requiring it.
5. The typing test (Part 2, English and Kannada) is in go-live scope as per the RFP syllabus.
6. KEONICS supplies templates, fee rules, centre data and legacy data in agreed formats.

## Risks

1. Go-live at T + 3 months with development complete by T + 2 months is tight for the size of the scope.
2. Video recording at 2,000 concurrent candidates needs large storage and centre / SDC bandwidth.
3. HRMS and Aadhaar AUA / KUA onboarding timelines are outside the Service Provider's control.
4. Secure exam client lockdown depends on operating system versions at centres.
5. Legacy CLT data quality is unknown.
