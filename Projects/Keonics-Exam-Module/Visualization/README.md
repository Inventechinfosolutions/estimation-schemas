# EXAM Visualization Pack

ChatGPT / LLM **prompt briefs** to generate architecture and process visualizations for the KEONICS Examination Module.

**Source:** Feature pack — 12 modules, 87 features  
**DB:** `../EXAM_Database_Design.md` v2.1

## How to use

1. Open the module file for the diagram you need.
2. Copy from `PROMPT START` to `PROMPT END`.
3. Paste into ChatGPT (or similar) and ask for Mermaid diagrams / slides / whiteboard visuals.
4. If the model hits length limits, use the **Quick paste** section at the bottom of each file, then attach specific features as follow-ups.

## Modules

| Mod | Name | File | Features |
|-----|------|------|----------|
| 00 | Programme overview (all modules) | [`M00_programme-overview_ChatGPT_Brief.md`](./M00_programme-overview_ChatGPT_Brief.md) | 12 mods |
| 01 | User & Role Management | [`M01_01-user-and-role-management_ChatGPT_Brief.md`](./M01_01-user-and-role-management_ChatGPT_Brief.md) | 12 |
| 02 | API Integration Hub | [`M02_02-api-integration-hub_ChatGPT_Brief.md`](./M02_02-api-integration-hub_ChatGPT_Brief.md) | 4 |
| 03 | Examination Centre Management | [`M03_03-examination-centre-management_ChatGPT_Brief.md`](./M03_03-examination-centre-management_ChatGPT_Brief.md) | 11 |
| 04 | Question Bank & Examination Configuration | [`M04_04-question-bank-and-examination-configuration_ChatGPT_Brief.md`](./M04_04-question-bank-and-examination-configuration_ChatGPT_Brief.md) | 7 |
| 05 | Candidate Registration | [`M05_05-candidate-registration_ChatGPT_Brief.md`](./M05_05-candidate-registration_ChatGPT_Brief.md) | 14 |
| 06 | Examination Scheduling & Allocation | [`M06_06-examination-scheduling-and-allocation_ChatGPT_Brief.md`](./M06_06-examination-scheduling-and-allocation_ChatGPT_Brief.md) · **per-feature:** [`M06/`](./M06/) | 5 |
| 07 | Notification Service | [`M07_07-notification-service_ChatGPT_Brief.md`](./M07_07-notification-service_ChatGPT_Brief.md) | 7 |
| 08 | Centre Operations | [`M08_08-centre-operations_ChatGPT_Brief.md`](./M08_08-centre-operations_ChatGPT_Brief.md) | 5 |
| 09 | Secure Examination Conduct | [`M09_09-secure-examination-conduct_ChatGPT_Brief.md`](./M09_09-secure-examination-conduct_ChatGPT_Brief.md) | 8 |
| 10 | Evaluation & Results | [`M10_10-evaluation-and-results_ChatGPT_Brief.md`](./M10_10-evaluation-and-results_ChatGPT_Brief.md) | 5 |
| 11 | Certificate Management | [`M11_11-certificate-management_ChatGPT_Brief.md`](./M11_11-certificate-management_ChatGPT_Brief.md) | 6 |
| 12 | Examination Administration & Reporting | [`M12_12-examination-administration-and-reporting_ChatGPT_Brief.md`](./M12_12-examination-administration-and-reporting_ChatGPT_Brief.md) | 3 |

## Suggested diagram set (programme-level)

1. Full 12-module platform context map
2. Candidate journey (Modules 05 → 06 → 07 → 09 → 10 → 11)
3. Centre exam-day journey (Modules 03 → 08 → 09)
4. Admin configuration spine (01 → 02 → 03 → 04 → 07)
5. Enterprise data model overview from DDL

## Related files

- `../EXAM_Database_DDL_MySQL.sql`
- `../EXAM_Database_DDL.sql`
- `../EXAM_Database_Gap_Analysis.md`
