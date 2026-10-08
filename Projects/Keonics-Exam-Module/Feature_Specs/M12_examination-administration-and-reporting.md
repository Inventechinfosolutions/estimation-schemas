# Module 12: Examination Administration & Reporting

**Source:** `EXAM_Feature_Specification (1).md`  
**Features:** 3 (F12-010 … F12-012)  
**Parent pack:** [../EXAM_Feature_Specification (1).md](../EXAM_Feature_Specification%20(1).md)

---

## 12 Examination Administration & Reporting

745.5 hours · 84 tasks · Business

Department-wide administrator dashboard, operational oversight, and exportable examination MIS reports.

### F12-010 Centre-wise MIS Report Suite

245.15 hours · Go-live · 28 tasks

##### Description

Centre-wise MIS reports covering centre registration allocation summary, centre attendance summary, centre pass-fail summary, and centre session utilization report with filters, on-screen grids, and Excel and PDF export.

##### Business objective

Enable administrators to analyse examination operations and outcomes by authorised examination centre for capacity planning and centre performance review.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

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

##### Inputs

- Examination cycle identifier
- Examination identifier
- Optional centre multi-select
- Optional session date range
- Pagination for large centre lists

##### Outputs

- Centre-wise summary grids
- Excel export files
- PDF export files

##### Business rules

- Only authorised centres from module 03 appear in centre-wise reports
- Allocation counts from module 06 per centre
- Attendance from module 08 per centre
- Pass-fail from module 10 attributed to allotted centre on attempt
- Session utilization compares module 08 activated sessions to module 06 scheduled slots per centre
- Utilization percentage capped at 100 unless overbooking flag configured

##### Validations

- Examination cycle and examination mandatory
- Session date range required for attendance and session utilization reports
- Centre multi-select values must be authorised centres
- Date range within schedule bounds

##### Calculations

- Centre utilization equals allocated divided by capacity multiplied by 100
- Centre attendance rate equals appeared divided by allocated multiplied by 100
- Centre pass rate equals passed divided by evaluated non-absent at centre multiplied by 100
- Session utilization equals activated sessions divided by scheduled sessions multiplied by 100

##### Workflow

Centre reporting flow: ParametersEntry → Generating → ResultsDisplayed → Exporting. Session utilization: Scheduled → Activated when module 08 activates candidate session at centre.

##### Search requirements

- Centre multi-select lookup with code and name search
- Examination lookup

##### Reports

- Centre allocation summary MIS report
- Centre attendance summary MIS report
- Centre pass-fail summary MIS report
- Centre session utilization MIS report

##### Security

- Examination Administrator role required
- Centre-wise reports scoped department-wide not centre-login restricted
- Export audit-logged

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 03 — Examination Centre Management: Centre master and capacity
- Module 06 — Examination Scheduling & Allocation: Allocations and schedules
- Module 08 — Centre Operations: Attendance and activation
- Module 10 — Evaluation & Results: Pass-fail by attempt centre

##### Assumptions

- Candidate attributed to centre based on final allocation not preference
- Up to 500 centres per examination supported with pagination

##### Risks

- Centres with zero capacity configuration cause division errors without validation guard
- Cross-centre reassignment after allocation rare; report uses final allocation only

##### Non-functional requirements

- Centre allocation summary for 500 centres generates within 12 seconds
- Paginated centre grid pages load within 3 seconds

##### Notes

SOW section 40 centre-wise reporting views.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Centre-wise MIS report suite index screen | Easy | 14 |
| UI | Centre allocation summary report parameter form | Medium | 16 |
| UI | Centre allocation summary report result grid | Medium | 16 |
| UI | Centre attendance summary report parameter form | Medium | 16 |
| UI | Centre attendance summary report result grid | Medium | 16 |
| UI | Centre pass-fail summary report parameter form | Medium | 16 |
| UI | Centre pass-fail summary report result grid | Medium | 16 |
| UI | Centre session utilization report parameter form | Medium | 16 |
| UI | Centre session utilization report result grid | Medium | 16 |
| UI | Centre-wise MIS report empty state | Simple | 5 |
| API | Generate centre allocation summary MIS report data | Complex | 8 |
| API | Generate centre attendance summary MIS report data | Complex | 8 |
| API | Generate centre pass-fail summary MIS report data | Complex | 8 |
| API | Generate centre session utilization MIS report data | Complex | 8 |
| API | Export centre allocation summary MIS report to Excel | Complex | 8 |
| API | Export centre allocation summary MIS report to PDF | Complex | 8 |
| API | Export centre attendance summary MIS report to Excel | Complex | 8 |
| API | Export centre attendance summary MIS report to PDF | Complex | 8 |
| API | Export centre pass-fail summary MIS report to Excel | Complex | 8 |
| API | Export centre pass-fail summary MIS report to PDF | Complex | 8 |
| API | Export centre session utilization MIS report to Excel | Complex | 8 |
| API | Export centre session utilization MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for centre-wise allocation attendance pass-fail aggregates | Complex | 0.5 |
| Testing | Happy-path generation and exports for all four centre-wise MIS reports | Complex | 0.5 |
| Testing | Zero-capacity centre utilization guard and invalid date range cases | Medium | 0.3 |
| Testing | Centre pass rate denominator and pagination boundary cases | Medium | 0.3 |
| Documentation | Administrator runbook for centre-wise MIS report parameters and exports | Medium | 0.3 |
| Documentation | Technical notes for centre attribution and utilization calculations | Easy | 0.25 |

### F12-011 Category-wise and Department-wise MIS Report Suite

274.2 hours · Go-live · 30 tasks

##### Description

Category-wise and department-wise MIS reports covering registration counts, fee collection, attendance, and pass-fail outcomes grouped by candidate category and government department or organisation affiliation with parameter forms, on-screen grids, and Excel and PDF export.

##### Business objective

Support departmental management reporting on examination participation and outcomes segmented by candidate category and department or organisation for policy and workforce planning.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

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
- PDF export per category and department report
- Category and department report empty state
- Category and department report parameter validation display

##### Inputs

- Report identifier
- Examination cycle identifier
- Optional examination identifier
- Category multi-select filter
- Department multi-select filter
- Optional date range

##### Outputs

- Category-wise summary grids
- Department-wise summary grids
- Excel export files
- PDF export files

##### Business rules

- Candidate category sourced from module 05 registration category at time of registration
- Department attribution uses KGID department for government employees and organisation name for PSU and other categories
- Unclassified department bucket captures registrations missing department affiliation
- Pass-fail metrics include only evaluated attempts
- Fee collection category-wise totals include successful payments only
- Percentage share columns calculated against report totals row

##### Validations

- Examination cycle mandatory on all reports
- Category multi-select optional; empty means all categories
- Department multi-select optional; empty means all departments
- Date range within examination cycle bounds when provided
- Department filter ignored on category-only reports and vice versa where not applicable

##### Calculations

- Category registration share equals category count divided by total registrations multiplied by 100
- Department pass rate equals department passed divided by department evaluated non-absent multiplied by 100
- Category fee total sums successful payment amounts for registrations in that category

##### Workflow

Report flow: ParametersEntry → Validating → Generating → ResultsDisplayed → Exporting. Category assignment fixed at registration confirmation per module 05.

##### Search requirements

- Category multi-select lookup
- Department multi-select lookup with code and name search
- Examination lookup

##### Reports

- Category-wise registration summary MIS report
- Department-wise registration summary MIS report
- Category-wise pass-fail MIS report
- Department-wise pass-fail MIS report
- Category-wise fee collection MIS report

##### Security

- Examination Administrator role required
- Department-wise reports may contain workforce statistics subject to departmental data classification policy
- Export audit-logged with report type and filter snapshot

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 02 — API Integration Hub: KGID department fields on government employee registrations
- Module 05 — Candidate Registration: Category, department, and organisation affiliation
- Module 08 — Centre Operations: Attendance for pass-fail denominators
- Module 10 — Evaluation & Results: Pass-fail outcomes
- Module 02 — API Integration Hub: Payment records for category fee report

##### Assumptions

- Department master list aligns with KGID department codes for government employees
- PSU and other organisation candidates grouped by organisation name text field

##### Risks

- Inconsistent department naming for non-government candidates may fragment department-wise totals
- Large department master may require top-N filtering on reports

##### Non-functional requirements

- Department-wise pass-fail report for 200 departments generates within 10 seconds
- Category reports generate within 5 seconds for up to 20 categories

##### Notes

SOW section 40 category-wise and department-wise reporting views for government and other organisation candidates.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Category-wise and department-wise MIS report suite index screen | Easy | 14 |
| UI | Category-wise registration summary report parameter form | Medium | 16 |
| UI | Category-wise registration summary report result grid | Medium | 16 |
| UI | Department-wise registration summary report parameter form | Medium | 16 |
| UI | Department-wise registration summary report result grid | Medium | 16 |
| UI | Category-wise pass-fail report parameter form | Medium | 16 |
| UI | Category-wise pass-fail report result grid | Medium | 16 |
| UI | Department-wise pass-fail report parameter form | Medium | 16 |
| UI | Department-wise pass-fail report result grid | Medium | 16 |
| UI | Category-wise fee collection report parameter form | Medium | 16 |
| UI | Category-wise fee collection report result grid | Medium | 16 |
| UI | Category and department MIS report empty state | Simple | 5 |
| UI | Category and department MIS report parameter validation error display | Simple | 5 |
| API | Generate category-wise registration summary MIS report data | Complex | 8 |
| API | Generate department-wise registration summary MIS report data | Complex | 8 |
| API | Generate category-wise pass-fail MIS report data | Complex | 8 |
| API | Generate department-wise pass-fail MIS report data | Complex | 8 |
| API | Generate category-wise fee collection MIS report data | Complex | 8 |
| API | Export category-wise registration summary MIS report to Excel | Complex | 8 |
| API | Export category-wise registration summary MIS report to PDF | Complex | 8 |
| API | Export department-wise registration summary MIS report to Excel | Complex | 8 |
| API | Export department-wise registration summary MIS report to PDF | Complex | 8 |
| API | Export category-wise pass-fail MIS report to Excel | Complex | 8 |
| API | Export department-wise pass-fail MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for category and department dimension aggregates | Complex | 0.5 |
| Testing | Happy-path generation and exports for all five category and department reports | Complex | 0.5 |
| Testing | Unclassified department bucket and empty multi-select all-categories cases | Medium | 0.3 |
| Testing | Category share percentage and pass rate denominator edge cases | Medium | 0.3 |
| Documentation | Administrator runbook for category-wise and department-wise MIS reports | Medium | 0.3 |
| Documentation | Technical notes for department attribution rules across candidate categories | Medium | 0.3 |

### F12-012 Certificate MIS Report Suite

226.15 hours · Go-live · 26 tasks

##### Description

Certificate MIS report suite covering certificate issuance summary, certificate eligibility backlog report, certificate status register report, and examination-wise certificate statistics with parameter forms, on-screen grids, and Excel and PDF export.

##### Business objective

Provide Examination Administrators MIS reporting on certificate issuance progress, eligibility backlog, and revoked certificates for departmental compliance reporting.

##### Actors

- Examination Administrator

##### User journey

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

##### Functional capabilities

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
- Certificate MIS report parameter validation errors

##### Inputs

- Report identifier
- Examination cycle identifier
- Optional examination multi-select
- Certificate status filter
- Days-pending threshold for backlog report
- Search text for certificate register
- Pagination parameters

##### Outputs

- Certificate summary and register grids
- Excel export files
- PDF export files

##### Business rules

- Certificate eligibility determined by module 11 rules after module 10 pass outcome
- Issued count includes active certificates with issued status
- Revoked and cancelled certificates counted separately in status register
- Backlog report includes only eligible-not-issued records
- Certificate numbers displayed in register when issued
- Public verification portal functionality remains module 11 out of scope for this module

##### Validations

- Examination cycle mandatory
- Days-pending threshold must be non-negative integer
- Certificate status filter limited to issued, eligible-not-issued, revoked, cancelled
- Certificate number search requires minimum five characters
- Backlog export row limit enforced

##### Calculations

- Days pending equals current date minus eligibility date for backlog rows
- Issuance rate equals issued divided by eligible multiplied by 100
- Pending issuance equals eligible minus issued excluding revoked before issue

##### Workflow

Certificate display lifecycle: NotEligible → Eligible → Issued; Issued → Revoked or Cancelled. Report flow: ParametersEntry → Generating → ResultsDisplayed → Exporting.

##### Search requirements

- Certificate number partial and exact search
- Candidate name partial search on status register
- Examination multi-select lookup

##### Reports

- Certificate issuance summary MIS report
- Certificate eligibility backlog MIS report
- Certificate status register MIS report
- Examination-wise certificate statistics MIS report

##### Security

- Examination Administrator role required
- Certificate register export contains PII governed by masking policy
- Certificate report access audit-logged
- Revocation details visible to administrators only not public verification scope

##### Dependencies

- Module 01 — User & Role Management: Administrator authorization
- Module 05 — Candidate Registration: Candidate identity on certificate records
- Module 04 — Question Bank & Examination Configuration: Examination definitions
- Module 10 — Evaluation & Results: Pass outcome driving eligibility
- Module 11 — Certificate Management: Eligibility, issuance, numbering, and revocation states

##### Assumptions

- Certificate eligibility date stored when eligibility first determined in module 11
- QR code and PDF generation logic not duplicated; reports reference certificate metadata only

##### Risks

- Large backlog exports may expose significant PII volume requiring export approval workflow in future
- Eligibility backlog counts mismatch if batch issuance jobs lag

##### Non-functional requirements

- Certificate issuance summary generates within 8 seconds for 50,000 certificate records
- Status register search returns first page within 3 seconds

##### Notes

SOW section 40 certificate report suite; certificate transactional logic remains module 11.

##### Tasks

| Area | Task | Complexity | Hours |
| --- | --- | --- | ---: |
| UI | Certificate MIS report suite index screen | Easy | 14 |
| UI | Certificate issuance summary report parameter form | Medium | 16 |
| UI | Certificate issuance summary report result grid | Medium | 16 |
| UI | Certificate eligibility backlog report parameter form | Medium | 16 |
| UI | Certificate eligibility backlog report result grid with days pending column | Medium | 16 |
| UI | Certificate status register report parameter form | Medium | 16 |
| UI | Certificate status register report searchable result grid | Medium | 16 |
| UI | Examination-wise certificate statistics report parameter form | Medium | 16 |
| UI | Examination-wise certificate statistics report result grid | Medium | 16 |
| UI | Certificate MIS report empty state | Simple | 5 |
| UI | Certificate MIS report parameter validation error display | Simple | 5 |
| API | Generate certificate issuance summary MIS report data | Complex | 8 |
| API | Generate certificate eligibility backlog MIS report data | Complex | 8 |
| API | Search and generate certificate status register MIS report data | Complex | 8 |
| API | Generate examination-wise certificate statistics MIS report data | Complex | 8 |
| API | Export certificate issuance summary MIS report to Excel | Complex | 8 |
| API | Export certificate issuance summary MIS report to PDF | Complex | 8 |
| API | Export certificate eligibility backlog MIS report to Excel | Complex | 8 |
| API | Export certificate status register MIS report to Excel | Complex | 8 |
| API | Export examination-wise certificate statistics MIS report to PDF | Complex | 8 |
| Database | Reporting indexes for certificate eligibility issuance and status aggregates | Complex | 0.5 |
| Testing | Happy-path generation search and exports for all four certificate MIS reports | Complex | 0.5 |
| Testing | Days pending calculation and certificate number search minimum length cases | Medium | 0.3 |
| Testing | Revoked certificate status display and PII masking in export cases | Medium | 0.3 |
| Documentation | Administrator runbook for certificate MIS reports and backlog monitoring | Medium | 0.3 |
| Documentation | Technical notes for certificate status enumerations aligned with module 11 | Easy | 0.25 |
