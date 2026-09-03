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
1. Who creates: Office user
2. How they create: Office user opens Asset create and selects an allotted FE (F03-008) and CA from programme references (F02-005).
3. How they edit: User enters description, location, latitude and longitude (or obtains them via F02-008), dates of attachment and absolute, court-order reference, IO valuation, Section 7(1) valuation and guidance/market value as known to the office.
4. How they send for approval: User saves. Another Officer allotted to that FE can open the same asset and see those office-entered fields. Select allotted FE/CA → enter office particulars → geocode if needed → save.
5. How the approver sees pending items: There is no separate approver inbox on this feature unless a later feature owns the decision. Office user works from the register or workbench.
6. How the approver decides: No approval decision is recorded on this feature. The user saves; a later feature may consume the result.
7. How the user sees history: Office user opens history on the record.
8. How the supervisor / auditor sees history: Authorised supervisor or auditor opens the same history within need-to-know.

### Functional Capabilities
- Create immovable asset on staff web with FE/CA, location, attachment dates and office-known values
- Obtain lat/long from address via F02-008 when typed
- Stamp Office user ID/Name/Designation/Mobile from the shared Person

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| My create immovable asset list / queue | Medium |
| Immovable asset create (office web) | Complex |
| Create immovable asset history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Asset create with office validations | Complex |
| Update create immovable asset | Medium |
| Search create immovable asset | Medium |
| Read create immovable asset history | Easy |

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
|---|---|---|---|
| My create immovable asset list / queue | UI | Medium | 6 |
| Immovable asset create (office web) | UI | Complex | 12 |
| Create immovable asset history | UI | Medium | 6 |
| Asset create with office validations | API | Complex | 8 |
| Update create immovable asset | API | Medium | 6 |
| Search create immovable asset | API | Medium | 6 |
| Read create immovable asset history | API | Easy | 4 |
| Create immovable asset persistence | DB | Medium | 4 |
| Geocode and FE/CA consume on create | Integration | Medium | 16 |
| Create immovable asset (office web) feature tests | Testing | Complex | 8 |
| Create immovable asset (office web) implementation documentation | Documentation | Medium | 3 |
| **Total** | | | **79** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Each named UI screen and each logical API operation is estimated separately.
- Logical APIs are business operations, not REST endpoints or database schema.
- Screens and integrations assume a production-quality enterprise build with validation, logging and security.
