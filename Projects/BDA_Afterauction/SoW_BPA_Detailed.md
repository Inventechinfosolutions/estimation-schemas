# Statement of Work — BDA Post-Auction Award, Payment and Completion Management Module

**Client:** Bangalore Development Authority (BDA), T. Chowdaiah Road, Kumara Park West, Bengaluru – 560 020  
**System name:** BDA Auction Module (Post-Auction), referred to as "the Module"  
**Project code:** BPA  
**Document purpose:** Detailed Scope of Work for RFP response and effort estimation  
**Reference:** Section 6 of the Request for Proposal — Scope of Work

---

## 1. Introduction

Bangalore Development Authority (BDA) disposes of its sites and properties through e-auction. As directed by the Government, the e-auction, including live bidding, is conducted on the e-Auction module of the Karnataka Public Procurement Portal (KPPP).

Once KPPP declares the highest bidder, the remaining work is handled manually today: approval of the result, intimation to the successful bidder, collection of the sale consideration in instalments, processing of the case by the concerned Deputy Secretary, preparation of the draft sale deed and recording of registration. This causes delay, repeated office visits by bidders and the absence of a consolidated status of awarded sites.

This Statement of Work describes the design, development, implementation, warranty and maintenance of a Post-Auction Award, Payment and Completion Management Module that takes each awarded site from the KPPP result to the completion of the auction process.

## 2. Project Overview

| Item | Description |
|------|-------------|
| Client | Bangalore Development Authority (BDA) |
| System | BDA Auction Module (Post-Auction) |
| Starting point | Auction result for a site received from KPPP |
| End point | Site marked "Auction Process Completed" |
| Users | BDA officials (result verifiers, approving authorities, Deputy Secretaries, case workers, finance, administrators, management) and successful bidders |
| Channels | BDA staff portal (web) and Bidder Tracking Portal (web, mobile-responsive) |
| Key integrations | KPPP e-Auction module, CDRMS, BDA Web GIS, e-payment gateway and bank, e-mail / SMS / WhatsApp gateways, DSC / e-Sign, Kaveri (where permitted) |
| Hosting | Karnataka State Data Centre (SDC) or BDA-specified infrastructure |
| Timeline | Go-live at T + 100 days; final acceptance at T + 160 days (T = contract signing) |
| Support | One-year warranty and three-year operation and maintenance from go-live |

## 3. Project Objectives

1. Bring every awarded site onto a single digital workflow, from the KPPP result to completion, with no manual re-entry of data.
2. Ensure timely collection of the sale consideration through online payment, reminders and default handling.
3. Route each case automatically to the concerned Deputy Secretary based on area, with the complete case file.
4. Give the successful bidder online visibility of every stage, payment and document, reducing office visits.
5. Give BDA management real-time information on pendency, revenue realised and payments due.

## 4. In Scope / Out of Scope

### 4.1 In scope

- Receipt of the auction result from KPPP through API, or through controlled upload of KPPP result reports where the API is not available
- Matching of results with BDA site references and retrieval of the site package from CDRMS (read-only)
- Verification and multi-level approval of results, draft proceedings, and intimation of rejected or unsold sites to the allotment section
- Creation of the successful bidder's account, OTP login and bilingual, digitally signed intimation letter
- Instalment demands (25%, 50%, remaining 25%), online and offline payments, receipts, daily bank reconciliation, reminders, extensions, default proceedings and payment disputes
- Automatic forwarding of cases to Deputy Secretaries (DS1 / DS2 / DS3) by area, case processing, document requests and timelines
- Draft sale deed generation, review, approval and bidder access
- Recording of registration done outside the Module, data exchange with Kaveri where permitted, completion of the auction process and status update to the allotment section and CDRMS
- Bidder Tracking Portal in Kannada and English
- Dashboards, MIS reports and a configurable report builder
- Notifications by e-mail, SMS and WhatsApp (where enabled by BDA)
- Role-based access with DS-wise data isolation, tamper-evident audit trail, security and data protection controls
- Migration of pending cases from earlier auctions
- Training, documentation, warranty, operation and maintenance

### 4.2 Out of scope

- Any live bidding facility: bid submission, bid acceptance, delta time, auction closure, live monitoring or Force Close (performed on KPPP)
- Pre-auction activities: selection of sites in CDRMS, preparation of the site package, configuration, creation and publication of the auction on KPPP
- Bidder registration, DSC login for bidding, payment of participation fee and Earnest Money Deposit (EMD), and refund of EMD to unsuccessful bidders (performed on KPPP)
- Public auction information portal, pre-bid queries and site inspection booking
- Registration of the sale deed, which is done by the Department of Stamps and Registration outside the Module
- Hosting infrastructure, gateway and messaging charges, DSC tokens and certificates (provided by BDA)

## 5. Solution Expectations

- A single web application with a staff portal and a Bidder Tracking Portal, sharing one case record per awarded site
- Configurable business rules (instalment percentages, due periods, EMD adjustment, interest and penalty, DS area allocation, approval levels, thresholds, timelines and templates) maintained by the Auction Admin without code changes
- Workflow, documents and approvals embedded inside each business process; no separate document management product
- Digitally signed letters, approvals and draft sale deeds using DSC / e-Sign
- Bilingual (Kannada and English) bidder-facing content, letters and notifications
- Mobile-responsive bidder portal compliant with the Guidelines for Indian Government Websites (GIGW 3.0)
- Tamper-evident audit trail suitable for certification under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023

## 6. Consolidated Functional Modules

### 01. User, Role & Access Management

**Purpose:** Control access for BDA officials and enforce role permissions and DS-wise data isolation across the Module.

**Functional requirements:**
- Secure login for BDA officials with session management
- User management for all roles listed in Section 8
- Permissions configurable without code changes
- DS-wise data isolation: Deputy Secretaries and their case workers see only cases allocated to their DS office
- Registration of DSC certificates of approving officers and their signing authority

**Acceptance criteria:** Each role sees only the menus, actions and records permitted to it; DS-wise isolation is enforced on every screen, report and export; approving officers can sign only with a registered, valid DSC.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Staff Authentication & Session Security | Login for BDA officials with password policy, OTP verification, lockout and secure sessions |
| F01-002 | Staff User Management & Role Assignment | Create and maintain official accounts, assign roles and DS office |
| F01-003 | Permission Matrix & DS-wise Data Isolation | Configurable role permissions and DS-wise record visibility |
| F01-004 | Officer DSC Registration & Signing Authority | Register officers' DSC certificates and define what each officer may sign |

### 02. Auction Rules & Configuration

**Purpose:** Hold every rule and template that BDA may change over time, so that revisions to disposal rules can be applied without code changes.

**Functional requirements:**
- Instalment percentages, due periods, EMD adjustment, interest, penalty and grace rules, with effective dates
- Area allocation rules mapping layouts / areas to DS1, DS2 and DS3
- Approval levels (up to the Commissioner, the Authority or the Government) and thresholds for abnormal bids
- Processing timelines for each stage with alert and escalation rules
- Bilingual templates for intimation letters, proceedings, show-cause and cancellation notices and draft sale deeds
- Reference masters used across the Module

**Acceptance criteria:** A change to any rule takes effect from its effective date for new cases without code changes, and every change is versioned and audited.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Instalment & Payment Rule Configuration | Percentages, due periods, EMD adjustment, interest, penalty and extension rules |
| F02-002 | Deputy Secretary Area Allocation Rules | Map layouts and areas to DS1 / DS2 / DS3 with effective dates |
| F02-003 | Approval Hierarchy & Bid Threshold Configuration | Approval levels by case criteria and abnormal bid thresholds |
| F02-004 | Stage Timeline & Escalation Configuration | Time limits per stage, alerts and escalation rules |
| F02-005 | Document Template Management | Bilingual, versioned templates for letters, proceedings, notices and sale deeds |
| F02-006 | Reference Masters | Layouts, Sub-Registrar offices, bank accounts, document types, reasons and holidays |

### 03. KPPP Result Intake & Site Package

**Purpose:** Receive auction results from KPPP without manual re-entry and build the case file for each awarded site.

**Functional requirements:**
- Receipt of results through KPPP API: KPPP auction reference, BDA site reference, highest bidder details, final bid amount, result status and bid history where provided
- Where the API is not available, controlled upload of standard KPPP result reports (Excel / PDF) with format validation, row-level checks and hash-based integrity locking
- Matching of each result with the BDA site reference; flagging of unmatched, duplicate and withdrawn-site results for resolution
- Read-only retrieval of the site package from CDRMS: site details, GIS location and boundary, e-CDR, legal report, allotment section report, photographs and documents
- Locking of every imported result; any re-import is versioned with reason and approval

**Acceptance criteria:** Results are available in the Module within one hour of receipt by API and on the same working day by upload; no result can be altered after import; every awarded site has a complete case file before verification.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | KPPP Result Receipt through API | Automated receipt and creation of awarded site records from KPPP |
| F03-002 | Controlled KPPP Result Report Upload | Validated upload of KPPP Excel / PDF result reports with integrity locking |
| F03-003 | Result-to-Site Matching & Exception Resolution | Match results to BDA sites and resolve unmatched, duplicate and withdrawn cases |
| F03-004 | CDRMS Site Package Retrieval & Case File Creation | Read-only retrieval of the site package and creation of the case file |
| F03-005 | Result Locking & Versioned Re-import | Lock imported results and allow re-import only with reason and approval |

### 04. Result Verification & Approval

**Purpose:** Verify each KPPP result and obtain approval from the competent authority before the bidder is intimated.

**Functional requirements:**
- Site-wise display of upset price, final bid amount, premium over upset price, number of bidders and number of bids
- Flagging of single-bidder sites and abnormal bids against configurable thresholds
- Configurable approval workflow up to the Commissioner, the Authority or the Government, with remarks and DSC
- Site-wise decisions: confirm, reject or re-auction
- Generation of draft proceedings for approval of auction results
- Listing of rejected and unsold sites and intimation to the allotment section for re-auction

**Acceptance criteria:** No bidder is intimated before the result is approved at the required level; every decision is signed and recorded site-wise; rejected and unsold sites reach the allotment section.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Site-wise Result Review Workbench | Verify results with price, premium, bidder and bid indicators and the case file |
| F04-002 | Single-Bidder & Abnormal Bid Flagging | Automatic flags for single bidders and bids outside thresholds |
| F04-003 | Multi-Level Result Approval Workflow | Configurable, DSC-signed approval with confirm, reject or re-auction decisions |
| F04-004 | Draft Proceedings Generation | Generate draft proceedings for approval of auction results |
| F04-005 | Rejected & Unsold Site Intimation | List rejected and unsold sites and intimate the allotment section |

### 05. Successful Bidder Notification & Account

**Purpose:** Inform the successful bidder of the approved result and give them secure access to track their site.

**Functional requirements:**
- Automatic creation of a bidder account on approval
- Login with registered mobile number and e-mail through One Time Password (OTP)
- Downloadable intimation letter in Kannada and English, signed with DSC, with result details, site details, final bid amount, payment requirements and next steps
- E-mail and SMS notification with recording of delivery status

**Acceptance criteria:** Every approved result produces a bidder account, a signed bilingual intimation letter and notifications whose delivery status is recorded.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Bidder Account Creation | Automatic account creation for the successful bidder on approval |
| F05-002 | Bidder OTP Login & Profile | OTP login through mobile and e-mail, with profile management |
| F05-003 | Bilingual Signed Intimation Letter | Kannada and English intimation letter generated and signed with DSC |
| F05-004 | Result Intimation Dispatch & Delivery Status | Send intimation by e-mail and SMS and record delivery status |

### 06. Payment & Instalment Management

**Purpose:** Collect the sale consideration in instalments on time, with complete reconciliation and rule-based handling of extensions, defaults and disputes.

**Functional requirements:**
- Instalments: first 25% within 4 days of intimation; second 50% within 90 days; final 25% after the draft sale deed, as per BDA rules; all values configurable, including EMD adjustment
- Online payment through BDA's e-payment gateway (net banking, UPI, cards, NEFT / RTGS challan) with automatic receipt
- Recording of offline payments (Demand Draft, NEFT, RTGS) with proof upload and verification by the Payment Reconciler
- Daily bank reconciliation with settlement data; mismatch and pending-credit reports
- Payment history for bidders and officials with downloadable receipts
- Automatic reminders by e-mail and SMS before and after each due date
- Extension requests with interest or penalty computation and approval
- Default handling: show-cause, cancellation and forfeiture proceedings, and listing of the site for re-auction
- Payment disputes (debited but not credited, wrong amount) with acknowledgement, resolution timelines and escalation

**Acceptance criteria:** Payment status changes to "25% Payment Completed", "75% Payment Completed" and "100% Payment Completed" only on confirmed credit; reconciliation for the previous day is available by 11:00 hours; every extension, default and dispute follows the configured rules.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | Instalment Schedule & Demand Generation | Rule-based instalment schedule and demands with EMD adjustment |
| F06-002 | Online Instalment Payment & Receipt | Online payment through the e-payment gateway with automatic receipt |
| F06-003 | Offline Payment Recording & Verification | Record DD / NEFT / RTGS payments with proof and verify them |
| F06-004 | Daily Bank Reconciliation | Reconcile receipts with bank settlement data and report mismatches |
| F06-005 | Payment Status & Ledger Tracking | Site-wise payment ledger, instalment status and payment history |
| F06-006 | Payment Reminders & Overdue Monitoring | Reminders before and after due dates and overdue tracking |
| F06-007 | Payment Extension Requests | Bidder extension requests with interest or penalty and approval |
| F06-008 | Default, Cancellation & Forfeiture Proceedings | Show-cause, cancellation and forfeiture as per rules, and re-auction listing |
| F06-009 | Payment Dispute Handling | Register, track and resolve payment disputes with escalation |

### 07. Case Forwarding & Deputy Secretary Processing

**Purpose:** Route each case to the concerned Deputy Secretary after 75% payment and support processing to the draft sale deed stage.

**Functional requirements:**
- Automatic forwarding to DS1 / DS2 / DS3 on completion of 75% payment, by the area allocation rule
- Re-assignment by the Auction Admin with reason
- Case file view: site details and GIS location, auction and bidder details, e-CDR, legal report, allotment section report, documents and payment history
- Notes and remarks, requests for documents from the bidder, bidder uploads and status updates visible to the bidder
- Configurable processing timelines with pending-case alerts

**Acceptance criteria:** Every case reaching 75% is in the correct DS queue without manual action; all processing actions are visible in the case history; overdue cases are alerted.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F07-001 | Automatic Case Forwarding by Area | Forward cases to the correct DS queue on 75% payment |
| F07-002 | Case Re-assignment | Re-assign cases between DS offices and case workers with reason |
| F07-003 | Deputy Secretary Case File Workspace | Complete case file view for the DS and case worker |
| F07-004 | Case Processing, Document Requests & Bidder Uploads | Notes, document requests to the bidder, bidder uploads and status updates |
| F07-005 | Processing Timelines & Pending Case Alerts | Stage time limits, pending-case alerts and escalation |

### 08. Draft Sale Deed

**Purpose:** Prepare the draft sale deed from approved templates and make it available to the bidder.

**Functional requirements:**
- Generation from approved templates, auto-filled with site, bidder, auction and payment details
- Edit, review and approval by the DS office, with version history and digital signature
- Bidder view and download with status and date
- Raising of the demand for the remaining 25% on approval of the draft sale deed, where so configured

**Acceptance criteria:** Every draft sale deed is generated from an approved template version, every revision is retained, and the bidder sees only the approved version.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F08-001 | Draft Sale Deed Generation | Generate the draft sale deed from the approved template with case data |
| F08-002 | Sale Deed Review, Approval & Version History | Edit, review, sign and approve the draft with full version history |
| F08-003 | Bidder Access to Draft Sale Deed | Bidder views and downloads the approved draft with status and date |
| F08-004 | Final Instalment Demand Trigger | Raise the remaining 25% demand on draft approval, where configured |

### 09. Registration Recording & Completion

**Purpose:** Record the registration done outside the Module and close each site as completed.

**Functional requirements:**
- Recording of registration number, date, Sub-Registrar office and the registered sale deed copy
- Data exchange with the Kaveri system of the Department of Stamps and Registration, where permitted
- Marking of the site as "Auction Process Completed" with a completion record
- Sharing of completion status with the allotment section and CDRMS

**Acceptance criteria:** A site is completed only after 100% payment and recorded registration; completion is reflected in CDRMS.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F09-001 | Registration Details Recording | Record registration reference and upload the registered deed copy |
| F09-002 | Kaveri Registration Data Exchange (Conditional) | Fetch registration status from Kaveri where the Department permits |
| F09-003 | Auction Process Completion | Mark the site completed and generate the completion record |
| F09-004 | Completion Status Sharing with Allotment Section & CDRMS | Update the allotment section and the CDRMS site master |

### 10. Bidder Tracking Portal

**Purpose:** Give each successful bidder online visibility of their awarded sites, stages, payments and documents.

**Functional requirements:**
- My Awarded Sites, searchable by auction number, site number or layout, with status
- Awarded site details (auction number, site number, layout, area, final bid amount, auction date, photograph and map) and a tracker of all eleven stages with date and status
- Payment history, documents (intimation letter, receipts, draft sale deed, other letters), notifications and profile
- Mobile-responsive design, Kannada–English toggle and GIGW 3.0 compliance

**Acceptance criteria:** A bidder can see the current stage, dues and documents of every awarded site without visiting BDA.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F10-001 | My Awarded Sites | List and search all sites awarded to the bidder |
| F10-002 | Awarded Site Details & Stage Tracker | Site details, map and the eleven-stage tracker |
| F10-003 | Bidder Payment History & Receipts | Instalment dues, payments made and receipt downloads |
| F10-004 | Bidder Documents, Notifications & Profile | Letters and documents, notification inbox and profile |
| F10-005 | Bilingual, Responsive & GIGW-Compliant Portal | Kannada–English toggle, responsive layout and GIGW 3.0 accessibility |

### 11. Dashboards, MIS & Reports

**Purpose:** Give BDA management, Deputy Secretaries and Finance real-time information on pendency, collections and completion.

**Functional requirements:**
- Dashboards for the Commissioner, Deputy Secretaries and Finance: sites awarded, stage-wise pendency, payments due, received and overdue, revenue against upset price, defaulted, cancelled and completed sites
- Auction-wise, layout-wise, DS-wise and period-wise reports in Excel and PDF
- Configurable report builder for authorised users

**Acceptance criteria:** Dashboards reflect transactions in near real time and honour DS-wise isolation; reports export correctly to Excel and PDF.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F11-001 | Commissioner & Management Dashboard | Organisation-wide view of awards, pendency, revenue and completion |
| F11-002 | Deputy Secretary Dashboard | DS-wise case pendency, timelines and workload |
| F11-003 | Finance Dashboard | Dues, collections, overdue amounts and reconciliation status |
| F11-004 | Standard MIS Reports | Auction-, layout-, DS- and period-wise reports in Excel and PDF |
| F11-005 | Configurable Report Builder | Authorised users build and save their own reports |

### 12. Notification Service

**Purpose:** Send timely, bilingual notifications at every stage through e-mail, SMS and WhatsApp.

**Functional requirements:**
- Notifications for result intimation, payment demand, reminder, receipt, overdue, extension decision, case forwarded, document requested, draft sale deed available, 100% payment, registration recorded and process completed
- SMS with DLT-registered templates; WhatsApp where enabled by BDA
- Bilingual, configurable templates
- Recording of delivery status

**Acceptance criteria:** Every stage event produces the configured notifications in the bidder's preferred language, and delivery status is visible to officials.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F12-001 | Bilingual Notification Template Management | Configurable Kannada and English templates with DLT IDs |
| F12-002 | Stage Event Notification Engine | Trigger notifications on stage events and schedules |
| F12-003 | Email, SMS & WhatsApp Gateway Connectors | Connect to BDA's e-mail, SMS and WhatsApp gateways |
| F12-004 | Notification Delivery Log | Delivery status, retries and notification history |

### 13. Integration Hub

**Purpose:** Provide common, monitored integration services used by the business modules.

**Functional requirements:**
- Secure storage of integration credentials, retries and logging for all external calls
- Monitoring of integration health and an error queue for failed transactions
- DSC / e-Sign signing service used for intimation letters, approvals and draft sale deeds
- BDA Web GIS map display of awarded sites

**Acceptance criteria:** Failed external calls are retried and visible to administrators; signing and map services are available to all modules that need them.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F13-001 | Integration Framework & Credential Management | Common connector framework, credentials, retries and logging |
| F13-002 | Integration Monitoring & Error Queue | Integration health, failed transactions and reprocessing |
| F13-003 | DSC & e-Sign Signing Service | Shared signing and signature verification service |
| F13-004 | BDA Web GIS Map Integration | Map location and boundary of awarded sites |

### 14. Audit, Security & Compliance

**Purpose:** Make every action traceable and tamper-evident, and protect bidder and BDA data.

**Functional requirements:**
- Tamper-evident audit trail with cryptographic hash-chaining and NTP timestamps; logs read-only for all roles, including Super Admin
- Records maintained to support certification under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023
- Role-based access, OTP for bidders, DSC for approving officers, secure sessions, AES-256 encryption at rest, TLS 1.2 or above in transit and OWASP Top 10 compliance
- Compliance with the Digital Personal Data Protection Act, 2023, the Information Technology Act, 2000 and Government of Karnataka IT and security policies
- VAPT by a CERT-In empanelled auditor before go-live and annually

**Acceptance criteria:** Audit records cannot be altered by any role, and integrity verification detects any tampering; the Module passes VAPT before go-live.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F14-001 | Tamper-Evident Audit Trail | Hash-chained, NTP-timestamped, read-only audit of all actions |
| F14-002 | Audit Viewer & Evidence Certificate Support | Search audit records, verify integrity and support Section 63 certification |
| F14-003 | Application Security Controls | Encryption, session security, OWASP controls and rate limiting |
| F14-004 | Personal Data Protection Compliance | Privacy notice, consent, data principal requests and data retention |

### 15. Platform Operations & Support

**Purpose:** Run the Module reliably at the required service levels.

**Functional requirements:**
- Development, UAT and production environments with controlled releases
- Daily automated backups, RPO not exceeding 1 hour and RTO not exceeding 4 hours
- Monitoring of availability (99.5% monthly) and performance (3-second response, 500 concurrent users)
- Helpdesk tickets with severity-based resolution and monthly reports on system health, pendency and SLA compliance

**Acceptance criteria:** Backups and restores are tested; availability and SLA compliance are reported monthly from monitoring and helpdesk data.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F15-001 | Environments, CI/CD & Release Management | Separate environments and controlled build and release pipeline |
| F15-002 | Backup, Recovery & Disaster Recovery | Automated backups and recovery within RPO and RTO |
| F15-003 | Monitoring, Availability & SLA Reporting | Availability and performance monitoring and monthly SLA report |
| F15-004 | Support Helpdesk & Ticket Tracking | Severity-based tickets, resolution tracking and escalation |

### 16. Legacy Case Migration

**Purpose:** Bring awarded sites from earlier auctions whose post-auction process is pending into the Module from go-live.

**Functional requirements:**
- Migration of pending cases (payment, DS processing or registration stages)
- Migration plan, validation and sign-off by BDA before go-live

**Acceptance criteria:** Every pending case is migrated at its correct stage with its payment history, and BDA signs off reconciliation.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F16-001 | Migration Templates & Staging Load | Templates for legacy cases and payments and load into staging |
| F16-002 | Migration Validation & Reconciliation | Validate, reconcile and obtain BDA sign-off |
| F16-003 | Migrated Case Activation | Place migrated cases at the correct stage in the live workflow |

## 7. End-to-End Workflows

### 7.1 Awarded site flow

| Step | Stage | Actor | Output in the Module |
|------|-------|-------|----------------------|
| 1 | Auction result received from KPPP | System (integration) | Awarded site record created |
| 2 | Result verified and approved | Result Verifier / Approving Authority | Result approved |
| 3 | Successful bidder notification | System | Intimation letter, login credentials |
| 4 | 25% payment within 4 days | Successful bidder | Receipt; 25% completed |
| 5 | 50% payment within 90 days | Successful bidder | Receipt; 75% completed |
| 6 | Case forwarded to Deputy Secretary | System (area rule) | Case in DS1 / DS2 / DS3 queue |
| 7 | DS processing | Deputy Secretary and case worker | Case processed with remarks |
| 8 | Draft sale deed prepared | DS office | Draft sale deed available to bidder |
| 9 | Remaining 25% payment | Successful bidder | Receipt; 100% completed |
| 10 | Registration (outside the Module) | Bidder / DS office | Registration reference recorded |
| 11 | Auction process completed | DS office | Site closed as completed |

### 7.2 Exception flows

- **Unmatched or duplicate result:** flagged at intake, resolved by the Auction Admin before verification
- **Rejected or re-auction decision:** site listed for the allotment section; no bidder intimation
- **Extension:** bidder request, interest or penalty computed, approval, revised due date
- **Default:** overdue beyond the permitted period, show-cause, cancellation and forfeiture, re-auction listing
- **Payment dispute:** registered, acknowledged, resolved within timelines or escalated
- **Re-assignment:** Auction Admin moves a case between DS offices with reason

## 8. Access Control / RBAC

**Access model:** User → Role → Permissions, with DS-wise data isolation. Bidders use a separate OTP-based login and see only their own sites.

| Role | Main responsibilities |
|------|-----------------------|
| Successful Bidder | Track sites, pay instalments, upload documents, request extensions, raise disputes |
| Result Verifier | Verify KPPP results and prepare them for approval |
| Approving Authority | Approve, reject or order re-auction with DSC |
| Payment Reconciler | Verify offline payments and run bank reconciliation |
| Deputy Secretary (DS1 / DS2 / DS3) | Process cases, approve draft sale deeds, record completion |
| Case Worker | Prepare case notes, request documents, draft sale deeds |
| Finance Officer | Monitor collections, dues, reconciliation and disputes |
| Auction Admin | Configure rules and templates, resolve intake exceptions, re-assign cases |
| Super Admin | Manage users, roles and permissions |
| Read-only Viewer (Commissioner / management) | View dashboards and reports |

Permissions are configurable without code changes. DS-wise isolation applies to queues, case files, dashboards, reports and exports.

## 9. Channels

| Channel | Users | Notes |
|---------|-------|-------|
| BDA staff portal | All BDA roles | Web application on the BDA network and internet as permitted |
| Bidder Tracking Portal | Successful bidders | Mobile-responsive, Kannada–English, GIGW 3.0 |
| Notifications | Bidders and officials | E-mail, SMS (DLT templates), WhatsApp where enabled |

## 10. Integrations

| System | Purpose | Direction |
|--------|---------|-----------|
| KPPP e-Auction module | Receipt of auction results (API, or controlled report upload where the API is not available) | Inbound |
| CDRMS | Read-only retrieval of the site package; update of completion status | Inbound and outbound |
| BDA Web GIS | Map location and boundary of the awarded site | Inbound |
| e-Payment gateway and bank | Collection and reconciliation of instalment payments | Both |
| E-mail, SMS and WhatsApp gateways | Notifications | Outbound |
| DSC / e-Sign | Signing of intimation letters, approvals and draft sale deeds | Both |
| Kaveri (where permitted) | Registration status and reference | Inbound |

Non-availability of the KPPP API is handled through the controlled upload route and does not change the scope.

## 11. Audit, Compliance & Security

- Tamper-evident audit trail with hash-chaining and NTP-sourced timestamps; read-only for every role
- Support for certification of electronic records under Section 63 of the Bharatiya Sakshya Adhiniyam, 2023
- Role-based access, OTP for bidders, DSC for approving officers, secure session management
- AES-256 encryption at rest and TLS 1.2 or above in transit; OWASP Top 10 compliance
- VAPT by a CERT-In empanelled auditor before go-live and annually; high and critical findings closed within 7 days
- Compliance with the DPDP Act, 2023, the IT Act, 2000 and Government of Karnataka IT and security policies

## 12. Non-Functional Requirements

| Area | Requirement |
|------|-------------|
| Performance | Page response within 3 seconds under normal load; at least 500 concurrent users |
| Availability | 99.5% or higher per month; scheduled maintenance outside office hours |
| Backup and recovery | Daily automated backups; RPO not exceeding 1 hour; RTO not exceeding 4 hours |
| Hosting | Karnataka State Data Centre or BDA-specified infrastructure |
| Usability | Mobile-responsive bidder portal; Kannada and English; GIGW 3.0 |
| Integration timeliness | KPPP result import within 1 hour (API) or the same working day (upload); payment reconciliation daily by 11:00 hours |
| Support | Critical 4 hours, High 8 hours, Medium 2 working days, Low 5 working days |

## 13. Data Migration

In scope. Awarded sites from earlier auctions whose post-auction process is still pending (payment, DS processing or registration) are migrated so that they are tracked in the Module from go-live. The Service Provider prepares the migration plan and templates; BDA provides the legacy data and signs off validation before go-live.

## 14. Phased Delivery

The Module is delivered in a single implementation phase followed by stabilisation, warranty and maintenance.

| Sl. | Deliverable | Timeline |
|-----|-------------|----------|
| 1 | System Requirement Specification, including KPPP and CDRMS integration study, payment rules and DS area allocation rules | T + 21 days |
| 2 | UI/UX design and clickable prototype (BDA screens and Bidder Tracking Portal) | T + 30 days |
| 3 | Development of all modules and integrations; test reports | T + 75 days |
| 4 | User Acceptance Testing, VAPT report and data migration | T + 90 days |
| 5 | Go-live in production, with training completed | T + 100 days |
| 6 | Final acceptance after 60 days of stable operation | T + 160 days |
| 7 | Source code, database scripts and documentation handover | At final acceptance and on exit |
| 8 | Warranty (1 year) and operation and maintenance (3 years) | From go-live |

## 15. Deliverables

- System Requirement Specification and integration study
- UI/UX design and clickable prototype
- Tested application with all modules and integrations, and test reports
- VAPT report and closure of findings
- Migrated legacy cases with reconciliation sign-off
- Training (minimum two rounds per role), bidder help guide and short video tutorials in Kannada and English
- User manuals, administrator manual and technical documentation
- Source code and database scripts
- Monthly reports on system health, pendency, SLA compliance and issues resolved

## 16. Acceptance Criteria (Program Level)

1. All modules pass User Acceptance Testing against the approved System Requirement Specification.
2. KPPP results flow into the Module (API or upload) and every awarded site has a complete case file.
3. Instalment payments, receipts and daily reconciliation operate correctly with the e-payment gateway and bank.
4. Cases forward automatically to the correct DS office on 75% payment.
5. Draft sale deeds, registration recording and completion work end to end, with completion reflected in CDRMS.
6. VAPT is cleared before go-live.
7. Pending legacy cases are migrated and signed off.
8. The Module runs for 60 days after go-live within the agreed service levels.

## 17. Expected Benefits

- End-to-end visibility of every awarded site from result to completion
- Faster collection of sale consideration, with fewer defaults
- Fewer office visits by bidders through online tracking, payment and documents
- Consistent, rule-based handling of extensions, defaults and disputes
- Reliable, tamper-evident records for audit and legal purposes
- Real-time management information on pendency and revenue

## 18. Assumptions & Dependencies

1. KPPP provides the result API or, failing that, standard result reports in a stable format.
2. CDRMS provides read access to the site package and accepts completion status updates.
3. BDA provides the e-payment gateway, bank settlement files, e-mail, SMS (with DLT registration) and WhatsApp accounts, and the e-Sign / DSC arrangements.
4. Approving officers hold valid DSC tokens.
5. Kaveri data exchange is implemented only where the Department of Stamps and Registration permits it.
6. BDA provides approved templates for letters, proceedings, notices and the sale deed, and the payment and area allocation rules.
7. BDA provides legacy case data for migration in the agreed templates.
8. Hosting infrastructure is provided by BDA at the State Data Centre or as specified.
9. Workflow and document handling are embedded in each business process.
10. Access model: User → Role → Permissions with DS-wise data isolation; bidders have a separate OTP login.

## 19. Vendor Response Expectations

- Understanding of the post-auction process and the KPPP and CDRMS integration approach, including the upload fallback
- Approach to configurable rules, workflow, digital signing and bilingual content
- Security, audit and data protection approach, including Section 63 support
- Delivery plan aligned with the timelines in Section 14, and the proposed team
- Separate prices for (a) design, development and implementation and (b) operation and maintenance for three years

## Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User, Role & Access Management | Shared | F01-001 … F01-004 (4) |
| 02 | Auction Rules & Configuration | Business | F02-001 … F02-006 (6) |
| 03 | KPPP Result Intake & Site Package | Business | F03-001 … F03-005 (5) |
| 04 | Result Verification & Approval | Business | F04-001 … F04-005 (5) |
| 05 | Successful Bidder Notification & Account | Business | F05-001 … F05-004 (4) |
| 06 | Payment & Instalment Management | Business | F06-001 … F06-009 (9) |
| 07 | Case Forwarding & Deputy Secretary Processing | Business | F07-001 … F07-005 (5) |
| 08 | Draft Sale Deed | Business | F08-001 … F08-004 (4) |
| 09 | Registration Recording & Completion | Business | F09-001 … F09-004 (4) |
| 10 | Bidder Tracking Portal | Business | F10-001 … F10-005 (5) |
| 11 | Dashboards, MIS & Reports | Business | F11-001 … F11-005 (5) |
| 12 | Notification Service | Shared | F12-001 … F12-004 (4) |
| 13 | Integration Hub | Technical | F13-001 … F13-004 (4) |
| 14 | Audit, Security & Compliance | Technical | F14-001 … F14-004 (4) |
| 15 | Platform Operations & Support | Technical | F15-001 … F15-004 (4) |
| 16 | Legacy Case Migration | Technical | F16-001 … F16-003 (3) |

## Appendix B — Key Entities

Awarded site case; KPPP result and import batch; site package; bidder and bidder account; approval decision; proceedings; intimation letter; instalment demand; payment and receipt; reconciliation record; extension request; default proceeding; payment dispute; case assignment; case note and document request; draft sale deed and version; registration record; completion record; notification; audit record.

## Appendix C — Document Types

Intimation letter; draft proceedings; payment receipt; show-cause notice; cancellation and forfeiture order; extension order; document request letter; draft sale deed; registered sale deed copy; completion record; offline payment proof; bidder-submitted documents; site package documents (e-CDR, legal report, allotment section report, photographs).
