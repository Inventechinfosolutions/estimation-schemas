# SoW CCC — Detailed Statement of Work

## Introduction
The Food, Civil Supplies and Consumer Affairs Department, Government of Karnataka, invites application software for a State-Level Command and Control Centre (CCC)
to monitor Public Distribution System (PDS) commodity movement and wholesale godown operations, as specified in tender FCS/IT-02/09/1/26-27 (CCC Tender).
This Statement of Work restates the **application software** functional scope for RFP discussion and estimation. The original tender remains the commercial and compliance baseline.

## Project Overview
FCS Karnataka State Command and Control Centre provides centralized real-time monitoring by integrating GPS-based Vehicle Location Tracking System (VLTS / AIS-140) data for wholesale and retail food-grain transportation vehicles
and CCTV surveillance feeds from wholesale godowns, with RFID and ANPR-based vehicle identification, alerts, incidents, GIS, dashboards and MIS.
The CCC is established at the Office of the Commissioner, Bengaluru, with application hosting on Karnataka State Data Centre (KSDC).

## Project Objectives
- Reduce pilferage, diversion risk and operational discrepancies through technology-enabled monitoring.
- Provide unified live visibility of vehicle movement, warehouse activities and exceptions.
- Enforce route compliance, geo-fence and unauthorized stoppage detection with auditable incidents.
- Integrate VLTS, CCTV (ONVIF/multi-vendor), SMART-PDS and APIs such as Vahan and Sarathi.
- Support role-scoped State and District supervision with comprehensive audit trail.

## In Scope / Out of Scope
### In Scope
- Application software modules listed in Section 6 (web CCC platform, dashboards, GIS software views, alerts, incidents, MIS, RBAC).
- Logical integrations for VLTS/AIS-140 (multi-vendor), CCTV/ONVIF, RFID/ANPR event channels, SMART-PDS, Vahan, Sarathi and other identified departmental APIs.
- Person → Post → Role access, maker–checker where required, and access audit logging.
- Embedded document/evidence attachments on incidents and masters (no standalone DMS product).

### Out of Scope
- CCC room hardware (video wall, consoles, switches, firewalls, UPS, cabling) and civil works.
- GPS device supply, SIM, vehicle installation and field GPS maintenance (tender: SI not responsible).
- CCTV camera supply, installation, NVR/DVR and camera networking (tender: SI not responsible).
- KSDC hosting consumption (INR), AMC/O&M person-months, resident manpower and training delivery (excluded from this estimate).
- Detailed technical architecture, class diagrams and UI wireframes (design stage).

## Solution Expectations (Business-level Only)
- Configuration-driven masters, geo-fences, alert rules and role-scoped dashboards.
- Real-time operational views with exception-driven incident handling.
- Tamper-evident history of who acted, from which Post, when.
- PDF/Excel MIS exports and scheduled reports.

## Consolidated Functional Modules

### 01. Person, Post, Role and Access Governance
**Purpose:** Staff identity as Person mapped to FCS Posts with Roles for CCC, district and godown-scoped access.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F01-001 | Foundational person directory. | Access Administrator maintains each FCS official as a unique Person |
| F01-002 | Unit-scoped post catalogue. | Administrator maintains Posts placed on State CCC, District, Taluk or Godown units with a supervising Post for approvals |
| F01-003 | Effective-dated occupancy. | Administrator maps a Person to a Post with effective dates; Checker approves before login under that Post |
| F01-004 | Post-level permission matrix. | Administrator assigns Roles (view/create/approve by CCC module) to Posts; permissions are never granted directly to Persons |
| F01-005 | Login and Post selection. | Person signs in, optionally completes OTP/2FA, then selects a current Post |
| F01-006 | Access forensic log. | Auditor searches who did what, when, from which Post on CCC modules |


### 02. Organisation and Location Masters
**Purpose:** District, taluk, wholesale godown and FPS location masters used for geo-fence, scope and GIS.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F02-001 | Admin geography catalogue. | Master Data Administrator maintains District and Taluk units used for Post placement and district-wise CCC views |
| F02-002 | Warehouse and FPS locations for geo-fence and GIS. | Administrator maintains Wholesale Godown and Fair Price Shop locations with coordinates used for geo-fence, RFID/ANPR sites and GIS |


### 03. Vehicle and GPS Device Onboarding
**Purpose:** Vehicle, transporter and AIS-140 GPS device registration, mapping, health and permit tracking.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F03-001 | Vehicle/transporter catalogue. | Fleet Administrator maintains transport vehicles and contractor/transporter details including load capacity, permit and fitness validity |
| F03-002 | AIS-140 device mapping. | Administrator onboards GPS devices, maps them to vehicles, tracks warranty/AMC of devices, and monitors device health/status |


### 04. Route Master and Route Compliance
**Purpose:** Authorized routes, geo-fences, stoppages, ETA rules and vehicle–route assignment.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F04-001 | Route and geo-fence catalogue. | Route Administrator defines source–destination routes, geo-fences for warehouses/FPS, deviation limits, authorized stoppages and expected travel time |
| F04-002 | Assignment and compliance setup. | Administrator assigns vehicles to authorized routes and activates compliance monitoring rules used by live GPS and alerts |


### 05. GPS Live Monitoring and Trip Lifecycle
**Purpose:** Live tracking, trip start/end, halt/idle, deviation monitoring, replay and utilization.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F05-001 | State-wide live GPS view. | Operators view state-wide live vehicle locations, movement/ignition status, district and contractor filters, and load-carrying details from VLTS feed |
| F05-002 | Trip start/end, halt, replay. | System manages trip initiation/closure (including geo-fence automation), halt/idle, route deviation monitoring, historical trip replay and utilization |


### 06. RFID Vehicle Identification
**Purpose:** RFID tag/reader management, entry/exit detection and cross-check with ANPR.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F06-001 | RFID tag/reader catalogue. | Administrator manages RFID tags, maps tags to vehicles, and registers readers at warehouse entry/exit |
| F06-002 | Entry/exit and unauthorized detection. | System logs vehicle entry/exit via RFID, flags unauthorized vehicles, and supports cross-verification with ANPR |


### 07. ANPR Vehicle Detection
**Purpose:** ANPR camera integration, plate capture, entry/exit logging and unauthorized detection.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F07-001 | ANPR camera catalogue. | Administrator registers ANPR cameras at warehouse entry/exit and maps them to godown sites |
| F07-002 | Plate capture and analytics. | System captures plates, logs entry/exit with timestamps, detects unauthorized vehicles, and integrates with RFID validation |


### 08. CCTV Surveillance Monitoring
**Purpose:** Centralized CCTV feed integration, live view, playback, video analytics (tripwire/intrusion/IMD) and camera health (cameras supplied by godown owners).

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F08-001 | Camera catalogue and health. | Administrator registers godown CCTV cameras for CCC integration, monitors availability/recording health |
| F08-002 | Live view and playback. | Operators view live feeds, entry/exit and loading/unloading monitoring, incident-linked playback |
| F08-003 | Video analytics rules and events. | Configure tripwire, intrusion and intelligent motion analytics; ingest events; review and escalate to incidents |


### 09. Alerts, Incidents and Escalation
**Purpose:** Intelligent alerts for deviations/exceptions and incident management with escalation.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F09-001 | Alert engine. | Administrator configures alert rules for route deviation, unauthorized stoppage, delay, device tampering, unauthorized RFID/ANPR, camera down; system dispatches in-app/SMS/email to Posts |
| F09-002 | Incident management. | Operators raise or auto-create incidents from alerts; track escalation, assignment, remarks and closure with audit trail |


### 10. Command Control Dashboards and GIS
**Purpose:** Unified CCC dashboards (state/district/executive) and GIS visualization of vehicles, routes, godowns and incidents.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F10-001 | Unified CCC dashboards. | Configurable dashboards for vehicle, CCTV, alert, incident, executive, SLA and system-health views with district drill-down |
| F10-002 | GIS visualization. | GIS map shows live vehicles, routes, godowns, district/taluk boundaries, incidents, alerts and geo-fenced areas with drill-down |


### 11. Reports, MIS and Analytics
**Purpose:** Operational MIS, compliance reports, KPIs, scheduled reports and PDF/Excel export.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F11-001 | Core MIS reports. | Users run vehicle movement, route compliance, RFID/ANPR, CCTV activity, alert/incident, district performance and load monitoring reports with export |
| F11-002 | Analytics and schedules. | Analytical KPI dashboards and scheduled automated report delivery to configured Posts |


### 12. External Integrations Hub
**Purpose:** VLTS/AIS-140 multi-vendor GPS, CCTV/ONVIF, SMART-PDS, Vahan, Sarathi and API management hooks.

**Functional requirements:**
- Provide the workflows and unit-scoped processing required for FCS CCC operations.
- Enforce Person–Post–Role access and audit-grade traceability.
- Provide reliable outputs for State/District supervision and MIS.

**Acceptance criteria:**
- Transactions and approvals (where used) complete with history.
- Role-scoped access prevents unauthorised viewing/acting.
- Operational views and reports reflect controlled live and historical records.

#### Key capabilities (feature outline)
| Feature ID | Capability | Description |
|---|---|---|
| F12-001 | GPS/VLTS API integration. | Integration Administrator configures mappings and schedules to ingest AIS-140/VLTS data from multiple GPS vendors; coordinates with GPS vendors |
| F12-002 | CCTV ecosystem integration. | Configure multi-vendor CCTV/ONVIF connections for live and playback into CCC |
| F12-003 | Departmental and RTO APIs. | API management hooks for SMART-PDS and external APIs such as Vahan, Sarathi and other identified departmental systems |


## End-to-End Workflows
- Person authenticates, selects current Post, works within unit scope.
- Vehicles and GPS devices onboarded; routes and geo-fences configured; vehicles assigned to routes.
- Live GPS trips monitored; RFID/ANPR validate gate events; CCTV supports warehouse surveillance.
- Alerts create or feed incidents with escalation; dashboards/GIS and MIS support supervision.
- External feeds from VLTS, CCTV vendors and departmental APIs sustain live data.

## Access Control / RBAC
Staff access is Person → Post → Role → Permissions. A Person is mapped to a Post placed on State CCC, District, Taluk or Godown.
Roles and permissions attach to the Post. Data scope follows the Post's unit unless a State CCC Role allows a wider view.
Approval routing uses the supervising Post. Maker–checker applies to masters and configured transactions. Every action is logged against Person and Post.

## Channels
- Staff web application for State CCC operators, District officers, warehouse/surveillance Posts and executives.
- No citizen portal in this tender scope.

## Integrations
- VLTS / AIS-140 multi-vendor GPS APIs (devices by separate vendors).
- CCTV multi-vendor / ONVIF (cameras by godown owners).
- RFID and ANPR event channels at warehouse gates.
- SMART-PDS and APIs such as Vahan, Sarathi and other identified systems.
- Optional SMS/email for alerts and OTP.

## Audit, Compliance & Security
- Access and operational audit trails; secure authentication; CERT/security expectations as in tender for the SI programme (software logging in this estimate).

## Non-Functional Requirements
- High availability and scalability suitable for state-wide monitoring; performance for live dashboards; India/KSDC hosting constraint.

## Data Migration
No large legacy CCC database migration is assumed. Reference masters (geography, vehicles, cameras) are loaded through application masters and integration onboarding. If the Department later mandates bulk legacy extract loads, that is a change to this SOW.

## Phased Delivery
- Phase 1: Access, organisation/location masters, vehicle/GPS onboarding, route masters.
- Phase 2: Live GPS/trips, RFID, ANPR, CCTV software monitoring.
- Phase 3: Alerts/incidents, dashboards/GIS, MIS, external API hub.

## Deliverables
- Production-grade CCC application modules and integrations named above.
- Test-ready build with audit logging and role-scoped access.
- Configuration and operations documentation for the application software.

## Acceptance Criteria (Program Level)
- Live GPS, CCTV software views, RFID/ANPR logs and incident workflows operate with history and correct scope.
- Dashboards/GIS/MIS reflect controlled operational records.
- VLTS/CCTV/SMART-PDS/Vahan/Sarathi hooks run against agreed mappings.

## Expected Benefits
- Improved transparency and faster response to diversion and operational exceptions.
- Unified State/District supervision of PDS transport and godown activity.

## Assumptions & Dependencies
- Department confirms Post catalogue and supervising Posts for State CCC, District and Godown.
- GPS and CCTV vendors provide API/ONVIF access; Department confirms SMART-PDS/Vahan/Sarathi operations.
- AMC, O&M manpower, KSDC charges and CCC hardware are outside this application-software estimate.

## Vendor Response Expectations
- Provide a production-quality CCC application aligned to functional scope and acceptance criteria.
- Maintain security, validation and traceability for government operations.

## Appendices
- Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|---|---|---|---|
| 01 | Person, Post, Role and Access Governance | Shared | F01-001, F01-002, F01-003, F01-004, F01-005, F01-006 (6) |
| 02 | Organisation and Location Masters | Business | F02-001, F02-002 (2) |
| 03 | Vehicle and GPS Device Onboarding | Business | F03-001, F03-002 (2) |
| 04 | Route Master and Route Compliance | Business | F04-001, F04-002 (2) |
| 05 | GPS Live Monitoring and Trip Lifecycle | Business | F05-001, F05-002 (2) |
| 06 | RFID Vehicle Identification | Business | F06-001, F06-002 (2) |
| 07 | ANPR Vehicle Detection | Business | F07-001, F07-002 (2) |
| 08 | CCTV Surveillance Monitoring | Business | F08-001, F08-002, F08-003 (3) |
| 09 | Alerts, Incidents and Escalation | Business | F09-001, F09-002 (2) |
| 10 | Command Control Dashboards and GIS | Business | F10-001, F10-002 (2) |
| 11 | Reports, MIS and Analytics | Business | F11-001, F11-002 (2) |
| 12 | External Integrations Hub | Technical | F12-001, F12-002, F12-003 (3) |
