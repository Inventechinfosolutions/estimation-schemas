# EXAM Database — Gap Analysis

**Basis:** `EXAM_Feature_Specification (1).md` (12 modules, **87** features)  
**Compared to:** `EXAM_Database_Design.md` **v2.1**  
**DDL companion:** `EXAM_Database_DDL.sql`  
**Date:** 10 September 2026  
**Status:** **CLOSED — all critical and medium schema gaps filled**

---

## 1. Verdict

| Metric | Was (v2.0) | Now (v2.1) |
|--------|------------|------------|
| Critical gaps | 8 open | **0 open** |
| Medium gaps | 12 open | **0 open** |
| Pack features mapped | 87 | 87 |
| Design + DDL aligned | Partial | **Yes** |

Logical design and DDL now include first-class tables/columns for every previously open gap. Remaining out-of-scope items (object storage layout, exact external JSON schemas, OLAP) are intentional, not schema gaps.

---

## 2. Critical gaps — filled

| # | Gap | Feature | Resolution in v2.1 / DDL |
|---|-----|---------|--------------------------|
| 1 | Staff session policy | F01-017 | `iam.session_policy` |
| 2 | Password history | F01-018 | `iam.staff_password_history` + `credential_policy.history_count` |
| 3 | OTP + candidate session | F05-021 | `otp_security_parameter`, `otp_challenge`, `candidate_portal_session` |
| 4 | Examination fee rules | F04-007 / F05-029 | `qbank.examination_fee_rule` |
| 5 | Centre devices as rows | F03-015 | `centre.centre_device` UNIQUE (centre, device_identifier) |
| 6 | Attendance / verification history | F08-003 | `conduct.attendance_event` + reason columns on `exam_attempt` |
| 7 | Conduct security policy | F09-006 | `qbank.conduct_security_policy` + violation counters on `exam_attempt` |
| 8 | Certificate numbering + issuance log | F11-001 | `certificate_number_sequence`, `certificate_issuance_log`, `disclosure_snapshot_json` |

---

## 3. Medium gaps — filled

| Gap | Feature | Resolution |
|-----|---------|------------|
| `employee_id` on staff | F01-014 | Column + partial unique among active admins |
| Per-session seat capacity | F03-010 | `exam_centre_capacity.per_session_seat_capacity` |
| Typed infrastructure fields | F03-011 | `computer_terminal_count`, `lab_count`, `power_backup` |
| Org sub-category | F05-025 | `registration.organisation_sub_category` |
| Candidate photograph URI | F08-003 | `registration.photograph_uri` |
| Admin verification flag | F05-034 | `examination.requires_admin_verification` |
| Fee determination audit | F05-029 | `registration.fee_determination_audit` |
| Notification resend link | F07-006 | `notification_job.parent_job_id`, `resend_reason` |
| Evaluation config snapshot | F10-001/003 | `evaluation_run.config_snapshot_json`, `config_version_ref` |
| Public verify rate-limit | F01-010 | `iam.rate_limit_bucket` |
| Allocation override reason | F06-002 | `candidate_allocation.override_reason` |
| Centre–session mapping clarity | F03-012 | `centre_session_eligibility.exam_session_id` FK + unique pair index |

---

## 4. Coverage by module (post-fill)

| Module | Severity |
|--------|----------|
| 01 User & Role | Closed |
| 02 Integration Hub | Closed |
| 03 Centre | Closed |
| 04 Q-Bank & Config | Closed |
| 05 Registration | Closed |
| 06 Scheduling | Closed |
| 07 Notification | Closed |
| 08 Centre Ops | Closed |
| 09 Conduct | Closed |
| 10 Results | Closed |
| 11 Certificate | Closed |
| 12 MIS | Closed |

---

## 5. Feature → status (all OK)

Every previously GAP / PARTIAL feature is now **OK** against design v2.1 + DDL. See `EXAM_Database_Design.md` §16 for table index.

---

## 6. Intentionally not modelled (not gaps)

| Item | Reason |
|------|--------|
| Object-storage folder layout | URI columns only |
| Exact KGID / payment gateway JSON | Stored as snapshots |
| OLAP / warehouse facts | Phase 2 |
| Pack feature ID renumbering (old cross-refs) | Spec documentation issue, not schema |

---

## 7. Design vs repo SOW (secondary — unchanged)

| Item | Feature pack DB | Repo 9-module SOW |
|------|-----------------|-------------------|
| Modules | 12 | 9 |
| Features | 87 | 34 |
| Hours | 10,164.6 | 4,090 |

---

## 8. Next steps (optional)

1. Apply `EXAM_Database_DDL.sql` to scratch PostgreSQL and smoke-test FKs.  
2. Generate ERD from DDL.  
3. Seed reference data (roles, MIS report codes already seeded).

---

**End of gap analysis (CLOSED)**
