# LMS — Estimation Summary

> **Detailed module & feature-wise hours:** [`LMS_Estimation_Summary_FeatureWise.md`](LMS_Estimation_Summary_FeatureWise.md)

Source: `SoW_LMS_Detailed.md`  
Modules file: `LMS_Modules.md`  
Pipeline: `CONTROL.md`  
Basis: Estimation Master in `feature_schema.md`  
Status: **Step 4 complete for all modules · Step 5 summary**

---

## Progress

| Module | Features | Total Hours | Status |
|--------|----------|-------------|--------|
| 01 User & Role Management | 8 | 368 | Complete |
| 02 Master Data & System Configuration | 7 | 354 | Complete |
| 03 Layout Management | 6 | 297 | Complete |
| 04 Site Management & Classification | 7 | 398 | Complete |
| 05 Auction Management | 6 | 349 | Complete |
| 06 Allotment Management | 7 | 477 | Complete |
| 07 CA Site Management | 5 | 296 | Complete |
| 08 Land Loser Management | 3 | 177 | Complete |
| 09 GIS & GeoServer Synchronization | 6 | 544 | Complete (Phase 1 full) |
| 10 Citizen & Public Portal | 6 | 323 | Complete |
| 11 Notification Service | 6 | 195 | Complete |
| 12 API / Integration Hub | 5 | 270 (base 93 / cond 76 / opt 101) | Complete |
| 13 Analytics, Dashboards & Reports | 9 | 343 | Complete |
| 14 Data Migration | 5 | 255 | Complete |
| | **Features** | **86** | |
| | **Grand total (all catalogued hours)** | **4646** | |
| | **Go-live recommended (excl. DigiLocker/eKYC optional)** | **4545** | |
| | **Base (excl. payment + DigiLocker/eKYC)** | **4469** | |

---

## Module 12 line items

| Bucket | Features | Hours |
|--------|----------|------:|
| Base mandatory | F12-002, F12-003 | 93 |
| Conditional (online EMD/fees) | F12-001 Payment Gateway | 76 |
| Optional (exclude unless approved) | F12-004 DigiLocker, F12-005 Aadhaar eKYC | 101 |
| **Module 12 all** | | **270** |

**Go-live recommended** includes Module 12 base + conditional payment (typical for auction/allotment fees) and excludes DigiLocker/eKYC.

---

## Reconciliation notes

| Item | Treatment |
|------|-----------|
| Document Management | Embedded in layout/site/process features — no separate module hours |
| Workflow engine | Config in Module 02; runtime in business features — no standalone BPM product |
| GIS / GeoServer VH (40h) | Booked in Module 09 sync features (Phase 1) |
| Payment Gateway VH | Booked in F12-001; Module 05 keeps hub-consumption / payment-link stub only |
| SMS / Email | Dispatch in Module 11; connectors/credentials via notification + ops |

---

## Open assumptions / risks (program)

1. Auction mode (including any e-auction mechanics) finalized in BDA workshops within Module 05 boundaries.  
2. GIS/GeoServer environments and counterparts available for Phase 1 bidirectional sync.  
3. Citizen portal exposes only configured published fields.  
4. Legacy migration completeness limited to data BDA can supply.  
5. Payment gateway included in go-live recommended total; confirm for RFP commercial.  
6. DigiLocker / Aadhaar eKYC optional unless approved.  
7. English UI mandatory; Kannada bilingual-ready preferred.  

---

## Suggested next actions

1. Review feature hours for Modules 05–06 (Auction / Allotment) against final process depth.  
2. Confirm Module 12 payment + optional connectors for bid package.  
3. Add non-product commercial streams: training, UAT, hypercare, warranty/AMC, hosting/provider licenses.  
4. Export feature-wise summary for client proposal if required.  

---

*End of Step 5 summary*
