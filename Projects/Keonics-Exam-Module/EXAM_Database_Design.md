# Examination Module — Logical Database Design

**Project:** KEONICS Examination Module (`EXAM`)  
**Basis (authoritative):** `EXAM_Feature_Specification (1).md` — 12 modules, 87 features  
**Document type:** Logical / physical-ready data model  
**Version:** 2.1 (gaps filled)  
**Date:** 10 September 2026  
**DDL (PostgreSQL):** `EXAM_Database_DDL.sql`  
**DDL (MySQL 8):** `EXAM_Database_DDL_MySQL.sql`  
**Gap log:** `EXAM_Database_Gap_Analysis.md` (closed in v2.1)

This design is aligned to the **feature pack you provided**, not the 9-module repo SOW estimate.

| Pack metric | Value |
|-------------|------:|
| Modules | 12 |
| Features | 87 |
| All-in estimate (pack) | 10,164.6 hours |
| Physical tables in DDL | 84+ |

Technology-agnostic (PostgreSQL types shown in DDL). Physical hosting sizing refined at build time.

---

## 1. Design conventions

| Convention | Rule |
|------------|------|
| Primary key | `id` — UUID or bigserial |
| Soft lifecycle | Prefer `status` over hard delete for masters and accounts |
| Audit columns | `created_at`, `created_by`, `updated_at`, `updated_by` on mutable tables |
| Money | `DECIMAL(12,2)` + `currency_code` (INR) |
| Mobile | `VARCHAR(15)` normalised |
| Secrets | Store hashes / encrypted secrets only; never clear OTP or raw passwords |
| Naming | `snake_case`; module ownership noted below |

**Schemas:** `iam`, `integration`, `centre`, `qbank`, `registration`, `schedule`, `notify`, `ops_centre`, `conduct`, `result`, `certificate`, `mis`, `audit`

---

## 2. Module map

| # | Module | Features (count) |
|---|--------|------------------|
| 01 | User & Role Management | F01-007…020 (12) |
| 02 | API Integration Hub | F02-001…004 (4) |
| 03 | Examination Centre Management | F03-006…016 (11) |
| 04 | Question Bank & Examination Configuration | F04-001…007 (7) |
| 05 | Candidate Registration | F05-021…034 (14) |
| 06 | Examination Scheduling & Allocation | F06-001…005 (5) |
| 07 | Notification Service | F07-001…007 (7) |
| 08 | Centre Operations | F08-001…005 (5) |
| 09 | Secure Examination Conduct | F09-001…008 (8) |
| 10 | Evaluation & Results | F10-001…005 (5) |
| 11 | Certificate Management | F11-001…006 (6) |
| 12 | Examination Administration & Reporting | F12-010…012 (3) |

---

## 3. Module 01 — User & Role Management

**Features:** F01-007 … F01-020

#### `platform_role`
| Column | Notes |
|--------|-------|
| id PK | |
| code UNIQUE | `CANDIDATE`, `EXAM_ADMIN`, `INVIGILATOR`, `VERIFIER_PUBLIC` |
| name | |
| actor_category | `CANDIDATE`, `STAFF_ADMIN`, `STAFF_CENTRE`, `PUBLIC` |
| status | `DRAFT`, `ACTIVE`, `INACTIVE` |

#### `permission`
| id, code UNIQUE, journey_stage, module_area, is_baseline, description |

#### `role_permission`
| role_id, permission_id, effective_from, effective_to |

#### `permission_snapshot` — F01-007…010, F01-016  
| id, role_id, version_no, effective_from, grants_json, status (`PUBLISHED`/`SUPERSEDED`) |

#### `staff_user` — F01-014, F01-015, F01-011  
| id, username UNIQUE, **employee_id**, display_name, official_email, mobile, password_hash, user_kind (`ADMINISTRATOR`/`CENTRE_INVIGILATOR`), status, org_scope, must_reset_password, password_changed_at, failed_login_count, locked_until |  
**Constraint:** unique `employee_id` among active administrators (F01-014).

#### `staff_user_role`
| staff_user_id, role_id, effective_from, effective_to |

#### `staff_user_centre` — F01-009, F01-015, F03-013  
| staff_user_id, exam_centre_id, status |

#### `staff_session` — F01-011, F01-017  
| id, staff_user_id, token_hash, issued_at, expires_at, last_seen_at, revoked_at, client_meta_json |

#### `session_policy` — **gap fill F01-017**  
| id, role_type (`ADMINISTRATOR`/`CENTRE_INVIGILATOR`/`DEFAULT`), idle_timeout_minutes, absolute_lifetime_minutes, concurrent_session_limit, version_no, status, effective_from |  
Rule: idle < absolute; concurrent ≥ 1.

#### `credential_policy` — F01-018  
| min_length, complexity flags, history_count, max_failed_attempts, lockout_minutes, reset_token_ttl_minutes, version_no, status |

#### `staff_password_history` — **gap fill F01-018**  
| id, staff_user_id, password_hash, set_at | Last-N reuse prevention.

#### `staff_password_reset`
| id, staff_user_id, token_hash, expires_at, consumed_at |

#### `iam_security_event` — F01-019  
| Append-only: login success/fail, lock, permission change, session revoke |

#### `authorization_hook_registration` — F01-020  
| module_code, permission_codes_json, consumer_name |

#### `rate_limit_bucket` — **gap fill F01-010 (optional)**  
| bucket_key, window_start, hit_count | Public certificate verification probing control.

---

## 4. Module 02 — API Integration Hub

**Features:** F02-001 … F02-004

#### `integration_endpoint` — F02-003  
| id, code UNIQUE (`KGID`, `PAYMENT_GATEWAY`, …), name, base_url, auth_type, credential_ref, timeout_ms, retry_limit, is_primary, status |

#### `integration_credential` — F02-003  
| id, endpoint_id, secret_ciphertext, rotated_at, status |

#### `integration_call_log` — F02-004  
| id, endpoint_id, correlation_id, direction, http_status, success, attempt_no, request_meta_json (masked), response_meta_json (masked), error_code, occurred_at |

#### `kgid_lookup_cache` (optional) — F02-001  
| id, kgid_number, payload_json, fetched_at, expires_at |

Payment business rows live in Module 05 `payment_transaction`; Hub logs raw gateway calls here.

---

## 5. Module 03 — Examination Centre Management

**Features:** F03-006 … F03-016

#### `exam_centre`
| id, centre_code UNIQUE, name, address_line1/2, city, district, state, pincode, status (`DRAFT`/`ACTIVE`/`INACTIVE`) |

#### `exam_centre_capacity` — F03-010  
| centre_id UNIQUE, approved_capacity, **per_session_seat_capacity**, effective_from |  
Rule: per-session ≤ approved total.

#### `exam_centre_infrastructure` — F03-011  
| centre_id, **computer_terminal_count**, **lab_count**, **power_backup**, network_notes, details_json |

#### `centre_session_eligibility` — F03-012  
| id, exam_centre_id, examination_id NULL, **exam_session_id NULL**, allows_all_exams, status, effective_from |  
Unique (centre, session) when `exam_session_id` set.

#### `centre_network_restriction` — F03-014  
| centre_id, label, cidr, status |

#### `centre_device` — **gap fill F03-015**  
| centre_id, device_identifier, device_label, os_fingerprint, status | UNIQUE (centre_id, device_identifier) for whitelist + bulk import.

#### `centre_device_restriction` (optional legacy JSON)
| centre_id, allowed_device_json, whitelist_mode, status |

#### `centre_allocation_summary_cache` (optional) — F03-016  
| centre_id, as_of, allocated_count, capacity, utilisation_pct |

Invigilator binding: `iam.staff_user_centre`.

---

## 6. Module 04 — Question Bank & Examination Configuration

**Features:** F04-001 … F04-007

#### `question_category` — F04-001  
| id, code UNIQUE, name, parent_id NULL, status |

#### `question` / `question_option` — F04-002  
| question: category_id, question_type, stem_text, difficulty, marks, status |  
| option: question_id, option_key, option_text, is_correct, display_order |

#### `question_import_batch` — F04-003  
| file_name, imported_by, row/success/fail counts, status, error_log_json |

#### `examination` — F04-004  
| id, code UNIQUE, name, description, registration_open_at/close_at, **requires_admin_verification** (F05-034), **auto_evaluation_enabled**, status |

#### `examination_selection_rule` — F04-005  
| examination_id, total_question_count, rules_json, status, version_no |

#### `examination_randomisation_setting` — F04-006  
| examination_id, paper_version_count, randomise_questions, randomise_options, status, version_no |

#### `examination_lifecycle_config` — F04-007  
| examination_id, duration_minutes, question_count, total_marks, pass_marks, pass_percentage, negative_marking_*, unanswered_handling, multi_select_partial_rule, result_display_rules_json, certificate_eligibility_rules_json, version_no, status |

#### `examination_fee_rule` — **gap fill F04-007 / F05-029**  
| examination_id, candidate_category (`GOVERNMENT`/`OTHER_ORG`), attempt_type (`FIRST`/`SUBSEQUENT`), fee_amount, currency_code, status |  
Unique active row per (exam, category, attempt_type).

#### `conduct_security_policy` — **gap fill F09-006** (owned with exam config)  
| examination_id NULL (global default), allow_session_takeover, max_focus_violations, max_visibility_violations, critical_immediate_terminate, approved_browser_json, bind_device_fingerprint, status, version_no |

Freeze F04-005/006/007 (+ fee/security) snapshots onto `exam_session` / `exam_attempt` at schedule or start.

---

## 7. Module 05 — Candidate Registration

**Features:** F05-021 … F05-034

#### `candidate` — F05-021  
| id, mobile UNIQUE, display_name NULL, status |

#### `otp_security_parameter` — **gap fill F05-021**  
| otp_length, otp_ttl_seconds, max_verify_attempts, max_resends, resend_interval_seconds, idle_timeout_minutes, concurrent_session_limit, status, version_no |

#### `otp_challenge` — **gap fill F05-021**  
| mobile, candidate_id NULL, otp_hash, expires_at, verify_attempts, resend_count, locked_until, consumed_at |

#### `candidate_portal_session` — **gap fill F05-021**  
| candidate_id, token_hash, issued_at, expires_at, last_seen_at, revoked_at, client_meta_json |

#### `document_template` — F05-026  
| code UNIQUE, name, file_uri, status |

#### `registration` — F05-022…034  
| registration_number UNIQUE NULL (set at F05-032), candidate_id, examination_id, category_type, **organisation_sub_category** (`PSU`/`BOARD`/`CORPORATION`/`SOCIETY`/`OTHER`), kgid_number, kgid_snapshot_json, supplementary_json, employee_id, organisation_name, designation, date_of_joining, **photograph_uri**, attempt_no, fee_applicable, fee_amount, currency_code, fee_basis_snapshot_json, status, confirmed_at |

#### `registration_centre_preference` — F05-028  
| registration_id, preference_rank (1\|2), exam_centre_id |

#### `competent_authority_document` — F05-026  
| registration_id, template_code, file_name, storage_uri, content_type, uploaded_at |

#### `payment_transaction` — F05-030, F05-031, F02-002  
| registration_id, amount, currency_code, gateway_ref, status, initiated_at, completed_at, failure_reason, receipt_number, callback_json, correlation_id |

#### `registration_admin_review` — F05-034  
| registration_id UNIQUE, decision, remarks, reviewed_by, decided_at |

#### `candidate_exam_attempt_counter` — F05-029  
| candidate_id, examination_id, attempt_count |

#### `fee_determination_audit` — **gap fill F05-029**  
| registration_id, candidate_id, examination_id, category_type, attempt_no, fee_applicable, fee_amount, rule_id, decided_at, detail_json |

---

## 8. Module 06 — Examination Scheduling & Allocation

**Features:** F06-001 … F06-005

#### `exam_session` — F06-001  
| examination_id, exam_centre_id, session_date, start_time, end_time, reporting_time, duration_minutes, seat_capacity, config_snapshot_json, status |

#### `candidate_allocation` — F06-002  
| registration_id UNIQUE, exam_session_id, exam_centre_id, allocation_source (`AUTO`/`MANUAL`/`OVERRIDE`), **override_reason**, allocated_at, allocated_by |

#### `seat_assignment` — F06-003  
| allocation_id UNIQUE, seat_label, computer_label, locked_at |

#### `hall_ticket` — F06-004  
| registration_id UNIQUE, allocation_id, ticket_number UNIQUE, payload_json, issued_at, status |

#### `exam_credential` — F06-005  
| registration_id UNIQUE, allocation_id, login_id UNIQUE, password_hash, delivery_channel, delivered_at, status |

---

## 9. Module 07 — Notification Service

**Features:** F07-001 … F07-007

#### `notification_template` — F07-001  
| code UNIQUE, channel (`SMS`/`EMAIL`/`IN_APP`), subject, body_template, version_no, status |

#### `notification_channel_config` — F07-002  
| channel UNIQUE, provider_name, config_json, credential_ref, is_enabled |

#### `notification_event_route` — F07-003  
| event_code, template_id, channel, is_enabled |

#### `notification_job` — F07-004…006  
| event_code, channel, recipient, candidate_id NULL, staff_user_id NULL, registration_id NULL, payload_json, status, attempts, last_error, **parent_job_id**, **resend_reason**, created_at, sent_at |

#### `notification_delivery_attempt` — F07-005  
| job_id, attempt_no, provider_ref, status, occurred_at, error_text |

#### `in_app_notification` — F07-007  
| candidate_id, title, body, is_read, created_at |

---

## 10. Module 08 — Centre Operations

**Features:** F08-001 … F08-005

Operational state on **`exam_attempt`** (shared with Module 09):

| Column | Module 08 use |
|--------|----------------|
| registration_id, exam_session_id, exam_centre_id, allocation_id | F08-002 |
| attendance_status | `ABSENT`/`PRESENT`/`VERIFIED` |
| **verification_status** | `PENDING`/`VERIFIED`/`REJECTED` — F08-003 |
| **verification_reject_reason**, **absent_reason** | F08-003 |
| identity_verified_at, verified_by | F08-003 |
| activation_status | `NOT_ACTIVATED`/`ACTIVATED`/`REVOKED` — F08-004 |
| activated_by, activated_at | F08-004 |
| status | Feeds F08-001 / F08-005 |

#### `attendance_event` — **gap fill F08-003**  
| exam_attempt_id, event_type (`VERIFY`/`VERIFY_REJECT`/`MARK_PRESENT`/`MARK_ABSENT`/`CORRECTION`), from_status, to_status, reason_text, actor_staff_id, occurred_at |

#### `centre_ops_snapshot` (optional)  
| centre_id, session_id, as_of, present_count, activated_count, in_progress_count, submitted_count |

Photograph for identity check: `registration.photograph_uri`.

---

## 11. Module 09 — Secure Examination Conduct

**Features:** F09-001 … F09-008

#### `exam_attempt` (conduct fields) — F09-001, F09-002, F09-005…008  
| login_at, started_at, submitted_at, submit_mode, client_ip, device_fingerprint, network_check_result, timer_ends_at, last_heartbeat_at, **focus_violation_count**, **visibility_violation_count**, security_flags_json, status |  
Partial unique: one `IN_PROGRESS` attempt per registration.

#### `paper_instance` / `paper_instance_item` — F09-003  
| version_label, seed_value; items: sequence_no, question_id, option_order_json, correct_option_map_json |

#### `exam_response` — F09-004, F09-008  
| exam_attempt_id, paper_instance_item_id, selected_option_ids, answered_at, is_marked_for_review, is_locked |

#### `exam_activity_event` — F09-007  
| Append-only: LOGIN, START, AUTOSAVE, SECURITY, SUBMIT, TIMER_EXPIRY, … |

#### `access_denial_log` — F09-002  
| registration_id NULL, session_id NULL, reason_code, client_ip, occurred_at |

Security thresholds from `qbank.conduct_security_policy`.

---

## 12. Module 10 — Evaluation & Results

**Features:** F10-001 … F10-005

#### `evaluation_run` — F10-001, F10-003  
| exam_attempt_id UNIQUE, correct/incorrect/unanswered counts, **config_version_ref**, **config_snapshot_json**, engine_version, evaluated_at |

#### `score_result` — F10-002  
| evaluation_run_id UNIQUE, raw_score, negative_marks, total_score, percentage, pass_fail |

#### `evaluation_rule_alignment` — F10-003  
| examination_id, lifecycle_config_id, validation_status, error_codes_json, last_checked_at |

#### `result_publication` — F10-004  
| examination_id, exam_session_id NULL, status (`WITHHELD`/`PUBLISHED`), published_at, published_by, display_rules_snapshot_json |

#### `candidate_result` — F10-005  
| registration_id UNIQUE, score_result_id, publication_id, visible_to_candidate, display_snapshot_json |

---

## 13. Module 11 — Certificate Management

**Features:** F11-001 … F11-006

#### `certificate_number_sequence` — **gap fill F11-001**  
| examination_id UNIQUE, prefix, next_value, max_value, pad_width |

#### `certificate` — F11-001, F11-005  
| registration_id UNIQUE, examination_id, certificate_number UNIQUE, issue_date, status, **disclosure_snapshot_json**, document_uri, issued_at, cancelled_at, cancel_reason, cancelled_by |

#### `certificate_document` — F11-002  
| certificate_id UNIQUE, pdf_uri, qr_embedded, generated_at, render_engine_version |

#### `certificate_verification_token` — F11-002, F11-004  
| certificate_id UNIQUE, token UNIQUE, public_disclosure_json, status |

#### `certificate_verification_hit` — F11-004  
| token, result_code (`VALID`/`INVALID`/`CANCELLED`), queried_at, client_ip |

#### `certificate_download_log` — F11-003  
| certificate_id, candidate_id, downloaded_at |

#### `certificate_issuance_log` — **gap fill F11-001**  
| registration_id, examination_id, batch_run_id, outcome (`ISSUED`/`ISSUANCE_SKIPPED`/`ISSUANCE_FAILED`), certificate_id NULL, error_text, occurred_at |

#### `certificate_export_run` — F11-006 (optional)  
| requested_by, parameters_json, output_uri, row_count, status |

---

## 14. Module 12 — MIS Reporting

**Features:** F12-010 … F12-012

#### `mis_report_definition`
| code UNIQUE (`CENTRE_WISE`, `CATEGORY_DEPT_WISE`, `CERTIFICATE`), name, default_params_json, status |

#### `mis_report_run`
| report_code, parameters_json, requested_by, status, output_uri, row_count, created_at, completed_at |

Read models over operational tables; materialised views optional later.

---

## 15. Cross-cutting audit

#### `audit_event`
| id BIGSERIAL, occurred_at, actor_type, actor_id, module_code (`01`…`12`), action_code, entity_type, entity_id, before_json, after_json, channel, correlation_id |

F01-019 may write IAM subset into `iam_security_event` **or** `audit_event` with `module_code='01'`.

---

## 16. Feature → primary tables (v2.1)

| Feature range | Primary tables |
|---------------|----------------|
| F01-007…020 | `platform_role`, `permission`, `role_permission`, `permission_snapshot`, `staff_user*`, `staff_session`, `session_policy`, `credential_policy`, `staff_password_history`, `iam_security_event`, `rate_limit_bucket` |
| F02-001…004 | `integration_endpoint`, `integration_credential`, `integration_call_log`, `kgid_lookup_cache` |
| F03-006…016 | `exam_centre*`, `centre_device`, network restriction, `staff_user_centre`, eligibility (+ session FK) |
| F04-001…007 | `question*`, `examination`, selection/randomisation/lifecycle, `examination_fee_rule`, `conduct_security_policy` |
| F05-021…034 | `candidate`, OTP/session tables, `registration*`, payment, admin review, `fee_determination_audit` |
| F06-001…005 | `exam_session`, `candidate_allocation`, `seat_assignment`, `hall_ticket`, `exam_credential` |
| F07-001…007 | `notification_*` (incl. parent_job_id / resend_reason), `in_app_notification` |
| F08-001…005 | `exam_attempt` attendance/verification fields; `attendance_event`; ops snapshots |
| F09-001…008 | `exam_attempt` conduct + violation counters, `paper_instance*`, `exam_response`, activity/denial |
| F10-001…005 | `evaluation_run` (+ config snapshot), `score_result`, `result_publication`, `candidate_result` |
| F11-001…006 | `certificate_number_sequence`, `certificate*`, issuance log, verification token/hits |
| F12-010…012 | `mis_report_definition`, `mis_report_run` |

---

## 17. Suggested DDL order

1. Module 01 roles/permissions/staff + session/password policies  
2. Module 03 centres + devices (+ bind staff_user_centre)  
3. Module 04 examination + question bank + fee rules + security policy  
4. Module 02 integration endpoints  
5. Module 05 candidate + OTP + registration + payment + fee audit  
6. Module 06 schedule/allocation/ticket/credential (+ eligibility session FK)  
7. Module 07 notification  
8. Module 08/09 exam_attempt + attendance_event + paper + responses + activity  
9. Module 10 evaluation/results  
10. Module 11 certificates + numbering + issuance log  
11. Module 12 MIS run tables  
12. Global `audit_event`

---

## 18. Critical integrity rules

| Rule | Enforcement |
|------|-------------|
| Candidate baseline permissions immutable | `permission.is_baseline` + app |
| Invigilator only sees mapped centres | `staff_user_centre` |
| Two centre preferences | `preference_rank IN (1,2)` unique per registration |
| Fee rule uniqueness | Active unique (exam, category, attempt_type) |
| Payment success before confirm (when fee mandatory) | Registration status machine + `payment_transaction` |
| Hall ticket after allocation | FK hall_ticket → allocation |
| Paper randomisation preserves key | `paper_instance_item.correct_option_map_json` |
| Single in-progress attempt | Partial unique on `exam_attempt` |
| Certificate number / QR token unique | UNIQUE constraints + sequence table |
| Cancelled certificate verifies as cancelled | Token status + certificate.status |
| Integration secrets not in call logs | Masking in `integration_call_log` |
| Password reuse blocked | `staff_password_history` vs `credential_policy.history_count` |
| Device whitelist uniqueness | UNIQUE (centre_id, device_identifier) |

---

## 19. Out of scope

- Vendor-specific DDL beyond PostgreSQL dump  
- Object-storage layout (URI columns only)  
- Exact KGID/payment JSON schemas (snapshots)  
- OLAP warehouse (Phase 2)

---

## 20. Version history

| Version | Change |
|---------|--------|
| 1.0 | 9-module repo SOW design |
| 2.0 | Rebuilt for 12-module / 87-feature pack |
| **2.1** | **Filled all critical + medium schema gaps** (see gap analysis closed) |

---

**End of database design (v2.1 — gaps filled)**
