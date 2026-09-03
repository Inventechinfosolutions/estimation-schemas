# EVAL — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total:** 4,481 hours · **Go-live:** 4,481 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Shared User & Access Control (consumed) | Shared | 5 | 312 | 7.0% |
| 02 | Valuation Masters, Property Coding & References | Shared | 8 | 539 | 12.0% |
| 03 | Immovable Asset Register (3(2) & Office Capture) | Business | 9 | 554 | 12.4% |
| 04 | Valuer Assignment & GIS Field Capture (Data Capturing – I) | Business | 8 | 607 | 13.5% |
| 05 | Immovable Valuation Methods & Statutory Forms (Data Capturing – II) | Business | 10 | 745 | 16.6% |
| 06 | Movables QR Coding & Valuation (eValueM) | Business | 8 | 564 | 12.6% |
| 07 | CA Assessment, MIS Reports & Auction-Display Photos | Business | 7 | 456 | 10.2% |
| 08 | Valuer Billing | Business | 3 | 179 | 4.0% |
| 09 | Valuation Android Application (Approved Valuers) | Business | 6 | 525 | 11.7% |
| | **Total** | | **64** | **4,481** | **100%** |

## 01 — Shared User & Access Control (consumed) (312 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Consume shared Person–Post–Role identity | 62 | Wiring to Claim Module 01; not a second Person master |
| F01-002 | Valuation Posts on the shared component | 60 | Configure Office user / Valuer / CA Posts on shared IAM |
| F01-003 | Assignment and need-to-know on valuation documents | 67 | Valuer sees only assigned asset deeds, photos and reports |
| F01-004 | Valuation web and Android on shared identity | 71 | Same Person credentials and 2FA on web and Android |
| F01-005 | In-app training and FAQ for valuation | 52 | Per-module Help/FAQ on web and Android; not classroom scheduling |

## 02 — Valuation Masters, Property Coding & References (539 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Approved valuer professional master | 71 | Rates, order, category linked to shared Person; not a password store |
| F02-002 | Immovable asset category master | 49 | Land, Property, Building, Lease Holding, Other — extendable |
| F02-003 | Unique seized-property code with Google location | 56 | Property code bound to Google location; not FE unique code |
| F02-004 | Movable category and sub-code catalogue | 62 | eValueM tree AC/PCP/VEH and children for QR consistency |
| F02-005 | FE and CA identity reference | 72 | Select FE/CA from Claim/FE programme reference; no new FE dossier |
| F02-006 | Central static masters for valuation | 52 | Locality HIG/MIG/LIG, zone types, condition grades |
| F02-007 | Certified structure-classification master | 57 | Specification class, economic life, residual/scrap for depreciation |
| F02-008 | Geocoding, reverse geocoding and map markers | 120 | Address ↔ coordinates/Place ID; reverse geocode; map markers on web and Android |

## 03 — Immovable Asset Register (3(2) & Office Capture) (554 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Create immovable asset (office web) | 79 | Office 3(2) create with allotted FE, location, IO/7(1)/guidance values |
| F03-002 | Asset particulars, boundaries and registration | 62 | Name, type, N/S/E/W, measure, parties, stamp duty, category |
| F03-003 | Upload court order and sale deeds | 56 | Office uploads the files the valuer later opens with View |
| F03-004 | 3(2) preparation, photograph and office location link | 68 | 3(2) prepared gate; unique code; office photo and location; assignment eligibility |
| F03-005 | Search and update rights / physical status | 56 | Search within allotted FEs; rights/status history for CA |
| F03-006 | CAD / layout upload for maintenance and security | 52 | Digital layout/CAD on the asset for officers and CA review |
| F03-007 | Link to Claim attached-asset record | 69 | Select existing Claim Module 03 row; no re-type; auction stays in Claim |
| F03-008 | Allotted-FE scope for the office user | 65 | Office create/search limited to allotted FEs; CA/admin override |
| F03-009 | Deactivate or delete asset | 47 | History-logged deactivate; blocks new assignment; login delete stays on Claim 01 |

## 04 — Valuer Assignment & GIS Field Capture (Data Capturing – I) (607 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Assign asset to approved valuer | 58 | Assignment number/date; eligible 3(2) only; reassign drops previous valuer |
| F04-002 | Display office-entered basics to the assigned valuer | 49 | Assigned-asset dropdown; office basics read-only; remaining fields in Module 05 |
| F04-003 | View sale deeds and court order | 53 | Valuer View opens office-uploaded files; gap recorded if missing |
| F04-004 | Preliminary site inspection — location and boundaries | 63 | Location pack: asset no, road, landmark, N/S/E/W with valuer identity and time |
| F04-005 | Nearby amenities, Map link and QR | 112 | Auto distances including V-1 civic/transport rows; Map link, QR, marker |
| F04-006 | GIS-tagged photographs and video | 120 | Min 4 photos, each ≥5MB, GIS tag, date on photo; video; captured date/time |
| F04-007 | Valuer live location, negative factors, remarks and approved sources | 83 | Live GIS + reverse-geocode address; remarks; named approved sources; no generative AI |
| F04-008 | Visit date, allotted valuer team and stage of valuation | 69 | Date of Visit, team names/mobiles, stage history; feeds CA Time Taken |

## 05 — Immovable Valuation Methods & Statutory Forms (Data Capturing – II) (745 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Select format and method; populate by asset code | 56 | Format/method select; populate assigned asset only; then method fields |
| F05-002 | Cost of construction — Accounts method | 80 | Materials/labour, dates, depreciation from F02-007, likely MV, accounts certificate |
| F05-003 | Comparable method for built-up properties | 67 | Flats/shops/offices comparables and adjustment factors; reason if below minimum |
| F05-004 | Floor-disposition weightage for FMV | 59 | FRS floor table; Bangalore reverse-trend requires explicit confirm/replace |
| F05-005 | Land and Building method with adjustments and depreciation | 86 | Applicability tests; min 3 comparables; FRS factors; PWD-PAR; Le and Q; value A+E |
| F05-006 | Property specification proforma | 63 | Foundation through facilities, floor by floor; empty mandatory blocks block form issue |
| F05-007 | Form V-1 immovable report and declaration | 84 | Full V-1 including Part II/III; digital sign via F05-010; V-5 not offered |
| F05-008 | Forms V-2, V-3 and V-4 | 86 | Agri V-2, forests/plantations V-3, mines/quarries V-4; no V-5; digital sign F05-010 |
| F05-009 | Tag photos and videos into the valuation library | 62 | Tag Module 04 media into report library; untagged excluded from CA photo-picker |
| F05-010 | Expert Valuer assignment and digital declaration | 102 | Optional Expert Valuer; digital sign on V-1–V-8; unsigned cannot go to CA |

## 06 — Movables QR Coding & Valuation (eValueM) (564 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | Classify and register a movable | 62 | eValueM code tree; location, model, likely purchase date/price, bank/account |
| F06-002 | Tabulate condition and value attributes | 54 | Serials, material/colour, rating, condition grades, appreciating/depreciating |
| F06-003 | Tagging sticker / label | 52 | Sticker dataset: category, name, serial, condition; required for inspection-complete |
| F06-004 | Group and sample photographs | 77 | Group of similar items plus sample photos; Android GIS/date rules via Module 09 |
| F06-005 | Form V-6 — equipment, furniture, machinery and plant | 71 | V-6 line-wise codes, prices, depreciation; digital sign F05-010 |
| F06-006 | Form V-7 — gemstones, precious metals and jewellery | 88 | Weights, stone/metal values, purity-testing methods, Sub-Annexures I–II, digital sign |
| F06-007 | Form V-8 — art and handicrafts | 72 | Base value plus hand-crafted, antiquity and rarity additions; digital sign |
| F06-008 | Cash and foreign currency handover; RBI damaged-note application | 88 | Quantity, value, damage at handover; RBI application from stored format; no generative draft |

## 07 — CA Assessment, MIS Reports & Auction-Display Photos (456 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F07-001 | Valuation MIS report from valuer data | 80 | Generate from valuer-entered data; tagged media; version history on regenerate |
| F07-002 | CA assessment on key parameters | 67 | Time Taken shown from F07-006; category, method, factors, 7(1), guidance |
| F07-003 | Select photographs for auction display | 60 | CA marks tagged photos for auction display; does not run the auction |
| F07-004 | Accept, reject, revaluation or SCN | 69 | Accept unlocks billing and Claim release; revaluation resets stage; SCN on valuer master |
| F07-005 | CAD / layout available during CA review | 45 | Open F03-006 CAD in CA context; absence visible; not an automatic Accept block |
| F07-006 | Compute Time Taken from assignment, visit and submit | 56 | Elapsed from Assignment Date, Date of Visit, submit timestamp; CA cannot silently overwrite |
| F07-007 | Release accepted valuation pack to Claim for auction | 79 | After Accept only: code, report, selected photos, Claim link; no auction sale/deposit |

## 08 — Valuer Billing (179 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F08-001 | Open billing only after CA acceptance | 56 | Valuer Code populate; billing window blocked unless CA Accept |
| F08-002 | Prepare bill and voucher from approved particulars | 67 | Rates/incidental from F02-001; rate change on bill needs reason; does not rewrite master |
| F08-003 | Submit bill online and file signed hard copy | 56 | Both online submit and signed scan required; payment execution out of scope |

## 09 — Valuation Android Application (Approved Valuers) (525 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F09-001 | Android login on shared identity | 71 | Official app sign-in with shared Person + 2FA; assigned work only; deactivation blocks |
| F09-002 | Retrieve assigned assets and office documents | 79 | Assigned assets + View deeds/orders on device; no re-type of FE/CA/asset identity |
| F09-003 | Device GIS photo, video and live location | 120 | Device capture of min 4 photos ≥5MB, GIS tag, date on photo, video, live GIS reverse-geocode |
| F09-004 | Method-specific remaining entry on Android | 88 | Method/format remaining fields including eValueM; approved sources; no generative AI |
| F09-005 | Submit field package to web for CA | 93 | Submit inspection/valuation working; retry state; drafts attributable; feeds Time Taken |
| F09-006 | Distribution and Play Store licensing | 74 | Secure distribution; Play Store only if SPLOCA approves; IP with SPLOCA; not speculative |

## Indicative phasing

| Phase | Modules |
|-------|---------|
| P1 — Identity and masters | 01, 02 |
| P2 — Office asset register | 03 |
| P3 — Field capture and methods | 04, 05 |
| P4 — Movables and cash | 06 |
| P5 — CA, billing, Android | 07, 08, 09 |

## Exclusions (not in feature hours)

- Rebuild of user management (Claim Management Module 01)
- Claim settlement, auction sale and recovered-fund deposit
- Legal Management Application
- Form V-5
- Office IT inventory and maintenance tickets
- Generative AI
- Hardware and hosting AMC
