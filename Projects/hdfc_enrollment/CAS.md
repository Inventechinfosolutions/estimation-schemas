# CA Site Allotment & Institution Registration Portal (CAS)— Project & Repository Data Submission

**Client context:** BDA / Government of Karnataka

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

- **BE** = `cas-backend`  
- **FE** = `cas-frontend`  

No passwords, keys, tokens or other secrets are reproduced in this document. Where secrets may exist, they are reported by **location only** (Section 25.2).

---

# A. PROJECT INFORMATION

## 1. Project Identification

| Field | Value | Status | Source / Evidence |
|-------|--------|--------|-------------------|
| Project name | **CAS** — CA Site Allotment & Institution Registration Portal | Available | FE/`index.html`; FE/`src/locales/en.json`; BE initial commit message |
| Client / Department | **BDA** (references in README / product copy) | Partially Available — confirm legal entity with PM | BE/`README.md` |
| Industry / Domain | Government e-Governance — civic amenity (CA) site allotment, institution registration, renewal, payments | Available | FE modules; BE domain folders |
| Project type | **Government** | Available | BDA context + module set |
| Project start date | First commits **04-02-2026** (BE & FE) | Available (repository) — contract date **Not Available** | `git log --reverse` |
| Project end date / current status | Active development; last merges **08-10-2026** (BE PR #175, FE PR #297) | Available | `git log -1` |
| Project duration (so far) | ~35 weeks / ~246 days of repository activity | Available | git log |
| Current production status | Branches include `prod`, `uat`, `release/uat`. Prod CORS placeholder `https://cas.example.com`. Live production confirmation **Not Verified** | Not Verified — To be obtained from DevOps | `git branch -r`; BE env templates (hostnames only) |
| Environments | Local / dev / uat / prod (env templates + branches) | Partially Available | BE env file names; branches |
| Repository names | `cas-backend`; `cas-frontend` | Available | remotes |
| Repository URLs | `https://github.com/Inventechinfosolutions/cas-backend.git`; `https://github.com/Inventechinfosolutions/cas-frontend.git` | Available | `git remote -v` |
| Repository type | GitHub (organisation: **Inventechinfosolutions**) | Available | remotes |
| Repository visibility | Not Verified | Not Verified | — |
| Repository owner / Technical owner | [To be filled] | To be obtained from PM | — |
| Project manager | [To be filled] | To be obtained from PM | — |
| Solution architect | [To be filled] | To be obtained from PM | — |
| DevOps / Infrastructure owner | [To be filled] | To be obtained from DevOps | — |
| Security owner | [To be filled] | To be obtained from Security | — |
| Contributors (git authors) | BE ~21 identities; FE ~20 identities (top: Darshini G B, Dhruthi863, shiva-Inventech, …) | Available | `git shortlog -sn --all` |
| Commits / PR merges | BE ~657 commits / ~172 PR merges; FE ~1314 commits / ~292 PR merges | Available | git log |
| Tags | **0** on both repos | Available | `git tag` |

---

## 2. Project Scope (as implemented)

**Business objective** — Digitize CA site allotment: institution registration, notifications, CA applications, evaluation workflows, payments, renewals, refunds, digital signing, and admin masters.  
Source: implemented modules in BE/`src/` and FE/`src/` (no formal SOW found).

| Item | Implemented scope | Status | Evidence |
|------|-------------------|--------|----------|
| Major modules | Admin (auth/users/masters); applicant/institution registration; notification; CA application / CA site application; renewal; finance; refund; Razorpay; SMS; mail; audit; dashboard; digital certificate; document uploader; announcement; manuals; approval-flow engine | Available | BE/`src/`; FE/`src/modules/` |
| User types | applicant, caseworker, hod, superintendent, finance/accounts chain, super_admin, zone roles, engineering/legal/finance/institution roles | Available | BE/`userTypes.enum.ts`; `roleCode.enum.ts` |
| Approximate number of users | Not Available | Not Available | — |
| External systems integrated | MySQL; Redis (optional); MinIO/S3; SMS gateway; SMTP; Razorpay; DSC/Signabyte signing | Available | modules + env key names |
| APIs exposed | REST under `/api/v1`; **~51** controllers; **~355** HTTP handlers; Swagger `/api/docs` when enabled | Available | BE controllers; BE/`README.md` |
| APIs consumed | SMS API; SMTP; Razorpay; MinIO/S3; Redis | Available | as above |
| Major workflows | Staff login (password + captcha) → JWT; applicant OTP login → institution registration → caseworker/superintendent/HOD review → CA applications → evaluation → Razorpay payment → allotment → renewal/refund/finance | Available | controllers + FE routes |
| Reports / dashboards | Dashboard module (CA site scopes) | Available | BE/`src/dashboard/`; FE/`src/modules/dashboard/` |
| Mobile application | Not Applicable (responsive web only) | Not Applicable | no mobile repo |
| Web application | Yes — React SPA, base path `/casite/` | Available | FE/; FE/`vite.config.ts` |
| Backend services | Single NestJS API | Available | BE/`package.json` |
| Batch / scheduled jobs | None found (`@Cron` / `@Interval` absent) | Available (verified absent) | source search |
| Notification services | In-app notifications + SMS OTP + SMTP mail | Available | BE notification/sms/mail modules |
| File / document processing | Object store uploads; PDF (pdfkit / @react-pdf); Excel (xlsx); digital signing | Available | packages + modules |
| AI/ML | None | Not Applicable | dependency review |
| Requirements / SRS / SOW | **No SOW/SRS found** | Not Available | repo search |
| Architecture document | Not Available | Not Available | — |
| Functional / technical notes | FE/`PROJECT_STRUCTURE.md`; FE/`docs/*`; BE/`README.md`; SQL under BE/`docs/sql/` | Partially Available | as listed |

---

# B. TECHNOLOGY & ARCHITECTURE

## 3. Technology Stack (verified against build files)

### Frontend — Web [Project]

Source: FE/`package.json`, FE/`package-lock.json`, FE/`vite.config.ts`

| Item | Value |
|------|--------|
| Framework | React **19.2.4** |
| Language | TypeScript **5.9.3** |
| Build tool | Vite **7.3.1** |
| Package manager | npm |
| Routing | react-router-dom **7.13.0** |
| State | TanStack Query **5.90.20**; Redux Toolkit **2.11.2** |
| HTTP | axios **1.13.4** |
| Forms / validation | react-hook-form, zod |
| UI | antd **6.2.3**, Tailwind **3.4.19**, lucide-react, framer-motion, recharts |
| i18n | English / Kannada locales |
| Documents | @react-pdf/renderer; xlsx-js-style |
| Deploy path | Vite `base: '/casite/'` |
| Automated tests | None found |
| Docker / CI | Not Available |

### Backend [Project]

Source: BE/`package.json`, BE/`package-lock.json`, BE/`Dockerfile`, BE/`README.md`

| Item | Value |
|------|--------|
| Framework | NestJS **10.4.22** |
| Language / runtime | TypeScript **5.9.3**; Node **20** (Dockerfile `node:20-alpine`) |
| Architecture | Modular NestJS monolith |
| ORM | TypeORM **0.3.28** |
| DB driver | mysql2 **3.16.2** |
| Auth | @nestjs/jwt, passport-jwt, bcrypt (salt rounds **12**) |
| Security libs | helmet, @nestjs/throttler, class-validator, sanitize-html, cookie-parser, cors |
| Object storage | @aws-sdk/client-s3 (MinIO) |
| Cache | cache-manager + Redis (optional) |
| Metrics | prom-client |
| Mail / SMS / Payments | nodemailer; custom SMS module; Razorpay module |
| Automated tests | Jest configured; **0** unit specs under `src/`; e2e scaffold only |

### Database [Project]

| Item | Value | Evidence |
|------|--------|----------|
| Technology / type | MySQL (relational) | mysql2; README |
| DB names (config) | `cas` / `dev_cas_db` / `CAS` | env templates (names only) |
| Server version | Not Verified | To be obtained — Infra |
| Schema management | TypeORM entities + `src/migrations/*` + `docs/sql/*` | Available |
| Tables / entities | ~48 entity files / ~55+ `@Entity` tables | Available |

### Other technologies — verification result

| Technology | Used? | Evidence / note |
|------------|-------|-----------------|
| Redis | Optional | env keys + cache |
| MinIO / S3 | Yes | object-store / s3-client |
| Docker | Backend yes; Frontend no | BE/`Dockerfile`, `docker-compose.yml` |
| Elasticsearch / Kafka / RabbitMQ | No | dependencies |
| API gateway / Nginx / K8s / Helm / Argo | Not found (FE/`nginx/` empty dir) | Not Verified / Not Available |
| Jenkins / GitHub Actions | Not found | Not Available |
| Monitoring | Prometheus metrics endpoint `/api/v1/metrics`; health `/api/v1/health` | Partially Available |
| SIEM / WAF / DDoS | Not in repos | To be obtained from Infra/Security |
| Cloud / third-party | Razorpay, SMS, SMTP | Available (code) |

---

## 4. Architecture

| Item | Status | Detail / Evidence |
|------|--------|-------------------|
| Application architecture diagram | Not Available | Logical architecture derived below |
| Deployment / network / cloud diagrams | Not Available | To be obtained from DevOps/Infra |
| Integration architecture | Partially Available | Razorpay, SMS, SMTP, MinIO, Redis |
| Data architecture | Partially Available | entities + migrations; no ER diagram |
| Authentication architecture | Available (code) | Staff: password + captcha → JWT; Applicant: SMS OTP → JWT; refresh cookies + CSRF; token blacklist |
| Security architecture | Partially Available | Section 10 |

**Logical architecture derived from repository [Project]:**

```
Browser (React SPA, base /casite/, EN/KN)
              │
              ▼ HTTPS / reverse proxy / WAF — Not Verified
              ▼
NestJS API (/api/v1)  [Docker Node 20]
  ├── MySQL (CAS)
  ├── Redis (optional — cache / rate / blacklist)
  ├── MinIO/S3 (documents)
  ├── SMS gateway (OTP)
  ├── SMTP (mail)
  └── Razorpay (checkout + webhook/callback)
```

| Component | Identified | Evidence |
|-----------|------------|----------|
| Application server | NestJS on Node 20 | Dockerfile; main.ts |
| Web server for SPA | Not Verified (Vite build; nginx dir empty) | FE/`vite.config.ts` |
| Database / cache / object storage | MySQL / Redis / MinIO | as above |
| Message broker | None | — |
| Identity provider | In-application (no external IdP) | admin auth |
| Monitoring | Health + Prometheus metrics | app.controller |

---

# C. SECURITY ASSESSMENT & CONTROLS

## 5. Repository & Development Practices [Project]

| Item | Finding | Status | Evidence |
|------|---------|--------|----------|
| Repository structure | BE modular Nest `src/*`; FE modules under `src/modules`, `src/ca-*` | Available | tree |
| Branching | Feature branches → `main`; also `prod`, `uat`, `release/uat`, `uat_legacy` | Partially Available | `git branch -r` |
| Pull requests | Heavily used (BE ~172, FE ~292 PR merges) | Available | git log |
| Code review / branch protection | Not Verified on GitHub | Not Verified | — |
| Commit standards | Husky + lint-staged + Commitizen on BE | Partially Available | BE/`.husky/` |
| CODEOWNERS / tags / release notes | Not Available (0 tags) | Not Available | — |
| Access controls | Not Verified | To be obtained | GitHub org admin |

## 6. SDLC & Development Process

| Area | Finding | Status |
|------|---------|--------|
| Requirement management | No SOW/SRS in repos | Not Available |
| Development / PR process | Feature branch + PR merges | Partially Available |
| Unit / integration / UAT / security / performance testing | Minimal automated tests; no formal reports | Not Available / Partially Available |
| Release / change / rollback policies | Not in repos | To be obtained |

## 7. Authentication & User Access Management

| Control | Actual implementation | Status | Evidence |
|---------|----------------------|--------|----------|
| Staff authentication | LoginId + password (XOR transport header) → bcrypt → captcha → JWT access + refresh cookie | Available | BE/`public.controller.ts`; `user.service.ts` |
| Applicant authentication | Mobile OTP via SMS (`send-otp` / `verify-otp`) → JWT | Available | BE/`applicant.controller.ts`; sms module |
| Authorization / RBAC | JwtAuthGuard + PermissionsGuard + `@Permissions`; role/permission/post-permission tables | Available | BE auth guards |
| MFA | Not implemented | Not Available | — |
| Captcha | Staff login step-2 | Available | captcha / user_captcha |
| Password hashing | bcrypt salt rounds **12** | Available | `security.constants.ts` |
| Password complexity (API) | Create-user DTO: no MinLength/complexity rules | Partially Available | `createUser.dto.ts` |
| OTP flood controls | Cooldown, max sends, max verify failures; throttler on auth | Available | applicant.service; AppThrottlerGuard |
| Failed login lockout | `LOCKED` status enum exists; automatic lockout after N failures **not found** | Partially Available | userStatus.enum |
| Session timeout | `SESSION_TIMEOUT_MINUTES` (default **60** if unset) | Available | auth session-config |
| CSRF / refresh | Double-submit CSRF + refresh + blacklist tokens | Available | CsrfGuard; blacklistedtokens |
| FE auth bypass | `config.bypassAuth` **defaults true** unless `VITE_BYPASS_AUTH=false` | Available (gap) | FE/`src/lib/config.ts` |
| Privilege / PAM / access reviews | Not in repos | To be obtained | — |

## 8. Data Model & Data Dictionary

| Item | Status | Evidence |
|------|--------|----------|
| ER diagram / formal Data Dictionary | Not Available | — |
| Schema / entities | Available | BE entities (~48 files) |
| Important entities | users, personal_details, posts/roles/permissions, applicant, institution_registration, ca_application, ca_site_application, cas_payment, renewals/finance/refund, audit_logs, sms_audit, object_store, approval process/tasks, digital_certificate, login_history, captcha, blacklist | Available |
| PII | name, email, mobile, gender, address, PAN, bank account/IFSC, signatory details, documents | Available |
| Financial data | cas_payment, Razorpay IDs, amounts | Available |
| Auth data | password hash; applicant otp_code + expiry | Available |
| Audit data | audit_logs + interceptor; sms_audit; login_history | Available |

## 9. Data Storage & Handling

| Area | Finding | Status |
|------|---------|--------|
| Storage | MySQL + MinIO/S3 + optional Redis | Available (code) |
| On-prem / Cloud / Hybrid | Not defined in repos | To be obtained — Infra |
| Encryption at rest | Not documented | To be obtained |
| Encryption in transit | Prod HTTPS Not Verified; secure cookie flags via environment | Partially Available |
| Secret management | Env files; **BE `.env*` files are tracked in git** (critical gap) | Available (as gap) |
| Backup / archival / retention / purge | Not in repos | To be obtained |

## 10. Application Security

| Control | Status | Evidence |
|---------|--------|----------|
| Input validation / sanitize-html | Available | ValidationPipe + SanitizePipe |
| AuthN / AuthZ / RBAC / session | Available | Section 7 |
| Password security | Partially Available | bcrypt12; weak DTO complexity |
| Helmet / CSP / HSTS | Available (env toggles) | BE/`main.ts` |
| CORS | Available | allowlist + Razorpay origins |
| Rate limiting | Available | Nest throttler + OTP never skipped |
| FE security headers / anti-clickjack / XSS checks | Available | FE/`vite.config.ts`; `xssValidation.ts` |
| CSRF | Available | CsrfGuard |
| SQL injection mitigation | Available | TypeORM |
| File upload / object store | Available | document uploader + MinIO |
| Brute-force lockout | Partially Available / gap | enum only |
| Audit trail / logging | Available | audit interceptor |
| Password transport | XOR obfuscation (not cryptography) | Available (gap) | password-transport utils |

## 11. VAPT / Security Audit / Code Review

**Not Available – To be obtained from Security/Compliance Team.**  
FE Vite comments reference VAPT findings; **no VAPT report artefact** in repositories.

## 12. WAF / DDoS / Network Security

**To be obtained from Infra/Security.** Not configured in application repositories.

## 13. Encryption & Digital Certificates

| Area | Finding | Status |
|------|---------|--------|
| TLS / HTTPS / cert inventory | Not Verified in repos | To be obtained |
| Password hashing | bcrypt (12 rounds) | Available |
| JWT | Access + refresh | Available |
| Digital signing | Digital certificate / DSC Signabyte module | Available (code) |
| Private keys / secrets | **Not shared** | — |

## 14. Incident Management

**Not Available** in project repos. **To be obtained from Security/Operations [Org].**

## 15. Logging & Monitoring

| Item | Finding | Status |
|------|---------|--------|
| Application / security event logging | Nest Logger; SECURITY_EVENT / LOGIN_FAILED JSON | Available |
| Audit logging | audit_logs | Available |
| Health / metrics | `/api/v1/health`, `/api/v1/metrics` (Prometheus) | Available |
| ELK / Grafana / SIEM / APM | Not in repos | Not Available / To be obtained |

## 16. CI/CD & Deployment

| Item | Finding | Status |
|------|---------|--------|
| GitHub Actions / Jenkins | Not found | Not Available |
| Docker | BE Dockerfile + compose; FE none | Partially Available |
| K8s / Helm | Not found | Not Available |
| Approval / rollback docs | Not Available | To be obtained |

## 17. Infrastructure & Hosting

| Item | Status | Evidence |
|------|--------|----------|
| Hosting model / cloud / DC | To be obtained | — |
| Port hints | APP_PORT templates 3500 / 2700; FE API localhost:3500 | Partially Available |
| SPA base | `/casite/` | Available |
| Prod URL | Placeholder `cas.example.com`; payment host hint `cas-payments.inventech-developer.in` | Partially Available |

## 18. Disaster Recovery & Business Continuity

**Not Available** in repositories. **To be obtained from Infra.**

## 19. Third-Party Integrations

| System | Purpose | Type | Auth | Data | Status |
|--------|---------|------|------|------|--------|
| MinIO / S3 | Documents/media | Object API | Access key (env) | Files | Available |
| Redis | Cache / rate / blacklist | Cache | Env | Tokens/cache | Available (optional) |
| SMS gateway | Applicant OTP + SMS | HTTP | Env keys | OTP / SMS | Available |
| SMTP | Email | SMTP | Env | Mail | Available |
| Razorpay | Payments | API + webhook | Key/secret (env) | Payment data | Available |
| DSC / Signabyte | Digital signing | Integration | Config | Signatures | Available |
| External IdP / Aadhaar eKYC | — | — | — | — | Not Available |

## 20. Project Size & Effort

| Metric | Value | Status |
|--------|-------|--------|
| Man-days / team commercials | Not Available | To be obtained from PM |
| Git contributors | ~20–21 identities | Partially Available |
| Modules | Large multi-domain portal (admin + applicant + CA site + finance) | Available |
| APIs | ~355 handlers / ~51 controllers | Available |
| Screens | Multiple FE modules (admin, applicant, caseworker, HOD, renewal, dashboard, payments, …) | Partially Available |

## 21. Government / Enterprise Project Evidence

| Field | Value | Status |
|-------|--------|--------|
| Client | BDA (confirm legal name) | Partially Available |
| Project | CAS — CA Site Allotment & Institution Registration Portal | Available |
| Sector | Government | Available |
| Scope | Institution registration → allotment → payment → renewal | Available (code) |
| PO / completion certificates | Not in repos | To be obtained |
| Deployment model | Dockerized API + SPA under `/casite/` | Partially Available |

## 22. Quality & Certifications

Organisation / project certificates: **Not Available** in repos. **To be obtained from Compliance [Org].**

## 23. Policies Relevant to the Project

ISMS policy set: **Not Available** in repos. **To be obtained [Org].**  
Public policy UI pages exist (privacy/terms/refund/copyright) — Partially Available (UI only).

---

# D. EVIDENCE REGISTER (mandatory)

| # | Assessment Area | Requirement | Evidence Available | Evidence Type | Location / Link | Date | Owner | Status |
|---|-----------------|-------------|-------------------|---------------|-----------------|------|-------|--------|
| 1 | Project ID | Project & client | Yes | Code / UI | FE title; BE README | 08-10-2026 | Project | Available |
| 2 | Repositories | Source control | Yes | Git remote | Inventechinfosolutions/cas-* | 08-10-2026 | Project | Available |
| 3 | Stack | NestJS / React / MySQL | Yes | package.json / Docker | BE & FE roots | 08-10-2026 | Project | Available |
| 4 | Auth | JWT + captcha + OTP | Yes | Source | BE auth / applicant / sms | 08-10-2026 | Project | Available |
| 5 | RBAC | Permissions | Yes | Source | BE guards + role enums | 08-10-2026 | Project | Available |
| 6 | Payments | Razorpay | Yes | Source | BE/`src/razorpay/` | 08-10-2026 | Project | Available |
| 7 | Audit | Audit logs | Yes | Source + SQL | BE/`src/audit/`; docs/sql | 08-10-2026 | Project | Available |
| 8 | Docker | Backend container | Yes | Dockerfile | BE/`Dockerfile` | 08-10-2026 | Project | Available |
| 9 | Metrics | Prometheus | Yes | Endpoint | `/api/v1/metrics` | 08-10-2026 | Project | Available |
| 10 | FE bypassAuth default | Auth bypass risk | Yes | Config | FE/`src/lib/config.ts` | 08-10-2026 | Project | Gap |
| 11 | Env secrets in git | Tracked BE `.env*` | Yes | git ls-files | BE root | 08-10-2026 | Security | Gap |
| 12 | CI/CD | Pipeline | No | — | — | — | DevOps | Not Available |
| 13 | VAPT | Report | No | Report | — | — | Security | To be obtained |
| 14 | WAF/DDoS | Protection | No | Config | — | — | Infra | To be obtained |
| 15 | Backup/DR | Evidence | No | Report | — | — | Infra | To be obtained |
| 16 | SOW | Formal SOW | No | Document | — | — | PM | Not Available |
| 17 | Policies / Certs | ISMS / ISO | No | Policy/Cert | — | — | Compliance | To be obtained |
| 18 | PR history | Pull requests | Yes | Git | BE~172 / FE~292 merges | 08-10-2026 | Project | Available |

---

# E. DOCUMENT REGISTER

| Document | Location | Status |
|----------|----------|--------|
| Backend README | BE/`README.md` | Available |
| Frontend structure | FE/`PROJECT_STRUCTURE.md`; FE/`docs/*` | Available |
| SQL helpers | BE/`docs/sql/*` | Available |
| Migrations | BE/`src/migrations/*` | Available |
| SOW / SRS / Architecture pack | — | Not Available |
| VAPT / DR / PO / certificates / org policies | — | Not Available / To be obtained |
| This assessment | FE/`docs/HDFC-Vendor-Assessment-CAS.md` | Available (draft) |

---

# F. GAPS

| # | Gap | Severity | Action owner |
|---|-----|----------|--------------|
| G1 | No formal SOW/SRS in repositories | Medium | PM / Client |
| G2 | BE `.env*` files tracked in git | High | Security / DevOps |
| G3 | FE `bypassAuth` defaults to enabled | High | Project |
| G4 | No automatic account lockout; weak password DTO rules | Medium | Project |
| G5 | Password transport is XOR obfuscation | Medium | Project / Security |
| G6 | No CI/CD; FE not containerised | Medium | DevOps |
| G7 | No VAPT / WAF / DR / backup evidence | High | Security / Infra |
| G8 | Minimal automated tests | Medium | Project |
| G9 | No architecture / ER / data dictionary docs | Medium | Architect |
| G10 | Org policies & certifications not attached | High | Compliance |
| G11 | Production hosting / TLS inventory Not Verified | Medium | Infra |

### Availability summary

| Bundle | Overall |
|--------|---------|
| A. Project Information | Available (owners/commercials partial) |
| B. Technology & Architecture | Available (diagrams/hosting partial) |
| C. Security Assessment | Partially Available (strong OTP/RBAC/payments; secrets-in-git & bypassAuth gaps) |
| D–F | Available (draft) |

---

## 25. Repository Review — Mandatory Checks

| Check | BE | FE |
|-------|----|----|
| README / package.json | Available | Available |
| Dockerfile / compose | Available | Not Available |
| K8s / Helm / CI | Not Available | Not Available |
| Env configuration | Present — **tracked in git (gap)** | `.env` gitignored |
| Auth / AuthZ / Audit / Logging | Available | Client Available |
| Object store / payments / SMS | Available | Client Available |
| Backup / monitoring dashboards | Not Available | Not Available |

### 25.2 Secrets hygiene (location only)

| Finding | Action |
|---------|--------|
| BE tracks `.env`, `.env.dev`, `.env.local`, `.env.prod` despite ignore patterns | Rotate credentials; remove from history; enforce ignore |
| Do not paste JWT/DB/SMS/Razorpay/SMTP/MinIO values into this assessment | Report to Security/DevOps separately |

---

## 26. Final Submission Pack Checklist

| Pack | Status |
|------|--------|
| A. Project Information | Complete (draft) — fill named owners |
| B. Technology & Architecture | Complete (draft) |
| C. Security Assessment | Complete (draft) with gaps |
| D. Evidence Register | Complete (draft) |
| E. Document Register | Complete (draft) |
| F. Gaps | Complete |

---

**End of document — CAS Project & Repository Data Submission v1.0 (draft)**  
Prepared for consolidation into the organisation-level HDFC Vendor Onboarding and Security Assessment checklist.
