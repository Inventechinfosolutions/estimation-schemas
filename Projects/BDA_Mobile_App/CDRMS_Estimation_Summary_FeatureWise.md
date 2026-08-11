# CDRMS — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 797 hours · **Go-live:** 797 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User & Access Management | Shared | 5 | 92 | 11.5% |
| 02 | Master Data & System Configuration | Business | 5 | 117 | 14.7% |
| 03 | Mobile Onboarding & Geo Enforcement | Business | 5 | 110 | 13.8% |
| 04 | Field Site Visit Capture | Business | 9 | 238 | 29.9% |
| 05 | CAO Verification & PDF Export | Business | 5 | 134 | 16.8% |
| 06 | Dashboards, KPIs & MIS | Business | 2 | 67 | 8.4% |
| 07 | Notification Service | Technical | 1 | 39 | 4.9% |
| | **Total** | | **32** | **797** | **100%** |

## 01 — User & Access Management (92 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F01-001 | User Management | 26 | Create, update, search, activate and deactivate BDA users who will use CDRMS (En |
| F01-002 | Role Assignment | 14 | Assign each user one of Engineer, CAO, or Super Admin roles controlling channel |
| F01-003 | Engineer Credential & Geo Binding | 22 | Provision engineer login credentials and bind each engineer to exactly one geo-l |
| F01-004 | CAO & Super Admin Credentials | 14 | Provision and manage web login credentials for CAO and Super Admin users. |
| F01-005 | Access Deactivation & Reset | 16 | Deactivate users and support secure credential reset when access must be revoked |

## 02 — Master Data & System Configuration (117 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F02-001 | Geo-Location Master | 26 | Maintain the geo-location list used to bind engineers and filter applications/KP |
| F02-002 | Site Visit Attribute Masters | 27 | Maintain dropdown/coded values for CDR capture: site category/type, shape, road |
| F02-003 | Application Status Configuration | 14 | Maintain application statuses: Draft, Submitted, Returned, Verified, Rejected. |
| F02-004 | System Parameters & Media Limits | 22 | Configure OTP validity, photo count/size (default 10 / 10 MB), video max size, s |
| F02-005 | Master Search Filter Export | 28 | Search, filter, and export master lists for administration. |

## 03 — Mobile Onboarding & Geo Enforcement (110 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F03-001 | Engineer Mobile Login | 26 | Initiate engineer mobile login using provisioned identity with no OTP-free acces |
| F03-002 | Mandatory OTP Login (Every Session) | 33 | Require OTP validation on every login before establishing a session; fresh OTP a |
| F03-003 | Mandatory Location Enablement | 14 | Require device location services to be enabled before capture features can be us |
| F03-004 | Assigned Geo-Location Enforcement | 29 | Prevent capture/submit outside the engineer’s assigned geo-location with server- |
| F03-005 | Engineer Profile & Assignment View | 8 | Show engineer identity and assigned geo-location on mobile. |

## 04 — Field Site Visit Capture (238 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F04-001 | Site Visit Application Create & Draft | 24 | Create and save draft CDR/site-visit applications on mobile within geo rules. |
| F04-002 | Site Details Capture | 37 | Capture site identification, shape, and regular or odd/irregular multi-side dime |
| F04-003 | Check Bandi Capture | 15 | Capture Check Bandi date, number, acknowledgement (optional remarks) on the appl |
| F04-004 | Directions & Width Capture | 22 | Capture narrative directions and mandatory approach/road width (optional road ty |
| F04-005 | Surroundings Capture | 22 | Capture what is around the site at each direction (type + short description). |
| F04-006 | Photo Capture (10 × 10 MB) | 39 | Capture/upload up to 10 photographs with per-file max 10 MB enforcement. |
| F04-007 | Video Capture | 36 | Capture/upload one video per application within configured max size. |
| F04-008 | Application Validation & Submit | 26 | Validate mandatory data/media and submit application to CAO queue. |
| F04-009 | Engineer Application Status View | 17 | Engineer views own applications and statuses. |

## 05 — CAO Verification & PDF Export (134 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F05-001 | CAO Application Workbench | 24 | List/search/filter all site-visit/CDR applications for CAO. |
| F05-002 | Application Detail & Media Review | 28 | Review full application data, photos, and video. |
| F05-003 | Verify / Return / Reject Workflow | 29 | Perform verification decisions with remarks and status update. |
| F05-004 | PDF Generation & Download | 31 | Generate and download PDF copy of the application for official use. |
| F05-005 | Resubmission Handling | 22 | Allow returned applications to be corrected by engineer and resubmitted. |

## 06 — Dashboards, KPIs & MIS (67 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F06-001 | Super Admin Basic KPIs | 43 | Simple count KPIs for users/applications for Super Admin with date/geo filters a |
| F06-002 | CAO Basic KPIs | 24 | Pending and outcome count KPIs for CAO with filters. |

## 07 — Notification Service (39 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| Feature ID | Feature Name | Total Hours | Notes |
| F07-001 | SMS OTP Dispatch & Validation | 39 | Send and validate OTP via SMS gateway for every engineer mobile login. |

## Effort profile

### By module type

| Type | Hours |
|---|---:|
| Business | 666 |
| Shared | 92 |
| Technical | 39 |

### Top features by hours

| Hours | Feature ID | Name | Module |
|---:|---|---|---|
| 43 | F06-001 | Super Admin Basic KPIs | Dashboards, KPIs & MIS |
| 39 | F07-001 | SMS OTP Dispatch & Validation | Notification Service |
| 39 | F04-006 | Photo Capture (10 × 10 MB) | Field Site Visit Capture |
| 37 | F04-002 | Site Details Capture | Field Site Visit Capture |
| 36 | F04-007 | Video Capture | Field Site Visit Capture |
| 33 | F03-002 | Mandatory OTP Login (Every Session) | Mobile Onboarding & Geo Enforcement |
| 31 | F05-004 | PDF Generation & Download | CAO Verification & PDF Export |
| 29 | F05-003 | Verify / Return / Reject Workflow | CAO Verification & PDF Export |
| 29 | F03-004 | Assigned Geo-Location Enforcement | Mobile Onboarding & Geo Enforcement |
| 28 | F05-002 | Application Detail & Media Review | CAO Verification & PDF Export |

## Indicative phasing

- **Phase 1:** Modules 01–07 — full go-live estimate above.
- **Phase 2:** As agreed with BDA later (not estimated).

## Exclusions (not in feature hours)

- Hardware / devices, hosting infra procurement
- Training delivery beyond documentation hours in features
- AMC / warranty commercial
- Legacy paper digitization
- SMS gateway commercial fees
