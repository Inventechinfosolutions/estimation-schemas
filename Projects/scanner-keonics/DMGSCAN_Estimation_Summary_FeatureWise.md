# DMGSCAN — Estimation Summary (Feature-Wise)

Internal detail. Hours from Estimation Master via feature files.

**Grand total (operational software):** 749 hours · **Go-live:** 749 · **Optional:** 0

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User and Access Management | Shared | 3 | 128 | 17.1% |
| 02 | File Inward, Unique ID and Pre-Scan Control | Business | 3 | 141 | 18.8% |
| 03 | Scanning and Searchable PDF/A Production | Business | 3 | 117 | 15.6% |
| 04 | Quality Control and Physical Return | Business | 3 | 137 | 18.3% |
| 05 | Metadata, Cataloguing and Indexing | Business | 2 | 93 | 12.4% |
| 06 | e-Office Upload, Backup and Progress MIS | Technical | 3 | 133 | 17.8% |
| | **Total** | | **17** | **749** | **100%** |

## Effort profile

| Type | Hours | % |
|------|------:|---:|
| Shared | 128 | 17.1% |
| Business | 488 | 65.2% |
| Technical | 133 | 17.8% |

Largest features: F02-002 (61), F06-001 (59), F04-001 (57), F05-002 (55), F01-001 (50), F03-001 (48).

## Indicative phasing

IFQ contract is two months, single phase. Software build order:

| Phase | Modules |
|-------|---------|
| P1 — Access and custody | 01, 02 |
| P2 — Scan, QC, return | 03, 04 |
| P3 — Metadata, e-Office, MIS | 05, 06 |

## Optional commercial line items (not in feature hours)

Quote in the IFQ format (unit rate including all taxes):

| Line | Description | Indicative quantity |
|------|-------------|---------------------|
| 1 | Pre-scanning activities | 5,45,000 pages |
| 2 | Scanning A4 and/or Legal | 5,15,000 pages |
| 3 | Scanning A3 or larger | 30,000 pages |
| 4 | Post-scanning activities | 5,45,000 pages |
| 5 | Metadata creation, cataloguing, indexing | 12,000 files |

## Exclusions (not in feature hours)

- Scanners, PCs, servers, LAN, UPS, consumables, licensed QC imaging software, manpower for page production.
- DMG space, furniture, electricity, internet.
- Building e-Office or a public/mobile app.
- SLA penalties and liquidated damages.
- Blank pages (not payable per IFQ).

## 01 — User and Access Management (128 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F01-001 | Project Staff Accounts | 50 | SP and Department users with name, designation and ID |
| F01-002 | Login and Role Session | 48 | Operator / Supervisor / Department Officer session |
| F01-003 | Authorised Handover List | 30 | Who may hand over and receive physical files |

## 02 — File Inward, Unique ID and Pre-Scan Control (141 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F02-001 | Unique File ID | 40 | ID marked on covers and noting pages |
| F02-002 | Inward Log and Page Census | 61 | IFQ inward fields and page counts by size |
| F02-003 | Pre-Scan Batch and Exceptions | 40 | Batch prep; missing page / unfit-for-scan flags |

## 03 — Scanning and Searchable PDF/A Production (117 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F03-001 | Scan Production Recording | 48 | Pages by size and colour/grey; no blanks |
| F03-002 | Searchable PDF/A Package | 43 | One searchable PDF/A per file |
| F03-003 | Exception Capture Devices | 26 | Overhead, flatbed, camera, high-DPI |

## 04 — Quality Control and Physical Return (137 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F04-001 | Independent QC Checklist | 57 | IFQ image checks; scanner cannot QC own file |
| F04-002 | Rescan and Defect Closure | 36 | Failures tracked to QC pass |
| F04-003 | Outward Log and Physical Return | 44 | Daily return with authorised countersignature |

## 05 — Metadata, Cataloguing and Indexing (93 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F05-001 | Folder Tree and File Naming | 38 | Department-approved path and file name |
| F05-002 | File Metadata Capture | 55 | Active / Closed / Archive quarry-lease fields |

## 06 — e-Office Upload, Backup and Progress MIS (133 hours)

| Feature ID | Feature Name | Hours | Notes |
|---|---|---:|---|
| F06-001 | e-Office and Department Upload | 59 | Compatibility gate, upload status, retry |
| F06-002 | Backup and Restore Verification | 34 | Daily backup log and restore tests |
| F06-003 | Progress Reports | 40 | Daily, weekly, monthly and overall MIS |
