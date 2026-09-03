# BDAIT — Estimation Summary

Internal roll-up. Hours from feature files via Estimation Master.

| Item | Value |
|------|------:|
| Modules | 5 |
| Features | 13 |
| **Grand total** | **541 hours** |
| Recommended go-live | 541 hours |
| Optional / conditional | 0 hours |

## Per-module totals

| # | Module | Type | Features | Hours |
|---|--------|------|---------:|------:|
| 01 | User Account and Access Management | Shared | 4 | 188 |
| 02 | Dropdown Values | Business | 1 | 16 |
| 03 | Asset Request Management | Business | 3 | 122 |
| 04 | Ticket Management | Business | 3 | 120 |
| 05 | Admin Dashboard | Business | 2 | 95 |
| | **Total** | | **13** | **541** |

All 13 features are recommended go-live. Nothing is optional in this baseline.

Module 02 is create-only dropdown values (not a catalogue). Hours reduced from the previous 75-hour catalogue pair.

## Open assumptions / risks

1. Access is User / Admin only — no person or post.
2. Admin-only credentials; no self-service password, OTP, or SSO.
3. Dropdown values are create-only; no edit/deactivate catalogue.
4. No email/SMS, HR feed, inventory, purchase, or data migration.
5. Admin status change is the workflow; no maker–checker.
6. Hosting, SSL, and backup operations are not in feature hours.

## Suggested next actions

1. Review feature hours with BDA IT.
2. Confirm employee-number format and whether a seed Admin account is provided by BDA.
3. Client Word export is in `BDAIT_Estimation_Summary_FeatureWise_Client.docx`.
