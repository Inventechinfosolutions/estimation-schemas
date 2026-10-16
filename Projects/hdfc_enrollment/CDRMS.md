# Correct Dimension Report Management System (CDRMS)— Project & Repository Data Submission

**Client context:** BDA / Government of Karnataka

| Item | Detail |
|------|--------|
| Prepared from | Repository review of backend, web and mobile repositories (local clones), project documents under `required project details/` |
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

- **BE** = `iis-cdrms-backend`  
- **WEB** = `iis-cdrms-web`  
- **MOB** = `iis-cdrms-mobile`  

No passwords, keys, tokens or other secrets are reproduced in this document. Where secrets may exist locally, they are reported by **location only** (Section 25.2).

---

# A. PROJECT INFORMATION

## 1. Project Identification

| Field | Value | Status | Source / Evidence |
|-------|--------|--------|-------------------|
| Project name | Correct Dimension Report Management System (**CDRMS**) | Available | WEB/`required project details/SoW_CDRMS_Detailed.md`; WEB/`src/lib/gov-terminology.ts` (`SYSTEM_FULL`) |
| Client / Department | **BDA** / Government of Karnataka (as stated in SOW + terminology) | Partially Available — confirm legal entity name with PM | SOW §1 header; WEB/`src/lib/gov-terminology.ts` (`ORG_SHORT`, `ORG_STATE`) |
| Industry / Domain | Government — e-Governance / Urban development / Field site inspection & CDR | Available | SOW §2 |
| Project type | **Government** | Available | SOW |
| Project start date | First commits: MOB 25-07-2026; WEB 29-07-2026; BE 29-07-2026 | Available (repository) — contract date **Not Available** | `git log --reverse` on each repo |
| Project end date / current status | Active development; last merges 07–08-10-2026. SOW status: **Draft** | Available | `git log`; SOW header |
| Project duration (so far) | ~10–11 weeks of repository activity (Jul–Oct 2026) | Available | `git log` |
| Current production status | **Not Verified.** Config comments reference `https://bdakarnataka.in/cdrms`. UAT APK artefact present in mobile repo. No production deployment pipeline/logs in repositories | Not Verified — To be obtained from DevOps | WEB/`src/lib/config.ts`; MOB/`.env.example`; MOB/`CDRMS-UAT-*.apk*` (artefact name only) |
| Environments | Local development documented (BE README). UAT artefacts for mobile. Production URL hint only. No `prod` / `release/uat` branches found (unlike Examination Portal pattern) | Partially Available | BE/`README.md`; git branches |
| Repository names | `iis-cdrms-backend`; `iis-cdrms-web`; `iis-cdrms-mobile` | Available | `git remote -v` |
| Repository URLs | `https://github.com/Inventechinfosolutions/iis-cdrms-backend.git`; `https://github.com/Inventechinfosolutions/iis-cdrms-web.git`; `https://github.com/Inventechinfosolutions/iis-cdrms-mobile.git` | Available | `git remote -v` |
| Repository type | GitHub (organisation: **Inventechinfosolutions**) | Available | remotes |
| Repository visibility | Not Verified (GitHub settings not checked during review) | Not Verified | — |
| Repository owner / Technical owner | [To be filled] | To be obtained from PM | — |
| Project manager | [To be filled] | To be obtained from PM | — |
| Solution architect | [To be filled] | To be obtained from PM | — |
| DevOps / Infrastructure owner | [To be filled] | To be obtained from DevOps | — |
| Security owner | [To be filled] | To be obtained from Security team | — |
| Contributors (git authors) | ~8–10 identities across repos (Darshini G B, Monisha-s-2003, shiva Reddy, Srinath R, Narendra, abhiyanthinventech28, IIS-AshokTejaReddy, others) | Available | `git shortlog -sn --all` |

---

## 2. Project Scope (as implemented)

**Business objective** — Digitize the Correct Dimension Report (CDR) process used by BDA engineers to capture site dimensions and related site information during field visits, with CAO verification and downloadable PDF packs for official use.  
Source: WEB/`required project details/SoW_CDRMS_Detailed.md` §1–3.

| Item | Implemented scope | Status | Evidence |
|------|-------------------|--------|----------|
| Major modules | 01 User Access Management; 02 Master Data & System Configuration; 03 Mobile Onboarding & Geo Enforcement; 04 Field Site Visit Capture; 05 CAO Verification & PDF Export; 06 Dashboards / KPIs / MIS; 07 Notification Service (OTP — **specified**, server implementation **gap**) | Available (spec) / Partially Available (OTP) | WEB/`required project details/CDRMS_Modules.md`; `modules/01`–`07` |
| Major functionalities | Engineer/person/post/role management; geo masters; geo-bound field capture (site details, Check Bandi, directions/width, surroundings, photos/video); CAO verify/return/reject; PDF; auction allocation; dashboards; in-app notifications; object-store media; audit logs; location check-ins | Available | BE controllers + WEB/MOB feature folders; SOW §6–7 |
| User types | `super_admin`, `cao`, `zonal_commissioner`, `engineer`, `aee`, `ee` | Available | BE/`src/admin/users/enums/user-types.enum.ts`; BE/`src/admin/auth/utils/role-permissions.ts` |
| Approximate number of users | Not Available | Not Available | — |
| External systems integrated | **MinIO/S3** (object storage) — live in code. **Redis** optional. **SMS OTP gateway** required by SOW but **not implemented** server-side. Email gateway not found. Payment not found. Maps via device GPS / Leaflet / RN Maps (client) | Partially Available | BE/`src/object-store/`; SOW §10; MOB OTP UI without server verify |
| APIs exposed | REST under `/api/*`; **11 controllers**, **~114** HTTP handler decorators (`@Get/@Post/@Put/@Patch/@Delete`). Routes include auth, users, masters, applications, dashboard, object-store, notifications, location, audit-logs, public, health | Available | BE/`src/**/*.controller.ts` |
| APIs consumed | MinIO/S3-compatible API; optional Redis; no live SMS/email/payment adapters found | Partially Available | BE object-store + cache config |
| Major workflows | Super Admin provisions person/post/mapping → engineer login (password JWT; SOW requires OTP every login) → location enablement → geo-enforced site capture → submit to CAO → verify/return/reject → PDF; auction path for CAO | Available | SOW §7; BE/`src/applications/`; WEB features; MOB screens |
| Reports / dashboards | Admin/CAO/ZC/engineer dashboards & KPI views; reports page on web | Available | WEB/`src/admin/pages/dashboard-page.tsx`, `reports-page.tsx`; BE/`src/admin/dashboard/` |
| Mobile application | Yes — Expo / React Native app (field + officer flows) | Available | MOB/ |
| Web application | Yes — React SPA (Super Admin, CAO, ZC, AEE, engineer/officer portals) | Available | WEB/ |
| Backend services | Single NestJS API application | Available | BE/`package.json`, BE/`src/main.ts` |
| Batch / scheduled jobs | None found (`@Cron` / `@Interval` / node-cron not present in app source) | Available (verified absent) | source search |
| Notification services | In-app notifications (DB). Expo push partially configured. **SMS OTP not delivered by backend** (SOW Module 07 gap). Mobile OTP screen does not call a validation API | Available (as gap) | BE/`src/notifications/`; MOB/`AuthScreens.tsx`; SOW Module 07 |
| File / document processing | Photo/video upload to object store; PDF generation (web jspdf; mobile expo-print); profile photos | Available | BE/`src/object-store/`; WEB jspdf; MOB camera/media |
| AI/ML components | None | Not Applicable | dependency review of three `package.json` files |
| Requirements / SRS | No standalone SRS found | Not Available | — |
| SOW | `SoW_CDRMS_Detailed.md` (v1.0, **Draft**, prepared by BDA) | Partially Available (draft) | WEB/`required project details/SoW_CDRMS_Detailed.md` |
| Architecture document | Not Available (no diagram pack in repositories) | Not Available | — |
| Functional / technical specification | Feature MDs F01–F07 under `required project details/modules/`; BE/`README.md`; BE/`src/admin/README.md` | Partially Available | as listed |

---

# B. TECHNOLOGY & ARCHITECTURE

## 3. Technology Stack (verified against build files)

### Frontend — Web [Project]

Source: WEB/`package.json`, WEB/`vite.config.ts`, WEB/`wrangler.json`

| Item | Value |
|------|--------|
| Framework | React ^19.2.7 |
| Language | TypeScript ~6.0.2 |
| Build tool | Vite ^8.1.1 |
| Package manager | npm (lockfile may be absent on some workstations — regenerate via `npm install`) |
| Routing | react-router-dom ^7.18.1 |
| Server state | TanStack Query ^5.101.4 |
| HTTP | axios ^1.18.1 |
| Forms / validation | zod ^4.4.3 |
| UI | Tailwind CSS ^4.3.3, Base UI / shadcn, lucide-react, framer-motion, recharts, sonner, Leaflet / react-leaflet |
| Documents | jspdf ^4.2.1, html-to-image |
| Deploy config | Cloudflare Workers/Pages assets (`wrangler.json` → `./dist`) |
| Code quality | oxlint |
| Automated tests | None found (`*.test.*` / `*.spec.*` absent in app source) |

### Frontend — Mobile [Project]

Source: MOB/`package.json`, MOB/`package-lock.json`, MOB/`app.json`, MOB/`eas.json`

| Item | Value |
|------|--------|
| Framework | Expo ~54.0.0 (resolved **54.0.36**), React Native **0.81.5**, React **19.1.0** |
| Language | TypeScript ~5.9.2 |
| Secure storage | expo-secure-store ~15.0.8 |
| Location / camera / media | expo-location, expo-camera, expo-image-picker, expo-av, expo-video, react-native-maps |
| Notifications | expo-notifications |
| UI | Gluestack, Uniwind/Tailwind, Moti |
| Builds | EAS (`eas.json`: preview APK, production AAB) |
| Native projects | `android/`, `ios/` present |
| Automated tests | None found in app source |

### Backend [Project]

Source: BE/`package.json`, BE/`package-lock.json`, BE/`README.md`

| Item | Value |
|------|--------|
| Framework | NestJS (@nestjs/common **11.1.28**) |
| Language / runtime | TypeScript ~5.8.3; Node.js 20+ (README prerequisite) |
| Architecture | Modular NestJS application (admin, applications, audit, location, notifications, object-store) |
| ORM | TypeORM **0.3.31** |
| DB driver | mysql2 **3.23.2** |
| Auth | @nestjs/jwt **11.0.2**, bcrypt **6.0.0** |
| Security libs | helmet **8.3.0**, @nestjs/throttler **6.5.0**, class-validator, sanitize-html, cookie-parser |
| Object storage | @aws-sdk/client-s3 **3.1097.0** (MinIO-compatible) |
| Cache | cache-manager + @keyv/redis (optional Redis) |
| Automated tests | Jest configured; **1** unit spec (`src/app.controller.spec.ts`) + e2e scaffold (`test/app.e2e-spec.ts`) — Partially Available |

### Database [Project]

| Item | Value | Evidence |
|------|--------|----------|
| Technology / type | MySQL (relational) | BE/`package.json` (`mysql2`); BE/`README.md` |
| Version | Exact server version **Not Verified** in repo (driver mysql2 3.23.2) | To be obtained from Infra |
| Number of databases | 1 application database (single TypeORM connection) | BE TypeORM config / README |
| Schema management | TypeORM entities + manual SQL under `docs/sql/` and `scripts/` (not Flyway/Liquibase) | BE/`docs/sql/*`, BE/`scripts/*.sql` |
| Tables / entities | **~25** entity files (excl. base models), including users, personal_details, post_details, mappings, roles/permissions, masters, applications, auctions, audit_logs, notifications, user_locations, document meta | BE/`src/**/*.entity.ts` |
| Test DB | Not separately profiled beyond Jest scaffold | Partially Available |

### Other technologies — verification result

| Technology | Used? | Evidence / note |
|------------|-------|-----------------|
| Redis | Optional — cache / JWT token blacklist when `REDIS_HOST` set; else in-memory | BE/`README.md`; auth blacklist keys |
| MinIO / object storage | Yes — documents/media | BE/`src/object-store/services/s3-client.service.ts`; env `MINIO_*` |
| Docker | **No** Dockerfile / docker-compose at repo roots | Not Available |
| Elasticsearch / Typesense / Qdrant | No | not in dependencies |
| Kafka / RabbitMQ | No | not in dependencies |
| API gateway | Not found in repositories | Not Verified — Infra |
| Nginx / reverse proxy | Not found in repositories | Not Verified — Infra |
| Kubernetes / Helm / Istio / Argo | No manifests found | Not Available |
| Jenkins / GitHub Actions / other CI | No `.github/workflows`, Jenkinsfile, etc. | Not Available |
| Cloudflare | Partial — WEB static deploy (`wrangler.json`); tunnel URL comments for mobile API | Partially Available |
| Monitoring | `ENABLE_METRICS` env name only; health is liveness string; no Prometheus/Grafana config | Partially Available / gap |
| Logging | Nest `Logger` + exception filter; no ELK/Winston shipping config | Available (app) / Not Available (central) |
| SIEM / WAF / DDoS | Not found in repositories | To be obtained from Infra/Security |
| Cloud services | Hosting model not defined in repos; SOW says per BDA instructions | Not Verified — Infra / Client |
| Third-party services | Maps/GPS client-side; SMS/email gateways not live | as Section 19 |

---

## 4. Architecture

| Item | Status | Detail / Evidence |
|------|--------|-------------------|
| Application architecture diagram | Not Available | No diagram in repositories. Logical architecture derived from code below |
| Deployment / network / cloud / on-prem architecture | Not Available | To be obtained from DevOps/Infra |
| Integration architecture | Partially Available | Object store (S3 API); optional Redis; SMS/email ports not implemented |
| Data architecture | Partially Available | TypeORM entities + SQL scripts; no ER diagram document |
| Authentication architecture | Available (code) | Login credentials → bcrypt verify → JWT access + refresh; httpOnly cookies (web); SecureStore (mobile); Redis/in-memory token blacklist on logout; session idle via `SESSION_TIMEOUT_MINUTES` |
| Security architecture | Partially Available (code only) | Section 10 |
| Cloud / on-premise architecture | Not Available | SOW §17: hosting follows BDA instructions |

**Logical architecture derived from repository [Project]:**

```
Mobile (Expo RN)          Web (React + Vite SPA)
        \                       /
         \                     /
          ▼                   ▼
     HTTPS (prod TLS — Not Verified in repo)
                   ▼
     [Reverse proxy / LB / WAF — Not Verified]
                   ▼
     NestJS API (default APP_HOST 127.0.0.1; port per env, README cites 3710)
       ├── MySQL (application data)
       ├── Redis (optional cache / token blacklist)
       ├── MinIO / S3 (photos, video, documents)
       └── In-app notifications (DB)
```

| Component | Identified | Evidence |
|-----------|------------|----------|
| Application server | NestJS on Node.js | BE/`src/main.ts` |
| Web server for SPA | Not Verified (Vite `dist/`; Cloudflare Workers assets config present) | WEB/`wrangler.json` |
| API gateway / load balancer | Not Verified | — |
| Database / cache / object storage | MySQL / optional Redis / MinIO-S3 | as above |
| Message broker | None | — |
| Identity provider | In-application JWT (no external IdP/SSO found) | BE/`src/admin/auth/` |
| Monitoring / security components | Health endpoint only; WAF/IDS not verified | BE/`src/app.controller.ts` |
| Architecture document location | Not Available | — |

---

# C. SECURITY ASSESSMENT & CONTROLS

## 5. Repository & Development Practices [Project]

| Item | Finding | Status | Evidence |
|------|---------|--------|----------|
| Repository structure | BE: Nest `src/{admin,applications,audit,location,notifications,object-store}`; WEB: `src/{admin,features,components,lib}`; MOB: `src/{auth,cdrms,features}` | Available | tree |
| Branching strategy | Feature branches (`feature/*`, `fetaure/*` typo branches) merged via PR into `main` (WEB/MOB) or `dev` (BE default) | Partially Available (not documented) | `git branch -a` |
| Development / UAT / Production branches | BE: `dev`, `main`; WEB/MOB: `main` + feature branches. **No** dedicated `prod` / `release/uat` branches observed | Partially Available | `git branch -r` |
| Pull request process | Used: BE ~18 PR merges; WEB ~24; MOB ~18 | Available | `git log --merges` (“Merge pull request #…”) |
| Code review / approvals | Not Verified — check GitHub PR review records | Not Verified | GitHub PR pages |
| Branch protection | Not Verified — GitHub settings not accessible during review | Not Verified | GitHub → Settings → Branches |
| Commit standards | Not enforced (no commitlint/husky observed); mixed message quality | Available (gap) | `git log` |
| Code ownership | No `CODEOWNERS` file found | Not Available | — |
| Release / versioning / tagging | **0** git tags across all three repos; MOB uses EAS profiles | Not Available / Partially Available | `git tag`; MOB/`eas.json` |
| Release / deployment history | Not Available in repository | Not Available | — |
| Coding standards | BE ESLint/Prettier; WEB oxlint; MOB Expo/AGENTS.md notes | Partially Available | configs |
| Repository access controls | Not Verified (GitHub org membership/teams) | To be obtained from GitHub org admin | — |

## 6. SDLC & Development Process

| Area | Finding | Status | Evidence |
|------|---------|--------|----------|
| Requirement management | SOW + module/feature MDs in WEB repo | Available | WEB/`required project details/` |
| Development process | Feature-branch + PR merge observed | Partially Available | git history |
| Code review | PRs exist; approval evidence Not Verified on GitHub | Partially Available | — |
| Unit testing | Backend Jest scaffold only; web/mobile tests absent | Partially Available | BE test files |
| Integration / system / UAT / security / performance testing | Process docs and reports not in repos | Not Available | — |
| Release / change / production / rollback / defect management | Not documented in repos | Not Available | To be obtained |
| SDLC / coding / release / change policies | Not in project repos | To be obtained from Org/Compliance | — |

## 7. Authentication & User Access Management

| Control | Actual implementation | Status | Evidence |
|---------|----------------------|--------|----------|
| Authentication mechanism | Login ID / email + password → JWT access + refresh tokens | Available | BE/`src/admin/auth/auth.service.ts`, `auth.controller.ts` |
| Authorization mechanism | Permission-code checks via `PermissionsGuard` / `@Permissions(...)` | Available | BE auth guards; controllers |
| RBAC implementation | Roles mapped to permission arrays; catalog seeded | Available | BE/`src/admin/auth/utils/role-permissions.ts` |
| Roles available | super_admin, cao, zonal_commissioner, engineer, aee, ee | Available | enums + ROLE_PERMISSIONS |
| Permissions | APPLICATION:\*, DASHBOARD:VIEW, TASK:VIEW, AUCTION:\*, CDR:VIEW, SETTINGS:VIEW, MASTER:\*, NOTIFICATION:\*, OBJECT_STORE:\*, USER:\* | Available | `ALL_PERMISSIONS` / `PERMISSION_CATALOG` |
| Role–permission mapping | Hard-coded maps + DB role_permission entities | Available | role-permissions.ts; role entities |
| Admin / privileged roles | `super_admin` (full permission set via helper) | Available | role-permissions.ts |
| MFA | Not implemented | Not Available | — |
| SMS OTP every login | **Required by SOW**; **no backend OTP send/validate API**; mobile OTP UI accepts filled code without server verification | Available (as gap) | SOW Module 07; MOB/`AuthScreens.tsx` |
| Password policy / complexity | DTO `@MinLength(6)` only — no complexity/expiry/history rules found | Partially Available | BE/`login.dto.ts`, `register.dto.ts` |
| Password hashing | bcrypt cost factor **10** | Available | auth/users services |
| Failed login / account lockout | Not found | Not Available | — |
| Session timeout | `SESSION_TIMEOUT_MINUTES` (README default **30**) | Available | BE/`auth.service.ts`; BE/`README.md` |
| Password reset | Super Admin can set person password (API); self-service reset flow Not Verified | Partially Available | BE users controller password patch |
| User provisioning / de-provisioning / activation | Person + post + mapping; user status ACTIVE gate on login | Available | BE/`users.service.ts`; auth login |
| Third-party user access / PAM / periodic access review | Not in repos | To be obtained | — |
| Web token storage | `sessionStorage` for tokens + httpOnly cookies from API | Available | WEB auth API / `src/lib/api.ts` |
| Mobile token storage | expo-secure-store | Available | MOB/`src/auth/AuthContext.tsx` |

**Do not expose credentials.** Bootstrap/seed password patterns exist in BE seed/service code — report existence to Security/DevOps; values are **not** copied into this assessment (Section 25.2).

## 8. Data Model & Data Dictionary

| Item | Status | Evidence |
|------|--------|----------|
| ER diagram | Not Available | — |
| Formal Data Dictionary | Not Available | — |
| Database schema / entities | Available | BE/`src/**/*.entity.ts` |
| SQL helpers / migrations (manual) | Available | BE/`docs/sql/*`, BE/`scripts/*.sql` |
| Important entities | users; personal_details; post_details; post_person_mapping; role / permission / role_permission; masters (district, taluk, village, zone, geo-location, attributes, system parameters); applications; auctions; audit_logs; notifications; user_locations; document_meta_info; series_generator | Available | entity files |
| PII fields | name, email, mobileNumber, gender, district, profilePhoto, GPS/geo address JSON, engineer location history | Available | personal-details, application, user-location entities |
| Financial data | No payment ledger found; PAN default constant on applications (document classification enums for PAN/Aadhaar docs) | Partially Available | application entity / object-store enums |
| Authentication data | password hash (`select: false`), loginId, JWT (client-side / cookies) | Available | user.entity.ts |
| Audit data | audit_logs (+ interceptor scrubbing sensitive keys such as password/OTP) | Available | BE/`src/audit/` |

## 9. Data Storage & Handling

| Area | Finding | Status |
|------|---------|--------|
| Where stored | MySQL (structured); MinIO/S3 (media/files); optional Redis (cache/tokens); application logs to process stdout | Available (code) |
| On-premise / Cloud / Hybrid | Not defined in repos; SOW: per BDA instructions | To be obtained — Client / Infra |
| Encryption at rest | Not configured in application repositories | To be obtained — Infra |
| Encryption in transit | Prod HTTPS **Not Verified**; cookies set `secure` when `ENVIRONMENT` is production/prod/uat; MOB `app.json` allows cleartext / ATS arbitrary loads (dev risk) | Partially Available |
| Algorithms | bcrypt (passwords); TLS version Not Verified | Partially Available |
| Key / secret management | Environment variables; `.env*` gitignored patterns present | Partially Available |
| Backup / restore / archival / retention / purging | Not in repositories; SOW RPO/RTO “as defined in RFP” | Not Available — To be obtained from Infra |

## 10. Application Security

| Control | Status | Evidence |
|---------|--------|----------|
| Input validation | Available | Global `ValidationPipe` (whitelist) + DTOs |
| HTML sanitization | Available | sanitize-html / SanitizePipe |
| Authentication / Authorization / RBAC | Available | Section 7 |
| Session management | Available | JWT + refresh + blacklist + idle timeout |
| Password security | Partially Available | bcrypt; weak min-length only |
| API security | Partially Available | JWT guards; public routes under `/api/public/*` documented |
| Secure headers (Helmet/CSP/HSTS) | Partially Available | Env-gated: `ENABLE_HELMET`, `ENABLE_CSP`, `ENABLE_HSTS` in BE/`src/main.ts` |
| CORS | Available | Allowlist via `CORS_ORIGIN`, credentials true — `main.ts` |
| CSRF | Not explicitly documented for cookie+SPA model | Not Verified |
| SQL injection prevention | Available (ORM parameterized queries) | TypeORM usage |
| XSS protection | Partially Available | sanitize-html; WEB/`src/lib/xssValidation.ts` |
| File upload security | Partially Available | multer + object-store; media limits in SOW/masters — malware scanning Not Available |
| Rate limiting | Partially Available | Global throttler **off** unless `ENABLE_RATE_LIMITING=true`; auth endpoints use `@Throttle` |
| Brute-force / lockout | Not Available | — |
| Error handling | Available | Nest exception filter |
| Logging / audit trail | Available | Logger + audit interceptor/DB |
| Sensitive data masking in audit | Partially Available | interceptor scrubbing for password/OTP keys |
| Secrets management | Partially Available | env files; no vault integration in repo |
| Security libraries | Available | helmet, throttler, bcrypt, jwt, class-validator, sanitize-html |

## 11. VAPT / Security Audit / Code Review

| Field | Value |
|-------|--------|
| Assessment records in repositories | **None found** |
| Status | **Not Available – To be obtained from Security/Compliance Team** |

Do not invent findings. Attach report location when available.

## 12. WAF / DDoS / Network Security

| Control | Status | Note |
|---------|--------|------|
| WAF | To be obtained from Infra/Security | Not in app repos. Cloudflare static hosting ≠ confirmed API WAF |
| DDoS protection | To be obtained | — |
| Firewall / IDS/IPS / VPN / segmentation | To be obtained | — |
| API gateway / LB / reverse proxy | Not Verified | — |

No timestamped WAF/DDoS evidence in repositories.

## 13. Encryption & Digital Certificates

| Area | Finding | Status |
|------|---------|--------|
| Data in transit (TLS version, cert type, validity) | Not documented in repos | To be obtained — Infra |
| HTTPS for API/web | Expected in production; Not Verified | Not Verified |
| Data at rest (DB/file/backup encryption) | Not documented | To be obtained |
| Password hashing | bcrypt | Available |
| Token mechanism | JWT access + refresh | Available |
| API authentication | Bearer JWT / cookies | Available |
| Digital signatures | Not found as app feature | Not Applicable / Not Available |
| Certificates inventory | Prod TLS inventory Not Available. MOB contains Play upload `.pem` artefacts (signing) — not TLS server certs | Partially Available |
| Private keys / secrets | **Not shared in this document** | — |

## 14. Incident Management

| Item | Status |
|------|--------|
| Project-level IR process, escalation matrix, SLA, RCA templates, ticket evidence | **Not Available** in repositories |
| Organisation IR policy / team | **To be obtained from Security / Operations [Org]** |

Do not include confidential incident content.

## 15. Logging & Monitoring

| Item | Finding | Status |
|------|---------|--------|
| Application logging | Nest Logger | Available |
| Audit logging | `audit_logs` table + interceptor | Available |
| Security / access / API / DB / infra logging platforms | Not configured in repos | Not Available |
| ELK / Grafana / Prometheus / Splunk / SIEM / CloudWatch / Azure Monitor / App Insights | Not found | Not Available |
| Health endpoint | `GET /api/health` liveness | Available |
| Log retention / alerting / dashboards | Not Available | To be obtained |

## 16. CI/CD & Deployment

| Item | Finding | Status |
|------|---------|--------|
| Source repositories | Three GitHub repos (Section 1) | Available |
| CI tool (Actions/Jenkins/Bitbucket/Argo) | Not found | Not Available |
| Build process | `nest build`; `vite build`; Expo/EAS | Partially Available |
| Test automation in pipeline | Not Available | — |
| Security / container scanning | Not Available | — |
| Artifact / image registry | Not Available (MOB EAS cloud builds Partially Available) | Partially Available |
| Docker / Kubernetes / Helm / GHCR | Not Available | — |
| Deployment environments / approval / rollback | Not documented | To be obtained — DevOps |
| Web deploy config | `wrangler.json` | Partially Available |
| Mobile deploy config | `eas.json` + UAT APK artefact name | Partially Available |

## 17. Infrastructure & Hosting

| Item | Status | Evidence |
|------|--------|----------|
| Hosting model | To be obtained (SOW: BDA decides cloud / on-prem / hybrid) | SOW §17 |
| Cloud provider / region / DC | Not Verified | — |
| Kubernetes / VM / storage / network / firewall / LB / backup / DR infra | To be obtained — Infra | — |
| Production URL hint | `bdakarnataka.in/cdrms` (comment only) | WEB/`src/lib/config.ts`; MOB/`.env.example` |

## 18. Disaster Recovery & Business Continuity

| Item | Status |
|------|--------|
| DR architecture, site, RPO, RTO, procedures, test reports | **Not Available** in repositories |
| SOW note | RPO/RTO “as defined in RFP” — **To be obtained** from RFP / Infra / Client | SOW §12 |

## 19. Third-Party Integrations

| System | Purpose | Integration type | API/Protocol | Authentication | Data exchanged | Owner | Status |
|--------|---------|------------------|--------------|----------------|----------------|-------|--------|
| MinIO / S3-compatible | Media & documents | Object storage | S3 API | Access key (env) | Photos, video, files | Project / Infra | Available |
| Redis (optional) | Cache / token blacklist | Cache | Redis protocol | URL / password env | Session/token keys | Project / Infra | Available (optional) |
| Device GPS / Leaflet / RN Maps / OSM | Geo stamp & maps UI | Client SDK / HTTP | HTTPS | Maps key optional | Lat/long, place labels | Project | Partially Available |
| SMS gateway | OTP every login | Required by SOW | — | — | OTP codes | Client / Project | **Not Available (gap)** |
| Email service | Optional notify | — | — | — | — | — | Not Available |
| Payment gateway | — | — | — | — | — | — | Not Applicable / Not Available |
| Aadhaar eKYC | — | Doc type enum only | — | — | — | — | Not Applicable (no eKYC API found) |
| Other BDA APIs | Direct hand-off | Out of SOW baseline | — | — | — | Client | Out of scope |

## 20. Project Size & Effort

| Metric | Value | Status |
|--------|-------|--------|
| Man-days (dev/test/devops/architecture/support) | Not Available | To be obtained from PM |
| Team size / peak / role counts | Not Available (git shows ~8–10 commit identities) | Partially Available (git only) |
| Function Points | Not Available | — |
| Number of modules | **7** functional modules (documented) | Available |
| Number of screens (approx.) | WEB: 20 admin pages + multiple feature portals; MOB: 12 screen modules | Partially Available |
| Number of APIs | ~114 route handlers / 11 controllers | Available |
| Number of integrations (live) | MinIO (+ optional Redis); maps client-side | Available |
| Supporting commercials (PO, estimation, completion certificate) | Not in repos | To be obtained |

## 21. Government / Enterprise Project Evidence

| Field | Value | Status |
|-------|--------|--------|
| Client name | BDA / Government of Karnataka | Available (confirm legal name) |
| Project name | CDRMS | Available |
| Sector | Government | Available |
| Scope | Field CDR capture → CAO verification → PDF; admin masters/users/KPIs | Available — SOW |
| Contract value / duration / team size / man-days | Not Available | To be obtained |
| Technology | NestJS, React, Expo RN, MySQL, MinIO | Available |
| Major modules | 01–07 | Available |
| Major integrations | Object storage; SMS OTP pending | Partially Available |
| Deployment model | TBD by BDA | To be obtained |
| Completion status | In development / UAT artefacts present | Partially Available |
| Evidence (PO, work order, completion/client certificate) | Not in repositories | To be obtained — PM / Sales |

## 22. Quality & Certifications

| Scope | Finding | Status |
|-------|---------|--------|
| Organisation certifications (ISO 9001/27001/20000, CMMI, SOC, PCI, CERT-In, etc.) | Not present in project repositories | To be obtained from Compliance **[Org]** |
| Project / data centre / cloud certs | Not Available | To be obtained |

## 23. Policies Relevant to the Project

| Policy | In project repos? | Status |
|--------|-------------------|--------|
| Information Security / Data Protection / Privacy / Access Control / Password / Encryption / Key Management | No | To be obtained **[Org]** — SOW cites BDA IT policy alignment |
| Secure SDLC / Incident Response / Backup / Retention / Archival / Purging | No | To be obtained |
| Change / Vulnerability / Patch / BCP / DR / WAF / DDoS policies | No | To be obtained |
| In-app Privacy Policy screens | UI copy only (WEB privacy page; MOB `PrivacyPolicyScreen.tsx`) | Partially Available (not a controlled policy document) |

For each org policy, central team should supply: version, owner, approval authority, effective/review dates, applicability, implementation evidence.

---

# D. EVIDENCE REGISTER (mandatory)

| # | Assessment Area | Requirement | Evidence Available | Evidence Type | Location / Link | Date | Owner | Status |
|---|-----------------|-------------|-------------------|---------------|-----------------|------|-------|--------|
| 1 | Project ID | Client & system name | Yes | SOW / Code | WEB/`required project details/SoW_CDRMS_Detailed.md`; WEB/`src/lib/gov-terminology.ts` | 08-10-2026 | Project | Available |
| 2 | Repositories | Source control URLs | Yes | Repository | GitHub Inventechinfosolutions / iis-cdrms-* | 08-10-2026 | Project | Available |
| 3 | Scope | Modules 01–07 | Yes | SOW / Feature MD | WEB/`required project details/` | 08-10-2026 | Project | Available |
| 4 | Technology | NestJS / React / Expo / MySQL | Yes | package.json / lock | BE, WEB, MOB roots | 08-10-2026 | Project | Available |
| 5 | Auth | JWT + bcrypt | Yes | Source | BE/`src/admin/auth/` | 08-10-2026 | Project | Available |
| 6 | RBAC | Roles & permissions | Yes | Source | BE/`src/admin/auth/utils/role-permissions.ts` | 08-10-2026 | Project | Available |
| 7 | Audit | Audit trail | Yes | Source + SQL | BE/`src/audit/`; BE/`docs/sql/create-audit-logs-table.sql` | 08-10-2026 | Project | Available |
| 8 | Object store | MinIO/S3 | Yes | Source | BE/`src/object-store/` | 08-10-2026 | Project | Available |
| 9 | OTP / MFA | SMS OTP every login | No (gap vs SOW) | Spec vs code | SOW Module 07; MOB/`AuthScreens.tsx` | 08-10-2026 | Project | Gap — Available as finding |
| 10 | Password policy | Complexity / expiry / lockout | Partial | Source | BE login/register DTOs (min 6 only) | 08-10-2026 | Project | Partially Available |
| 11 | Security headers | Helmet/CSP/HSTS | Partial | Configuration | BE/`src/main.ts` (env-gated) | 08-10-2026 | Project / Infra | Partially Available |
| 12 | Rate limiting | Global throttle | Partial | Configuration | BE/`app-throttler.guard.ts` | 08-10-2026 | Project / Infra | Partially Available |
| 13 | CI/CD | Pipeline | No | — | — | — | DevOps | Not Available |
| 14 | Docker/K8s | Containers / orchestration | No | — | — | — | DevOps | Not Available |
| 15 | VAPT | Latest report / safe-to-host | No | Report | — | — | Security | To be obtained |
| 16 | WAF / DDoS | Protection evidence | No | Config / Dashboard | — | — | Infra / Security | To be obtained |
| 17 | Backup / DR | Backup logs / DR test | No | Report | — | — | Infra | To be obtained |
| 18 | Monitoring | Central APM/SIEM | No | Dashboard | — | — | Infra | To be obtained |
| 19 | Policies | ISMS policy set | No | Policy | — | — | Compliance | To be obtained |
| 20 | Certifications | ISO / SOC / CERT-In | No | Certificate | — | — | Compliance | To be obtained |
| 21 | Hosting | Prod infra confirmation | Partial | URL comment | `bdakarnataka.in/cdrms` comments | 08-10-2026 | Infra | To be confirmed |
| 22 | PR process | Pull request history | Yes | Git history | `git log --merges` (BE~18, WEB~24, MOB~18) | 08-10-2026 | Project | Available |
| 23 | Web deploy | Cloudflare config | Yes | Configuration | WEB/`wrangler.json` | 08-10-2026 | Project | Partially Available |
| 24 | Mobile build | EAS profiles | Yes | Configuration | MOB/`eas.json` | 08-10-2026 | Project | Partially Available |

---

# E. DOCUMENT REGISTER

| Document | Location | Status |
|----------|----------|--------|
| SOW (Draft v1.0) | WEB/`required project details/SoW_CDRMS_Detailed.md` | Available (draft) |
| Module index | WEB/`required project details/CDRMS_Modules.md` | Available |
| Feature specifications F01–F07 | WEB/`required project details/modules/**` | Available |
| Backend README | BE/`README.md` | Available |
| Admin module README | BE/`src/admin/README.md` | Available |
| SQL / schema helpers | BE/`docs/sql/*`, BE/`scripts/*.sql` | Available |
| Web README | WEB/`README.md` (Vite template — weak) | Partially Available |
| Mobile README / AGENTS / CLAUDE | MOB root | Available |
| Architecture diagrams | — | Not Available |
| ER / Data Dictionary | — | Not Available |
| VAPT / DR / backup / audit reports | — | Not Available |
| PO / Work order / Completion / Client certificates | — | Not Available |
| Organisation policies & certifications | — | To be obtained **[Org]** |
| This assessment | WEB/`required project details/HDFC-Vendor-Assessment-CDRMS.md` | Available (draft) |

---

# F. GAPS

| # | Gap | Category | Severity for HDFC | Action owner |
|---|-----|----------|-------------------|--------------|
| G1 | SMS OTP required by SOW but not implemented server-side; mobile OTP not server-validated | Application Security / Scope | High | Project (Dev) + Security |
| G2 | No MFA; no account lockout; password policy is min-length 6 only | Access Control | High | Project + Compliance (align to BDA IT policy) |
| G3 | Helmet / CSP / HSTS / global rate-limit are env-gated — production flag values unknown | Security config | Medium | DevOps |
| G4 | No CI/CD pipelines, Docker, K8s, or IaC in repositories | SDLC / Deploy | Medium | DevOps |
| G5 | No VAPT / safe-to-host / CERT-In auditor evidence | Security assessment | High | Security / Compliance |
| G6 | No WAF/DDoS/firewall evidence confirming API/web are protected | Network security | High | Infra / Security |
| G7 | No backup logs, restore tests, DR architecture, RPO/RTO evidence | Backup / DR | High | Infra |
| G8 | No central monitoring/SIEM/alerting evidence | Monitoring | Medium | Infra |
| G9 | No formal architecture / ER / data dictionary documents | Documentation | Medium | Architect |
| G10 | No org ISMS policies / certificates attached to project pack | Policies / Certs | High | Compliance **[Org]** |
| G11 | Mobile ATS/cleartext relaxed in `app.json` | Mobile security | Medium | Mobile Dev / Security |
| G12 | Bootstrap/seed credential patterns in code/SQL — hygiene risk | Secrets | High | Security / DevOps (do not publish values) |
| G13 | Production hosting URL and environment matrix not confirmed | Infra | Medium | DevOps / Client |
| G14 | Contractual dates, man-days, PO, completion certificates missing | Project credentials | Medium | PM / Sales |
| G15 | Branch protection / PR approval evidence not verified on GitHub | Dev practices | Medium | Tech lead / GitHub admin |
| G16 | Automated test coverage minimal (backend scaffold only) | Quality | Medium | Project |
| G17 | SOW still Draft / unsigned | Requirements | Medium | PM / Client |

### Availability summary (for consolidators)

| Bundle | Overall |
|--------|---------|
| A. Project Information | **Available** (owners/dates/commercials partial) |
| B. Technology & Architecture | **Available** (diagrams / prod hosting partial) |
| C. Security Assessment | **Partially Available** (strong JWT/RBAC/audit; OTP/MFA/lockout/VAPT/WAF gaps) |
| D. Evidence Register | **Available** (this document) |
| E. Document Register | **Partially Available** |
| F. Gaps | **Available** (listed honestly) |

---

## 25. Repository Review — Mandatory Checks

| Check | BE | WEB | MOB |
|-------|----|-----|-----|
| README | Available | Partially Available (Vite template) | Available |
| package.json / lock | Available | package.json Available; lock may be missing | Available |
| Dockerfile / docker-compose | Not Available | Not Available | Not Available |
| Kubernetes / Helm | Not Available | Not Available | Not Available |
| CI/CD pipelines | Not Available | Not Available | Not Available |
| Environment configuration | `.env` / `.env.local` (local); no committed `.env.example` on BE | `.env.example` Available | `.env.example` Available |
| Infrastructure-as-Code | Not Available | Not Available | Not Available |
| API documentation (OpenAPI/Swagger) | Not found as published UI | — | — |
| Database scripts | Available (`docs/sql`, `scripts`) | — | — |
| Authentication / Authorization | Available | Client usage Available | Client usage Available |
| Logging / Audit trail | Available | Consumes API | Consumes API |
| Security configuration | Partially Available (env-gated) | CORS client; xss helper | SecureStore; ATS flags |
| Encryption / certificates | App hashing Available; TLS Not Verified | — | upload `.pem` present |
| Third-party integrations | MinIO/Redis | Maps | Maps / notifications |
| Monitoring configuration | Health only | — | — |
| Backup scripts | Not Available | Not Available | Not Available |
| Deployment documentation | Partially Available (README / wrangler / eas) | Partially Available | Partially Available |

### 25.2 Secrets hygiene (report existence only — do not copy values)

| Finding | Action |
|---------|--------|
| Local `.env` / `.env.local` files may exist on developer machines (gitignored patterns present) | Confirm they are never committed; rotate if ever exposed |
| Seed / bootstrap password patterns exist in BE seed SQL / user bootstrap code | Security/DevOps to review, remove defaults from non-dev environments |
| If any secret is found committed historically | Report to Security/DevOps separately; **do not paste into this assessment** |

---

## 26. Final Submission Pack Checklist

| Pack | Contents | Status |
|------|----------|--------|
| **A. Project Information** | Sections 1–2 | Complete (draft) — fill named owners |
| **B. Technology & Architecture** | Sections 3–4 | Complete (draft) — attach diagrams when available |
| **C. Security Assessment** | Sections 5–15 (+ 7–10 focus) | Complete (draft) with gaps flagged |
| **D. Evidence Register** | Section 24 table | Complete (draft) |
| **E. Document Register** | Section E | Complete (draft) |
| **F. Gaps** | Section F | Complete |

---

**End of document — CDRMS HDFC Vendor Assessment Data Submission v1.0 (draft)**  
Prepared for consolidation into the organisation-level HDFC Vendor Onboarding and Security Assessment checklist.
