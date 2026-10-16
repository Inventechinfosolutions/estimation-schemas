# BDA Post-Auction Award, Payment and Completion Management Module — Module List

Source: `SoW_BPA_Detailed.md` (derived from `BDA PostAuction SoW.docx`, RFP Section 6)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User, Role & Access Management | Shared | Staff login and sessions, user and role management, configurable permissions with DS-wise isolation, officer DSC registration | Explicit |
| 02 | Auction Rules & Configuration | Business | Instalment and payment rules, DS area allocation, approval hierarchy and thresholds, stage timelines, document templates, reference masters | Explicit |
| 03 | KPPP Result Intake & Site Package | Business | KPPP API receipt, controlled report upload, matching and exceptions, CDRMS site package, locking and versioned re-import | Explicit |
| 04 | Result Verification & Approval | Business | Result review workbench, single-bidder and abnormal bid flags, multi-level DSC approval, draft proceedings, rejected / unsold intimation | Explicit |
| 05 | Successful Bidder Notification & Account | Business | Bidder account creation, OTP login and profile, bilingual DSC-signed intimation letter, dispatch with delivery status | Explicit |
| 06 | Payment & Instalment Management | Business | Instalment demands, online and offline payments, daily reconciliation, ledger, reminders, extensions, defaults and disputes | Explicit |
| 07 | Case Forwarding & Deputy Secretary Processing | Business | Automatic forwarding by area on 75% payment, re-assignment, case file workspace, processing and document requests, timelines and alerts | Explicit |
| 08 | Draft Sale Deed | Business | Template-based draft sale deed, review and approval with versions and DSC, bidder access, final instalment trigger | Explicit |
| 09 | Registration Recording & Completion | Business | Registration reference and deed copy, Kaveri exchange where permitted, completion record, status update to allotment section and CDRMS | Explicit |
| 10 | Bidder Tracking Portal | Business | My awarded sites, site details and eleven-stage tracker, payments and receipts, documents, notifications and profile, bilingual GIGW portal | Explicit |
| 11 | Dashboards, MIS & Reports | Business | Commissioner, DS and Finance dashboards, standard MIS reports, configurable report builder | Explicit |
| 12 | Notification Service | Shared | Bilingual DLT templates, stage event engine, e-mail / SMS / WhatsApp connectors, delivery log | Explicit |
| 13 | Integration Hub | Technical | Connector framework and credentials, integration monitoring and error queue, DSC / e-Sign service, Web GIS map | Derived |
| 14 | Audit, Security & Compliance | Technical | Hash-chained audit trail, audit viewer and Section 63 support, security controls, DPDP compliance | Explicit |
| 15 | Platform Operations & Support | Technical | Environments and releases, backup and DR, monitoring and SLA reporting, support helpdesk | Derived |
| 16 | Legacy Case Migration | Technical | Migration templates and staging, validation and reconciliation, activation of migrated cases at the correct stage | Explicit |

---

## Module Details

### 01. User, Role & Access Management

- **Type:** Shared
- **Summary:** Staff login and sessions, user and role management, configurable permissions with DS-wise isolation, officer DSC registration.
- **Source:** Explicit (SOW §4.10, §4.12)
- **In Scope:** Staff authentication with OTP and lockout; user register; role assignment with DS office; permission matrix; DS-wise record isolation; DSC certificate registration and signing authority
- **Out of Scope:** Bidder login (Module 05); single sign-on with other BDA systems
- **Key Actors:** Super Admin; Auction Admin; all BDA roles
- **Dependencies:** F12-003 (OTP SMS / e-mail); F13-003 (DSC verification); F14-001 (audit)
- **Notes:** Access model User → Role → Permissions with DS-wise data isolation; bidders use a separate OTP login
- **Features:** F01-001 Staff Authentication & Session Security, F01-002 Staff User Management & Role Assignment, F01-003 Permission Matrix & DS-wise Data Isolation, F01-004 Officer DSC Registration & Signing Authority

### 02. Auction Rules & Configuration

- **Type:** Business
- **Summary:** Instalment and payment rules, DS area allocation, approval hierarchy and thresholds, stage timelines, document templates, reference masters.
- **Source:** Explicit (SOW §4.2, §4.4A, §4.5, §4.6, §4.11)
- **In Scope:** Versioned, effective-dated rules and bilingual templates maintained by the Auction Admin
- **Out of Scope:** Notification templates (Module 12)
- **Key Actors:** Auction Admin; Super Admin; Approving Authority (template approval)
- **Dependencies:** Consumed by Modules 03–09
- **Notes:** Delivers the 'no code change for rule revisions' requirement
- **Features:** F02-001 Instalment & Payment Rule Configuration, F02-002 Deputy Secretary Area Allocation Rules, F02-003 Approval Hierarchy & Bid Threshold Configuration, F02-004 Stage Timeline & Escalation Configuration, F02-005 Document Template Management, F02-006 Reference Masters

### 03. KPPP Result Intake & Site Package

- **Type:** Business
- **Summary:** KPPP API receipt, controlled report upload, matching and exceptions, CDRMS site package, locking and versioned re-import.
- **Source:** Explicit (SOW §4.1)
- **In Scope:** Result intake by API or upload; site matching; exception queue; read-only site package; integrity lock; re-import with approval
- **Out of Scope:** Any live bidding or pre-auction activity on KPPP
- **Key Actors:** System; Auction Admin; Result Verifier
- **Dependencies:** F13-001; F02-006; KPPP and CDRMS access
- **Notes:** Upload route ensures scope is not blocked if the KPPP API is unavailable
- **Features:** F03-001 KPPP Result Receipt through API, F03-002 Controlled KPPP Result Report Upload, F03-003 Result-to-Site Matching & Exception Resolution, F03-004 CDRMS Site Package Retrieval & Case File Creation, F03-005 Result Locking & Versioned Re-import

### 04. Result Verification & Approval

- **Type:** Business
- **Summary:** Result review workbench, single-bidder and abnormal bid flags, multi-level DSC approval, draft proceedings, rejected / unsold intimation.
- **Source:** Explicit (SOW §4.2)
- **In Scope:** Verification, flags, configurable approval up to Government, site-wise decisions, proceedings, allotment section intimation
- **Out of Scope:** Re-auction execution on KPPP
- **Key Actors:** Result Verifier; Approving Authority; Auction Admin
- **Dependencies:** Module 03; F02-003; F02-005; F13-003
- **Notes:** Workflow embedded; no separate workflow module
- **Features:** F04-001 Site-wise Result Review Workbench, F04-002 Single-Bidder & Abnormal Bid Flagging, F04-003 Multi-Level Result Approval Workflow, F04-004 Draft Proceedings Generation, F04-005 Rejected & Unsold Site Intimation

### 05. Successful Bidder Notification & Account

- **Type:** Business
- **Summary:** Bidder account creation, OTP login and profile, bilingual DSC-signed intimation letter, dispatch with delivery status.
- **Source:** Explicit (SOW §4.3)
- **In Scope:** Account on approval; mobile / e-mail OTP; intimation letter; e-mail and SMS dispatch
- **Out of Scope:** Bidder registration on KPPP
- **Key Actors:** System; Successful Bidder; Auction Admin
- **Dependencies:** Module 04; F02-005; Module 12; F13-003
- **Notes:** Bidder login is separate from staff login
- **Features:** F05-001 Bidder Account Creation, F05-002 Bidder OTP Login & Profile, F05-003 Bilingual Signed Intimation Letter, F05-004 Result Intimation Dispatch & Delivery Status

### 06. Payment & Instalment Management

- **Type:** Business
- **Summary:** Instalment demands, online and offline payments, daily reconciliation, ledger, reminders, extensions, defaults and disputes.
- **Source:** Explicit (SOW §4.4)
- **In Scope:** 25% / 50% / 25% instalments with EMD adjustment; gateway payments; offline verification; bank reconciliation; extension, default and dispute handling
- **Out of Scope:** EMD collection and refund (KPPP); accounting system postings
- **Key Actors:** Successful Bidder; Payment Reconciler; Finance Officer; Approving Authority; Auction Admin
- **Dependencies:** F02-001; Module 12; e-payment gateway and bank settlement files
- **Notes:** Highest-risk financial module; gateway connector is built here
- **Features:** F06-001 Instalment Schedule & Demand Generation, F06-002 Online Instalment Payment & Receipt, F06-003 Offline Payment Recording & Verification, F06-004 Daily Bank Reconciliation, F06-005 Payment Status & Ledger Tracking, F06-006 Payment Reminders & Overdue Monitoring, F06-007 Payment Extension Requests, F06-008 Default, Cancellation & Forfeiture Proceedings, F06-009 Payment Dispute Handling

### 07. Case Forwarding & Deputy Secretary Processing

- **Type:** Business
- **Summary:** Automatic forwarding by area on 75% payment, re-assignment, case file workspace, processing and document requests, timelines and alerts.
- **Source:** Explicit (SOW §4.5)
- **In Scope:** DS1 / DS2 / DS3 queues; case file; notes; bidder document requests and uploads; stage timers
- **Out of Scope:** Registration of the deed
- **Key Actors:** Deputy Secretary; Case Worker; Auction Admin; Successful Bidder
- **Dependencies:** F02-002; F02-004; F06-005; Module 03 (site package)
- **Notes:** DS-wise isolation from F01-003 applies
- **Features:** F07-001 Automatic Case Forwarding by Area, F07-002 Case Re-assignment, F07-003 Deputy Secretary Case File Workspace, F07-004 Case Processing, Document Requests & Bidder Uploads, F07-005 Processing Timelines & Pending Case Alerts

### 08. Draft Sale Deed

- **Type:** Business
- **Summary:** Template-based draft sale deed, review and approval with versions and DSC, bidder access, final instalment trigger.
- **Source:** Explicit (SOW §4.6)
- **In Scope:** Generation, editing, approval, signing, bidder download, final 25% demand
- **Out of Scope:** Stamp duty computation and registration
- **Key Actors:** Case Worker; Deputy Secretary; Successful Bidder
- **Dependencies:** F02-005; F13-003; F06-001
- **Notes:** —
- **Features:** F08-001 Draft Sale Deed Generation, F08-002 Sale Deed Review, Approval & Version History, F08-003 Bidder Access to Draft Sale Deed, F08-004 Final Instalment Demand Trigger

### 09. Registration Recording & Completion

- **Type:** Business
- **Summary:** Registration reference and deed copy, Kaveri exchange where permitted, completion record, status update to allotment section and CDRMS.
- **Source:** Explicit (SOW §4.7)
- **In Scope:** Registration capture; conditional Kaveri link; completion; CDRMS write-back
- **Out of Scope:** Registration itself (Department of Stamps and Registration)
- **Key Actors:** Case Worker; Deputy Secretary; Successful Bidder; System
- **Dependencies:** Module 06 (100% payment); F13-001; CDRMS update access
- **Notes:** Kaveri exchange is conditional on departmental permission
- **Features:** F09-001 Registration Details Recording, F09-002 Kaveri Registration Data Exchange (Conditional), F09-003 Auction Process Completion, F09-004 Completion Status Sharing with Allotment Section & CDRMS

### 10. Bidder Tracking Portal

- **Type:** Business
- **Summary:** My awarded sites, site details and eleven-stage tracker, payments and receipts, documents, notifications and profile, bilingual GIGW portal.
- **Source:** Explicit (SOW §4.8)
- **In Scope:** Self-service tracking for successful bidders in Kannada and English
- **Out of Scope:** Public auction information portal
- **Key Actors:** Successful Bidder
- **Dependencies:** Modules 05–09; F13-004
- **Notes:** Payment initiation and uploads reuse Module 06 and 07 operations
- **Features:** F10-001 My Awarded Sites, F10-002 Awarded Site Details & Stage Tracker, F10-003 Bidder Payment History & Receipts, F10-004 Bidder Documents, Notifications & Profile, F10-005 Bilingual, Responsive & GIGW-Compliant Portal

### 11. Dashboards, MIS & Reports

- **Type:** Business
- **Summary:** Commissioner, DS and Finance dashboards, standard MIS reports, configurable report builder.
- **Source:** Explicit (SOW §4.9)
- **In Scope:** Role dashboards; auction-, layout-, DS- and period-wise reports in Excel / PDF; report builder
- **Out of Scope:** External BI tools
- **Key Actors:** Commissioner / Read-only Viewer; Deputy Secretary; Finance Officer; Auction Admin
- **Dependencies:** All business modules; F01-003
- **Notes:** DS-wise isolation applies to all outputs
- **Features:** F11-001 Commissioner & Management Dashboard, F11-002 Deputy Secretary Dashboard, F11-003 Finance Dashboard, F11-004 Standard MIS Reports, F11-005 Configurable Report Builder

### 12. Notification Service

- **Type:** Shared
- **Summary:** Bilingual DLT templates, stage event engine, e-mail / SMS / WhatsApp connectors, delivery log.
- **Source:** Explicit (SOW §4.11)
- **In Scope:** Event and schedule-based notifications for every stage; delivery tracking
- **Out of Scope:** Gateway subscription charges
- **Key Actors:** Auction Admin; System; recipients
- **Dependencies:** BDA e-mail, SMS (DLT) and WhatsApp accounts; F13-001
- **Notes:** Used by Modules 01 and 03–10
- **Features:** F12-001 Bilingual Notification Template Management, F12-002 Stage Event Notification Engine, F12-003 Email, SMS & WhatsApp Gateway Connectors, F12-004 Notification Delivery Log

### 13. Integration Hub

- **Type:** Technical
- **Summary:** Connector framework and credentials, integration monitoring and error queue, DSC / e-Sign service, Web GIS map.
- **Source:** Derived (SOW §4.13)
- **In Scope:** Shared integration services; signing; maps
- **Out of Scope:** KPPP, CDRMS, payment and Kaveri business mapping (built in owning features)
- **Key Actors:** Super Admin; Auction Admin; System
- **Dependencies:** BDA e-Sign / DSC arrangement; BDA Web GIS service
- **Notes:** Business connectors live in Modules 03, 06 and 09 and reuse this framework
- **Features:** F13-001 Integration Framework & Credential Management, F13-002 Integration Monitoring & Error Queue, F13-003 DSC & e-Sign Signing Service, F13-004 BDA Web GIS Map Integration

### 14. Audit, Security & Compliance

- **Type:** Technical
- **Summary:** Hash-chained audit trail, audit viewer and Section 63 support, security controls, DPDP compliance.
- **Source:** Explicit (SOW §4.12)
- **In Scope:** Tamper-evident audit; integrity verification; encryption; OWASP controls; privacy and data principal requests
- **Out of Scope:** VAPT execution by the CERT-In empanelled auditor
- **Key Actors:** Super Admin; auditors; Successful Bidder (privacy requests)
- **Dependencies:** NTP source; hosting key management
- **Notes:** Audit is read-only for every role including Super Admin
- **Features:** F14-001 Tamper-Evident Audit Trail, F14-002 Audit Viewer & Evidence Certificate Support, F14-003 Application Security Controls, F14-004 Personal Data Protection Compliance

### 15. Platform Operations & Support

- **Type:** Technical
- **Summary:** Environments and releases, backup and DR, monitoring and SLA reporting, support helpdesk.
- **Source:** Derived (SOW §4.14, §4.17, §8)
- **In Scope:** Dev / UAT / production; pipelines; backups within RPO / RTO; availability monitoring; tickets and monthly report
- **Out of Scope:** Hosting infrastructure and licences
- **Key Actors:** Super Admin; support team; BDA IT
- **Dependencies:** State Data Centre or BDA infrastructure
- **Notes:** Supports SLA measurement and monthly reporting
- **Features:** F15-001 Environments, CI/CD & Release Management, F15-002 Backup, Recovery & Disaster Recovery, F15-003 Monitoring, Availability & SLA Reporting, F15-004 Support Helpdesk & Ticket Tracking

### 16. Legacy Case Migration

- **Type:** Technical
- **Summary:** Migration templates and staging, validation and reconciliation, activation of migrated cases at the correct stage.
- **Source:** Explicit (SOW §4.15)
- **In Scope:** Pending cases from earlier auctions with payments and documents
- **Out of Scope:** Data entry of paper records (BDA provides data in templates)
- **Key Actors:** Auction Admin; Finance Officer; Deputy Secretary; migration team
- **Dependencies:** Modules 03–09; legacy data from BDA
- **Notes:** BDA sign-off required before go-live
- **Features:** F16-001 Migration Templates & Staging Load, F16-002 Migration Validation & Reconciliation, F16-003 Migrated Case Activation

## Excluded / Embedded Capabilities

- **Workflow / approvals:** embedded in Modules 04 (result approval), 06 (extension, default, dispute), 07 (case processing) and 08 (deed approval); no separate workflow engine module.
- **Document management:** embedded — site package (F03-004), letters and proceedings (F04-004, F05-003), payment proofs (F06-003), bidder uploads (F07-004), sale deed versions (F08-002), registered deed (F09-001).
- **Scheduler / background jobs:** embedded in F03-001 (KPPP polling), F06-004 (daily reconciliation), F06-006 (reminders), F07-005 (timers), F12-002 (scheduled notifications).
- **Live bidding, pre-auction, EMD and bidder registration:** out of scope (KPPP).
- **VAPT execution and annual VAPT:** service by a CERT-In empanelled auditor; remediation is covered under warranty.
- **Training, help guides and video tutorials:** service deliverables, outside feature hours.

## Assumptions

1. Access model is User → Role → Permissions with DS-wise data isolation; bidders use a separate OTP login.
2. KPPP and CDRMS business connectors are built in the owning features (F03-001, F03-004, F09-004) on top of the Integration Hub framework (F13-001).
3. The e-payment gateway connector and bank settlement intake are built in Module 06.
4. Kaveri data exchange (F09-002) is conditional on permission from the Department of Stamps and Registration.
5. BDA supplies approved templates, rules and legacy data in agreed formats.

## Risks

1. KPPP API availability and result format stability are outside BDA's and the vendor's control; the upload route mitigates this.
2. CDRMS site package completeness affects case file quality and DS processing.
3. Gateway settlement file formats vary by bank and may need rework.
4. Tight timeline (development by T + 75 days) against the size of the scope.
5. Legacy data quality for pending cases is unknown.
