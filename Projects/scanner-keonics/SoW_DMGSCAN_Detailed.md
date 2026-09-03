# Statement of Work (SOW)

# Karnataka State Electronics Development Corporation Limited (KEONICS)

# Scanning and Digitization of Files and Records  
# Department of Mines and Geology, Bengaluru Urban District

**Document Type:** Statement of Work – Business Requirements  
**Version:** 1.0  
**Status:** Draft  
**Source:** Invitation for Quotation No. KSEDC/IT/P2S1/2026-27 [E-245458] dated 28.08.2026  
**Prepared for:** KEONICS (Purchaser) / Department of Mines and Geology, Bengaluru Urban (User Department)

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [Project Objectives](#3-project-objectives)
4. [In Scope / Out of Scope](#4-in-scope--out-of-scope)
5. [Solution Expectations](#5-solution-expectations)
6. [Consolidated Functional Modules](#6-consolidated-functional-modules)
7. [End-to-End Workflows](#7-end-to-end-workflows)
8. [Access Control](#8-access-control)
9. [Channels](#9-channels)
10. [Integrations](#10-integrations)
11. [Audit, Compliance & Security](#11-audit-compliance--security)
12. [Non-Functional Requirements](#12-non-functional-requirements)
13. [Data Migration](#13-data-migration)
14. [Phased Delivery](#14-phased-delivery)
15. [Deliverables](#15-deliverables)
16. [Acceptance Criteria](#16-acceptance-criteria)
17. [Expected Benefits](#17-expected-benefits)
18. [Assumptions & Dependencies](#18-assumptions--dependencies)
19. [Vendor Response Expectations](#19-vendor-response-expectations)
20. [Appendix A — Module & Feature Index](#20-appendix-a--module--feature-index)
21. [Appendix B — Indicative Volumes and Quotation Lines](#21-appendix-b--indicative-volumes-and-quotation-lines)
22. [Appendix C — Metadata Fields](#22-appendix-c--metadata-fields)
23. [Appendix D — Inward Log Fields](#23-appendix-d--inward-log-fields)

---

## 1. Introduction

This Statement of Work restates the **Invitation for Quotation (IFQ)** issued by **Karnataka State Electronics Development Corporation Limited (KEONICS)** to appoint a **Service Provider** for **scanning and digitization of files and records** at the **Department of Mines and Geology (DMG), Bengaluru Urban District**, office of the Senior Geologist.

The IFQ is a **service procurement** (on-site scanning, digitization, metadata, upload and physical file return). This SOW is prepared for RFP discussion and estimation. It does **not** prescribe technology stack, APIs, database design or screen layouts.

**Document handling** (physical files and searchable PDF/A) and **status workflow** (inward → scan → quality check → metadata → upload → return) are **embedded** in the production process. They are not a separate document-management product. Target storage for departmental use is **e-Office and/or the Department’s system**, not a new public portal.

---

## 2. Project Overview

KEONICS invites sealed quotations from GST-registered companies/firms to complete scanning and digitization **only at** the DMG Bengaluru Urban office (not at multiple locations or at the Service Provider’s premises).

Indicative volume is **12,000 files** and **5,45,000 pages** (about **5,15,000** A4 and/or Legal pages and **30,000** A3 or larger pages). Quantities in the IFQ are **indicative** for arriving at total project cost; actual A3/A2/A1 counts will be determined from physical files during work.

The production chain is:

1. **Pre-scanning** — receive files, clean/dust/fumigate, untag/unpin, number pages, unique file ID, inward log.  
2. **Scanning and digitization** — sheet-feed / overhead / flatbed / digital camera as required; searchable PDF/A (ISO 19005-1:2005) at 150–200 dpi grey scale or colour (or 600 dpi+ if not legible); English and/or Kannada text searchable as present on the page.  
3. **Post-scanning** — independent quality check, incremental backup, restore physical order, outward log, return files daily.  
4. **Metadata, cataloguing and indexing** — Department-approved folder tree, file names, and metadata for **Active**, **Closed** and **Archive** files (quarry-lease oriented fields).  
5. **Upload** to e-Office and/or the Department’s system; daily backup and periodic restore tests; daily/weekly/monthly progress reports; training of Department staff.

### 2.1 Business context

| Aspect | Description |
| ------ | ----------- |
| Purchaser | KEONICS (a Government of Karnataka enterprise) |
| User department | Department of Mines and Geology, Bengaluru Urban |
| Place of work | Office of the Senior Geologist, DMG Bengaluru Urban only |
| Working hours | 10:00 AM to 05:30 PM on Government working days; longer hours/holidays only with Senior Geologist permission |
| Contract period | Two (2) months |
| Payment | 100% after successful completion and Department certification; KEONICS pays the Service Provider after receipt of corresponding payment from DMG |
| Primary outcome | Searchable PDF/A files with metadata, uploaded as required, physical files returned intact |

### 2.2 Guiding principles

1. Files never leave DMG premises.  
2. Physical files are returned in original order, all pages intact, on a daily basis to authorised staff.  
3. Scanned PDF/A must be a replica of the paper file and compatible with e-Office (and any Department DMS) — compatibility is tested **before** full-scale production.  
4. Blank pages are not counted for payment.  
5. Unfinished work, left-outs and error rectification identified during or after the contract remain the Service Provider’s responsibility at no extra cost.  
6. Confidentiality: no third party or public in the designated area; no scanning of files other than those handed over by the Department.

---

## 3. Project Objectives

1. Digitise the indicated DMG Bengaluru Urban files and records on site within the contract period.  
2. Maintain an auditable chain of custody (unique ID, inward/outward log, authorised staff).  
3. Produce searchable PDF/A files (English and/or Kannada as on the page) at the required quality.  
4. Capture metadata, catalogue and index files for Active, Closed and Archive categories.  
5. Upload digitised files to e-Office and/or the Department system.  
6. Protect data through daily backup and restore verification.  
7. Train Department staff on scanning, indexing, upload and retrieval in the software and/or e-Office.  
8. Provide daily, weekly, monthly and overall progress visibility to the Department.

---

## 4. In Scope / Out of Scope

### In Scope

**A. Scanning and digitization services (commercial / production — IFQ quotation lines)**

- Pre-scanning activities for the indicative page volume.  
- Scanning and digitization of A4 and/or Legal pages and of A3 or larger pages.  
- Post-scanning activities (QC, backup of images, physical reconstitution).  
- Metadata creation, cataloguing and indexing per file.  
- On-site scanners (sheet-feed, overhead, flatbed), digital camera where no scanner can be used, computers, servers, LAN, UPS, printers, consumables, pinning/unpinning tools, licensed QC software, and skilled staff.  
- Work only at DMG Bengaluru Urban; hours as in the IFQ.  
- Training of Department staff.  
- Completion of leftover/error work at no extra cost.

**B. Operational software supporting the service (estimable application scope in Section 6)**

- Simple **user → role** access for Service Provider operators/supervisors and Department authorised officers.  
- Digital support for **unique file ID**, **inward/outward log** (fields in Appendix D), page census and exception flags (missing pages, unfit for scan).  
- Recording of scan production (page size, colour/grey, device type) and link to the PDF/A package.  
- Quality-check recording (independent of the scanning team) and rescan tracking.  
- Capture of folder path, file name and metadata (Appendix C), expandable per Department instruction.  
- Recording of e-Office / Department-system upload status.  
- Backup/restore verification log and daily/weekly/monthly progress reports.

### Out of Scope

- Scanning at any location other than DMG Bengaluru Urban.  
- Building, replacing or customising **e-Office** or a general Department DMS product (compatibility and upload only).  
- Citizen / public portal, mobile application for the public, or KEONICS-wide scanning factory software beyond this site.  
- (The IFQ IPR clause mentions web/mobile source code in generic purchaser language. **No mobile or public web product is specified** in the scope of services; none is included here.)  
- Payment for blank pages.  
- Office space, furniture, electricity and internet bandwidth (provided by DMG).  
- GST registration of the bidder (eligibility; not a deliverable).  
- SLA cash penalties, liquidated damages and commercial bid evaluation (procurement, not software features).  
- Civil works, department file-room redesign, and long-term archival hardware owned by DMG after handover.  
- Detailed technical architecture, API contracts, database schemas and UI wireframes (design stage).

---

## 5. Solution Expectations

- Chain of custody is complete: every file handed over is uniquely identified, logged in, scanned (or exception recorded), quality-checked, metadated, backed up, uploaded as required, and logged out with signatures.  
- PDF/A packages open page-by-page over the network and print 1:1 legibly after compression.  
- Metadata supports quarry-lease retrieval (file no., lease no., applicant/lease/crusher, survey, village/hobli/taluk, keywords, status).  
- Department officers can see progress without waiting for the final invoice.  
- e-Office compatibility is proven on a sample **before** mass scanning.  
- Language and labels suit Department and Service Provider staff (English/Kannada content on pages; operational UI language as agreed with the Department).

---

## 6. Consolidated Functional Modules

These modules are the **operational software** that supports the IFQ production process. Physical scanning throughput, hardware hire and page-rate effort are **not** converted into software hours; they remain IFQ commercial lines (Appendix B).

### 01. User and Access Management

**Purpose:** Identify Service Provider and Department staff who may receive, scan, check, metadate or acknowledge files, without a person/post hierarchy.

**Type:** Shared

**Functional requirements:**

- Maintain accounts for Service Provider operators, Service Provider supervisor, and Department authorised officers.  
- Capture name, designation and ID of staff authorised to receive and return files (IFQ 3.3.2.11).  
- One role per account; login with credentials issued for this project site.  
- Disable accounts when a person is no longer authorised.

**Acceptance criteria:**

- Only listed authorised staff appear on inward/outward logs.  
- Department officers cannot be impersonated by Service Provider operators.  
- Disabled accounts cannot sign in.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F01-001 | Project staff accounts | Create and maintain Service Provider and Department users with name, designation and ID |
| F01-002 | Login and role session | Sign-in shows only the functions of Operator, Supervisor or Department Officer |
| F01-003 | Authorised handover list | Maintain who may hand over and receive physical files for the log |

---

### 02. File Inward, Unique ID and Pre-Scan Control

**Purpose:** Receive files from the Department, assign a unique ID, number pages, record the inward log, and prepare batches without mixing chronology.

**Type:** Business

**Functional requirements:**

- Allocate and mark a unique file ID on front cover, back cover and internal noting pages before scanning.  
- Record inward log fields (Appendix D), including page counts by size and grey/colour intent.  
- Record cleaning/dusting/fumigation done, untag/unpin, manual page numbering (self-inking numbering machines), sequence check.  
- Flag missing pages/documents and files unfit for scan; notify Department Official (recorded, not email product).  
- Track that files do not leave premises.

**Acceptance criteria:**

- No scan job starts without unique ID and inward log.  
- Page count at inward is available to compare with pages scanned.  
- Missing-page exceptions are visible to the Department Officer.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F02-001 | Unique file ID | Allocate and record unique ID marked on file covers and noting pages |
| F02-002 | Inward log and page census | Log receipt with IFQ inward fields and page counts by size |
| F02-003 | Pre-scan batch and exceptions | Batch preparation notes; missing page / unfit-for-scan flags |

---

### 03. Scanning and Searchable PDF/A Production

**Purpose:** Capture every page with the appropriate device and store one searchable PDF/A digital file per physical file.

**Type:** Business

**Functional requirements:**

- Record device used (sheet-feed, overhead, flatbed, digital camera) per file or page-range.  
- Produce searchable PDF/A (ISO 19005-1:2005) at 150–200 dpi grey/colour, or 600 dpi+ if not legible; bilingual search English/Kannada as on the page.  
- Do not count blank pages for production/payment quantities.  
- Store under Department-approved naming (detailed in Module 05) and keep pages in original chronology.

**Acceptance criteria:**

- Each completed file has one PDF/A containing all required pages.  
- Pages scanned can be reconciled to inward page census (excluding blanks).  
- Torn/fragile items use overhead/flatbed/camera as recorded.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F03-001 | Scan production recording | Record pages scanned by size, colour/grey and device |
| F03-002 | Searchable PDF/A package | Assemble and store one searchable PDF/A per file |
| F03-003 | Exception capture devices | Record overhead, flatbed, camera and high-DPI rescans for fragile or illegible pages |

---

### 04. Quality Control and Physical Return

**Purpose:** An independent team checks image quality against the IFQ checklist, triggers rescan, reconstitutes the physical file, and logs outward return.

**Type:** Business

**Functional requirements:**

- QC by a team other than scanners: skew, crop, lighting, colour consistency, blur, folds, binding bulge, edge darkness, replica of original.  
- Failures raise rescan; no extra commercial claim.  
- After QC, restore original tagging/stapling, serial count, outward log with date-time and Department countersignature.  
- Daily return to authorised officer.

**Acceptance criteria:**

- QC pass/fail is stored against the digital file.  
- Outward log matches inward unique IDs.  
- Damage incidents can be recorded for penalty handling (penalty itself is commercial).

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F04-001 | Independent QC checklist | Record IFQ image-quality checks pass/fail |
| F04-002 | Rescan and defect closure | Track failed QC to rescan completion |
| F04-003 | Outward log and physical return | Log return of reconstituted files to Department |

---

### 05. Metadata, Cataloguing and Indexing

**Purpose:** Apply Department-approved folder tree, file names, keywords and metadata for Active, Closed and Archive files (Mines and Geology / e-Office digitisation framework).

**Type:** Business

**Functional requirements:**

- Store files in the approved folder tree with approved file names.  
- Capture metadata sets in Appendix C; fields are indicative and must be extendable when the Department customises them.  
- Keywords for search; document type; page size and number; file status; remarks / closing / archive remarks as applicable.

**Acceptance criteria:**

- A digitised file cannot be marked complete for upload without mandatory metadata for its status (Active / Closed / Archive).  
- Search by file no., quarry lease no., survey no., village and keywords is possible in the operational tool.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F05-001 | Folder tree and file naming | Apply Department-approved storage path and file name |
| F05-002 | File metadata capture | Capture Active, Closed and Archive metadata including quarry-lease fields |

---

### 06. e-Office Upload, Backup and Progress MIS

**Purpose:** Upload packages to e-Office and/or the Department system, prove daily backups, and report progress.

**Type:** Technical

**Functional requirements:**

- Record upload of each digitised file to e-Office and/or Department system; retry on failure.  
- Daily incremental backup to secure external storage; periodic restore test recorded.  
- If data is lost during the contract, rescan at no extra cost (operational obligation; system records the loss event).  
- Daily, weekly, monthly and overall progress reports (files, pages by size, QC pending, uploaded, returned).  
- Sample compatibility test with e-Office **before** full-scale scanning (gate recorded).

**Acceptance criteria:**

- Upload status is visible per unique file ID.  
- Backup and restore tests are dated and attributable.  
- Progress reports match production counts used for Department certification.

#### Key capabilities (feature outline)

| Feature ID | Capability | Description |
|------------|------------|-------------|
| F06-001 | e-Office and department upload | Record and complete upload of each PDF/A package |
| F06-002 | Backup and restore verification | Daily backup log and periodic restore test |
| F06-003 | Progress reports | Daily, weekly, monthly and overall production MIS |

---

## 7. End-to-End Workflows

### 7.1 File day cycle

1. Department authorised officer hands over files; both sides identified.  
2. Service Provider inward-logs, unique-IDs, numbers pages, prepares batch.  
3. Operators scan with the appropriate device; PDF/A is stored.  
4. Separate QC team checks images; fail → rescan.  
5. Metadata and folder/file name applied.  
6. Incremental backup; upload when Department requires.  
7. Physical file reconstituted and outward-logged; returned the same day.

There is **no** maker–checker approval of allotment or lease decisions. Department countersignature on the log is custody acknowledgement, not a content approval inbox.

### 7.2 e-Office compatibility gate

1. Service Provider produces a sample set of PDF/A files.  
2. Compatibility with e-Office / Department DMS is tested.  
3. Full-scale scanning proceeds only after this check is recorded as passed.

---

## 8. Access Control

Access is **user → role**. There is no person, post or organisational-position model in the IFQ.

| Role | Who | What they can do |
| ---- | --- | ---------------- |
| Service Provider Operator | Scanning / metadata staff | Inward (as assigned), scan recording, metadata entry, not final Department acknowledgement |
| Service Provider Supervisor | Site in-charge | All operator functions plus QC oversight, reports, staff list, backup verification |
| Department Officer | DMG authorised staff | Hand over / receive files, view logs and progress, countersign outward, raise exceptions |

Rules:

- Permissions only through the role on the account.  
- Cross-user visibility of all files is Supervisor and Department Officer.  
- Operators work the production queue they are assigned.

---

## 9. Channels

| Channel | In scope | Notes |
| ------- | -------- | ----- |
| On-site operational application at DMG office | Yes | Used by Service Provider and Department officers |
| e-Office / Department system (upload target) | Yes | Existing systems; not rebuilt |
| Citizen / public portal | No | |
| Native mobile app | No | Not specified in IFQ services |

---

## 10. Integrations

| System | Status |
| ------ | ------ |
| e-Office | In scope — compatibility test and upload of digitised files |
| Department application / DMS | In scope if the Department designates it as the upload target |
| Email / SMS gateways | Out of scope |
| Payment gateways | Out of scope |

Internet for upload is provided by DMG (IFQ Section 4).

---

## 11. Audit, Compliance & Security

- Log who received, scanned, QC’d, metadated, uploaded and returned each unique file ID, with date and time.  
- Maintain confidentiality; Service Provider is responsible for data breach.  
- No third party or public in the designated area.  
- Backup media handled securely; data does not leave premises except as Department-approved upload.  
- IPR of deliverable digital records vests with the Purchaser as per IFQ; this SOW does not add a custom product IPR beyond operational software for this site.

---

## 12. Non-Functional Requirements

- Production window: 10:00–17:30 Government working days unless extended by Senior Geologist.  
- PDF/A viewable page-by-page over typical office network.  
- Scanners, PCs and licensed QC tools kept working; replacements at Service Provider cost (SLA).  
- Bilingual page content (English/Kannada) must be searchable in the PDF/A.  
- Contract duration two months; software must be usable from day one of production (simple, not a multi-year platform).

---

## 13. Data Migration

**This project is the digitization of paper records.** There is no separate legacy *database* migration. Historical paper files become PDF/A + metadata as described. Prior digital repositories are out of scope unless already inside e-Office.

---

## 14. Phased Delivery

**Single contract phase of two months**, covering all IFQ services.

Indicative build order for operational software (not a second commercial phase):

1. Access, unique ID, inward/outward log.  
2. Scan production + PDF/A + QC.  
3. Metadata, e-Office upload, backup, MIS.

---

## 15. Deliverables

1. Digitised searchable PDF/A files for accepted pages/files.  
2. Metadata, catalogue and index as approved by the Department.  
3. Upload into e-Office and/or Department system as instructed.  
4. Physical files returned intact with logs.  
5. Backup copies as specified.  
6. Daily/weekly/monthly/overall progress reports.  
7. Training of Department staff.  
8. Operational software listed in Section 6 (site use for the contract).

---

## 16. Acceptance Criteria

Program-level acceptance (aligned to Department certification before payment) is met when:

1. Agreed files are digitised to IFQ quality, blank pages excluded from counts.  
2. Unique IDs, inward and outward logs, and page reconciliation are complete.  
3. QC has been performed by a team other than scanners; defects closed.  
4. Metadata for Active/Closed/Archive is captured as instructed.  
5. Files are uploaded where required; backups exist and restore has been demonstrated.  
6. Physical files are returned; Department has certified completion.

---

## 17. Expected Benefits

- Retrievable digital copies of quarry/lease files without removing paper from site during the job.  
- Search by lease, survey and location fields.  
- Use inside e-Office.  
- Auditable movement of files during the two-month exercise.

---

## 18. Assumptions & Dependencies

1. Project code for artefacts is **DMGSCAN**; display name as on this cover.  
2. Output root is `Projects/scanner-keonics/`. Original IFQ PDF is unchanged.  
3. Access model is user → role (Operator / Supervisor / Department Officer).  
4. **Feature-hour estimates (later)** cover only Section 6 operational software. IFQ quotation lines 1–5 (pre-scan, scan A4/Legal, scan A3+, post-scan, metadata **production labour**) are commercial page/file rates, not software hours.  
5. Log register in the IFQ may be paper; the operational software **digitally mirrors** those fields for unique-ID tracking, metadata and MIS.  
6. e-Office APIs/upload method will be as the Department can actually provide; effort assumes a documented upload channel. If only manual e-Office user upload is allowed, F06-001 is a recording-and-checklist feature rather than a system-to-system feed.  
7. Metadata field lists in Appendix C are indicative and may be extended during the project without changing module boundaries.  
8. Cover-table A4/Legal quantity **5,15,000** is used for quotation; clause 3.1.13.3 stating 5,14,000 is treated as the same indicative band.  
9. Last date of quotation in the IFQ is read as printed; this SOW does not change procurement dates.  
10. DMG provides space, furniture, electricity and internet.  
11. No SMS/email notification product.  
12. Licensed QC software is brought by the Service Provider; this SOW does not rebuild a full imaging-QC engine, only **records** QC results in the operational tool.

---

## 19. Vendor Response Expectations

Vendors should:

1. Quote IFQ lines 1–5 inclusive of all taxes as specified.  
2. Confirm on-site only delivery, two-month duration, and e-Office compatibility test before full scan.  
3. Describe (business language) how unique ID, logs, QC independence, metadata and backup will be run.  
4. Not treat this SOW as a licence to bill a separate statewide DMS or mobile app.  
5. Identify dependencies on DMG (authorised officers, e-Office access, internet).

---

## 20. Appendix A — Module & Feature Index

| Module | Module Name | Type | Feature IDs (count) |
|--------|-------------|------|---------------------|
| 01 | User and Access Management | Shared | F01-001 … F01-003 (3) |
| 02 | File Inward, Unique ID and Pre-Scan Control | Business | F02-001 … F02-003 (3) |
| 03 | Scanning and Searchable PDF/A Production | Business | F03-001 … F03-003 (3) |
| 04 | Quality Control and Physical Return | Business | F04-001 … F04-003 (3) |
| 05 | Metadata, Cataloguing and Indexing | Business | F05-001 … F05-002 (2) |
| 06 | e-Office Upload, Backup and Progress MIS | Technical | F06-001 … F06-003 (3) |

**Total:** 6 modules, 17 feature outlines.

Slugs: `user-and-access-management`, `file-inward-unique-id-and-pre-scan-control`, `scanning-and-searchable-pdfa-production`, `quality-control-and-physical-return`, `metadata-cataloguing-and-indexing`, `eoffice-upload-backup-and-progress-mis`.

---

## 21. Appendix B — Indicative Volumes and Quotation Lines

| Line | Description | Indicative quantity |
|------|-------------|---------------------|
| 1 | Pre-scanning activities | 5,45,000 pages |
| 2 | Scanning and digitization of A4 and/or Legal | 5,15,000 pages |
| 3 | Scanning and digitization of A3 or larger | 30,000 pages |
| 4 | Post-scanning activities | 5,45,000 pages |
| 5 | Metadata creation, cataloguing, indexing | 12,000 files |

Quantities are indicative for total cost; actual A3/A2/A1 counts follow physical files.

---

## 22. Appendix C — Metadata Fields

**Active files:** File No.; Quarry Lease No.; Applicant / Lease / Crusher name; Subject/Description; Taluk; Hobli; Village; Survey No.; Keywords for Search; Created date; Document Type; Page Size & No.; File status; Remark.

**Closed files:** as Active, plus Closed date; Closing Remarks (Created date still captured).

**Archive files:** as Closed, plus Archived By; Archived On; Archived Remarks.

Fields are indicative and to be customised with the Department.

---

## 23. Appendix D — Inward Log Fields

Name of the document collected; Number of pages (A4 / Legal / A3 / A2 / A1 / A0 / others); Greyscale or colour scanning; Collected from (Department Official Name); Collected by and signature (Service Provider); Date of collection; Expected date of return; Returned to (Department Official) name and signature; Returned by (Service Provider); Actual date of return.

---

**End of Statement of Work**
