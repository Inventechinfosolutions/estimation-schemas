# EXAM — Estimation Summary

Internal roll-up. Hours from feature files via Estimation Master.

| Item | Value |
|------|------:|
| Modules | 9 |
| Features | 34 |
| **Grand total** | **4090 hours** |
| Recommended go-live | 4090 hours |
| Optional / conditional | 0 hours |

## Per-module totals

| # | Module | Type | Features | Hours |
|---|--------|------|---------:|------:|
| 01 | Access Control and Staff User Management | Shared | 2 | 228 |
| 02 | Candidate Portal Access (OTP Login) | Shared | 2 | 229 |
| 03 | Examination, Centre and Fee Masters | Business | 4 | 494 |
| 04 | Candidate Registration and Fee Payment | Business | 6 | 656 |
| 05 | Scheduling, Allocation, Hall Tickets and Examination Credentials | Business | 4 | 409 |
| 06 | Question Bank and Paper Versions | Business | 2 | 256 |
| 07 | Secure Centre-Based Examination Conduct | Business | 6 | 794 |
| 08 | Evaluation, Results and Certificates | Business | 4 | 459 |
| 09 | Dashboards, Reports, Notifications and Audit | Shared | 4 | 565 |
| | **Total** | | **34** | **4090** |

## Open assumptions / risks

1. KGID API field availability drives government registration path completeness.
2. Centre-only CBT technical enforcement (IP/device/browser) finalised with Department infrastructure.
3. Payment gateway merchant setup is a Department dependency.
4. Question pool depth must support configured multi-version randomisation.
5. Attempt history for fee rules starts in this system unless legacy data is supplied.
6. Notification channels (SMS/email/portal) finalised at confirmation.

## Suggested next actions

1. Review feature hours with delivery leads.
2. Confirm optional features (if any) for go-live cut.
3. Share client Word export (`EXAM_Estimation_Summary_FeatureWise_Client.docx`).
