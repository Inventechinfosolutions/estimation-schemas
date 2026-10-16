# HDFC Vendor Assessment – Project & Repository Data Collection

## Project: IEBA V2 (Frontend + Backend)

| Field | Value |
|---|---|
| Prepared on | 08-10-2026 |
| Prepared from | Static review of local clones of the project repositories (code, config, git history) |
| Repositories reviewed | `Inventechinfosolutions/ieba-v2-backend`, `Inventechinfosolutions/IEBA-Client-Side` |
| Review method | Source code, configuration, `package.json`, `docker-compose.yml`, git branches/merge history, in-repo docs. GitHub server-side settings (branch protection, reviewers, Actions) were **not** queried. |
| Classification | **INTERNAL – CONFIDENTIAL.** Section 27 (Security Findings) is **RESTRICTED** to the Security / DevOps team. Do not forward Section 27 outside the organization. |

**Status vocabulary used throughout:** Available · Partially Available · Not Available · Not Applicable · To be obtained from another team · Not Verified

**Information level tags:** `[Project]` project-level · `[Org]` organization-level · `[Client]` client-specific · `[Infra]` infrastructure-level · `[SecTeam]` security-team controlled

> No passwords, keys, tokens, or connection strings are reproduced in this document. Where secrets were found, only the file location and type are recorded (Section 27).

---

## 1. Project Identification

| Item | Value | Source / Evidence | Status |
|---|---|---|---|
| Project Name | IEBA V2 (re-platform of an existing IEBA application; "database and tables are unchanged (legacy schema)") | `ieba-v2-backend/docs/PROJECT_GUIDE.md` §1 | Available |
| Expansion of "IEBA" | Not stated anywhere in the repositories | – | Not Verified – confirm with PM |
| Client / Department | Development is tracked in the Zoho Projects portal `paperlessknowledgeinc` (Paperless Knowledge Inc.). The code has a "PKI" user flag and `pki-report-access.service`. End users are US county agencies; the county databases referenced in config include `trinity` and `tuolumne_prod`. | `IEBA-V2/scripts/zoho-ticket.js` (portal URL), `src/modules/user/entity/userprofile.model.ts` (`pki` flag), backend `README.md` (namespace DB names) | Partially Available – confirm contracting entity with PM |
| Industry / Domain | Public sector: California county agencies (Health/Social Services), covering employee time study and federal/state administrative cost claiming. Evidence: Random Moment Time Study (`rmts*`), apportioning, cost pools, SPMP/FFP flags, and claiming reports for MAA/TCM (Medi-Cal Administrative Activities / Targeted Case Management), MCAH / Title V, WIC, CDSS AC741, and DSSRPT1–5. Counties Trinity and Tuolumne are hard-coded in the report generator with their logos. | Backend `src/generaladmin/*`; `src/generaladmin/reports/manualreports/pdf/report-pdf.generator.ts` (county names); `manualreports/logos/`; frontend `src/features/reports/pdf/*` | Available (inferred from code) |
| Project Type | Government (end client), likely delivered via a partner/prime vendor | As above | To be confirmed by PM |
| Project Start Date | First commit 10-03-2026 (frontend) / 12-03-2026 (backend) | `git log --reverse` on both repos | Available (repo evidence only; contract start date Not Verified) |
| Project End Date / Current Status | Ongoing, active development. Last merge to `prod` on 08-10-2026. | `git log origin/prod` | Available |
| Project Duration | ~7 months to date (Mar 2026 – Oct 2026) | git history | Available |
| Current Production Status | A `prod` branch exists and receives PR merges. The live production URL and hosting are not in the repo. | `origin/prod` branch | Partially Available – hosting To be obtained from DevOps |
| Environments | Dev (local), UAT (`release/uat`, `release/client-uat`), Prod (`prod`). Backend config supports `ENVIRONMENT=UAT/PROD` namespace blocks. | Git branches; `.env.example`; `src/config/database.config.ts` | Partially Available – environment URLs/hosting Not in repo |
| Repository Name(s) | `ieba-v2-backend`, `IEBA-Client-Side` | `git remote -v` | Available |
| Repository URL | `git@github.com:Inventechinfosolutions/ieba-v2-backend.git`, `git@github.com:Inventechinfosolutions/IEBA-Client-Side.git` | `git remote -v` | Available |
| Repository Type | GitHub (organization `Inventechinfosolutions`) | `git remote -v` | Available |
| Repository Owner / Technical Owner | Not recorded in repo (no `CODEOWNERS`) | – | To be obtained from PM |
| Project Manager | Not recorded in repo | – | To be obtained |
| Solution Architect | Not recorded in repo | – | To be obtained |
| DevOps / Infrastructure Owner | Not recorded in repo | – | To be obtained |
| Security Owner | Not recorded in repo | – | To be obtained |
| Contributors (git authors) | Backend: SushmithaGowda20/Sushmitha, arunkumar-an, Monisha-s-2003, Srujan-Krishna/Srujan, vadiraj Karanam, Anil Kishore, Naresh647754. Frontend: arunkumar-an, Naresh647754/Naresh DJ, Monisha-s-2003, Sushmitha/SushmithaGowda20, Srujan-Krishna/Srujan, Inventech Info Solutions, Ashok. | `git shortlog -sn --all` | Available |

---

## 2. Project Scope

### 2.1 Business objective
A multi-tenant (one database per county) web application. Its purpose is to record employee time-study data and administer programs, activities, cost pools, job pools and payroll/benefits. It apportions time and cost and generates statutory/claiming reports for county agencies. Source: backend modules and report generators (see 2.3). `[Project]` – **Status: Available (inferred from code); formal business objective document Not Available in repo.**

### 2.2 User types (roles)
| Role | Source |
|---|---|
| Super Admin (role id 1) | `src/generaladmin/timestudyrecord/constants/time-study-eligible-role-ids.ts`, frontend `src/hooks/usePermissions.ts` |
| Client Admin (2) | same |
| Department Admin (3) | same |
| Payroll Admin / Time Study Admin (5) | same |
| Time Study Supervisor (6) | same |
| User / Employee (7) | same |
| Global Admin (a single login id configured via env `GLOBALADMIN`, used for cross-county administration) | `src/core/auth/guards/global-admin.guard.ts` |

Approximate number of users: **Not Available in repo – To be obtained from PM/client.**

### 2.3 Major modules (verified in code)
| Module | Backend location | Frontend location |
|---|---|---|
| Authentication, OTP, password reset, sessions | `src/core/auth` | `src/features/auth`, `src/features/change-password` |
| User / employee management, profile, documents, impersonation ("mimic") | `src/modules/user`, `userprofile`, `userdepartmentrole`, `document` | `src/features/user`, `Profile` |
| Department, department roles & permissions | `src/modules/department` | `src/features/department`, `DepartmentRole` |
| Programs (budget / time-study programs, activities) | `src/generaladmin/budgetprograms`, `timestudyprograms`, `activity`, `src/modules/program` | `src/features/program`, `CountyActivityCode`, `master-code` |
| Cost pool, job pool, job classification | `src/generaladmin/costpool`, `jobpool`, `jobclassification` | `src/features/cost-pool`, `job-pool`, `job-classification` |
| Time study records, apportioning, RMTS scheduling | `src/generaladmin/timestudyrecord`, `rmts` | `src/features/PersonalTimeStudy`, `schedule-time-study` |
| Payroll management (Excel/CSV upload) | `src/generaladmin/payrollmanagement` | `src/features/payroll` |
| Leave approval, To-do, Notifications | `src/modules/...`, `src/generaladmin/todo`, `notification` | `src/features/leave-approval`, `todo`, `notification` |
| Reports (PDF/Excel/CSV), internal cross-county report A010 | `src/generaladmin/reports`, `src/modules/report` | `src/features/reports` (22 PDF templates), `internal-reports` |
| Settings (2FA toggle, OTP timeout, inactivity timeout, fiscal year, holidays) | `src/generaladmin/appsettings` | `src/features/settings` |
| Global (multi-county) administration | `src/modules/iebaglobal` | `src/features/auth` (county switch) |
| Page Assistant (FAQ + AI) | `src/assistant` | `src/components/assistant` |
| Dashboard | `src/modules/dashboard` | `src/features/dashboard` |

### 2.4 Size indicators (verified counts)
| Metric | Count | Source |
|---|---|---|
| Backend controllers | 41 | `grep @Controller(` in `src` |
| Backend HTTP endpoints | 330 (GET 175, POST 82, PUT 40, DELETE 33). 4 public: login, send-otp, refresh, me. | `@Get/@Post/@Put/@Delete` decorators in `src` |
| Backend DB entities (tables mapped) | 78 entities / 77 distinct tables (`department` mapped twice) | `@Entity(` in `src` |
| Backend scheduled jobs | 6 cron jobs + 1 startup job | `@Cron` occurrences |
| Frontend feature folders | 25 (1 empty `chatbot`, 1 unrouted `fte-allocation`, 1 demo `users`) | `src/features` |
| Frontend routed screens | 24 (4 public, 20 authenticated) | `src/routes.tsx` |
| Frontend distinct API paths called | ~190 | `src/lib/api.ts` call sites |
| Report PDF templates (frontend) | 22 | `src/features/reports/pdf` |
| Git commits | Backend 976, Frontend 1,255 (all branches) | `git rev-list --all --count` |
| Merged pull requests | Backend ~462, Frontend ~450 (merge commits "Merge pull request #…") | `git log --merges` |

### 2.5 APIs, integrations, jobs
- **APIs exposed:** REST/JSON under `/api/v1` (configurable `API_PREFIX`); OpenAPI/Swagger at `/api/docs` (`src/main.ts`). **Available.**
- **APIs consumed (verified in code):** SMTP email (nodemailer), Twilio SMS / generic HTTP SMS (optional, env-driven), Google Gemini API (`@google/genai`, Page Assistant), MinIO/S3 object storage. See Section 19.
- **Batch / scheduled jobs:** nightly apportioning calculation (`0 0 * * *`); 4 daily 06:00 time-study reminder jobs; weekly Friday reminder; fiscal-year auto-creation at startup. Source: `timestudyrecord.service.ts`, `notification-scheduler.service.ts`, `fiscalyear-startup.service.ts`.
- **Notification services:** email (SMTP), optional SMS, in-app notifications (Redis + `notification` table).
- **File/document processing:**
  - Payroll Excel import is parsed with ExcelJS (`payrollmanagement.service.ts`).
  - User, client and time-study supporting documents are stored in MinIO.
  - `pdf-parse` extracts PDF text for the assistant.
  - Report Excel/CSV is generated on the server (ExcelJS). Report PDFs are rendered in the browser (`@react-pdf/renderer`). A Puppeteer HTML-to-PDF generator exists in the backend but is not called by any controller or service.
- **AI/ML components:** The Page Assistant (`src/assistant/assistant.service.ts`) works as follows:
  - An admin uploads a role user-manual PDF.
  - The text is chunked and sent to Google Gemini (`gemini-flash-lite-latest`, key `GEMINI_API_KEY`), which generates Q&A pairs.
  - The pairs are stored in `assistant_qa_bank` and cached in Redis for 24 h.
  - Only manual text and the role name are sent. No employee, payroll or time-study data goes to the LLM.
  - A code comment references Gemini **free-tier** limits, so the data-use terms of the Google plan need confirmation.
  - The local env file also has OpenAI / local-LLM variables, but **no code uses them**.
  - Qdrant appears only in `docker-compose.yml` (not used in code). The `chatbot` folders (backend `src/modules/chatbot`, `data/chatbot/vectordb`, frontend `features/chatbot`) are empty.
- **Mobile application:** Not Applicable (none found).
- **Web application:** Yes – React SPA.

### 2.6 Requirement / design documents
| Document | Status | Location |
|---|---|---|
| Requirements / SRS / SOW | Not Available in repo | To be obtained from PM |
| Architecture document | Partially Available – coding-architecture guide only | `ieba-v2-backend/docs/PROJECT_GUIDE.md`, `prompt/prompt.txt`, backend `README.md` |
| Functional specification | Partially Available – report calculation guides | `IEBA-V2/docs/dssrpt-calculation-guides/*.docx/.xlsx` (DSSRPT1–5) |
| Technical specification (API) | Available (auto-generated) | Swagger `/api/docs`; `docs/user-management-apis.md` |
| User manuals (7 role-based PDFs) | Available | Frontend `src/documents/*.pdf` |
| Ticket-level requirements | Available (external) | Zoho Projects portal `paperlessknowledgeinc`; branch names `I-1-I<n>` map to Zoho issue IDs |

---

## 3. Technology Stack (verified against `package.json` and installed `node_modules`)

### 3.1 Frontend – `IEBA-Client-Side`
| Item | Value |
|---|---|
| Framework | React 19.2.4 (SPA) |
| Language | TypeScript 5.9.3 |
| Build tool | Vite 7.3.1 |
| Package manager | npm (`package-lock.json`) |
| UI | Tailwind CSS 4.2.1, shadcn/ui, Radix UI, lucide / tabler icons, sonner, vaul |
| State / data | TanStack Query 5.90.21, React Hook Form + Zod 4.3.6, TanStack Table |
| Routing | react-router-dom 7.13.1 |
| Reports / export | `@react-pdf/renderer`, `xlsx` 0.18.5, `recharts` |
| Security libs | `dompurify` 3.4.11 (used in some components only) |
| Lint | ESLint 9 (no tests) |

### 3.2 Backend – `ieba-v2-backend`
| Item | Value |
|---|---|
| Framework | NestJS 10.4.22 |
| Language / runtime | TypeScript 5.9.3 on Node.js (v22.22.3 on the dev machine; production runtime version Not Verified) |
| Architecture | Modular monolith; Controller → Service → DataService → Repository; multi-tenant DB-per-county |
| ORM / DB driver | TypeORM 0.3.28, mysql2 3.19.1 |
| Auth | `@nestjs/jwt`, `passport-jwt` 4.0.1, `bcrypt` 5.1.1 |
| Validation | class-validator, class-transformer (global ValidationPipe) |
| Logging | nestjs-pino 4.6.0 / pino-http |
| Cache / sessions | ioredis 5.10.0 (Redis) |
| Storage | `minio` 8.0.7 and `@aws-sdk/client-s3` (pointed at MinIO) |
| Scheduling | `@nestjs/schedule` |
| Reports | ExcelJS 4.4.0 (all Excel writes and payroll parsing). `xlsx` 0.18.5 is imported but its writes go through ExcelJS. Puppeteer 25.3.0 is present but its PDF generator is not invoked. |
| Email | nodemailer 9.0.3 |
| AI | `@google/genai` 2.14.0 |
| API docs | `@nestjs/swagger` |
| Quality | ESLint, Prettier, Husky pre-commit with lint-staged, Jest (1 trivial spec) |

### 3.3 Database
| Item | Value | Status |
|---|---|---|
| Technology | MySQL (`mysql:8.1` in dev compose); `DB_TYPE` per namespace | Available |
| Type | Relational; one schema per county/tenant + a `global` DB (login → county mapping) | Available – `src/core/database/tenant-connection.manager.ts`, `src/config/database.config.ts` |
| Number of databases | 1 global + N county DBs (namespaces `app1…app8` appear in the local env file) | Partially Available – production count To be obtained from DevOps |
| Production DB version | – | Not Verified |
| Stored procedures | 13 report procedures (e.g. `rpt_p100_paidtime`, `rpt_AC741_timerecording`, `rpt_TCM_MAA_timestudyrecord`, `rpt_IC214_Activitylog`, `rpt_TSH_Program_FTE`) and functions (`get_salary`, `get_benefits`, `get_SUM_TOTAL_HRS_*`), called by `report-data.service.ts`. Dump committed at `src/core/storage/use uat_v2_trinity;.sql`; `seed-data/stored-procedures/reports/P100`. | Available |
| Schema migrations | No TypeORM migrations. `synchronize` defaults to false (set false for all namespaces). Changes are made via 13 hand-run, idempotent SQL scripts in `scripts/mysql-*.sql`. The `migration:*` npm scripts reference `src/core/database/data-source.ts`, **which does not exist**. | Partially Available |

> Note: `docs/PROJECT_GUIDE.md` and `prompt/prompt.txt` state PostgreSQL. The code and configuration actually use **MySQL**. A Postgres container exists in `docker-compose.yml` but is unused. **Documentation needs update.**

### 3.4 Other technologies – verification matrix
| Technology | Used? | Evidence |
|---|---|---|
| Redis | **Yes** | `src/core/redis/*` (OTP, refresh-token blacklist, active sessions, permission cache, in-app notifications) |
| MinIO / object storage | **Yes** | `src/core/storage/storage.service.ts`, `src/common/s3-client/s3-client.service.ts` |
| Elasticsearch / Typesense | No | Not found |
| Qdrant / vector DB | Dev compose only, not used in code | `docker-compose.yml`; `src/modules/chatbot` empty |
| Apache Tika | Dev compose only, not used in code | `docker-compose.yml` |
| Keycloak | Dev compose only, not used in code | `docker-compose.yml` |
| Kafka | Commented out in compose; not used | `docker-compose.yml` |
| RabbitMQ | No | Not found |
| API Gateway | Not found in repo | To be obtained from DevOps |
| Nginx / reverse proxy | Not found in repo | To be obtained from DevOps |
| Istio / Kubernetes / Helm | Not found in repo | To be obtained from DevOps |
| Docker | Dev `docker-compose.yml` only; **no Dockerfile** for app | backend `docker-compose.yml` |
| Jenkins / GitHub Actions / Argo | Not found in repo (no `.github/workflows`, no `Jenkinsfile`) | – |
| Monitoring (Prometheus/Grafana/APM) | Not found in code | To be obtained from DevOps |
| Logging | pino → stdout. No log shipping configured in repo. | `src/app.module.ts` |
| SIEM / WAF / DDoS | Not found in repo | To be obtained from Infra/Security |
| Cloud services | Google Gemini API (SaaS). Hosting cloud Not in repo. | `src/assistant/assistant.service.ts` |
| Third-party SaaS | SMTP provider, Twilio (optional), Google Gemini, Google Fonts (frontend `index.html`), Zoho Projects (ticketing) | See Section 19 |

---

## 4. Architecture

| Architecture artefact | Status | Location |
|---|---|---|
| Application architecture (layering, module structure) | Partially Available (text only, no diagram) | `ieba-v2-backend/docs/PROJECT_GUIDE.md`, `README.md` |
| Deployment architecture | Not Available | To be obtained from DevOps |
| Network architecture | Not Available | To be obtained from Infra |
| Integration architecture | Not Available (derivable from Section 19) | – |
| Data architecture | Partially Available (multi-tenant design in README) | backend `README.md` "Database config (two modes)" |
| Authentication architecture | Not Available as document. Implementation is described in Section 7. | `src/core/auth/*` |
| Security architecture | Not Available | To be obtained |
| Cloud / On-prem architecture | Not Available | To be obtained from DevOps |

**Logical architecture (derived from code, `[Project]`):**

```
Browser (React SPA, Vite build)
   │  HTTPS (assumed – TLS terminated outside the app; not in repo)
   ▼
NestJS API  (/api/v1, plain HTTP listener – src/main.ts)
   ├── JWT auth (Bearer access token + httpOnly refresh cookie)
   ├── Tenant resolution (JWT tenantId / X-Tenant-Id header)
   ├── MySQL: global DB + one DB per county (TypeORM, stored procedures for reports)
   ├── Redis: OTP, sessions, token blacklist, permission cache, notifications
   ├── MinIO (S3 API): documents, payroll uploads, profile images
   ├── SMTP / SMS (Twilio or HTTP) – notifications
   ├── Google Gemini API – Page Assistant
   └── Excel/CSV report generation (ExcelJS); PDFs rendered in the browser
```

| Component | Identified | Evidence |
|---|---|---|
| Application server | Node.js / NestJS | `src/main.ts` |
| Web server / static hosting for SPA | Not in repo | To be obtained |
| API gateway / Load balancer | Not in repo | To be obtained |
| Database | MySQL | `src/config/database.config.ts` |
| Cache | Redis | `src/core/redis` |
| Object storage | MinIO | `src/core/storage` |
| Message broker | None | – |
| Identity provider | In-app (no external IdP) | `src/core/auth` |
| Monitoring / Security components | Not in repo | To be obtained |

---

## 5. Repository & Development Practices

| Item | Finding | Evidence | Status |
|---|---|---|---|
| Repository structure | Backend: `src/{core,modules,generaladmin,assistant,common,config}`, `scripts/*.sql`, `docs/`, `seed-data/`. Frontend: `src/{features,components,lib,hooks,layouts,contexts}` | Repo tree | Available |
| Branching strategy | Feature/bug branches named after Zoho tickets (`I-1-I427`, `feature/*`, `bug/*`, `dssrpt*/…`). Merged via PR into `main`, then promoted to `release/uat`, `release/client-uat`, `prod`. | `git branch -r` (backend 191, frontend 180 remote branches) | Available (inferred; no written policy) |
| Long-lived branches | `main` (default), `release/uat`, `release/client-uat`, `prod`; frontend also has `ics214/*` and `wic/*` | `git branch -r` | Available |
| Pull request process | In use. Backend `main` first-parent history: 261 of 276 commits are PR merges (13 direct). Frontend `main`: 249 of 263 (12 direct). | `git log --first-parent origin/main` | Available (git evidence) |
| Code review / approvals | Not verifiable from local git. Review/approval data lives on GitHub. | – | Not Verified – export from GitHub |
| Branch protection | Not verifiable locally. Direct commits on `main`/`prod` exist, which suggests protection is absent or was bypassed at times. | First-parent analysis above | Not Verified – check GitHub settings |
| Commit standards | Husky pre-commit runs `lint-staged` (Prettier + ESLint) in backend only. No commit-message convention enforced. | backend `.husky/pre-commit`, `package.json` `lint-staged` | Partially Available |
| Release / versioning | No git tags, no GitHub releases found locally. Backend `version: 1.0.0` and frontend `0.0.0` (static). | `git tag` (0 tags) | Not Available |
| Code ownership | No `CODEOWNERS` file | – | Not Available |
| Repository access controls | GitHub org `Inventechinfosolutions`. Membership/permissions not queried. | – | To be obtained from GitHub org admin |
| Deployment history | Not available in repo (no CI/CD) | – | Not Available |

---

## 6. SDLC & Development Process

| Area | Finding | Evidence | Status |
|---|---|---|---|
| Requirement management | Zoho Projects issues (`paperlessknowledgeinc` portal). Branch names reference issue IDs. | `IEBA-V2/scripts/zoho-ticket.js`, branch names | Available (external tool) |
| Development process | Feature branch → PR → `main` → UAT branches → `prod` | Git history | Available (inferred) |
| Coding standards | Documented layering/naming rules; ESLint + Prettier | `docs/PROJECT_GUIDE.md`, `prompt/prompt.txt`, `.eslintrc.js`, `.prettierrc`, frontend `eslint.config.js`, `.cursorrules` | Available |
| Unit testing | Backend: 1 placeholder spec (`s3-client.service.spec.ts`). Frontend: none. | `git ls-files` | **Gap** |
| Integration / E2E testing | `test:e2e` script points to a missing `test/` folder | backend `package.json` | Not Available |
| System testing / UAT | UAT branches exist (`release/uat`, `release/client-uat`). Test cases/sign-offs not in repo. | Branches | Partially Available – UAT sign-off To be obtained |
| Security testing (SAST/DAST/SCA) | No tooling configured in repo | – | Not Available |
| Performance testing | None found | – | Not Available |
| Release / change management | PR merges to `prod`. No release notes, tags, or CAB records in repo. | – | Partially Available |
| Production deployment & rollback | Not documented in repo | – | To be obtained from DevOps |
| Defect management | Zoho Projects issues | Zoho portal | Available (external) |
| SDLC / Secure SDLC policy | Not in repo | – | To be obtained `[Org]` |

---

## 7. Authentication & User Access Management (as implemented in code)

| Control | Implementation | Evidence | Status |
|---|---|---|---|
| Authentication mechanism | Login ID + password. Server issues a JWT access token (Bearer) and a refresh token in an httpOnly cookie. | `src/core/auth/auth.controller.ts`, `auth.service.ts`, `utils/auth-cookie.util.ts` | Available |
| Token algorithm / lifetime | HS256 (library default). Access token 1 h default; refresh token 7 d default; both configurable via env. | `src/config/jwt.config.ts`, `src/core/auth/auth.module.ts` | Available |
| Refresh token cookie | `httpOnly`, `SameSite=Strict`; `Secure` only when `NODE_ENV=production` | `auth-cookie.util.ts` | Available |
| Authorization | Global `JwtAuthGuard` plus `PermissionsGuard` (`module:action` permissions from `role` → `rolepermission`, cached in Redis) | `src/app.module.ts`, `src/core/auth/guards/permissions.guard.ts` | Available – **with gaps (Section 27)** |
| RBAC / roles | DB-driven roles per department (`userdepartmentrole`), permission catalogue (`permission`, `subpermission`, `appmodule`) | Entities under `src/modules/user/entity`, `src/modules/department` | Available |
| Role-permission matrix document | Not available as document (data lives in DB tables `role`, `rolepermission`) | – | **Gap** – export matrix |
| Admin / privileged roles | Super Admin (role 1), Client Admin (2), Global Admin (env-defined single login) | Section 2.2 | Available |
| User impersonation ("mimic") | Permission `user:mimic`. Issues a 1 h token flagged `mimic`; recorded only in the app log. | `src/modules/user/controller/user.controller.ts`, `user.service.ts` | Available – audit gap |
| MFA | Email OTP (6 digits), enabled per county via setting `TWO_FA_ENABLED` (default **off**); always on for the Global Admin login. **Implementation weaknesses found (Section 27).** | `auth.service.ts`, `src/core/common/services/settings.service.ts` | Partially Available |
| Password hashing | bcrypt, cost 10 | `src/modules/user/service/user.service.ts` | Available |
| Password complexity | Backend: length 10–16 on admin create/update only; no complexity on self-service change/reset. Frontend: change 10–16 with upper/lower/digit/symbol; reset 7–40 with upper/digit/symbol. Rules are inconsistent. | `create-user.dto.ts`, `change-password.dto.ts`, `reset-password.dto.ts`; frontend `features/change-password/schemas.ts`, `features/auth/schemas.ts` | Partially Available |
| Password expiry | Not implemented (`lastPasswordChanged` stored but not enforced) | `user.service.ts` | **Not Available** |
| Password history | Not implemented | – | **Not Available** |
| Failed login attempts / account lockout | Not implemented. A `LOCKED` status exists but is never set automatically. | `userstatus.enum.ts`, `auth.service.ts` | **Not Available** |
| Session timeout | Idle timeout in the frontend, tenant-configurable (default 120 min). Server-side: access-token expiry only. | Frontend `features/settings/components/General/AppLogout.tsx` | Partially Available |
| Logout / revocation | Refresh token blacklisted (Redis + DB). Access tokens not revoked. Deactivation/password change does not revoke sessions. | `auth.service.ts`, `blacklist-token.service.ts` | Partially Available |
| Password reset | Self-service OTP flow, plus admin reset to a default password with forced change on next login | `auth.service.ts`, `user.controller.ts` | Available – **critical weakness (Section 27)** |
| User provisioning | Admin creates user (`POST /users`, permission `user:add`); synced to global DB | `user.controller.ts`, `user.service.ts` | Available |
| De-provisioning / deactivation | `active` flag / status (`inactive`, `suspended`, `locked`, `marked_for_delete`); no hard delete | `userstatus.enum.ts` | Available |
| Third-party user access | Not applicable / not found | – | Not Applicable |
| PAM | Not found | – | Not Available |
| Periodic access review | No feature or records in repo | – | To be obtained `[Org]` |
| SSO / external IdP | Not implemented (Keycloak only in dev compose) | – | Not Available |

---

## 8. Data Model & Data Dictionary

| Artefact | Status | Location / Note |
|---|---|---|
| ER diagram | **Not Available** | Can be generated from the TypeORM entities or the MySQL schema |
| Data dictionary | **Not Available** | – |
| Data model (code) | Available | 78 TypeORM entities in backend `src/**/entity`, `src/**/models` |
| Database schema dump | Available (UAT, Trinity) | `src/core/storage/use uat_v2_trinity;.sql` (committed; includes stored procedures) |
| Change scripts | Available | backend `scripts/mysql-*.sql` (15 files) |
| Primary key strategy | Mixed: UUID for users (`randomUUID`), integer IDs in legacy tables | `user.service.ts`, entity files |

**Tables mapped in code (78):** activity, activity_bhsa_config, activitycode, activitydepartment, address, appmodule, apportioning_history, assistant_qa_bank, audit_log, audit_log_fields, blacklistedtokens, budgetprogram, budgetunit, client, contact, content, costpool, costpool_assignment_history, costpoolactivityassignment, costpooluserassignment, county_report_map, countymastercode, department, department_history, department_notification_config, department_report_config, departmentrole, document, document_meta_info, emergencycontact, fiscalyear, globaluser, holidaycalendar, jobclassification, jobpool, jobpool_assignment_history, jobpoolactivityassigment, jobpooluserassignment, location, mastercode, namespace, notes, notification, notification_history, payroll, payrollsetting, payrollupload, permission, program_activity_history, program_activity_mapping, report, rmtsgroup, rmtspayperiods, rmtsppgrouplist, rmtsusergroup, role, rolepermission, settings, subpermission, timestudyprogram, timestudyrecord, todo, user, useractivity, useractivity_history, userallowmulticodehistory, userdepartmentrole, userdepartmentrole_history, userdocument, userjob, userleave, userloginaudit, usermulticode, userprofile, userprogram, userprogram_history, userprogramassignment.

**Sensitive data classification (from entity fields):**
| Category | Tables / fields | Evidence |
|---|---|---|
| PII | `userprofile` (first/last name, **DOB**, gender, employeeId, position, supervisor), `address`, `contact`, `emergencycontact`, `user` (loginId = email) | `src/modules/user/entity/userprofile.model.ts` |
| Financial | `payroll`: employee ID, name, department, bargaining unit, position, pay period, check date, salary, benefits, FICA, PERS, deferred comp, cafeteria, life insurance, overtime, standby, stipends, cash-out/payout. `payrollupload`: uploaded payroll spreadsheets in MinIO. Cost pool data. Report DSSRPT5 outputs salary and benefits by employee. | `src/generaladmin/payrollmanagement/entity/payrollmanagement.model.ts` |
| Other PII | `contact` / `emergencycontact` (names, phone, email, relationship), `userleave` (leave dates, comments), `timestudyrecord` / `notes` (daily work records), `document_meta_info` (person name) | `src/modules/user/entity/*`, `src/generaladmin/timestudyrecord/entity/*` |
| Authentication | `user.password` (bcrypt), `blacklistedtokens` (stores raw refresh-token text), Redis OTP keys | `src/core/auth/entity/blacklisted-token.model.ts` |
| Audit | `audit_log`, `audit_log_fields`, `*_history` tables, `userloginaudit` (defined but unused) | `src/core/audit/entities` |
| SSN | Not found in entities | – |

---

## 9. Data Storage & Handling

| Area | Finding | Status |
|---|---|---|
| Where data is stored | MySQL (per-county DBs + global DB), Redis, MinIO. Hosting location (cloud/on-prem/region) not in repo. | Partially Available – hosting To be obtained from DevOps |
| File / object storage | MinIO bucket (`MINIO_BUCKET`); object keys are UUIDs | Available – `src/core/storage`, `src/common/s3-client` |
| Log storage | stdout only (pino). Destination/retention not in repo. | To be obtained from DevOps |
| Encryption at rest | No application-level/field encryption. DB/disk/MinIO encryption not in repo. | Not Verified – To be obtained from Infra |
| Encryption in transit | App listens on plain HTTP; TLS assumed at proxy (not in repo). No TLS options for MySQL or Redis connections. MinIO TLS only if `MINIO_USE_SSL=true`. SMTP TLS optional. | Partially Available – **gap** |
| Key / secret management | Environment variables / `.env*` files. No Vault/KMS. Hardcoded fallback secrets in code (Section 27). | **Gap** |
| Backup (frequency, type, location, retention, logs, restore test) | Nothing in repo | **To be obtained from DevOps/DBA** |
| Archival | No archival policy/code. Payroll uploads kept in MinIO ("archived uploads" UI). | Not Available |
| Data retention | No retention configuration in code. Only Redis TTLs (OTP, token blacklist) and an in-app notification cap per user. | Not Available |
| Data purging / secure deletion | No purge jobs or secure-deletion mechanism | Not Available |

---

## 10. Application Security Controls (code review summary)

| Control | Finding | Evidence | Status |
|---|---|---|---|
| Input validation | Global `ValidationPipe` (`whitelist`, `forbidNonWhitelisted`, `transform`); class-validator DTOs. Some inline-typed bodies bypass validation. Frontend uses Zod. | `src/main.ts`, `src/app.module.ts` | Available (with gaps) |
| SQL injection prevention | TypeORM parameterised queries mostly. **Report stored-procedure calls built by string interpolation** (Section 27). | `report-data.service.ts`, `report.service.ts` | Partially Available – **gap** |
| XSS | React escaping by default; DOMPurify on master-code/job-classification views. **Unsanitised `dangerouslySetInnerHTML`** in Personal Time Study (5 places) and `innerHTML` in 2 rich-text editors. No CSP. | Frontend files listed in Section 27 | Partially Available – **gap** |
| Secure headers (helmet/CSP/HSTS) | Not implemented in app; may exist at proxy (not in repo) | `src/main.ts` | Not Available in app |
| CORS | `credentials: true`, origin from `CORS_ORIGIN`. **If unset, any origin is reflected.** | `src/main.ts` | Partially Available – **gap** |
| CSRF | No CSRF token. Mitigated only by `SameSite=Strict` on the refresh cookie (API uses Bearer header). | `auth-cookie.util.ts` | Partially Available |
| Rate limiting / brute force | **Not implemented** (no throttler, no lockout, no OTP attempt limit) | `package.json` | **Not Available** |
| File upload security | Size and MIME allowlists on some endpoints (time-study docs 5 MB, client docs 15 MB, profile images 5 MB). **4 upload endpoints have no limits.** MIME is client-supplied; no magic-byte check; no malware scanning. | Upload controllers (Section 27) | Partially Available – **gap** |
| Error handling | Global exception filter; stack traces not returned. Raw error messages for non-HTTP errors are returned. | `src/core/common/filters/http-exception.filter.ts` | Partially Available |
| Logging | pino; no redaction config. TypeORM SQL query logging is enabled in production. | `src/app.module.ts`, `tenant-connection.manager.ts` | Partially Available – **gap** |
| Audit trail | Field-level audit (who, when, IP, old/new values) on TypeORM insert/update/remove; password/otp/token fields excluded. Raw SQL writes bypass audit. Login audit only goes to the app log (`userloginaudit` table unused). | `src/core/audit/audit.subscriber.ts`, `auth-audit.service.ts` | Partially Available |
| Sensitive data masking | Audit excludes secrets; logs not redacted. Frontend logs the full user-details object to the console. | `AuthContext.tsx` | Partially Available |
| API documentation exposure | Swagger UI always enabled (including production) | `src/main.ts` | **Gap** |
| Secrets management | env-based; hardcoded fallbacks present | Section 27 | **Gap** |
| Dependency security | `xlsx` 0.18.5 (npm) has known CVEs (prototype pollution CVE-2023-30533, ReDoS CVE-2024-22363). It is a dependency in both repos, but payroll uploads are parsed with ExcelJS and no `XLSX.read` call was found, so exposure is low. It should still be upgraded or removed. Puppeteer configured with `--no-sandbox` (generator currently unused). No SCA tooling. | `package.json`, `payrollmanagement.service.ts`, `report-pdf.generator.ts` | **Gap** |

---

## 11. VAPT / Security Audit / Code Review

| Assessment | Auditor | CERT-In | Date | Env | Report | Safe-to-host | Status |
|---|---|---|---|---|---|---|---|
| VAPT (external) | – | – | – | – | – | – | **Not Available – To be obtained from Security/Compliance Team** |
| Source code security review (third-party) | – | – | – | – | – | – | **Not Available – To be obtained from Security/Compliance Team** |
| Internal static code review (this exercise) | Project team (internal, not a certified audit) | N/A | 08-10-2026 | Source code (main / prod branches, local clone) | This document, Section 27 | N/A | Available – findings open |

No security findings were created or assumed beyond what is directly observable in the source code (Section 27).

---

## 12. WAF / DDoS / Network Security

| Control | Status |
|---|---|
| WAF (product, mode, rules, logs, alerting) | Not found in repo – **To be obtained from Infra/Security** |
| DDoS protection | Not found in repo – **To be obtained from Infra/Security** |
| Firewall / IDS / IPS / VPN / segmentation | Not found in repo – **To be obtained from Infra** |
| API gateway / Load balancer / Reverse proxy | Not found in repo – **To be obtained from DevOps** |
| Application-level rate limiting | Not implemented (see Section 10) |

---

## 13. Encryption & Digital Certificates

| Item | Finding | Status |
|---|---|---|
| TLS version / HTTPS | Not configured in the application (plain HTTP listener). Termination point not in repo. | To be obtained from DevOps |
| Certificates (type, CA, validity, renewal) | No certificates in repos | To be obtained from DevOps |
| DB / Redis TLS | Not configured in code | **Gap / Not Verified** |
| Database / file / backup encryption at rest | Not in repo | To be obtained from Infra |
| Password hashing | bcrypt (cost 10) | Available |
| Token mechanism | JWT HS256. Access token 1 h, refresh 7 d with rotation and blacklist. No `iss`/`aud`/token-type claims. | Available – gap noted |
| Token hashing | SHA-256 of refresh tokens for session tracking (but raw token text also stored in `blacklistedtokens`) | Partially Available |
| OTP generation | `Math.random()` (not cryptographically secure) | **Gap** |
| Digital signatures | Not used | Not Applicable |

---

## 14. Incident Management
No incident-management process, escalation matrix, SLA, RCA or incident records exist in the repositories. Zoho Projects is used for issues/defects (including production bugs; see branches `bug/prod`, `issues/prodjuly13`, `issue/prod_july(31)`). **Status: Partially Available (defect tickets only). Incident policy/matrix/RCA: To be obtained `[Org]`.**

---

## 15. Logging & Monitoring

| Item | Finding | Status |
|---|---|---|
| Application logging | pino (JSON) to stdout; level `info` in prod | Available – `src/app.module.ts` |
| Request / access logging | Method, URL (with query string), status, duration, IP, userId, namespace | Available – `src/common/middleware/request-logger.middleware.ts` |
| Audit logging | DB tables `audit_log` / `audit_log_fields`; `GET /audit-history` | Available – see gaps in Section 10 |
| Security logging (login success/fail) | App log only (`auth-audit.service.ts`); failures for unknown users not recorded | Partially Available |
| DB / infrastructure logging | Not in repo | To be obtained from DevOps |
| Monitoring tools (ELK, Grafana, Prometheus, CloudWatch, SIEM) | None configured in repo. **No health-check endpoint** (no `@nestjs/terminus`/`/health`), no metrics, tracing or APM (Prometheus/OpenTelemetry/Sentry). | Not Available in app – infra monitoring To be obtained from DevOps |
| Log retention / alerting / dashboards | Not in repo | To be obtained from DevOps |

---

## 16. CI/CD & Deployment

| Item | Finding | Status |
|---|---|---|
| Source repository | GitHub (`Inventechinfosolutions`) | Available |
| CI tool | **None in repo** (no GitHub Actions, Jenkins, Bitbucket Pipelines) | Not Available |
| Build | Backend `nest build` → `dist/`, run with `node dist/main`. Frontend `tsc -b && vite build`. | Available – `package.json` |
| Test automation / security scanning / container scanning | None | Not Available |
| Artifact repository / image registry | None in repo (no Dockerfile) | Not Available |
| Deployment tool / Kubernetes / Helm / Argo | None in repo | To be obtained from DevOps |
| Approval process | PR merge into `prod` branch (GitHub reviewer settings Not Verified) | Partially Available |
| Rollback mechanism | Not documented | To be obtained from DevOps |
| Pre-commit quality gate | Husky + lint-staged (backend only) | Available |

---

## 17. Infrastructure & Hosting
Hosting model, cloud provider/region, data centre, VMs or Kubernetes, storage, network, firewall, load balancer, backup and DR infrastructure are **not described in the repositories**. Only a developer `docker-compose.yml` (MySQL, Redis, MinIO, Qdrant, Tika, Keycloak, Postgres) exists. **Status: To be obtained from DevOps / Client infrastructure team `[Infra]` / `[Client]`.**

---

## 18. Disaster Recovery & Business Continuity
DR architecture, DR site, RPO/RTO, DR procedure, DR tests and BCP are **not available in the repositories**. **Status: To be obtained from DevOps / Client / Org BCP owner.**

---

## 19. Third-Party Integrations

| System | Purpose | Integration Type | API / Protocol | Authentication | Data Exchanged | Owner | Evidence |
|---|---|---|---|---|---|---|---|
| SMTP mail server (provider not in repo) | OTP, password reset, time-study reminders, notifications | Outbound | SMTP (TLS optional via `SMTP_SECURE`) | Username/password (env) | Recipient email, name, OTP, notification text | To be confirmed | `src/generaladmin/notification/notification.service.ts`, `notification-smtp.service.ts`, `src/config/notification.config.ts` |
| Twilio / generic HTTP SMS (optional) | SMS notifications | Outbound | HTTPS REST | Basic auth (SID/token) / env headers | Phone number, message | To be confirmed (whether enabled in prod) | `notification.service.ts` |
| Google Gemini API | Generates Page Assistant Q&A from uploaded role manuals | Outbound SaaS | HTTPS (`@google/genai`) | API key (env `GEMINI_API_KEY`, missing from `.env.example`) | Extracted manual text and role name only (no employee/payroll data) | To be confirmed (Google account/plan – code comment refers to free tier) | `src/assistant/assistant.service.ts` |
| MinIO (S3-compatible) | Document & file storage | Internal service | S3 API | Access/secret key (env) | User documents, payroll files, profile images | DevOps | `src/core/storage`, `src/common/s3-client` |
| Redis | Cache, OTP, sessions | Internal service | RESP (no TLS configured) | Password (env) | OTPs, token hashes, permissions, notifications | DevOps | `src/core/redis` |
| MySQL | Primary data store | Internal | MySQL protocol (no TLS configured) | User/password (env) | All application data | DevOps/DBA | `src/core/database` |
| Google Fonts | Web fonts | Browser → CDN | HTTPS | None (no SRI) | Client IP / UA | Frontend team | frontend `index.html` |
| Zoho Projects | Issue / requirement tracking (development tool, not the app) | Dev tooling | HTTPS REST (OAuth2) | OAuth refresh token (local file) | Ticket data | PM | `IEBA-V2/scripts/zoho-ticket.js` |
| jsonplaceholder.typicode.com | Leftover demo module (`/users` route) | Browser → public API | HTTPS | None | Demo data | Frontend team – **remove** | frontend `src/features/users/*` |

No payment gateway, banking, Aadhaar, maps/GIS or government-system integrations were found in code.

---

## 20. Project Size & Effort

| Item | Value | Status |
|---|---|---|
| Man-days (total / dev / test / DevOps / architecture / support) | Not in repo | To be obtained from PM (timesheets / Zoho) |
| Team size (from git authors) | ~8 distinct developers across both repos (some with two identities) | Available (git) – roles To be confirmed |
| Testers / DevOps / Architects / Support | Not in repo | To be obtained |
| Function points | Not available | Not Available |
| Number of modules | ~20 business modules (Section 2.3) | Available |
| Number of screens | 24 routed screens (plus modals/drawers) | Available |
| Number of APIs | 330 backend endpoints across 41 controllers | Available |
| Number of integrations | 4 runtime external (SMTP, SMS, Gemini, Google Fonts) + 3 internal infra (MySQL, Redis, MinIO) | Available |
| Number of reports | 22+ PDF report templates, plus Excel/CSV exports | Available |
| Estimation artefacts | Zoho estimate scans and spreadsheets (e.g. `IEBA-V2/docs/I-1-I414_QTR_Month_Rainbow_Estimate.xlsx`, `tmp/I-1-I256-Rainbow-FTE-SalBen-Estimate.xlsx`) | Partially Available |
| SOW / PO / Project plan / Completion certificate | Not in repo | To be obtained from PM / Finance |

---

## 21. Government / Enterprise Project Evidence

| Field | Value | Status |
|---|---|---|
| Client name | Paperless Knowledge Inc. (portal) / US county agencies (end users) | To be confirmed |
| Project name | IEBA V2 | Available |
| Sector | Public sector – county government (time study / cost claiming) | Available (inferred) |
| Scope | Sections 2–3 | Available |
| Contract value | – | To be obtained (if permitted) |
| Duration | Mar 2026 – ongoing | Available (git) |
| Technology | React 19 / NestJS 10 / MySQL / Redis / MinIO | Available |
| Team size / Man-days | See Section 20 | To be obtained |
| Deployment model | Multi-tenant SaaS-style (DB per county) – hosting To be confirmed | Partially Available |
| Completion status | In progress (production branch active) | Available |
| PO / Work order / Completion certificate / Client certificate / SOW | – | **To be obtained from PM / Finance** |

---

## 22. Quality & Certifications
No certification evidence (ISO 9001, ISO 27001, ISO 20000, CMMI, SOC 1/2, PCI DSS, CERT-In empanelment) is present in or relevant to the repositories. **Status: To be obtained from Organization Compliance team `[Org]`** (and from the cloud/data-centre provider `[Infra]` once hosting is confirmed).

---

## 23. Policies Relevant to the Project

| Policy | Exists in repo? | Evidence of implementation in code | Status |
|---|---|---|---|
| Information Security / Data Protection / Data Privacy | No | – | To be obtained `[Org]` |
| Access Control | No | RBAC implemented (Section 7); gaps in Section 27 | To be obtained `[Org]` |
| Password Policy | No | Partial (length/complexity inconsistent; no expiry, history or lockout) | To be obtained `[Org]`; **implementation gap** |
| Encryption / Key Management | No | bcrypt only; no KMS | To be obtained `[Org]` |
| Secure SDLC | Partial (coding standards only: `docs/PROJECT_GUIDE.md`) | Lint/format only; no security testing | To be obtained `[Org]` |
| Incident Response | No | – | To be obtained `[Org]` |
| Backup / DR / BCP | No | – | To be obtained `[Org]/[Infra]` |
| Data Retention / Archival / Purging | No | Not implemented in code | To be obtained `[Org]`; **implementation gap** |
| Change Management | No (PR flow only) | PR merges to `prod` | To be obtained `[Org]` |
| Vulnerability / Patch Management | No | No SCA/Dependabot config in repo | To be obtained `[Org]` |
| WAF / DDoS | No | – | To be obtained `[Infra]` |

For each policy, version, owner, approval authority, effective date and review dates: **To be obtained from Organization Compliance.**

---

## 24. Evidence Register

| # | Assessment Area | Requirement | Evidence Available | Evidence Type | Location / Link | Date | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Project | Repository identification | Yes | Repository | `github.com/Inventechinfosolutions/ieba-v2-backend`, `…/IEBA-Client-Side` | 08-10-2026 | Tech owner (TBC) | Available |
| 2 | Project | Start date / activity | Yes | Repository (git log) | First commits 10-03-2026 / 12-03-2026 | 08-10-2026 | Tech owner | Available |
| 3 | Technology | Frontend stack | Yes | Configuration | `IEBA-Client-Side/package.json` | 07-10-2026 | Frontend lead | Available |
| 4 | Technology | Backend stack | Yes | Configuration | `ieba-v2-backend/package.json` | 07-10-2026 | Backend lead | Available |
| 5 | Architecture | Application architecture | Partial | Document | `ieba-v2-backend/docs/PROJECT_GUIDE.md`, `README.md` | – | Architect | Partially Available (no diagrams; DB stated as PostgreSQL – needs update) |
| 6 | Architecture | Deployment / network / security architecture | No | Architecture diagram | – | – | DevOps | To be obtained |
| 7 | Repository | PR-based merges | Yes | Repository (git history) | `git log --first-parent origin/main` (261/276 BE, 249/263 FE via PR) | 08-10-2026 | Tech owner | Available |
| 8 | Repository | Branch protection / review approvals | No | Screenshot (GitHub settings) | GitHub repo settings | – | GitHub org admin | To be obtained |
| 9 | Repository | Release tags / history | No | Repository | 0 git tags | 08-10-2026 | Tech owner | Not Available |
| 10 | SDLC | Coding standards | Yes | Document / Configuration | `docs/PROJECT_GUIDE.md`, `.eslintrc.js`, `.prettierrc`, `.husky/pre-commit` | – | Tech owner | Available |
| 11 | SDLC | Unit / integration tests | No | Repository | 1 placeholder spec (BE), 0 (FE) | 08-10-2026 | Tech owner | Not Available |
| 12 | SDLC | Defect / requirement tracking | Yes | Ticket | Zoho Projects portal `paperlessknowledgeinc` | – | PM | Available (external) |
| 13 | Authentication | JWT + refresh cookie | Yes | Repository | `src/core/auth/*`, `src/config/jwt.config.ts` | 08-10-2026 | Backend lead | Available |
| 14 | Authentication | MFA (email OTP, per-county toggle) | Partial | Repository | `auth.service.ts`, `settings.service.ts` | 08-10-2026 | Backend lead | Partially Available – weaknesses (S-2) |
| 15 | Authentication | Password hashing (bcrypt) | Yes | Repository | `src/modules/user/service/user.service.ts` | 08-10-2026 | Backend lead | Available |
| 16 | Authentication | Account lockout / failed attempts | No | Repository | – | 08-10-2026 | Backend lead | Not Available |
| 17 | Authentication | Password expiry / history | No | Repository | – | 08-10-2026 | Backend lead | Not Available |
| 18 | Access Control | RBAC (roles / permissions) | Yes | Repository | `permissions.guard.ts`, `role`/`rolepermission` entities | 08-10-2026 | Backend lead | Available – gaps (S-3, S-4) |
| 19 | Access Control | Role-permission matrix document | No | Document | – | – | PM / BA | To be obtained (export from DB) |
| 20 | Access Control | Periodic access review records | No | Report | – | – | Client / Org | To be obtained |
| 21 | Data | Data model (entities) | Yes | Repository | 78 entities in backend `src` | 08-10-2026 | Backend lead | Available |
| 22 | Data | ER diagram / data dictionary | No | Document | – | – | Architect | Not Available |
| 23 | Data | Schema dump | Yes | Repository | `src/core/storage/use uat_v2_trinity;.sql` | – | Backend lead | Available |
| 24 | Audit | Field-level audit trail | Yes | Repository | `src/core/audit/audit.subscriber.ts` | 08-10-2026 | Backend lead | Available (gaps noted) |
| 25 | Logging | Structured app logging | Yes | Configuration | `src/app.module.ts` (nestjs-pino) | 08-10-2026 | Backend lead | Available |
| 26 | Monitoring | Monitoring / alerting dashboards | No | Dashboard | – | – | DevOps | To be obtained |
| 27 | Encryption | TLS / certificates | No | Certificate / Configuration | – | – | DevOps | To be obtained |
| 28 | Encryption | Encryption at rest | No | Configuration | – | – | Infra | To be obtained |
| 29 | Backup | Backup schedule / logs / restore test | No | Backup report | – | – | DevOps / DBA | To be obtained |
| 30 | DR | DR plan / test report / RPO-RTO | No | Report | – | – | DevOps / Client | To be obtained |
| 31 | VAPT | Latest VAPT report / safe-to-host | No | Report / Certificate | – | – | Security/Compliance | To be obtained |
| 32 | WAF / DDoS | WAF & DDoS configuration | No | Configuration / Screenshot | – | – | Infra / Security | To be obtained |
| 33 | CI/CD | Pipeline configuration | No | Configuration | No CI files in repo | 08-10-2026 | DevOps | Not Available |
| 34 | Integrations | Third-party integration list | Yes | Repository | Section 19 | 08-10-2026 | Backend lead | Available |
| 35 | Project credentials | SOW / PO / completion certificate | No | SOW / PO | – | – | PM / Finance | To be obtained |
| 36 | Certifications | ISO / CMMI / SOC | No | Certificate | – | – | Compliance | To be obtained |
| 37 | Policies | Security & IT policies | No | Policy | – | – | Compliance | To be obtained |
| 38 | Security | Internal code review findings | Yes | Report | This document, Section 27 | 08-10-2026 | Security / Tech owner | Available – remediation open |

---

## 25. Repository Review – Mandatory Checks

| Check | Backend | Frontend |
|---|---|---|
| README | Present (accurate for stack; DB-mode docs) | Present but **outdated template** (describes JSONPlaceholder demo) |
| package.json / build files | Present | Present |
| Dockerfile | **Absent** | **Absent** |
| docker-compose | Present (dev infra only; contains dev default credentials) | Absent |
| Kubernetes / Helm | Absent | Absent |
| CI/CD pipelines | Absent | Absent |
| Environment configuration | `.env.example` tracked (contains non-placeholder values – S-6). `.env`/`.env.local` gitignored and never committed (verified in history). | No env template. `.gitignore` covers `*.local` but **not `.env`**. |
| Infrastructure-as-Code | Absent | Absent |
| API documentation | Swagger (`/api/docs`), `docs/user-management-apis.md` | N/A |
| Database / migration scripts | `scripts/*.sql` (15), schema dump; no TypeORM migrations | N/A |
| Authentication / authorization implementation | Present (`src/core/auth`) | Present (route guards, `usePermissions`) |
| Logging / audit trail | Present | Console logging only |
| Security configuration (helmet, rate limiting, CSP) | **Absent** | **Absent** (no CSP) |
| Encryption / certificate configuration | Absent | Absent |
| Third-party integrations | SMTP, SMS, Gemini, MinIO | Google Fonts, demo JSONPlaceholder |
| Monitoring configuration | Absent | Absent |
| Backup scripts | Absent | Absent |
| Deployment documentation | Absent | Absent |

---

## 26. Gaps Summary

| # | Area | Gap | Category |
|---|---|---|---|
| G-1 | Security | Critical/high authentication & authorization defects (Section 27, S-1 to S-5) | **Needs remediation before assessment** |
| G-2 | Authentication | No account lockout, failed-attempt limit, rate limiting, password expiry or password history; inconsistent complexity rules | Missing |
| G-3 | Authentication | MFA is optional per county (default off), and the OTP is returned in API responses | Needs update |
| G-4 | Access Control | No role-permission matrix document; no access-review evidence | Missing |
| G-5 | Architecture | No deployment/network/security architecture diagrams; project guide states PostgreSQL but code uses MySQL | Missing / Needs update |
| G-6 | Data | No ER diagram or data dictionary | Missing |
| G-7 | Data | No retention, archival or purging implementation/policy; no field-level encryption of PII (DOB) or payroll data | Missing |
| G-8 | Testing | Effectively no automated tests; no SAST/DAST/SCA | Missing |
| G-9 | CI/CD | No pipeline, no Dockerfile, no release tags/versioning | Missing |
| G-10 | Repository | Branch protection and PR approval enforcement not verified; direct commits exist on `main`/`prod` | Needs confirmation from GitHub admin |
| G-11 | App security | No helmet/CSP/HSTS; permissive CORS default; Swagger exposed in prod; SQL logging in prod; no malware scanning on uploads | Needs update |
| G-12 | Dependencies | `xlsx` 0.18.5 with known CVEs; Puppeteer `--no-sandbox`; broken `migration:*` scripts (missing `data-source.ts`); no health-check endpoint | Needs update |
| G-13 | Infra | Hosting, TLS, WAF, DDoS, firewall, backup, DR, monitoring, SIEM – not in repo | Needs confirmation from DevOps / Infra |
| G-14 | VAPT | No VAPT report or safe-to-host certificate | To be obtained from Security/Compliance |
| G-15 | Governance | Project owners/PM/architect not documented; no SOW/PO/completion certificate | To be obtained from PM |
| G-16 | Org | Policies and certifications | To be obtained from Compliance |
| G-17 | Hygiene | Frontend demo module calling public API; outdated frontend README; unused `userloginaudit` table; empty chatbot module | Needs update |

---

## 27. RESTRICTED – Security Findings for Security / DevOps Team

> **Distribution: Security / DevOps / Tech owner only. Do not include in external HDFC submission.**
> Findings come from static code review on 08-10-2026 and have **not been exploited or tested at runtime**. They must be validated and remediated, then re-verified, ideally by the VAPT vendor. No secret values are reproduced.

| ID | Severity (internal estimate) | Finding | Evidence (backend unless stated) |
|---|---|---|---|
| S-1 | Critical | **Unauthenticated password reset / account takeover.** `POST /auth/send-otp` is public and returns both the OTP and a signed token for any login ID. `POST /auth/reset-password` only checks that token `sub` equals the body `userId`. It does not check that the OTP was validated or that the token carries the `user:resetpassword` permission. | `src/core/auth/auth.controller.ts` (send-otp, reset-password), `src/core/auth/auth.service.ts` `sendOtp()` return value, `resetPassword()`; `src/core/auth/strategies/jwt.strategy.ts` |
| S-2 | Critical | **OTP returned in API responses** (login and send-otp), which makes 2FA ineffective. The frontend pre-fills it. The OTP is generated with `Math.random()`, has no attempt limit, and the plaintext password is cached in Redis during the OTP step. | `auth.service.ts` (login return, `sendOtp`), `src/core/auth/utils/otp.util.ts`; frontend `src/features/auth/api/login.ts`, `pages/LoginPage.tsx`, `pages/OtpAuthentication.tsx` |
| S-3 | Critical | **Privilege escalation:** any authenticated user can assign or unassign any role (including Super Admin) to any user. The controller has only `JwtAuthGuard`, with no `@Permissions`. | `src/modules/userdepartmentrole/controller/userdepartmentrole.controller.ts` |
| S-4 | High | **Missing permission checks** on several controllers: global user/namespace creation and listing across counties; audit history; document uploader/preview with no tenant/ownership check; master codes; cost-pool assignments; user documents; theme update by arbitrary id; assistant manual upload (any user can replace a role's Q&A bank). Tenant header `X-Tenant-Id` is trusted on public routes. | `src/modules/iebaglobal/controller/global-user.controller.ts`, `src/core/audit/audit.controller.ts`, `document-uploader.controller.ts`, `src/assistant/assistant.controller.ts`, `src/core/tenant/tenant.middleware.ts`, `src/core/tenant/tenant-async.interceptor.ts` |
| S-5 | High | **SQL injection risk** in report stored-procedure invocation: `CALL ${procedureName}(${args})` with string literals not properly escaped; `userIds` not element-validated; procedures use dynamic `PREPARE`. | `src/generaladmin/reports/service/report-data.service.ts`, `report.service.ts` (`toSqlLiteral`), `dto/generatereport.dto.ts` |
| S-6 | High | **Hardcoded secret fallbacks / credentials in source.** JWT access and refresh secret fallbacks; MinIO default key fallbacks; DB `root` with empty-password fallback; hardcoded default user reset password (also echoed in API message and shown in frontend). `.env.example` contains non-placeholder DB/MinIO values. `docker-compose.yml` has dev default credentials. **Rotate any value that matches a real environment.** | `src/config/jwt.config.ts`, `src/config/storage.config.ts`, `src/core/storage/storage.service.ts`, `src/config/database.config.ts`, `src/core/database/tenant-connection.manager.ts`, `src/modules/user/constants/user-defaults.constants.ts`, `.env.example`, `docker-compose.yml`; frontend `src/features/user/api.ts` |
| S-7 | High | **Plaintext OAuth credentials on developer workstation** for Zoho Projects (client secret + non-expiring refresh token) in an untracked file in the workspace root. Not in git, but it should be moved to a secret store and rotated if shared. | `IEBA-V2/scripts/.zoho.env` |
| S-8 | High | **Stored/reflected XSS:** 5 unsanitised `dangerouslySetInnerHTML` sinks with server data; 2 rich-text editors write stored HTML to `innerHTML`. The document preview serves uploads inline with the client-supplied MIME type. No CSP. | Frontend `src/features/PersonalTimeStudy/components/{PersonalTimeStudyMinutesCard,PersonalTimeStudyEntryForm,ApportioningDrawer,PersonalTimeStudyPeriodsSection}.tsx`, `src/features/master-code/components/MasterCodeFormModal.tsx`, `src/features/job-classification/components/JobClassificationFormModal.tsx`; backend `document-uploader.controller.ts` |
| S-9 | Medium | CORS reflects any origin with credentials when `CORS_ORIGIN` is unset; Swagger always on; no helmet; no rate limiting. | `src/main.ts` |
| S-10 | Medium | Session control: access tokens not revocable; deactivation/password change do not revoke sessions; refresh does not re-check user status; raw refresh tokens stored in `blacklistedtokens`. | `auth.service.ts`, `blacklist-token.service.ts` |
| S-11 | Medium | Forced password change can be dismissed by the user (`POST /auth/dismiss-password-change`) and bypassed client-side via a `localStorage` flag. | `auth.controller.ts`; frontend `src/features/auth/utils/buildAuthUser.ts` |
| S-12 | Medium | SQL query logging enabled in production (may log PII/hashes); no log redaction; frontend logs user details to the console. | `tenant-connection.manager.ts`; frontend `src/contexts/AuthContext.tsx` |
| S-13 | Medium | Frontend sends the bearer token to any absolute URL containing `/client/documents/preview/` regardless of host. | Frontend `src/features/reports/pdf/reportPdf.ts` |
| S-14 | Medium | Upload endpoints without size/type limits; no magic-byte validation; no malware scanning. `xlsx` 0.18.5 (known CVEs) remains a dependency (payroll parsing uses ExcelJS). | `document-uploader.controller.ts`, `user-document.controller.ts`, `assistant.controller.ts`, `payrollmanagement.controller.ts` |
| S-15 | Low | User enumeration via distinct login error messages; bcrypt fallback to plaintext if the native module fails to load; Puppeteer `--no-sandbox`; production build fallback API URL is `http://localhost`. | `auth.service.ts`, `user.service.ts`; `report-pdf.generator.ts`; frontend `src/lib/config.ts` |

**Recommended immediate actions before the HDFC assessment:** fix S-1 to S-5, remove the OTP from responses (S-2), remove hardcoded fallbacks and rotate secrets (S-6, S-7), add rate limiting/lockout, helmet/CSP, a restricted CORS origin, and disable Swagger in production. Then commission a VAPT and record revalidation.

---

## 28. Document Register

| Document type | Available? | Location | Owner |
|---|---|---|---|
| Policies | No | – | Compliance |
| VAPT / audit reports | No | – | Security/Compliance |
| Certificates (ISO / SSL / safe-to-host) | No | – | Compliance / DevOps |
| Architecture diagrams | No (text guide only) | `ieba-v2-backend/docs/PROJECT_GUIDE.md` | Architect |
| API documentation | Yes | Swagger `/api/docs`; `ieba-v2-backend/docs/user-management-apis.md` | Backend lead |
| Report calculation guides | Yes | `IEBA-V2/docs/dssrpt-calculation-guides/` (DSSRPT1–5 `.docx` / `.xlsx`) | BA / Backend lead |
| User manuals (7 roles) | Yes | `IEBA-Client-Side/src/documents/*.pdf` | PM |
| Estimates | Partial | `IEBA-V2/docs/I-1-I414_QTR_Month_Rainbow_Estimate.xlsx`, `IEBA-V2/tmp/I-1-I256-Rainbow-FTE-SalBen-Estimate.xlsx` | PM |
| SOW / PO / Completion certificate | No | – | PM / Finance |
| DR / backup reports | No | – | DevOps |
| Schema / DB scripts | Yes | `ieba-v2-backend/src/core/storage/use uat_v2_trinity;.sql`, `ieba-v2-backend/scripts/*.sql` | Backend lead |
