# BMTC_MMVM — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Product hours:** 6,007 · **AMC 12 months:** 3,840 · **Hosting run 12 months:** 960 · **All-in:** 10,807

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Person, Post, Role & Access Governance | Shared | 6 | 692 | 11.5% |
| 02 | Organisation and Location Masters | Business | 2 | 182 | 3.0% |
| 03 | Item Master and Catalogue | Business | 2 | 182 | 3.0% |
| 04 | Vehicle Master, KM and Fleet History | Business | 3 | 411 | 6.8% |
| 05 | Digital Job Card and Fitment | Business | 3 | 371 | 6.2% |
| 06 | Component Removal, Lifecycle, Warranty and Scrap | Business | 3 | 383 | 6.4% |
| 07 | Tyre and Major Assembly Management | Business | 3 | 423 | 7.0% |
| 08 | Fuel Management | Business | 3 | 419 | 7.0% |
| 09 | Preventive Maintenance Scheduling | Business | 1 | 155 | 2.6% |
| 10 | Stores Receipt and Inspection | Business | 2 | 272 | 4.5% |
| 11 | Distribution, Stock Visibility and Replenishment | Business | 3 | 417 | 6.9% |
| 12 | Purchase and Supplier Management | Business | 3 | 369 | 6.1% |
| 13 | Barcode, QR, Notifications and External Integrations | Technical | 3 | 449 | 7.5% |
| 14 | Reporting and Dashboards | Business | 3 | 395 | 6.6% |
| 15 | Data Migration and Record Digitisation | Business | 2 | 346 | 5.8% |
| 16 | Hosting, Helpdesk and Post Go-Live Maintenance | Technical | 3 | 541 | 9.0% |
| | **Total** | | **45** | **6,007** | **100%** |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Access and location masters | 01, 02 |
| P2 — Item, vehicle, job card, removals | 03, 04, 05, 06 |
| P3 — Tyre, fuel, PM | 07, 08, 09 |
| P4 — Stores, distribution, purchase | 10, 11, 12 |
| P5 — Integrations, reports, migration | 13, 14, 15 |
| P6 — Hosting, helpdesk, AMC tooling | 16 |

## Exclusions (not in feature hours)

- Barcode/QR scanner and printer hardware (RFP: not paid by BMTC).
- Classroom training delivery and scanning bureau operations, unless separately ordered.
- SMS usage charges (BMTC). MeitY cloud **consumption (INR)** sits in the per-user-per-month quote, not in product hours.
- Optional second AMC year at the same price (original contract-period clause) is not in the 12-month AMC hours.


## 01 — Person, Post, Role & Access Governance (692 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Person Master | 91 | Foundational person directory. |
| F01-002 | Post Master and Unit Placement | 91 | Unit-scoped post catalogue. |
| F01-003 | Post-to-Person Mapping with Effective Dates | 125 | Effective-dated occupancy. |
| F01-004 | Role-to-Post Mapping and Permission Matrix | 119 | Post-level permission matrix. |
| F01-005 | Authentication, Session, OTP and 2FA | 115 | Login, OTP and 2FA. |
| F01-006 | Access Audit Log and Recertification | 151 | Access forensic log. |

## 02 — Organisation and Location Masters (182 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Depot, Zone and Workshop Master | 91 | Depot/zone/workshop catalogue. |
| F02-002 | Stores Location and Section Master | 91 | Stores and section catalogues. |

## 03 — Item Master and Catalogue (182 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | BMTC Item ID and OEM Linkage | 91 | FR-S-05, FR-S-06. |
| F03-002 | Schedule Hierarchy, ABC and Substitute Items | 91 | FR-S-07 to FR-S-09. |

## 04 — Vehicle Master, KM and Fleet History (411 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Vehicle Master and Depot Allocation | 91 | FR-M-19, FR-M-23 allocation. |
| F04-002 | Daily KM Entry and AVLS KM | 169 | FR-M-20 and RFP AVLS KM. |
| F04-003 | Vehicle Lifecycle, Transfer and History | 151 | Transfers, scrap alerts, assembly history view. |

## 05 — Digital Job Card and Fitment (371 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Digital Job Card Creation and Work Capture | 151 | Job card create/edit/submit. |
| F05-002 | Stores Issue and Fitment Recording | 97 | Issue + fitment. |
| F05-003 | Job Card Closure and Labour Hours | 123 | Supervisor sign-off and labour. |

## 06 — Component Removal, Lifecycle, Warranty and Scrap (383 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Item Removal and Inter-Vehicle Transfer | 119 | Removal and transfer. |
| F06-002 | Reusable Return and Scrap Routing | 145 | Stock routing. |
| F06-003 | Warranty Claim against Supplier | 119 | Warranty tracking. |

## 07 — Tyre and Major Assembly Management (423 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Tyre History Card, Position and Inflation | 153 | Tyre card. |
| F07-002 | Tyre Life Analysis and Scrap Tyres | 139 | Life analysis and scrap. |
| F07-003 | New and RC Major Assembly Tracking | 131 | Assembly tracking. |

## 08 — Fuel Management (419 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Underground Tank Master | 91 | UGT catalogue. |
| F08-002 | Fuel GRN and Fuel Register | 139 | Fuel receipt. |
| F08-003 | Daily Fuel Issue and KMPL | 189 | Issue and KMPL. |

## 09 — Preventive Maintenance Scheduling (155 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | PM Schedule, Due Calculation and Alerts | 155 | PM engine. |

## 10 — Stores Receipt and Inspection (272 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F10-001 | Gate Entry (Receipt Control) | 119 | Gate entry. |
| F10-002 | Inspection Report and Receipt Voucher | 153 | IR and RV. |

## 11 — Distribution, Stock Visibility and Replenishment (417 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F11-001 | Indent, Stock Transfer and Acknowledgement | 135 | Distribution flow. |
| F11-002 | Real-Time Stock Visibility | 95 | Live stock views. |
| F11-003 | Min/Reorder Alerts, Average Cost and Physical Verification | 187 | Control and PV. |

## 12 — Purchase and Supplier Management (369 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F12-001 | Supplier Master | 91 | Supplier catalogue. |
| F12-002 | Auto Purchase Request and Manual PR | 127 | PR. |
| F12-003 | CPO, LPO, LOI and PO Amendment | 151 | PO lifecycle. |

## 13 — Barcode, QR, Notifications and External Integrations (449 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F13-001 | Barcode and QR Generation and Scanning | 109 | QR/barcode software only. |
| F13-002 | SMS and Email Notifications | 155 | Notifications. |
| F13-003 | AVLS and BMTC IT Integration Hooks | 185 | External hooks. |

## 14 — Reporting and Dashboards (395 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F14-001 | Job Card and Maintenance Reports | 91 | Maintenance MIS. |
| F14-002 | CME Analysis Reports (Defect, KMPL, DVP) | 125 | CME/DC/DME analysis. |
| F14-003 | Role-based Dashboards and Accounts Views | 179 | Dashboards. |

## 15 — Data Migration and Record Digitisation (346 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F15-001 | Legacy Data Migration | 195 | Migration software effort. |
| F15-002 | Paper Record Digitisation into System Structures | 151 | Digitisation of paper into masters/transactions. |

## 16 — Hosting, Helpdesk and Post Go-Live Maintenance (541 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F16-001 | MeitY Cloud Hosting Provision and Operations Console | 229 | Bidder-provided MeitY hosting setup. |
| F16-002 | Standalone Complaint Registering and Monitoring | 149 | Standalone helpdesk. |
| F16-003 | CERT-IN Audit, VAPT and Safe-to-Host Cycle | 163 | Audit cycle tooling. |
