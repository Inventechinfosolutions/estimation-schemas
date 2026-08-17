# GIS Field Valuation — eValueI / eValueM (KPID / SPLOCA) — Module List

Source: `SoW_EVAL_Detailed.md` (v1.1)

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | Shared User & Access Control (consumed) | Shared | Consume Claim Module 01; valuation Posts, assignment need-to-know, web+Android, in-app FAQ | Explicit in SOW |
| 02 | Valuation Masters, Property Coding & References | Shared | Valuer professional master, categories, unique property code, eValueM codes, geocoding, structure class | Explicit in SOW |
| 03 | Immovable Asset Register (3(2) & Office Capture) | Business | Office 3(2) create, deeds/orders, CAD, allotted-FE scope, deactivate, Claim-asset link | Explicit in SOW |
| 04 | Valuer Assignment & GIS Field Capture (Data Capturing – I) | Business | Assign valuer; inspection; GIS photos/video/location; amenities; visit/stage/team | Explicit in SOW |
| 05 | Immovable Valuation Methods & Statutory Forms (Data Capturing – II) | Business | Methods, specification proforma, Forms V-1–V-4, Expert Valuer digital declaration | Explicit in SOW |
| 06 | Movables QR Coding & Valuation (eValueM) | Business | Movable coding, stickers, photos, Forms V-6–V-8, cash/FCY and RBI damaged-note application | Explicit in SOW |
| 07 | CA Assessment, MIS Reports & Auction-Display Photos | Business | MIS, CA key-parameter assessment, computed Time Taken, photo pick, Claim release | Explicit in SOW |
| 08 | Valuer Billing | Business | Bill and voucher only after CA Accept; online submit and signed hard copy | Explicit in SOW |
| 09 | Valuation Android Application (Approved Valuers) | Business | Valuer Android: retrieve, GIS capture, method entry, submit; distribution/licensing | Explicit in SOW |

---

## Module Details

### 01. Shared User & Access Control (consumed)

- **Type:** Shared
- **Slug:** `shared-user-access-control`
- **Summary:** Wire valuation web and Android to Claim Management Module 01; valuation Posts, assignment visibility, document rights, training/FAQ.
- **Source:** Explicit in SOW §6 Module 01; Claim SOW F01-001–F01-007, F01-010; Proceedings items 1, 13, 23.
- **In Scope:** F01-001 … F01-005.
- **Out of Scope:** Rebuilding Person/Post/Role/OTP/2FA; office IT inventory credentials as a local directory.
- **Key Actors:** Administrator (shared IAM), Office user, Approved Valuer, Competent Authority.
- **Dependencies:** Claim Management Module 01.
- **Notes:** Approved Valuer **professional** master is Module 02, not login.

### 02. Valuation Masters, Property Coding & References

- **Type:** Shared
- **Slug:** `valuation-masters-property-coding`
- **Summary:** Valuer rates/order/category, immovable and movable catalogues, unique seized-property code with Google location, FE/CA references, structure-classification master, geocoding.
- **Source:** Explicit in SOW §6 Module 02; Annexure-01; Proceedings items 9, 22.
- **In Scope:** F02-001 … F02-008.
- **Out of Scope:** Unique **FE** code (existing FE application); second password store.
- **Key Actors:** Office user, Administrator.
- **Dependencies:** 01 Shared access; Claim FE import / existing FE app for FE/CA references.
- **Notes:** Geocoding is a named capability, not a separate technical module.

### 03. Immovable Asset Register (3(2) & Office Capture)

- **Type:** Business
- **Slug:** `immovable-asset-register`
- **Summary:** Office-created 3(2) immovable record, particulars, court order/sale deeds, CAD, search/status, allotted-FE restriction, deactivate, link to Claim attached-asset.
- **Source:** Explicit in SOW §6 Module 03; Annexure-01 sl.1/3; Proceedings items 9, 12.
- **In Scope:** F03-001 … F03-009.
- **Out of Scope:** Claim title/e-Khata/dues workflow; auction sale; field GIS capture (Module 04).
- **Key Actors:** Office user, Administrator, Competent Authority.
- **Dependencies:** 01 Access; 02 Masters/codes; Claim Module 03 for F03-007.
- **Notes:** 3(2) prepared is the gate to assignment.

### 04. Valuer Assignment & GIS Field Capture (Data Capturing – I)

- **Type:** Business
- **Slug:** `valuer-assignment-gis-field-capture`
- **Summary:** Assign approved valuer; display office basics; View deeds/orders; preliminary inspection; amenities and Map/QR; GIS media; live location; visit date/team/stage.
- **Source:** Explicit in SOW §6 Module 04; Annexure-01 Data Capturing – I; Proceedings items 9–11.
- **In Scope:** F04-001 … F04-008.
- **Out of Scope:** Method-specific statutory forms (Module 05); office Android (valuer Android is Module 09).
- **Key Actors:** Office user, Approved Valuer.
- **Dependencies:** 01 Access; 02 Geocoding/masters; 03 Eligible 3(2) assets.
- **Notes:** Minimum four photographs, each at least 5 MB, GIS-tagged, date on photo.

### 05. Immovable Valuation Methods & Statutory Forms (Data Capturing – II)

- **Type:** Business
- **Slug:** `immovable-valuation-methods-forms`
- **Summary:** Select format/method; accounts and comparable; floor weightage; land-and-building with FRS factors; specification proforma; Forms V-1–V-4; media library; Expert Valuer digital declaration.
- **Source:** Explicit in SOW §6 Module 05; Annexure-01 formats and Forms V-1–V-4.
- **In Scope:** F05-001 … F05-010.
- **Out of Scope:** Form V-5 (absent in source); generative comparable invention.
- **Key Actors:** Approved Valuer, Expert Valuer, Office user (appoint expert).
- **Dependencies:** 02 Structure class; 04 Inspection pack.
- **Notes:** Digital declaration required before CA review.

### 06. Movables QR Coding & Valuation (eValueM)

- **Type:** Business
- **Slug:** `movables-qr-coding-valuation`
- **Summary:** eValueM code tree, tabulation, sticker/label, group/sample photos, Forms V-6–V-8, cash/FCY handover and RBI damaged-note application.
- **Source:** Explicit in SOW §6 Module 06; Annexure-01 Additional Module; Proceedings item 9.
- **In Scope:** F06-001 … F06-008.
- **Out of Scope:** Office IT inventory (Proceedings item 13 last sentence).
- **Key Actors:** Office user, Approved Valuer.
- **Dependencies:** 01 Access; 02 Movable codes; 05-010 digital declaration.
- **Notes:** Digital signature on V-6–V-8 via F05-010.

### 07. CA Assessment, MIS Reports & Auction-Display Photos

- **Type:** Business
- **Slug:** `ca-assessment-mis-auction-photos`
- **Summary:** MIS from valuer data; CA assessment including computed Time Taken; auction-display photo selection; Accept/Reject/Revaluation/SCN; release pack to Claim.
- **Source:** Explicit in SOW §6 Module 07; Annexure-01 sl.5–6; Proceedings item 12.
- **In Scope:** F07-001 … F07-007.
- **Out of Scope:** Auction sale and recovered-fund deposit (Claim Module 03).
- **Key Actors:** Competent Authority, Office user.
- **Dependencies:** 04–06 completed valuation; Claim Module 03 for F07-007.
- **Notes:** Billing and Claim release both require CA Accept.

### 08. Valuer Billing

- **Type:** Business
- **Slug:** `valuer-billing`
- **Summary:** Prepare bill and voucher from approved rates only after CA Accept; submit online and upload signed hard copy.
- **Source:** Explicit in SOW §6 Module 08; Annexure-01 sl.7; Proceedings item 13.
- **In Scope:** F08-001 … F08-003.
- **Out of Scope:** Payment execution / treasury disbursement unless later ordered; claim settlement payments.
- **Key Actors:** Billing officer, Office user, Approved Valuer, Competent Authority.
- **Dependencies:** 02 Valuer rates; 07 CA Accept.
- **Notes:** Window does not open unless Accepted.

### 09. Valuation Android Application (Approved Valuers)

- **Type:** Business
- **Slug:** `valuation-android-application`
- **Summary:** Official valuer Android on shared identity: retrieve assigned assets, GIS capture, method remaining entry, submit to web; distribution/licensing.
- **Source:** Explicit in SOW §6 Module 09; Annexure-01 App; Proceedings items 10–11, 19.
- **In Scope:** F09-001 … F09-006.
- **Out of Scope:** iOS; public consumer app; office-user Android as a separate product.
- **Key Actors:** Approved Valuer.
- **Dependencies:** 01 Shared identity; 04–06 field/method behaviour.
- **Notes:** IP with SPLOCA; Play Store only where specifically approved.

---

## Excluded / Embedded Capabilities

| Capability | Treatment |
|------------|-----------|
| User management / IAM | Consumed from Claim Module 01 |
| Document Management | Embedded in asset, inspection, forms, billing |
| Workflow | Embedded in assignment stage (F04-008) and CA decision |
| Geocoding service | Feature F02-008 inside Module 02 — not a standalone technical module |
| Notification Service | Not required as a standalone module |
| Platform backup / HTTPS / AES-256 | NFR; not a separate module |
| Claim auction sale / recovered funds | Claim Module 03; this SOW only F07-007 release |
| Legal Management | Separate SOW |
| FE unique-code generation | Existing FE application |
| Form V-5 | Out of scope |
| Office IT inventory / maintenance tickets | Out of scope |
| Generative AI | Prohibited |

---

## Assumptions

1. Module `{NN}` and feature IDs match `SoW_EVAL_Detailed.md` v1.1 (64 feature outlines).
2. Shared IAM is Claim Module 01.
3. PHP/geocoding are FRS platform constraints, not interface design in this step.
4. No hours in this step.

---

## Risks

1. Shared IAM and Claim Module 03 linkage delay office create and pack release.
2. Nearby-amenity auto-fetch depends on an Authority-approved map/places capability.
3. Bangalore floor-weightage reverse-trend (F05-004) needs Authority confirmation.
4. 3-month FRS target may not match 64-feature delivery; vendor must confirm after estimation.
5. Approved secure sources list for valuers is a dependency.
