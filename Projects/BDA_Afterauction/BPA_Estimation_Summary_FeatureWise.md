# BPA — Feature-wise Estimation Summary (Internal)

**Project:** BDA Post-Auction Award, Payment and Completion Management Module  
**Project code:** BPA  
**As of:** 2026-10-14

## Grand totals

| Bucket | Hours |
|--------|------:|
| Recommended go-live | 4766 |
| Conditional | 49 |
| All-in | 4815 |
| Features | 75 |
| Modules | 16 |

## Module-wise summary

| # | Module | Type | Features | UI | API | DB | Integ. | Test | Docs | Hours |
|---|--------|------|---------:|---:|---:|---:|---:|---:|---:|------:|
| 01 | User, Role & Access Management | Shared | 4 | 138 | 244 | 30 | 8 | 78 | 17 | 515 |
| 02 | Auction Rules & Configuration | Business | 6 | 174 | 212 | 25 | 0 | 74 | 14 | 499 |
| 03 | KPPP Result Intake & Site Package | Business | 5 | 126 | 208 | 36 | 48 | 70 | 14 | 502 |
| 04 | Result Verification & Approval | Business | 5 | 132 | 182 | 14 | 0 | 62 | 10 | 400 |
| 05 | Successful Bidder Notification & Account | Business | 4 | 72 | 106 | 11 | 0 | 38 | 6 | 233 |
| 06 | Payment & Instalment Management | Business | 9 | 218 | 340 | 30 | 40 | 118 | 20 | 766 |
| 07 | Case Forwarding & Deputy Secretary Processing | Business | 5 | 96 | 140 | 11 | 0 | 38 | 8 | 293 |
| 08 | Draft Sale Deed | Business | 4 | 64 | 82 | 7 | 0 | 24 | 5 | 182 |
| 09 | Registration Recording & Completion | Business | 4 | 36 | 66 | 5 | 40 | 22 | 6 | 175 |
| 10 | Bidder Tracking Portal | Business | 5 | 64 | 58 | 5 | 0 | 36 | 6 | 169 |
| 11 | Dashboards, MIS & Reports | Business | 5 | 72 | 110 | 10 | 0 | 34 | 9 | 235 |
| 12 | Notification Service | Shared | 4 | 34 | 88 | 10 | 36 | 24 | 7 | 199 |
| 13 | Integration Hub | Technical | 4 | 42 | 96 | 11 | 40 | 26 | 8 | 223 |
| 14 | Audit, Security & Compliance | Technical | 4 | 40 | 92 | 10 | 0 | 40 | 10 | 192 |
| 15 | Platform Operations & Support | Technical | 4 | 24 | 62 | 4 | 0 | 22 | 9 | 121 |
| 16 | Legacy Case Migration | Technical | 3 | 28 | 54 | 4 | 0 | 18 | 7 | 111 |
| | **Total** | | **75** | **1360** | **2140** | **223** | **212** | **724** | **156** | **4815** |

## Feature-wise detail

### 01 — User, Role & Access Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F01-001 | Staff Authentication & Session Security | 8 | 11 | 36 | 62 | 11 | 0 | 24 | 3 | 136 | Go-live |
| F01-002 | Staff User Management & Role Assignment | 8 | 12 | 42 | 68 | 9 | 0 | 18 | 5 | 142 | Go-live |
| F01-003 | Permission Matrix & DS-wise Data Isolation | 6 | 9 | 38 | 74 | 6 | 0 | 24 | 5 | 147 | Go-live |
| F01-004 | Officer DSC Registration & Signing Authority | 5 | 7 | 22 | 40 | 4 | 8 | 12 | 4 | 90 | Go-live |

**Module total: 515 hours**

### 02 — Auction Rules & Configuration

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F02-001 | Instalment & Payment Rule Configuration | 6 | 7 | 38 | 40 | 6 | 0 | 18 | 3 | 105 | Go-live |
| F02-002 | Deputy Secretary Area Allocation Rules | 6 | 7 | 28 | 42 | 4 | 0 | 12 | 2 | 88 | Go-live |
| F02-003 | Approval Hierarchy & Bid Threshold Configuration | 5 | 7 | 32 | 38 | 4 | 0 | 14 | 2 | 90 | Go-live |
| F02-004 | Stage Timeline & Escalation Configuration | 4 | 5 | 18 | 28 | 2 | 0 | 12 | 2 | 62 | Go-live |
| F02-005 | Document Template Management | 5 | 7 | 32 | 38 | 4 | 0 | 12 | 3 | 89 | Go-live |
| F02-006 | Reference Masters | 6 | 5 | 26 | 26 | 5 | 0 | 6 | 2 | 65 | Go-live |

**Module total: 499 hours**

### 03 — KPPP Result Intake & Site Package

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F03-001 | KPPP Result Receipt through API | 4 | 8 | 20 | 52 | 14 | 24 | 20 | 5 | 135 | Go-live |
| F03-002 | Controlled KPPP Result Report Upload | 5 | 7 | 34 | 42 | 4 | 0 | 14 | 2 | 96 | Go-live |
| F03-003 | Result-to-Site Matching & Exception Resolution | 4 | 7 | 26 | 38 | 4 | 0 | 14 | 2 | 84 | Go-live |
| F03-004 | CDRMS Site Package Retrieval & Case File Creation | 4 | 7 | 20 | 40 | 10 | 24 | 14 | 3 | 111 | Go-live |
| F03-005 | Result Locking & Versioned Re-import | 4 | 6 | 26 | 36 | 4 | 0 | 8 | 2 | 76 | Go-live |

**Module total: 502 hours**

### 04 — Result Verification & Approval

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F04-001 | Site-wise Result Review Workbench | 7 | 8 | 42 | 44 | 4 | 0 | 16 | 3 | 109 | Go-live |
| F04-002 | Single-Bidder & Abnormal Bid Flagging | 3 | 6 | 12 | 32 | 2 | 0 | 12 | 2 | 60 | Go-live |
| F04-003 | Multi-Level Result Approval Workflow | 6 | 9 | 46 | 54 | 4 | 0 | 22 | 3 | 129 | Go-live |
| F04-004 | Draft Proceedings Generation | 4 | 6 | 18 | 28 | 2 | 0 | 6 | 1 | 55 | Go-live |
| F04-005 | Rejected & Unsold Site Intimation | 3 | 5 | 14 | 24 | 2 | 0 | 6 | 1 | 47 | Go-live |

**Module total: 400 hours**

### 05 — Successful Bidder Notification & Account

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F05-001 | Bidder Account Creation | 4 | 6 | 20 | 32 | 4 | 0 | 10 | 2 | 68 | Go-live |
| F05-002 | Bidder OTP Login & Profile | 4 | 6 | 18 | 24 | 3 | 0 | 10 | 2 | 57 | Go-live |
| F05-003 | Bilingual Signed Intimation Letter | 4 | 6 | 20 | 26 | 2 | 0 | 12 | 1 | 61 | Go-live |
| F05-004 | Result Intimation Dispatch & Delivery Status | 3 | 6 | 14 | 24 | 2 | 0 | 6 | 1 | 47 | Go-live |

**Module total: 233 hours**

### 06 — Payment & Instalment Management

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F06-001 | Instalment Schedule & Demand Generation | 3 | 6 | 16 | 34 | 4 | 0 | 14 | 2 | 70 | Go-live |
| F06-002 | Online Instalment Payment & Receipt | 6 | 9 | 32 | 58 | 6 | 24 | 20 | 5 | 145 | Go-live |
| F06-003 | Offline Payment Recording & Verification | 5 | 7 | 26 | 36 | 2 | 0 | 10 | 2 | 76 | Go-live |
| F06-004 | Daily Bank Reconciliation | 5 | 7 | 32 | 40 | 4 | 16 | 18 | 2 | 112 | Go-live |
| F06-005 | Payment Status & Ledger Tracking | 4 | 6 | 18 | 36 | 4 | 0 | 14 | 2 | 74 | Go-live |
| F06-006 | Payment Reminders & Overdue Monitoring | 3 | 5 | 14 | 24 | 2 | 0 | 10 | 1 | 51 | Go-live |
| F06-007 | Payment Extension Requests | 5 | 7 | 24 | 38 | 2 | 0 | 12 | 2 | 78 | Go-live |
| F06-008 | Default, Cancellation & Forfeiture Proceedings | 7 | 8 | 36 | 46 | 4 | 0 | 14 | 2 | 102 | Go-live |
| F06-009 | Payment Dispute Handling | 4 | 6 | 20 | 28 | 2 | 0 | 6 | 2 | 58 | Go-live |

**Module total: 766 hours**

### 07 — Case Forwarding & Deputy Secretary Processing

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F07-001 | Automatic Case Forwarding by Area | 2 | 5 | 8 | 22 | 1 | 0 | 6 | 1 | 38 | Go-live |
| F07-002 | Case Re-assignment | 3 | 5 | 12 | 22 | 2 | 0 | 6 | 1 | 43 | Go-live |
| F07-003 | Deputy Secretary Case File Workspace | 6 | 7 | 40 | 40 | 2 | 0 | 10 | 3 | 95 | Go-live |
| F07-004 | Case Processing, Document Requests & Bidder Uploads | 5 | 7 | 26 | 34 | 4 | 0 | 10 | 2 | 76 | Go-live |
| F07-005 | Processing Timelines & Pending Case Alerts | 2 | 4 | 10 | 22 | 2 | 0 | 6 | 1 | 41 | Go-live |

**Module total: 293 hours**

### 08 — Draft Sale Deed

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F08-001 | Draft Sale Deed Generation | 3 | 5 | 22 | 26 | 4 | 0 | 10 | 2 | 64 | Go-live |
| F08-002 | Sale Deed Review, Approval & Version History | 4 | 6 | 26 | 28 | 2 | 0 | 6 | 1 | 63 | Go-live |
| F08-003 | Bidder Access to Draft Sale Deed | 3 | 4 | 12 | 14 | 1 | 0 | 4 | 1 | 32 | Go-live |
| F08-004 | Final Instalment Demand Trigger | 1 | 3 | 4 | 14 | 0 | 0 | 4 | 1 | 23 | Go-live |

**Module total: 182 hours**

### 09 — Registration Recording & Completion

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F09-001 | Registration Details Recording | 3 | 4 | 12 | 14 | 2 | 0 | 4 | 1 | 33 | Go-live |
| F09-002 | Kaveri Registration Data Exchange (Conditional) | 1 | 3 | 4 | 12 | 1 | 24 | 6 | 2 | 49 | Conditional |
| F09-003 | Auction Process Completion | 3 | 4 | 12 | 20 | 1 | 0 | 6 | 1 | 40 | Go-live |
| F09-004 | Completion Status Sharing with Allotment Section & CDRMS | 2 | 4 | 8 | 20 | 1 | 16 | 6 | 2 | 53 | Go-live |

**Module total: 175 hours**

### 10 — Bidder Tracking Portal

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F10-001 | My Awarded Sites | 2 | 2 | 10 | 12 | 0 | 0 | 4 | 1 | 27 | Go-live |
| F10-002 | Awarded Site Details & Stage Tracker | 3 | 3 | 16 | 14 | 2 | 0 | 6 | 1 | 39 | Go-live |
| F10-003 | Bidder Payment History & Receipts | 3 | 3 | 12 | 12 | 0 | 0 | 4 | 1 | 29 | Go-live |
| F10-004 | Bidder Documents, Notifications & Profile | 3 | 3 | 14 | 12 | 1 | 0 | 4 | 1 | 32 | Go-live |
| F10-005 | Bilingual, Responsive & GIGW-Compliant Portal | 3 | 2 | 12 | 8 | 2 | 0 | 18 | 2 | 42 | Go-live |

**Module total: 169 hours**

### 11 — Dashboards, MIS & Reports

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F11-001 | Commissioner & Management Dashboard | 2 | 4 | 18 | 24 | 4 | 0 | 6 | 2 | 54 | Go-live |
| F11-002 | Deputy Secretary Dashboard | 2 | 3 | 10 | 14 | 0 | 0 | 6 | 1 | 31 | Go-live |
| F11-003 | Finance Dashboard | 2 | 3 | 10 | 14 | 0 | 0 | 6 | 1 | 31 | Go-live |
| F11-004 | Standard MIS Reports | 3 | 4 | 14 | 24 | 4 | 0 | 8 | 3 | 53 | Go-live |
| F11-005 | Configurable Report Builder | 3 | 5 | 20 | 34 | 2 | 0 | 8 | 2 | 66 | Go-live |

**Module total: 235 hours**

### 12 — Notification Service

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F12-001 | Bilingual Notification Template Management | 3 | 4 | 14 | 18 | 2 | 0 | 6 | 2 | 42 | Go-live |
| F12-002 | Stage Event Notification Engine | 1 | 5 | 6 | 28 | 4 | 0 | 8 | 2 | 48 | Go-live |
| F12-003 | Email, SMS & WhatsApp Gateway Connectors | 1 | 5 | 4 | 28 | 0 | 36 | 6 | 2 | 76 | Go-live |
| F12-004 | Notification Delivery Log | 2 | 3 | 10 | 14 | 4 | 0 | 4 | 1 | 33 | Go-live |

**Module total: 199 hours**

### 13 — Integration Hub

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F13-001 | Integration Framework & Credential Management | 2 | 5 | 10 | 30 | 6 | 0 | 8 | 3 | 57 | Go-live |
| F13-002 | Integration Monitoring & Error Queue | 2 | 5 | 12 | 24 | 2 | 0 | 6 | 2 | 46 | Go-live |
| F13-003 | DSC & e-Sign Signing Service | 3 | 5 | 14 | 32 | 2 | 24 | 8 | 2 | 82 | Go-live |
| F13-004 | BDA Web GIS Map Integration | 1 | 2 | 6 | 10 | 1 | 16 | 4 | 1 | 38 | Go-live |

**Module total: 223 hours**

### 14 — Audit, Security & Compliance

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F14-001 | Tamper-Evident Audit Trail | 0 | 4 | 0 | 24 | 6 | 0 | 8 | 3 | 41 | Go-live |
| F14-002 | Audit Viewer & Evidence Certificate Support | 4 | 4 | 20 | 26 | 0 | 0 | 6 | 2 | 54 | Go-live |
| F14-003 | Application Security Controls | 1 | 4 | 4 | 22 | 2 | 0 | 20 | 3 | 51 | Go-live |
| F14-004 | Personal Data Protection Compliance | 4 | 4 | 16 | 20 | 2 | 0 | 6 | 2 | 46 | Go-live |

**Module total: 192 hours**

### 15 — Platform Operations & Support

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F15-001 | Environments, CI/CD & Release Management | 0 | 3 | 0 | 18 | 0 | 0 | 6 | 3 | 27 | Go-live |
| F15-002 | Backup, Recovery & Disaster Recovery | 0 | 2 | 0 | 12 | 0 | 0 | 8 | 3 | 23 | Go-live |
| F15-003 | Monitoring, Availability & SLA Reporting | 2 | 3 | 10 | 16 | 2 | 0 | 4 | 2 | 34 | Go-live |
| F15-004 | Support Helpdesk & Ticket Tracking | 3 | 4 | 14 | 16 | 2 | 0 | 4 | 1 | 37 | Go-live |

**Module total: 121 hours**

### 16 — Legacy Case Migration

| Feature ID | Feature Name | Screens | APIs | UI | API | DB | Integ. | Test | Docs | Hours | Notes |
|------------|--------------|--------:|-----:|---:|---:|---:|---:|---:|---:|------:|-------|
| F16-001 | Migration Templates & Staging Load | 2 | 3 | 8 | 18 | 4 | 0 | 6 | 3 | 39 | Go-live |
| F16-002 | Migration Validation & Reconciliation | 3 | 3 | 16 | 18 | 0 | 0 | 6 | 2 | 42 | Go-live |
| F16-003 | Migrated Case Activation | 1 | 3 | 4 | 18 | 0 | 0 | 6 | 2 | 30 | Go-live |

**Module total: 111 hours**

## Effort profile

| Area | Hours | % |
|------|------:|---:|
| UI | 1360 | 28.2% |
| API | 2140 | 44.4% |
| Database | 223 | 4.6% |
| Integration | 212 | 4.4% |
| Testing | 724 | 15.0% |
| Documentation | 156 | 3.2% |

## Indicative phasing (from the SOW)

| Phase | Timeline | Modules |
|-------|----------|---------|
| SRS, integration study, prototype | T + 21 to T + 30 days | All (design) |
| Foundation | T + 30 to T + 45 days | 01, 02, 12, 13, 14, 15 |
| Intake, approval, bidder account | T + 40 to T + 60 days | 03, 04, 05 |
| Payments and DS processing | T + 50 to T + 75 days | 06, 07, 08, 09 |
| Portal, dashboards, migration | T + 60 to T + 90 days | 10, 11, 16 |
| UAT, VAPT, go-live | T + 75 to T + 100 days | All |

## Exclusions

- PM, SRS, prototype, training, help material, VAPT service, on-site staffing, warranty and O&M, hosting and gateway charges
