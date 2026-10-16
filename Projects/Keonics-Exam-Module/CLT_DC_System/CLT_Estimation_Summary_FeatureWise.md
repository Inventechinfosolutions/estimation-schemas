# CLT — Feature-wise Estimation Summary (Internal)

**Project:** Online Computer Literacy Test (CLT) and Digital Certification System  
**Project code:** CLT  
**As of:** 2026-10-14

## Grand totals

| Bucket | Hours |
|--------|------:|
| Recommended go-live | 5136 |
| Conditional | 50 |
| All-in | 5186 |
| Features | 90 |
| Modules | 18 |

## Module-wise summary

| # | Module | Type | Features | UI | API | DB | Integ. | Test | Docs | Hours |
|---|--------|------|---------:|---:|---:|---:|---:|---:|---:|------:|
| 01 | Access Control & Staff User Management | Shared | 3 | 102 | 152 | 16 | 0 | 38 | 8 | 316 |
| 02 | Examination Configuration & Masters | Business | 6 | 136 | 152 | 20 | 0 | 42 | 10 | 360 |
| 03 | CLT Web Portal & Mobile Application | Business | 4 | 104 | 54 | 6 | 16 | 38 | 12 | 230 |
| 04 | Candidate Registration & eKYC | Business | 6 | 168 | 168 | 20 | 0 | 56 | 11 | 423 |
| 05 | Online Test Booking, Fees & Hall Ticket | Business | 6 | 108 | 174 | 19 | 0 | 50 | 10 | 361 |
| 06 | Question Bank & Content Authoring Tool | Business | 8 | 196 | 178 | 22 | 0 | 58 | 16 | 470 |
| 07 | Question Paper Generation & Mock Test | Business | 4 | 26 | 98 | 12 | 0 | 34 | 6 | 176 |
| 08 | Test Centre Operations & Candidate Validation | Business | 6 | 96 | 146 | 14 | 16 | 36 | 12 | 320 |
| 09 | Online Examination Engine | Business | 7 | 144 | 178 | 18 | 40 | 78 | 16 | 474 |
| 10 | Screen Proctoring & Malpractice Management | Business | 6 | 112 | 158 | 18 | 40 | 52 | 11 | 391 |
| 11 | Evaluation, Results & Digital Certification | Business | 6 | 76 | 118 | 13 | 0 | 36 | 10 | 253 |
| 12 | Central Monitoring Centre & Examination Monitoring Unit | Business | 4 | 78 | 96 | 10 | 0 | 28 | 7 | 219 |
| 13 | MIS, Dashboards & Reports | Business | 4 | 60 | 76 | 14 | 0 | 24 | 7 | 181 |
| 14 | Notifications & Helpdesk | Shared | 4 | 54 | 76 | 10 | 24 | 22 | 6 | 192 |
| 15 | Integration Hub | Technical | 6 | 32 | 128 | 14 | 160 | 46 | 13 | 393 |
| 16 | Security, Audit & Compliance | Technical | 4 | 32 | 90 | 15 | 0 | 34 | 14 | 185 |
| 17 | Platform, Performance & Operations | Technical | 4 | 26 | 72 | 8 | 0 | 38 | 15 | 159 |
| 18 | Legacy CLT Data Porting | Technical | 2 | 22 | 36 | 6 | 0 | 14 | 5 | 83 |
| | **Total** | | **90** | **1572** | **2150** | **255** | **296** | **724** | **189** | **5186** |

## Feature-wise detail

### 01 — Access Control & Staff User Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F01-001 | Staff Authentication & Session Security | 7 | 9 | 32 | 52 | 6 | 0 | 14 | 3 | 107 | Go-live |
| F01-002 | Staff User, Role & Centre Mapping | 7 | 9 | 38 | 48 | 6 | 0 | 12 | 2 | 106 | Go-live |
| F01-003 | Permission Matrix & Data Scope | 5 | 7 | 32 | 52 | 4 | 0 | 12 | 3 | 103 | Go-live |

**Module total: 316 hours**

### 02 — Examination Configuration & Masters

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F02-001 | Syllabus, Marks & Weightage Configuration | 5 | 6 | 34 | 34 | 6 | 0 | 12 | 2 | 88 | Go-live |
| F02-002 | Test Centre, Seat & Terminal Master | 5 | 6 | 26 | 32 | 4 | 0 | 6 | 2 | 70 | Go-live |
| F02-003 | Session Calendar & Batch Rules | 4 | 5 | 20 | 30 | 4 | 0 | 6 | 2 | 62 | Go-live |
| F02-004 | Fee Rule Configuration | 4 | 4 | 18 | 18 | 2 | 0 | 6 | 1 | 45 | Go-live |
| F02-005 | Document & Certificate Template Management | 4 | 4 | 26 | 22 | 2 | 0 | 8 | 2 | 60 | Go-live |
| F02-006 | Reference Masters | 3 | 3 | 12 | 16 | 2 | 0 | 4 | 1 | 35 | Go-live |

**Module total: 360 hours**

### 03 — CLT Web Portal & Mobile Application

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F03-001 | Public Information Portal | 6 | 4 | 30 | 18 | 1 | 0 | 6 | 1 | 56 | Go-live |
| F03-002 | Portal Content & Study Material Management | 4 | 4 | 18 | 16 | 2 | 0 | 4 | 2 | 42 | Go-live |
| F03-003 | Bilingual, Responsive & Device-Agnostic Design | 2 | 1 | 10 | 4 | 1 | 0 | 14 | 5 | 34 | Go-live |
| F03-004 | Candidate Mobile Application | 8 | 3 | 46 | 16 | 2 | 16 | 14 | 4 | 98 | Go-live |

**Module total: 230 hours**

### 04 — Candidate Registration & eKYC

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F04-001 | Candidate OTP Login & Account | 5 | 7 | 34 | 38 | 4 | 0 | 12 | 2 | 90 | Go-live |
| F04-002 | Government Employee Registration with KGID & HRMS Validation | 5 | 6 | 32 | 36 | 6 | 0 | 14 | 2 | 90 | Go-live |
| F04-003 | Prospective Candidate & Non-KGID Registration with eKYC | 5 | 6 | 40 | 32 | 4 | 0 | 14 | 2 | 92 | Go-live |
| F04-004 | Centre-Assisted Registration & Photo Capture | 5 | 4 | 24 | 18 | 2 | 0 | 6 | 2 | 52 | Go-live |
| F04-005 | Registration Scrutiny & Metadata Validation | 4 | 5 | 26 | 30 | 2 | 0 | 6 | 2 | 66 | Go-live |
| F04-006 | Differently-Abled Candidate Support Requests | 3 | 3 | 12 | 14 | 2 | 0 | 4 | 1 | 33 | Go-live |

**Module total: 423 hours**

### 05 — Online Test Booking, Fees & Hall Ticket

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F05-001 | Online Test Booking & Slot Availability | 4 | 6 | 28 | 38 | 6 | 0 | 14 | 2 | 88 | Go-live |
| F05-002 | Attempt-Based Fee Calculation & Online Payment | 3 | 6 | 16 | 38 | 4 | 0 | 8 | 2 | 68 | Go-live |
| F05-003 | Payment Receipt, Reconciliation & Exceptions | 4 | 5 | 20 | 30 | 4 | 0 | 8 | 2 | 64 | Go-live |
| F05-004 | Hall Ticket with Barcode & Receipt | 2 | 5 | 8 | 26 | 2 | 0 | 6 | 1 | 43 | Go-live |
| F05-005 | Candidate Self-Service Rescheduling | 2 | 3 | 10 | 16 | 1 | 0 | 6 | 1 | 34 | Go-live |
| F05-006 | Minimum Batch Check & Forced Rescheduling | 4 | 4 | 26 | 26 | 2 | 0 | 8 | 2 | 64 | Go-live |

**Module total: 361 hours**

### 06 — Question Bank & Content Authoring Tool

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F06-001 | Question Paper Guidelines & Blueprint | 4 | 4 | 28 | 20 | 2 | 0 | 6 | 2 | 58 | Go-live |
| F06-002 | Bilingual Rich-Content Question Authoring | 6 | 6 | 60 | 36 | 6 | 0 | 14 | 3 | 119 | Go-live |
| F06-003 | Maker-Checker & Technical Committee Approval | 4 | 5 | 34 | 28 | 4 | 0 | 8 | 2 | 76 | Go-live |
| F06-004 | Question Component Segregation & Bank Privacy | 2 | 4 | 12 | 24 | 2 | 0 | 8 | 2 | 48 | Go-live |
| F06-005 | Field Test & Difficulty Calibration | 3 | 3 | 22 | 18 | 2 | 0 | 6 | 2 | 50 | Conditional |
| F06-006 | Excel / CSV Question Import | 3 | 3 | 14 | 20 | 2 | 0 | 6 | 2 | 44 | Go-live |
| F06-007 | Mock & Main Question Bank Management | 3 | 4 | 16 | 20 | 2 | 0 | 6 | 2 | 46 | Go-live |
| F06-008 | Typing Test Passage Management | 2 | 3 | 10 | 12 | 2 | 0 | 4 | 1 | 29 | Go-live |

**Module total: 470 hours**

### 07 — Question Paper Generation & Mock Test

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F07-001 | Weightage & Difficulty-Based Paper Generation | 2 | 4 | 10 | 36 | 4 | 0 | 14 | 2 | 66 | Go-live |
| F07-002 | Question & Option Jumbling per Candidate | 0 | 3 | 0 | 20 | 4 | 0 | 6 | 1 | 31 | Go-live |
| F07-003 | Sealed Paper Storage & Session Release | 1 | 4 | 4 | 24 | 2 | 0 | 8 | 2 | 40 | Go-live |
| F07-004 | Mock Test Engine | 3 | 4 | 12 | 18 | 2 | 0 | 6 | 1 | 39 | Go-live |

**Module total: 176 hours**

### 08 — Test Centre Operations & Candidate Validation

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F08-001 | Proctor Management, Authentication & Attendance | 4 | 5 | 22 | 24 | 2 | 0 | 6 | 3 | 57 | Go-live |
| F08-002 | Centre Readiness Check & Session Start | 2 | 5 | 18 | 28 | 2 | 0 | 8 | 2 | 58 | Go-live |
| F08-003 | Candidate Identity Validation & Photo Capture | 3 | 5 | 22 | 30 | 4 | 0 | 6 | 2 | 64 | Go-live |
| F08-004 | Biometric & Aadhaar Authentication at Centre | 2 | 4 | 10 | 20 | 2 | 16 | 6 | 2 | 56 | Go-live |
| F08-005 | Seat Allocation & Hall Ticket Login Control | 2 | 4 | 10 | 22 | 2 | 0 | 6 | 1 | 41 | Go-live |
| F08-006 | Attendance Sheets, Scans & Centre Incident Records | 3 | 5 | 14 | 22 | 2 | 0 | 4 | 2 | 44 | Go-live |

**Module total: 320 hours**

### 09 — Online Examination Engine

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F09-001 | Secure Test Login & Language Selection | 4 | 4 | 16 | 24 | 2 | 0 | 8 | 2 | 52 | Go-live |
| F09-002 | Rich MCQ Delivery & Navigation | 5 | 3 | 54 | 18 | 2 | 0 | 14 | 2 | 90 | Go-live |
| F09-003 | Server-Synchronised Timer & Disruption Compensation | 3 | 5 | 16 | 32 | 2 | 0 | 8 | 2 | 60 | Go-live |
| F09-004 | English & Kannada Typing Test | 3 | 4 | 28 | 26 | 2 | 0 | 8 | 2 | 66 | Go-live |
| F09-005 | Response Autosave & Answer Integrity | 2 | 4 | 6 | 36 | 6 | 0 | 14 | 2 | 64 | Go-live |
| F09-006 | Submission, Early Exit & Immediate Score | 2 | 3 | 10 | 16 | 2 | 0 | 6 | 1 | 35 | Go-live |
| F09-007 | Secure Exam Client & Device Compatibility | 3 | 4 | 14 | 26 | 2 | 40 | 20 | 5 | 107 | Go-live |

**Module total: 474 hours**

### 10 — Screen Proctoring & Malpractice Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F10-001 | Continuous Screen Recording | 1 | 4 | 6 | 26 | 4 | 16 | 8 | 2 | 62 | Go-live |
| F10-002 | Webcam Recording & Automated Monitoring | 2 | 4 | 10 | 32 | 4 | 24 | 16 | 2 | 88 | Go-live |
| F10-003 | Browser Activity & Tab-Switch Detection | 2 | 3 | 8 | 16 | 2 | 0 | 8 | 1 | 35 | Go-live |
| F10-004 | Real-Time Suspicious Activity Alerts | 3 | 4 | 30 | 26 | 2 | 0 | 8 | 2 | 68 | Go-live |
| F10-005 | Malpractice Case Management & Reports | 4 | 5 | 30 | 30 | 4 | 0 | 6 | 2 | 72 | Go-live |
| F10-006 | Recording Storage, Playback & Retention | 4 | 5 | 28 | 28 | 2 | 0 | 6 | 2 | 66 | Go-live |

**Module total: 391 hours**

### 11 — Evaluation, Results & Digital Certification

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F11-001 | Automatic MCQ & Typing Evaluation | 2 | 4 | 10 | 26 | 4 | 0 | 8 | 2 | 50 | Go-live |
| F11-002 | Answer Key Challenge | 4 | 4 | 20 | 22 | 2 | 0 | 6 | 2 | 52 | Go-live |
| F11-003 | Result Finalisation & Signed Submission | 3 | 4 | 16 | 24 | 2 | 0 | 6 | 2 | 50 | Go-live |
| F11-004 | Digitally Signed Certificate Generation | 2 | 4 | 10 | 22 | 2 | 0 | 6 | 2 | 42 | Go-live |
| F11-005 | Certificate Issue Workflow & Download | 3 | 4 | 12 | 18 | 2 | 0 | 6 | 1 | 39 | Go-live |
| F11-006 | Public Certificate Verification | 2 | 2 | 8 | 6 | 1 | 0 | 4 | 1 | 20 | Go-live |

**Module total: 253 hours**

### 12 — Central Monitoring Centre & Examination Monitoring Unit

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F12-001 | Real-Time Centre & Session Monitoring | 3 | 3 | 34 | 22 | 4 | 0 | 8 | 2 | 70 | Go-live |
| F12-002 | Exam-Day Control & Venue Change Handling | 3 | 5 | 28 | 32 | 2 | 0 | 8 | 2 | 72 | Go-live |
| F12-003 | Central Monitoring Reports | 1 | 4 | 6 | 22 | 2 | 0 | 6 | 1 | 37 | Go-live |
| F12-004 | Post-Test Wrap-Up & Archival | 2 | 4 | 10 | 20 | 2 | 0 | 6 | 2 | 40 | Go-live |

**Module total: 219 hours**

### 13 — MIS, Dashboards & Reports

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F13-001 | Management Dashboard | 2 | 2 | 18 | 14 | 4 | 0 | 6 | 2 | 44 | Go-live |
| F13-002 | Registration, Test & Result MIS Reports | 3 | 4 | 20 | 34 | 2 | 0 | 8 | 2 | 66 | Go-live |
| F13-003 | Question Bank Quarterly Reports | 1 | 2 | 6 | 12 | 2 | 0 | 4 | 1 | 25 | Go-live |
| F13-004 | Data Retrieval & Query Tool | 2 | 3 | 16 | 16 | 6 | 0 | 6 | 2 | 46 | Go-live |

**Module total: 181 hours**

### 14 — Notifications & Helpdesk

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F14-001 | Notification Templates & Event Engine | 3 | 4 | 16 | 22 | 2 | 0 | 6 | 2 | 48 | Go-live |
| F14-002 | E-mail & SMS Gateway Integration | 1 | 4 | 4 | 20 | 2 | 24 | 6 | 1 | 57 | Go-live |
| F14-003 | Helpdesk Ticketing & Call Logging | 5 | 4 | 26 | 22 | 4 | 0 | 6 | 2 | 60 | Go-live |
| F14-004 | Notification Delivery Log | 2 | 3 | 8 | 12 | 2 | 0 | 4 | 1 | 27 | Go-live |

**Module total: 192 hours**

### 15 — Integration Hub

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F15-001 | Integration Framework & Monitoring | 3 | 4 | 18 | 24 | 4 | 0 | 8 | 3 | 57 | Go-live |
| F15-002 | HRMS Integration | 1 | 3 | 4 | 18 | 2 | 48 | 8 | 2 | 82 | Go-live |
| F15-003 | Aadhaar Authentication & eKYC Integration | 0 | 4 | 0 | 24 | 2 | 40 | 8 | 2 | 76 | Go-live |
| F15-004 | Payment Gateway Integration | 0 | 4 | 0 | 20 | 2 | 24 | 8 | 2 | 56 | Go-live |
| F15-005 | HSM Key Management Integration | 1 | 4 | 6 | 26 | 2 | 24 | 8 | 2 | 68 | Go-live |
| F15-006 | DSC & e-Sign Integration | 1 | 3 | 4 | 16 | 2 | 24 | 6 | 2 | 54 | Go-live |

**Module total: 393 hours**

### 16 — Security, Audit & Compliance

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F16-001 | Data Encryption & Key Management | 1 | 3 | 4 | 18 | 4 | 0 | 8 | 3 | 37 | Go-live |
| F16-002 | Tamper-Evident Audit Trail | 2 | 4 | 10 | 32 | 6 | 0 | 8 | 3 | 59 | Go-live |
| F16-003 | Application Security & Safe-to-Host Support | 1 | 3 | 4 | 16 | 1 | 0 | 12 | 6 | 39 | Go-live |
| F16-004 | DPDP Compliance & Aadhaar Data Vault | 3 | 4 | 14 | 24 | 4 | 0 | 6 | 2 | 50 | Go-live |

**Module total: 185 hours**

### 17 — Platform, Performance & Operations

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F17-001 | SDC Deployment, Hardening & Release Management | 1 | 3 | 4 | 20 | 1 | 0 | 6 | 7 | 38 | Go-live |
| F17-002 | Scalability & Load Testing for 2,000 Concurrent Candidates | 0 | 3 | 0 | 22 | 4 | 0 | 20 | 4 | 50 | Go-live |
| F17-003 | Backup, Restore & Data Retention | 1 | 2 | 4 | 12 | 1 | 0 | 6 | 2 | 25 | Go-live |
| F17-004 | Availability Monitoring & SLA Reporting | 3 | 3 | 18 | 18 | 2 | 0 | 6 | 2 | 46 | Go-live |

**Module total: 159 hours**

### 18 — Legacy CLT Data Porting

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F18-001 | Legacy Data Templates & Porting | 2 | 4 | 12 | 26 | 4 | 0 | 8 | 3 | 53 | Go-live |
| F18-002 | Ported Data Validation & Reconciliation | 2 | 2 | 10 | 10 | 2 | 0 | 6 | 2 | 30 | Go-live |

**Module total: 83 hours**

## Effort profile

| Area | Hours | % |
|------|------:|---:|
| UI | 1572 | 30.3% |
| API | 2150 | 41.5% |
| Database | 255 | 4.9% |
| Integration | 296 | 5.7% |
| Testing | 724 | 14.0% |
| Documentation | 189 | 3.6% |

## Indicative phasing (from the SOW)

| Phase | Timeline | Modules |
|-------|----------|---------|
| FRS | T to T + 1 month | All (requirements) |
| Design and foundation | T + 0.5 to T + 1.5 months | 01, 02, 14, 15, 16, 17 |
| Candidate journey and question bank | T + 1 to T + 2 months | 03, 04, 05, 06, 07 |
| Exam engine, centre, proctoring, results | T + 1 to T + 2 months | 08, 09, 10, 11, 12 |
| MIS and data porting | T + 1.5 to T + 2 months | 13, 18 |
| UAT | T + 2 to T + 2.5 months | All |
| Safe-to-Host and go-live | T + 2.5 to T + 3 months | All |

## Exclusions

- PM, FRS and design phase, SME question content, helpdesk staffing, Safe-to-Host audit fee and SSL, training and how-to videos, warranty and CAMC, exit management, SDC hosting and third-party transaction charges
