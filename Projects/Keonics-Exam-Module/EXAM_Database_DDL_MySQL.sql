-- =============================================================================
-- KEONICS Examination Module (EXAM) — MySQL CREATE dump
-- Basis : EXAM_Feature_Specification (12 modules / 87 features)
-- Companion: EXAM_Database_Design.md v2.1 + EXAM_Database_Gap_Analysis.md
-- Date  : 2026-09-10
-- Dialect: MySQL 8.0+ (InnoDB, utf8mb4)
-- Notes :
--   * PostgreSQL schemas mapped to MySQL databases (iam, integration, ...)
--   * UUID -> CHAR(36) DEFAULT (UUID())
--   * TIMESTAMPTZ -> DATETIME(6)
--   * JSONB -> JSON
--   * Partial unique indexes implemented via generated columns where needed
--   * Staff IAM: person -> post occupancy -> post_manager -> post_role;
--     centre binding is on post; staff_user is login linked to person
--   * Module 01 decisions:
--       - Administrator posts always org-wide (no centre)
--       - Multi-centre invigilator OK (union of post centres)
--       - Vacant posts allowed; person without login allowed
--       - session_policy by role_type; multi-post uses PRIMARY person_post
--       - created_by / updated_by / assigned_by store acting post id (iam.post)
--   * Module 02 decisions:
--       - One ACTIVE endpoint per integration_type (KGID | PAYMENT)
--       - No kgid_lookup_cache; always call external API + call_log
--       - Retries stay on integration_call_log (attempt_no / correlation_id)
--   * Module 03 decisions:
--       - Device whitelist = centre_device rows only (no JSON restriction table)
--       - No allocation summary cache; compute live
--       - Centre eligibility = examination-level (centre_exam_eligibility)
--       - Capacity is versioned history (effective_from/to); one ACTIVE current per centre
--   * Module 04 decisions:
--       - Selection rules normalized (examination_selection_rule_line)
--       - One ACTIVE selection / randomisation / lifecycle per examination
--       - Result display + certificate eligibility as typed columns (no JSON)
--       - conduct_security_policy: global default + optional per-exam; browsers as rows
--   * Module 05 decisions:
--       - Keep KGID/supplementary/fee JSON snapshots
--       - Govt identity = unique KGID; Other = unique (employee_id + aadhaar_hash)
--       - Aadhaar = hash + last4 only; multi-exam registrations allowed
--       - At most one CONFIRMED registration per candidate + examination
--   * Module 06 decisions:
--       - Seat label unique per exam_session; hard seat_capacity (no over-allocate)
--       - Hall ticket keeps payload_json snapshot
--       - No session config_snapshot_json; use live ACTIVE Module 04 config
-- =============================================================================

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

CREATE DATABASE IF NOT EXISTS iam;
CREATE DATABASE IF NOT EXISTS integration;
CREATE DATABASE IF NOT EXISTS centre;
CREATE DATABASE IF NOT EXISTS qbank;
CREATE DATABASE IF NOT EXISTS registration;
CREATE DATABASE IF NOT EXISTS schedule;
CREATE DATABASE IF NOT EXISTS notify;
CREATE DATABASE IF NOT EXISTS ops_centre;
CREATE DATABASE IF NOT EXISTS conduct;
CREATE DATABASE IF NOT EXISTS result;
CREATE DATABASE IF NOT EXISTS certificate;
CREATE DATABASE IF NOT EXISTS mis;
CREATE DATABASE IF NOT EXISTS audit;

-- =============================================================================
-- MODULE 01 — User & Role Management
-- =============================================================================

CREATE TABLE `iam`.`platform_role` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64)  NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    actor_category  VARCHAR(32)  NOT NULL
                    CHECK (actor_category IN ('CANDIDATE','STAFF_ADMIN','STAFF_CENTRE','PUBLIC')),
    status          VARCHAR(32)  NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`permission` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(128) NOT NULL UNIQUE,
    journey_stage   VARCHAR(64),
    module_area     VARCHAR(32),
    is_baseline     BOOLEAN      NOT NULL DEFAULT FALSE,
    description     TEXT,
    created_at      DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6)  NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`role_permission` (
    role_id         CHAR(36) NOT NULL REFERENCES `iam`.`platform_role`(id),
    permission_id   CHAR(36) NOT NULL REFERENCES `iam`.`permission`(id),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    effective_to    DATETIME(6),
    PRIMARY KEY (role_id, permission_id, effective_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`permission_snapshot` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    role_id         CHAR(36) NOT NULL REFERENCES `iam`.`platform_role`(id),
    version_no      INTEGER NOT NULL,
    effective_from  DATETIME(6) NOT NULL,
    grants_json     JSON NOT NULL,
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('PUBLISHED','SUPERSEDED')),
    published_by    CHAR(36),
    published_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    UNIQUE (role_id, version_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ---------------------------------------------------------------------------
-- Org model: post -> person occupancy -> post&manager -> post_role
-- Rules: one person may hold many posts; one post has at most one active person;
--        manager is post -> manager_post; centre binding lives on post.
-- ---------------------------------------------------------------------------

CREATE TABLE `iam`.`person` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    employee_id     VARCHAR(64),
    display_name    VARCHAR(200) NOT NULL,
    official_email  VARCHAR(200),
    mobile          VARCHAR(15),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- exam_centre_id FK added after centre.exam_centre exists
CREATE TABLE `iam`.`post` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    post_kind       VARCHAR(32) NOT NULL
                    CHECK (post_kind IN ('ADMINISTRATOR','CENTRE_INVIGILATOR','OTHER')),
    exam_centre_id  CHAR(36) NULL COMMENT 'Centre-scoped posts (e.g. invigilator); NULL = org-wide',
    org_scope       BOOLEAN NOT NULL DEFAULT FALSE COMMENT 'TRUE for organisation-wide admin posts',
    description     TEXT,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    CHECK (
        (post_kind = 'CENTRE_INVIGILATOR' AND exam_centre_id IS NOT NULL AND org_scope = FALSE)
        OR (post_kind = 'ADMINISTRATOR' AND org_scope = TRUE)
        OR (post_kind = 'OTHER')
    )
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`person_post` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    person_id       CHAR(36) NOT NULL REFERENCES `iam`.`person`(id),
    post_id         CHAR(36) NOT NULL REFERENCES `iam`.`post`(id),
    is_primary      BOOLEAN NOT NULL DEFAULT FALSE
                    COMMENT 'Primary post for session_policy when person holds multiple posts',
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    effective_to    DATETIME(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    assigned_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    assigned_by     CHAR(36) COMMENT 'Acting post id (iam.post) that performed the assignment',
    UNIQUE KEY `uq_person_post_pair_from` (person_id, post_id, effective_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`post_manager` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    post_id         CHAR(36) NOT NULL REFERENCES `iam`.`post`(id),
    manager_post_id CHAR(36) NOT NULL REFERENCES `iam`.`post`(id),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    effective_to    DATETIME(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    CHECK (post_id <> manager_post_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`post_role` (
    post_id         CHAR(36) NOT NULL REFERENCES `iam`.`post`(id),
    role_id         CHAR(36) NOT NULL REFERENCES `iam`.`platform_role`(id),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    effective_to    DATETIME(6),
    PRIMARY KEY (post_id, role_id, effective_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Login account: one staff_user per person (credentials only; profile on person; authz via posts)
CREATE TABLE `iam`.`staff_user` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    person_id       CHAR(36) NOT NULL UNIQUE REFERENCES `iam`.`person`(id),
    username        VARCHAR(100) NOT NULL UNIQUE,
    password_hash   TEXT NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    must_reset_password BOOLEAN NOT NULL DEFAULT FALSE,
    password_changed_at DATETIME(6),
    failed_login_count INTEGER NOT NULL DEFAULT 0,
    locked_until    DATETIME(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`staff_session` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    staff_user_id   CHAR(36) NOT NULL REFERENCES `iam`.`staff_user`(id),
    token_hash      TEXT NOT NULL UNIQUE,
    issued_at       DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    expires_at      DATETIME(6) NOT NULL,
    last_seen_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    revoked_at      DATETIME(6),
    client_meta_json JSON
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`session_policy` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    role_type       VARCHAR(32) NOT NULL
                    COMMENT 'Resolved from platform role on PRIMARY person_post'
                    CHECK (role_type IN ('ADMINISTRATOR','CENTRE_INVIGILATOR','DEFAULT')),
    idle_timeout_minutes      INTEGER NOT NULL,
    absolute_lifetime_minutes INTEGER NOT NULL,
    concurrent_session_limit  INTEGER NOT NULL DEFAULT 1,
    version_no      INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    CHECK (idle_timeout_minutes > 0
       AND absolute_lifetime_minutes > idle_timeout_minutes
       AND concurrent_session_limit >= 1)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`credential_policy` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    min_length      INTEGER NOT NULL DEFAULT 8,
    require_upper   BOOLEAN NOT NULL DEFAULT TRUE,
    require_lower   BOOLEAN NOT NULL DEFAULT TRUE,
    require_digit   BOOLEAN NOT NULL DEFAULT TRUE,
    require_special BOOLEAN NOT NULL DEFAULT TRUE,
    history_count   INTEGER NOT NULL DEFAULT 5,
    max_failed_attempts INTEGER NOT NULL DEFAULT 5,
    lockout_minutes INTEGER NOT NULL DEFAULT 30,
    reset_token_ttl_minutes INTEGER NOT NULL DEFAULT 60,
    version_no      INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`staff_password_history` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    staff_user_id   CHAR(36) NOT NULL REFERENCES `iam`.`staff_user`(id),
    password_hash   TEXT NOT NULL,
    set_at          DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_staff_password_history_user` ON `iam`.`staff_password_history` (staff_user_id, set_at DESC);

CREATE TABLE `iam`.`staff_password_reset` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    staff_user_id   CHAR(36) NOT NULL REFERENCES `iam`.`staff_user`(id),
    token_hash      TEXT NOT NULL UNIQUE,
    expires_at      DATETIME(6) NOT NULL,
    consumed_at     DATETIME(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`iam_security_event` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    event_type      VARCHAR(64) NOT NULL,
    staff_user_id   CHAR(36),
    actor_username  VARCHAR(100),
    resource_type   VARCHAR(64),
    resource_id     VARCHAR(128),
    reason_code     VARCHAR(64),
    success         BOOLEAN NOT NULL,
    client_ip       VARCHAR(64),
    detail_json     JSON
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`authorization_hook_registration` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    module_code     VARCHAR(8) NOT NULL,
    permission_codes_json JSON NOT NULL,
    consumer_name   VARCHAR(200) NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `iam`.`rate_limit_bucket` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    bucket_key      VARCHAR(200) NOT NULL,
    window_start    DATETIME(6) NOT NULL,
    hit_count       INTEGER NOT NULL DEFAULT 0,
    UNIQUE (bucket_key, window_start)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 03 — Examination Centre (then bind post.exam_centre_id)
-- =============================================================================

CREATE TABLE `centre`.`exam_centre` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_code     VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    address_line1   VARCHAR(200) NOT NULL,
    address_line2   VARCHAR(200),
    city            VARCHAR(100) NOT NULL,
    district        VARCHAR(100) NOT NULL,
    state           VARCHAR(100) NOT NULL,
    pincode         VARCHAR(10)  NOT NULL,
    status          VARCHAR(32)  NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `iam`.`post`
    ADD CONSTRAINT fk_post_exam_centre
    FOREIGN KEY (exam_centre_id) REFERENCES `centre`.`exam_centre`(id);

CREATE TABLE `centre`.`exam_centre_capacity` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_id       CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    approved_capacity INTEGER NOT NULL CHECK (approved_capacity > 0),
    per_session_seat_capacity INTEGER CHECK (per_session_seat_capacity IS NULL OR per_session_seat_capacity > 0),
    effective_from  DATE NOT NULL DEFAULT (CURRENT_DATE),
    effective_to    DATE NULL COMMENT 'NULL = current open-ended version',
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','SUPERSEDED')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    CHECK (per_session_seat_capacity IS NULL
        OR per_session_seat_capacity <= approved_capacity),
    CHECK (effective_to IS NULL OR effective_to >= effective_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `centre`.`exam_centre_infrastructure` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_id       CHAR(36) NOT NULL UNIQUE REFERENCES `centre`.`exam_centre`(id),
    computer_terminal_count INTEGER,
    lab_count       INTEGER,
    power_backup    BOOLEAN,
    network_notes   TEXT,
    details_json    JSON,
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Centre approved for an examination (any later session of that exam)
CREATE TABLE `centre`.`centre_exam_eligibility` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    exam_centre_id  CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    examination_id  CHAR(36) NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    effective_from  DATE,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    UNIQUE KEY `uq_centre_exam_eligibility` (exam_centre_id, examination_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `centre`.`centre_network_restriction` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_id       CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    label           VARCHAR(100),
    cidr            VARCHAR(64) NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `centre`.`centre_device` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_id       CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    device_identifier VARCHAR(200) NOT NULL,
    device_label    VARCHAR(200),
    os_fingerprint  VARCHAR(200),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    UNIQUE (centre_id, device_identifier)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 04 — Question Bank & Examination Configuration
-- =============================================================================

CREATE TABLE `qbank`.`question_category` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    parent_id       CHAR(36) REFERENCES `qbank`.`question_category`(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`question` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    category_id     CHAR(36) NOT NULL REFERENCES `qbank`.`question_category`(id),
    question_type   VARCHAR(32) NOT NULL
                    CHECK (question_type IN ('SINGLE_CHOICE','MULTI_CHOICE','TRUE_FALSE')),
    stem_text       TEXT NOT NULL,
    difficulty      VARCHAR(16)
                    CHECK (difficulty IS NULL OR difficulty IN ('EASY','MEDIUM','HARD')),
    marks           NUMERIC(8,2) NOT NULL CHECK (marks > 0),
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`question_option` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    question_id     CHAR(36) NOT NULL REFERENCES `qbank`.`question`(id) ON DELETE CASCADE,
    option_key      VARCHAR(8) NOT NULL,
    option_text     TEXT NOT NULL,
    is_correct      BOOLEAN NOT NULL DEFAULT FALSE,
    display_order   INTEGER NOT NULL DEFAULT 0,
    UNIQUE (question_id, option_key)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`question_import_batch` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    file_name       VARCHAR(255) NOT NULL,
    imported_by     CHAR(36) COMMENT 'Acting post id (iam.post)',
    row_count       INTEGER NOT NULL DEFAULT 0,
    success_count   INTEGER NOT NULL DEFAULT 0,
    fail_count      INTEGER NOT NULL DEFAULT 0,
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('PROCESSING','COMMITTED','FAILED')),
    error_log_json  JSON,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    completed_at    DATETIME(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`examination` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    description     TEXT,
    registration_open_at  DATETIME(6),
    registration_close_at DATETIME(6),
    requires_admin_verification BOOLEAN NOT NULL DEFAULT FALSE,
    auto_evaluation_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','OPEN','CLOSED','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

ALTER TABLE `centre`.`centre_exam_eligibility`
    ADD CONSTRAINT fk_centre_exam_eligibility_exam
    FOREIGN KEY (examination_id) REFERENCES `qbank`.`examination`(id);

CREATE TABLE `qbank`.`examination_selection_rule` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    total_question_count INTEGER NOT NULL CHECK (total_question_count > 0),
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`examination_selection_rule_line` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    selection_rule_id CHAR(36) NOT NULL REFERENCES `qbank`.`examination_selection_rule`(id) ON DELETE CASCADE,
    category_id     CHAR(36) NOT NULL REFERENCES `qbank`.`question_category`(id),
    required_count  INTEGER NOT NULL CHECK (required_count > 0),
    difficulty      VARCHAR(16)
                    CHECK (difficulty IS NULL OR difficulty IN ('EASY','MEDIUM','HARD')),
    display_order   INTEGER NOT NULL DEFAULT 0,
    UNIQUE KEY `uq_selection_rule_category_diff` (selection_rule_id, category_id, difficulty)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`examination_randomisation_setting` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    paper_version_count INTEGER NOT NULL DEFAULT 1 CHECK (paper_version_count > 0),
    randomise_questions BOOLEAN NOT NULL DEFAULT TRUE,
    randomise_options   BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`examination_lifecycle_config` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    question_count  INTEGER,
    total_marks     NUMERIC(10,2) NOT NULL,
    pass_marks      NUMERIC(10,2),
    pass_percentage NUMERIC(5,2),
    negative_marking_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    negative_mark_value NUMERIC(8,2),
    unanswered_handling VARCHAR(32),
    multi_select_partial_rule VARCHAR(32),
    show_numeric_score BOOLEAN NOT NULL DEFAULT TRUE,
    show_pass_fail BOOLEAN NOT NULL DEFAULT TRUE,
    immediate_result_display BOOLEAN NOT NULL DEFAULT FALSE,
    certificate_requires_pass BOOLEAN NOT NULL DEFAULT TRUE,
    certificate_minimum_score NUMERIC(10,2),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`examination_fee_rule` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    candidate_category VARCHAR(32) NOT NULL
                    CHECK (candidate_category IN ('GOVERNMENT','OTHER_ORG')),
    attempt_type    VARCHAR(32) NOT NULL
                    CHECK (attempt_type IN ('FIRST','SUBSEQUENT')),
    fee_amount      DECIMAL(12,2) NOT NULL CHECK (fee_amount >= 0),
    currency_code   CHAR(3) NOT NULL DEFAULT 'INR',
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `qbank`.`conduct_security_policy` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NULL
                    COMMENT 'NULL = global default; set = per-exam override'
                    REFERENCES `qbank`.`examination`(id),
    allow_session_takeover BOOLEAN NOT NULL DEFAULT FALSE,
    max_focus_violations INTEGER NOT NULL DEFAULT 5,
    max_visibility_violations INTEGER NOT NULL DEFAULT 5,
    critical_immediate_terminate BOOLEAN NOT NULL DEFAULT TRUE,
    bind_device_fingerprint BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `qbank`.`conduct_security_allowed_browser` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    policy_id       CHAR(36) NOT NULL REFERENCES `qbank`.`conduct_security_policy`(id) ON DELETE CASCADE,
    browser_code    VARCHAR(64) NOT NULL,
    min_version     VARCHAR(32),
    UNIQUE KEY `uq_policy_browser` (policy_id, browser_code)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 02 — API Integration Hub
-- =============================================================================

CREATE TABLE `integration`.`integration_endpoint` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    integration_type VARCHAR(32) NOT NULL
                    CHECK (integration_type IN ('KGID','PAYMENT')),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    base_url        TEXT NOT NULL,
    auth_type       VARCHAR(32) NOT NULL
                    CHECK (auth_type IN ('API_KEY','OAUTH2','BASIC','NONE')),
    credential_ref  VARCHAR(200),
    timeout_ms      INTEGER NOT NULL DEFAULT 30000,
    retry_limit     INTEGER NOT NULL DEFAULT 3,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `integration`.`integration_credential` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    endpoint_id     CHAR(36) NOT NULL REFERENCES `integration`.`integration_endpoint`(id),
    secret_ciphertext TEXT NOT NULL,
    rotated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','ROTATED')),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `integration`.`integration_call_log` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    endpoint_id     CHAR(36) NOT NULL REFERENCES `integration`.`integration_endpoint`(id),
    correlation_id  VARCHAR(100) NOT NULL,
    direction       VARCHAR(16) NOT NULL CHECK (direction IN ('OUTBOUND','INBOUND')),
    http_status     INTEGER,
    success         BOOLEAN NOT NULL,
    attempt_no      INTEGER NOT NULL DEFAULT 1,
    request_meta_json  JSON,
    response_meta_json JSON,
    error_code      VARCHAR(64),
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_integration_call_log_corr` ON `integration`.`integration_call_log` (correlation_id);

-- =============================================================================
-- MODULE 05 — Candidate Registration
-- =============================================================================

CREATE TABLE `registration`.`candidate` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    mobile          VARCHAR(15) NOT NULL UNIQUE,
    display_name    VARCHAR(200),
    -- Identity (canonical): Govt = KGID; Other = employee_id + aadhaar_hash
    kgid_number     VARCHAR(64) NULL COMMENT 'Unique for government employees',
    employee_id     VARCHAR(64) NULL COMMENT 'Used with aadhaar for PSU/Other',
    aadhaar_hash    VARCHAR(128) NULL COMMENT 'SHA-256 (or similar) of Aadhaar; never store full number',
    aadhaar_last4   CHAR(4) NULL COMMENT 'Display only',
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','BLOCKED')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`otp_security_parameter` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    otp_length      INTEGER NOT NULL DEFAULT 6,
    otp_ttl_seconds INTEGER NOT NULL DEFAULT 300,
    max_verify_attempts INTEGER NOT NULL DEFAULT 5,
    max_resends     INTEGER NOT NULL DEFAULT 3,
    resend_interval_seconds INTEGER NOT NULL DEFAULT 60,
    idle_timeout_minutes INTEGER NOT NULL DEFAULT 30,
    concurrent_session_limit INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`otp_challenge` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    mobile          VARCHAR(15) NOT NULL,
    candidate_id    CHAR(36) REFERENCES `registration`.`candidate`(id),
    otp_hash        TEXT NOT NULL,
    expires_at      DATETIME(6) NOT NULL,
    verify_attempts INTEGER NOT NULL DEFAULT 0,
    resend_count    INTEGER NOT NULL DEFAULT 0,
    locked_until    DATETIME(6),
    consumed_at     DATETIME(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_otp_challenge_mobile` ON `registration`.`otp_challenge` (mobile, created_at DESC);

CREATE TABLE `registration`.`candidate_portal_session` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    candidate_id    CHAR(36) NOT NULL REFERENCES `registration`.`candidate`(id),
    token_hash      TEXT NOT NULL UNIQUE,
    issued_at       DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    expires_at      DATETIME(6) NOT NULL,
    last_seen_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    revoked_at      DATETIME(6),
    client_meta_json JSON
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`document_template` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    file_uri        TEXT NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`registration` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_number VARCHAR(64) UNIQUE,
    candidate_id    CHAR(36) NOT NULL REFERENCES `registration`.`candidate`(id),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    category_type   VARCHAR(32) NOT NULL
                    CHECK (category_type IN ('GOVERNMENT','OTHER_ORG')),
    organisation_sub_category VARCHAR(32)
                    CHECK (organisation_sub_category IS NULL OR organisation_sub_category IN
                          ('PSU','BOARD','CORPORATION','SOCIETY','OTHER')),
    kgid_number     VARCHAR(64),
    kgid_snapshot_json JSON,
    supplementary_json JSON,
    employee_id     VARCHAR(64),
    aadhaar_hash    VARCHAR(128) NULL COMMENT 'Captured at registration; hash only',
    aadhaar_last4   CHAR(4) NULL,
    organisation_name VARCHAR(200),
    designation     VARCHAR(200),
    date_of_joining DATE,
    photograph_uri  TEXT,
    attempt_no      INTEGER NOT NULL DEFAULT 1 CHECK (attempt_no >= 1),
    fee_applicable  BOOLEAN NOT NULL DEFAULT FALSE,
    fee_amount      DECIMAL(12,2),
    currency_code   CHAR(3) DEFAULT 'INR',
    fee_basis_snapshot_json JSON,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN (
                        'DRAFT','AWAITING_PAYMENT','PAYMENT_FAILED',
                        'PENDING_ADMIN_VERIFICATION','CONFIRMED','REJECTED','CANCELLED'
                    )),
    confirmed_at    DATETIME(6),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_registration_candidate_exam` ON `registration`.`registration` (candidate_id, examination_id);

CREATE TABLE `registration`.`registration_centre_preference` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id) ON DELETE CASCADE,
    preference_rank SMALLINT NOT NULL CHECK (preference_rank IN (1, 2)),
    exam_centre_id  CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    UNIQUE (registration_id, preference_rank),
    UNIQUE (registration_id, exam_centre_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`competent_authority_document` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id) ON DELETE CASCADE,
    template_code   VARCHAR(64) REFERENCES `registration`.`document_template`(code),
    file_name       VARCHAR(255) NOT NULL,
    storage_uri     TEXT NOT NULL,
    content_type    VARCHAR(100),
    uploaded_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`payment_transaction` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id),
    amount          DECIMAL(12,2) NOT NULL,
    currency_code   CHAR(3) NOT NULL DEFAULT 'INR',
    gateway_ref     VARCHAR(128),
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('INITIATED','SUCCESS','FAILED','REFUNDED','ABANDONED')),
    initiated_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    completed_at    DATETIME(6),
    failure_reason  TEXT,
    receipt_number  VARCHAR(64),
    callback_json   JSON,
    correlation_id  VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_payment_registration` ON `registration`.`payment_transaction` (registration_id, initiated_at DESC);

CREATE TABLE `registration`.`registration_admin_review` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    decision        VARCHAR(32) NOT NULL CHECK (decision IN ('APPROVED','REJECTED')),
    remarks         TEXT,
    reviewed_by     CHAR(36) COMMENT 'Acting post id (iam.post)',
    decided_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`candidate_exam_attempt_counter` (
    candidate_id    CHAR(36) NOT NULL REFERENCES `registration`.`candidate`(id),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    attempt_count   INTEGER NOT NULL DEFAULT 0 CHECK (attempt_count >= 0),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY (candidate_id, examination_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `registration`.`fee_determination_audit` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id),
    candidate_id    CHAR(36) NOT NULL,
    examination_id  CHAR(36) NOT NULL,
    category_type   VARCHAR(32) NOT NULL,
    attempt_no      INTEGER NOT NULL,
    fee_applicable  BOOLEAN NOT NULL,
    fee_amount      DECIMAL(12,2),
    rule_id         CHAR(36),
    decided_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    detail_json     JSON
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 06 — Scheduling & Allocation
-- =============================================================================

CREATE TABLE `schedule`.`exam_session` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    exam_centre_id  CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    session_date    DATE NOT NULL,
    start_time      TIME NOT NULL,
    end_time        TIME NOT NULL,
    reporting_time  TIME,
    duration_minutes INTEGER NOT NULL,
    seat_capacity   INTEGER NOT NULL CHECK (seat_capacity > 0)
                    COMMENT 'Hard cap: allocations must not exceed this (app-enforced)',
    status          VARCHAR(32) NOT NULL DEFAULT 'SCHEDULED'
                    CHECK (status IN ('DRAFT','SCHEDULED','IN_PROGRESS','COMPLETED','CANCELLED')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    created_by      CHAR(36) COMMENT 'Acting post id (iam.post)',
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_by      CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_exam_session_centre_date` ON `schedule`.`exam_session` (exam_centre_id, session_date);

CREATE TABLE `schedule`.`candidate_allocation` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    exam_session_id CHAR(36) NOT NULL REFERENCES `schedule`.`exam_session`(id),
    exam_centre_id  CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    allocation_source VARCHAR(32) NOT NULL
                    CHECK (allocation_source IN ('AUTO','MANUAL','OVERRIDE'))
                    COMMENT 'OVERRIDE = manual centre/session choice; must still respect seat_capacity',
    override_reason TEXT,
    allocated_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    allocated_by    CHAR(36) COMMENT 'Acting post id (iam.post)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `schedule`.`seat_assignment` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    allocation_id   CHAR(36) NOT NULL UNIQUE REFERENCES `schedule`.`candidate_allocation`(id),
    exam_session_id CHAR(36) NOT NULL REFERENCES `schedule`.`exam_session`(id),
    seat_label      VARCHAR(64) NOT NULL,
    computer_label  VARCHAR(64),
    locked_at       DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    UNIQUE KEY `uq_session_seat_label` (exam_session_id, seat_label)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `schedule`.`hall_ticket` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    allocation_id   CHAR(36) NOT NULL REFERENCES `schedule`.`candidate_allocation`(id),
    ticket_number   VARCHAR(64) NOT NULL UNIQUE,
    payload_json    JSON NOT NULL,
    issued_at       DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'ISSUED'
                    CHECK (status IN ('ISSUED','REISSUED','CANCELLED'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `schedule`.`exam_credential` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    allocation_id   CHAR(36) NOT NULL REFERENCES `schedule`.`candidate_allocation`(id),
    login_id        VARCHAR(64) NOT NULL UNIQUE,
    password_hash   TEXT NOT NULL,
    delivery_channel VARCHAR(32),
    delivered_at    DATETIME(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'GENERATED'
                    CHECK (status IN ('GENERATED','DELIVERED','USED','REVOKED')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 07 — Notification Service
-- =============================================================================

CREATE TABLE `notify`.`notification_template` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    subject         VARCHAR(500),
    body_template   TEXT NOT NULL,
    version_no      INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `notify`.`notification_channel_config` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    channel         VARCHAR(16) NOT NULL UNIQUE CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    provider_name   VARCHAR(100) NOT NULL,
    config_json     JSON,
    credential_ref  VARCHAR(200),
    is_enabled      BOOLEAN NOT NULL DEFAULT TRUE,
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `notify`.`notification_event_route` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    event_code      VARCHAR(64) NOT NULL,
    template_id     CHAR(36) NOT NULL REFERENCES `notify`.`notification_template`(id),
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    is_enabled      BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (event_code, channel)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `notify`.`notification_job` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    event_code      VARCHAR(64) NOT NULL,
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    recipient       VARCHAR(255) NOT NULL,
    candidate_id    CHAR(36) REFERENCES `registration`.`candidate`(id),
    staff_user_id   CHAR(36) REFERENCES `iam`.`staff_user`(id),
    registration_id CHAR(36) REFERENCES `registration`.`registration`(id),
    payload_json    JSON,
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED'
                    CHECK (status IN ('QUEUED','PENDING','SENT','DELIVERED','FAILED','EXHAUSTED_FAILED','CANCELLED')),
    attempts        INTEGER NOT NULL DEFAULT 0,
    last_error      TEXT,
    parent_job_id   CHAR(36) REFERENCES `notify`.`notification_job`(id),
    resend_reason   TEXT,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    sent_at         DATETIME(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_notification_job_status` ON `notify`.`notification_job` (status, created_at);

CREATE TABLE `notify`.`notification_delivery_attempt` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    job_id          CHAR(36) NOT NULL REFERENCES `notify`.`notification_job`(id),
    attempt_no      INTEGER NOT NULL,
    provider_ref    VARCHAR(128),
    status          VARCHAR(32) NOT NULL,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    error_text      TEXT,
    UNIQUE (job_id, attempt_no)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `notify`.`in_app_notification` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    candidate_id    CHAR(36) NOT NULL REFERENCES `registration`.`candidate`(id),
    title           VARCHAR(200) NOT NULL,
    body            TEXT NOT NULL,
    is_read         BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_in_app_notification_candidate` ON `notify`.`in_app_notification` (candidate_id, created_at DESC);

-- =============================================================================
-- MODULE 08 / 09 — Centre Ops + Secure Conduct
-- =============================================================================

CREATE TABLE `conduct`.`exam_attempt` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id),
    exam_session_id CHAR(36) NOT NULL REFERENCES `schedule`.`exam_session`(id),
    exam_centre_id  CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    allocation_id   CHAR(36) NOT NULL REFERENCES `schedule`.`candidate_allocation`(id),
    -- Module 08
    attendance_status VARCHAR(32)
                    CHECK (attendance_status IS NULL OR attendance_status IN ('ABSENT','PRESENT','VERIFIED')),
    verification_status VARCHAR(32)
                    CHECK (verification_status IS NULL OR verification_status IN ('PENDING','VERIFIED','REJECTED')),
    verification_reject_reason TEXT,
    absent_reason   TEXT,
    identity_verified_at DATETIME(6),
    verified_by     CHAR(36) REFERENCES `iam`.`staff_user`(id),
    activation_status VARCHAR(32) NOT NULL DEFAULT 'NOT_ACTIVATED'
                    CHECK (activation_status IN ('NOT_ACTIVATED','ACTIVATED','REVOKED')),
    activated_by    CHAR(36) REFERENCES `iam`.`staff_user`(id),
    activated_at    DATETIME(6),
    -- Module 09
    login_at        DATETIME(6),
    started_at      DATETIME(6),
    submitted_at    DATETIME(6),
    submit_mode     VARCHAR(32)
                    CHECK (submit_mode IS NULL OR submit_mode IN ('CANDIDATE','AUTO_TIMER','FORCE','SECURITY')),
    client_ip       VARCHAR(64),
    device_fingerprint TEXT,
    network_check_result VARCHAR(32),
    timer_ends_at   DATETIME(6),
    last_heartbeat_at DATETIME(6),
    focus_violation_count INTEGER NOT NULL DEFAULT 0,
    visibility_violation_count INTEGER NOT NULL DEFAULT 0,
    security_flags_json JSON,
    status          VARCHAR(32) NOT NULL DEFAULT 'SCHEDULED'
                    CHECK (status IN (
                        'SCHEDULED','ACTIVATED','IN_PROGRESS','SUBMITTED',
                        'LOCKED','TERMINATED_SECURITY','ABSENT'
                    )),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    UNIQUE (registration_id, exam_session_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `conduct`.`attendance_event` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    exam_attempt_id CHAR(36) NOT NULL REFERENCES `conduct`.`exam_attempt`(id),
    event_type      VARCHAR(32) NOT NULL
                    CHECK (event_type IN (
                        'VERIFY','VERIFY_REJECT','MARK_PRESENT','MARK_ABSENT','CORRECTION'
                    )),
    from_status     VARCHAR(32),
    to_status       VARCHAR(32),
    reason_text     TEXT,
    actor_staff_id  CHAR(36) REFERENCES `iam`.`staff_user`(id),
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `ops_centre`.`centre_ops_snapshot` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    centre_id       CHAR(36) NOT NULL REFERENCES `centre`.`exam_centre`(id),
    session_id      CHAR(36) NOT NULL REFERENCES `schedule`.`exam_session`(id),
    as_of           DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    present_count   INTEGER NOT NULL DEFAULT 0,
    activated_count INTEGER NOT NULL DEFAULT 0,
    in_progress_count INTEGER NOT NULL DEFAULT 0,
    submitted_count INTEGER NOT NULL DEFAULT 0,
    UNIQUE (centre_id, session_id, as_of)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `conduct`.`paper_instance` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    exam_attempt_id CHAR(36) NOT NULL UNIQUE REFERENCES `conduct`.`exam_attempt`(id),
    version_label   VARCHAR(64) NOT NULL,
    seed_value      BIGINT,
    assembled_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','LOCKED'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `conduct`.`paper_instance_item` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    paper_instance_id CHAR(36) NOT NULL REFERENCES `conduct`.`paper_instance`(id) ON DELETE CASCADE,
    sequence_no     INTEGER NOT NULL,
    question_id     CHAR(36) NOT NULL REFERENCES `qbank`.`question`(id),
    option_order_json JSON,
    correct_option_map_json JSON,
    marks           NUMERIC(8,2),
    UNIQUE (paper_instance_id, sequence_no),
    UNIQUE (paper_instance_id, question_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `conduct`.`exam_response` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    exam_attempt_id CHAR(36) NOT NULL REFERENCES `conduct`.`exam_attempt`(id),
    paper_instance_item_id CHAR(36) NOT NULL REFERENCES `conduct`.`paper_instance_item`(id),
    selected_option_ids JSON,
    answered_at     DATETIME(6),
    is_marked_for_review BOOLEAN NOT NULL DEFAULT FALSE,
    is_locked       BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (exam_attempt_id, paper_instance_item_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `conduct`.`exam_activity_event` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    exam_attempt_id CHAR(36) NOT NULL REFERENCES `conduct`.`exam_attempt`(id),
    event_type      VARCHAR(64) NOT NULL,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    detail_json     JSON
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_exam_activity_attempt` ON `conduct`.`exam_activity_event` (exam_attempt_id, occurred_at);

CREATE TABLE `conduct`.`access_denial_log` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    registration_id CHAR(36) REFERENCES `registration`.`registration`(id),
    session_id      CHAR(36) REFERENCES `schedule`.`exam_session`(id),
    reason_code     VARCHAR(64) NOT NULL,
    client_ip       VARCHAR(64),
    detail_json     JSON,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 10 — Evaluation & Results
-- =============================================================================

CREATE TABLE `result`.`evaluation_run` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    exam_attempt_id CHAR(36) NOT NULL UNIQUE REFERENCES `conduct`.`exam_attempt`(id),
    correct_count   INTEGER NOT NULL DEFAULT 0,
    incorrect_count INTEGER NOT NULL DEFAULT 0,
    unanswered_count INTEGER NOT NULL DEFAULT 0,
    config_version_ref VARCHAR(64),
    config_snapshot_json JSON,
    engine_version  VARCHAR(32),
    evaluated_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `result`.`score_result` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    evaluation_run_id CHAR(36) NOT NULL UNIQUE REFERENCES `result`.`evaluation_run`(id),
    raw_score       NUMERIC(10,2) NOT NULL,
    negative_marks  NUMERIC(10,2) NOT NULL DEFAULT 0,
    total_score     NUMERIC(10,2) NOT NULL,
    percentage      NUMERIC(5,2),
    pass_fail       VARCHAR(8) NOT NULL CHECK (pass_fail IN ('PASS','FAIL'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `result`.`evaluation_rule_alignment` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    lifecycle_config_id CHAR(36) REFERENCES `qbank`.`examination_lifecycle_config`(id),
    validation_status VARCHAR(32) NOT NULL
                    CHECK (validation_status IN ('OK','BLOCKED','WARNING')),
    error_codes_json JSON,
    last_checked_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `result`.`result_publication` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    exam_session_id CHAR(36) REFERENCES `schedule`.`exam_session`(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'WITHHELD'
                    CHECK (status IN ('WITHHELD','PUBLISHED')),
    published_at    DATETIME(6),
    published_by    CHAR(36) REFERENCES `iam`.`staff_user`(id),
    display_rules_snapshot_json JSON,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `result`.`candidate_result` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    score_result_id CHAR(36) NOT NULL REFERENCES `result`.`score_result`(id),
    publication_id  CHAR(36) REFERENCES `result`.`result_publication`(id),
    visible_to_candidate BOOLEAN NOT NULL DEFAULT FALSE,
    display_snapshot_json JSON,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 11 — Certificate Management
-- =============================================================================

CREATE TABLE `certificate`.`certificate_number_sequence` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    examination_id  CHAR(36) NOT NULL UNIQUE REFERENCES `qbank`.`examination`(id),
    prefix          VARCHAR(32) NOT NULL,
    next_value      BIGINT NOT NULL DEFAULT 1,
    max_value       BIGINT,
    pad_width       INTEGER NOT NULL DEFAULT 6,
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL UNIQUE REFERENCES `registration`.`registration`(id),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    certificate_number VARCHAR(64) NOT NULL UNIQUE,
    issue_date      DATE NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ISSUED'
                    CHECK (status IN ('ISSUED','CANCELLED','REVOKED')),
    disclosure_snapshot_json JSON NOT NULL,
    document_uri    TEXT,
    issued_at       DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    cancelled_at    DATETIME(6),
    cancel_reason   TEXT,
    cancelled_by    CHAR(36) REFERENCES `iam`.`staff_user`(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_document` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    certificate_id  CHAR(36) NOT NULL UNIQUE REFERENCES `certificate`.`certificate`(id),
    pdf_uri         TEXT NOT NULL,
    qr_embedded     BOOLEAN NOT NULL DEFAULT TRUE,
    generated_at    DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    render_engine_version VARCHAR(32)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_verification_token` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    certificate_id  CHAR(36) NOT NULL UNIQUE REFERENCES `certificate`.`certificate`(id),
    token           VARCHAR(128) NOT NULL UNIQUE,
    public_disclosure_json JSON NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','CANCELLED')),
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_verification_hit` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    token           VARCHAR(128) NOT NULL,
    result_code     VARCHAR(32) NOT NULL
                    CHECK (result_code IN ('VALID','INVALID','CANCELLED')),
    queried_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    client_ip       VARCHAR(64)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_download_log` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    certificate_id  CHAR(36) NOT NULL REFERENCES `certificate`.`certificate`(id),
    candidate_id    CHAR(36) NOT NULL REFERENCES `registration`.`candidate`(id),
    downloaded_at   DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_issuance_log` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    registration_id CHAR(36) NOT NULL REFERENCES `registration`.`registration`(id),
    examination_id  CHAR(36) NOT NULL REFERENCES `qbank`.`examination`(id),
    batch_run_id    CHAR(36),
    outcome         VARCHAR(32) NOT NULL
                    CHECK (outcome IN ('ISSUED','ISSUANCE_SKIPPED','ISSUANCE_FAILED')),
    certificate_id  CHAR(36) REFERENCES `certificate`.`certificate`(id),
    error_text      TEXT,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `certificate`.`certificate_export_run` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    requested_by    CHAR(36) REFERENCES `iam`.`staff_user`(id),
    parameters_json JSON,
    output_uri      TEXT,
    row_count       INTEGER,
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED',
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    completed_at    DATETIME(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- MODULE 12 — MIS Reporting
-- =============================================================================

CREATE TABLE `mis`.`mis_report_definition` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    default_params_json JSON,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    updated_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `mis`.`mis_report_run` (
    id              CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    report_code     VARCHAR(64) NOT NULL REFERENCES `mis`.`mis_report_definition`(code),
    parameters_json JSON,
    requested_by    CHAR(36) REFERENCES `iam`.`staff_user`(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED'
                    CHECK (status IN ('QUEUED','RUNNING','COMPLETED','FAILED')),
    output_uri      TEXT,
    row_count       INTEGER,
    created_at      DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    completed_at    DATETIME(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =============================================================================
-- Cross-cutting audit
-- =============================================================================

CREATE TABLE `audit`.`audit_event` (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    occurred_at     DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    actor_type      VARCHAR(32) NOT NULL
                    CHECK (actor_type IN ('STAFF','CANDIDATE','SYSTEM','PUBLIC')),
    actor_id        CHAR(36),
    module_code     VARCHAR(8) NOT NULL,
    action_code     VARCHAR(64) NOT NULL,
    entity_type     VARCHAR(64),
    entity_id       VARCHAR(128),
    before_json     JSON,
    after_json      JSON,
    channel         VARCHAR(32),
    correlation_id  VARCHAR(100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE INDEX `ix_audit_event_module_time` ON `audit`.`audit_event` (module_code, occurred_at DESC);

-- Seed MIS report codes from pack



-- One ACTIVE primary post per person (session_policy resolution)
ALTER TABLE `iam`.`person_post`
    ADD COLUMN `active_primary_person` CHAR(36)
        GENERATED ALWAYS AS (
            CASE
                WHEN `status` = 'ACTIVE' AND `is_primary` = TRUE THEN `person_id`
                ELSE NULL
            END
        ) STORED,
    ADD UNIQUE KEY `uq_person_one_active_primary_post` (`active_primary_person`);

-- created_by / updated_by / assigned_by → iam.post (acting post)
ALTER TABLE `iam`.`platform_role`
    ADD CONSTRAINT `fk_platform_role_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`platform_role`
    ADD CONSTRAINT `fk_platform_role_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`person`
    ADD CONSTRAINT `fk_person_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`person`
    ADD CONSTRAINT `fk_person_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`post`
    ADD CONSTRAINT `fk_post_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`post`
    ADD CONSTRAINT `fk_post_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`person_post`
    ADD CONSTRAINT `fk_person_post_assigned_by_post`
    FOREIGN KEY (`assigned_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`post_manager`
    ADD CONSTRAINT `fk_post_manager_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`staff_user`
    ADD CONSTRAINT `fk_staff_user_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `iam`.`staff_user`
    ADD CONSTRAINT `fk_staff_user_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `integration`.`integration_credential`
    ADD CONSTRAINT `fk_integration_credential_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `centre`.`exam_centre`
    ADD CONSTRAINT `fk_exam_centre_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `centre`.`exam_centre`
    ADD CONSTRAINT `fk_exam_centre_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `centre`.`exam_centre_capacity`
    ADD CONSTRAINT `fk_exam_centre_capacity_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `centre`.`exam_centre_infrastructure`
    ADD CONSTRAINT `fk_exam_centre_infrastructure_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `centre`.`centre_exam_eligibility`
    ADD CONSTRAINT `fk_centre_exam_eligibility_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `qbank`.`question`
    ADD CONSTRAINT `fk_question_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `qbank`.`question`
    ADD CONSTRAINT `fk_question_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `qbank`.`examination`
    ADD CONSTRAINT `fk_examination_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `qbank`.`examination`
    ADD CONSTRAINT `fk_examination_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `schedule`.`exam_session`
    ADD CONSTRAINT `fk_exam_session_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `schedule`.`exam_session`
    ADD CONSTRAINT `fk_exam_session_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);

-- Module 02: at most one ACTIVE endpoint per integration_type (KGID / PAYMENT)
ALTER TABLE `integration`.`integration_endpoint`
    ADD COLUMN `active_integration_type` VARCHAR(32)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `integration_type` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_integration_one_active_per_type` (`active_integration_type`);

ALTER TABLE `integration`.`integration_endpoint`
    ADD CONSTRAINT `fk_integration_endpoint_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);
ALTER TABLE `integration`.`integration_endpoint`
    ADD CONSTRAINT `fk_integration_endpoint_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);


-- Module 03: one ACTIVE (current) capacity version per centre
ALTER TABLE `centre`.`exam_centre_capacity`
    ADD COLUMN `active_capacity_centre` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' AND `effective_to` IS NULL THEN `centre_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_exam_centre_one_active_capacity` (`active_capacity_centre`);

ALTER TABLE `centre`.`exam_centre_capacity`
    ADD CONSTRAINT `fk_exam_centre_capacity_created_by_post`
    FOREIGN KEY (`created_by`) REFERENCES `iam`.`post`(`id`);

ALTER TABLE `centre`.`centre_exam_eligibility`
    ADD CONSTRAINT `fk_centre_exam_eligibility_updated_by_post`
    FOREIGN KEY (`updated_by`) REFERENCES `iam`.`post`(`id`);


-- Module 04: one ACTIVE config of each kind per examination
ALTER TABLE `qbank`.`examination_selection_rule`
    ADD COLUMN `active_exam_key` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `examination_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_one_active_selection_rule` (`active_exam_key`);

ALTER TABLE `qbank`.`examination_randomisation_setting`
    ADD COLUMN `active_exam_key` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `examination_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_one_active_randomisation` (`active_exam_key`);

ALTER TABLE `qbank`.`examination_lifecycle_config`
    ADD COLUMN `active_exam_key` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `examination_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_one_active_lifecycle` (`active_exam_key`);

-- One ACTIVE global default (examination_id NULL) and one ACTIVE override per exam
ALTER TABLE `qbank`.`conduct_security_policy`
    ADD COLUMN `active_policy_scope` VARCHAR(64)
        GENERATED ALWAYS AS (
            CASE
                WHEN `status` = 'ACTIVE' AND `examination_id` IS NULL THEN 'GLOBAL'
                WHEN `status` = 'ACTIVE' THEN `examination_id`
                ELSE NULL
            END
        ) STORED,
    ADD UNIQUE KEY `uq_one_active_security_policy_scope` (`active_policy_scope`);

ALTER TABLE `qbank`.`question_import_batch`
    ADD CONSTRAINT `fk_question_import_batch_imported_by_post`
    FOREIGN KEY (`imported_by`) REFERENCES `iam`.`post`(`id`);


-- Module 05 identity uniqueness (on candidate)
ALTER TABLE `registration`.`candidate`
    ADD COLUMN `kgid_unique_key` VARCHAR(64)
        GENERATED ALWAYS AS (
            CASE WHEN `kgid_number` IS NOT NULL AND `kgid_number` <> '' THEN `kgid_number` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_candidate_kgid` (`kgid_unique_key`);

ALTER TABLE `registration`.`candidate`
    ADD COLUMN `other_org_identity_key` VARCHAR(200)
        GENERATED ALWAYS AS (
            CASE
                WHEN `employee_id` IS NOT NULL AND `employee_id` <> ''
                 AND `aadhaar_hash` IS NOT NULL AND `aadhaar_hash` <> ''
                THEN CONCAT(`employee_id`, ':', `aadhaar_hash`)
                ELSE NULL
            END
        ) STORED,
    ADD UNIQUE KEY `uq_candidate_employee_aadhaar` (`other_org_identity_key`);

-- At most one CONFIRMED registration per candidate + examination
ALTER TABLE `registration`.`registration`
    ADD COLUMN `confirmed_candidate_exam` VARCHAR(80)
        GENERATED ALWAYS AS (
            CASE
                WHEN `status` = 'CONFIRMED' THEN CONCAT(`candidate_id`, ':', `examination_id`)
                ELSE NULL
            END
        ) STORED,
    ADD UNIQUE KEY `uq_one_confirmed_registration_per_exam` (`confirmed_candidate_exam`);

ALTER TABLE `registration`.`registration_admin_review`
    ADD CONSTRAINT `fk_registration_admin_review_reviewed_by_post`
    FOREIGN KEY (`reviewed_by`) REFERENCES `iam`.`post`(`id`);


ALTER TABLE `schedule`.`candidate_allocation`
    ADD CONSTRAINT `fk_candidate_allocation_allocated_by_post`
    FOREIGN KEY (`allocated_by`) REFERENCES `iam`.`post`(`id`);

-- Unique employee_id among ACTIVE persons (when set)
ALTER TABLE `iam`.`person`
    ADD COLUMN `employee_id_active` VARCHAR(64)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `employee_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_person_employee_id_active` (`employee_id_active`);

-- One ACTIVE occupant per post (one post -> one person)
ALTER TABLE `iam`.`person_post`
    ADD COLUMN `active_post_occupant` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `post_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_person_post_one_active_occupant` (`active_post_occupant`);

-- One ACTIVE manager mapping per post (post -> manager post)
ALTER TABLE `iam`.`post_manager`
    ADD COLUMN `active_managed_post` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'ACTIVE' THEN `post_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_post_one_active_manager` (`active_managed_post`);


-- Partial unique: one ACTIVE fee rule per exam/category/attempt (F04-007)
ALTER TABLE `qbank`.`examination_fee_rule`
    ADD COLUMN `active_fee_key` VARCHAR(200)
        GENERATED ALWAYS AS (
            CASE
                WHEN `status` = 'ACTIVE' THEN CONCAT(`examination_id`, ':', `candidate_category`, ':', `attempt_type`)
                ELSE NULL
            END
        ) STORED,
    ADD UNIQUE KEY `uq_exam_fee_rule_active` (`active_fee_key`);


-- Partial unique: one IN_PROGRESS attempt per registration (F09)
ALTER TABLE `conduct`.`exam_attempt`
    ADD COLUMN `registration_in_progress` CHAR(36)
        GENERATED ALWAYS AS (
            CASE WHEN `status` = 'IN_PROGRESS' THEN `registration_id` ELSE NULL END
        ) STORED,
    ADD UNIQUE KEY `uq_exam_attempt_one_in_progress` (`registration_in_progress`);



INSERT INTO `mis`.`mis_report_definition` (code, name, status) VALUES
    ('CENTRE_WISE', 'Centre-wise MIS Report Suite', 'ACTIVE'),
    ('CATEGORY_DEPT_WISE', 'Category-wise and Department-wise MIS Report Suite', 'ACTIVE'),
    ('CERTIFICATE', 'Certificate MIS Report Suite', 'ACTIVE');

-- =============================================================================
-- End of CREATE dump
-- Table count (approx): 85+ including gap-fill satellites
-- =============================================================================

SET FOREIGN_KEY_CHECKS = 1;
