-- =============================================================================
-- KEONICS Examination Module (EXAM) — PostgreSQL CREATE dump
-- Basis : EXAM_Feature_Specification (12 modules / 87 features)
-- Companion: EXAM_Database_Design.md v2.1 + EXAM_Database_Gap_Analysis.md (gaps filled)
-- Date  : 2026-09-10
-- Dialect: PostgreSQL 14+
-- =============================================================================

BEGIN;

CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- -----------------------------------------------------------------------------
-- Schemas
-- -----------------------------------------------------------------------------
CREATE SCHEMA IF NOT EXISTS iam;
CREATE SCHEMA IF NOT EXISTS integration;
CREATE SCHEMA IF NOT EXISTS centre;
CREATE SCHEMA IF NOT EXISTS qbank;
CREATE SCHEMA IF NOT EXISTS registration;
CREATE SCHEMA IF NOT EXISTS schedule;
CREATE SCHEMA IF NOT EXISTS notify;
CREATE SCHEMA IF NOT EXISTS ops_centre;
CREATE SCHEMA IF NOT EXISTS conduct;
CREATE SCHEMA IF NOT EXISTS result;
CREATE SCHEMA IF NOT EXISTS certificate;
CREATE SCHEMA IF NOT EXISTS mis;
CREATE SCHEMA IF NOT EXISTS audit;

-- =============================================================================
-- MODULE 01 — User & Role Management
-- =============================================================================

CREATE TABLE iam.platform_role (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64)  NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    actor_category  VARCHAR(32)  NOT NULL
                    CHECK (actor_category IN ('CANDIDATE','STAFF_ADMIN','STAFF_CENTRE','PUBLIC')),
    status          VARCHAR(32)  NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_by      UUID
);

CREATE TABLE iam.permission (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(128) NOT NULL UNIQUE,
    journey_stage   VARCHAR(64),
    module_area     VARCHAR(32),
    is_baseline     BOOLEAN      NOT NULL DEFAULT FALSE,
    description     TEXT,
    created_at      TIMESTAMPTZ  NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE iam.role_permission (
    role_id         UUID NOT NULL REFERENCES iam.platform_role(id),
    permission_id   UUID NOT NULL REFERENCES iam.permission(id),
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    effective_to    TIMESTAMPTZ,
    PRIMARY KEY (role_id, permission_id, effective_from)
);

CREATE TABLE iam.permission_snapshot (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    role_id         UUID NOT NULL REFERENCES iam.platform_role(id),
    version_no      INTEGER NOT NULL,
    effective_from  TIMESTAMPTZ NOT NULL,
    grants_json     JSONB NOT NULL,
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('PUBLISHED','SUPERSEDED')),
    published_by    UUID,
    published_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (role_id, version_no)
);

CREATE TABLE iam.staff_user (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username        VARCHAR(100) NOT NULL UNIQUE,
    employee_id     VARCHAR(64),
    display_name    VARCHAR(200) NOT NULL,
    official_email  VARCHAR(200),
    mobile          VARCHAR(15),
    password_hash   TEXT NOT NULL,
    user_kind       VARCHAR(32) NOT NULL
                    CHECK (user_kind IN ('ADMINISTRATOR','CENTRE_INVIGILATOR')),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    org_scope       BOOLEAN NOT NULL DEFAULT FALSE,
    must_reset_password BOOLEAN NOT NULL DEFAULT FALSE,
    password_changed_at TIMESTAMPTZ,
    failed_login_count INTEGER NOT NULL DEFAULT 0,
    locked_until    TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

CREATE UNIQUE INDEX uq_staff_admin_employee_active
    ON iam.staff_user (employee_id)
    WHERE employee_id IS NOT NULL
      AND user_kind = 'ADMINISTRATOR'
      AND status = 'ACTIVE';

CREATE TABLE iam.staff_user_role (
    staff_user_id   UUID NOT NULL REFERENCES iam.staff_user(id),
    role_id         UUID NOT NULL REFERENCES iam.platform_role(id),
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    effective_to    TIMESTAMPTZ,
    PRIMARY KEY (staff_user_id, role_id, effective_from)
);

-- exam_centre created later; staff_user_centre FK added after centre.exam_centre
CREATE TABLE iam.staff_user_centre (
    staff_user_id   UUID NOT NULL REFERENCES iam.staff_user(id),
    exam_centre_id  UUID NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    bound_at        TIMESTAMPTZ NOT NULL DEFAULT now(),
    bound_by        UUID,
    PRIMARY KEY (staff_user_id, exam_centre_id)
);

CREATE TABLE iam.staff_session (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    staff_user_id   UUID NOT NULL REFERENCES iam.staff_user(id),
    token_hash      TEXT NOT NULL UNIQUE,
    issued_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at      TIMESTAMPTZ NOT NULL,
    last_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    revoked_at      TIMESTAMPTZ,
    client_meta_json JSONB
);

CREATE TABLE iam.session_policy (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    role_type       VARCHAR(32) NOT NULL
                    CHECK (role_type IN ('ADMINISTRATOR','CENTRE_INVIGILATOR','DEFAULT')),
    idle_timeout_minutes      INTEGER NOT NULL,
    absolute_lifetime_minutes INTEGER NOT NULL,
    concurrent_session_limit  INTEGER NOT NULL DEFAULT 1,
    version_no      INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    CHECK (idle_timeout_minutes > 0
       AND absolute_lifetime_minutes > idle_timeout_minutes
       AND concurrent_session_limit >= 1)
);

CREATE TABLE iam.credential_policy (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
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
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE iam.staff_password_history (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    staff_user_id   UUID NOT NULL REFERENCES iam.staff_user(id),
    password_hash   TEXT NOT NULL,
    set_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_staff_password_history_user
    ON iam.staff_password_history (staff_user_id, set_at DESC);

CREATE TABLE iam.staff_password_reset (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    staff_user_id   UUID NOT NULL REFERENCES iam.staff_user(id),
    token_hash      TEXT NOT NULL UNIQUE,
    expires_at      TIMESTAMPTZ NOT NULL,
    consumed_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE iam.iam_security_event (
    id              BIGSERIAL PRIMARY KEY,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    event_type      VARCHAR(64) NOT NULL,
    staff_user_id   UUID,
    actor_username  VARCHAR(100),
    resource_type   VARCHAR(64),
    resource_id     VARCHAR(128),
    reason_code     VARCHAR(64),
    success         BOOLEAN NOT NULL,
    client_ip       VARCHAR(64),
    detail_json     JSONB
);

CREATE TABLE iam.authorization_hook_registration (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    module_code     VARCHAR(8) NOT NULL,
    permission_codes_json JSONB NOT NULL,
    consumer_name   VARCHAR(200) NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE iam.rate_limit_bucket (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    bucket_key      VARCHAR(200) NOT NULL,
    window_start    TIMESTAMPTZ NOT NULL,
    hit_count       INTEGER NOT NULL DEFAULT 0,
    UNIQUE (bucket_key, window_start)
);

-- =============================================================================
-- MODULE 03 — Examination Centre (before staff_user_centre FK complete)
-- =============================================================================

CREATE TABLE centre.exam_centre (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
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
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

ALTER TABLE iam.staff_user_centre
    ADD CONSTRAINT fk_staff_user_centre_centre
    FOREIGN KEY (exam_centre_id) REFERENCES centre.exam_centre(id);

CREATE TABLE centre.exam_centre_capacity (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL UNIQUE REFERENCES centre.exam_centre(id),
    approved_capacity INTEGER NOT NULL CHECK (approved_capacity > 0),
    per_session_seat_capacity INTEGER CHECK (per_session_seat_capacity IS NULL OR per_session_seat_capacity > 0),
    effective_from  DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID,
    CHECK (per_session_seat_capacity IS NULL
        OR per_session_seat_capacity <= approved_capacity)
);

CREATE TABLE centre.exam_centre_infrastructure (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL UNIQUE REFERENCES centre.exam_centre(id),
    computer_terminal_count INTEGER,
    lab_count       INTEGER,
    power_backup    BOOLEAN,
    network_notes   TEXT,
    details_json    JSONB,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

-- examination FK added after qbank.examination
CREATE TABLE centre.centre_session_eligibility (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_centre_id  UUID NOT NULL REFERENCES centre.exam_centre(id),
    examination_id  UUID,
    allows_all_exams BOOLEAN NOT NULL DEFAULT FALSE,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    effective_from  DATE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID
);

CREATE TABLE centre.centre_network_restriction (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL REFERENCES centre.exam_centre(id),
    label           VARCHAR(100),
    cidr            VARCHAR(64) NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE centre.centre_device (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL REFERENCES centre.exam_centre(id),
    device_identifier VARCHAR(200) NOT NULL,
    device_label    VARCHAR(200),
    os_fingerprint  VARCHAR(200),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (centre_id, device_identifier)
);

-- retained for legacy whitelist JSON if needed alongside centre_device
CREATE TABLE centre.centre_device_restriction (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL UNIQUE REFERENCES centre.exam_centre(id),
    allowed_device_json JSONB,
    whitelist_mode  BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE centre.centre_allocation_summary_cache (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL REFERENCES centre.exam_centre(id),
    as_of           TIMESTAMPTZ NOT NULL DEFAULT now(),
    allocated_count INTEGER NOT NULL DEFAULT 0,
    capacity        INTEGER NOT NULL DEFAULT 0,
    utilisation_pct NUMERIC(5,2),
    UNIQUE (centre_id, as_of)
);

-- =============================================================================
-- MODULE 04 — Question Bank & Examination Configuration
-- =============================================================================

CREATE TABLE qbank.question_category (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    parent_id       UUID REFERENCES qbank.question_category(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE qbank.question (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id     UUID NOT NULL REFERENCES qbank.question_category(id),
    question_type   VARCHAR(32) NOT NULL
                    CHECK (question_type IN ('SINGLE_CHOICE','MULTI_CHOICE','TRUE_FALSE')),
    stem_text       TEXT NOT NULL,
    difficulty      VARCHAR(16)
                    CHECK (difficulty IS NULL OR difficulty IN ('EASY','MEDIUM','HARD')),
    marks           NUMERIC(8,2) NOT NULL CHECK (marks > 0),
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

CREATE TABLE qbank.question_option (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    question_id     UUID NOT NULL REFERENCES qbank.question(id) ON DELETE CASCADE,
    option_key      VARCHAR(8) NOT NULL,
    option_text     TEXT NOT NULL,
    is_correct      BOOLEAN NOT NULL DEFAULT FALSE,
    display_order   INTEGER NOT NULL DEFAULT 0,
    UNIQUE (question_id, option_key)
);

CREATE TABLE qbank.question_import_batch (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    file_name       VARCHAR(255) NOT NULL,
    imported_by     UUID,
    row_count       INTEGER NOT NULL DEFAULT 0,
    success_count   INTEGER NOT NULL DEFAULT 0,
    fail_count      INTEGER NOT NULL DEFAULT 0,
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('PROCESSING','COMMITTED','FAILED')),
    error_log_json  JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ
);

CREATE TABLE qbank.examination (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    description     TEXT,
    registration_open_at  TIMESTAMPTZ,
    registration_close_at TIMESTAMPTZ,
    requires_admin_verification BOOLEAN NOT NULL DEFAULT FALSE,
    auto_evaluation_enabled BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','OPEN','CLOSED','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

ALTER TABLE centre.centre_session_eligibility
    ADD CONSTRAINT fk_centre_session_eligibility_exam
    FOREIGN KEY (examination_id) REFERENCES qbank.examination(id);

CREATE TABLE qbank.examination_selection_rule (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    total_question_count INTEGER,
    rules_json      JSONB NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE qbank.examination_randomisation_setting (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    paper_version_count INTEGER NOT NULL DEFAULT 1 CHECK (paper_version_count > 0),
    randomise_questions BOOLEAN NOT NULL DEFAULT TRUE,
    randomise_options   BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE qbank.examination_lifecycle_config (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    question_count  INTEGER,
    total_marks     NUMERIC(10,2) NOT NULL,
    pass_marks      NUMERIC(10,2),
    pass_percentage NUMERIC(5,2),
    negative_marking_enabled BOOLEAN NOT NULL DEFAULT FALSE,
    negative_mark_value NUMERIC(8,2),
    unanswered_handling VARCHAR(32),
    multi_select_partial_rule VARCHAR(32),
    result_display_rules_json JSONB,
    certificate_eligibility_rules_json JSONB,
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE qbank.examination_fee_rule (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    candidate_category VARCHAR(32) NOT NULL
                    CHECK (candidate_category IN ('GOVERNMENT','OTHER_ORG')),
    attempt_type    VARCHAR(32) NOT NULL
                    CHECK (attempt_type IN ('FIRST','SUBSEQUENT')),
    fee_amount      DECIMAL(12,2) NOT NULL CHECK (fee_amount >= 0),
    currency_code   CHAR(3) NOT NULL DEFAULT 'INR',
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE UNIQUE INDEX uq_exam_fee_rule_active
    ON qbank.examination_fee_rule (examination_id, candidate_category, attempt_type)
    WHERE status = 'ACTIVE';

CREATE TABLE qbank.conduct_security_policy (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID REFERENCES qbank.examination(id),
    allow_session_takeover BOOLEAN NOT NULL DEFAULT FALSE,
    max_focus_violations INTEGER NOT NULL DEFAULT 5,
    max_visibility_violations INTEGER NOT NULL DEFAULT 5,
    critical_immediate_terminate BOOLEAN NOT NULL DEFAULT TRUE,
    approved_browser_json JSONB,
    bind_device_fingerprint BOOLEAN NOT NULL DEFAULT TRUE,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- =============================================================================
-- MODULE 02 — API Integration Hub
-- =============================================================================

CREATE TABLE integration.integration_endpoint (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    base_url        TEXT NOT NULL,
    auth_type       VARCHAR(32) NOT NULL
                    CHECK (auth_type IN ('API_KEY','OAUTH2','BASIC','NONE')),
    credential_ref  VARCHAR(200),
    timeout_ms      INTEGER NOT NULL DEFAULT 30000,
    retry_limit     INTEGER NOT NULL DEFAULT 3,
    is_primary      BOOLEAN NOT NULL DEFAULT FALSE,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE integration.integration_credential (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    endpoint_id     UUID NOT NULL REFERENCES integration.integration_endpoint(id),
    secret_ciphertext TEXT NOT NULL,
    rotated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','ROTATED')),
    created_by      UUID,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE integration.integration_call_log (
    id              BIGSERIAL PRIMARY KEY,
    endpoint_id     UUID NOT NULL REFERENCES integration.integration_endpoint(id),
    correlation_id  VARCHAR(100) NOT NULL,
    direction       VARCHAR(16) NOT NULL CHECK (direction IN ('OUTBOUND','INBOUND')),
    http_status     INTEGER,
    success         BOOLEAN NOT NULL,
    attempt_no      INTEGER NOT NULL DEFAULT 1,
    request_meta_json  JSONB,
    response_meta_json JSONB,
    error_code      VARCHAR(64),
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_integration_call_log_corr
    ON integration.integration_call_log (correlation_id);

CREATE TABLE integration.kgid_lookup_cache (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    kgid_number     VARCHAR(64) NOT NULL,
    payload_json    JSONB NOT NULL,
    fetched_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at      TIMESTAMPTZ NOT NULL
);

CREATE INDEX ix_kgid_lookup_cache_number
    ON integration.kgid_lookup_cache (kgid_number, fetched_at DESC);

-- =============================================================================
-- MODULE 05 — Candidate Registration
-- =============================================================================

CREATE TABLE registration.candidate (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mobile          VARCHAR(15) NOT NULL UNIQUE,
    display_name    VARCHAR(200),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','BLOCKED')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE registration.otp_security_parameter (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    otp_length      INTEGER NOT NULL DEFAULT 6,
    otp_ttl_seconds INTEGER NOT NULL DEFAULT 300,
    max_verify_attempts INTEGER NOT NULL DEFAULT 5,
    max_resends     INTEGER NOT NULL DEFAULT 3,
    resend_interval_seconds INTEGER NOT NULL DEFAULT 60,
    idle_timeout_minutes INTEGER NOT NULL DEFAULT 30,
    concurrent_session_limit INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    version_no      INTEGER NOT NULL DEFAULT 1,
    effective_from  TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE registration.otp_challenge (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mobile          VARCHAR(15) NOT NULL,
    candidate_id    UUID REFERENCES registration.candidate(id),
    otp_hash        TEXT NOT NULL,
    expires_at      TIMESTAMPTZ NOT NULL,
    verify_attempts INTEGER NOT NULL DEFAULT 0,
    resend_count    INTEGER NOT NULL DEFAULT 0,
    locked_until    TIMESTAMPTZ,
    consumed_at     TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_otp_challenge_mobile
    ON registration.otp_challenge (mobile, created_at DESC);

CREATE TABLE registration.candidate_portal_session (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    candidate_id    UUID NOT NULL REFERENCES registration.candidate(id),
    token_hash      TEXT NOT NULL UNIQUE,
    issued_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    expires_at      TIMESTAMPTZ NOT NULL,
    last_seen_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    revoked_at      TIMESTAMPTZ,
    client_meta_json JSONB
);

CREATE TABLE registration.document_template (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    file_uri        TEXT NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE registration.registration (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_number VARCHAR(64) UNIQUE,
    candidate_id    UUID NOT NULL REFERENCES registration.candidate(id),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    category_type   VARCHAR(32) NOT NULL
                    CHECK (category_type IN ('GOVERNMENT','OTHER_ORG')),
    organisation_sub_category VARCHAR(32)
                    CHECK (organisation_sub_category IS NULL OR organisation_sub_category IN
                          ('PSU','BOARD','CORPORATION','SOCIETY','OTHER')),
    kgid_number     VARCHAR(64),
    kgid_snapshot_json JSONB,
    supplementary_json JSONB,
    employee_id     VARCHAR(64),
    organisation_name VARCHAR(200),
    designation     VARCHAR(200),
    date_of_joining DATE,
    photograph_uri  TEXT,
    attempt_no      INTEGER NOT NULL DEFAULT 1 CHECK (attempt_no >= 1),
    fee_applicable  BOOLEAN NOT NULL DEFAULT FALSE,
    fee_amount      DECIMAL(12,2),
    currency_code   CHAR(3) DEFAULT 'INR',
    fee_basis_snapshot_json JSONB,
    status          VARCHAR(32) NOT NULL DEFAULT 'DRAFT'
                    CHECK (status IN (
                        'DRAFT','AWAITING_PAYMENT','PAYMENT_FAILED',
                        'PENDING_ADMIN_VERIFICATION','CONFIRMED','REJECTED','CANCELLED'
                    )),
    confirmed_at    TIMESTAMPTZ,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_registration_candidate_exam
    ON registration.registration (candidate_id, examination_id);

CREATE TABLE registration.registration_centre_preference (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id) ON DELETE CASCADE,
    preference_rank SMALLINT NOT NULL CHECK (preference_rank IN (1, 2)),
    exam_centre_id  UUID NOT NULL REFERENCES centre.exam_centre(id),
    UNIQUE (registration_id, preference_rank),
    UNIQUE (registration_id, exam_centre_id)
);

CREATE TABLE registration.competent_authority_document (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id) ON DELETE CASCADE,
    template_code   VARCHAR(64) REFERENCES registration.document_template(code),
    file_name       VARCHAR(255) NOT NULL,
    storage_uri     TEXT NOT NULL,
    content_type    VARCHAR(100),
    uploaded_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE registration.payment_transaction (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id),
    amount          DECIMAL(12,2) NOT NULL,
    currency_code   CHAR(3) NOT NULL DEFAULT 'INR',
    gateway_ref     VARCHAR(128),
    status          VARCHAR(32) NOT NULL
                    CHECK (status IN ('INITIATED','SUCCESS','FAILED','REFUNDED','ABANDONED')),
    initiated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ,
    failure_reason  TEXT,
    receipt_number  VARCHAR(64),
    callback_json   JSONB,
    correlation_id  VARCHAR(100)
);

CREATE INDEX ix_payment_registration
    ON registration.payment_transaction (registration_id, initiated_at DESC);

CREATE TABLE registration.registration_admin_review (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    decision        VARCHAR(32) NOT NULL CHECK (decision IN ('APPROVED','REJECTED')),
    remarks         TEXT,
    reviewed_by     UUID REFERENCES iam.staff_user(id),
    decided_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE registration.candidate_exam_attempt_counter (
    candidate_id    UUID NOT NULL REFERENCES registration.candidate(id),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    attempt_count   INTEGER NOT NULL DEFAULT 0 CHECK (attempt_count >= 0),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    PRIMARY KEY (candidate_id, examination_id)
);

CREATE TABLE registration.fee_determination_audit (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id),
    candidate_id    UUID NOT NULL,
    examination_id  UUID NOT NULL,
    category_type   VARCHAR(32) NOT NULL,
    attempt_no      INTEGER NOT NULL,
    fee_applicable  BOOLEAN NOT NULL,
    fee_amount      DECIMAL(12,2),
    rule_id         UUID,
    decided_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    detail_json     JSONB
);

-- =============================================================================
-- MODULE 06 — Scheduling & Allocation
-- =============================================================================

CREATE TABLE schedule.exam_session (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    exam_centre_id  UUID NOT NULL REFERENCES centre.exam_centre(id),
    session_date    DATE NOT NULL,
    start_time      TIME NOT NULL,
    end_time        TIME NOT NULL,
    reporting_time  TIME,
    duration_minutes INTEGER NOT NULL,
    seat_capacity   INTEGER NOT NULL CHECK (seat_capacity > 0),
    config_snapshot_json JSONB,
    status          VARCHAR(32) NOT NULL DEFAULT 'SCHEDULED'
                    CHECK (status IN ('DRAFT','SCHEDULED','IN_PROGRESS','COMPLETED','CANCELLED')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    created_by      UUID,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_by      UUID
);

CREATE INDEX ix_exam_session_centre_date
    ON schedule.exam_session (exam_centre_id, session_date);

-- F03-012: allow centre eligibility to bind a concrete session once scheduled
ALTER TABLE centre.centre_session_eligibility
    ADD COLUMN exam_session_id UUID REFERENCES schedule.exam_session(id);

CREATE UNIQUE INDEX uq_centre_session_pair
    ON centre.centre_session_eligibility (exam_centre_id, exam_session_id)
    WHERE exam_session_id IS NOT NULL;

CREATE TABLE schedule.candidate_allocation (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    exam_session_id UUID NOT NULL REFERENCES schedule.exam_session(id),
    exam_centre_id  UUID NOT NULL REFERENCES centre.exam_centre(id),
    allocation_source VARCHAR(32) NOT NULL
                    CHECK (allocation_source IN ('AUTO','MANUAL','OVERRIDE')),
    override_reason TEXT,
    allocated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    allocated_by    UUID
);

CREATE TABLE schedule.seat_assignment (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    allocation_id   UUID NOT NULL UNIQUE REFERENCES schedule.candidate_allocation(id),
    seat_label      VARCHAR(64) NOT NULL,
    computer_label  VARCHAR(64),
    locked_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE schedule.hall_ticket (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    allocation_id   UUID NOT NULL REFERENCES schedule.candidate_allocation(id),
    ticket_number   VARCHAR(64) NOT NULL UNIQUE,
    payload_json    JSONB NOT NULL,
    issued_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    status          VARCHAR(32) NOT NULL DEFAULT 'ISSUED'
                    CHECK (status IN ('ISSUED','REISSUED','CANCELLED'))
);

CREATE TABLE schedule.exam_credential (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    allocation_id   UUID NOT NULL REFERENCES schedule.candidate_allocation(id),
    login_id        VARCHAR(64) NOT NULL UNIQUE,
    password_hash   TEXT NOT NULL,
    delivery_channel VARCHAR(32),
    delivered_at    TIMESTAMPTZ,
    status          VARCHAR(32) NOT NULL DEFAULT 'GENERATED'
                    CHECK (status IN ('GENERATED','DELIVERED','USED','REVOKED')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- =============================================================================
-- MODULE 07 — Notification Service
-- =============================================================================

CREATE TABLE notify.notification_template (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    subject         VARCHAR(500),
    body_template   TEXT NOT NULL,
    version_no      INTEGER NOT NULL DEFAULT 1,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('DRAFT','ACTIVE','INACTIVE')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE notify.notification_channel_config (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    channel         VARCHAR(16) NOT NULL UNIQUE CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    provider_name   VARCHAR(100) NOT NULL,
    config_json     JSONB,
    credential_ref  VARCHAR(200),
    is_enabled      BOOLEAN NOT NULL DEFAULT TRUE,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE notify.notification_event_route (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_code      VARCHAR(64) NOT NULL,
    template_id     UUID NOT NULL REFERENCES notify.notification_template(id),
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    is_enabled      BOOLEAN NOT NULL DEFAULT TRUE,
    UNIQUE (event_code, channel)
);

CREATE TABLE notify.notification_job (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_code      VARCHAR(64) NOT NULL,
    channel         VARCHAR(16) NOT NULL CHECK (channel IN ('SMS','EMAIL','IN_APP')),
    recipient       VARCHAR(255) NOT NULL,
    candidate_id    UUID REFERENCES registration.candidate(id),
    staff_user_id   UUID REFERENCES iam.staff_user(id),
    registration_id UUID REFERENCES registration.registration(id),
    payload_json    JSONB,
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED'
                    CHECK (status IN ('QUEUED','PENDING','SENT','DELIVERED','FAILED','EXHAUSTED_FAILED','CANCELLED')),
    attempts        INTEGER NOT NULL DEFAULT 0,
    last_error      TEXT,
    parent_job_id   UUID REFERENCES notify.notification_job(id),
    resend_reason   TEXT,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    sent_at         TIMESTAMPTZ
);

CREATE INDEX ix_notification_job_status
    ON notify.notification_job (status, created_at);

CREATE TABLE notify.notification_delivery_attempt (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    job_id          UUID NOT NULL REFERENCES notify.notification_job(id),
    attempt_no      INTEGER NOT NULL,
    provider_ref    VARCHAR(128),
    status          VARCHAR(32) NOT NULL,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    error_text      TEXT,
    UNIQUE (job_id, attempt_no)
);

CREATE TABLE notify.in_app_notification (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    candidate_id    UUID NOT NULL REFERENCES registration.candidate(id),
    title           VARCHAR(200) NOT NULL,
    body            TEXT NOT NULL,
    is_read         BOOLEAN NOT NULL DEFAULT FALSE,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX ix_in_app_notification_candidate
    ON notify.in_app_notification (candidate_id, created_at DESC);

-- =============================================================================
-- MODULE 08 / 09 — Centre Ops + Secure Conduct
-- =============================================================================

CREATE TABLE conduct.exam_attempt (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id),
    exam_session_id UUID NOT NULL REFERENCES schedule.exam_session(id),
    exam_centre_id  UUID NOT NULL REFERENCES centre.exam_centre(id),
    allocation_id   UUID NOT NULL REFERENCES schedule.candidate_allocation(id),
    -- Module 08
    attendance_status VARCHAR(32)
                    CHECK (attendance_status IS NULL OR attendance_status IN ('ABSENT','PRESENT','VERIFIED')),
    verification_status VARCHAR(32)
                    CHECK (verification_status IS NULL OR verification_status IN ('PENDING','VERIFIED','REJECTED')),
    verification_reject_reason TEXT,
    absent_reason   TEXT,
    identity_verified_at TIMESTAMPTZ,
    verified_by     UUID REFERENCES iam.staff_user(id),
    activation_status VARCHAR(32) NOT NULL DEFAULT 'NOT_ACTIVATED'
                    CHECK (activation_status IN ('NOT_ACTIVATED','ACTIVATED','REVOKED')),
    activated_by    UUID REFERENCES iam.staff_user(id),
    activated_at    TIMESTAMPTZ,
    -- Module 09
    login_at        TIMESTAMPTZ,
    started_at      TIMESTAMPTZ,
    submitted_at    TIMESTAMPTZ,
    submit_mode     VARCHAR(32)
                    CHECK (submit_mode IS NULL OR submit_mode IN ('CANDIDATE','AUTO_TIMER','FORCE','SECURITY')),
    client_ip       VARCHAR(64),
    device_fingerprint TEXT,
    network_check_result VARCHAR(32),
    timer_ends_at   TIMESTAMPTZ,
    last_heartbeat_at TIMESTAMPTZ,
    focus_violation_count INTEGER NOT NULL DEFAULT 0,
    visibility_violation_count INTEGER NOT NULL DEFAULT 0,
    security_flags_json JSONB,
    status          VARCHAR(32) NOT NULL DEFAULT 'SCHEDULED'
                    CHECK (status IN (
                        'SCHEDULED','ACTIVATED','IN_PROGRESS','SUBMITTED',
                        'LOCKED','TERMINATED_SECURITY','ABSENT'
                    )),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (registration_id, exam_session_id)
);

CREATE UNIQUE INDEX uq_exam_attempt_one_in_progress
    ON conduct.exam_attempt (registration_id)
    WHERE status = 'IN_PROGRESS';

CREATE TABLE conduct.attendance_event (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_attempt_id UUID NOT NULL REFERENCES conduct.exam_attempt(id),
    event_type      VARCHAR(32) NOT NULL
                    CHECK (event_type IN (
                        'VERIFY','VERIFY_REJECT','MARK_PRESENT','MARK_ABSENT','CORRECTION'
                    )),
    from_status     VARCHAR(32),
    to_status       VARCHAR(32),
    reason_text     TEXT,
    actor_staff_id  UUID REFERENCES iam.staff_user(id),
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE ops_centre.centre_ops_snapshot (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    centre_id       UUID NOT NULL REFERENCES centre.exam_centre(id),
    session_id      UUID NOT NULL REFERENCES schedule.exam_session(id),
    as_of           TIMESTAMPTZ NOT NULL DEFAULT now(),
    present_count   INTEGER NOT NULL DEFAULT 0,
    activated_count INTEGER NOT NULL DEFAULT 0,
    in_progress_count INTEGER NOT NULL DEFAULT 0,
    submitted_count INTEGER NOT NULL DEFAULT 0,
    UNIQUE (centre_id, session_id, as_of)
);

CREATE TABLE conduct.paper_instance (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_attempt_id UUID NOT NULL UNIQUE REFERENCES conduct.exam_attempt(id),
    version_label   VARCHAR(64) NOT NULL,
    seed_value      BIGINT,
    assembled_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','LOCKED'))
);

CREATE TABLE conduct.paper_instance_item (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    paper_instance_id UUID NOT NULL REFERENCES conduct.paper_instance(id) ON DELETE CASCADE,
    sequence_no     INTEGER NOT NULL,
    question_id     UUID NOT NULL REFERENCES qbank.question(id),
    option_order_json JSONB,
    correct_option_map_json JSONB,
    marks           NUMERIC(8,2),
    UNIQUE (paper_instance_id, sequence_no),
    UNIQUE (paper_instance_id, question_id)
);

CREATE TABLE conduct.exam_response (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_attempt_id UUID NOT NULL REFERENCES conduct.exam_attempt(id),
    paper_instance_item_id UUID NOT NULL REFERENCES conduct.paper_instance_item(id),
    selected_option_ids JSONB,
    answered_at     TIMESTAMPTZ,
    is_marked_for_review BOOLEAN NOT NULL DEFAULT FALSE,
    is_locked       BOOLEAN NOT NULL DEFAULT FALSE,
    UNIQUE (exam_attempt_id, paper_instance_item_id)
);

CREATE TABLE conduct.exam_activity_event (
    id              BIGSERIAL PRIMARY KEY,
    exam_attempt_id UUID NOT NULL REFERENCES conduct.exam_attempt(id),
    event_type      VARCHAR(64) NOT NULL,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    detail_json     JSONB
);

CREATE INDEX ix_exam_activity_attempt
    ON conduct.exam_activity_event (exam_attempt_id, occurred_at);

CREATE TABLE conduct.access_denial_log (
    id              BIGSERIAL PRIMARY KEY,
    registration_id UUID REFERENCES registration.registration(id),
    session_id      UUID REFERENCES schedule.exam_session(id),
    reason_code     VARCHAR(64) NOT NULL,
    client_ip       VARCHAR(64),
    detail_json     JSONB,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- =============================================================================
-- MODULE 10 — Evaluation & Results
-- =============================================================================

CREATE TABLE result.evaluation_run (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_attempt_id UUID NOT NULL UNIQUE REFERENCES conduct.exam_attempt(id),
    correct_count   INTEGER NOT NULL DEFAULT 0,
    incorrect_count INTEGER NOT NULL DEFAULT 0,
    unanswered_count INTEGER NOT NULL DEFAULT 0,
    config_version_ref VARCHAR(64),
    config_snapshot_json JSONB,
    engine_version  VARCHAR(32),
    evaluated_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE result.score_result (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    evaluation_run_id UUID NOT NULL UNIQUE REFERENCES result.evaluation_run(id),
    raw_score       NUMERIC(10,2) NOT NULL,
    negative_marks  NUMERIC(10,2) NOT NULL DEFAULT 0,
    total_score     NUMERIC(10,2) NOT NULL,
    percentage      NUMERIC(5,2),
    pass_fail       VARCHAR(8) NOT NULL CHECK (pass_fail IN ('PASS','FAIL'))
);

CREATE TABLE result.evaluation_rule_alignment (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    lifecycle_config_id UUID REFERENCES qbank.examination_lifecycle_config(id),
    validation_status VARCHAR(32) NOT NULL
                    CHECK (validation_status IN ('OK','BLOCKED','WARNING')),
    error_codes_json JSONB,
    last_checked_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE result.result_publication (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    exam_session_id UUID REFERENCES schedule.exam_session(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'WITHHELD'
                    CHECK (status IN ('WITHHELD','PUBLISHED')),
    published_at    TIMESTAMPTZ,
    published_by    UUID REFERENCES iam.staff_user(id),
    display_rules_snapshot_json JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE result.candidate_result (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    score_result_id UUID NOT NULL REFERENCES result.score_result(id),
    publication_id  UUID REFERENCES result.result_publication(id),
    visible_to_candidate BOOLEAN NOT NULL DEFAULT FALSE,
    display_snapshot_json JSONB,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- =============================================================================
-- MODULE 11 — Certificate Management
-- =============================================================================

CREATE TABLE certificate.certificate_number_sequence (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    examination_id  UUID NOT NULL UNIQUE REFERENCES qbank.examination(id),
    prefix          VARCHAR(32) NOT NULL,
    next_value      BIGINT NOT NULL DEFAULT 1,
    max_value       BIGINT,
    pad_width       INTEGER NOT NULL DEFAULT 6,
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE certificate.certificate (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL UNIQUE REFERENCES registration.registration(id),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    certificate_number VARCHAR(64) NOT NULL UNIQUE,
    issue_date      DATE NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ISSUED'
                    CHECK (status IN ('ISSUED','CANCELLED','REVOKED')),
    disclosure_snapshot_json JSONB NOT NULL,
    document_uri    TEXT,
    issued_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
    cancelled_at    TIMESTAMPTZ,
    cancel_reason   TEXT,
    cancelled_by    UUID REFERENCES iam.staff_user(id)
);

CREATE TABLE certificate.certificate_document (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    certificate_id  UUID NOT NULL UNIQUE REFERENCES certificate.certificate(id),
    pdf_uri         TEXT NOT NULL,
    qr_embedded     BOOLEAN NOT NULL DEFAULT TRUE,
    generated_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
    render_engine_version VARCHAR(32)
);

CREATE TABLE certificate.certificate_verification_token (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    certificate_id  UUID NOT NULL UNIQUE REFERENCES certificate.certificate(id),
    token           VARCHAR(128) NOT NULL UNIQUE,
    public_disclosure_json JSONB NOT NULL,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE'
                    CHECK (status IN ('ACTIVE','INACTIVE','CANCELLED')),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE certificate.certificate_verification_hit (
    id              BIGSERIAL PRIMARY KEY,
    token           VARCHAR(128) NOT NULL,
    result_code     VARCHAR(32) NOT NULL
                    CHECK (result_code IN ('VALID','INVALID','CANCELLED')),
    queried_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    client_ip       VARCHAR(64)
);

CREATE TABLE certificate.certificate_download_log (
    id              BIGSERIAL PRIMARY KEY,
    certificate_id  UUID NOT NULL REFERENCES certificate.certificate(id),
    candidate_id    UUID NOT NULL REFERENCES registration.candidate(id),
    downloaded_at   TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE certificate.certificate_issuance_log (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    registration_id UUID NOT NULL REFERENCES registration.registration(id),
    examination_id  UUID NOT NULL REFERENCES qbank.examination(id),
    batch_run_id    UUID,
    outcome         VARCHAR(32) NOT NULL
                    CHECK (outcome IN ('ISSUED','ISSUANCE_SKIPPED','ISSUANCE_FAILED')),
    certificate_id  UUID REFERENCES certificate.certificate(id),
    error_text      TEXT,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE certificate.certificate_export_run (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    requested_by    UUID REFERENCES iam.staff_user(id),
    parameters_json JSONB,
    output_uri      TEXT,
    row_count       INTEGER,
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ
);

-- =============================================================================
-- MODULE 12 — MIS Reporting
-- =============================================================================

CREATE TABLE mis.mis_report_definition (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code            VARCHAR(64) NOT NULL UNIQUE,
    name            VARCHAR(200) NOT NULL,
    default_params_json JSONB,
    status          VARCHAR(32) NOT NULL DEFAULT 'ACTIVE',
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE mis.mis_report_run (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    report_code     VARCHAR(64) NOT NULL REFERENCES mis.mis_report_definition(code),
    parameters_json JSONB,
    requested_by    UUID REFERENCES iam.staff_user(id),
    status          VARCHAR(32) NOT NULL DEFAULT 'QUEUED'
                    CHECK (status IN ('QUEUED','RUNNING','COMPLETED','FAILED')),
    output_uri      TEXT,
    row_count       INTEGER,
    created_at      TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at    TIMESTAMPTZ
);

-- =============================================================================
-- Cross-cutting audit
-- =============================================================================

CREATE TABLE audit.audit_event (
    id              BIGSERIAL PRIMARY KEY,
    occurred_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    actor_type      VARCHAR(32) NOT NULL
                    CHECK (actor_type IN ('STAFF','CANDIDATE','SYSTEM','PUBLIC')),
    actor_id        UUID,
    module_code     VARCHAR(8) NOT NULL,
    action_code     VARCHAR(64) NOT NULL,
    entity_type     VARCHAR(64),
    entity_id       VARCHAR(128),
    before_json     JSONB,
    after_json      JSONB,
    channel         VARCHAR(32),
    correlation_id  VARCHAR(100)
);

CREATE INDEX ix_audit_event_module_time
    ON audit.audit_event (module_code, occurred_at DESC);

-- Seed MIS report codes from pack
INSERT INTO mis.mis_report_definition (code, name, status) VALUES
    ('CENTRE_WISE', 'Centre-wise MIS Report Suite', 'ACTIVE'),
    ('CATEGORY_DEPT_WISE', 'Category-wise and Department-wise MIS Report Suite', 'ACTIVE'),
    ('CERTIFICATE', 'Certificate MIS Report Suite', 'ACTIVE');

COMMIT;

-- =============================================================================
-- End of CREATE dump
-- Table count (approx): 85+ including gap-fill satellites
-- =============================================================================
