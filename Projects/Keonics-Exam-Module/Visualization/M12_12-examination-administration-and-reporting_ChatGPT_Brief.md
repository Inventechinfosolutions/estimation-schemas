# ChatGPT Visualization Brief — Module 12: Examination Administration & Reporting

**How to use:** Copy everything from “PROMPT START” to “PROMPT END” into ChatGPT (or another diagramming LLM). Ask it to generate diagrams (architecture, sequence, state machines, ERD, swimlanes, charts). Prefer Mermaid.

**Source:** `EXAM_Feature_Specification` — KEONICS Examination Module
**Module:** 12 Examination Administration & Reporting
**Features:** 3 (F12-010 … F12-012)
**DB design:** `EXAM_Database_Design.md` v2.1 · DDL: `EXAM_Database_DDL_MySQL.sql` / `EXAM_Database_DDL.sql`

---

## PROMPT START

You are a solutions architect and visualization designer. Using ONLY the Module 12 specification below, generate clear diagrams and visuals for stakeholders and developers. Prefer Mermaid where possible; also describe what each diagram should show.

**Produce these visuals:**
1. MIS suite map (centre-wise / category-dept / certificate)
2. Report run pipeline (params → query ops tables → export)
3. Data lineage from modules 03/05/06/08/10/11 into MIS
4. Admin report UX flow
5. Feature relationship / dependency graph within this module and to other modules
6. ERD for tables listed in DATA MODEL section

---

### MODULE OVERVIEW

**Name:** Examination Administration & Reporting
**Purpose:** MIS reporting suites: centre-wise, category/department-wise, and certificate reports over operational data from prior modules.

**Actors (union across features):**
- Examination Administrator

**Feature list:**
- **F12-010** — Centre-wise MIS Report Suite
- **F12-011** — Category-wise and Department-wise MIS Report Suite
- **F12-012** — Certificate MIS Report Suite

### DATA MODEL (from EXAM DB design v2.1)

- `mis_report_definition`
- `mis_report_run`

### FEATURE CATALOGUE

#### F12-010 — Centre-wise MIS Report Suite

**One-liner / description:** Centre-wise MIS reports covering centre registration allocation summary, centre attendance summary, centre pass-fail summary, and centre session utilization report with filters, on-screen grids, and Excel and PDF export.

**Business objective:** Enable administrators to analyse examination operations and outcomes by authorised examination centre for capacity planning and centre performance review.

**Actors:** Examination Administrator

**User journey (14 steps):**
1. Administrator opens Centre-wise MIS Report Suite index.
2. Administrator selects Centre Allocation Summary Report.
3. Parameters include examination cycle, examination, and optional centre multi-select.
4. Grid lists each centre with configured capacity, allocated candidates, utilization percentage, and unallocated overflow count referred from other centres if applicable.
5. Administrator exports allocation summary.
6. Administrator selects Centre Attendance Summary Report.
7. Parameters add session date range.
8. Grid shows appeared, absent, and attendance rate per centre.
9. Administrator selects Centre Pass-Fail Summary Report.
10. Grid shows passed, failed, and pass rate per centre for evaluated candidates.
11. Administrator selects Centre Session Utilization Report.
12. Grid lists session slots per centre with activated versus scheduled counts.
13. Administrator exports each report to Excel and PDF as needed.
14. Empty state when no centres match filters.

**Functional capabilities:**
- Centre-wise MIS report suite index
- Centre allocation summary report parameter form
- Centre allocation summary report grid
- Centre attendance summary report parameter form
- Centre attendance summary report grid
- Centre pass-fail summary report parameter form
- Centre pass-fail summary report grid
- Centre session utilization report parameter form
- Centre session utilization report grid
- Excel export per centre-wise report
- PDF export per centre-wise report
- Centre-wise report empty state

**Inputs:** Examination cycle identifier; Examination identifier; Optional centre multi-select; Optional session date range; Pagination for large centre lists

**Outputs:** Centre-wise summary grids; Excel export files; PDF export files

**Business rules:**
- Only authorised centres from module 03 appear in centre-wise reports
- Allocation counts from module 06 per centre
- Attendance from module 08 per centre
- Pass-fail from module 10 attributed to allotted centre on attempt
- Session utilization compares module 08 activated sessions to module 06 scheduled slots per centre
- Utilization percentage capped at 100 unless overbooking flag configured

**Validations:**
- Examination cycle and examination mandatory
- Session date range required for attendance and session utilization reports
- Centre multi-select values must be authorised centres
- Date range within schedule bounds

**Workflow / states:** Centre reporting flow: ParametersEntry → Generating → ResultsDisplayed → Exporting. Session utilization: Scheduled → Activated when module 08 activates candidate session at centre.

**Dependencies:**
- Module 01 — User & Role Management: Administrator authorization
- Module 03 — Examination Centre Management: Centre master and capacity
- Module 06 — Examination Scheduling & Allocation: Allocations and schedules
- Module 08 — Centre Operations: Attendance and activation
- Module 10 — Evaluation & Results: Pass-fail by attempt centre

**Risks:** Centres with zero capacity configuration cause division errors without validation guard; Cross-centre reassignment after allocation rare; report uses final allocation only

**Notes:** SOW section 40 centre-wise reporting views.

---

#### F12-011 — Category-wise and Department-wise MIS Report Suite

**One-liner / description:** Category-wise and department-wise MIS reports covering registration counts, fee collection, attendance, and pass-fail outcomes grouped by candidate category and government department or organisation affiliation with…

**Business objective:** Support departmental management reporting on examination participation and outcomes segmented by candidate category and department or organisation for policy and workforce planning.

**Actors:** Examination Administrator

**User journey (17 steps):**
1. Administrator opens Category-wise and Department-wise MIS Report Suite index.
2. Administrator selects Category-wise Registration Summary Report.
3. Parameter form captures examination cycle, optional examination, and category multi-select.
4. Grid displays registration counts and percentage share per category with totals row.
5. Administrator exports category registration summary to Excel and PDF.
6. Administrator selects Department-wise Registration Summary Report.
7. Parameters include examination cycle, examination, and optional department multi-select.
8. Grid lists departments with registration counts sorted descending.
9. Administrator selects Category-wise Pass-Fail Report.
10. Grid shows appeared, passed, failed, and pass rate per category.
11. Administrator selects Department-wise Pass-Fail Report.
12. Grid shows pass-fail metrics per department for selected examination.
13. Administrator selects Category-wise Fee Collection Report.
14. Grid shows collected fee totals per category.
15. Administrator exports each report as needed.
16. Empty state when filters yield no rows.
17. Validation errors display for missing mandatory examination cycle.

**Functional capabilities:**
- Category and department MIS report suite index
- Category-wise registration summary report parameter form
- Category-wise registration summary report grid
- Department-wise registration summary report parameter form
- Department-wise registration summary report grid
- Category-wise pass-fail report parameter form
- Category-wise pass-fail report grid
- Department-wise pass-fail report parameter form
- Department-wise pass-fail report grid
- Category-wise fee collection report parameter form
- Category-wise fee collection report grid
- Excel export per category and department report

**Inputs:** Report identifier; Examination cycle identifier; Optional examination identifier; Category multi-select filter; Department multi-select filter; Optional date range

**Outputs:** Category-wise summary grids; Department-wise summary grids; Excel export files; PDF export files

**Business rules:**
- Candidate category sourced from module 05 registration category at time of registration
- Department attribution uses KGID department for government employees and organisation name for PSU and other categories
- Unclassified department bucket captures registrations missing department affiliation
- Pass-fail metrics include only evaluated attempts
- Fee collection category-wise totals include successful payments only
- Percentage share columns calculated against report totals row

**Validations:**
- Examination cycle mandatory on all reports
- Category multi-select optional; empty means all categories
- Department multi-select optional; empty means all departments
- Date range within examination cycle bounds when provided
- Department filter ignored on category-only reports and vice versa where not applicable

**Workflow / states:** Report flow: ParametersEntry → Validating → Generating → ResultsDisplayed → Exporting. Category assignment fixed at registration confirmation per module 05.

**Dependencies:**
- Module 01 — User & Role Management: Administrator authorization
- Module 02 — API Integration Hub: KGID department fields on government employee registrations
- Module 05 — Candidate Registration: Category, department, and organisation affiliation
- Module 08 — Centre Operations: Attendance for pass-fail denominators
- Module 10 — Evaluation & Results: Pass-fail outcomes
- Module 02 — API Integration Hub: Payment records for category fee report

**Risks:** Inconsistent department naming for non-government candidates may fragment department-wise totals; Large department master may require top-N filtering on reports

**Notes:** SOW section 40 category-wise and department-wise reporting views for government and other organisation candidates.

---

#### F12-012 — Certificate MIS Report Suite

**One-liner / description:** Certificate MIS report suite covering certificate issuance summary, certificate eligibility backlog report, certificate status register report, and examination-wise certificate statistics with parameter forms,…

**Business objective:** Provide Examination Administrators MIS reporting on certificate issuance progress, eligibility backlog, and revoked certificates for departmental compliance reporting.

**Actors:** Examination Administrator

**User journey (17 steps):**
1. Administrator opens Certificate MIS Report Suite index.
2. Administrator selects Certificate Issuance Summary Report.
3. Parameter form requires examination cycle and optional examination multi-select.
4. Grid displays eligible, issued, pending issuance, and revoked counts per examination.
5. Administrator exports issuance summary to Excel and PDF.
6. Administrator selects Certificate Eligibility Backlog Report.
7. Parameters include examination cycle, examination, and optional days-pending threshold.
8. Grid lists candidates eligible but not yet issued with registration number, name, eligibility date, and days pending.
9. Administrator exports backlog listing to Excel.
10. Administrator selects Certificate Status Register Report.
11. Parameters allow filter by certificate status issued revoked cancelled.
12. Grid lists certificate number, candidate name, examination, issue date, status, and revocation date if applicable.
13. Administrator searches certificate register by certificate number or candidate name.
14. Administrator selects Examination-wise Certificate Statistics Report.
15. Grid shows issuance rate and revocation count per examination.
16. Administrator exports each report as needed.
17. Empty and validation error states display when applicable.

**Functional capabilities:**
- Certificate MIS report suite index
- Certificate issuance summary report parameter form
- Certificate issuance summary report grid
- Certificate eligibility backlog report parameter form
- Certificate eligibility backlog report grid
- Certificate status register report parameter form
- Certificate status register report grid with search
- Examination-wise certificate statistics report parameter form
- Examination-wise certificate statistics report grid
- Excel export per certificate MIS report
- PDF export per certificate MIS report
- Certificate MIS report empty state

**Inputs:** Report identifier; Examination cycle identifier; Optional examination multi-select; Certificate status filter; Days-pending threshold for backlog report; Search text for certificate register; Pagination parameters

**Outputs:** Certificate summary and register grids; Excel export files; PDF export files

**Business rules:**
- Certificate eligibility determined by module 11 rules after module 10 pass outcome
- Issued count includes active certificates with issued status
- Revoked and cancelled certificates counted separately in status register
- Backlog report includes only eligible-not-issued records
- Certificate numbers displayed in register when issued
- Public verification portal functionality remains module 11 out of scope for this module

**Validations:**
- Examination cycle mandatory
- Days-pending threshold must be non-negative integer
- Certificate status filter limited to issued, eligible-not-issued, revoked, cancelled
- Certificate number search requires minimum five characters
- Backlog export row limit enforced

**Workflow / states:** Certificate display lifecycle: NotEligible → Eligible → Issued; Issued → Revoked or Cancelled. Report flow: ParametersEntry → Generating → ResultsDisplayed → Exporting.

**Dependencies:**
- Module 01 — User & Role Management: Administrator authorization
- Module 05 — Candidate Registration: Candidate identity on certificate records
- Module 04 — Question Bank & Examination Configuration: Examination definitions
- Module 10 — Evaluation & Results: Pass outcome driving eligibility
- Module 11 — Certificate Management: Eligibility, issuance, numbering, and revocation states

**Risks:** Large backlog exports may expose significant PII volume requiring export approval workflow in future; Eligibility backlog counts mismatch if batch issuance jobs lag

**Notes:** SOW section 40 certificate report suite; certificate transactional logic remains module 11.

---

### CROSS-MODULE CONTEXT

Place this module on the platform map:
```text
[01 IAM] → [02 Integration] → [03 Centre] → [04 Q-Bank/Config]
         → [05 Registration] → [06 Schedule] → [07 Notify]
         → [08 Centre Ops] → [09 Conduct] → [10 Results]
         → [11 Certificate] → [12 MIS]
```
Highlight Module 12 and its immediate upstream/downstream dependencies from the feature Dependencies sections.

### VISUALIZATION STYLE HINTS

- Prefer Mermaid (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`)
- Short node labels; put detail in notes under each diagram
- Colour: internal module services vs external systems vs other modules
- Call out audit, security, and idempotency points explicitly
- Do not invent features outside this specification

## PROMPT END

### Quick paste (if length-limited)

> Visualize KEONICS Exam **Module 12 Examination Administration & Reporting** (3 features).
> Features: F12-010 Centre-wise MIS Report Suite; F12-011 Category-wise and Department-wise MIS Report Suite; F12-012 Certificate MIS Report Suite.
> Purpose: MIS reporting suites: centre-wise, category/department-wise, and certificate reports over operational data from prior modules.
> Draw: MIS suite map (centre-wise / category-dept / certificate); Report run pipeline (params → query ops tables → export); Data lineage from modules 03/05/06/08/10/11 into MIS; Admin report UX flow; ERD for `mis_report_definition`, `mis_report_run`.
