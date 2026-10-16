 BDA_Grievnace - Project & Repository Data CollectionDFC

**Project:** BDA Grievance Redressal Portal
**Prepared from:** Repository review of `bda-grievance-backend` and `bda-grievance-frontend` (local clones, all branches fetched)
**Review date:** 08-10-2026
**Prepared by:** _<Name – Repository/Technical Owner>_ (to be filled)
**Reviewed by:** _<Project Manager / Security Owner>_ (to be filled)

> **Method.** Every statement below was verified against the repository (source code, configuration, git history) unless marked otherwise. File references are relative to the repository root named in the row. Items that cannot be verified from the repository are marked **Not Verified** or **To be obtained from another team**. No passwords, keys, tokens or personal data are reproduced in this document.
>
> **Classification legend:** `[Project]` project-level · `[Org]` organization-level · `[Client]` client-specific · `[Infra]` infrastructure-level · `[SecTeam]` security-team controlled
>
> **Status legend:** Available · Partially Available · Not Available · Not Applicable · To be obtained from another team · Not Verified

---

## ⚠️ Items to report separately to Security / DevOps (do NOT include values in this assessment)

These were found during the mandatory repository review (Section 25). Values have **not** been copied anywhere.

| # | Issue | Location | Severity (indicative) | Action |
|---|---|---|---|---|
| S1 | Environment files with non-empty secret variables are **committed to git** (on `main`) — `DB_PASSWORD`, `JWT_SECRET`, `S3_SECRET_ACCESS_KEY`, `EXTERNAL_API_KEY`; `.env.dev` additionally has `SMS_USERNAME/SMS_PASSWORD/SMS_SECURE_KEY`, `MINIO_SECRET_KEY` | backend: `.env.dev`, `.env.uat`, `.env.prod` (tracked since 2025-09-23 commit "Initial commit with Husky setup"); `env.example` also contains real-looking values | Critical | Rotate all affected credentials; remove from repo and purge history; confirm which values are live |
| S2 | Hardcoded MongoDB Atlas connection string with credentials | backend branch `origin/feature/chatbot`: `chatbot/backend/src/app.module.ts:24` | Critical | Rotate credential; purge branch history |
| S3 | Hardcoded secrets/defaults in source: JWT fallback secret, default staff password, fixed citizen OTP | backend: `src/common/auth/strategies/jwt.strategy.ts:24`, `src/common/core/constants/user.constants.ts:8`, `src/common/user/service/user.service.ts:973`, `src/citizen/services/citizen.service.ts:41` | Critical | Remove; move to secret store |
| S4 | Real citizen PII committed to git (names, mobile numbers, addresses, grievance text) | backend: `BDA_EAST.xlsx`, `BDA_west.xlsx`, `BDA_UPDATE_NORTH.xlsx`, `bda_updated_south.xlsx`, `zone_data_jan25.sql`, `zone-data-new (1).sql`, `insert_existing_raise_grievance*.sql`, `scripts/master.sql`, `scripts/insert_*.sql`, `scripts/BDA Helpline Master Sheet From 01.07.2025.xlsx` | High (DPDP Act exposure) | Remove from repo and history; confirm repository visibility/access list |
| S5 | 168 citizen grievance attachments (PDF/images/audio/video) committed to git | backend: `uploads/` (incl. `uploads/voice/`) | High | Remove from repo and history |

---

# A. PROJECT INFORMATION

## 1. Project Identification

| Field | Value | Source / Evidence | Status |
|---|---|---|---|
| Project Name | BDA Grievance Redressal Portal (BDA Grievance Management System) | frontend `src/locales/en.json` → `homePage.portalTitle`; frontend `BDA_GRIEVANCE_CASE_STUDY.md` | Available |
| Client / Department | Bangalore Development Authority (BDA), Government of Karnataka | frontend `BDA_GRIEVANCE_CASE_STUDY.md`; footer text in `src/pages/HomePage.tsx`; SMS gateway `smsmobileone.karnataka.gov.in` | Available `[Client]` |
| Industry / Domain | Government – Urban Development / Public Grievance Redressal | Case study doc | Available |
| Project Type | **Government** | — | Available |
| Project Start Date | Backend repo first commit **23-09-2025**; frontend repo first commit **29-12-2025** (contractual start date not in repo) | `git log --reverse` in both repos | Partially Available – contractual date to be obtained from PM |
| Project End Date / Current Status | **Ongoing – active development.** Latest commits: backend 05-10-2026, frontend 08-10-2026 | `git log` | Available |
| Project Duration | ~12.5 months to date (Sep-2025 → Oct-2026) by commit history | git history | Partially Available |
| Current Production Status | **Not Verified from repo.** Indicators: `prod` branch exists in both repos (last updated 11-02-2026); `release/uat` last updated 24-09-2026; code falls back to public URL `grievance.bdakarnataka.in` (`src/raiseGrievance/service/reportScheduler.service.ts`) | git branches; source | To be obtained from PM / DevOps |
| Environments | local, dev, uat, prod configuration files exist | backend `.env.local` (untracked), `.env.dev`, `.env.uat`, `.env.prod`; `package.json` scripts `build:dev/uat/prod` | Partially Available – actual hosted URLs/servers to be obtained from DevOps |
| Repository Name(s) | `bda-grievance-backend`, `bda-grievance-frontend` | `git remote -v` | Available |
| Repository URL | `github.com/Inventechinfosolutions/bda-grievance-backend`, `github.com/Inventechinfosolutions/bda-grievance-frontend` | `git remote -v` | Available |
| Repository Type | **GitHub** (organization `Inventechinfosolutions`) | `git remote -v` | Available |
| Repository Owner / Technical Owner | GitHub org: Inventech Info Solutions. Top contributors: Srinath R (backend 137 / frontend 163 commits), AnilKishoreDR / Anil Kishore (160 / 134), srinathinvent45, Sushmitha, shiva Reddy, Harsha Gowda | `git shortlog -sn --all` | Partially Available – named owner to be confirmed |
| Project Manager | — | Not in repo | To be obtained from PMO |
| Solution Architect | — | Not in repo | To be obtained from PMO |
| DevOps / Infrastructure Owner | — | Not in repo | To be obtained from DevOps |
| Security Owner | — | Not in repo | To be obtained from Security team |

---

## 2. Project Scope

**Business objective** (source: frontend `BDA_GRIEVANCE_CASE_STUDY.md`): Replace paper/email/spreadsheet handling of BDA citizen grievances with a single digital workflow providing traceability, zone-wise routing, SLA tracking, Open House Meeting (OHM) scheduling and SMS notification at every stage.

**Major business processes / workflows** (verified in backend `src/raiseGrievance`, `src/zonalApplications`, `src/scheduledApplication`, `src/grievanceNodalHistory`):
1. Citizen registers grievance (mobile + OTP) or Helpdesk/Tapal registers on behalf of citizen
2. Helpdesk verification → zone assignment (North / South / East / West)
3. Zone Commissioner decision / hearing; Zone Officer action; Nodal Officer escalation
4. OHM (Open House Meeting) scheduling with slot management, rescheduling, postponement
5. Closure, reopen, send-back, reassign, escalation (SLA: 30 days general / 7 days urgent)
6. Legacy ("Existing") grievance digitisation and management
7. MIS generation and daily report SMS

**Major modules**

| Module | Backend location | Frontend location |
|---|---|---|
| Citizen (OTP login, register, status) | `src/citizen`, `src/raiseGrievance` | `src/modules/citizen` |
| Tapal / Helpdesk | `src/helpdesk`, `src/raiseGrievance` | `src/modules/tapal` |
| Zonal (Zone Commissioner) | `src/zonalApplications`, `src/modules/zone` | `src/modules/zonal` |
| Zone Officer | `src/scheduledApplication` | `src/modules/zone-officer` |
| Nodal Officer | `src/grievanceNodalHistory` | `src/modules/nodal-officer` |
| Central / CAC | `src/raiseGrievance` | `src/modules/central`, `src/modules/cac` |
| OHM scheduling + public calendar | `src/scheduledApplication` | `src/modules/public`, `src/modules/zonal` |
| Management / User admin (person, post, permissions) | `src/userAdmin`, `src/common/user` | `src/modules/personal`, `src/modules/auth` |
| Master data (zones, holidays, locations, etc.) | `src/master` | `src/modules/master-data` |
| MIS reports / exports | `src/modules/zone`, `src/raiseGrievance` | MIS generator pages |
| SMS gateway & templates | `src/sms-gateway` | — |
| Documents (upload/download) | `src/common/document-uploader`, `src/common/s3-client` | — |

**User types** (backend `src/common/user/enums/userTypes.enum.ts`): CITIZEN, AGENT, TEAMLEAD (Tapal/Helpdesk), ZONE_COMMISSIONER, ZONE_OFFICER, NODAL_OFFICER, ADMINISTRATOR, ADMIN, SUPER_ADMIN, AUDITOR, LAC_JOINT_DIRECTOR, LAC_SENIOR_DEPUTY_DIRECTOR.

**Approximate number of users:** Not Verified. Legacy data volume reference: ~7,467 helpline records (backend `scripts/excel_to_sql_summary.md`). Grievance series configured to start at 6000 (`scripts/set-grievance-series-to-6000.sql`). → *Production user/grievance counts to be obtained from DB owner / PM.*

| Scope item | Details | Evidence | Status |
|---|---|---|---|
| External systems integrated | Karnataka Mobile Seva SMS gateway; MinIO (S3-compatible) object storage | backend `src/sms-gateway/services/sms-gateway.service.ts:21-22`; `src/common/s3-client/s3-client.service.ts` | Available |
| APIs exposed | REST API, global prefix `/api/v1`; **319 live endpoints** across 52 controllers (157 GET, 64 POST, 59 PUT, 1 PATCH, 38 DELETE); 68 endpoints without authentication (see §10) | backend controllers under `src/**/controller*`; `src/main.ts` | Available |
| APIs consumed | SMS gateway (HTTP form POST) | `sms-gateway.service.ts` | Available |
| Major reports / dashboards | Role dashboards, MIS generator (New & Existing grievance), Excel exports (ExcelJS), PDF exports (Puppeteer), daily report PDF via SMS link | backend `src/modules/zone/service/zone.service.ts`, `src/raiseGrievance/service/reportScheduler.service.ts` | Available |
| Mobile application | None (responsive web only) | No mobile project in repos | Not Applicable |
| Web application | React SPA (English + Kannada) | frontend repo | Available |
| Backend services | Single NestJS modular monolith | backend repo | Available |
| Batch / scheduled jobs | (1) SLA remaining-days sync 23:45 IST daily (MySQL `GET_LOCK` for single-run); (2) Daily grievance report PDF + SMS 08:00 IST | backend `src/raiseGrievance/service/grievanceRemainingDaysScheduler.service.ts:34-37`; `reportScheduler.service.ts:65-84` | Available |
| Notification services | SMS only (DLT templates in `sms_template` table). No email/WhatsApp/push | `src/sms-gateway/models/sms-template.entity.ts`; `scripts/insert-all-sms-templates.sql` | Available |
| File / document processing | Uploads (documents, images, voice, video) to MinIO; PDF generation (Puppeteer); Excel export (ExcelJS) | `s3-client.service.ts`; `src/common/core/utils/puppeteer-launch.util.ts` | Available |
| AI/ML components | **None on `main`.** A separate chatbot sub-project using Google Gemini + MongoDB exists only on branch `feature/chatbot` (not merged) | `git ls-tree origin/feature/chatbot` (72 files under `chatbot/`) | Not Applicable (main) / Needs confirmation |
| Requirements / SRS / SOW | Not in repo | — | To be obtained from PMO |
| Architecture document | Not in repo (only `docs/STAFF_USER_POST_PERSON_LOGIN_MODEL.md` – login data model note) | backend `docs/` | Not Available |
| Functional specification | Partial: frontend `BDA_GRIEVANCE_CASE_STUDY.md`, `EXISTING_GRIEVANCE_FLOW_ANALYSIS.md` | frontend repo | Partially Available |
| Technical specification | Partial: frontend `API_SPECIFICATION.md` (early, single endpoint), backend `POSTMAN_GUIDE.md`; Swagger generated at runtime (`/api/docs`, dev only) | — | Partially Available |

---

# B. TECHNOLOGY & ARCHITECTURE

## 3. Technology Stack (verified against `package.json`, lock files and installed `node_modules`)

### Frontend `[Project]` — source: frontend `package.json`, `package-lock.json`

| Item | Value |
|---|---|
| Framework | React **19.2.3** (SPA, `BrowserRouter`) |
| Language | TypeScript **5.9.3** (`strict: true` in `tsconfig.app.json`) |
| Build tool | Vite **7.3.0** (`@vitejs/plugin-react` 5.1.2) |
| Package manager | npm (lockfileVersion 3) |
| Routing | react-router-dom 7.11.0 (114 routes in `src/App.tsx`) |
| State management | Redux Toolkit 2.11.2 + react-redux 9.2.0; @tanstack/react-query 5.90.14 |
| UI | Tailwind CSS 3.4.19, hand-written shadcn-style components (`src/components/ui`), lucide-react 0.562.0 |
| HTTP | axios 1.13.2 (`src/lib/api.ts`) |
| i18n | react-intl 8.0.10 (English `en.json`, Kannada `kn.json`) |
| Charts / docs | chart.js 4.5.1, jspdf 4.2.0 + autotable, exceljs 4.4.0, xlsx 0.18.5 |
| Other | libphonenumber-js; zod/react-hook-form installed but unused |
| Dependency flags | `xlsx` 0.18.5 has known public advisories; `express.js` 1.0.0 (unofficial, unused package) present in dependencies |

### Backend `[Project]` — source: backend `package.json`, `node_modules`

| Item | Value |
|---|---|
| Framework | NestJS **10.4.20** (core/common/platform-express); some v11 packages mixed (`@nestjs/jwt` 11.0.2, `@nestjs/passport` 11.0.5, `@nestjs/typeorm` 11) |
| Language | TypeScript ^5.1.3 |
| Runtime | Node.js 20 (Docker `node:20-alpine`); no `engines` field |
| Architecture | Modular monolith, REST, Controller → Service → TypeORM Repository |
| ORM / DB driver | TypeORM 0.3.27, mysql2 3.15.0 |
| Auth | @nestjs/jwt, passport-jwt 4.0.1, bcrypt 6.0.0 |
| Security | helmet 8.1.0, @nestjs/throttler 6.5.0, class-validator 0.14.2, eslint-plugin-security (dev) |
| Documents | puppeteer 24.34 (PDF), exceljs 4.4 |
| Storage SDK | @aws-sdk/client-s3 (transitive via `@nxtworkforce/s3-service`) → MinIO |
| Scheduling | @nestjs/schedule 4.1.2 + cron 3.2.1 (**installed locally but missing from `package.json`/lock** – build risk) |
| Monitoring | prom-client 15.1.3 |
| Logging | winston 3.19 via private package `@inventech/nxtworkforce-common-service` (pinned to `latest`) |
| Transactions | typeorm-transactional 0.5 |

### Database `[Project]`

| Item | Value | Evidence |
|---|---|---|
| Technology | MySQL (InnoDB, utf8mb4) | `src/config/database.config.ts:75`; SQL scripts |
| Version | 8.0.42 (from dump header) | `zone_data_jan25.sql` header |
| Type | Relational | — |
| Number of databases | 1 application schema | `DB_NAME` in env config |
| Tables / entities | 54 TypeORM entities (53 registered) | `src/config/database.config.ts:81-148` |
| Schema management | `synchronize: false`; 3 TypeORM migrations + manual SQL scripts in `scripts/` | `database.config.ts:150`; `src/migrations/` |

### Other technologies — verification matrix

| Technology | Used? | Evidence |
|---|---|---|
| Redis | **No (configured but disabled).** `RedisModule` commented out; cache is in-memory per process. Health check only pings Redis TCP | backend `src/app.module.ts:78-87`; `src/health/health.service.ts` |
| Elasticsearch / Typesense | No | Not found |
| Qdrant / vector DB | No | Not found |
| MinIO / object storage | **Yes** – MinIO via S3 SDK | `src/common/s3-client/s3-client.service.ts` |
| Kafka / RabbitMQ / queues | No | Not found |
| API Gateway | Not found in repo | To be confirmed by DevOps |
| Nginx / reverse proxy | Not found in repo (`TRUST_PROXY=true` in `.env.prod` implies a proxy) | To be confirmed by DevOps |
| Istio / Kubernetes / Helm | No manifests in repo | Not found |
| Docker | **Yes** – backend `Dockerfile` (multi-stage, non-root), `docker-compose.yml` (app + Prometheus). Frontend has no Dockerfile | backend repo root |
| Jenkins / GitHub Actions / Argo | **None in repo** | No pipeline files in either repo |
| Monitoring | Prometheus (`prometheus-config.yml`, `/api/v1/metrics`) | backend repo |
| Logging | winston JSON file logs (`./logs/app.log`) | `src/app.module.ts:45-55` |
| SIEM / WAF / DDoS | Not found in repo | To be obtained from Infra/Security team |
| Cloud services | Not found in repo | To be obtained from DevOps |
| Third-party services | Karnataka Mobile Seva SMS (Govt.) | `sms-gateway.service.ts` |

---

## 4. Architecture

**Architecture documents:** Not Available in repo. **Gap** – application, deployment, network, data, authentication and security architecture diagrams must be produced or obtained from the Solution Architect / DevOps.

**Application architecture (derived from code – for drafting the diagram):**

```
Citizen / Officer browser
   │  HTTPS (termination point Not Verified)
   ▼
React SPA (Vite build, static hosting – host Not Verified)
   │  REST /api/v1  (Bearer JWT; refresh cookie)
   ▼
NestJS API (Docker, node:20-alpine, port 3100)
   ├── MySQL 8 (host.docker.internal:3306)
   ├── MinIO object storage (host.docker.internal:9000)
   ├── Local disk: storage/report-links (daily report PDFs)
   ├── Karnataka Mobile Seva SMS gateway (HTTP, outbound)
   └── /api/v1/metrics ← Prometheus (docker-compose)
```

| Component | Identified | Evidence | Status |
|---|---|---|---|
| Application server | NestJS container, port 3100 | backend `Dockerfile:41`, `docker-compose.yml` | Available |
| Web server (frontend) | Not in repo (SPA needs server fallback to `index.html`) | — | To be obtained from DevOps |
| API gateway / load balancer | Not in repo | — | To be obtained from DevOps |
| Database | MySQL 8 on Docker host (`host.docker.internal`) per `.env.prod` | `.env.prod` (host names only) | Partially Available |
| Cache | In-memory (cache-manager, no store) | `CacheModule.register()` in modules | Available |
| File / object storage | MinIO | `s3-client.service.ts` | Available |
| Message broker | None | — | Not Applicable |
| External integrations | SMS gateway | — | Available |
| Identity provider | None (application-managed users + JWT) | `src/common/auth` | Available |
| Monitoring | Prometheus (no alert rules) | `prometheus-config.yml` | Partially Available |
| Security components (WAF/IDS) | Not in repo | — | To be obtained from Infra/Security |
| Cloud / on-premise | Not determinable from repo | — | To be obtained from DevOps |

---

## 5. Repository & Development Practices

| Item | Finding | Evidence | Status |
|---|---|---|---|
| Repository structure | Backend: NestJS `src/` by domain module, `scripts/`, `docs/`, `test/`. Frontend: `src/modules/<role>`, `src/store`, `src/locales`, `src/components/ui` | repo trees | Available |
| Branching strategy | Feature branches `feature/*`, `bug/*` → PR into `main`; `release/uat` and `prod` branches exist | `git branch -a` (backend ~70 remote branches, frontend ~75) | Available (informal; no written policy) |
| Dev / UAT / Prod branches | `main` (dev integration), `release/uat` (last: BE 24-09-2026, FE 24-09-2026), `prod` (last: **11-02-2026** both repos) | `git log -1 origin/prod`, `origin/release/uat` | Available – **prod branch appears stale; confirm actual production release source** |
| Pull request process | GitHub PRs used. Backend PRs #1–#197; frontend PRs #1–#224. 157 PR merges on backend `main`, 221 on frontend `main` | `git log --merges` ("Merge pull request #…") | Available |
| Code review / merge approval | PR merges performed via GitHub UI. **Reviewer approvals cannot be verified from git** | GitHub PR history | To be verified on GitHub (screenshots of PR reviews) |
| Branch protection | **Not enforced historically**: direct (non-PR) commits on `main` – backend 25 (latest 19-02-2026), frontend 90 (latest 07-09-2026) | `git log origin/main --first-parent --no-merges` | **Gap** – confirm/enable GitHub branch protection |
| Commit standards | commitizen configured (`npm run commit`), but only 2 of 230 backend commits follow conventional format; no commit-msg hook | backend `package.json`; `.husky/` | Partially Available |
| Pre-commit quality gate | Backend: husky + lint-staged → ESLint (incl. `eslint-plugin-security`) + Prettier. Frontend: **none** (no ESLint/Prettier config) | backend `.husky/pre-commit`, `.eslintrc.js`; frontend repo | Partially Available |
| Release process / versioning | No tags, no CHANGELOG; `package.json` versions `1.0.0` (BE) / `0.0.0` (FE) never bumped | `git tag` (empty) | **Not Available** |
| Tagging strategy | None | `git tag` | Not Available |
| Code ownership | No `CODEOWNERS` file | `git ls-files` | Not Available |
| Repository access controls | GitHub org-level; not verifiable from clone | — | To be obtained (GitHub org admin screenshot) |
| Evidence – PRs | Yes | GitHub PR list | Available |
| Evidence – code reviews / approvals | Not verifiable locally | — | To be verified on GitHub |
| Evidence – release history | No tags/releases | — | Not Available |
| Evidence – deployment history | No CI/CD; not in repo | — | To be obtained from DevOps |

---

## 6. SDLC & Development Process

| Area | Finding | Evidence | Status |
|---|---|---|---|
| Requirement management | Not in repo (tool e.g. Jira not referenced) | — | To be obtained from PM |
| Development process | Feature branch + PR to `main`, promotion to `release/uat` / `prod` | git history | Partially Available |
| Code review | PR-based (approval evidence on GitHub) | — | To be verified |
| Unit testing | **Effectively none**: 2 spec files with a single "should be defined" test each; frontend has no tests | backend `src/common/s3-client/s3-client.service.spec.ts`, `src/series-generator/services/series-generator.service.spec.ts` | **Gap** |
| Integration / E2E testing | 1 template e2e file (`test/app.e2e-spec.ts`), stale (expects `status: 'ok'`) | backend `test/` | **Gap** |
| System testing / UAT | `release/uat` branch and `.env.uat` exist; UAT sign-off not in repo | — | To be obtained from QA/PM |
| Security testing | ESLint security plugin only (static lint). No SAST/DAST/dependency scanning pipelines | `.eslintrc.js` | **Gap** |
| Performance testing | Not found | — | Not Available |
| Release / change management | No documented process, tags or change tickets in repo | — | To be obtained from PM |
| Production deployment | No deployment scripts/pipelines in repo; manual process presumed | — | To be obtained from DevOps |
| Rollback process | Not documented | — | Not Available |
| Defect management | Not in repo (branch names like `feature/updated_bugs` suggest tracking) | — | To be obtained from QA |
| SDLC policy / coding standards | Org-level documents not in repo; repo-level: ESLint + Prettier (backend only) | — | To be obtained from Org/QA `[Org]` |

---

# C. SECURITY ASSESSMENT

## 7. Authentication & User Access Management

| Control | Actual implementation | Evidence (backend unless stated) | Status |
|---|---|---|---|
| Staff authentication | Login ID + password (bcrypt) → JWT | `src/common/user/controller/public.controller.ts:35-68`; `src/common/user/service/user.service.ts:124-283` | Available |
| Citizen authentication | Mobile + 4-digit SMS OTP → JWT. **Legacy endpoint `POST /citizen/login` accepts a hardcoded fixed OTP for any mobile number** | `src/citizen/services/citizen.service.ts:41, 66-269, 290` | **Gap – Critical** |
| Token mechanism | JWT HS256 (default; algorithm not pinned). Access token default 1h; refresh token default 7d, rotated, stored in httpOnly `sameSite=strict` cookie | `src/common/auth/auth.service.ts:38-54`; `src/common/auth/strategies/jwt.strategy.ts:15-26` | Available |
| Frontend token storage | Access + refresh tokens persisted in `sessionStorage` (XSS-readable); no refresh flow implemented | frontend `src/store/reducers/publicLoginReducer.ts:85-88`; `publicGrievanceReducer.ts:38-41`; `src/lib/api.ts` | Partially Available |
| Authorization mechanism | `JwtAuthGuard` + `@Permissions()` decorators + `PermissionsGuard`. **`PermissionsGuard.canActivate` always returns `true`** (logic commented out) – permission decorators are not enforced | `src/common/auth/guards/permissions.guards.ts:23-61` | **Gap – Critical** |
| RBAC data model | Tables `role`, `permission`, `role_permission`, `role_menu`, `post_permission`, `post_permission_limit`; permissions loaded into JWT at login | `src/common/user/models/*`, `src/userAdmin/models/*`; `user.service.ts:323-358` | Partially Available (model exists, not enforced) |
| Roles available | See §2 user types (12 roles) | `src/common/user/enums/userTypes.enum.ts` | Available |
| Role–permission matrix | **No seed/migration defining it; stored only in DB** | — | **Not Available** – export from production DB |
| Frontend route protection | **No route guards**; role routing only at login; 401 from API redirects to login | frontend `src/App.tsx` (114 routes), `src/lib/api.ts:130-206` | **Gap** |
| Admin / privileged users | SUPER_ADMIN, ADMINISTRATOR, ADMIN. "Mimic" (impersonation) endpoint `GET /user/mimic/:id` available to any authenticated user (write methods blocked for mimic tokens) | `src/common/user/controller/user.controller.ts:307-319`; `jwt.strategy.ts:44-56` | **Gap** |
| MFA | **Not implemented for staff/admin**. Citizens: OTP (single factor) | — | **Not Available** |
| Password hashing | bcrypt, cost 10 | `user.service.ts:102` | Available |
| Password complexity | Strong rule (10–16 chars, upper/lower/digit/symbol) exists but only used in a disabled endpoint; active change/reset flows require only 6–20 chars | `src/common/core/utils/utilites.util.ts:45-77`; `user.service.ts:760-778, 941-951` | Partially Available |
| Password expiry / history | Not implemented (`lastPasswordChanged` stored, not checked) | — | Not Available |
| Failed login attempts / lockout | Not implemented (`LOCKED` status exists but not checked at login; login does not check user status) | `user.service.ts:124-283`; `src/common/user/enums/userStatus.enum.ts` | **Not Available** |
| Session timeout | Access token expiry only (1h prod config); no idle timeout on frontend | `.env.prod` `JWT_EXPIRES_IN`; frontend | Partially Available |
| Concurrent sessions | Not controlled | — | Not Available |
| Password reset | OTP-based forgot-password (6-digit, 10-min TTL, in-memory). **Also `POST /user/reset-password` and `PUT /user/auto-reset-password` have no authentication guard** (reset by email without verification; auto-reset to default password) | `public.controller.ts:70-113`; `user.controller.ts:213-255`; `user.service.ts:656-717` | **Gap – Critical** |
| First-login password change | Flag returned to UI, not enforced server-side | `user.service.ts:112, 261-263` | Partially Available |
| User provisioning / de-provisioning | Via Management module: person → post → post-person mapping (start/end dates) creates/maps login | `docs/STAFF_USER_POST_PERSON_LOGIN_MODEL.md`; `src/userAdmin` | Available (mechanism); records to be obtained |
| Activation / deactivation | `status` enum (ACTIVE/INACTIVE/LOCKED/SUSPENDED) – **not enforced at login** | `userStatus.enum.ts` | Partially Available |
| CAPTCHA | **Not implemented** (captcha table dropped; DTO fields ignored) | `src/migrations/1756117800000-DropCaptchaTable.ts`; `src/common/user/dto/userLogin.dto.ts:22-31` | Not Available |
| Logout / revocation | Refresh-token blacklist (in-memory + DB). Defects: TTL unit mismatch (seconds vs ms), DB→cache sync key mismatch; `GET /public/logout` unauthenticated | `src/common/auth/services/blackListToken.service.ts`; `public.controller.ts:115-190` | Partially Available |
| Login history | `login_history` (login/logout time, user, post); no IP/user-agent; failed logins not recorded | `src/common/user/models/loginHistory.entity.ts` | Partially Available |
| Third-party user access / PAM / periodic access review | Not found | — | To be obtained from Security/PM |

**Evidence still required:** application screenshots of login/OTP/role management; production role–permission export; access-review and onboarding/offboarding records.

---

## 8. Data Model & Data Dictionary

| Item | Status | Notes / Evidence |
|---|---|---|
| ER diagram | **Not Available** | Can be generated from entities / DB (e.g., MySQL Workbench reverse-engineer) |
| Data dictionary | **Not Available** | Entities are the only source: 54 files `src/**/models/*.entity.ts`, `*.model.ts` |
| Database schema (DDL) | Partially Available | No baseline migration; schema = entities + manual SQL (`scripts/create-*.sql`, `scripts/alter-*.sql`) + 3 migrations. Full DDL to be exported from DB |
| Primary keys | Available | Mix of auto-increment INT and UUID |
| Foreign keys | Partially Available | Only 5 TypeORM relations declared (e.g., `raise_grievance_status_history`, `grievance_nodal_history`, `schedule_details`, `raise_zonal_applications` → `raise_grievance`); most links are plain ID columns without FK constraints |
| Audit columns | Available | `createdBy/createdAt/updatedBy/updatedAt` via `src/common/core/models/base.entity.ts` (not on `users`, `login_history`, `report_links`) |
| Soft delete | Not Available | No `@DeleteDateColumn`; hard deletes used |

**Important entities & sensitive fields**

| Table | Purpose | Sensitive data |
|---|---|---|
| `raise_grievance` | Core grievance | **PII:** citizen name, mobile, email, address, applicant image, voice/video/document paths, layout/property details |
| `existing_raise_grievance`, `zone_data`, `grievence_master_data` | Legacy grievances | **PII:** name, contact, address, email |
| `citizen` | Citizen login | **PII:** mobile; **Auth:** `otpcode` stored in **plaintext**, no expiry |
| `users` | Staff/citizen login accounts | **Auth:** bcrypt password hash, `randomPassword` column; email; login timestamps |
| `user_admin_user` | Legacy users | **Auth:** password |
| `personal_details` | Staff profile | **Staff PII:** name, email, mobile, gender |
| `post_details`, `post_person_mapping`, `post_permission` | Org structure & access | Access-control data |
| `sms_audit` | SMS log | **PII:** mobile; full message text incl. **OTPs in plaintext** |
| `raise_grievance_status_history`, `grievance_nodal_history`, `login_history` | Audit | Audit data |
| `blacklistedtokens`, `user_admin_blacklisted_tokens`, `report_links` | Tokens | **Auth:** JWTs / public link tokens (no expiry on `report_links`) |
| `object_store` | Document metadata | person name, file references |
| `master_*` (≈22 tables) | Reference data | Non-sensitive |

**Financial data:** None (no payment integration). **Aadhaar:** Not collected.

---

## 9. Data Storage & Handling

| Area | Finding | Evidence | Status |
|---|---|---|---|
| Where data is stored | MySQL (structured), MinIO (documents/media), local disk (`storage/report-links` PDFs; logs) | `.env.prod` hosts; `reportScheduler.service.ts:144-145` | Available |
| On-prem / cloud / hybrid | Not determinable from repo (`host.docker.internal` = same Docker host) | — | To be obtained from DevOps |
| Encryption at rest – DB | No application-level/field encryption. DB-level (TDE/disk) Not Verified | No `createCipheriv`/AES in code | **Not Verified** – Infra |
| Encryption at rest – objects | Not configured in code (no SSE parameters) | `s3-client.service.ts` | Not Verified – Infra |
| Encryption in transit – browser↔API | App listens on plain HTTP; TLS presumed at proxy – Not Verified | `src/main.ts:166-167` | To be obtained from DevOps |
| Encryption in transit – API↔DB | SSL enabled only if `NODE_ENV==='production'` (never true – all env files set `NODE_ENV=local`); when enabled `rejectUnauthorized:false`; `DB_SSL_CA` empty | `src/config/database.config.ts:71,170-177`; `.env.prod:13` | **Gap** |
| Encryption in transit – API↔MinIO | `S3_SSL_ENABLED=false` in all env files | env files (flag only) | **Gap** |
| Encryption in transit – API↔SMS gateway | **Plain HTTP** | `sms-gateway.service.ts:21-22` | **Gap** |
| Key / secret management | `.env` files via `@nestjs/config`; no vault/KMS; secrets committed (see S1) | `src/app.module.ts:32-44` | **Gap** |
| Backup (frequency/type/location/retention/logs/restore test) | **No backup scripts or configuration in repo** | — | To be obtained from DevOps/DB admin |
| Archival policy/process | None in code | — | Not Available |
| Data retention | No retention configuration or jobs (grievances, `sms_audit`, `login_history`, logs, report PDFs are kept indefinitely) | — | **Not Available** |
| Data purging | No purge jobs; hard deletes in ~30 service methods without approval workflow | — | Not Available |
| Log storage | `./logs/app.log`, append-only, **no rotation/retention** implemented in the logger package | `@inventech/nxtworkforce-common-service` logger; `docker-compose.yml` mounts `./logs` | **Gap** |

---

## 10. Application Security Controls

| Control | Implementation | Evidence (backend unless stated) | Assessment |
|---|---|---|---|
| Input validation | Global `ValidationPipe` (`whitelist`, `forbidNonWhitelisted`, `transform`); class-validator DTOs | `src/main.ts:100-106` | Implemented (a few bypasses with `any` bodies) |
| SQL injection | TypeORM QueryBuilder/parameterised raw queries; `multipleStatements:false`. One unvalidated sort field interpolated into `orderBy` | `src/userAdmin/services/postDetails.service.ts:849-851` | Mostly implemented – 1 finding |
| XSS (server) | Custom `@NoScriptTags` regex validator on some DTOs only | `src/common/core/validators/no-script-tags.validator.ts` | Partial |
| XSS (client) | **21 `dangerouslySetInnerHTML` usages rendering grievance HTML without sanitiser** (no DOMPurify) | frontend e.g. `ZonalInbox.tsx`, `TapalDashboard.tsx`, `CitizenGrievanceDetails.tsx` | **Gap – High** |
| Authentication | JWT (see §7) | — | Implemented with gaps |
| Authorization / RBAC | Permission guard is a no-op; ~52 endpoints unintentionally unauthenticated, incl. role/permission admin (`/role`, `/permission`, `/role-permission`, `/users`), `/sms/*` (open SMS relay), `/document-uploader/*` (upload/download/delete), `/citizen/:id` GET/PUT/DELETE, `/grievance-history` PUT/DELETE, `/zone-data` reads with PII, `/user/report`; no record-ownership checks (IDOR) on grievance by id | controllers listed in §2/§7; e.g. `src/sms-gateway/controllers/sms-gateway.controller.ts:15`, `src/common/document-uploader/controller/document-uploader.controller.ts:35`, `src/citizen/controller/citizen.controller.ts:208-236` | **Gap – Critical** |
| Session management | See §7 | — | Partial |
| Password security | bcrypt; weak policy on active flows; plaintext password logged at login | `user.service.ts:125-127` | **Gap** |
| API security | Bearer JWT; Swagger disabled in UAT/prod env files (`ENABLE_SWAGGER=false`) | `src/main.ts:140-161` | Partial |
| Secure headers | helmet (if `ENABLE_HELMET=true`): noSniff, frameguard deny, referrer policy; CSP/HSTS flag-controlled (HSTS true in uat/prod env files) | `src/main.ts:36-80` | Implemented (config-dependent) |
| CORS | Allow-list + `CORS_ORIGIN`, `credentials:true`; hardcoded defaults always include localhost and two plain-HTTP IP origins | `src/main.ts:116-138` | Partial – remove hardcoded origins |
| CSRF | No CSRF tokens; refresh cookie `sameSite=strict` (partial mitigation); API uses Bearer header | — | Partial |
| Cookies | httpOnly, sameSite strict; `secure` only when `NODE_ENV==='production'` (never set) | `public.controller.ts:53-57` | **Gap** |
| File upload security | 10 MB limit on grievance uploads; document-uploader has no size limit; magic-byte validator exists but **not called**; client MIME stored; no malware scanning | `src/common/core/utils/fileType.utils.ts`; `document-uploader.controller.ts:111` | **Gap** |
| Rate limiting / brute force | Global throttler per IP (prod env: 20 req / 15 min); no per-account/login-specific limits; `TRUST_PROXY` not applied in code; public OHM endpoints `@SkipThrottle` | `src/app.module.ts:63-76,131-134` | Partial |
| Error handling | Nest default handler (no stack traces); custom filters exist but unregistered; internal error messages re-thrown to clients | `src/common/core/filters/*` | Partial |
| Logging | Application logs present; **sensitive data logged**: plaintext login password, password hash, access token, citizen OTP, phone numbers | `user.service.ts:125-127,150`; `public.controller.ts:49-51`; `citizen.service.ts:120-122` | **Gap – High** |
| Audit trail | Grievance status history, nodal history, login history, SMS audit, audit columns. Not audited: failed logins, role/permission changes, password resets, admin actions, document access. History endpoints are writable without auth | `src/grievanceHistory`, `src/grievanceNodalHistory` | Partial |
| Sensitive data masking | None | — | Not Available |
| Secrets management | See S1–S3 | — | **Gap – Critical** |
| Health / metrics exposure | `/api/v1/health` and `/api/v1/metrics` unauthenticated (health returns environment/version/raw errors) | `src/health/health.controller.ts`; `src/app.controller.ts:22-31` | Gap – Medium |
| Dependency hygiene | Unpinned private package (`latest`); undeclared runtime deps; FE `xlsx` advisories | `package.json` | Gap |

---

## 11. VAPT / Security Audit / Code Review

| Assessment | Status |
|---|---|
| VAPT (application) | **Not Available – To be obtained from Security/Compliance Team** (no report in repos) |
| Auditor / CERT-In status | To be obtained |
| Safe-to-host certificate | **Not Available – To be obtained** (typically mandatory for Govt. of Karnataka hosting – confirm with client/KSDC) |
| Source code review (third-party) | Not Available – To be obtained |
| Internal repository review (this document) | Performed 08-10-2026 – findings in §7, §10, S1–S5 (not a formal VAPT) |

> No security findings have been assumed; all findings listed in this document are directly observed in source/configuration.

---

## 12. WAF / DDoS / Network Security

| Control | Finding | Status |
|---|---|---|
| WAF | Not referenced in repo | To be obtained from Infra/Security team |
| DDoS protection | Not referenced in repo | To be obtained from Infra team |
| Firewall / IDS/IPS / VPN | Not referenced | To be obtained from Infra team |
| Network segmentation | Not determinable (DB, MinIO, app on same Docker host per `host.docker.internal`) | To be obtained |
| API gateway / load balancer / reverse proxy | Not in repo; `TRUST_PROXY=true` in `.env.prod` suggests a proxy | To be confirmed by DevOps |
| Application-level throttling | Present (see §10) | Available |

---

## 13. Encryption & Digital Certificates

| Area | Finding | Evidence | Status |
|---|---|---|---|
| TLS version / HTTPS (public) | Not configured in app; depends on hosting proxy | — | To be obtained from DevOps (SSL Labs scan) |
| Certificate type / CA / validity | Not in repo | — | To be obtained from DevOps |
| API encryption | Relies on transport TLS | — | Not Verified |
| DB encryption in transit | Effectively disabled (see §9) | `database.config.ts` | Gap |
| Database / object / backup encryption at rest | Not Verified | — | To be obtained from Infra |
| Password hashing | bcrypt (cost 10) | `user.service.ts` | Available |
| Other hashing | SHA-1 (SMS gateway password, required by gateway), SHA-512 (SMS request key) | `sms-gateway.service.ts:1244-1267` | Available (gateway-imposed) |
| Token mechanism | JWT HS256 (default), secrets from env; algorithm not pinned; access/refresh may share secret if separate secrets unset (not set in env files) | `jwt.strategy.ts`, `auth.service.ts` | Partial |
| OTP generation | `Math.random()` (not cryptographically secure) | `citizen.service.ts:76`; `user.service.ts:853` | Gap |
| Digital signatures | None | — | Not Applicable |

---

## 14. Incident Management

No incident management artefacts in repository (no runbooks, escalation matrix, SLA, RCA templates). Status: **To be obtained from Support/Security team `[Org]`** — incident process, severity levels, escalation matrix, response team, tickets, RCA documents.

Application capabilities that support incident investigation: application logs (`logs/app.log`), `login_history`, grievance status history, `sms_audit`, Prometheus metrics.

---

## 15. Logging & Monitoring

| Type | Finding | Evidence | Status |
|---|---|---|---|
| Application logging | winston JSON to `./logs/app.log` + Nest console logs | `src/app.module.ts:45-55` | Available |
| Audit logging | Business audit tables (see §10) | — | Partial |
| Security logging | Successful logins/logouts only; no failed-login or authorization-failure logging | — | Gap |
| Access / API logging | `LoggingInterceptor` on some controllers (method + URL) | `src/common/core/interceptors` | Partial |
| Database logging | `DB_LOGGING=true` in all env files (all queries logged) | `database.config.ts:151` | Available (privacy concern) |
| Infrastructure logging | Not in repo | — | To be obtained |
| Monitoring tools | Prometheus scrape config (target path mismatch: scrapes `/metrics`, actual `/api/v1/metrics`); no Grafana, no alert rules | `prometheus-config.yml` | Partial |
| ELK / Splunk / SIEM / CloudWatch | Not found | — | Not Available / To be obtained |
| Log retention | Not implemented (no rotation) | — | **Gap** |
| Alerting / dashboards | Not found | — | Not Available |

---

## 16. CI/CD & Deployment

| Item | Finding | Status |
|---|---|---|
| Source repository | GitHub (`Inventechinfosolutions`) | Available |
| CI tool | **None** (no GitHub Actions/Jenkins/Bitbucket/GitLab files) | **Not Available** |
| Build process | Backend: `npm run build:<env>` (webpack → `dist/main.js`), Docker multi-stage build. Frontend: `vite build` (no type-check, no lint) | Available (manual) |
| Test automation | None | Not Available |
| Security / container scanning | None | Not Available |
| Artifact repository / image registry | Not in repo | To be obtained from DevOps |
| Deployment tool | docker-compose (backend app + Prometheus); frontend hosting not in repo | Partially Available |
| Kubernetes / Helm / Argo | Not used | Not Applicable |
| Approval process / production deployment / rollback | Not documented | To be obtained from DevOps |
| Known deployment defects | Dockerfile `HEALTHCHECK` runs `node dist/main.js` (starts a second instance); compose healthcheck uses `curl` (absent in alpine) on wrong path; `@nestjs/schedule`/`cron` missing from `package.json` (clean `npm ci` build risk); Puppeteer/Chromium not installed in image | Gap |

---

## 17. Infrastructure & Hosting

| Item | Finding | Status |
|---|---|---|
| Hosting model | Docker on a host running MySQL and MinIO (`host.docker.internal` in uat/prod env files) | Partially Available |
| Cloud provider / data centre / region | Not in repo (Govt. project – possibly KSDC/client DC; **unverified**) | To be obtained from DevOps/Client |
| VM / Kubernetes | Not in repo | To be obtained |
| Storage | MinIO + local disk volumes (`./logs` mounted; `storage/` not mounted – data loss on container restart) | Partially Available |
| Network / firewall / LB | Not in repo | To be obtained |
| Backup / DR infrastructure | Not in repo | To be obtained |

---

## 18. Disaster Recovery & Business Continuity

No DR architecture, RPO/RTO, DR procedure or DR test evidence in repository. Application is single-instance-oriented (in-memory cache/OTP state; cron uses MySQL lock). Status: **To be obtained from DevOps/Infra team** — DR site, backup mechanism, RPO, RTO, DR test date/report.

---

## 19. Third-Party Integrations

| System | Purpose | Integration Type | API / Protocol | Authentication | Data Exchanged | Owner |
|---|---|---|---|---|---|---|
| Karnataka Mobile Seva SMS Gateway (`smsmobileone.karnataka.gov.in`) | OTP, grievance status SMS, daily report link | Outbound REST (form POST) | **HTTP (not HTTPS)** | Username + SHA-1 password + SHA-512 request key (env `SMS_*`) | Mobile number, message text (incl. OTP), DLT template ID | Govt. of Karnataka (CeG) – credentials via BDA |
| MinIO object storage | Grievance documents, images, voice, video | S3 API | HTTP (`S3_SSL_ENABLED=false`) | Access key / secret (env) | Citizen files | Project / Infra |
| Prometheus | Metrics scraping | Pull | HTTP `/api/v1/metrics` | None | Process metrics | Project |
| YouTube | OHM session video links (URL stored only, no API call) | Link | — | — | URL | — |
| Google Gemini + MongoDB Atlas | Chatbot (branch `feature/chatbot` only, not on `main`) | SDK | HTTPS | API key / connection string | Chat queries, OHM invite lists | Needs confirmation |
| Payment / Aadhaar / Maps / Email / Banking | Not integrated | — | — | — | — | Not Applicable |

---

## 20. Project Size & Effort

| Metric | Value | Source | Status |
|---|---|---|---|
| Number of modules | 19 backend NestJS modules; 13 frontend modules | `src/app.module.ts`; frontend `src/modules` | Available |
| Number of screens | 74 page components; 114 routes (9 "Coming Soon") | frontend `src/modules/*/pages`, `src/App.tsx` | Available |
| Number of APIs | 319 live endpoints (52 controllers) | backend controllers | Available |
| Number of DB tables (entities) | 54 | backend entities | Available |
| Number of integrations | 2 active external (SMS, MinIO) | §19 | Available |
| Scheduled jobs | 2 | §2 | Available |
| Languages | 2 (English, Kannada; ~2,295 keys) | frontend `src/locales` | Available |
| Commits / PRs | Backend 454 commits, 197 PRs; Frontend 560 commits, 224 PRs | git | Available |
| Contributors (git) | ~10 distinct developers (some with 2 identities) | `git shortlog` | Available |
| Man-days (total/dev/test/DevOps/arch/support) | — | — | To be obtained from PMO |
| Team size / peak / roles | — | — | To be obtained from PMO |
| Function points | — | — | Not Available |
| SOW / PO / project plan / estimation / completion certificate | — | — | To be obtained from PMO/Sales |

---

## 21. Government / Enterprise Project Evidence

| Field | Value | Status |
|---|---|---|
| Client name | Bangalore Development Authority, Govt. of Karnataka | Available |
| Project name | BDA Grievance Redressal Portal | Available |
| Sector | Government – Urban Development | Available |
| Scope | See §2 | Available |
| Contract value | — | To be obtained (if permitted) |
| Duration | Sep-2025 → ongoing | Partially Available |
| Technology | React 19 / NestJS 10 / MySQL 8 / MinIO / Docker | Available |
| Team size / man-days | — | To be obtained |
| Major modules / integrations | See §2, §19 | Available |
| Deployment model | Docker-based; hosting location to be confirmed | Partially Available |
| Completion status | Ongoing | Available |
| PO / work order / completion certificate / client certificate / SOW | — | To be obtained from PMO/Sales |

---

## 22. Quality & Certifications

No certificates are stored in the repositories. All items **To be obtained from Org Compliance team `[Org]`**: ISO 9001, ISO 27001, ISO 20000, CMMI, SOC 1/2, PCI DSS (likely Not Applicable – no card data), CERT-In empanelment of VAPT auditor, data-centre certifications (hosting provider).

---

## 23. Policies Relevant to the Project

No policy documents exist in either repository. The table records observed **implementation evidence in the code** for each policy area; policy documents themselves must be obtained from the Org Compliance team `[Org]`.

| Policy | Policy document | Implementation evidence in project | Gap |
|---|---|---|---|
| Information Security | To be obtained | — | Needs confirmation |
| Data Protection / Privacy | To be obtained | PII in git; no masking; no retention | Implementation gap |
| Access Control | To be obtained | RBAC model exists but not enforced | Implementation gap |
| Password | To be obtained | bcrypt; weak complexity on active flows; no expiry/lockout | Implementation gap |
| Encryption / Key Management | To be obtained | No at-rest/field encryption; secrets in git | Implementation gap |
| Secure SDLC | To be obtained | ESLint security plugin (BE); no tests/SAST/CI | Implementation gap |
| Incident Response | To be obtained | — | Needs confirmation |
| Backup / DR / BCP | To be obtained | No backup config in repo | Needs confirmation |
| Data Retention / Archival / Purging | To be obtained | None implemented | Implementation gap |
| Change Management | To be obtained | PR-based; no tags/releases | Partial |
| Vulnerability / Patch Management | To be obtained | No dependency scanning | Implementation gap |
| WAF / DDoS | To be obtained | Not in repo | Needs confirmation |

---

# D. EVIDENCE REGISTER

| # | Assessment Area | Requirement | Evidence Available | Evidence Type | Location / Link | Date | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Identification | Repository URLs | Yes | Repository | github.com/Inventechinfosolutions/bda-grievance-backend, …/bda-grievance-frontend | 08-10-2026 | Tech Owner | Available |
| 2 | Scope | Business objective & modules | Yes | Document | frontend `BDA_GRIEVANCE_CASE_STUDY.md` | 23-03-2026 | Tech Owner | Available |
| 3 | Scope | SRS / SOW | No | Document | — | — | PM | To be obtained |
| 4 | Technology | Stack versions | Yes | Configuration | backend & frontend `package.json`, `package-lock.json` | 08-10-2026 | Tech Owner | Available |
| 5 | Architecture | Architecture diagrams | No | Architecture diagram | — | — | Architect | Not Available |
| 6 | Architecture | Container definition | Yes | Configuration | backend `Dockerfile`, `docker-compose.yml` | 17-03-2026 | DevOps | Available |
| 7 | Repository | PR-based merges | Yes | Repository | GitHub PRs BE #1–#197, FE #1–#224 | 24-09-2026 | Tech Owner | Available |
| 8 | Repository | PR review approvals | Unknown | Screenshot | GitHub PR review pages | — | Tech Owner | To be obtained |
| 9 | Repository | Branch protection | No (direct commits found) | Repository | `git log origin/main --first-parent --no-merges` | 07-09-2026 | Tech Owner | Gap |
| 10 | Repository | Release tags / history | No | Repository | `git tag` empty | — | Tech Owner | Not Available |
| 11 | SDLC | Pre-commit lint (security rules) | Yes (BE only) | Configuration | backend `.husky/pre-commit`, `.eslintrc.js` | 13-02-2026 | Tech Owner | Partially Available |
| 12 | SDLC | Automated tests | No (2 trivial specs) | Repository | backend `src/**/*.spec.ts` | — | QA | Gap |
| 13 | SDLC | UAT sign-off | No | Report | — | — | QA/PM | To be obtained |
| 14 | Authentication | Password hashing (bcrypt) | Yes | Repository | backend `src/common/user/service/user.service.ts:102` | — | Tech Owner | Available |
| 15 | Authentication | Citizen OTP login | Yes | Repository | backend `src/citizen/services/citizen.service.ts` | — | Tech Owner | Available (with gaps) |
| 16 | Authentication | MFA for admin/staff | No | — | — | — | Tech Owner | Not Available |
| 17 | Authentication | Account lockout | No | — | — | — | Tech Owner | Not Available |
| 18 | Authorization | Permission enforcement | No (guard returns true) | Repository | backend `src/common/auth/guards/permissions.guards.ts:23-61` | — | Tech Owner | Gap |
| 19 | Authorization | Role–permission matrix | No | DB export | Production DB tables `role_permission`, `post_permission` | — | DB Admin | To be obtained |
| 20 | Access mgmt | User onboarding/offboarding records | No | Records | — | — | PM/Client | To be obtained |
| 21 | Access mgmt | Periodic access review | No | Records | — | — | Security | To be obtained |
| 22 | Data | ER diagram / data dictionary | No | Document | Generate from DB | — | DB Admin | Not Available |
| 23 | Data | Entity definitions | Yes | Repository | backend `src/**/models/*.entity.ts` (54) | — | Tech Owner | Available |
| 24 | Data protection | Encryption at rest | No | Configuration | — | — | Infra | Not Verified |
| 25 | Data protection | DB TLS | No (disabled by config) | Configuration | backend `src/config/database.config.ts:170-177`; `.env.prod:13` | — | DevOps | Gap |
| 26 | Backup | Backup schedule & logs | No | Backup report | — | — | DevOps | To be obtained |
| 27 | Backup | Restore test | No | Report | — | — | DevOps | To be obtained |
| 28 | Retention | Retention/purging configuration | No | Configuration | — | — | Tech Owner | Not Available |
| 29 | App security | Input validation | Yes | Repository | backend `src/main.ts:100-106` | — | Tech Owner | Available |
| 30 | App security | Security headers (helmet) | Yes | Repository | backend `src/main.ts:36-80` | — | Tech Owner | Available |
| 31 | App security | Rate limiting | Yes | Repository | backend `src/app.module.ts:63-76,131-134` | — | Tech Owner | Partially Available |
| 32 | App security | Audit trail | Partial | Repository | backend `src/grievanceHistory`, `src/grievanceNodalHistory`, `login_history`, `sms_audit` | — | Tech Owner | Partially Available |
| 33 | App security | Secrets management | No (secrets in git) | Repository | backend `.env.dev/.env.uat/.env.prod` | 23-09-2025 | DevOps | Gap (report S1) |
| 34 | VAPT | Latest VAPT report | No | Report | — | — | Security/Compliance | To be obtained |
| 35 | VAPT | Safe-to-host certificate | No | Certificate | — | — | Security/Client | To be obtained |
| 36 | Network | WAF / DDoS | No | Configuration/Dashboard | — | — | Infra | To be obtained |
| 37 | Encryption | TLS certificate details | No | Certificate | — | — | DevOps | To be obtained |
| 38 | Monitoring | Prometheus metrics | Yes | Configuration | backend `prometheus-config.yml`, `src/app.controller.ts` | 13-02-2026 | DevOps | Partially Available |
| 39 | Monitoring | Alerting / dashboards | No | Dashboard | — | — | DevOps | Not Available |
| 40 | Logging | Log retention | No | Configuration | — | — | DevOps | Gap |
| 41 | CI/CD | Pipeline configuration | No | Configuration | — | — | DevOps | Not Available |
| 42 | Infra | Hosting/DC details | No | Document | — | — | DevOps/Client | To be obtained |
| 43 | DR | DR plan, RPO/RTO, test report | No | Report | — | — | DevOps | To be obtained |
| 44 | Integrations | SMS gateway integration | Yes | Repository | backend `src/sms-gateway/services/sms-gateway.service.ts` | — | Tech Owner | Available |
| 45 | Effort | Man-days, team size | No | Project plan | — | — | PMO | To be obtained |
| 46 | Credentials | PO / work order / completion cert | No | PO/Certificate | — | — | PMO/Sales | To be obtained |
| 47 | Certifications | ISO 27001 / 9001 / CMMI | No | Certificate | — | — | Compliance | To be obtained |
| 48 | Policies | All policies (§23) | No | Policy | — | — | Compliance | To be obtained |
| 49 | Incident | Incident process / tickets / RCA | No | Policy/Ticket | — | — | Support/Security | To be obtained |

---

# E. DOCUMENT REGISTER

| Document | Available in repo | Location | Current / Last updated | Notes |
|---|---|---|---|---|
| Project case study (functional overview) | Yes | frontend `BDA_GRIEVANCE_CASE_STUDY.md` | 23-03-2026 | Functional summary, no volumes |
| Existing grievance flow analysis | Yes | frontend `EXISTING_GRIEVANCE_FLOW_ANALYSIS.md` | 02-03-2026 | Functional |
| Citizen login setup guide | Yes | frontend `CITIZEN_LOGIN_SETUP_GUIDE.md` | 27-02-2026 | Developer guide |
| API specification | Partial | frontend `API_SPECIFICATION.md`; backend `POSTMAN_GUIDE.md`; Swagger at runtime (dev) | 13-02-2026 | Outdated / single API |
| Staff login data model | Yes | backend `docs/STAFF_USER_POST_PERSON_LOGIN_MODEL.md` | 27-04-2026 | Partial data model |
| RTI backend blueprint | Yes | backend `docs/RTI_BACKEND_BLUEPRINT.md` | 27-04-2026 | **Different/future system – not this project** |
| README (backend / frontend) | Yes (template) | repo roots | 13-02-2026 | **Generic template text – needs update** |
| Home page pattern | Yes | frontend `HOME_PAGE_PATTERN.md` | 23-03-2026 | Stale (references missing file) |
| Architecture diagrams | No | — | — | Missing |
| ER diagram / data dictionary | No | — | — | Missing |
| SRS / SOW / PO / work order | No | — | — | To be obtained |
| Completion certificate | No | — | — | Project ongoing |
| VAPT report / safe-to-host | No | — | — | To be obtained |
| DR test report | No | — | — | To be obtained |
| Audit reports | No | — | — | To be obtained |
| Policies | No | — | — | To be obtained (Org) |
| Certificates (ISO/CMMI/etc.) | No | — | — | To be obtained (Org) |

---

# F. GAPS

### Critical (fix before HDFC assessment)
| # | Gap | Category | Evidence |
|---|---|---|---|
| G1 | Secrets committed to git (env files, chatbot branch) | Missing control | S1, S2 |
| G2 | Hardcoded fixed OTP / default password / JWT fallback secret | Missing control | S3 |
| G3 | Permission guard is a no-op – RBAC not enforced | Missing control | `permissions.guards.ts:23-61` |
| G4 | ~52 unintentionally unauthenticated endpoints (role/permission admin, SMS relay, documents, citizen records, password reset) | Missing control | §10 |
| G5 | Unauthenticated password reset (`/user/reset-password`, `/user/auto-reset-password`) | Missing control | `user.controller.ts:213-255` |
| G6 | Citizen PII and grievance attachments committed to git | Missing control | S4, S5 |

### High
| # | Gap | Category |
|---|---|---|
| G7 | Plaintext passwords, tokens, OTPs logged; OTPs stored plaintext in `citizen` and `sms_audit` | Missing control |
| G8 | No MFA for admin/staff; no account lockout; weak password policy on active flows; user status not checked at login | Missing control |
| G9 | Stored-XSS risk: 21 `dangerouslySetInnerHTML` without sanitiser | Missing control |
| G10 | `NODE_ENV` never `production` → DB TLS off, cookies not `secure`; DB TLS `rejectUnauthorized:false` | Misconfiguration |
| G11 | SMS gateway and MinIO over plain HTTP | Missing control |
| G12 | No VAPT report / safe-to-host certificate available | Missing evidence – Security team |
| G13 | No backup, DR, RPO/RTO evidence | Missing evidence – DevOps |
| G14 | No CI/CD, no automated tests, no SAST/dependency scanning | Missing control |

### Medium
| # | Gap | Category |
|---|---|---|
| G15 | No branch protection evidence (direct commits to `main`); no tags/releases; `prod` branch stale since 11-02-2026 | Process gap |
| G16 | No architecture diagrams, ER diagram, data dictionary | Missing documentation |
| G17 | No data retention / archival / purging; report links never expire | Missing control |
| G18 | No log rotation/retention; no alerting; Prometheus path misconfigured | Missing control |
| G19 | File upload: magic-byte check not used, no malware scan, unlimited size on document-uploader | Missing control |
| G20 | Unauthenticated `/health` and `/metrics`; hardcoded HTTP/IP CORS origins | Misconfiguration |
| G21 | Token blacklist defects (TTL unit, key mismatch, in-memory only); no frontend route guards / idle timeout | Defect |
| G22 | Undeclared dependencies (`@nestjs/schedule`, `cron`), unpinned private package, `xlsx` advisories, unused `express.js` package | Build/supply-chain risk |
| G23 | READMEs are template text; API documentation outdated | Needs update |

### Needs confirmation from another team
- Production status, hosting location (cloud/KSDC/on-prem), servers, TLS certificates, WAF/DDoS, firewall – **DevOps/Infra**
- VAPT, safe-to-host, CERT-In auditor – **Security/Compliance**
- Backup/DR evidence – **DevOps/DB admin**
- SOW, PO, man-days, team, PM/Architect names – **PMO**
- Policies and certifications – **Org Compliance**
- Role–permission matrix and user counts from production DB – **DB admin / Client**

### Not Applicable
Mobile app; payment/financial data; Aadhaar; Kubernetes/Helm/Argo; message brokers; AI/ML on `main` branch.

---

## 25. Repository Review – Mandatory Checks (summary)

| Check | Backend | Frontend |
|---|---|---|
| README | Template text | Template text |
| package.json / build files | Yes | Yes |
| Dockerfile | Yes (healthcheck defect) | No |
| docker-compose | Yes (app + Prometheus) | No |
| Kubernetes manifests / Helm | No | No |
| CI/CD pipelines | No | No |
| Environment configuration | Yes – **secrets committed (S1)** | `config.ts` (env vars only, no secrets) |
| Infrastructure-as-Code | No | No |
| API documentation | Swagger (runtime, dev), Postman guide | `API_SPECIFICATION.md` (outdated) |
| Database / migration scripts | 3 migrations + manual SQL scripts (some with PII – S4) | N/A |
| Authentication implementation | Yes (gaps §7) | Token handling (sessionStorage) |
| Authorization implementation | Yes but not enforced (G3) | No route guards |
| Logging | Yes (sensitive data logged – G7) | console logs in prod build |
| Audit trail | Partial | N/A |
| Security configuration | helmet, throttler, validation pipe, CORS | — |
| Encryption configuration | bcrypt only; DB TLS effectively off | — |
| Certificate configuration | None | None |
| Third-party integrations | SMS gateway, MinIO | — |
| Monitoring configuration | Prometheus | — |
| Backup scripts | None | — |
| Deployment documentation | None | None |
| Secrets found | **Yes – reported separately (S1–S3)** | No |
