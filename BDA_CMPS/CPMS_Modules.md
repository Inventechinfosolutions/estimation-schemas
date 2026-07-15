# BDA Commercial Property Management System (CPMS) — Module List

Source: `SoW_CPMS_Detailed.md`

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User & Role Management | Shared | Authentication, roles, permissions, and data-scope access control | Explicit in document (SOW §6 Module 1.C / §8); separated for implementation |
| 02 | Master Data & System Configuration | Business | Configurable masters, business rules, system parameters, and approval workflow configuration | Explicit in document (SOW §6 Module 1) |
| 03 | Property & Asset Inventory | Business | Commercial property, building, unit, parking inventory, status lifecycle, and vacancy tracking | Explicit in document (SOW §6 Module 2) |
| 04 | Tenant & Lease Lifecycle | Business | Tenant onboarding, allotment/lease, handover, renewal/termination, and security deposits | Explicit in document (SOW §6 Module 3) |
| 05 | Revenue Billing & Collections | Business | Rent demand, collections, receipts, arrears, penalties, GST, and tenant payments | Explicit in document (SOW §6 Module 4) |
| 06 | Utilities & Statutory Payments | Business | Utility meters/bills/recovery and property tax assessment/payment tracking | Explicit in document (SOW §6 Module 5) |
| 07 | Operations, Maintenance & Expenditure | Business | Complaints, work orders, inspections, vendors/contractors, and property expenditure | Explicit in document (SOW §6 Module 6) |
| 08 | Document Management | Shared | Central document repository, versioning, notice PDF archive, and entity-linked artefacts | Explicit in document (SOW §6 Module 7) |
| 09 | Notification Service | Technical | SMS, email, and in-app notification dispatch for OTPs, notices, reminders, and workflow alerts | Added for implementation (derived from SOW §6 Module 7.B / §9) |
| 10 | API / Integration Hub | Technical | External connectors for payment gateway, GIS/maps, and optional ERP/Treasury/DigiLocker/eKYC | Added for implementation (derived from SOW §9) |
| 11 | Analytics, Dashboards & Reports | Business | Operational/executive dashboards, MIS, and exportable management reports | Explicit in document (SOW §6 Module 8) |

---

## Module Details

### 01. User & Role Management

- **Type:** Shared
- **Summary:** Provide secure login, role-based access, permission sets, and property/location data scoping for all users including tenant portal accounts.
- **Source:** Explicit in document (bundled under SOW Module 1.C and §8); extracted as a Shared module per schema defaults (Identity & Access).
- **In Scope:**
  - User create/update, activate/deactivate
  - Roles (indicative list in SOW §8.1) and permission sets (module + action)
  - Map users to organizational units / properties (data scope)
  - Secure login, password policy, session timeout, optional 2FA
  - Tenant portal credential issuance and reset
  - Login history and user activity logs (access-related)
  - Segregation-of-duties support for sensitive finance actions
- **Out of Scope:**
  - External IdP/SSO federation unless later specified
  - Full SIEM product; application-level activity logs only
- **Key Actors:** Super Administrator, Auditor, all officer roles (consumers), Tenant (portal login)
- **Dependencies:** None (foundation). Consumed by all modules.
- **Notes:** Workflow *configuration* remains in Module 02; runtime approvals execute inside business modules using roles from this module.

---

### 02. Master Data & System Configuration

- **Type:** Business
- **Summary:** Maintain configurable property/location/rental/financial masters, effective-dated business rules, notice templates, system parameters, and approval workflow definitions.
- **Source:** Explicit in document (SOW §6 Module 1), excluding User & Role (moved to Module 01).
- **In Scope:**
  - Property & location masters: Complex, Building, Floor, Shop/Unit, Parking Area, Open Space, Utility Meter, Asset; Zone → Division → Circle → Ward → Layout → Survey Number
  - Rental & financial masters: Property Category/Type, Lease Type, Rent Revision / Penalty / Deposit rules, GST configuration, Expense/Income categories, Utility Types, Tax Types, Payment Modes, Bank Masters
  - Effective dating / versioning for rules that change over time
  - Activate/deactivate masters without breaking historical references
  - Approval workflow configuration by transaction type and amount threshold
  - Notice template configuration (merge-field definitions for SMS/email/PDF)
  - System parameters (financial year, billing cut-off, receipt series, etc.)
  - Search, filter, export of masters
- **Out of Scope:**
  - Transactional property register (Module 03)
  - User/role administration (Module 01)
  - Building a standalone generic workflow product beyond configurable approval definitions used by business modules
- **Key Actors:** Super Administrator, Estate Officer, Accounts Officer, Data Entry Operator
- **Dependencies:** Module 01 (permissions)
- **Notes:** Individual CRUD masters are grouped here intentionally as in the SOW; do not split into one module per master table.

---

### 03. Property & Asset Inventory

- **Type:** Business
- **Summary:** System of record for commercial properties, buildings, units, parking inventory, status lifecycle, geo-tagging, and vacancy management.
- **Source:** Explicit in document (SOW §6 Module 2)
- **In Scope:**
  - Property and building register with hierarchy Complex → Building → Floor → Unit/Shop/Parking/Open space
  - Areas, photos, documents linkage, geo-location (map pin)
  - Status lifecycle: Vacant, Occupied, Under Maintenance, Reserved, Auctioned, Under Litigation, Blocked
  - Computed building occupancy %
  - Parking inventory and occupancy classification (visitor/reserved)
  - Vacancy tracking: vacant since, expected revenue loss, marketing status, inspection readiness, proposed rent, ready-for-allocation
  - Status-change approvals where configured
- **Out of Scope:**
  - E-auction / public bidding portal (SOW out of scope)
  - Full litigation/case management beyond status, dates, and linked documents
  - Lease creation (Module 04); masters definition (Module 02)
- **Key Actors:** Estate Officer, Property Manager, Commissioner (approvals), Data Entry Operator
- **Dependencies:** Module 01, Module 02; GIS via Module 10; documents via Module 08
- **Notes:** Parking *rent* and allocation to lease are fulfilled with Modules 04–05; this module owns parking as inventory/units.

---

### 04. Tenant & Lease Lifecycle

- **Type:** Business
- **Summary:** Manage tenants, application-to-lease allotment, handover, amendments, renewals/termination, and security deposit lifecycle.
- **Source:** Explicit in document (SOW §6 Module 3)
- **In Scope:**
  - Tenant types and profiles (Individual, Partnership, Company, Trust, Society) including KYC/GST/PAN/Aadhaar fields as applicable
  - Duplicate detection (configurable)
  - Allocation process: availability → application → verification → approval → agreement → deposit → handover → billing start → renewal/termination
  - Lease data, multi-unit/parking linkage, escalation, grace/penalty rule linkage, amendments with history
  - Security deposit collection, adjustment, refund, forfeiture, optional interest
  - Lease-related notice triggers (expiry/renewal/eviction templates) — generation coordinated with Modules 08–09
  - Tenant portal: lease summary view (portal shell features estimated with consuming modules)
- **Out of Scope:**
  - Court process / full legal case management
  - Auction bidding engine
  - Aadhaar eKYC / DigiLocker automation (optional via Module 10)
  - Recurring rent demand engine (Module 05)
- **Key Actors:** Estate Officer, Property Manager, Accounts Officer, Tenant (portal), Approvers
- **Dependencies:** Modules 01–03; Module 08 (KYC/lease docs); Module 09 (notices); Module 05 for post-handover billing commencement
- **Notes:** Vacancy-to-allocation flow spans Modules 03 and 04.

---

### 05. Revenue Billing & Collections

- **Type:** Business
- **Summary:** Automate rent and related demand generation, multi-mode collections, receipts, arrears/ageing, penalties, GST, and online payments.
- **Source:** Explicit in document (SOW §6 Module 4)
- **In Scope:**
  - Scheduled and ad-hoc demand generation (rent, advance, arrears, penalties, GST, interest, misc, parking, CAM/lease-linked charges)
  - Bulk bill run with exception report; credit notes / demand cancellation with maker-checker
  - Collections: online gateway, UPI, bank transfer, NEFT/RTGS, DD, cheque, cash (as enabled)
  - Cheque bounce / realization handling; partial payment allocation rules
  - Digital receipts, payment history, outstanding statements
  - Defaulter/ageing views and rent due/overdue notice triggers
  - Tenant portal: view dues, pay online, download receipts/statements
- **Out of Scope:**
  - Full GL / ERP accounting (hooks only via Module 10)
  - Utility bill calculation engines owned by Module 06 (may post recoverable charges into tenant dues)
- **Key Actors:** Accounts Officer, Revenue Officer, Tenant (portal), Auditor
- **Dependencies:** Modules 01–04; Module 10 (payment gateway); Module 09 (reminders); Module 08 (receipt PDFs)
- **Notes:** Payment gateway connector implementation effort sits primarily in Module 10; this module owns billing/collection business logic and reconciliation UX.

---

### 06. Utilities & Statutory Payments

- **Type:** Business
- **Summary:** Track utility consumption and payments and maintain property tax assessments, challans, receipts, and outstanding tax.
- **Source:** Explicit in document (SOW §6 Module 5)
- **In Scope:**
  - Utilities: Electricity, Water, DG, CAM, Sewage, other configurable types
  - Meter linkage, readings validation, consumption, bill amount, due date, payment status, bill uploads
  - BDA-paid utilities with optional recovery to tenant lease account
  - Property tax assessments, dues, payments, challan/receipt upload, history, outstanding
  - Cross-link tax payments to expenditure where applicable (Module 07)
  - Overdue utility/tax notice candidates
- **Out of Scope:**
  - External utility company portals / automated bill fetch unless later integrated
  - Municipal tax assessment calculation engine beyond recording BDA’s assessed amounts
- **Key Actors:** Utility Officer, Tax Officer, Accounts Officer, Property Manager, Tenant (if recovery/dues visible)
- **Dependencies:** Modules 01–03; Module 04 (when recovering to tenant dues); Module 07 (expenditure link); Modules 08–09
- **Notes:** Meter master definition in Module 02; meter instances linked to property/unit here and in inventory as needed.

---

### 07. Operations, Maintenance & Expenditure

- **Type:** Business
- **Summary:** Manage maintenance complaints, inspections, work orders, vendor/contractor registry, and property-linked expenditure with approvals.
- **Source:** Explicit in document (SOW §6 Module 6)
- **In Scope:**
  - Complaint registration (officer + tenant portal), assignment, inspection, work order, completion, verification, closure
  - Configurable categories and SLA timers/escalation
  - Periodic/ad-hoc inspections with checklists, photos, recommendations; spawn work orders
  - Vendor registration, agreements/AMC, performance basics, blacklist
  - Work assignment, cost estimate, completion certificate, payment linkage
  - Expenditure posting by category with vendor/invoice/GST/payment status/documents and threshold approvals
  - Optional simple budget vs actual by category/property
- **Out of Scope:**
  - Full procurement/e-tender platform
  - Native mobile apps (responsive web in scope)
- **Key Actors:** Maintenance Officer, Chief Engineer, Property Manager, Vendor (data subject), Tenant (complaints), Accounts Officer
- **Dependencies:** Modules 01–03; Module 08 (attachments); Module 09 (SLA/alerts); Module 04/06 as needed for cross-charges
- **Notes:** Vendor *payments* are tracked here operationally; deep banking integrations are via Module 10 only if required later.

---

### 08. Document Management

- **Type:** Shared
- **Summary:** Central repository for property, tenant, lease, finance, and operations documents with versioning, access control, and notice PDF archival.
- **Source:** Explicit in document (SOW §6 Module 7.A; notice archive from 7.B)
- **In Scope:**
  - Upload, classify/tag, version, preview, download
  - Link documents to property/tenant/lease/vendor/complaint and other entities
  - Categories such as lease, possession, plans, tax receipts, utility bills, insurance, NOC, photos, KYC, vendor agreements, completion certificates, legal supporting docs
  - Role-based document access; retention/archival flags
  - Archive generated notice PDFs and digital receipts
  - Document search by property, tenant, lease, type
- **Out of Scope:**
  - Legacy physical digitization/scanning services (BDA responsibility)
  - DigiLocker connector (optional Module 10)
  - SMS/email transport (Module 09)
- **Key Actors:** All officer roles (as permitted), Tenant (own documents), Auditor, Super Administrator
- **Dependencies:** Module 01; consumed by Modules 03–07, 11
- **Notes:** Notice *business generation* and batch selection remain with owning business modules + template config in Module 02; this module stores artefacts. Channel dispatch is Module 09.

---

### 09. Notification Service

- **Type:** Technical
- **Summary:** Cross-cutting service to send SMS, email, and in-app notifications for OTPs, notices, reminders, receipts, and workflow alerts, with delivery logs.
- **Source:** Added for implementation (derived from SOW §6 Module 7.B, §9 SMS/Email, NFR alerts)
- **In Scope:**
  - SMS gateway and email service integration usage (credentials via Module 10 connectors as applicable)
  - In-app notification center/alerts
  - Template rendering using Module 02 templates / merge fields
  - Batch and event-driven dispatch
  - Delivery status and acknowledgement logs where available
  - OTP messages for auth/2FA when enabled
- **Out of Scope:**
  - Designing notice *policy* (owned by business modules)
  - WhatsApp/RCS unless later added
- **Key Actors:** System; Revenue Officer / Estate Officer (trigger batch notices); Super Administrator (config)
- **Dependencies:** Module 01, Module 02 (templates), Module 10 (gateway connectors), Module 08 (PDF archive handoff)
- **Notes:** Separated from Document Management so channel reliability, retries, and provider mapping can be estimated as a standalone technical unit.

---

### 10. API / Integration Hub

- **Type:** Technical
- **Summary:** Implement and operate external system integrations required by CPMS, including mandatory payment, SMS, email, and GIS connectors plus optional ERP/Treasury/DigiLocker/eKYC.
- **Source:** Added for implementation (derived from SOW §9)
- **In Scope:**
  - **Mandatory:** Payment Gateway (Razorpay/SBI/other govt-approved), SMS Gateway, Email Service, GIS/Map Services
  - **Optional / phase:** Accounting/ERP, Karnataka Treasury, DigiLocker, Aadhaar eKYC
  - Connector configuration, auth, mapping, retry/failure handling, reconciliation hooks, security
  - Documented REST APIs for future extensions (as integration surface)
- **Out of Scope:**
  - Replacing external systems
  - Building an e-auction platform
- **Key Actors:** Super Administrator, technical operations; business modules as consumers
- **Dependencies:** Module 01; consumed especially by Modules 03, 05, 09
- **Notes:** Business UX for payments remains in Module 05; geo capture UX in Module 03. Estimate connector complexity here using Integration rows in the Estimation Master during feature generation.

---

### 11. Analytics, Dashboards & Reports

- **Type:** Business
- **Summary:** Deliver property, revenue, expenditure, financial, and property-health dashboards plus standard MIS reports with PDF/Excel export and role-scoped data.
- **Source:** Explicit in document (SOW §6 Module 8)
- **In Scope:**
  - Dashboards: Property, Revenue, Expenditure, Financial, Property Health with drill-down
  - Standard report groups: Property, Tenant/Lease, Financial, Maintenance (as listed in SOW)
  - Filters, role/property scoping, PDF and Excel export
  - KPI reconciliation to transactional ledgers for closed periods
- **Out of Scope:**
  - Standalone BI warehouse product unless proposed by vendor as implementation choice
  - Ad-hoc pixel-perfect statutory formats beyond agreed standard reports (can be change-requested)
- **Key Actors:** Commissioner, Chief Engineer, Estate/Accounts/Revenue officers, Auditor
- **Dependencies:** Modules 03–07 (data); Module 01 (scope); Module 08 as needed for document links from drill-down
- **Notes:** Operational list screens inside business modules are not duplicated here; this module owns MIS/dashboard/report packs.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| Generic workflow engine product | Embedded — approval definitions in Module 02; runtime in business modules |
| Audit trail / compliance logging | Embedded — system-wide NFR across modules; not a separate module |
| Search & filter | Embedded — standard list behaviour in each module |
| File storage infrastructure | Embedded under Module 08 (Document Management) |
| Background jobs / schedulers | Embedded — support bill runs, SLA timers, inspection schedules inside owning modules |
| Tenant self-service portal (as a product shell) | Embedded — portal features estimated within Modules 04, 05, 07 (and related); not a separate business module |
| Notice business rules / batch selection | Embedded in Modules 04–06 with templates in 02; PDF archive in 08; dispatch in 09 |
| Data migration | Implementation/service activity (templates, import, reconciliation) — not a product module; call out during project estimation/commercials |
| Training, UAT, hypercare, warranty/AMC | Project services — outside product module list |
| Native iOS/Android apps | Out of scope (optional) |
| E-auction engine / full litigation CMS / full ERP GL | Out of scope per SOW |

---

## Assumptions

1. SOW’s eight consolidated functional modules are the primary business scope; User & Role, Notification Service, and API / Integration Hub are split out only where the module schema requires standalone implementation units.
2. Workflow Engine is not a separate module; configurable approvals are sufficient.
3. English UI is mandatory at go-live; Kannada labels are bilingual-ready but not a separate module.
4. Optional integrations (ERP, Treasury, DigiLocker, eKYC) will be estimated as optional features under Module 10, not as separate modules.
5. Tenant portal is delivered as role-based UI within existing modules rather than an independent domain module.
6. Hosting/DR/monitoring remain NFR/infrastructure concerns unless the user later requests a dedicated technical module.

---

## Risks

1. **Boundary overlap — Notices:** Logic could be duplicated across Modules 04–06, 08, and 09 if ownership is not kept clear during feature generation.
2. **Master vs Inventory:** Shop/Unit appears in both masters (02) and inventory (03); feature specs must clarify template/master vs transactional instance.
3. **Payment & integrations:** Underestimating gateway reconciliation and cheque instruments in Module 05 vs connector work in Module 10.
4. **Vacancy/lease split:** Vacancy-to-allocation spans Modules 03 and 04; weak dependency management may cause rework.
5. **Reporting volume:** Large report pack in Module 11 may expand if BDA adds statutory formats during UAT.
6. **Optional integrations becoming mandatory:** Late inclusion of DigiLocker/eKYC/ERP can inflate Module 10 without changing business module count.

---

## Review Checklist

- [x] Major SOW sections map to a module or are marked embedded/out of scope
- [x] No duplicate modules for the same capability
- [x] Business vs Technical vs Shared separation applied
- [x] Implementation-friendly names and stable numbering
- [x] Boundaries support feature breakdown
- [x] Dependencies documented
- [x] Out-of-scope items documented
- [x] Module count (11) practical for estimation

---

*Pipeline Step 1 complete. Folders created in Step 2. Awaiting user confirmation (Step 3) before feature generation.*
