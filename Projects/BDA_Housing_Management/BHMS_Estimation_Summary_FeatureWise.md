# BHMS — Estimation Summary (Feature-Wise)

**Project:** BDA Housing Management System (BHMS)  
**Source:** `SoW_BHMS_Detailed.md`  
**Basis:** Estimation Master in `feature_schema.md`  
**Status:** Step 5–6 complete (access model: Person → Post → Role → Permissions)

> Roll-up: [`BHMS_Estimation_Summary.md`](BHMS_Estimation_Summary.md)

---

## 1. Grand totals

| Scope | Features | Hours |
|-------|----------|------:|
| All features (incl. DigiLocker/eKYC optional) | 75 | **3941** |
| Recommended go-live (excl. DigiLocker/eKYC) | 73 | **3855** |
| Optional connectors only | 2 | **86** |

**Access model note:** Officer authority follows **Person → Post → Role → Permissions**, with **Post → Manager Post** hierarchy. Approval levels map to Posts.

---

## 2. Module-wise summary

| # | Module | Type | Features | Hours |
|---|--------|------|----------|------:|
| 01 | User & Role Management | Shared | 7 | **395** |
| 02 | Master Data & System Configuration | Business | 5 | **249** |
| 03 | Housing Project Management | Business | 4 | **203** |
| 04 | Flats & Villas Inventory & Status | Business | 5 | **286** |
| 05 | Housing Notification Management | Business | 3 | **182** |
| 06 | Citizen Registration & Portal | Shared | 5 | **262** |
| 07 | Application & First-Come Booking | Business | 6 | **382** |
| 08 | Online Payment Management | Business | 5 | **311** |
| 09 | Allotment, Sale Deed, Registration & Possession | Business | 4 | **258** |
| 10 | Cancellation, Refund & Auto-Cancellation | Business | 4 | **249** |
| 11 | Bank / Loan NOC Management | Business | 4 | **147** |
| 12 | Notification Service | Technical | 6 | **214** |
| 13 | Integrations | Technical | 4 | **208** (base 122 / opt 86) |
| 14 | Analytics, Dashboards & Reports | Business | 8 | **317** |
| 15 | Data Migration | Shared | 5 | **278** |
| | **Go-live** | | **73** | **3855** |
| | **All-in** | | **75** | **3941** |

---

## 3. Feature-wise estimation

### Module 01: User & Role Management

**Type:** Shared  
**Module total:** **395 hours** · **7 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F01-001 | Person Master & Person–Post Mapping | 65 | Person occupies Post; no direct person roles |
| F01-002 | Roles & Permission Sets | 59 | Role → permissions; attached to Posts |
| F01-003 | Post Master, Post–Role & Post–Manager Mapping | 80 | Post has Role; Post → Manager Post |
| F01-004 | Authentication, Password & Session Security | 55 | Session resolves Post → Role → permissions |
| F01-005 | Citizen Credential Linkage | 38 | Citizen portal (unchanged model) |
| F01-006 | Login History & Access Audit | 43 | Includes Person/Post/Role context |
| F01-007 | Segregation-of-Duties Enforcement | 55 | Evaluated on Person/Post/Role |
| | **Subtotal** | **395** | |

### Module 02: Master Data & System Configuration

**Type:** Business  
**Module total:** **249 hours** · **5 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F02-001 | Housing Structure Masters | 41 | Included in module scope. |
| F02-002 | Charges & Document Type Masters | 41 | Included in module scope. |
| F02-003 | Notification Templates & System Parameters | 57 | Included in module scope. |
| F02-004 | Approval Workflow Configuration | 74 | Levels map to Posts (not persons) |
| F02-005 | Master Activate, Deactivate & Export | 36 | Included in module scope. |
| | **Subtotal** | **249** | |

### Module 03: Housing Project Management

**Type:** Business  
**Module total:** **203 hours** · **4 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F03-001 | Housing Project Register | 53 | Included in module scope. |
| F03-002 | Project Documents & Media | 40 | Included in module scope. |
| F03-003 | Project Publish Approval | 70 | Included in module scope. |
| F03-004 | Project History & Search | 40 | Included in module scope. |
| | **Subtotal** | **203** | |

### Module 04: Flats & Villas Inventory & Status

**Type:** Business  
**Module total:** **286 hours** · **5 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F04-001 | Flat & Villa Unit Register | 53 | Included in module scope. |
| F04-002 | Unit Pricing & Charges | 45 | Included in module scope. |
| F04-003 | Unit Documents & Media | 40 | Included in module scope. |
| F04-004 | Unit Status Lifecycle | 78 | Included in module scope. |
| F04-005 | Post-Publish Unit Change Approval | 70 | Included in module scope. |
| | **Subtotal** | **286** | |

### Module 05: Housing Notification Management

**Type:** Business  
**Module total:** **182 hours** · **3 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F05-001 | Housing Notification Create & Publish | 70 | Included in module scope. |
| F05-002 | Notification Extend, Modify & Withdraw | 70 | Included in module scope. |
| F05-003 | Citizen Active Notification Visibility | 42 | Included in module scope. |
| | **Subtotal** | **182** | |

### Module 06: Citizen Registration & Portal

**Type:** Shared  
**Module total:** **262 hours** · **5 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F06-001 | Citizen OTP Registration | 39 | OTP-verified identity capture |
| F06-002 | Citizen Profile, Login & Password | 39 | Self-service profile and credentials |
| F06-003 | Published Inventory Search & Compare | 61 | Published inventory discovery |
| F06-004 | Citizen Portal Shell & Ownership Isolation | 68 | Portal shell and ownership boundary |
| F06-005 | Citizen Downloads & Status Tracking | 55 | Personal tracking and released downloads |
| | **Subtotal** | **262** | |

### Module 07: Application & First-Come Booking

**Type:** Business  
**Module total:** **382 hours** · **6 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F07-001 | Online Application Submission | 78 | Citizen application intake |
| F07-002 | Officer-Assisted Application Entry | 47 | Same workflow through officer entry |
| F07-003 | Application Verification & Approval | 86 | Scrutiny and configured approvals |
| F07-004 | First-Come Booking Confirmation | 70 | Payment-gated FCFS booking |
| F07-005 | Concurrent Booking Exclusivity Controls | 62 | Double-booking prevention |
| F07-006 | Booking Confirmation & Receipts | 39 | Confirmation and receipt artefacts |
| | **Subtotal** | **382** | |

### Module 08: Online Payment Management

**Type:** Business  
**Module total:** **311 hours** · **5 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F08-001 | Payment Dues Ledger & Heads | 62 | Dues, heads, and balances |
| F08-002 | Online Payment Checkout & Status | 70 | Hub-backed checkout and status |
| F08-003 | Payment Receipts & History | 47 | Receipts and payment history |
| F08-004 | Payment Due Reminders | 62 | Due qualification and reminders |
| F08-005 | Accounts Reconciliation Views | 70 | Accounts exceptions and reconciliation |
| | **Subtotal** | **311** | |

### Module 09: Allotment, Sale Deed, Registration & Possession

**Type:** Business  
**Module total:** **258 hours** · **4 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F09-001 | Allotment Letter Generation | 62 | Approval-gated allotment letter |
| F09-002 | Draft Sale Deed Generate, Revise & Approve | 76 | Versioned deed drafting and approval |
| F09-003 | Offline Registration Record & Deed Upload | 50 | Offline registration recording |
| F09-004 | Possession Letter & Handover | 70 | Readiness-gated handover |
| | **Subtotal** | **258** | |

### Module 10: Cancellation, Refund & Auto-Cancellation

**Type:** Business  
**Module total:** **249 hours** · **4 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F10-001 | Voluntary Cancellation Request & Approval | 70 | Approval-controlled cancellation |
| F10-002 | Refund Calculation & Processing | 70 | Configurable refund calculation |
| F10-003 | Auto-Cancellation for Non-Payment | 62 | 130-day configurable auto-cancel |
| F10-004 | Inventory Release & Notifications Handoff | 47 | Safe inventory release and notices |
| | **Subtotal** | **249** | |

### Module 11: Bank / Loan NOC Management

**Type:** Business  
**Module total:** **147 hours** · **4 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F11-001 | NOC Request Capture | 31 |  |
| F11-002 | NOC Scrutiny & Approval | 54 |  |
| F11-003 | NOC Letter Issuance & Download | 31 |  |
| F11-004 | NOC Reissue, Withdraw & History | 31 |  |
| | **Subtotal** | **147** | |

### Module 12: Notification Service

**Type:** Technical  
**Module total:** **214 hours** · **6 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F12-001 | In-app & Portal Notification Framework | 31 |  |
| F12-002 | SMS Dispatch Service | 43 |  |
| F12-003 | Email Dispatch Service | 43 |  |
| F12-004 | OTP Notification Flow | 34 |  |
| F12-005 | Process Event Alert Orchestration | 35 |  |
| F12-006 | Notification Delivery Logging | 28 |  |
| | **Subtotal** | **214** | |

### Module 13: Integrations

**Type:** Technical  
**Module total:** **208 hours** · **4 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F13-001 | Payment Gateway Connector | 76 |  |
| F13-002 | Integration Authentication, Callback & Reconciliation | 46 |  |
| F13-003 | DigiLocker Connector (Optional) | 43 | OPTIONAL |
| F13-004 | Aadhaar eKYC Connector (Optional) | 43 | OPTIONAL |
| | **Subtotal** | **208** | |

### Module 14: Analytics, Dashboards & Reports

**Type:** Business  
**Module total:** **317 hours** · **8 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F14-001 | Analytics Shell & Role-Based Views | 39 |  |
| F14-002 | Management Dashboard | 39 |  |
| F14-003 | Engineering Dashboard | 39 |  |
| F14-004 | Accounts Dashboard | 39 |  |
| F14-005 | Citizen Dashboard | 39 |  |
| F14-006 | Standard Operational Reports | 40 |  |
| F14-007 | Financial, Refund & Cancellation Reports | 40 |  |
| F14-008 | PDF & Excel Export Framework | 42 |  |
| | **Subtotal** | **317** | |

### Module 15: Data Migration

**Type:** Shared  
**Module total:** **278 hours** · **5 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F15-001 | Migration Templates & Validation | 56 |  |
| F15-002 | Project & Unit Bulk Import | 56 |  |
| F15-003 | Booking & Applicant Bulk Import | 56 |  |
| F15-004 | Document Metadata Bulk Link | 46 |  |
| F15-005 | Trial, Final Reconciliation & Cutover | 64 |  |
| | **Subtotal** | **278** | |

## 4. Optional commercial line items

| Feature ID | Feature Name | Hours | Recommendation |
|------------|--------------|------:|----------------|
| F13-003 | DigiLocker Connector | 43 | Subject to BDA / legal approval |
| F13-004 | Aadhaar eKYC Connector | 43 | Subject to legal approval |
| | **Optional subtotal** | **86** | |

---

## 5. Exclusions (not in feature hours)

- Training, UAT, hypercare, warranty/AMC
- Hosting/infra and third-party licences
- Physical scanning of legacy files
- Native mobile apps; lottery/quota; Sub-Registrar online integration
