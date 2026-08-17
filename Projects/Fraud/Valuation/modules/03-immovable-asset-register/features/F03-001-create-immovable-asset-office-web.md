# F03-001 — Create immovable asset (office web)

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-001 |
| **Feature Name** | Create immovable asset (office web) |
| **Module** | 03 — Immovable Asset Register (3(2) & Office Capture) |

### Description
An Office user logs in, opens Asset create, selects an allotted FE (F03-008) and CA from programme references, and enters asset description, location, latitude and longitude (or obtains them from the address via F02-008), dates of attachment and absolute, court-order reference, IO valuation, Section 7(1) valuation and guidance/market value as known to the office. The user saves. Another Officer allotted to that FE can open the same asset by identification and see those office-entered fields.

### Business Objective
Let the office create the seized/attached immovable record before any valuer field work.

### Actors
Office user.

### User Journey
1. Office user opens Asset create and selects an allotted FE (F03-008) and CA from programme references (F02-005).
2. User enters description, location, latitude and longitude (or obtains them via F02-008), dates of attachment and absolute, court-order reference, IO valuation, Section 7(1) valuation and guidance/market value as known to the office.
3. User saves. Another Officer allotted to that FE can open the same asset and see those office-entered fields.

### Functional Capabilities
- Create immovable asset on staff web with FE/CA, location, attachment dates and office-known values
- Obtain lat/long from address via F02-008 when typed
- Stamp Office user ID/Name/Designation/Mobile from the shared Person

### Inputs
Allotted FE; CA; Asset Description; Asset Location; Latitude & Longitude; Date of Attachment; Date of Absolute; Court Order reference; IO Valuation; Section 7(1) Valuation; Guidance / Market Value.

### Outputs
Saved office-side immovable asset; visible to other Officers allotted to that FE.

### Business Rules
- Valuer cannot invent the asset — office create is first
- Create is refused for a non-allotted FE (F03-008)
- Office user identity comes from the shared Person, not typed as a new directory

### Validations
- FE allotted to this Person/Post unless CA/admin override
- Location bind present or geocode succeeded
- Mandatory office fields as named in the SOW

### Calculations
None (IO / 7(1) / guidance are office-entered known values, not computed here).

### Workflow
Select allotted FE/CA → enter office particulars → geocode if needed → save.

### Search Requirements
Asset identification, FE, location (full search/status is F03-005).

### Documents
Court-order reference on create; files uploaded in F03-003.

### Reports
Newly created assets list.

### Notifications
None.

### Security
Allotted-FE scope; shared Person stamp; audit of create.

### Integrations
F02-008 geocoding; F02-005 FE/CA reference (auth, mapping, retry across those consumes).

### Dependencies
F01-001; F02-005; F02-008; F03-008.

### Assumptions
- Office-known IO/7(1)/guidance may be blank until later update if the Authority allows.

### Risks
Creating against the wrong FE if allotment is misconfigured.

### Non Functional Requirements
Staff web only for this create; Android does not create the 3(2) asset.

---

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---:|
| Immovable asset create (office web) | UI | Complex | 12 |
| Asset create with office validations | API | Complex | 8 |
| Immovable asset office record | Database | Medium | 4 |
| Geocode and FE/CA consume on create | Integration | Medium | 16 |
| Asset create tests | Testing | Complex | 8 |
| Office asset-create guide | Documentation | Medium | 3 |
| **Total** | | | **51** |

### Estimation Assumptions
- Particulars/boundaries are F03-002; 3(2) gate is F03-004.
