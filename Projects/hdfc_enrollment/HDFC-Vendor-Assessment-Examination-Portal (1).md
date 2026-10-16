# HDFC Vendor Assessment — Project & Repository Data Submission

## Project: Examination Management Portal (Computer Literacy Test, Government of Karnataka)

| Item | Detail |
|---|---|
| Prepared from | Repository review of the frontend and backend repositories (local clones, branch `main`), project documents in `docs/` |
| Review date | 08-10-2026 |
| Prepared by | _[Name / Repository owner]_ |
| Reviewed by | _[Technical owner / PM]_ |
| Version | 1.0 (draft) |

**How to read this document**

- Status values used: **Available**, **Partially Available**, **Not Available**, **Not Applicable**, **Not Verified**, **To be obtained from another team**.
- Information level: **[Project]** = verified in this project's repositories; **[Org]** = organisation-level, to be supplied by the central/security team; **[Client]** = client-specific; **[Infra]** = infrastructure/hosting team.
- Evidence paths are relative to the repository root. `FE` = `examination-management-portal-frontend`, `BE` = `-examination-management-portal-backend`.
- No passwords, keys, tokens or other secrets are reproduced in this document. Where secrets were found in the repository they are reported by location only (Section 25.2).

---

## A. PROJECT INFORMATION

## 1. Project Identification

| Field | Value | Status | Source / Evidence |
|---|---|---|---|
| Project name | Examination Management Portal — Computer Literacy Test (CLT) | Available | `docs/Statement-of-Work.md`; `BE/src/main/resources/application.yml` (`spring.application.name: examination-management-portal`) |
| Client / Department | KEONICS / Government of Karnataka (as stated in SOW draft) | Partially Available — confirm with PM | `docs/Statement-of-Work.md` §Header |
| Industry / Domain | Government — e-Governance / Examination & Certification | Available | SOW §2 |
| Project type | **Government** | Available | SOW |
| Project start date | 10-09-2026 (first commit in both repositories) | Available (repository) — contract date Not Available | `git log --reverse` on FE and BE |
| Project end date / current status | In development / internal testing; last commit 07-10-2026 | Available | `git log` |
| Project duration (so far) | ~4 weeks of repository activity | Available | `git log` |
| Current production status | **Not Verified.** `prod` and `release/uat` branches exist on GitHub, but no production deployment evidence (pipeline, release, tag, deployment log) is present in the repositories | Not Verified — To be obtained from DevOps | `git branch -r` (FE & BE): `origin/prod`, `origin/release/uat` |
| Environments | Profiles: `local`, `dev`, `test`, `prod` (backend). A dev server is referenced in `application-dev.yml` | Partially Available | `BE/src/main/resources/application-*.yml` |
| Repository names | `examination-management-portal-frontend`; `-examination-management-portal-backend` | Available | `git remote -v` |
| Repository URLs | `git@github.com:Inventechinfosolutions/examination-management-portal-frontend.git`; `git@github.com:Inventechinfosolutions/-examination-management-portal-backend.git` | Available | `git remote -v` |
| Repository type | **GitHub** (organisation: Inventechinfosolutions) | Available | `git remote -v` |
| Repository visibility (private/public) | Not Verified (GitHub CLI/API not available during review) | Not Verified | — |
| Repository owner / Technical owner | _[To be filled]_ | To be obtained from PM | — |
| Project manager | _[To be filled]_ | To be obtained from PM | — |
| Solution architect | _[To be filled]_ | To be obtained from PM | — |
| DevOps / Infrastructure owner | _[To be filled]_ | To be obtained from DevOps | — |
| Security owner | _[To be filled]_ | To be obtained from Security team | — |
| Contributors (git authors) | 5–6 individual developers committing under 10 git identities (Sushmitha, Narendra, Srinath R, Anil Kishore, Srujan, plus one "dev server" identity) | Available | `git shortlog -sn --all` |

## 2. Project Scope (as implemented)

**Business objective** — Online registration, scheduling, centre-based conduct, invigilation, computer-based testing, automated evaluation and certification of the Computer Literacy Test for Karnataka government employees. Source: `docs/Statement-of-Work.md` §2.

| Item | Implemented scope | Status | Evidence |
|---|---|---|---|
| Major modules | User management (persons, posts, roles, permissions, mappings); Masters (location, holidays, fee); Exam centres; Examinations; Question bank; Scheduling; Candidate registration; Registration review; Invigilator registration; Centre operations (verification, attendance, activation, monitoring); Exam portal (CBT); Results & certificates; IP allowlist; Audit trail; Localisation (EN/KN) | Available | `FE/src/features/*` (22 feature folders); `BE/src/main/java/com/backend/template/modules/*` (15 modules) |
| User types | Super Admin, Examination Administrator, Examination Centre Admin, Examination Centre Invigilator, Candidate, Public | Available | `BE/.../common/security/SystemRoles.java`; `BE/.../db/migration/V2__create_user_management.sql` |
| Approximate number of users | Not Available. Load test designed for 500 concurrent candidates in one session and 300 registrations | Partially Available | `BE` branch `origin/feature/loadTesting`: `load-tests/k6/reports/LOAD_TEST_REPORT.md` |
| External systems integrated | **None live.** Payment gateway, KGID lookup, SMS notification are **stubs**; email/SMTP not built | Available (as gap) | `BE/.../candidateregistration/integration/Stub*.java` |
| APIs exposed | REST/JSON under `/api/v1`; 31 controllers, ~226 endpoints; OpenAPI at `/v3/api-docs`, Swagger UI at `/swagger-ui.html` | Available | `BE/.../modules/*/controller/*.java`; `application.yml` (`springdoc`) |
| APIs consumed | None live (stub adapters only) | Available | as above |
| Major workflows | Staff login (credentials → captcha → JWT); candidate OTP login → profile → documents → exam/session → centre → fee → payment → submit → admin review → hall ticket; exam day: QR scan → identity verification → attendance → activation → CBT → auto-evaluation → result → certificate | Available | SOW §4; FE routes `FE/src/routes/*` (56 route files) |
| Reports / dashboards | Admin dashboard, centre dashboard, live monitoring, allocation summary (CSV export), audit summary & CSV export, question-bank summary | Available | `FE/src/features/dashboard`, `centre-operations`, `audit`; `BE/.../centre/controller/CentreController.java` (CSV) |
| Mobile application | Not Applicable (responsive web only) | Not Applicable | SOW §12 |
| Web application | React SPA (public, admin, centre, candidate, exam portal) | Available | `FE/` |
| Backend services | Single Spring Boot application (modular monolith) | Available | `BE/pom.xml`, `BE/Dockerfile` |
| Batch / scheduled jobs | **None found** (no `@Scheduled` / `@EnableScheduling` in source) | Available (verified absent) | source search |
| Notification services | Stub only — OTP written to server log, not delivered; no email | Available (as gap) | `BE/.../integration/StubNotificationAdapter.java` |
| File / document processing | Candidate documents & photograph upload (MIME and size checks, photo dimension check), Excel import (questions, device whitelist) via Apache POI, PDF generation (hall ticket, application, marks card, certificate), QR generation/scanning | Available | `BE/.../RegistrationService.java`, `PhotographValidator.java`, `pom.xml` (poi-ooxml 5.4.1); `FE` jsPDF, jsQR |
| AI/ML components | None | Not Applicable | dependency review of `package.json` and `pom.xml` |
| Requirements / SRS | Not Available as a separate SRS | Not Available | — |
| SOW | `docs/Statement-of-Work.md` / `.pdf` (draft v1.0, 08-10-2026, unsigned) | Partially Available (draft) | `docs/` |
| Architecture document | Not Available (no diagram in repositories) | Not Available | — |
| Functional / technical specification | Partial: `BE/PROJECT_GUIDE.md` (coding conventions), `FE/docs/PROJECT_STRUCTURE.md`, `FE/docs/DESIGN-SYSTEM.md` | Partially Available | as listed |

---

## B. TECHNOLOGY & ARCHITECTURE

## 3. Technology Stack (verified against build files)

### Frontend [Project] — Source: `FE/package.json`, `FE/vite.config.ts`

| Item | Value |
|---|---|
| Framework | React ^19.2.0 |
| Language | TypeScript ~5.9.2 |
| Build tool | Vite ^7.1.7 (`tsc -b && vite build`) |
| Package manager | npm (`package-lock.json`) |
| Routing | TanStack Router ^1.132.0 (file-based, auto code-splitting) |
| Server state | TanStack Query ^5.90.2 |
| Forms / validation | react-hook-form ^7.63.0, zod ^4.1.11 |
| UI | Tailwind CSS ^4.1.13, Radix UI ^1.6.7, shadcn, lucide-react, framer-motion, recharts, sonner |
| i18n | i18next ^26.4.2, react-i18next ^17.0.14 (English, Kannada) |
| Documents | jspdf ^4.2.1, html2canvas ^1.4.1, jsqr ^1.4.0 |
| Code quality | ESLint ^9.36.0, typescript-eslint, Prettier ^3.6.2 |
| Automated tests | **None** (no `*.test.ts(x)` / `*.spec.ts(x)` files) |

### Backend [Project] — Source: `BE/pom.xml`, `BE/Dockerfile`

| Item | Value |
|---|---|
| Framework | Spring Boot 3.5.5 (Web, Validation, Data JPA, Security, Actuator, Data Redis, Cache) |
| Language / runtime | Java 21; container image `eclipse-temurin:21-jre-alpine` |
| Architecture | Modular monolith; feature modules (controller / service / repository / entity / dto) |
| Security libs | Spring Security, jjwt 0.12.6 (JWT), BCrypt |
| Other libs | MapStruct 1.6.3, Lombok 1.18.46, springdoc-openapi 2.8.9, Apache POI 5.4.1, MinIO client 8.5.17, Flyway |
| Automated tests | 21 test classes, 81 `@Test` methods (JUnit / Spring Boot Test / Spring Security Test, H2) |
| Load testing | k6 suite and report on branch `origin/feature/loadTesting` (not merged to `main`) |

### Database [Project]

| Item | Value | Evidence |
|---|---|---|
| Technology / type | MySQL (relational). Compose file: `mysql:8.4`; load test used MySQL 8.0.41 | `BE/docker-compose.yml`; load-test report §3 |
| Number of databases | 1 application schema | `application-*.yml` |
| Schema management | Flyway, 33 migration scripts (`V1`–`V41`, with gaps) | `BE/src/main/resources/db/migration/` |
| Tables | ~46 tables created by Flyway; **9 tables used by the code are not created by any Flyway script** (see Gaps) | migration vs `@Table` comparison |
| Test DB | H2 in-memory (MySQL mode) | `application-test.yml` |

### Other technologies — verification result

| Technology | Used? | Evidence / note |
|---|---|---|
| Redis | **Yes** — cache, token revocation/session store | `application.yml` (`spring.data.redis`, `spring.cache.type: redis`), `BE/.../infrastructure/redis/` |
| MinIO / object storage | **Yes** — documents/photos | `application.yml` (`app.storage`), `MinioObjectStorageService.java` |
| Docker | **Partial** — backend `Dockerfile` (non-root user) and `docker-compose.yml` for local MySQL/Redis/MinIO; no frontend Dockerfile | `BE/Dockerfile`, `BE/docker-compose.yml` |
| Elasticsearch / Typesense / Qdrant | No | not in dependencies |
| Kafka / RabbitMQ | No | not in dependencies |
| API gateway | Not found in repositories | Not Verified — Infra |
| Nginx / reverse proxy | Not found in repositories. Code reads `X-Forwarded-For` / `X-Real-IP` / `CF-Connecting-IP`, which suggests a proxy is expected | `ClientIpResolver.java` — Not Verified |
| Kubernetes / Helm / Istio / Argo | No manifests found | Not Available |
| Jenkins / GitHub Actions / other CI | **No pipeline files** (`.github/workflows`, `Jenkinsfile`, etc. absent) | Not Available |
| Monitoring | Actuator endpoints `health, info, metrics, prometheus` exposed; no Prometheus/Grafana configuration in repo | `application.yml` (`management.endpoints`) — Partially Available |
| Logging | Console logging with correlation ID (logback pattern); no central log shipping configuration | `application.yml` (`logging.pattern`), `CorrelationIdFilter.java` |
| SIEM / WAF / DDoS | Not found in repositories | To be obtained from Infra/Security |
| Cloud services | None referenced | Not Verified — Infra |
| Third-party services | None live (payment, KGID, SMS stubbed) | `integration/Stub*.java` |

## 4. Architecture

| Item | Status | Detail / Evidence |
|---|---|---|
| Application architecture diagram | **Not Available** | No diagram in repositories. Logical architecture derived from code below |
| Deployment / network / cloud / on-prem architecture | **Not Available** | To be obtained from DevOps/Infra |
| Integration architecture | Partially Available | Port/adapter interfaces: `PaymentIntegrationPort`, `KgidIntegrationPort`, `NotificationPort`, `ExamCatalogPort`, `ExamSessionCatalogPort` with stub adapters |
| Data architecture | Partially Available | Flyway scripts; no ER diagram |
| Authentication architecture | Available (code) | Staff: JWT access (15 min) + refresh (8 h) with Redis revocation; Candidate: OTP → opaque session token (SHA-256 hash stored) with idle/absolute expiry |
| Security architecture | Partially Available (code only) | Section 10 |

**Logical architecture derived from repository [Project]:**

```
Browser (React SPA, EN/KN)
   │  HTTPS (not configured in repo — Not Verified)
   ▼
[Reverse proxy / LB — Not Verified]
   ▼
Spring Boot API (single instance, port 3600/3601)  ── /actuator (health, metrics, prometheus)
   ├── MySQL (Flyway-managed schema)
   ├── Redis (cache, JWT revocation, sessions)
   ├── MinIO (documents, photos; presigned URLs, 15-min expiry)
   └── Stub adapters: Payment, KGID, SMS (no external calls)
Exam workstations → IP allowlist check → Exam portal endpoints
```

| Component | Identified | Evidence |
|---|---|---|
| Application server | Embedded Tomcat (Spring Boot) | `pom.xml`, `application.yml` (`server.tomcat`) |
| Web server for SPA | Not Verified (Vite build output `dist/`; hosting not in repo) | `FE/package.json` |
| API gateway / load balancer | Not Verified | — |
| Database / cache / object storage | MySQL / Redis / MinIO | as above |
| Message broker | None | — |
| Identity provider | In-application (no external IdP/SSO) | `modules/auth` |
| Monitoring / security components | Actuator only; WAF/IDS not verified | — |

---

## 5. Repository & Development Practices [Project]

| Item | Finding | Status | Evidence |
|---|---|---|---|
| Repository structure | FE: `src/{app,components,features,lib,routes,locales,...}`; BE: `src/main/java/.../{config,common,infrastructure,modules}`, `db/migration` | Available | `FE/docs/PROJECT_STRUCTURE.md`, `BE/PROJECT_GUIDE.md` |
| Branching strategy | Feature branches (`feature/*`, `bug/*`, `ui/*`) merged into `main`; `release/uat` and `prod` branches exist | Partially Available (not documented) | `git branch -r` |
| Development / UAT / Production branches | `main` / `release/uat` / `prod` (FE: all three point to the same commit `c3b2fa3`; BE: three different PR merges #34/#35/#36 on 07-10-2026) | Available | `git log -1 origin/{main,release/uat,prod}` |
| Pull request process | Used: FE 52 PR merges (up to #52), BE 36 PR merges (up to #36) | Available | `git log --merges` ("Merge pull request #…") |
| Code review / approvals | **Not Verified** — PR review records and approvals must be checked on GitHub | Not Verified | GitHub PR pages |
| Branch protection | **Not Verified** — GitHub settings not accessible during review | Not Verified | GitHub → Settings → Branches |
| Commit standards | Not enforced (no commitlint/husky); mixed message quality (e.g. "bugs resolved") | Available (gap) | `git log` |
| Code ownership | No `CODEOWNERS` file | Not Available | — |
| Release / versioning / tagging | **No git tags**; no release notes; app version not managed | Not Available | `git tag` (0 tags) |
| Release history / deployment history | Not Available in repository | Not Available | — |
| Coding standards | `BE/PROJECT_GUIDE.md` (structure, naming, NEVER/ALWAYS rules), `BE/AGENTS.md`, `FE/CLAUDE.md`, ESLint + Prettier config | Partially Available | as listed |
| Repository access controls | Not Verified (GitHub organisation membership/teams) | To be obtained from GitHub org admin | — |

## 6. SDLC & Development Process

| Area | Finding | Status | Evidence |
|---|---|---|---|
| Requirement management | SOW draft only; no ticketing evidence in repo | Partially Available | `docs/Statement-of-Work.md` |
| Development process | Feature branch → PR → merge to `main` | Partially Available | git history |
| Unit / integration testing | BE: 21 test classes / 81 tests (controller and service tests, H2). FE: none | Partially Available | `BE/src/test/java` |
| System testing / UAT | No test plan, test cases or UAT sign-off in repo | Not Available | — |
| Security testing | No SAST/DAST/dependency scan configuration or report in repo | Not Available | — |
| Performance testing | **k6 load test performed 06–07 Oct 2026** — 7/7 objectives met; up to 500 concurrent exam candidates; re-test after fixes. Executed on a single laptop (not production-like) | Available (limited environment) | BE branch `origin/feature/loadTesting`: `load-tests/k6/reports/LOAD_TEST_REPORT.md/.pdf/.html` |
| Release / change / rollback / defect management | No documented process or tool evidence in repo | Not Available — To be obtained from PM / Org | — |
| SDLC policy, secure coding policy | Not in repo | To be obtained from Org | — |

---

## C. SECURITY ASSESSMENT

## 7. Authentication & User Access Management [Project — verified in code]

| Control | Implementation | Status | Evidence |
|---|---|---|---|
| Authentication (staff) | Login ID + password → server-side captcha challenge → JWT access + refresh tokens | Available | `BE/.../auth/controller/AuthController.java`, `AuthService.java`, `LoginCaptchaService.java` |
| Authentication (candidate) | Mobile number + 6-digit OTP (`SecureRandom`), OTP stored as SHA-256 hash; opaque session token (hash stored) | Available | `CandidateAuthService.java`, `OtpGenerator.java`, `HashUtil.java`, `CandidateSessionAuthenticationFilter.java` |
| Authentication (exam workstation) | IP allowlist + hall ticket number + registered name | Available | `modules/ipallowlist`, `modules/examportal` |
| Authorization / RBAC | Role- and permission-based; `@EnableMethodSecurity` with **107 `@PreAuthorize` annotations**; JWT carries roles, permissions, centre ID; centre-scoped data access for centre roles | Available | `SecurityConfig.java`, controllers, `common/security/AccessRules.java`, `ActorScope.java` |
| Roles | SUPER_ADMIN, EXAMINATION_ADMINISTRATOR, EXAMINATION_CENTRE_ADMIN, EXAMINATION_CENTRE_INVIGILATOR, CANDIDATE; scopes ORG_WIDE / CENTRE / PORTAL; custom roles can be created | Available | `SystemRoles.java`, `V2__create_user_management.sql` |
| Permissions & role–permission mapping | Permission catalogue + role–permission mapping UI and API; seeded navigation permissions | Available | `V2__…sql`, `V26__seed_role_nav_permissions.sql`, `FE/src/features/permissions` |
| Role matrix document | Not Available as a document (only in DB seed + UI) | Not Available | — |
| MFA | **Not implemented.** Staff login uses password + captcha (captcha is not a second factor). Candidate login is OTP-only (single factor, possession-based) | Not Available (gap) | `AuthService.java` |
| Password hashing | BCrypt (Spring default strength 10) | Available | `SecurityConfig.passwordEncoder()` |
| Password complexity | 10–16 chars, upper, lower, digit, special, no spaces — enforced on reset/change | Available | `BE/.../auth/dto/ResetPasswordRequest.java` (`@Pattern`) |
| Password expiry / history | **Not implemented** (`last_password_changed_at` column exists but no expiry or history check) | Not Available (gap) | `UserAccount.java` |
| Failed login attempts / lockout | Staff: lock after 5 failures for 30 min (configurable). Candidate OTP: 5 verify attempts, 30-min lockout, resend cooldown 60 s, max 5 resends (DB-configurable policy) | Available | `application.yml` (`app.auth.max-failed-attempts`, `lockout-duration`), `AuthService.registerFailedAttempt`, `OtpPolicy.java` |
| Session timeout | Staff access token 15 min, refresh 8 h; candidate session idle 30 min / absolute 8 h; frontend auto-logout on expiry | Available | `application.yml` (`JWT_ACCESS_TTL`, `JWT_REFRESH_TTL`), `OtpPolicy.java`, `FE/src/lib/session-expiry.ts` |
| Token revocation / logout | JWT ID (`jti`) revocation list in Redis | Available | `JwtTokenService.revoke*`, `SessionCacheService` |
| Password reset | OTP-based forgot/reset for staff. **OTP is not delivered** (no SMS/email integration) and is held in application memory (lost on restart, not shared across instances) | Partially Available (gap) | `StaffPasswordResetService.java` |
| User provisioning | Admin creates person → post → post–person mapping → staff login issued. **Uses a fixed default password defined in source code; no forced change at first login** | Partially Available (gap) | `UserAccountService.java`, `InvigilatorRegistrationService.java` |
| De-provisioning / activation | Enable/disable persons and accounts; unmap person from post | Available | `FE/src/features/persons`, `post-person-mappings`; `modules/usermanagement` |
| Third-party user access | Not Applicable (no third-party accounts) | Not Applicable | — |
| Privileged access management | Not implemented in application; infra PAM Not Verified | Not Available | — |
| Periodic access review | No process or records | Not Available — To be obtained from Org | — |
| Onboarding/deboarding records | Not Available | To be obtained from PM | — |

## 8. Data Model & Data Dictionary [Project]

| Item | Status | Detail / Evidence |
|---|---|---|
| ER diagram | **Not Available** | Can be generated from the database |
| Data dictionary | **Not Available** | — |
| Database schema | Available (as DDL) | 33 Flyway scripts in `BE/src/main/resources/db/migration/` |
| Table list (Flyway) | Available | users, roles, permissions, role_permissions, user_roles, posts, post_person_mappings, personal_details, mst_country/state/district/taluk, master_holidays, ctr_centre, exm_examination, examinations, examination_questions, examination_section_topics, questions, question_options, question_categories, sch_schedule, cand_candidate, cand_otp_challenge, cand_otp_policy, cand_portal_session, reg_application, reg_profile, reg_document, reg_document_template, reg_centre_preference, reg_fee_assessment, reg_payment_attempt, reg_review, reg_hall_ticket, reg_number_sequence, ops_attendance, ops_candidate_day, ops_identity_verification, ops_session_activation, ops_exam_portal_session, exam_attempts, exam_attempt_questions, exam_attempt_answers, certificates, auth_login_captcha |
| Tables without Flyway DDL | **Gap** | audit_events, ctr_capacity, ctr_device_restriction, ctr_infrastructure, ctr_session_mapping, ctr_user_binding, exam_ip_allowlist, invigilator, reg_fee_master (only created by Hibernate `ddl-auto: update` in the `local` profile; `prod` uses `ddl-auto: none`) |
| Keys / relationships | ~55 foreign-key references in DDL; UUID and BIGINT keys | migrations |
| Validation rules | Bean Validation on DTOs (`@Size`, `@Pattern`, `FieldPatterns`), zod schemas on frontend | `BE/.../dto/*`, `FE/src/**/schemas/*` |
| PII fields | Name, mobile, email, date of birth, gender, **Aadhaar number** (`reg_profile.aadhaar_number`, plain VARCHAR(12)), address, disability type/percent, KGID number and snapshot, photograph, signature and Aadhaar document uploads (MinIO) | Available | `V4__…`, `V5__profile_icsi_fields.sql`, `Profile.java` |
| Financial data | Fee amount, payment attempts, receipt number (no card/bank data — gateway not integrated) | Available | `reg_payment_attempt`, `reg_fee_assessment` |
| Authentication data | `password_hash` (BCrypt), `otp_hash`, session token hash, captcha hash (SHA-256) | Available | migrations, `HashUtil.java`, `AuthHashUtil.java` |
| Audit data | `audit_events`: occurred_at, event_type, actor, target, centre, HTTP method/path/status, IP, user agent, correlation ID, reason, sanitized request/before/after payloads | Available | `AuditEvent.java` |

## 9. Data Storage & Handling

| Area | Finding | Status | Evidence |
|---|---|---|---|
| Where data is stored | MySQL (structured), MinIO buckets (documents/photos), Redis (cache, token state) | Available | config files |
| Hosting (on-prem / cloud) | Not Verified. Dev profile references a private-network Redis/MinIO host and a dev URL on a public IP over plain HTTP | Not Verified — Infra | `application-dev.yml` |
| Encryption at rest (DB, MinIO, backups) | **Not configured in repository**. Aadhaar and other PII stored in plain columns (no field-level encryption / `AttributeConverter`) | Not Available (gap) / Infra Not Verified | `Profile.java` |
| Encryption in transit | Not configured in repo: DB URLs use `useSSL=false`; Redis SSL default `false`; MinIO endpoint `http://`; no TLS config in Spring Boot | Not Available in repo (gap) — Infra Not Verified | `.env.example`, `application*.yml` |
| Key / secret management | Environment variables + `.env` loader; **no vault/KMS**; secret defaults present in committed config (Section 25.2) | Partially Available (gap) | `DotEnvLoader.java`, `application.yml` |
| Backup (frequency, type, location, retention, logs, restore test) | No backup scripts or evidence in repo | Not Available — To be obtained from Infra/DBA | — |
| Archival policy / process | Not implemented | Not Available | — |
| Data retention | No retention configuration; audit log has no purge/retention job | Not Available | source search (no scheduled jobs) |
| Data purging / secure deletion | Not implemented; no purge logs | Not Available | — |

## 10. Application Security Controls [Project — verified in code]

| Control | Implementation | Status | Evidence |
|---|---|---|---|
| Input validation | Server: Bean Validation + custom validators (Aadhaar, photo, field patterns); client: zod | Available | `common/validation`, `AadhaarValidator.java`, `PhotographValidator.java` |
| Authentication / authorization | See Section 7 | Available | `SecurityConfig.java` |
| Session management | Stateless (`SessionCreationPolicy.STATELESS`), JWT + Redis revocation | Available | `SecurityConfig.java` |
| Token storage (browser) | Staff tokens in `localStorage` ("remember me") or `sessionStorage`; candidate token in `sessionStorage` — readable by JavaScript (XSS exposure) | Partially Available (risk) | `FE/src/lib/auth-token.ts`, `candidate-session.ts` |
| API security | All endpoints authenticated except an explicit public list (login, OTP, health, public catalogue, certificate verification, Swagger) | Available | `SecurityConfig.java` lines 40–71 |
| Swagger / API docs in production | `/swagger-ui.html` and `/v3/api-docs` are **public in all profiles** | Gap | `SecurityConfig.java` |
| Secure headers | Spring Security defaults (X-Content-Type-Options, X-Frame-Options DENY, cache-control; HSTS only over HTTPS). **No Content-Security-Policy** configured | Partially Available | `SecurityConfig.java` (no `headers()` customisation) |
| CORS | Allow-list of origins from `CORS_ORIGINS`; credentials allowed; all headers allowed | Available | `SecurityConfig.corsConfigurationSource()` |
| CSRF | Disabled — acceptable for bearer-token APIs (no cookies) | Available (by design) | `SecurityConfig.java` |
| SQL injection | JPA/Hibernate with parameter binding; Spring Data specifications | Available | repositories |
| XSS | React escapes output by default; no CSP | Partially Available | — |
| File upload security | Allowed MIME types (PDF/JPEG/PNG), 5 MB limit (Spring multipart + validator), photograph decoded with ImageIO and dimension-checked, SHA-256 checksum stored; MIME is taken from the client header (no magic-byte check for PDFs) | Partially Available | `RegistrationService.java` (`ALLOWED_MIME_TYPES`), `PhotographValidator.java`, `application.yml` (`multipart`) |
| Malware scanning | **Not implemented** | Not Available (gap) | no AV integration found |
| Rate limiting | **Not implemented** — a Redis key name for login rate limiting is defined but not used. OTP resend cooldown and lockouts exist | Partially Available (gap) | `RedisKeyNames.loginRateLimit` (unused) |
| Brute-force protection | Account lockout (staff), OTP attempt lockout (candidate), captcha on staff login | Available | Section 7 |
| Error handling | Global exception handler returns generic messages; stack traces only in server logs | Available | `GlobalExceptionHandler.java` |
| Logging | SLF4J/Logback, correlation ID per request (`X-Correlation-Id`) | Available | `CorrelationIdFilter.java`, `application.yml` |
| Audit trail | Append-only audit events (logins, access denials, data changes) captured by a servlet filter; UI with filters and CSV export | Available | `modules/audit/web/AuditCaptureFilter.java`, `AuditCaptureService.java`, `FE/src/features/audit` |
| Sensitive data masking | Audit payload sanitizer removes passwords, OTPs, tokens, secrets; destinations masked in reset logs | Available | `AuditPayloadSanitizer.java` (+ test), `StaffPasswordResetService.maskDestination` |
| Sensitive data in logs (gap) | Stub SMS adapter logs the plaintext OTP; dev profile accepts a fixed OTP | Gap (must be removed/disabled for production) | `StubNotificationAdapter.java`, `CandidateAuthService.java`, `StaffPasswordResetService.java` |
| IP spoofing (exam portal) | Forwarded headers trusted only when the direct peer is a proxy address | Available | `ClientIpResolver.java`, `IpAddressMatcher` |
| Certificate integrity | Certificate verification code + SHA-256 | Available | `CertificatePdfService.java` |
| Secrets management | See Section 9 and 25.2 | Partially Available (gap) | — |
| Dependency / SAST scanning | Not configured | Not Available | — |

## 11. VAPT / Security Audit / Code Review

| Assessment | Status |
|---|---|
| VAPT (web application) | **Not Available – To be obtained from Security/Compliance Team.** No report in repositories |
| CERT-In empanelled audit / Safe-to-host certificate | **Not Available – To be obtained from Security/Compliance Team** |
| Source code security review (SAST) | Not Available — no tool configuration or report |
| Dependency vulnerability scan (SCA) | Not Available |
| Performance / load test | Available — k6 report (06–07 Oct 2026), see Section 6 |

No security findings are assumed or invented in this section. Observations from this repository review are listed under Gaps (Section F) for remediation before VAPT.

## 12. WAF / DDoS / Network Security

| Control | Status | Note |
|---|---|---|
| WAF | Not Verified — To be obtained from Infra/Security | No configuration in repositories |
| DDoS protection | Not Verified — To be obtained from Infra/Security | — |
| Firewall / IDS / IPS / VPN / segmentation | Not Verified — To be obtained from Infra | — |
| API gateway / load balancer / reverse proxy | Not Verified | Code expects a proxy (`ClientIpResolver`) |
| Application-level network control | Available | Exam-portal IP allowlist (`modules/ipallowlist`, admin UI `FE/src/features/ip-allowlist`); centre device whitelist (`ctr_device_restriction`) |

## 13. Encryption & Digital Certificates

| Area | Finding | Status |
|---|---|---|
| TLS version / HTTPS | Not configured in repository; dev URL uses HTTP | Not Verified — Infra |
| SSL certificates (type, CA, validity, renewal) | Not Available in repo | To be obtained from Infra |
| Database / object / backup encryption | Not configured in repo | Not Verified — Infra |
| Password hashing | BCrypt | Available (`SecurityConfig.java`) |
| OTP / session / captcha hashing | SHA-256 | Available (`HashUtil.java`, `AuthHashUtil.java`) |
| Token mechanism | JWT signed with HMAC (jjwt `Keys.hmacShaKeyFor`), separate access and refresh keys, `jti` revocation | Available (`JwtTokenService.java`) |
| Digital signatures on documents | Not implemented (certificates use verification code + SHA-256, not PKI signature) | Not Available |
| Random generation | `SecureRandom` for OTP, captcha, reset codes | Available |

## 14. Incident Management

| Item | Status |
|---|---|
| Incident identification, classification, severity, escalation matrix, SLA, response team, RCA, closure | **Not Available in project repository — To be obtained from Org (Security / Delivery)** |
| Supporting application capability | Audit trail of access denials and logins; correlation IDs in logs for tracing |
| Incident tickets / RCA records for this project | Not Available |

## 15. Logging & Monitoring

| Item | Finding | Status | Evidence |
|---|---|---|---|
| Application / error logging | Console logs with timestamp, thread, correlation ID, level | Available | `application.yml` |
| Audit / security / access logging | Application audit trail (DB) incl. logins, access denials, changes, IP, user agent | Available | `modules/audit` |
| API logging | Captured in audit events (method, path, status) | Available | `AuditEvent.java` |
| DB / infrastructure logging | Not Verified | Infra |
| Monitoring tools (Prometheus/Grafana/ELK/SIEM) | Actuator `prometheus` endpoint exposed (authenticated); no monitoring stack config in repo | Partially Available | `application.yml` |
| Log retention / alerting / dashboards | Not Available | To be obtained from Infra |

## 16. CI/CD & Deployment

| Item | Finding | Status |
|---|---|---|
| Source repository | GitHub (2 repos) | Available |
| CI tool / pipeline | **None** — no GitHub Actions, Jenkins, Bitbucket or other pipeline definitions | Not Available (gap) |
| Build process | Manual: FE `npm run build`; BE `mvn package` then `docker build` (Dockerfile copies `target/*.jar`) | Available (manual) |
| Test automation in pipeline | Not Available | — |
| Security / container scanning | Not Available | — |
| Artifact repository / image registry | Not found | Not Available |
| Deployment tool / Kubernetes / Helm / Argo | Not found | Not Available |
| Approval / production deployment / rollback process | Not documented | Not Available — To be obtained from DevOps |
| Deployment documentation | Only local quick start in `BE/README.md` and `FE/README.md` | Partially Available |

## 17. Infrastructure & Hosting

All items — hosting model, cloud provider/data centre, VM/Kubernetes, storage, network, firewall, load balancer, backup and DR infrastructure — are **Not Verified — To be obtained from DevOps/Infra team**. The repositories contain only local Docker Compose definitions (MySQL 8.4, Redis 7.4, MinIO) and Spring profile configuration.

## 18. Disaster Recovery & Business Continuity

| Item | Status |
|---|---|
| DR architecture / site / RPO / RTO / procedure / test frequency / last test / report | **Not Available — To be obtained from Infra / Org** |
| Application readiness | Graceful shutdown configured (`server.shutdown: graceful`); Redis AOF enabled in compose (local) |

## 19. Third-Party Integrations

| System | Purpose | Integration type | API / Protocol | Authentication | Data exchanged | Owner | Status |
|---|---|---|---|---|---|---|---|
| Payment gateway | Registration fee | Adapter (`PaymentIntegrationPort`) | Not yet defined | Not yet defined | Application ID, amount, payment ref, status, receipt | Client / Vendor | **Stub — not integrated** |
| KGID / employee master | Verify government employees | Adapter (`KgidIntegrationPort`) | Planned: master data import (Excel) / optional API | Not yet defined | KGID, name, department, designation | Client | **Stub — not integrated** |
| SMS gateway | OTP and notifications | Adapter (`NotificationPort`) | Not yet defined | Not yet defined | Mobile number, OTP/message | Client / Vendor | **Stub — OTP logged, not sent** |
| Email (SMTP) | Notifications | — | SMTP (planned) | — | Email, message | Vendor | **Not built** |
| MinIO | Document storage | SDK | S3 API (HTTP in dev config) | Access key / secret key | Documents, photos | Infra | In use (self-hosted) |
| Aadhaar / UIDAI, DigiLocker, Maps, AI/LLM | — | — | — | — | — | — | Not Applicable (Aadhaar number captured, not verified with UIDAI) |

## 20. Project Size & Effort

| Metric | Value | Status / Source |
|---|---|---|
| Total / development / testing / DevOps / architecture / support man-days | _[To be filled from timesheets]_ | To be obtained from PM |
| Team size (from git) | 5–6 developers; peak concurrent contributors not measured | Available (git authors) |
| Testers / DevOps / architects / support | _[To be filled]_ | To be obtained from PM |
| Number of modules | 15 backend modules; 22 frontend feature areas | Available (repository) |
| Number of screens (route files) | 56 frontend route files | Available |
| Number of APIs | ~226 REST endpoints in 31 controllers | Available |
| Number of integrations | 3 designed (payment, KGID, SMS) + 1 planned (SMTP); 0 live | Available |
| Code size | FE ~448 TypeScript files; BE ~444 Java source files, 21 test classes | Available |
| Commits / PRs | FE 129 commits, 52 PRs; BE 93 commits, 36 PRs (10-09-2026 to 07-10-2026) | Available |
| Function points | Not Available | — |
| Supporting documents | SOW draft available; PO, project plan, estimation, completion certificate Not Available | To be obtained from PM / Commercial |

## 21. Government / Enterprise Project Evidence

| Field | Value |
|---|---|
| Client | KEONICS / Government of Karnataka (confirm) |
| Project | Examination Management Portal — Computer Literacy Test |
| Sector | Government (e-Governance, examinations) |
| Scope | Section 2 |
| Contract value | _[If permitted — To be obtained from Commercial]_ |
| Duration | Started Sep 2026; in progress |
| Technology | React 19 / TypeScript, Spring Boot 3.5 / Java 21, MySQL, Redis, MinIO |
| Team size / man-days | _[To be filled]_ |
| Deployment model | Not Verified |
| Completion status | **In progress — not suitable as a completed credential yet** |
| PO / work order / completion certificate / client certificate | Not Available — To be obtained from Commercial / PM |

## 22. Quality & Certifications

ISO 9001, ISO 27001, ISO 20000, CMMI, SOC 1/2, PCI DSS, CERT-In and data-centre/cloud certifications are **organisation- or infrastructure-level** and are **not evidenced in the project repositories — To be obtained from the central compliance team**. No project-level certification exists.

## 23. Policies Relevant to the Project

None of the listed policies (Information Security, Data Protection, Privacy, Access Control, Password, Encryption, Key Management, Secure SDLC, Incident Response, Backup, Retention, Archival, Purging, Change Management, Vulnerability, Patch, BCP, DR, WAF, DDoS) are present in the project repositories. **To be obtained from the central compliance team [Org].**

Project-level implementation evidence that can be mapped to policies:

| Policy | Project-level implementation evidence |
|---|---|
| Password policy | Complexity rule in `ResetPasswordRequest.java`; BCrypt; lockout 5/30 min. Gaps: expiry, history, fixed default password |
| Access control policy | RBAC + permissions + centre scope (`SecurityConfig.java`, `@PreAuthorize`, `AccessRules.java`) |
| Secure SDLC | PR-based merges; coding guide `BE/PROJECT_GUIDE.md`. Gaps: no CI, no security scanning |
| Logging / audit | `modules/audit`, `AuditPayloadSanitizer.java` |
| Encryption policy | BCrypt/SHA-256/JWT-HMAC in code. Gaps: TLS/at-rest not configured in repo |
| Change management | Not evidenced in repo |

---

## D. EVIDENCE REGISTER

| # | Area | Requirement | Evidence available | Type | Location / Link | Date | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Project | SOW | Yes (draft, unsigned) | SOW | `docs/Statement-of-Work.md`, `.pdf` | 08-10-2026 | PM | Partially Available |
| 2 | Repository | Source repositories | Yes | Repository | GitHub: Inventechinfosolutions/examination-management-portal-frontend, /-examination-management-portal-backend | 07-10-2026 (last commit) | Tech owner | Available |
| 3 | Repository | PR-based merges | Yes | Repository | `git log --merges` (FE #1–#52, BE #1–#36) | 10-09 to 07-10-2026 | Tech owner | Available |
| 4 | Repository | Code review approvals | Unknown | Screenshot | GitHub PR pages | — | Tech owner | Not Verified |
| 5 | Repository | Branch protection | Unknown | Screenshot | GitHub → Settings → Branches | — | GitHub admin | Not Verified |
| 6 | Repository | Release tags / history | No | Repository | `git tag` (0) | — | Tech owner | Not Available |
| 7 | Technology | Frontend stack | Yes | Configuration | `FE/package.json` | — | Tech owner | Available |
| 8 | Technology | Backend stack | Yes | Configuration | `BE/pom.xml`, `BE/Dockerfile` | — | Tech owner | Available |
| 9 | Architecture | Architecture diagram | No | Diagram | — | — | Architect | Not Available |
| 10 | Authentication | Staff login with captcha + JWT | Yes | Repository | `BE/.../auth/service/AuthService.java`, `LoginCaptchaService.java`, `JwtTokenService.java` | — | Tech owner | Available |
| 11 | Authentication | MFA | No | — | — | — | Tech owner | Not Available |
| 12 | Authentication | Account lockout 5 attempts / 30 min | Yes | Configuration | `BE/src/main/resources/application.yml` (`app.auth`), `AuthService.registerFailedAttempt` | — | Tech owner | Available |
| 13 | Authentication | Password complexity | Yes | Repository | `BE/.../auth/dto/ResetPasswordRequest.java` | — | Tech owner | Available |
| 14 | Authentication | Password expiry | No | — | — | — | Tech owner | Not Available |
| 15 | Authorization | RBAC / permissions | Yes | Repository | `SecurityConfig.java`; 107 `@PreAuthorize`; `V2__create_user_management.sql`; `V26__seed_role_nav_permissions.sql` | — | Tech owner | Available |
| 16 | Authorization | Role matrix document | No | Document | — | — | PM | Not Available |
| 17 | Session | Token TTLs and revocation | Yes | Configuration | `application.yml` (`JWT_*_TTL`), `JwtTokenService.java` | — | Tech owner | Available |
| 18 | Audit | Audit trail + export | Yes | Repository / Screenshot | `BE/.../modules/audit/*`, `FE/src/features/audit` | — | Tech owner | Available |
| 19 | Logging | Sensitive data masking in audit | Yes | Repository | `AuditPayloadSanitizer.java`, `AuditPayloadSanitizerTest.java` | — | Tech owner | Available |
| 20 | Data | Database schema (DDL) | Yes | Repository | `BE/src/main/resources/db/migration/` (33 files) | — | Tech owner | Available |
| 21 | Data | ER diagram / data dictionary | No | Document | — | — | Tech owner | Not Available |
| 22 | Data | PII inventory | Yes (from DDL) | Repository | `V4__…sql`, `V5__profile_icsi_fields.sql`, `Profile.java` | — | Tech owner | Partially Available |
| 23 | Encryption | Password hashing BCrypt | Yes | Repository | `SecurityConfig.passwordEncoder()` | — | Tech owner | Available |
| 24 | Encryption | TLS in transit | No (in repo) | Configuration | — | — | Infra | Not Verified |
| 25 | Encryption | Encryption at rest | No (in repo) | Configuration | — | — | Infra | Not Verified |
| 26 | File security | Upload MIME/size validation | Yes | Repository | `RegistrationService.java`, `PhotographValidator.java`, `application.yml` (multipart 5 MB) | — | Tech owner | Available |
| 27 | File security | Malware scanning | No | — | — | — | Tech owner | Not Available |
| 28 | API security | Rate limiting | No | — | `RedisKeyNames.loginRateLimit` (unused) | — | Tech owner | Not Available |
| 29 | Testing | Backend automated tests | Yes | Repository | `BE/src/test/java` (21 classes, 81 tests) | — | Tech owner | Available |
| 30 | Testing | Frontend automated tests | No | — | — | — | Tech owner | Not Available |
| 31 | Testing | Load / performance test | Yes | Report | BE branch `origin/feature/loadTesting`: `load-tests/k6/reports/LOAD_TEST_REPORT.pdf` | 07-10-2026 | Tech owner | Available (merge to `main` pending) |
| 32 | VAPT | Latest VAPT report | No | Report | — | — | Security team | To be obtained |
| 33 | VAPT | Safe-to-host certificate | No | Certificate | — | — | Security team | To be obtained |
| 34 | CI/CD | Pipeline configuration | No | Configuration | — | — | DevOps | Not Available |
| 35 | Deployment | Dockerfile (non-root) | Yes | Configuration | `BE/Dockerfile` | — | DevOps | Available |
| 36 | Infra | Hosting / network / firewall / WAF / DDoS | No (in repo) | — | — | — | Infra | To be obtained |
| 37 | Backup / DR | Backup and DR evidence | No | Report / Log | — | — | Infra | To be obtained |
| 38 | Monitoring | Monitoring / alerting | Partial | Configuration | `application.yml` (`management.endpoints`) | — | DevOps | Partially Available |
| 39 | Integrations | Payment / KGID / SMS / SMTP | No (stubs) | Repository | `BE/.../candidateregistration/integration/Stub*.java` | — | Tech owner | Not Available (planned — SOW §4.18–4.21) |
| 40 | Policies | Organisation policies | No (in repo) | Policy | — | — | Compliance | To be obtained |
| 41 | Certifications | ISO / CMMI / CERT-In etc. | No (in repo) | Certificate | — | — | Compliance | To be obtained |
| 42 | Commercial | PO / work order / completion certificate | No | PO / Certificate | — | — | Commercial | To be obtained |

## E. DOCUMENT REGISTER

| Document | Status | Location |
|---|---|---|
| Statement of Work | Available (draft v1.0, unsigned) | `docs/Statement-of-Work.md`, `docs/Statement-of-Work.pdf` |
| Load test report | Available | BE branch `origin/feature/loadTesting`: `load-tests/k6/reports/LOAD_TEST_REPORT.{md,pdf,html}` |
| Backend project guide / coding conventions | Available | `BE/PROJECT_GUIDE.md`, `BE/AGENTS.md`, `BE/README.md` |
| Frontend structure / design system | Available | `FE/docs/PROJECT_STRUCTURE.md`, `FE/docs/DESIGN-SYSTEM.md`, `FE/docs/TANSTACK.md`, `FE/docs/SHADCN.md`, `FE/README.md` |
| API documentation | Available at runtime | `/swagger-ui.html`, `/v3/api-docs` |
| Translation hand-off sheets | Available | `docs/*.xlsx` |
| SRS / functional / technical specification | Not Available | — |
| Architecture diagrams | Not Available | — |
| ER diagram / data dictionary | Not Available | — |
| Policies | Not Available in project | Central compliance team |
| VAPT / audit reports, safe-to-host certificate | Not Available | Security / compliance team |
| DR / backup reports | Not Available | Infra team |
| PO / work order / completion certificate | Not Available | Commercial team |
| Certifications | Not Available in project | Central compliance team |

---

## F. GAPS

### F.1 Gap list

| # | Area | Gap | Category | Recommended action | Owner |
|---|---|---|---|---|---|
| 1 | Secrets | Default credentials and secret defaults committed in repository (see 25.2) | **Missing control — high priority** | Remove defaults, rotate all affected secrets, move to a secret manager, scan git history | Tech owner + DevOps |
| 2 | Access | Fixed default password for new staff and invigilator accounts defined in source code; no forced password change at first login | Missing | Generate random one-time passwords; enforce change on first login | Tech owner |
| 3 | Access | No MFA for administrators | Missing | Add TOTP/OTP second factor for Super Admin and Exam Admin | Tech owner |
| 4 | Access | No password expiry / history | Missing | Implement as per org password policy | Tech owner |
| 5 | Access | Staff password-reset OTP not delivered and held in memory | Partially available | Integrate SMS/email (SOW §4.19–4.20); store challenge in Redis/DB | Tech owner |
| 6 | Data | Aadhaar number and other PII stored unencrypted; no masking in DB | Missing | Field-level encryption or tokenisation of Aadhaar; review need to store full number (UIDAI rules) | Tech owner + Security |
| 7 | Data | 9 tables (incl. `audit_events`, `exam_ip_allowlist`, `reg_fee_master`, centre tables) have no Flyway migration | Needs update | Add migrations so `prod` (`ddl-auto: none`) can build the schema reproducibly | Tech owner |
| 8 | Data | No ER diagram / data dictionary | Missing | Generate from DB and maintain in `docs/` | Tech owner |
| 9 | Data | No retention, archival or purge mechanism (incl. audit logs) | Missing | Define with client; implement scheduled purge/archive | PM + Tech owner |
| 10 | Transport | TLS not configured for DB (`useSSL=false`), Redis, MinIO (`http`); dev URL over HTTP | Needs confirmation (Infra) | Enforce HTTPS/TLS end to end in UAT/prod | Infra |
| 11 | App security | No rate limiting on public endpoints (login, OTP, public catalogue) | Missing | Add rate limiting (gateway or application, using existing Redis key) | Tech owner |
| 12 | App security | Swagger UI / API docs public in all profiles | Needs update | Disable or protect in `prod` | Tech owner |
| 13 | App security | No Content-Security-Policy; tokens stored in browser storage | Partially available | Add CSP and security headers; consider httpOnly cookies | Tech owner |
| 14 | App security | No malware scanning of uploads; PDF type based on client header | Missing | Add AV scan (e.g. ClamAV) and magic-byte validation | Tech owner |
| 15 | App security | Plaintext OTP logged by stub SMS adapter; fixed OTP in dev profile | Needs update | Ensure stubs/fixed OTP cannot run in prod (profile guard) | Tech owner |
| 16 | SDLC | No CI/CD pipeline, automated build/test, SAST, dependency or container scanning | Missing | Add GitHub Actions with build, tests, SAST, SCA, image scan | DevOps |
| 17 | SDLC | No frontend automated tests; no UAT test cases / sign-off | Missing | Add unit/E2E tests; prepare UAT plan | Tech owner + QA |
| 18 | Repository | No tags/releases, no CODEOWNERS, commit standards not enforced | Missing | Semantic version tags per release, CODEOWNERS, commit convention | Tech owner |
| 19 | Repository | Branch protection and PR review approvals not verified | Needs confirmation | Export GitHub settings / PR review screenshots | GitHub admin |
| 20 | Repository | Load-test report only on a feature branch | Needs update | Merge to `main` or store in project documents | Tech owner |
| 21 | Repository | Compiled class file and ad-hoc SQL fix script committed (`scripts/CopyH2ToMysql.class`, `fix-flyway-failed-v2.sql`) | Needs update | Remove from repository or document purpose | Tech owner |
| 22 | Architecture | No architecture, deployment, network or integration diagrams | Missing | Prepare architecture pack | Architect |
| 23 | Integrations | Payment, KGID, SMS stubbed; SMTP not built | Missing (planned) | Deliver per SOW §4.18–4.21 | Tech owner + Client |
| 24 | Infra | Hosting, WAF, DDoS, firewall, backup, DR, monitoring, logging retention not evidenced | Needs confirmation from another team | Obtain from Infra/DevOps | Infra |
| 25 | Security assurance | No VAPT / CERT-In audit / safe-to-host certificate | Missing | Schedule CERT-In empanelled audit after gaps 1–16 | Security team |
| 26 | Governance | Policies, certifications, incident management, PO/completion documents not in project | Needs confirmation from another team | Obtain from compliance / commercial | Central team |
| 27 | Project | Owners (PM, architect, DevOps, security) not recorded | Missing | Fill Section 1 | PM |

### F.2 Summary by status

| Status | Areas |
|---|---|
| **Available** | Source repositories, technology stack, RBAC/permissions, staff and candidate authentication, lockout, password complexity, session expiry/revocation, audit trail with sanitisation, input validation, upload size/type checks, BCrypt/SHA-256/JWT, backend unit tests, load test report, SOW draft |
| **Partially available** | SOW (unsigned), branching (undocumented), monitoring (actuator only), secrets management, password reset, file upload security, security headers, coding standards, PII inventory |
| **Missing** | MFA, password expiry, CI/CD, security scanning, FE tests, architecture diagrams, ER diagram/data dictionary, encryption at rest for PII, rate limiting, malware scanning, retention/purge, release tags, VAPT, live integrations |
| **Needs update** | Flyway coverage, Swagger exposure, stub/OTP logging guard, committed secrets, load-test report location |
| **Needs confirmation from another team** | Hosting, TLS/certificates, WAF/DDoS/firewall, backup/DR, log retention, branch protection & PR approvals, policies, certifications, incident management, PO/contract |
| **Not applicable** | Mobile app, AI/ML, message brokers, third-party user access |

---

## 25. Repository Review — Mandatory Checks

### 25.1 Checklist

| Item | Present? | Location / note |
|---|---|---|
| README | Yes | `BE/README.md`, `FE/README.md` (local setup only) |
| package.json / pom.xml | Yes | `FE/package.json`, `BE/pom.xml` |
| Dockerfile | Backend only | `BE/Dockerfile` |
| docker-compose | Yes (local infra) | `BE/docker-compose.yml` |
| Kubernetes manifests / Helm charts | No | — |
| CI/CD pipelines | No | — |
| Environment configuration | Yes | `BE/src/main/resources/application{,-dev,-prod,-test,-local}.yml`, `BE/.env.example`, `BE/env.dev`, `FE/.env.example` |
| Infrastructure-as-Code | No | — |
| API documentation | Yes (generated) | springdoc OpenAPI |
| Database / migration scripts | Yes | `BE/src/main/resources/db/migration/` (33) |
| Authentication implementation | Yes | `BE/.../modules/auth`, `candidateregistration/security` |
| Authorization implementation | Yes | `SecurityConfig.java`, `@PreAuthorize`, `common/security` |
| Logging | Yes | `application.yml`, `CorrelationIdFilter.java` |
| Audit trail | Yes | `modules/audit` |
| Security configuration | Yes | `SecurityConfig.java` |
| Encryption configuration | Hashing only; no TLS/at-rest config | — |
| Certificate configuration | No | — |
| Third-party integrations | Stubs | `candidateregistration/integration` |
| Monitoring configuration | Actuator only | `application.yml` |
| Backup scripts | No | — |
| Deployment documentation | No (beyond local quick start) | — |

### 25.2 Secrets found in repository — report separately to Security/DevOps

Values are intentionally **not** reproduced here. All listed credentials should be treated as exposed and rotated if they are used in any shared environment.

| # | File (tracked in git) | Type of secret | Note |
|---|---|---|---|
| 1 | `BE/src/main/resources/application.yml` | Default values for JWT access and refresh signing secrets, Redis password, MinIO access/secret keys | Used whenever the environment variable is not set — risk of production running with known JWT keys |
| 2 | `BE/src/main/resources/application-dev.yml` | Default DB password, MinIO access/secret keys; dev host addresses | — |
| 3 | `BE/src/main/resources/application-local.yml` | Default DB password | — |
| 4 | `BE/env.dev` | Full dev environment file: DB credentials, MinIO keys, hosts | Should not be committed (only `.env.example` with placeholders) |
| 5 | `BE/.env.example` | Contains real-looking DB/MinIO/Redis credentials instead of placeholders | Replace with placeholders |
| 6 | `BE/docker-compose.yml` | MySQL user/root passwords, Redis password, MinIO root credentials | Local development only — confirm not reused elsewhere |
| 7 | `BE/README.md` | MinIO console default login | Local default |
| 8 | `BE/.../usermanagement/service/UserAccountService.java` | Fixed default staff password constant | Applied to issued staff logins |
| 9 | `BE/.../candidateregistration/service/InvigilatorRegistrationService.java` | Fixed default invigilator password constant | Applied to approved invigilators |

Recommended: rotate affected secrets, remove defaults from tracked files, add secret scanning (e.g. GitHub secret scanning / gitleaks) and purge from git history if required by the security team.

---

_End of submission. Items marked "To be obtained" must be completed by the named teams before consolidation into the HDFC Vendor Assessment checklist._
