# CPMS — Module & Feature-wise Estimation Summary

**Project:** BDA Commercial Property Management System (CPMS)  
**Source:** `SoW_CPMS_Detailed.md` → `CPMS_Modules.md` → module `features/`  
**Basis:** Estimation Master in `feature_schema.md` (UI / API / Database / Integration / Testing / Documentation)  
**Pipeline:** `CONTROL.md`  

---

## 1. Grand totals

| Scope | Features | Hours |
|-------|----------|-------|
| **All features (incl. M10 optional connectors)** | 94 | **3906** |
| **Recommended go-live (excl. F10-006–009)** | 90 | **3676** |
| Module 10 optional connectors only | 4 | 230 |

GIS reconciliation applied: F03-005 Integration reduced to Easy (8h); GIS Very High (40h) owned by F10-005.

---

## 2. Module-wise summary

| # | Module | Type | Features | Hours | % of go-live* |
|---|--------|------|----------|-------|---------------|
| 01 | User & Role Management | Shared | 10 | **362** | 9.8% |
| 02 | Master Data & System Configuration | Business | 11 | **425** | 11.6% |
| 03 | Property & Asset Inventory | Business | 9 | **357** | 9.7% |
| 04 | Tenant & Lease Lifecycle | Business | 9 | **421** | 11.5% |
| 05 | Revenue Billing & Collections | Business | 9 | **405** | 11.0% |
| 06 | Utilities & Statutory Payments | Business | 7 | **255** | 6.9% |
| 07 | Operations, Maintenance & Expenditure | Business | 7 | **329** | 8.9% |
| 08 | Document Management | Shared | 6 | **203** | 5.5% |
| 09 | Notification Service | Technical | 6 | **204** | 5.5% |
| 10 | API / Integration Hub | Technical | 10 | **528** (mand 298 / opt 230) | 8.1% |
| 11 | Analytics, Dashboards & Reports | Business | 10 | **417** | 11.3% |
| | **Total (all)** | | **94** | **3906** | |
| | **Go-live (excl. M10 opt)** | | **90** | **3676** | 100% |

\*Percentages use go-live denominator (excludes F10-006–009).

---

## 3. Feature-wise estimation (all modules)

### Module 01: User & Role Management

**Type:** Shared  
**Folder:** `modules/01-user-role-management/features/`  
**Module total:** **362 hours** · **10 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F01-001 | Secure Login & Session Management | 32 | Foundation auth |
| F01-002 | Password Policy & Account Recovery | 40 | Includes forgot-password |
| F01-003 | Optional Two-Factor Authentication | 39 | Optional per SOW |
| F01-004 | User Lifecycle Management | 39 | CRUD + status |
| F01-005 | Role & Permission Management | 62 | Includes matrix UI |
| F01-006 | User Data Scope Mapping | 31 | Location/property scope |
| F01-007 | Segregation of Duties Controls | 29 | Finance SoD |
| F01-008 | Tenant Portal Credential Management | 34 | Issue/reset portal access |
| F01-009 | Login History & User Activity Logs | 32 | Access audit |
| F01-010 | Baseline Roles & Permission Seed | 24 | SOW indicative roles |
| | **Subtotal** | **362** | |

### Module 02: Master Data & System Configuration

**Type:** Business  
**Folder:** `modules/02-master-data-system-configuration/features/`  
**Module total:** **425 hours** · **11 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F02-001 | Location Hierarchy Masters | 41 | Zone→Survey |
| F02-002 | Property Structure & Asset Masters | 57 | Complex→Asset masters |
| F02-003 | Rental Classification Masters | 22 | Category/Type/Lease |
| F02-004 | Rent Revision Rule Configuration | 57 | Effective-dated |
| F02-005 | Penalty Rule Configuration | 31 | Grace/interest/flat |
| F02-006 | Deposit Rule Configuration | 31 | Multiples/forfeiture |
| F02-007 | GST Configuration | 31 | Rates/taxability |
| F02-008 | Financial & Payment Lookup Masters | 35 | Categories/Banks |
| F02-009 | Approval Workflow Configuration | 50 | Multi-level/threshold |
| F02-010 | Notice Template Configuration | 45 | SMS/Email/PDF |
| F02-011 | System Parameters Configuration | 25 | FY/billing/receipts |
| | **Subtotal** | **425** | |

### Module 03: Property & Asset Inventory

**Type:** Business  
**Folder:** `modules/03-property-asset-inventory/features/`  
**Module total:** **357 hours** · **9 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F03-001 | Property & Building Register | 59 | Core inventory |
| F03-002 | Rentable Unit Inventory | 39 | Shop/office/open space |
| F03-003 | Hierarchy Navigation & Search | 44 | Browse + finders |
| F03-004 | Property Status Lifecycle | 35 | 7 statuses + approvals |
| F03-005 | Geo-location & Map View | 43 | GIS map pin (reconciled) |
| F03-006 | Property Photos & Document Linkage | 34 | Media + DMS |
| F03-007 | Building Occupancy Percentage | 19 | Auto-computed |
| F03-008 | Parking Inventory Management | 37 | Bays + classification |
| F03-009 | Vacancy Management & Pipeline | 47 | Loss + ready-to-allot |
| | **Subtotal** | **357** | |

### Module 04: Tenant & Lease Lifecycle

**Type:** Business  
**Folder:** `modules/04-tenant-lease-lifecycle/features/`  
**Module total:** **421 hours** · **9 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F04-001 | Tenant Registration & KYC Profile | 63 | Types + duplicates |
| F04-002 | Allocation Application & Approval | 67 | Avail→Approve |
| F04-003 | Lease Creation & Agreement | 67 | Terms + activation |
| F04-004 | Property Handover & Possession | 37 | Checklist→Occupied |
| F04-005 | Lease Amendments & Version History | 37 | Rent/area/party |
| F04-006 | Lease Renewal & Termination | 39 | Renew/vacate |
| F04-007 | Security Deposit Lifecycle | 51 | Collect/refund/forfeit |
| F04-008 | Lease Notice Triggers | 38 | Expiry/eviction/deposit |
| F04-009 | Tenant Portal Lease Summary | 22 | Self-service view |
| | **Subtotal** | **421** | |

### Module 05: Revenue Billing & Collections

**Type:** Business  
**Folder:** `modules/05-revenue-billing-collections/features/`  
**Module total:** **405 hours** · **9 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F05-001 | Scheduled Demand Generation | 78 | Bulk bill run |
| F05-002 | Ad-hoc Demand & Manual Charges | 28 | Approved one-offs |
| F05-003 | Credit Notes & Demand Cancellation | 31 | Maker-checker |
| F05-004 | Offline Collections & Instruments | 39 | Cash/cheque/NEFT |
| F05-005 | Online Payment Collection | 49 | Gateway UX + reconcile |
| F05-006 | Payment Allocation Engine | 43 | Partial pay priority |
| F05-007 | Receipts, History & Outstanding Statements | 41 | PDF + ledgers |
| F05-008 | Arrears, Ageing & Defaulter Notices | 51 | Buckets + overdue |
| F05-009 | Tenant Portal Dues & Payments | 45 | View/pay/download |
| | **Subtotal** | **405** | |

### Module 06: Utilities & Statutory Payments

**Type:** Business  
**Folder:** `modules/06-utilities-statutory-payments/features/`  
**Module total:** **255 hours** · **7 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F06-001 | Utility Meter Registry & Linkage | 32 | Meter instances |
| F06-002 | Meter Reading Management | 37 | Validate current≥prev |
| F06-003 | Utility Bill Lifecycle | 43 | BDA-paid + informational |
| F06-004 | Tenant Utility Recovery Billing | 29 | Post to lease dues |
| F06-005 | Property Tax Assessment Register | 39 | Due/paid/outstanding |
| F06-006 | Property Tax Payments & Expenditure Link | 41 | Challan + Module 07 |
| F06-007 | Utility & Tax Overdue Alerts & Notices | 34 | M5-AC4 candidates |
| | **Subtotal** | **255** | |

### Module 07: Operations, Maintenance & Expenditure

**Type:** Business  
**Folder:** `modules/07-operations-maintenance-expenditure/features/`  
**Module total:** **329 hours** · **7 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F07-001 | Complaint Registration & Tracking | 51 | Officer + portal |
| F07-002 | Maintenance Work Order & SLA Workflow | 72 | Assign→Close |
| F07-003 | Inspection Scheduling & Execution | 47 | Periodic + ad-hoc |
| F07-004 | Vendor & Contractor Management | 43 | Register/AMC/blacklist |
| F07-005 | Vendor Work Assignment & Completion | 39 | Estimate→certificate |
| F07-006 | Property Expenditure Management | 53 | Categories + approvals |
| F07-007 | Simple Budget vs Actual | 24 | Optional annual |
| | **Subtotal** | **329** | |

### Module 08: Document Management

**Type:** Shared  
**Folder:** `modules/08-document-management/features/`  
**Module total:** **203 hours** · **6 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F08-001 | Document Repository Upload & Linkage | 51 | Core DMS |
| F08-002 | Document Versioning Preview & Download | 34 | History + viewers |
| F08-003 | Document Category Access Control | 37 | Restricted downloads |
| F08-004 | Cross-entity Document Search | 30 | Property/tenant/lease/type |
| F08-005 | Retention & Archival Management | 23 | Flags + policies |
| F08-006 | Generated Artefact Archival | 28 | Notices + receipts |
| | **Subtotal** | **203** | |

### Module 09: Notification Service

**Type:** Technical  
**Folder:** `modules/09-notification-service/features/`  
**Module total:** **204 hours** · **6 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F09-001 | Multi-channel Dispatch Engine | 57 | SMS/Email core |
| F09-002 | Template Rendering & Merge Fields | 26 | Uses F02-010 |
| F09-003 | In-app Notification Center | 30 | Bell + inbox |
| F09-004 | Delivery Status & Acknowledgement Logs | 31 | Audit trail |
| F09-005 | Batch & Event Notification Orchestration | 39 | Campaigns + events |
| F09-006 | OTP Messaging Support | 21 | Auth/2FA channel |
| | **Subtotal** | **204** | |

### Module 10: API / Integration Hub

**Type:** Technical  
**Folder:** `modules/10-api-integration-hub/features/`  
**Module total:** **528 hours** · **10 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F10-001 | Integration Hub Core Framework | 44 | Shared connector platform |
| F10-002 | Payment Gateway Connector | 76 | Mandatory VH |
| F10-003 | SMS Gateway Connector | 39 | Mandatory |
| F10-004 | Email Service Connector | 39 | Mandatory |
| F10-005 | GIS / Map Services Connector | 72 | Mandatory VH — reconcile F03 |
| F10-006 | Accounting / ERP Connector (Optional) | 76 | OPTIONAL Phase 3 · **OPTIONAL** |
| F10-007 | Karnataka Treasury Connector (Optional) | 53 | OPTIONAL · **OPTIONAL** |
| F10-008 | DigiLocker Connector (Optional) | 43 | OPTIONAL · **OPTIONAL** |
| F10-009 | Aadhaar eKYC Connector (Optional) | 58 | OPTIONAL legal · **OPTIONAL** |
| F10-010 | API Extension Surface & Documentation | 28 | Future extensions |
| | **Subtotal** | **528** | |

### Module 11: Analytics, Dashboards & Reports

**Type:** Business  
**Folder:** `modules/11-analytics-dashboards-reports/features/`  
**Module total:** **417 hours** · **10 features**

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|-------|-------|
| F11-001 | Analytics Shell & Drill-down Framework | 39 | Shared MIS chrome |
| F11-002 | Property Dashboard | 36 | Occupancy KPIs |
| F11-003 | Revenue Dashboard | 43 | Demand/collection % |
| F11-004 | Expenditure Dashboard | 36 | Spend by category |
| F11-005 | Financial Dashboard | 43 | P&L cascade |
| F11-006 | Property Health Dashboard | 39 | Trends/expiry |
| F11-007 | Standard Property Reports | 49 | 5 SOW reports |
| F11-008 | Standard Tenant & Lease Reports | 47 | 5 SOW reports |
| F11-009 | Standard Financial Reports | 50 | 6 SOW reports |
| F11-010 | Standard Maintenance Reports | 35 | 4 SOW reports |
| | **Subtotal** | **417** | |

---

## 4. Optional features (commercial line items)

| Feature ID | Feature Name | Hours | Recommendation |
|------------|--------------|-------|----------------|
| F10-006 | Accounting / ERP Connector | 76 | Phase 3 / if ERP identified |
| F10-007 | Karnataka Treasury Connector | 53 | If mandated & ICD available |
| F10-008 | DigiLocker Connector | 43 | Subject to BDA/legal approval |
| F10-009 | Aadhaar eKYC Connector | 58 | Subject to legal approval |
| | **Optional subtotal** | **230** | |

Also switchable / lightweight optional inside baseline (included in go-live hours):

| Feature ID | Feature Name | Hours | Note |
|------------|--------------|-------|------|
| F01-003 | Optional Two-Factor Authentication | 39 | Included; can be disabled by config |
| F07-007 | Simple Budget vs Actual | 24 | Included for SOW completeness |

---

## 5. Effort profile (go-live modules)

### Top 15 features by effort (go-live set)

| Rank | Feature ID | Feature Name | Module | Hours |
|------|------------|--------------|--------|-------|
| 1 | F05-001 | Scheduled Demand Generation | 05 | 78 |
| 2 | F10-002 | Payment Gateway Connector | 10 | 76 |
| 3 | F10-005 | GIS / Map Services Connector | 10 | 72 |
| 4 | F07-002 | Maintenance Work Order & SLA Workflow | 07 | 72 |
| 5 | F04-003 | Lease Creation & Agreement | 04 | 67 |
| 6 | F04-002 | Allocation Application & Approval | 04 | 67 |
| 7 | F04-001 | Tenant Registration & KYC Profile | 04 | 63 |
| 8 | F01-005 | Role & Permission Management | 01 | 62 |
| 9 | F03-001 | Property & Building Register | 03 | 59 |
| 10 | F09-001 | Multi-channel Dispatch Engine | 09 | 57 |
| 11 | F02-004 | Rent Revision Rule Configuration | 02 | 57 |
| 12 | F02-002 | Property Structure & Asset Masters | 02 | 57 |
| 13 | F07-006 | Property Expenditure Management | 07 | 53 |
| 14 | F08-001 | Document Repository Upload & Linkage | 08 | 51 |
| 15 | F07-001 | Complaint Registration & Tracking | 07 | 51 |

### Hours by module type (go-live)

| Type | Features | Hours | % |
|------|----------|-------|---|
| Business | 62 | 2609 | 71.0% |
| Shared | 16 | 565 | 15.4% |
| Technical | 12 | 502 | 13.7% |
| **Total** | **90** | **3676** | 100% |

---

## 6. Phasing hint (from SOW)

Indicative split for delivery planning (adjust during project plan):

| Phase | Scope | Hours |
|-------|-------|-------|
| **Phase 1 — Foundation & Core Revenue** | Modules 01–05, 08, 09, 10 mandatory (298), Module 11 core (F11-001, 002, 003, 007, 008 = 214) | **2,889** |
| **Phase 2 — Operations & Statutory** | Modules 06–07 + Module 11 remaining (F11-004, 005, 006, 009, 010 = 203) | **787** |
| **Phase 3 — Optional integrations** | F10-006–009 | **230** |
| | **Check:** Phase1 + Phase2 | **3,676** (go-live) |
| | **Check:** Go-live + Phase3 | **3,906** (all-in) |

---

## 7. Exclusions (not in feature hours)

| Item | Treatment |
|------|-----------|
| Data migration | Separate commercial/service stream |
| Training, UAT, hypercare | Project services |
| Warranty / AMC | Post-go-live commercial |
| Hosting / DR / licenses (SMS, email, maps, PG) | Infra & vendor fees |
| Legacy physical scanning | BDA responsibility |
| Native mobile apps / e-auction / full litigation CMS / full ERP GL | Out of scope |

---

## 8. Quick reference paths

| Artefact | Path |
|----------|------|
| This summary | `BDA_CMPS/CPMS_Estimation_Summary_FeatureWise.md` |
| Roll-up summary | `BDA_CMPS/CPMS_Estimation_Summary.md` |
| Module list | `BDA_CMPS/CPMS_Modules.md` |
| Per-module indexes | `BDA_CMPS/modules/*/features/_index.md` |
| Feature specs | `BDA_CMPS/modules/*/features/F*.md` |

---

**Document generated from 94 feature index rows. Go-live total = 3676h. All-in total = 3906h.**
