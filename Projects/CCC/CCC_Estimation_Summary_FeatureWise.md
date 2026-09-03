# CCC — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 3,392 hours · **Go-live:** 3,392 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Person, Post, Role and Access Governance | Shared | 6 | 529 | 15.6% |
| 02 | Organisation and Location Masters | Business | 2 | 178 | 5.2% |
| 03 | Vehicle and GPS Device Onboarding | Business | 2 | 220 | 6.5% |
| 04 | Route Master and Route Compliance | Business | 2 | 209 | 6.2% |
| 05 | GPS Live Monitoring and Trip Lifecycle | Business | 2 | 302 | 8.9% |
| 06 | RFID Vehicle Identification | Business | 2 | 216 | 6.4% |
| 07 | ANPR Vehicle Detection | Business | 2 | 220 | 6.5% |
| 08 | CCTV Surveillance Monitoring | Business | 3 | 416 | 12.3% |
| 09 | Alerts, Incidents and Escalation | Business | 2 | 240 | 7.1% |
| 10 | Command Control Dashboards and GIS | Business | 2 | 242 | 7.1% |
| 11 | Reports, MIS and Analytics | Business | 2 | 182 | 5.4% |
| 12 | External Integrations Hub | Technical | 3 | 438 | 12.9% |
| | **Total** | | **30** | **3,392** | **100%** |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Access and location masters | 01, 02 |
| P2 — Vehicle, route, live GPS/trips | 03, 04, 05 |
| P3 — RFID, ANPR, CCTV + video analytics | 06, 07, 08 |
| P4 — Alerts, dashboards/GIS, MIS, integrations | 09, 10, 11, 12 |

## Exclusions (not in feature hours)

- CCC room hardware, networking, UPS, video wall.
- GPS device supply/SIM/install; CCTV camera supply/NVR/field network.
- KSDC hosting consumption (INR).
- AMC (2 years), O&M / resident manpower, classroom training.
- Camera-side analytics engines (CCC consumes events via F08-003 / F12-002).


## 01 — Person, Post, Role and Access Governance (529 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Person Master | 87 | Foundational person directory. |
| F01-002 | Post Master and Organisational Placement | 87 | Unit-scoped post catalogue. |
| F01-003 | Post-to-Person Mapping with Effective Dates | 121 | Effective-dated occupancy. |
| F01-004 | Role-to-Post Mapping and Permission Matrix | 106 | Post-level permission matrix. |
| F01-005 | Authentication, Session and Optional 2FA | 79 | Login and Post selection. |
| F01-006 | Access Audit Log | 49 | Access forensic log. |

## 02 — Organisation and Location Masters (178 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | District, Taluk and Administrative Unit Master | 81 | Admin geography catalogue. |
| F02-002 | Wholesale Godown and FPS Location Master | 97 | Warehouse and FPS locations for geo-fence and GIS. |

## 03 — Vehicle and GPS Device Onboarding (220 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Vehicle and Transporter Master | 95 | Vehicle/transporter catalogue. |
| F03-002 | GPS Device Onboarding and Health Monitoring | 125 | AIS-140 device mapping. |

## 04 — Route Master and Route Compliance (209 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Route Master, Geo-fence and Stoppage Configuration | 126 | Route and geo-fence catalogue. |
| F04-002 | Vehicle-to-Route Assignment and Compliance Rules | 83 | Assignment and compliance setup. |

## 05 — GPS Live Monitoring and Trip Lifecycle (302 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Live Vehicle Tracking Dashboard | 138 | State-wide live GPS view. |
| F05-002 | Trip Lifecycle, Replay and Utilization | 164 | Trip start/end, halt, replay. |

## 06 — RFID Vehicle Identification (216 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | RFID Tag and Reader Master | 115 | RFID tag/reader catalogue. |
| F06-002 | RFID Entry Exit Detection and Compliance Log | 101 | Entry/exit and unauthorized detection. |

## 07 — ANPR Vehicle Detection (220 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | ANPR Camera Registration and Site Mapping | 111 | ANPR camera catalogue. |
| F07-002 | ANPR Capture, Entry Exit Log and Unauthorized Detection | 109 | Plate capture and analytics. |

## 08 — CCTV Surveillance Monitoring (416 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | CCTV Camera Onboarding and Health | 144 | Camera catalogue and health. |
| F08-002 | Live CCTV Monitoring and Playback | 116 | Live view and playback. |
| F08-003 | Video Analytics Rules and Events | 156 | Tripwire, intrusion, IMD events and escalation. |

## 09 — Alerts, Incidents and Escalation (240 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Alert Rules and Notification Dispatch | 117 | Alert engine. |
| F09-002 | Incident Register, Escalation and Closure | 123 | Incident management. |

## 10 — Command Control Dashboards and GIS (242 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F10-001 | Role-based Operational and Executive Dashboards | 140 | Unified CCC dashboards. |
| F10-002 | GIS Monitoring Map | 102 | GIS visualization. |

## 11 — Reports, MIS and Analytics (182 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F11-001 | Operational and Compliance Reports | 71 | Core MIS reports. |
| F11-002 | Analytical Dashboards KPIs and Scheduled Reports | 111 | Analytics and schedules. |

## 12 — External Integrations Hub (438 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F12-001 | VLTS and Multi-vendor GPS Integration | 142 | GPS/VLTS API integration. |
| F12-002 | CCTV ONVIF and Multi-vendor Video Integration | 130 | CCTV ecosystem integration. |
| F12-003 | SMART-PDS Vahan Sarathi and API Management | 166 | Departmental and RTO APIs. |
