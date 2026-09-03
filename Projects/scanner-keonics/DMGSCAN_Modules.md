# Scanning and Digitization (DMG Bengaluru Urban) — Module List

Source: SoW_DMGSCAN_Detailed.md (IFQ No. KSEDC/IT/P2S1/2026-27 [E-245458])

| # | Module | Type | Summary | Source |
|---|--------|------|---------|--------|
| 01 | User and Access Management | Shared | Service Provider and Department users with roles Operator, Supervisor, Department Officer. | Derived from IFQ authorised-staff rules |
| 02 | File Inward, Unique ID and Pre-Scan Control | Business | Unique file ID, inward log, page census, batch prep and exceptions. | Explicit in IFQ 3.3 |
| 03 | Scanning and Searchable PDF/A Production | Business | Device choice, page production, searchable PDF/A per file. | Explicit in IFQ 3.4 |
| 04 | Quality Control and Physical Return | Business | Independent QC checklist, rescan, outward log and daily physical return. | Explicit in IFQ 3.5 |
| 05 | Metadata, Cataloguing and Indexing | Business | Folder tree, file names, Active/Closed/Archive quarry-lease metadata. | Explicit in IFQ 3.6 |
| 06 | e-Office Upload, Backup and Progress MIS | Technical | e-Office/department upload, daily backup/restore tests, progress reports. | Explicit in IFQ 3.7–3.9 |

***Module Details***

### 01. User and Access Management

- **Type:** Shared
- **Summary:** Service Provider and Department users with roles Operator, Supervisor, Department Officer.
- **Source:** Derived from IFQ authorised-staff and confidentiality rules
- **In Scope:** Accounts with name, designation and ID; login; authorised handover list; enable/disable.
- **Out of Scope:** Person/post hierarchy, SSO, public users, KEONICS-wide IAM.
- **Key Actors:** Service Provider Supervisor (maintains SP staff); Department Officer (Department users as agreed); Operators (sign in).
- **Dependencies:** None.
- **Notes:** Access is user → role.

### 02. File Inward, Unique ID and Pre-Scan Control

- **Type:** Business
- **Summary:** Unique file ID, inward log, page census, batch prep and exceptions.
- **Source:** Explicit in IFQ
- **In Scope:** Unique ID on covers/noting; inward fields (SOW Appendix D); page counts; missing-page and unfit-for-scan flags; files must not leave premises (recorded).
- **Out of Scope:** Physical cleaning/fumigation labour hours (commercial pre-scan line); numbering-machine hardware purchase as a software feature.
- **Key Actors:** Department Officer (handover); Operator/Supervisor (receive and log).
- **Dependencies:** Module 01.
- **Notes:** Digital log mirrors the IFQ register.

### 03. Scanning and Searchable PDF/A Production

- **Type:** Business
- **Summary:** Device choice, page production, searchable PDF/A per file.
- **Source:** Explicit in IFQ
- **In Scope:** Record scan counts by size and colour/grey; PDF/A package; exception devices; blank pages excluded from counts.
- **Out of Scope:** Page-rate scanning labour and scanner hardware (IFQ quotation lines 2–3); building an OCR engine product beyond searchable PDF/A production recording.
- **Key Actors:** Operators scan; Supervisor oversees.
- **Dependencies:** Module 02.
- **Notes:** Physical scan work is commercial; this module is production recording and package storage.

### 04. Quality Control and Physical Return

- **Type:** Business
- **Summary:** Independent QC checklist, rescan, outward log and daily physical return.
- **Source:** Explicit in IFQ
- **In Scope:** QC checklist recording; rescan tracking; outward log with countersignature fields.
- **Out of Scope:** Licensed imaging-QC product (SP brings it); SLA penalty calculation engine; physical restapling labour (commercial post-scan line).
- **Key Actors:** QC operators (not the same as scanners); Department Officer countersigns return.
- **Dependencies:** Module 03.
- **Notes:** QC team independence is a process rule enforced by role.

### 05. Metadata, Cataloguing and Indexing

- **Type:** Business
- **Summary:** Folder tree, file names, Active/Closed/Archive quarry-lease metadata.
- **Source:** Explicit in IFQ
- **In Scope:** Approved path/name; metadata sets in SOW Appendix C; search by lease/survey/village/keywords.
- **Out of Scope:** Redesigning e-Office file taxonomy statewide; metadata labour per 12,000 files (commercial line 5) — software is capture and search, not per-file typing hours.
- **Key Actors:** Operators enter metadata; Supervisor/Department review completeness.
- **Dependencies:** Modules 02 and 03.
- **Notes:** Fields are indicative and extendable.

### 06. e-Office Upload, Backup and Progress MIS

- **Type:** Technical
- **Summary:** e-Office/department upload, daily backup/restore tests, progress reports.
- **Source:** Explicit in IFQ
- **In Scope:** Upload status per file; backup/restore log; daily/weekly/monthly/overall reports; compatibility-gate record.
- **Out of Scope:** Rebuilding e-Office; SMS/email; hosting beyond site backup devices.
- **Key Actors:** Supervisor; Department Officer (views MIS).
- **Dependencies:** Modules 04 and 05.
- **Notes:** Upload channel depends on what DMG can actually provide (assumption in SOW).

***Excluded / Embedded Capabilities***

| Capability | Treatment |
|------------|-----------|
| Document management product | Embedded as PDF/A + metadata; target is e-Office |
| Workflow engine | Embedded in inward → scan → QC → metadata → upload → return |
| Notifications | Out of scope |
| Audit | Embedded on custody and production records |
| Page-rate scanning, hardware, manpower | Commercial IFQ lines; not software modules |

***Assumptions***

1. SOW `{NN}` and `F{NN}-{SEQ}` reused.
2. Software hours exclude IFQ quotation labour lines 1–5.
3. Two-month on-site contract; software is a site operational tool.

***Risks***

1. e-Office may only allow manual upload — F06-001 effort and design change.
2. Indicative volumes may vary; MIS must not hard-code payment quantities as complete.
3. Treating this IFQ as a statewide DMS or mobile app would invent scope.
