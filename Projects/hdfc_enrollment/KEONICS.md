# KEONICS Portal— Project & Repository Data Submission

**Client context:** KEONICS (Karnataka State Electronics Development Corporation Limited) / Government of Karnataka

| Item | Detail |
|------|--------|
| Prepared from | Repository review of backend and frontend repositories (local clones) |
| Review date | 08-10-2026 |
| Prepared by | [Name / Repository owner] |
| Reviewed by | [Technical owner / PM] |
| Version | 1.0 (draft) |

## How to read this document

Status values used: **Available**, **Partially Available**, **Not Available**, **Not Applicable**, **Not Verified**, **To be obtained from another team**.

Information level:

- **[Project]** = verified in this project’s repositories  
- **[Org]** = organisation-level, to be supplied by the central/security team  
- **[Client]** = client-specific  
- **[Infra]** = infrastructure/hosting team  

Evidence path prefixes:

- **BE** = `keonics-backend`  
- **FE** = `keonics-frontend`  

No passwords, keys, tokens or other secrets are reproduced in this document. Where secrets may exist, they are reported by **location only** (Section 25.2).

---

# A. PROJECT INFORMATION

## 1. Project Identification

| Field | Value | Status | Source / Evidence |
|-------|--------|--------|-------------------|
| Project name | **KEONICS Portal** | Available | FE/`index.html`; FE/`public/site.webmanifest`; BE Swagger title `KEONICS` |
| Client / Department | **KEONICS** — Karnataka State Electronics Development Corporation Limited (UI also cites ISO 9001:2015) | Available (org name) — contracting entity **To be obtained from PM** | FE/`AuthWrapper.tsx`; webmanifest |
| Industry / Domain | Government / PSU e-procurement & operations (goods, HR, training, facility, services, expenditure, infra) | Available | BE/`app.module.ts`; FE/`src/modules/` |
| Project type | **Government** / PSU | Available | branding + module set |
| Project start date | BE first commit **20-12-2024**; FE **26-12-2024** | Available (repository) — contract date **Not Available** | `git log --reverse` |
| Project end date / current status | Active; BE last merge **28-09-2026** (PR #862 on `prod`); FE last commit **29-09-2026** | Available | `git log -1` |
| Project duration (so far) | ~21 months of repository activity | Available | git log |
| Current production status | Deploy scripts/Jenkins/PM2 and env branches (`prod`, `release/uat`, `release/dev`) exist. Live production confirmation **Not Verified** | Not Verified — To be obtained from DevOps | BE/`Jenkinsfile`; deploy scripts |
| Environments | local / dev / uat / prod (env files + branches) | Partially Available | env file names; branches |
| Repository names | `keonics-backend`; `keonics-frontend` | Available | remotes |
| Repository URLs | `https://github.com/Inventechinfosolutions/keonics-backend.git`; `https://github.com/Inventechinfosolutions/keonics-frontend.git` | Available | `git remote -v` |
| Historical CI remote | Bitbucket `inventechinfo-ieba/keonics-backend` referenced in Jenkinsfile | Available | BE/`Jenkinsfile` |
| Repository type | GitHub (current); Bitbucket historically for CI | Available | remotes + Jenkinsfile |
| Repository visibility | Not Verified | Not Verified | — |
| Repository owner / Technical owner | [To be filled] | To be obtained from PM | — |
| Project manager | [To be filled] | To be obtained from PM | — |
| Solution architect | [To be filled] | To be obtained from PM | — |
| DevOps / Infrastructure owner | [To be filled] | To be obtained from DevOps | — |
| Security owner | [To be filled] | To be obtained from Security | — |
| Contributors | BE ~59 identities; FE ~60 identities | Available | `git shortlog -sn --all` |
| Commits / PR merges | BE ~4366 commits / ~737 PR merges; FE ~6752 commits / ~1057 PR merges | Available | git log |
| Current local branches observed | BE: `prod`; FE: `fetaure/change` | Available | `git branch` |

---

## 2. Project Scope (as implemented)

**Business objective** — Multi-module KEONICS operations portal covering goods procurement, HR resources, training centres/students, facility/tenant management, service management, expenditure, plots/buyers, infra mapping/dashboard, and help desk.  
Source: implemented modules (no formal SOW found in repositories).

| Item | Implemented scope | Status | Evidence |
|------|-------------------|--------|----------|
| Major modules | UserAdmin/Master; Goods; HR; Training (+ Training Center); Facility Management; Service Management; Expenditure (+ Vendor); Cart; HelpDesk; Buyers/Plots; Infra mapping & dashboard; Preorders; Approval engine; Mail/RabbitMQ; S3/MinIO; Notifications | Available | BE/`src/`; FE/`src/modules/` |
| User types | VENDORS, DEPARTMENT, KEONICS, EVALUATOR, TRAINING_CENTER, TRAINING_STUDENT, TENANT, FACILITY_MANAGER | Available | BE/`userTypes.enum.ts` |
| Roles | Large role enum (KEONICS_ADMIN, DEPT_*, goods/accounts/HR/training roles, VENDORS, TENANT, SUPER_ADMIN, STUDENT, EVALUATOR, FACILITY_MANAGER, …) | Available | BE/`userRoles.enums.ts` |
| Approximate number of users | Not Available | Not Available | — |
| External systems | MySQL; Redis; MinIO/S3; SMTP; RabbitMQ; svg-captcha; digital signature validation; Filestack key on FE (env) | Available | app.module + env key names |
| APIs exposed | REST `/api/v1`; **~214** controllers; **~1684** HTTP handlers; Swagger enabled; FE/`swagger.json` dump | Available | controller counts; FE/`swagger.json` |
| APIs consumed | SMTP; MinIO; Redis; RabbitMQ; captcha; signer APIs | Available | as above |
| Major workflows | Multi-step approval flows (purchase order, invoice, HR, work order, vendor resource, facility, training center, student enrollment, expenditure, service indent/order, tenant invoice, etc.) | Available | BE/`approval_flows_json/`; approvalFlow module |
| Reports / dashboards | Infra dashboard, training dashboard APIs, goods/HR operational screens | Available | modules + BE/`docs/training-dashboard-api-design.md` |
| Mobile application | Not Applicable (web SPA; responsive helpers only) | Not Applicable | no keonics-mobile repo |
| Web application | Yes — React SPA (Crema/Ant Design) | Available | FE/ |
| Backend services | Single NestJS monolith | Available | BE/ |
| Batch / scheduled jobs | ScheduleModule + tenant help-desk escalation `@Cron` (midnight) | Available | BE tenant-help-desk-escalation service |
| Notification services | Notification module (email via mailer/RabbitMQ; SMS type enum without live SMS adapter found) | Partially Available | notification + mailer |
| File / document processing | MinIO uploads; Puppeteer PDF; ExcelJS/xlsx; instruction PDFs in FE public assets | Available | packages + public PDFs |
| AI/ML | None found | Not Applicable | — |
| Payment gateway SDK | No Razorpay/BillDesk/PayU adapter found; payment entities / offline payment fields exist | Partially Available | entities vs adapters |
| Requirements / SRS / SOW | **No SOW/SRS found** | Not Available | repo search |
| Architecture document | Not Available on mainline; Docker/Helm docs on `origin/k8-branch` only | Partially Available | branch-scoped |
| Functional notes | Training docs, inspection remarks, module PDFs, JDL | Partially Available | BE/`docs/`; FE/`docs/`; FE/`public/*.pdf` |

---

# B. TECHNOLOGY & ARCHITECTURE

## 3. Technology Stack (verified against build files)

### Frontend — Web [Project]

Source: FE/`package.json`, FE/`package-lock.json`

| Item | Value |
|------|--------|
| Framework | React **18.3.1** |
| Language | TypeScript **5.8.x** |
| Build tool | Vite **5.4.18** |
| Package manager | npm |
| UI | Ant Design **5.27.3**, Crema template (`crema-ant-ts` **4.1.1**), styled-components |
| State | Redux + RTK |
| HTTP | axios **1.7.9** |
| Routing | react-router-dom **6.x** |
| Documents / charts | jspdf, html2canvas, apexcharts, recharts |
| Template leftover deps | `@auth0/*`, `aws-amplify`, `firebase` listed; production auth path is JWT (Firebase commented) | Partially Available |
| Automated tests | Only Crema error-boundary specs; **no test script** | Partially Available |

### Backend [Project]

Source: BE/`package.json`, BE/`package-lock.json`, BE/`src/main.ts`

| Item | Value |
|------|--------|
| Framework | NestJS **10.4.22** |
| Language / runtime | TypeScript **5.9.3**; Node **22** referenced in deploy/Docker (k8-branch) |
| Architecture | Large modular NestJS monolith |
| ORM | TypeORM **0.3.28** + mysql2 **3.16.3** |
| Auth | JWT, passport-jwt, bcrypt / bcryptjs (salt rounds **10**) |
| Security | helmet (custom middleware), express-rate-limit, cors, cookie-parser |
| Cache | Redis (ioredis / cache-manager) |
| Object storage | AWS S3 SDK + nestjs-minio-client |
| Messaging | RabbitMQ (amqplib) — `mail_queue` |
| Mail | nestjs-modules/mailer + nodemailer |
| Logging | winston + nest-winston + daily rotate files |
| API docs | @nestjs/swagger |
| PDF / Excel | puppeteer, exceljs, xlsx |
| Captcha | svg-captcha |
| Package name anomaly | `"name": "auth"` (template leftover) | Available |

### Database [Project]

| Item | Value | Evidence |
|------|--------|----------|
| Technology / type | MySQL | TypeORM + mysql2 |
| Server version | Not Verified | To be obtained — Infra |
| Schema management | TypeORM + many `scripts/` SQL alters; `DB_SYNCHRONIZE` env | Available |
| Entities | ~173 `*.entity.ts` (~191 entity/model files total) | Available |
| Base audit columns | createdBy/At, updatedBy/At on BaseEntity | Available |

### Other technologies — verification result

| Technology | Used? | Evidence / note |
|------------|-------|-----------------|
| Redis | Yes | app.module + health checks |
| MinIO / S3 | Yes | s3-client module |
| RabbitMQ | Yes | mailer/rabbitMq.service |
| Docker / Helm | On **`origin/k8-branch` only** — absent on current `prod` HEAD | Partially Available |
| Jenkins | Yes | BE/`Jenkinsfile` |
| PM2 | Yes | deploy shell scripts |
| GitHub Actions | Not found | Not Available |
| Elasticsearch / Kafka / Qdrant | No | — |
| Monitoring APM/Grafana/Prometheus | Not found (Winston files + health module) | Partially Available |
| SIEM / WAF / DDoS | Not in repos | To be obtained |
| Payment gateway SDK | Not found | Partially Available (entities only) |
| SMS gateway | Not found (OTP hardcoded — gap) | Not Available |

---

## 4. Architecture

| Item | Status | Detail / Evidence |
|------|--------|-------------------|
| Application architecture diagram | Not Available | Logical architecture derived below |
| Deployment architecture | Partially Available | Jenkins + SSH + PM2; Helm on k8-branch |
| Network / cloud / on-prem diagrams | Not Available | To be obtained |
| Integration architecture | Partially Available | MinIO, Redis, RabbitMQ, SMTP, signer |
| Data architecture | Partially Available | large entity set; no ER document |
| Authentication architecture | Available (code) | Login + CAPTCHA → JWT access/refresh; Redis/DB blacklist; OTP flows exist but weakened (see §7) |
| Security architecture | Partially Available | Section 10 — note PermissionsGuard gap |

**Logical architecture derived from repository [Project]:**

```
Browser (React + Ant Design / Crema SPA)
              │
              ▼ HTTPS / reverse proxy / WAF — Not Verified
              ▼
NestJS API (/api/v1)  [PM2 on VM; optional K8s on k8-branch]
  ├── MySQL
  ├── Redis (cache / captcha / token blacklist)
  ├── MinIO / S3 (files)
  ├── RabbitMQ (mail queue)
  ├── SMTP (Nodemailer)
  └── Approval engine (JSON flow configs)
```

| Component | Identified | Evidence |
|-----------|------------|----------|
| Application server | NestJS / Node (PM2) | deploy scripts |
| Web SPA hosting | Not Verified in FE repo | — |
| Database / cache / object store / broker | MySQL / Redis / MinIO / RabbitMQ | app.module |
| Identity provider | In-application JWT (no live Auth0/Firebase path) | AppAuthProvider |
| Monitoring | Winston file logs + health checks | main.ts; health module |

---

# C. SECURITY ASSESSMENT & CONTROLS

## 5. Repository & Development Practices [Project]

| Item | Finding | Status | Evidence |
|------|---------|--------|----------|
| Structure | Large Nest modular backend; Crema-based FE modules | Available | trees |
| Branching | develop/main, release/dev, release/uat, prod + many feature branches (~755 BE / ~957 FE remotes) | Partially Available | `git branch -r` |
| Pull requests | Extensive (BE ~737 / FE ~1057 PR merges) | Available | git log |
| Code review / branch protection | Not Verified on GitHub | Not Verified | — |
| Commit hooks | Husky + lint-staged (BE) | Available | BE/`.husky/` |
| CODEOWNERS / tags | Not verified / not documented | Not Available | — |
| Access controls | Not Verified | To be obtained | GitHub/Bitbucket admin |

## 6. SDLC & Development Process

| Area | Finding | Status |
|------|---------|--------|
| Requirement management | No SOW/SRS; module PDFs and training docs only | Partially Available |
| Development | Feature branches + PR merges; Jenkins deploy from Bitbucket historically | Partially Available |
| Testing | Few BE unit specs; e2e scaffold; load-test scripts; FE almost none | Partially Available |
| Security / performance / UAT reports | Not in repos | Not Available |
| Release / change / rollback policies | Not documented beyond deploy scripts | To be obtained |

## 7. Authentication & User Access Management

| Control | Actual implementation | Status | Evidence |
|---------|----------------------|--------|----------|
| Authentication | Username/password → JWT access + httpOnly refresh cookie | Available | public.controller login; auth.controller |
| CAPTCHA | svg-captcha with Redis TTL; FE two-step sign-in | Available | public.service; SigninJwtAuth |
| Password hashing | bcrypt salt rounds **10** | Available | config + hash calls |
| Password change policy | Min 6; requires uppercase, number, special char | Available | changePassword.dto.ts |
| MFA | Not found | Not Available | — |
| OTP | Generate/verify flows for vendor/tenant/FM/evaluator; **static hardcoded OTP in source** (random generation commented out); OTP also returned in response body | Available (critical gap) | vendor/tenant/fcManager services (values not reproduced) |
| SMS OTP delivery | No SMS provider adapter found | Not Available | — |
| Session / refresh | Refresh rotation + Redis/DB blacklist | Available | auth.service |
| RBAC model | Roles, role-permissions, menus, post permissions; FE loads `/user/my-permissions` | Available | userAdmin + FE JWTAuthProvider |
| PermissionsGuard | **Always returns true** (real checks commented out) | Available (critical gap) | `permissions.guards.ts` |
| RolesGuard | Does not effectively match required roles | Available (weak) | `roles.guard.ts` |
| JwtAuthGuard | Widely applied | Available | controllers |
| Account lockout | `LOCKED` enum exists; **no failed-attempt lockout in login()** | Partially Available | user.service login |
| Default passwords in provisioning | Hardcoded default password literals hashed in source | Available (gap — values not copied) | personalDetails.service |
| Digital signature / DSC | Public validation APIs + FE signer env / test-signer | Available | public.service; test-signer module |

## 8. Data Model & Data Dictionary

| Item | Status | Evidence |
|------|--------|----------|
| ER diagram / formal Data Dictionary | Not Available | — |
| Entities | ~173–191 entity/model files | Available |
| Important domains | users/personal details; goods; HR; training; facility/tenant; expenditure/vendors; plots/buyers; infra; help desk; approval process/task instances | Available |
| PII | email, mobile, PAN, Aadhaar, GSTIN, bank account/IFSC, KGID, student/employee/vendor contacts | Available |
| Financial | PO/invoice/payment entities; offline payment fields | Available |
| Auth data | password hashes; tokens blacklist | Available |
| Central audit_logs module | **Not found** (base entity timestamps + process history instead) | Partially Available / Not Available |

## 9. Data Storage & Handling

| Area | Finding | Status |
|------|---------|--------|
| Storage | MySQL + MinIO/S3 + Redis + RabbitMQ + Winston log files | Available |
| Hosting model | VM + PM2 evidenced; K8s optional on k8-branch | Partially Available |
| Encryption at rest | Not documented | To be obtained |
| Encryption in transit | Prod HTTPS Not Verified | Not Verified |
| Secret management | Env files; AES-256-CBC encrypted `.env.prod.enc` + MASTER_KEY loader when `ENCRYPTED=true` | Available |
| Env files tracked in git | BE & FE track `.env*`; BE `.gitignore` has `#.env` commented out | Available (critical gap) |
| Backup / DR / retention / purge | Not in repos | To be obtained |

## 10. Application Security

| Control | Status | Evidence |
|---------|--------|----------|
| Helmet / CSP / HSTS / frameguard | Available | CustomHelmetMiddleware |
| CORS | Available | env-driven allowlist + localhost |
| Rate limiting | Available | express-rate-limit 250/min (comment inconsistency) |
| Nest Throttler package | Present but **not wired in src** | Partially Available |
| ValidationPipe | Present; **no whitelist/forbidNonWhitelisted** observed | Partially Available |
| Body size limit | 30mb | Available |
| AuthN | Available | JWT + captcha |
| AuthZ / RBAC enforcement | **Gap** — PermissionsGuard no-op | Available (as gap) |
| OTP security | **Gap** — hardcoded OTP | Available (as gap) |
| SQL injection mitigation | Available | TypeORM |
| Logging / trace id | Available | Winston + TraceIdMiddleware |
| Secrets in VCS / hardcoded hosts | Gap | Section 25.2 |

## 11. VAPT / Security Audit / Code Review

**Not Available – To be obtained from Security/Compliance Team.**

## 12. WAF / DDoS / Network Security

**To be obtained from Infra/Security.** Not present in application repositories.

## 13. Encryption & Digital Certificates

| Area | Finding | Status |
|------|---------|--------|
| TLS / cert inventory | Not Verified | To be obtained |
| Password hashing | bcrypt (10) | Available |
| JWT | Access + refresh + activation secret env keys | Available |
| Env encryption at rest (file) | AES-256-CBC `.env.prod.enc` | Available |
| Digital signatures / DSC | Validation APIs + FE signer | Available |
| Private keys / secrets | **Not shared** | — |

## 14. Incident Management

**Not Available** in project repos. **To be obtained from Security/Operations [Org].**

## 15. Logging & Monitoring

| Item | Finding | Status |
|------|---------|--------|
| Application logging | Winston daily rotate (100m / 14d) under `logs/` | Available |
| Health checks | MySQL, MinIO, Redis | Available |
| Central SIEM / Grafana / Prometheus / Sentry | Not found | Not Available |
| Load testing artefacts | BE/`test/load-testing/` | Available |
| FE web-vitals | Present | Partially Available |

## 16. CI/CD & Deployment

| Item | Finding | Status |
|------|---------|--------|
| Jenkins | BE/`Jenkinsfile` — Bitbucket checkout, npm build, SSH deploy | Available |
| Deploy scripts | `keonics-deployment.sh`, `keonics-backend-dev.sh`, `keonics-backend-prod.sh` + PM2 | Available |
| Docker / Helm | On `origin/k8-branch` only | Partially Available |
| FE CI | Not found | Not Available |
| GitHub Actions | Not found | Not Available |
| Security/container scanning in pipeline | Not evidenced | Not Available |

## 17. Infrastructure & Hosting

| Item | Status | Evidence |
|------|--------|----------|
| Hosting model | VM + PM2 evidenced; K8s optional | deploy scripts; k8-branch |
| Host hints | Internal IP / non-standard SSH ports / users present in Jenkinsfile | Available (location only — do not treat as public inventory without Infra confirmation) |
| Paths | `/home/inventech{3,4}/keonics/keonics-backend` | Available |
| Object storage / Redis / RabbitMQ / SMTP | Env-configured | Available |
| Public API hostname mention | Example `https://api.keonics.in` in docs | Partially Available |
| Timezone | Asia/Kolkata | Available |

## 18. Disaster Recovery & Business Continuity

**Not Available** in repositories. **To be obtained from Infra.**

## 19. Third-Party Integrations

| System | Purpose | Type | Auth | Data | Status |
|--------|---------|------|------|------|--------|
| MinIO / S3 | Files/documents | Object API | Env keys | Files | Available |
| Redis | Cache / captcha / blacklist | Cache | Env | Tokens/cache | Available |
| RabbitMQ | Mail queue | AMQP | Env | Mail jobs | Available |
| SMTP | Email | SMTP | Env | Mail | Available |
| Digital signer / DSC | Signature validation | API | Config | Signatures | Available |
| Filestack (FE env) | File picking (if enabled) | Client | Env key | Files | Partially Available |
| SMS gateway | OTP delivery | — | — | — | Not Available (OTP hardcoded) |
| Payment gateway | Online payments | — | — | — | Not Available as SDK |
| Auth0 / Amplify / Firebase | Template leftovers | — | — | — | Not used as primary auth |

## 20. Project Size & Effort

| Metric | Value | Status |
|--------|-------|--------|
| Man-days / commercials | Not Available | To be obtained from PM |
| Git contributors | ~59–60 identities | Partially Available |
| Modules | Very large multi-domain portal | Available |
| APIs | ~1684 handlers / ~214 controllers | Available |
| Entities | ~173–191 | Available |
| Approval flows | Many JSON configs | Available |

## 21. Government / Enterprise Project Evidence

| Field | Value | Status |
|-------|--------|--------|
| Client | KEONICS | Available |
| Project | KEONICS Portal | Available |
| Sector | Government / PSU | Available |
| Scope | Multi-module procurement & operations portal | Available (code) |
| PO / completion certificates | Not in repos | To be obtained |
| Deployment | Jenkins + PM2 (+ optional K8s) | Partially Available |

## 22. Quality & Certifications

| Item | Status |
|------|--------|
| ISO 9001:2015 | Mentioned in UI marketing copy only — certificate artefact **Not Available** in repos | Partially Available / To be obtained |
| Other org/project certs | Not Available | To be obtained from Compliance |

## 23. Policies Relevant to the Project

ISMS policy set: **Not Available** in repos. **To be obtained [Org].**

---

# D. EVIDENCE REGISTER (mandatory)

| # | Assessment Area | Requirement | Evidence Available | Evidence Type | Location / Link | Date | Owner | Status |
|---|-----------------|-------------|-------------------|---------------|-----------------|------|-------|--------|
| 1 | Project ID | Client & portal name | Yes | UI / Swagger | FE index.html; BE main.ts | 08-10-2026 | Project | Available |
| 2 | Repositories | Source control | Yes | Git remote | Inventechinfosolutions/keonics-* | 08-10-2026 | Project | Available |
| 3 | Stack | NestJS / React / MySQL / Redis / MinIO / RabbitMQ | Yes | package.json / app.module | BE & FE | 08-10-2026 | Project | Available |
| 4 | Auth | JWT + CAPTCHA | Yes | Source | BE public/auth; FE Signin | 08-10-2026 | Project | Available |
| 5 | CI/CD | Jenkins + PM2 | Yes | Config / scripts | BE/`Jenkinsfile`; deploy sh | 08-10-2026 | DevOps | Available |
| 6 | K8s | Helm/Docker | Partial | Branch | `origin/k8-branch` | 08-10-2026 | DevOps | Partially Available |
| 7 | Logging | Winston rotate | Yes | Source | BE/`main.ts` | 08-10-2026 | Project | Available |
| 8 | Health | Dependency health | Yes | Source | BE/`src/health/` | 08-10-2026 | Project | Available |
| 9 | OTP | Production-grade OTP | No | Source gap | vendor/tenant OTP services | 08-10-2026 | Project | Gap |
| 10 | AuthZ | Permission enforcement | No | Guard no-op | `permissions.guards.ts` | 08-10-2026 | Project | Gap |
| 11 | Secrets in git | Tracked `.env*` | Yes | git ls-files | BE & FE roots | 08-10-2026 | Security | Gap |
| 12 | VAPT | Report | No | Report | — | — | Security | To be obtained |
| 13 | WAF/DDoS | Protection | No | Config | — | — | Infra | To be obtained |
| 14 | Backup/DR | Evidence | No | Report | — | — | Infra | To be obtained |
| 15 | SOW | Formal SOW | No | Document | — | — | PM | Not Available |
| 16 | Policies / Certs | ISMS / ISO artefacts | No | Policy/Cert | — | — | Compliance | To be obtained |
| 17 | PR history | Pull requests | Yes | Git | BE~737 / FE~1057 | 08-10-2026 | Project | Available |
| 18 | API docs | OpenAPI dump | Yes | swagger.json | FE/`swagger.json` | 08-10-2026 | Project | Available |

---

# E. DOCUMENT REGISTER

| Document | Location | Status |
|----------|----------|--------|
| Backend README | BE/`README.md` (template-quality) | Partially Available |
| Training dashboard API design | BE/`docs/training-dashboard-api-design.md` | Available |
| Inspection remarks guides | BE/`docs/frontend-inspection-remarks.md`; FE/`docs/*` | Available |
| JHipster JDL | BE/`jhipster-jdl.jdl` | Available |
| Module instruction PDFs | FE/`public/*.pdf`, FE/`src/assets/*.pdf` | Available |
| OpenAPI dump | FE/`swagger.json` | Available |
| Docker/Helm docs | `origin/k8-branch` only | Partially Available |
| SOW / SRS / Architecture pack | — | Not Available |
| VAPT / DR / PO / org policies / certificates | — | Not Available / To be obtained |
| This assessment | FE/`docs/HDFC-Vendor-Assessment-KEONICS.md` | Available (draft) |

---

# F. GAPS

| # | Gap | Severity | Action owner |
|---|-----|----------|--------------|
| G1 | No formal SOW/SRS in repositories | Medium | PM / Client |
| G2 | Hardcoded static OTP + OTP returned in API response | Critical | Project / Security |
| G3 | PermissionsGuard always allows; weak RolesGuard | Critical | Project / Security |
| G4 | `.env*` tracked in git (BE & FE); BE ignore commented out | Critical | Security / DevOps |
| G5 | No failed-login lockout despite LOCKED enum | Medium | Project |
| G6 | Default passwords hashed in provisioning source | High | Project / Security |
| G7 | ValidationPipe lacks whitelist/forbidNonWhitelisted | Medium | Project |
| G8 | Docker/Helm not on mainline `prod` branch | Medium | DevOps |
| G9 | No VAPT / WAF / DR / backup evidence | High | Security / Infra |
| G10 | No central audit_logs module (unlike CDRMS/CAS) | Medium | Project |
| G11 | SMS gateway & payment gateway SDKs absent | Medium | Project / Client |
| G12 | Org policies & certificate artefacts not attached | High | Compliance |
| G13 | Jenkins/host credentials present in repo (location only) | High | DevOps / Security |
| G14 | Sparse automated FE tests; limited BE unit coverage | Medium | Project |

### Availability summary

| Bundle | Overall |
|--------|---------|
| A. Project Information | Available (owners/commercials partial) |
| B. Technology & Architecture | Available (diagrams/hosting partial; K8s branch-scoped) |
| C. Security Assessment | Partially Available — **critical AuthZ/OTP/secrets gaps** |
| D–F | Available (draft) |

---

## 25. Repository Review — Mandatory Checks

| Check | BE | FE |
|-------|----|----|
| README / package.json | Available (README weak) | Available |
| Dockerfile / Helm | On k8-branch only | Not Available |
| CI/CD | Jenkins + deploy scripts | Not Available |
| Env configuration | Present — **tracked in git (gap)** | Present — **tracked `.env` (gap)** |
| Auth / JWT / CAPTCHA | Available | Available |
| Effective permission enforcement | **Gap** | Client trusts API |
| Logging / health | Available | Partial (web-vitals) |
| Integrations | MinIO/Redis/RabbitMQ/SMTP | Filestack env / signer |
| Backup scripts / monitoring dashboards | Not Available | Not Available |

### 25.2 Secrets hygiene (location only)

| Finding | Action |
|---------|--------|
| BE tracks `.env`, `.env.dev`, `.env.local`, `.env.prod`, `.env.prod.enc`, `.env.uat` | Rotate; untrack; fix `.gitignore` |
| FE tracks `.env` | Same |
| Jenkinsfile contains host/users/credential IDs | Review with DevOps; avoid publishing |
| Hardcoded OTP / default password literals in source | Fix immediately; do not paste values into assessment |
| FE axios hardcoded internal API hosts | Move to env; scrub if public |

---

## 26. Final Submission Pack Checklist

| Pack | Status |
|------|--------|
| A. Project Information | Complete (draft) — fill named owners |
| B. Technology & Architecture | Complete (draft) |
| C. Security Assessment | Complete (draft) with critical gaps flagged |
| D. Evidence Register | Complete (draft) |
| E. Document Register | Complete (draft) |
| F. Gaps | Complete |

---

**End of document — KEONICS Portal Project & Repository Data Submission v1.0 (draft)**  
Prepared for consolidation into the organisation-level HDFC Vendor Onboarding and Security Assessment checklist.
