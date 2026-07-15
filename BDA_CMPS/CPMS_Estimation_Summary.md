# CPMS — Estimation Summary

> **Detailed module & feature-wise hours:** [`CPMS_Estimation_Summary_FeatureWise.md`](CPMS_Estimation_Summary_FeatureWise.md)

Source: `SoW_CPMS_Detailed.md`  
Modules file: `CPMS_Modules.md`  
Pipeline: `CONTROL.md`  
Status: **Step 4 complete for all modules · Step 5 summary**

## Progress

| Module | Features | Total Hours | Status |
|--------|----------|-------------|--------|
| 01 User & Role Management | 10 | 362 | Complete |
| 02 Master Data & System Configuration | 11 | 425 | Complete |
| 03 Property & Asset Inventory | 9 | 357 | Complete (GIS reconciled) |
| 04 Tenant & Lease Lifecycle | 9 | 421 | Complete |
| 05 Revenue Billing & Collections | 9 | 405 | Complete |
| 06 Utilities & Statutory Payments | 7 | 255 | Complete |
| 07 Operations, Maintenance & Expenditure | 7 | 329 | Complete |
| 08 Document Management | 6 | 203 | Complete |
| 09 Notification Service | 6 | 204 | Complete |
| 10 API / Integration Hub | 10 | 528 (mand 298 / opt 230) | Complete |
| 11 Analytics, Dashboards & Reports | 10 | 417 | Complete |
| | **Grand total (incl. M10 optional)** | **3906** | |
| | **Go-live recommended (excl. M10 optional)** | **3676** | |

## Module 11 Feature Totals

| Feature ID | Feature Name | Hours |
|------------|--------------|-------|
| F11-001 | Analytics Shell & Drill-down Framework | 39 |
| F11-002 | Property Dashboard | 36 |
| F11-003 | Revenue Dashboard | 43 |
| F11-004 | Expenditure Dashboard | 36 |
| F11-005 | Financial Dashboard | 43 |
| F11-006 | Property Health Dashboard | 39 |
| F11-007 | Standard Property Reports | 49 |
| F11-008 | Standard Tenant & Lease Reports | 47 |
| F11-009 | Standard Financial Reports | 50 |
| F11-010 | Standard Maintenance Reports | 35 |
| | **Total** | **417** |

## Module totals (product software)

| Module | Hours |
|--------|-------|
| 01 | 362 |
| 02 | 425 |
| 03 | 357 |
| 04 | 421 |
| 05 | 405 |
| 06 | 255 |
| 07 | 329 |
| 08 | 203 |
| 09 | 204 |
| 10 mandatory | 298 |
| 10 optional | 230 |
| 11 | 417 |
| **Sum (mand M10)** | **3676** |
| **Sum (all M10)** | **3906** |

## Reconciliation applied

| Item | Resolution |
|------|------------|
| GIS Very High (40h) | Counted in **F10-005**; **F03-005** Integration reduced Very High 40 → Easy 8 (−32h). Module 03 total 389 → **357**. |
| Payment Gateway VH | Counted in **F10-002**; F05-005 keeps Easy consumer |
| SMS/Email | Counted in **F10-003/004**; F09-001 keeps Easy consumers |

## Optional Module 10 line items (exclude unless approved)

| Feature | Hours |
|---------|-------|
| F10-006 Accounting / ERP | 76 |
| F10-007 Karnataka Treasury | 53 |
| F10-008 DigiLocker | 43 |
| F10-009 Aadhaar eKYC | 58 |
| **Optional subtotal** | **230** |

## Out of product-module hours (call out in commercials)

- Data migration (templates, cleansing, cutover)
- Training, UAT support, hypercare, warranty/AMC
- Hosting/infra, map/SMS/email/payment provider licenses
- Legacy scanning of physical files

## Open assumptions (program)

- Officer-mediated allotment (no public e-auction/self-allotment portal)
- No native mobile apps; responsive web including tenant portal slices in Modules 04/05/07
- Workflow embedded (not BPM product)
- Manual KYC baseline; DigiLocker/eKYC optional
- English UI mandatory; Kannada labels later

## Next actions

1. Review Module 11 + final totals.
2. Confirm which Module 10 optional connectors to include in bid.
3. Add non-product service streams (migration, training, AMC) for commercial proposal.
