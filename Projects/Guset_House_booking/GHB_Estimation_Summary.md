# GHB — Estimation Summary (Internal)

**Project:** Guest House Booking and Access Management Platform  
**Project code:** GHB  
**As of:** 2026-09-22  
**Source:** `SoW_GHB_Detailed.md` · feature indexes under `modules/*/features/_index.md`

## Totals

| Metric | Value |
|--------|------:|
| Modules | 8 |
| Features | 30 |
| **Recommended go-live hours** | **1601** |
| Optional / conditional hours | 158 |
| **All-in hours** | **1759** |

Optional hours are primarily F05-004 (hardware handoff) and F08-003 (hardware adapter).

## Per-module hours

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | User Registration & Authentication | Shared | 4 | 226 | 14.1% |
| 02 | Site, Building & Room Configuration | Business | 4 | 240 | 15.0% |
| 03 | Booking & Room Allocation | Business | 5 | 256 | 16.0% |
| 04 | Online Payment Processing | Business | 3 | 152 | 9.5% |
| 05 | Access Credentials & Guest Check-in | Business | 5 | 254 | 15.9% |
| 06 | Administration, Monitoring & Reports | Business | 4 | 217 | 13.6% |
| 07 | Notification Service | Technical | 2 | 111 | 6.9% |
| 08 | Integration Hub | Technical | 3 | 303 | 18.9% |

## Hours by module type

| Type | Hours |
|------|------:|
| Business | 1119 |
| Shared | 226 |
| Technical | 414 |

## Open assumptions / risks

1. Payment gateway and SMS/email provisioned by client.  
2. Government identity verification depth may expand beyond document + admin status.  
3. Access hardware optional; core booking must not depend on it.  
4. No Phase 1 legacy migration.  
5. User→Role access model (no post hierarchy).

## Suggested next actions

1. Review module list and feature hours with stakeholders.  
2. Confirm whether F05-004 / F08-003 are in commercial go-live or optional add-on.  
3. Use client Word export: `GHB_Estimation_Summary_FeatureWise_Client.docx`.  
4. Clarify identity verification SLA and payment hold duration before build.
