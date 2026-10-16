# RTI — Project & Repository Data Submission

**Project: Bangalore Development Authority — Right to Information (RTI) Management Portal (BDA RTI Portal)**

| Item | Detail |
| :--- | :--- |
| **Prepared from** | Repository review of the frontend (`rti-frontend`) and backend (`rti-backend`) repositories (local clones, branch `feature/applicant_name` / `main`), statutory RTI disclosures, and backend technical documents in `docs/` |
| **Review date** | 08-10-2026 |
| **Prepared by** | Shashank HL [Repository Contributor / Technical Lead] |
| **Reviewed by** | [Technical Owner / Solution Architect / PM] |
| **Version** | 1.0 (draft) |

---

### How to read this document

- **Status values used:** `Available`, `Partially Available`, `Not Available`, `Not Applicable`, `Not Verified`, `To be obtained from another team`.
- **Information level:** `[Project]` = verified directly in this project's repositories; `[Org]` = organisation-level, to be supplied by central/security team; `[Client]` = client-specific; `[Infra]` = infrastructure/hosting team.
- **Evidence paths:** Relative to repository root. `FE` = `rti-frontend`, `BE` = `rti-backend`.
- **Confidentiality:** No passwords, keys, tokens, or other production secrets are reproduced in this document. Where credentials/defaults were identified in tracked code/configuration, they are reported by file location only (Section 25.2).

---

## A. PROJECT INFORMATION

### 1. Project Identification

| Field | Value | Status | Source / Evidence |
| :--- | :--- | :--- | :--- |
| **Project name** | Bangalore Development Authority — Right to Information (RTI) Management Portal (BDA RTI Portal) | `Available` | `FE/src/locales/en.json` (`bdaCounter`, `registrationPlaceholder: BDA-RTI-*`); `BE/src/sms/`; `BE/docs/API_FRONTEND.md` |
| **Client / Department** | Bangalore Development Authority (BDA), Government of Karnataka | `Available` | `FE/src/pages/HomePage.tsx`; `FE/src/assets/bda-logo.jpg`; official Section 4(1)(a) & 4(1)(b) gazette orders in `FE/src/assets/sec-4-1a/` |
| **Industry / Domain** | Government — e-Governance / Citizen Grievance & Public Information (RTI Act, 2005) | `Available` | `FE/src/pages/PolicyPage.tsx`; `BE/src/rti-applications/` |
| **Project type** | **Government** | `Available` | BDA statutory implementation |
| **Project start date** | 16-04-2026 (FE initial commit `fad8295`); 28-04-2026 (BE initial commit `3314ecd`) | `Available` (repo) — Contract date `Not Available` | `git log --reverse` on FE and BE |
| **Project end date / current status** | In active development & UAT; latest commit 08-10-2026 | `Available` | `git log -1` on FE and BE |
| **Project duration (so far)** | ~5.5 months of active repository history (Apr 2026 – Oct 2026) | `Available` | `git log` |
| **Current production status** | **Not Verified**. `prod` branch exists on GitHub, staging/UAT server referenced at `http://14.97.141.54:7800`, but production deployment pipelines/tags are not present in repositories. | `Not Verified` — To be obtained from DevOps | `git branch -r` (`origin/prod`); `BE/.env.example` (`FRONTEND_URL`) |
| **Environments** | Profiles: `local`, `dev`, `test`, `prod` (NestJS config). Dev server referenced at `14.97.141.54:7800`. | `Partially Available` | `BE/src/app.module.ts`; `BE/.env.example`; `FE/.env.local` |
| **Repository names** | `rti-frontend` ; `rti-backend` | `Available` | `git remote -v` |
| **Repository URLs** | `git@github.com:Inventechinfosolutions/rti-frontend.git`<br>`git@github.com:Inventechinfosolutions/rti-backend.git` | `Available` | `git remote -v` |
| **Repository type** | GitHub (organisation: `Inventechinfosolutions`) | `Available` | `git remote -v` |
| **Repository visibility** | Private (GitHub organization access required) | `Available` | GitHub repository access |
| **Repository owner / Technical owner** | [To be filled from PM / Technical Lead] | `To be obtained from PM` | — |
| **Project manager** | [To be filled from PM] | `To be obtained from PM` | — |
| **Solution architect** | [To be filled from PM] | `To be obtained from PM` | — |
| **DevOps / Infrastructure owner** | [To be filled from DevOps] | `To be obtained from DevOps` | — |
| **Security owner** | [To be filled from Security Team] | `To be obtained from Security` | — |
| **Contributors (git authors)** | 7 active developers committing under 10 git identities: Shashank HL, Manveeth, Srinath R, Shiva-Inventech, Charangowda B R, Abhiyanth, and a dev server identity. | `Available` | `git shortlog -sn --all` on FE and BE |

---

### 2. Project Scope (as implemented)

**Business objective:** Provide a transparent, automated, and legally compliant online workflow management system for Right to Information (RTI) applications under the RTI Act, 2005 for the Bangalore Development Authority (BDA). Enables citizens to file RTI applications, submit statutory fees online or provide BPL proof, track application status, and file First Appeals. Enables BDA Public Information Officers (PIOs) and First Appellate Authorities (FAAs) to examine records, demand copy fees, issue summons, schedule hearings, and furnish certified responses.

| Item | Implemented Scope | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Major modules** | 1. Citizen Portal (Registration, OTP auth, profile, RTI filing, fee payment, BPL upload, tracking, appeal filing)<br>2. PIO Desk (Desk-based login, application review, fee request, file attachment, response closure)<br>3. Helpdesk Counter (Physical filing, Indian Postal Order [IPO] registration, manual fee receipt, PIO assignment)<br>4. PRO Assigner Portal (Public Relations Officer assignment, department allocation)<br>5. First Appellate Authority [FAA] Portal (First appeals, summons issuance, hearing scheduling, calendar)<br>6. User & Post Management (Desk post creation, post-person mapping, role-menu mapping)<br>7. Holiday Master (State holiday master for statutory SLA & deadline computation)<br>8. SMS Gateway & Audit (Automated SMS dispatch on filing, payment, hearing, closure)<br>9. Documents / Object Storage (MinIO S3 integration for ID proof, BPL certs, receipts, response docs)<br>10. Payment Gateway (PayU integration for application and additional copy fees)<br>11. Localization (English and Kannada - EN/KN support) | `Available` | `FE/src/pages/` (24 page files); `BE/src/` (20 NestJS feature modules) |
| **User types** | Super Admin, Public Information Officer (PIO), First Appellate Authority (FAA), Helpdesk, PRO Assigner, Assigner, Finance Member, Citizen / Public. | `Available` | `BE/src/common/enums/index.ts` (`StaffUserRole`); `BE/src/auth/jwt-payload.interface.ts` |
| **Approximate number of users** | Not Available in repo. Designed for all BDA zonal public applicants across Bengaluru Urban, plus ~100+ BDA departmental PIO/FAA officers. | `Partially Available` | Section 4(1)(a) gazette list of ~50+ PIO posts; load test not committed |
| **External systems integrated** | 1. **PayU Payment Gateway:** Active integration for application fee (₹10) and additional document copy fees.<br>2. **BDAGOV SMS Gateway:** Karnataka Mobile Seva SMS gateway integration for OTPs and status alerts.<br>3. **MinIO S3 Object Storage:** Storage for citizen proofs, application attachments, and PIO responses. | `Available` | `BE/src/payu/`; `BE/src/sms/`; `BE/src/documents/services/minio.service.ts` |
| **APIs exposed** | REST/JSON under `/api/v1` prefix; 20 controllers, 111 endpoints; health check at `/health`. | `Available` | `BE/src/main.ts`; 20 `*controller.ts` files |
| **APIs consumed** | PayU payment redirect and verification API; BDAGOV SMS gateway HTTP API; MinIO S3 API. | `Available` | `BE/src/payu/services/payu.service.ts`; `BE/src/sms/services/sms.service.ts` |
| **Major workflows** | 1. *Citizen Online Filing:* OTP Login &rarr; Profile check &rarr; RTI Subject & Details &rarr; Dept/PIO selection &rarr; Document upload &rarr; PayU Payment (or BPL upload) &rarr; Submission &rarr; SMS confirmation.<br>2. *Helpdesk Counter Filing:* Walk-in applicant &rarr; Helpdesk entry &rarr; IPO verification &rarr; Doc scanning &rarr; Assignment.<br>3. *PIO Response Workflow:* Post-desk login &rarr; Assigned cases review &rarr; Request additional fee / draft response &rarr; Attach response file &rarr; Status marked CLOSED.<br>4. *FAA Appeal & Summons:* Unsatisfied applicant files First Appeal &rarr; FAA schedules hearing date &rarr; Summons issued with date/venue &rarr; Hearing conducted &rarr; Order uploaded. | `Available` | `FE/src/App.tsx`; `FE/src/pages/`; `BE/docs/API_FRONTEND.md` |
| **Reports / dashboards** | Citizen Tracking Dashboard, PIO Dashboard, Helpdesk Assigner Dashboard, PRO Assigner Dashboard, FAA Dashboard, Summons Schedule Calendar Panel, Department Applications Overview. | `Available` | `FE/src/pages/PioDashboard.tsx`; `FE/src/pages/schedule/ScheduleCalendarPanel.tsx`; `FE/src/components/` |
| **Mobile application** | Not Applicable (Responsive web application optimised for mobile browsers). | `Not Applicable` | `FE/vite.config.ts`; `FE/src/layouts/` |
| **Web application** | React Single Page Application (SPA) with Redux Toolkit and React Router. | `Available` | `FE/package.json` |
| **Backend services** | Modular NestJS TypeScript monolithic backend service on Node.js runtime. | `Available` | `BE/package.json`; `BE/src/app.module.ts` |
| **Batch / scheduled jobs** | None found (no `@nestjs/schedule` or Cron jobs configured in repository). | `Available` (verified absent) | Source search in `BE/src/` |
| **Notification services** | Active SMS dispatch via Karnataka Mobile Seva gateway (`SMS_SENDER_ID: BDAGOV`). Email/SMTP service is not configured. | `Partially Available` | `BE/src/sms/`; `BE/.env.example` |
| **File / document processing** | ID proof / BPL certificate uploads, Indian Postal Order (IPO) payment proofs, PIO response documents, Summons notices, client-side PDF generation (jsPDF, html2canvas). | `Available` | `BE/src/documents/`; `FE/package.json` (jsPDF, html2canvas) |
| **AI / ML components** | None configured in repository. | `Not Applicable` | Dependency review of `package.json` |
| **Requirements / SRS / SOW** | Statutory framework defined by RTI Act 2005. BDA Office Orders and Section 4(1)(a)/4(1)(b) public disclosures in `FE/src/assets/sec-4-1a/`. Formal SOW/SRS document `Not Available` in repository. | `Partially Available` | `FE/src/assets/sec-4-1a/*.pdf`; `BE/docs/API_FRONTEND.md` |
| **Architecture document** | Not Available as a standalone diagram document in repository (logical architecture derived from code below). | `Not Available` | — |

---

## B. TECHNOLOGY & ARCHITECTURE

### 3. Technology Stack (verified against build files)

#### Frontend [Project] — Source: `FE/package.json`, `FE/vite.config.ts`

| Item | Value | Evidence / Note |
| :--- | :--- | :--- |
| **Framework** | **React ^19.2.4** | `FE/package.json` (`dependencies.react`) |
| **Language** | **TypeScript ~6.0.2** | `FE/package.json` (`devDependencies.typescript`) |
| **Build tool** | **Vite ^8.0.4** (`@vitejs/plugin-react ^6.0.1`) | `FE/vite.config.ts`; `npm run build` |
| **Package manager** | **npm** (lockfile: `package-lock.json`) | `FE/package-lock.json` |
| **Routing** | **react-router-dom ^7.14.1** | `FE/src/App.tsx` (BrowserRouter, Routes, Route) |
| **State management** | **Redux Toolkit ^2.11.2**, **react-redux ^9.2.0** | `FE/src/store/` (reducers, slices) |
| **HTTP client** | **Axios ^1.15.2** | `FE/src/lib/api.ts`, `FE/src/lib/rtiApi.ts` |
| **Styling & UI libraries** | **Tailwind CSS ^4.2.2** (`@tailwindcss/vite`), **@ant-design/icons ^6.1.1**, **framer-motion ^13.1.0**, **gsap ^3.15.0** | `FE/src/index.css`; component imports |
| **Internationalization (i18n)** | **react-intl ^10.1.5** (English and Kannada locales) | `FE/src/locales/en.json`, `FE/src/locales/kn.json` |
| **Document processing** | **jspdf ^4.2.1**, **html2canvas ^1.4.1** | Application summary, receipt, summons printing |
| **Code quality & linting** | **ESLint ^9.39.4**, **typescript-eslint ^8.58.0** | `FE/eslint.config.js` |
| **Automated tests** | **None** (no `*.test.ts(x)` or `*.spec.ts(x)` files in `FE/src`) | `Missing` (verified absent) |

#### Backend [Project] — Source: `BE/package.json`, `BE/src/app.module.ts`

| Item | Value | Evidence / Note |
| :--- | :--- | :--- |
| **Framework** | **NestJS 11.0.1** (`@nestjs/core`, `@nestjs/common`, `@nestjs/platform-express`) | `BE/package.json` |
| **Language & runtime** | **Node.js 20+** ; **TypeScript 5.7.3** | `BE/tsconfig.json`; `package.json` |
| **Architecture** | Modular Monolith (Controllers, Services, DataServices, Repositories/TypeORM Entities, DTOs) | 20 feature modules in `BE/src/` |
| **ORM & Database driver** | **TypeORM ^0.3.28** (`@nestjs/typeorm ^11.0.1`), **mysql2 ^3.22.3** | `BE/src/database/database.module.ts` |
| **Security libraries** | **bcrypt ^6.0.0**, **@nestjs/jwt ^11.0.2**, **passport ^0.7.0**, **passport-jwt ^4.0.1** | `BE/src/auth/` |
| **Validation & Mapping** | **class-validator ^0.15.1**, **class-transformer ^0.5.1**, `ValidationPipe` | `BE/src/main.ts` (whitelist, forbidNonWhitelisted) |
| **Object storage client** | **minio ^8.0.7** | `BE/src/documents/services/minio.service.ts` |
| **Excel / reporting** | **exceljs ^4.4.0** | `BE/package.json` |
| **Automated tests** | **Jest ^30.0.0**, **ts-jest ^29.2.5** (2 starter test files: `app.controller.spec.ts`, `app.e2e-spec.ts`) | `BE/test/app.e2e-spec.ts` |

#### Database [Project]

| Item | Value | Evidence / Note |
| :--- | :--- | :--- |
| **Technology / type** | **MySQL 8.x** (Relational DBMS) | `BE/src/database/database.module.ts` (`type: 'mysql'`) |
| **Database name / schema** | `new_rti` (single application database) | `BE/.env.example` (`DB_NAME: new_rti`) |
| **Schema management** | TypeORM entities (auto-sync disabled: `DB_SYNCHRONIZE=false` in configuration). Ad-hoc migration script: `scripts/migrate-rti-application-status-mysql.sql`. No Flyway/Liquibase tool. | `BE/src/database/database.module.ts`; `Partially Available` |
| **Tables count** | **25 registered TypeORM entity tables:** `citizen_details`, `rti_applications`, `appeal_applications`, `rti_application_documents`, `rti_application_history`, `rti_summons`, `rti_payments`, `object_store`, `departments`, `personal_details`, `post_details`, `post_person_mapping`, `post_person_mapping_history`, `staff_user`, `faa_details`, `faa_persons`, `faa_person_mapping`, `faa_person_mapping_history`, `reassign_requests`, `holidays`, `menus`, `roles`, `role_menu_mappings`, `sms_templates`, `sms_audit` | `BE/src/database/database.module.ts` |
| **Keys & constraints** | UUID primary keys on major transactional entities; Foreign Key relationships on citizen, post, application, and mapping tables. | `BE/src/**/models/*.entity.ts` |

#### Other Technologies — Verification Result

| Technology | Used? | Evidence / Note |
| :--- | :--- | :--- |
| **Redis** | `Partially Available` (Configured, not active) | Dependencies `@nestjs/cache-manager`, `ioredis`, `cache-manager-ioredis` in `package.json`; `REDIS_HOST` in `.env.example`. Active OTP store currently uses in-memory Map (`OtpStoreService`). |
| **MinIO / Object Storage** | `Yes — Active` | `BE/src/documents/services/minio.service.ts`; bucket `rti`; presigned URLs and binary streaming. |
| **Docker / Docker Compose** | `No — Absent` | No `Dockerfile` or `docker-compose.yml` present in either repository. |
| **Elasticsearch / Vector DB** | `No` | Not present in dependencies. Text searches performed via MySQL queries. |
| **Kafka / RabbitMQ** | `No` | No message brokers configured in repositories. |
| **API Gateway / Reverse Proxy** | `Not Verified — Infra` | Not in repository. Code reads `X-Forwarded-For` headers via Express. |
| **Kubernetes / Helm / Argo** | `No — Manifests absent` | No Kubernetes manifests or Helm charts found in repository. |
| **Jenkins / GitHub Actions / CI** | `No — Pipelines absent` | No CI/CD pipeline definitions (no `.github/workflows` or `Jenkinsfile`). |
| **Monitoring & Health** | `Partially Available` | Custom `/health` endpoint returning `{ ok: true, service: "rti-backend" }`; no Prometheus/Grafana stack in repository. |
| **Logging** | `Yes — Console & DB` | Console logging via NestJS Logger; database audit trail for SMS in `sms_audit` table. No central log shipping (ELK/Splunk) configuration. |
| **SIEM / WAF / DDoS** | `Not Verified` | To be obtained from Infrastructure / Security team. |
| **Third-Party Services** | `Yes — Live Integrations` | PayU payment gateway (`https://test.payu.in/_payment`); BDAGOV SMS gateway (Karnataka Mobile Seva). |

---

### 4. Architecture

| Item | Status | Detail / Evidence |
| :--- | :--- | :--- |
| **Application architecture diagram** | `Not Available` | No standalone diagram in repositories. Logical architecture derived from source code below. |
| **Deployment / Network / Cloud architecture** | `Not Verified` | To be obtained from DevOps / Infrastructure team. |
| **Integration architecture** | `Available` | PayU payment gateway integration (redirect / POST callbacks); BDAGOV SMS gateway integration; MinIO S3 SDK. |
| **Data architecture** | `Partially Available` | 25 TypeORM entities in MySQL `new_rti` database; MinIO S3 bucket `rti` for binary storage. No ER diagram in repo. |
| **Authentication architecture** | `Available` (code) | Citizen: Mobile OTP (4-digit, 5-min TTL) &rarr; JWT token (role: `citizen`). Staff: Desk login / username + bcrypt &rarr; JWT token (role: `SUPERADMIN`, `PIO`, `FAA`, `HELPDESK`, `PRO_ASSIGNER`, etc.) carrying post ID. |
| **Security architecture** | `Partially Available` | Section 10. Role-based guards (`RolesGuard`), `JwtAuthGuard`, `ValidationPipe`, bcrypt hashing. |

#### Logical Architecture derived from repository [Project]:

```
+----------------------------------------------------------------------------------------------------+
|                                     CLIENT BROWSERS & INTERFACES                                   |
|   +---------------------------------------+      +----------------------------------------------+  |
|   |   Citizen Portal (Web & Mobile Web)   |      |   Staff Workstations (PIO / FAA / Helpdesk)   |  |
|   |   - React 19 SPA (Vite 8, Tailwind)   |      |   - Desk-centric Post Login                  |  |
|   |   - Bilingual: English & Kannada      |      |   - Dashboard, Summons Calendar & Dispatch   |  |
|   +---------------------------------------+      +----------------------------------------------+  |
+----------------------------------------------------------------------------------------------------+
                                      |                                   |
                                      | HTTPS (TLS via Proxy) / REST API  |
                                      v                                   v
+----------------------------------------------------------------------------------------------------+
|                         BACKEND APPLICATION SERVER (Port 3300: NestJS 11 Monolith)                 |
|   Global Prefix: /api/v1     |     ValidationPipe (Whitelist: true)     |     CORS Allowed Origins |
|                                                                                                    |
|   +-------------------+  +--------------------+  +--------------------+  +---------------------+   |
|   |   Auth Module     |  | RtiApplications    |  | Faa & Summons      |  | Post & User Mapping |   |
|   | - Citizen OTP     |  | - Submission       |  | - First Appeals    |  | - Post Details      |   |
|   | - Staff bcrypt    |  | - Status Lifecycle |  | - Summons Notices  |  | - Post-Person Map   |   |
|   | - JWT Sign/Verify |  | - Copy Fee Demand  |  | - Hearing Calendar |  | - Desk Binding      |   |
|   +-------------------+  +--------------------+  +--------------------+  +---------------------+   |
|   +-------------------+  +--------------------+  +--------------------+  +---------------------+   |
|   | Documents Module  |  | Payments (PayU)    |  | SMS Module (BDAGOV)|  | Master Data         |   |
|   | - Upload Cap 25MB |  | - Hash Generator   |  | - Templates        |  | - Holidays Master   |   |
|   | - Presigned URLs  |  | - Return Callback  |  | - Gateway Dispatch |  | - Departments       |   |
|   | - Object Stream   |  | - Reconciliation   |  | - Delivery Audit   |  | - Role Menu Map     |   |
|   +-------------------+  +--------------------+  +--------------------+  +---------------------+   |
+----------------------------------------------------------------------------------------------------+
          |                            |                       |                       |
          v                            v                       v                       v
+-------------------+        +-------------------+   +-------------------+   +-------------------+
|  MySQL 8 Database |        |  MinIO Object S3  |   | PayU Gateway      |   | BDAGOV SMS Seva   |
|  - Schema: new_rti|        |  - Bucket: rti    |   | - Registration fee|   | - Karnataka Seva  |
|  - 25 TypeORM     |        |  - Citizen Proofs |   | - Additional pages|   | - OTPs & Alerts   |
|    Entity Tables  |        |  - Responses/IPO  |   | - Redirect & POST |   | - BDAGOV sender ID|
+-------------------+        +-------------------+   +-------------------+   +-------------------+
```

| Component | Identified In Repository | Evidence |
| :--- | :--- | :--- |
| **Application server** | NestJS 11 on Express (Node.js runtime, port 3300) | `BE/src/main.ts`; `BE/package.json` |
| **Web server for SPA** | Vite build output (`dist/`); hosting setup not in repository | `FE/package.json`; `FE/vite.config.ts` |
| **API Gateway / Load Balancer** | Not Verified in repository (expected in deployment) | To be obtained from DevOps |
| **Database & Object Storage** | MySQL 8 (Relational DBMS) + MinIO S3 Object Storage | `BE/src/database/database.module.ts`; `BE/src/documents/` |
| **Cache / In-memory Store** | In-memory Map with TTL (`OtpStoreService`); Redis dependencies ready | `BE/src/auth/services/otp-store.service.ts` |
| **External Gateways** | PayU (Payment Gateway), BDAGOV (Karnataka Mobile Seva SMS) | `BE/src/payu/`; `BE/src/sms/` |
| **Identity Provider** | In-application JWT + BCrypt + OTP generation (no external SSO/SAML/LDAP) | `BE/src/auth/` |
| **Security / Monitoring** | NestJS guards (`JwtAuthGuard`, `RolesGuard`), `/health` endpoint | `BE/src/auth/`; `BE/src/app.controller.ts` |

---

## C. SECURITY ASSESSMENT

### 5. Repository & Development Practices [Project]

| Item | Finding | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Repository structure** | FE: `src/{assets,components,contexts,data,hooks,layouts,lib,locales,pages,store}`<br>BE: `src/{auth,citizen,common,database,departments,documents,faa-*,holidays,menus,payu,personal-details,post-details,reassign-requests,roles,rti-applications,rti-payments,sms,staff}` | `Available` | `FE/src/` (218 files); `BE/src/` (188 files) |
| **Branching strategy** | Feature branch workflow (`feature/*` branches merged into `main`); `prod` branch exists on remote. | `Partially Available` | `git branch -r` on FE and BE |
| **Development / UAT / Prod branches** | FE: `main`, `prod`, 30+ feature branches.<br>BE: `main`, `prod`, 25+ feature branches. | `Available` | `git branch -a` |
| **Pull request process** | Extensively utilized: **136 PR merges in FE** (up to PR #136); **72 PR merges in BE** (up to PR #72). | `Available` | `git log --merges` on FE and BE |
| **Code review / approvals** | PR review records and mandatory approvals managed on GitHub. | `Not Verified` | GitHub Pull Request review pages |
| **Branch protection** | GitHub branch protection rules for `main` and `prod`. | `Not Verified` | GitHub &rarr; Settings &rarr; Branches |
| **Commit standards** | Structured feature commit messages; no automated `commitlint` or `husky` pre-commit hooks configured. | `Available (gap)` | `git log` |
| **Code ownership** | No `CODEOWNERS` file present in either repository. | `Not Available` | Repository root check |
| **Release / versioning / tagging** | No git release tags created (0 tags in FE and BE); semantic versioning not tracked via git tags. | `Not Available` | `git tag` (0 tags found) |
| **Release & deployment history** | Not Available in repository (managed externally or manually). | `Not Available` | — |
| **Coding standards** | ESLint configurations (`FE/eslint.config.js`, `BE/eslint.config.mjs`); Prettier config (`BE/.prettierrc`); backend API guides in `BE/docs/`. | `Available` | `eslint.config.*`; `BE/docs/STAFF_POST_LOGIN_MODEL.md` |
| **Repository access controls** | Restricted to authorized organization contributors on GitHub. | `To be obtained from Org Admin` | GitHub Organization Members |

---

### 6. SDLC & Development Process

| Area | Finding | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Requirement management** | RTI Act 2005 statutory compliance; BDA Section 4(1)(a) gazette documents; technical API specs in `BE/docs/API_FRONTEND.md`. Formal JIRA/Azure DevOps ticketing not in repo. | `Partially Available` | `FE/src/assets/sec-4-1a/`; `BE/docs/` |
| **Development process** | Feature branch &rarr; PR &rarr; Code review &rarr; Merge to `main`. | `Available` | Git history and merge commits |
| **Unit / integration testing** | Backend: Starter controller unit spec and e2e spec with Jest. Frontend: No automated test suite configured. | `Partially Available (gap)` | `BE/src/app.controller.spec.ts`; `BE/test/app.e2e-spec.ts` |
| **System testing / UAT** | Conducted on UAT server (`14.97.141.54:7800`); formal test sign-off certificates not in repository. | `Not Available` | To be obtained from QA / PM |
| **Security testing (SAST/DAST)** | No SAST/DAST or automated dependency vulnerability scanning configured in repository. | `Not Available` | No tool config in repo |
| **Performance testing** | No k6 or JMeter performance testing scripts or reports committed in repository. | `Not Available` | To be obtained from QA / DevOps |
| **Release / Rollback process** | Manual deployment process; no automated rollback configuration documented in repo. | `Not Available` | To be obtained from DevOps |
| **SDLC policy & Secure coding** | Organisational SDLC policy not stored in project repository. | `To be obtained from Org` | Central compliance repository |

---

### 7. Authentication & User Access Management [Project — verified in code]

| Control | Implementation | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Authentication (Staff)** | Login ID / PIO Desk ID + Password &rarr; Password verified with BCrypt &rarr; Staff JWT containing post ID and role. | `Available` | `BE/src/auth/services/auth.service.ts`; `BE/src/auth/controller/auth.controller.ts` |
| **Authentication (Citizen)** | Mobile Number &rarr; 4-digit OTP generated via `crypto.randomInt` &rarr; Dispatched via BDAGOV SMS &rarr; Verification returns Citizen JWT. | `Available` | `BE/src/auth/services/otp-store.service.ts`; `BE/src/auth/services/auth.service.ts` |
| **Desk-Centric Seat Binding** | Staff login for PIO seats binds to a post (`post_details`). Login is rejected unless an **ACTIVE** `post_person_mapping` exists for that seat. | `Available` | `BE/docs/STAFF_POST_LOGIN_MODEL.md`; `BE/src/auth/services/auth.service.ts` |
| **Authorization / RBAC** | NestJS guards: `JwtAuthGuard` + `RolesGuard` with `@Roles()` decorator on controllers enforcing strict access controls. | `Available` | `BE/src/auth/roles.guard.ts`; 43 `@UseGuards` and 86 `@Roles` instances |
| **Roles defined** | `SUPERADMIN`, `PIO`, `FAA`, `HELPDESK`, `ASSIGNER`, `PRO_ASSIGNER`, `FINANCE_MEMBER`, and `citizen`. | `Available` | `BE/src/common/enums/index.ts` (`StaffUserRole`) |
| **Role matrix document** | Not Available as a standalone signed document (enforced via NestJS route decorators and database `roles` / `role_menu_mappings` tables). | `Partially Available` | `BE/src/roles/`; `BE/src/menus/` |
| **Multi-Factor Auth (MFA)** | Not implemented for staff administrators. Staff login uses single-factor password. Citizen login is OTP-only. | `Not Available (gap)` | `BE/src/auth/services/auth.service.ts` |
| **Password hashing** | **BCrypt** with configurable salt rounds (default 10 rounds). | `Available` | `BE/src/auth/services/auth.service.ts`; `BE/src/post-details/services/post-details.service.ts` |
| **Password complexity** | DTO validation on password reset endpoints enforcing string patterns. | `Available` | `BE/src/auth/dto/reset-staff-password.dto.ts` |
| **Password expiry / history** | Not implemented (no password expiry interval or past password history table). | `Not Available (gap)` | `BE/src/staff/models/staff-user.entity.ts` |
| **Failed login attempts / Lockout** | Not implemented in backend code (no account lockout threshold after consecutive failed password attempts). | `Not Available (gap)` | `BE/src/auth/services/auth.service.ts` |
| **Session timeout** | Configured via JWT expiration: Access token (`JWT_ACCESS_EXPIRES_IN=1h`), Refresh token (`7d`). Token stored in browser `sessionStorage`. | `Available` | `BE/.env.example`; `FE/src/lib/tokens.ts` |
| **Token revocation / Logout** | Stateless JWT tokens. Client clears `sessionStorage` on logout. Server-side token blacklisting (Redis revocation) is not currently enabled. | `Partially Available (gap)` | `FE/src/lib/tokens.ts` |
| **User provisioning** | Super Admin creates person &rarr; creates post &rarr; assigns post-person mapping. Fallback desk password initialized on creation. | `Available` | `BE/src/personal-details/`; `BE/src/post-details/` |
| **De-provisioning / Activation** | Post-person mappings can be unmapped or deactivated (`status: INACTIVE`). Unmapping immediately revokes desk login capability. | `Available` | `BE/src/post-details/services/post-person-mapping.service.ts` |

---

### 8. Data Model & Data Dictionary [Project]

| Item | Detail / Implementation | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **ER diagram** | Not Available as a standalone diagram document in repository (derivable from TypeORM entity models). | `Not Available` | Can be generated from MySQL schema |
| **Data dictionary** | Not Available as a standalone data dictionary document. Documented via TypeORM entity class annotations and DTO interfaces. | `Partially Available` | `BE/src/**/models/*.entity.ts` |
| **Table list (25 tables)** | `citizen_details`, `rti_applications`, `appeal_applications`, `rti_application_documents`, `rti_application_history`, `rti_summons`, `rti_payments`, `object_store`, `departments`, `personal_details`, `post_details`, `post_person_mapping`, `post_person_mapping_history`, `staff_user`, `faa_details`, `faa_persons`, `faa_person_mapping`, `faa_person_mapping_history`, `reassign_requests`, `holidays`, `menus`, `roles`, `role_menu_mappings`, `sms_templates`, `sms_audit` | `Available` | `BE/src/database/database.module.ts` |
| **Keys / Relationships** | UUID primary keys on major transactional tables; foreign key linkages between citizens, applications, documents, payments, posts, and staff. | `Available` | TypeORM `@PrimaryGeneratedColumn('uuid')` and `@ManyToOne` relations |
| **Validation rules** | DTO-level validation using `class-validator` (`@IsNotEmpty`, `@IsEmail`, `@IsEnum`, `@MaxLength`, regex patterns). Global NestJS `ValidationPipe` with `whitelist: true`. | `Available` | `BE/src/main.ts`; `BE/src/**/dto/*.ts` |
| **PII fields (Personally Identifiable Info)** | Citizen full name, mobile number, email, residential address, gender; RTI applicant contact details, BPL card numbers, ID proofs, photos, Indian Postal Order copies in MinIO. | `Available` | `citizen_details`; `rti_applications`; `personal_details` |
| **Financial data** | Application fee amounts (₹10 / custom), PayU payment transaction IDs, PayU payment status, bank reference numbers, IPO numbers. (No credit/debit card numbers or CVVs stored — processed via PayU hosted checkout). | `Available` | `rti_payments` table; `BE/src/rti-payments/models/rti-payment.entity.ts` |
| **Authentication data** | BCrypt password hashes (`password` in `staff_user`); temporary in-memory OTP codes with 5-minute expiration; JWT signatures. | `Available` | `staff_user.password`; `OtpStoreService` |
| **Audit data** | `sms_audit` (SMS delivery logs), `post_person_mapping_history` (post assignments), `faa_person_mapping_history` (FAA assignments), `rti_application_history` (application status lifecycle changes). | `Available` | `BE/src/sms/entities/sms-audit.entity.ts`; mapping history entities |

---

### 9. Data Storage & Handling

| Area | Finding | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Where data is stored** | MySQL 8 (structured transactional tables), MinIO S3 (uploaded files, ID proof, response PDFs, receipts), Node.js memory (active OTP records). | `Available` | `BE/src/database/`; `BE/src/documents/` |
| **Hosting (on-prem / cloud)** | Dev / Staging server referenced on public IP: `http://14.97.141.54:7800`. Production hosting topology Not Verified. | `Not Verified — Infra` | `BE/.env.example` (`FRONTEND_URL`) |
| **Encryption at rest** | **Not configured in application code.** PII (names, mobiles, addresses) and BPL numbers stored as plain text in MySQL columns. MinIO bucket server-side encryption (SSE-S3 / SSE-KMS) not configured in repo. | `Not Available (gap)` | `citizen-details.entity.ts`; `minio.service.ts` |
| **Encryption in transit** | TLS/HTTPS not configured in application repositories. Database URL connects over plain TCP; MinIO configured with `MINIO_USE_SSL=false`. Production TLS expected at reverse proxy / load balancer. | `Not Verified in repo` | `BE/.env.example`; `minio.service.ts` |
| **Key / secret management** | Environment variables (`.env`, `.env.local`); no cloud KMS (AWS KMS, Azure Key Vault, HashiCorp Vault) integration in repository. Default credentials found in committed sample files (Section 25.2). | `Partially Available (gap)` | `BE/.env.example`; `BE/.env.local` |
| **Backup management** | No automated database dump scripts, backup policies, or restore testing records in project repository. | `To be obtained from DBA/Infra` | — |
| **Data retention & purging** | No scheduled background jobs or purging routines for expired OTPs, old audit events, or discarded draft applications. | `Not Available (gap)` | Source search in `BE/src/` |

---

### 10. Application Security Controls [Project — verified in code]

| Control | Implementation | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Input validation** | Server-side: `ValidationPipe` with `whitelist: true` and `forbidNonWhitelisted: true`; `class-validator` decorators on all DTOs. Client-side: regex and form validation in React components. | `Available` | `BE/src/main.ts`; `BE/src/**/dto/*.ts`; `FE/src/pages/` |
| **Authentication / Authorization** | Stateless JWT authentication (Passport JWT strategy). Enforced across all non-public routes with `JwtAuthGuard` and `RolesGuard`. | `Available` | `BE/src/auth/jwt-auth.guard.ts`; `BE/src/auth/roles.guard.ts` |
| **Token storage (browser)** | Stored in browser `sessionStorage` (`rti_api_citizen_jwt`, `rti_api_pio_jwt`). Cleared on browser tab closure or explicit logout. (Token is accessible to JavaScript). | `Partially Available (risk)` | `FE/src/lib/tokens.ts` |
| **API security** | All private endpoints require Bearer token. Public endpoints limited to: `/health`, `/auth/login`, `/auth/citizen/send-otp`, `/auth/citizen/verify-otp`, `/post-details` (PIO list), `/payu/success`, `/payu/failure`. | `Available` | `BE/src/auth/controller/auth.controller.ts`; `BE/src/payu/` |
| **Secure headers & Helmet** | Configuration flag `ENABLE_HELMET=true` and `ENABLE_CSP=true` in `.env.example`, but `helmet` middleware is not imported or registered in `main.ts`. | `Partially Available (gap)` | `BE/.env.example`; `BE/src/main.ts` |
| **CORS** | Configured via `app.enableCors()` reading from comma-separated `CORS_ORIGIN` env list, with fallback to all origins in development; `credentials: true` enabled. | `Available` | `BE/src/main.ts` (lines 17–20) |
| **CSRF protection** | Disabled by design — acceptable for stateless, Authorization Bearer header API endpoints with no cookie authentication. | `Available (by design)` | Stateless JWT architecture |
| **SQL injection prevention** | TypeORM repository abstraction and parameterized QueryBuilder queries; prevents direct SQL interpolation. | `Available` | `BE/src/**/services/*.service.ts` |
| **XSS protection** | React automatically escapes JSX content. React does not use `dangerouslySetInnerHTML` for user-supplied data. | `Available` | `FE/src/` component tree |
| **File upload security** | Multer memory storage; 25 MB max size cap enforced (`DOCUMENT_UPLOAD_MAX_BYTES`); application access check performed before presigning/uploading to MinIO. Client-supplied MIME type trusted; no file magic-byte validation. | `Partially Available` | `BE/src/documents/controller/documents.controller.ts`; `documents.service.ts` |
| **Malware / Antivirus scanning** | Not implemented. No ClamAV or third-party AV scanning integrated for uploaded documents. | `Not Available (gap)` | `BE/src/documents/` |
| **Rate limiting / Brute-force** | Configuration flags `ENABLE_RATE_LIMITING=false` present in `.env.example`. `@nestjs/throttler` is not installed or active in `AppModule`. | `Not Available (gap)` | `BE/src/app.module.ts`; `BE/package.json` |
| **Error handling** | Standard NestJS exception filters returning structured JSON error payloads; detailed stack traces not leaked to API clients. | `Available` | `BE/src/` controllers and services |
| **Audit trail** | Database audit logging for SMS notifications (`sms_audit`) and assignment lifecycle tracking (`post_person_mapping_history`, `faa_person_mapping_history`, `rti_application_history`). | `Available` | `BE/src/sms/entities/sms-audit.entity.ts`; `BE/src/rti-applications/` |
| **Dev / test override flags** | In non-production environments, `OTP_FIXED_CODE` and `dev_otp` in response payload allow bypassing SMS delivery for testing. Must be disabled in production. | `Available (gap)` | `BE/src/auth/services/otp-store.service.ts`; `BE/docs/API_FRONTEND.md` |

---

### 11. VAPT / Security Audit / Code Review

| Assessment | Status |
| :--- | :--- |
| **VAPT (Web application & API)** | `Not Available – To be obtained from Security/Compliance Team` (No report in repositories) |
| **CERT-In empanelled audit / Safe-to-host certificate** | `Not Available – To be obtained from Security/Compliance Team` |
| **Static Application Security Testing (SAST)** | `Not Available` — No automated SAST tool configuration (SonarQube, Snyk, Semgrep) in repo. |
| **Software Composition Analysis (SCA) / Dependency scan** | `Not Available` — No dependency vulnerability scan configuration in repo. |

---

### 12. WAF / DDoS / Network Security

| Control | Status | Note |
| :--- | :--- | :--- |
| **Web Application Firewall (WAF)** | `Not Verified` — To be obtained from Infra/Security | No WAF rule configuration in project repositories. |
| **DDoS protection** | `Not Verified` — To be obtained from Infra/Security | Infrastructure-level control. |
| **Firewall / Network segmentation** | `Not Verified` — To be obtained from Infra | Database and MinIO internal access isolation. |
| **Reverse proxy / Load balancer** | `Not Verified` | Application expects proxy headers (`X-Forwarded-For`). |

---

### 13. Encryption & Digital Certificates

| Area | Finding | Status |
| :--- | :--- | :--- |
| **TLS version / HTTPS** | Not configured in application repo; local development runs over HTTP. Staging URL uses HTTP (`http://14.97.141.54:7800`). | `Not Verified — Infra` |
| **SSL certificates (CA, validity)** | Not Available in repo. | `To be obtained from Infra` |
| **Database & object storage encryption** | Not configured in repository. | `Not Verified — Infra` |
| **Password hashing** | BCrypt (default 10 rounds). | `Available` (`auth.service.ts`) |
| **Token mechanism** | JWT signed with HMAC-SHA256 (`@nestjs/jwt`), access secret and refresh secret. | `Available` (`auth.module.ts`) |
| **Digital signatures on documents** | Not implemented (Application receipts and response PDFs generated via client jsPDF, not signed with DSC/e-Sign). | `Not Available` |
| **Cryptographic random generation** | Node.js `crypto.randomInt` for OTP generation; `uuidv4` for object storage identifiers. | `Available` (`otp-store.service.ts`) |

---

### 14. Incident Management

| Item | Status |
| :--- | :--- |
| **Incident identification, classification, SLA, escalation matrix, RCA** | `Not Available in project repository — To be obtained from Org (Security / Delivery)` |
| **Supporting application capability** | SMS audit trail (`sms_audit`) captures timestamps, mobile numbers, and delivery responses. |
| **Incident tickets / RCA records for this project** | `Not Available` in repository. |

---

### 15. Logging & Monitoring

| Item | Finding | Status | Evidence |
| :--- | :--- | :--- | :--- |
| **Application / error logging** | NestJS console logger outputting timestamp, context, and log level. | `Available` | `BE/src/` |
| **Audit / notification logging** | Database-backed audit trail in `sms_audit` table; assignment tenure tracking in mapping history tables. | `Available` | `sms_audit` |
| **API logging** | HTTP requests logged to console via NestJS; no dedicated morgan or correlation ID middleware in repository. | `Partially Available` | `BE/src/` |
| **Monitoring tools (Prometheus / ELK / Grafana)** | Custom `/health` endpoint returning JSON health status. No Prometheus metrics exporter or ELK log shipping in repo. | `Partially Available` | `BE/src/app.controller.ts` |
| **Log retention / Alerting dashboards** | Not Available in repository. | `To be obtained from Infra` | — |

---

### 16. CI/CD & Deployment

| Item | Finding | Status |
| :--- | :--- | :--- |
| **Source repository** | GitHub (2 repositories: `rti-frontend`, `rti-backend`) | `Available` |
| **CI tool / pipeline** | None — no GitHub Actions workflows, Jenkinsfile, or Bitbucket pipelines present in either repository. | `Not Available (gap)` |
| **Build process** | Manual: FE `npm run build` (Vite); BE `npm run build` (Nest CLI &rarr; `dist/`). | `Available (manual)` |
| **Test automation in pipeline** | Not Available. | `Not Available` |
| **Container image registry / Docker** | Not Available in repo (no Dockerfile). | `Not Available` |
| **Deployment documentation** | Starter NestJS README in backend; Vite starter README in frontend. Local setup only. | `Partially Available` |

---

### 17. Infrastructure & Hosting

All infrastructure items — hosting model, cloud provider / data centre, virtual machine specifications, storage, network firewalls, load balancers, backup infrastructure, and Disaster Recovery infrastructure — are `Not Verified — To be obtained from DevOps/Infra team`. The repositories contain only application code and local development configuration files.

---

### 18. Disaster Recovery & Business Continuity

| Item | Status |
| :--- | :--- |
| **DR architecture / site / RPO / RTO / drill frequency** | `Not Available — To be obtained from Infra / Org` |
| **Application readiness** | Stateless NestJS API instance allows horizontal scaling behind a load balancer; relational MySQL database and MinIO object storage require independent high-availability and backup configurations. |

---

### 19. Third-Party Integrations

| System | Purpose | Type / Protocol | Auth | Data Exchanged | Owner | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **PayU Payment Gateway** | Collection of RTI application fees (₹10) & additional copy charges | HTTP POST redirect / Server webhook callbacks | Merchant Key & SHA-512 Salt hash verification | Transaction ID, Application ID, Amount, Payment Status, Bank Ref Number | Client / PayU | `Live` |
| **BDAGOV SMS Gateway** | Citizen OTP verification & statutory RTI status notifications | REST / HTTP POST | Username, Password, Secure Key, Sender ID (`BDAGOV`) | Mobile Number, OTP code, RTI application number, status template text | Client (BDA) | `Live` |
| **MinIO Object Storage** | Secure storage for citizen ID proofs, BPL certs, IPO receipts, response files | S3 API over HTTP/HTTPS | Access Key & Secret Key | Binary document streams, UUID keys, Content-Type metadata | Infra | `Active` |
| **Aadhaar / DigiLocker** | Citizen Identity verification | — | — | Aadhaar number captured as optional text; not integrated with UIDAI / DigiLocker APIs. | — | `Not Applicable` |

---

### 20. Project Size & Effort

| Metric | Value | Status / Source |
| :--- | :--- | :--- |
| **Total project man-days** | [To be filled from timesheets] | `To be obtained from PM` |
| **Team size (from git commits)** | 7 active developers committing under 10 git identities | `Available` (`git shortlog`) |
| **Testers / DevOps / Architects / Support** | [To be filled] | `To be obtained from PM` |
| **Number of backend modules** | **20 NestJS feature modules** | `Available` (`BE/src/`) |
| **Number of screens / pages** | **24 page components** across 5 portals | `Available` (`FE/src/pages/`) |
| **Number of API endpoints** | **111 REST endpoints** across 20 controllers | `Available` (`*controller.ts`) |
| **Number of database tables** | **25 TypeORM entity tables** | `Available` (`database.module.ts`) |
| **External integrations** | 3 active (PayU, BDAGOV SMS Gateway, MinIO S3) | `Available` |
| **Code size** | FE: 218 source files; BE: 188 source files (406 total files in `src/`) | `Available` |
| **Total Commits & PRs** | FE: 405 commits, 136 PR merges; BE: 177 commits, 72 PR merges (582 commits total) | `Available` (`git rev-list`) |
| **Supporting documents** | Section 4(1)(a) BDA gazette orders, API frontend documentation, Staff desk login model | `Available` in repository |

---

### 21. Government / Enterprise Project Evidence

| Field | Value |
| :--- | :--- |
| **Client** | Bangalore Development Authority (BDA), Government of Karnataka |
| **Project** | Bangalore Development Authority — Right to Information (RTI) Management Portal |
| **Sector** | Government (e-Governance, Urban Development & Citizen Grievance Redressal) |
| **Scope** | End-to-end digital lifecycle of RTI applications, payment processing, PIO response dispatch, First Appeals, and Summons scheduling. |
| **Contract value** | [If permitted — To be obtained from Commercial / Management] |
| **Duration** | Started April 2026; currently active (5.5+ months) |
| **Technology** | React 19 / TypeScript, Vite 8, NestJS 11, Node.js 20, MySQL 8, MinIO S3, PayU, BDAGOV SMS Gateway |
| **Completion status** | **In Progress / UAT testing** — not suitable as a completed credential yet |
| **Official Evidence in repo** | Official BDA Section 4(1)(a) and 4(1)(b) gazette notifications for all BDA offices and departments stored in `FE/src/assets/sec-4-1a/` |

---

### 22. Quality & Certifications

ISO 9001, ISO 27001, ISO 20000, CMMI, SOC 1/2, PCI DSS, CERT-In, and data-centre/cloud certifications are organisation- or infrastructure-level and are not evidenced in the project repositories &mdash; `To be obtained from the central compliance team`. No project-level certification exists.

---

### 23. Policies Relevant to the Project

None of the listed organisational policies (Information Security Policy, Data Protection Policy, Secure SDLC Policy, Incident Response Policy, Backup Policy, Data Retention Policy, Vulnerability Management Policy, BCP/DR Policy) are present in the project repositories. `To be obtained from the central compliance team [Org]`.

#### Project-level implementation evidence that can be mapped to policies:

| Policy | Project-Level Implementation Evidence |
| :--- | :--- |
| **Password policy** | BCrypt hashing with 10 salt rounds; DTO complexity rules on reset. *Gaps:* No expiry, no history check, fixed default desk password. |
| **Access control policy** | RBAC with 8 roles enforced via `@Roles()` and `RolesGuard`; desk-centric post binding requires active mapping. |
| **Secure SDLC** | PR-based merges (136 FE, 72 BE PRs); ESLint and Prettier configs. *Gaps:* No automated CI/CD pipeline, no SAST scanning. |
| **Logging & Audit** | SMS audit trail in `sms_audit`; assignment changes in `post_person_mapping_history`. *Gaps:* No centralized SIEM/log shipping. |
| **Encryption policy** | BCrypt password hashing; HMAC-SHA256 JWT tokens; PayU SHA-512 hashes. *Gaps:* Plain HTTP dev endpoints; unencrypted PII columns. |

---

## D. EVIDENCE REGISTER

| # | Area | Requirement | Evid.? | Type | Location / Link | Date | Owner | Status |
| :- | :--- | :--- | :- | :--- | :--- | :- | :--- | :--- |
| 1 | Project | RTI Disclosures & Scope | Yes | Official PDF | `FE/src/assets/sec-4-1a/*.pdf` | Active | PM / Client | `Available` |
| 2 | Repository | Source repositories | Yes | Git Remotes | `GitHub: Inventechinfosolutions/rti-frontend, /rti-backend` | 08-10-2026 | Tech Owner | `Available` |
| 3 | Repository | PR-based merge history | Yes | Git Merges | `git log --merges` (FE #1–#136, BE #1–#72) | Apr–Oct 2026 | Tech Owner | `Available` |
| 4 | Repository | Code review approvals | Unknown | Screenshot | GitHub PR pages | — | Tech Owner | `Not Verified` |
| 5 | Repository | Branch protection rules | Unknown | Screenshot | GitHub &rarr; Settings &rarr; Branches | — | GitHub Admin | `Not Verified` |
| 6 | Repository | Release tags / history | No | Git Tags | `git tag` (0 tags found) | — | Tech Owner | `Not Available` |
| 7 | Technology | Frontend stack | Yes | Configuration | `FE/package.json`, `FE/vite.config.ts` | 08-10-2026 | Tech Owner | `Available` |
| 8 | Technology | Backend stack | Yes | Configuration | `BE/package.json`, `BE/src/app.module.ts` | 08-10-2026 | Tech Owner | `Available` |
| 9 | Architecture | Architecture diagram | No | Diagram | — | — | Architect | `Not Available` |
| 10 | Authentication | Staff login + JWT | Yes | Repository | `BE/src/auth/services/auth.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 11 | Authentication | Citizen Mobile OTP | Yes | Repository | `BE/src/auth/services/otp-store.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 12 | Authentication | MFA for staff admins | No | — | Single factor password only | — | Tech Owner | `Not Available` |
| 13 | Authentication | Account lockout policy | No | — | No lockout counter implemented | — | Tech Owner | `Not Available` |
| 14 | Authentication | Password complexity | Yes | Repository | `BE/src/auth/dto/reset-staff-password.dto.ts` | 08-10-2026 | Tech Owner | `Available` |
| 15 | Authorization | RBAC & 8 Roles | Yes | Repository | `BE/src/auth/roles.guard.ts`; `BE/src/common/enums/` | 08-10-2026 | Tech Owner | `Available` |
| 16 | Authorization | Desk seat binding | Yes | Repository / Doc | `BE/docs/STAFF_POST_LOGIN_MODEL.md` | 08-10-2026 | Tech Owner | `Available` |
| 17 | Session | Token TTL & expiry | Yes | Configuration | `BE/.env.example` (`JWT_ACCESS_EXPIRES_IN=1h`) | 08-10-2026 | Tech Owner | `Available` |
| 18 | Audit | SMS audit trail | Yes | Repository | `BE/src/sms/entities/sms-audit.entity.ts` | 08-10-2026 | Tech Owner | `Available` |
| 19 | Audit | Assignment history | Yes | Repository | `post_person_mapping_history.entity.ts` | 08-10-2026 | Tech Owner | `Available` |
| 20 | Data | Database schema | Yes | Repository | `BE/src/database/database.module.ts` (25 entities) | 08-10-2026 | Tech Owner | `Available` |
| 21 | Data | ER diagram / dictionary | No | Document | — | — | Tech Owner | `Not Available` |
| 22 | Data | PII identification | Yes | Repository | `citizen-details.entity.ts`, `personal-details.entity.ts` | 08-10-2026 | Tech Owner | `Available` |
| 23 | Encryption | Password hashing | Yes | Repository | `BE/src/auth/services/auth.service.ts` (BCrypt 10 rounds) | 08-10-2026 | Tech Owner | `Available` |
| 24 | Encryption | TLS in transit | No | Configuration | Plain HTTP dev URL in configuration | — | Infra | `Not Verified` |
| 25 | Encryption | Encryption at rest | No | Configuration | Plain text database columns in MySQL | — | Infra | `Not Verified` |
| 26 | File security | Upload size limit (25MB) | Yes | Repository | `BE/src/documents/services/documents.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 27 | File security | Malware / AV scan | No | — | No antivirus scanner integrated | — | Tech Owner | `Not Available` |
| 28 | API security | Rate limiting / throttle | No | Configuration | `ENABLE_RATE_LIMITING=false`; throttler absent | — | Tech Owner | `Not Available` |
| 29 | Testing | Backend unit tests | Yes | Repository | `BE/src/app.controller.spec.ts`, `BE/test/` | 08-10-2026 | Tech Owner | `Partially Available` |
| 30 | Testing | Frontend unit tests | No | — | No test files in frontend repository | — | Tech Owner | `Not Available` |
| 31 | Testing | Performance / load test | No | Report | No load test report in repository | — | QA / DevOps | `Not Available` |
| 32 | VAPT | Latest VAPT report | No | Report | — | — | Security Team | `To be obtained` |
| 33 | VAPT | Safe-to-host certificate | No | Certificate | — | — | Security Team | `To be obtained` |
| 34 | CI/CD | Pipeline automation | No | Configuration | No pipeline files in repository | — | DevOps | `Not Available` |
| 35 | Deployment | Containerization | No | Configuration | No Dockerfile or docker-compose in repo | — | DevOps | `Not Available` |
| 36 | Infra | Hosting / WAF / DDoS | No | — | Infrastructure level | — | Infra | `To be obtained` |
| 37 | Backup | Database backup logs | No | Report / Log | — | — | DBA / Infra | `To be obtained` |
| 38 | Monitoring | Health endpoint | Yes | Repository | `BE/src/app.controller.ts` (`/health`) | 08-10-2026 | Tech Owner | `Available` |
| 39 | Integrations | PayU payment gateway | Yes | Repository | `BE/src/payu/services/payu.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 40 | Integrations | BDAGOV SMS gateway | Yes | Repository | `BE/src/sms/services/sms.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 41 | Integrations | MinIO Object Store | Yes | Repository | `BE/src/documents/services/minio.service.ts` | 08-10-2026 | Tech Owner | `Available` |
| 42 | Policies | Org security policies | No | Policy Docs | — | — | Compliance | `To be obtained` |

---

## E. DOCUMENT REGISTER

| Document | Status | Location |
| :--- | :--- | :--- |
| **BDA Section 4(1)(a) & 4(1)(b) RTI Gazette Disclosures** | `Available` | `FE/src/assets/sec-4-1a/*.pdf` (Official gazette orders across all BDA branches) |
| **Backend API Reference Specification** | `Available` | `BE/docs/API_FRONTEND.md` (608 lines; detailed endpoint and payload contracts) |
| **Staff Desk Login & Post Mapping Architecture** | `Available` | `BE/docs/STAFF_POST_LOGIN_MODEL.md` (Post-centric seat model documentation) |
| **Database Schema Migration Script** | `Available` | `BE/scripts/migrate-rti-application-status-mysql.sql` |
| **SuperAdmin Seed Scripts** | `Available` | `BE/scripts/seed-superadmin.ts` |
| **Statement of Work (SOW) / SRS** | `To be obtained from PM` | Not committed in project repositories |
| **Architecture Diagrams (App, Network, Cloud)** | `Not Available` | To be prepared by Solution Architect |
| **ER Diagram & Data Dictionary** | `Not Available` | To be generated from MySQL schema |
| **VAPT Reports & Safe-to-Host Certificate** | `To be obtained from Security` | Security / Compliance team |
| **Backup & DR Test Reports** | `To be obtained from Infra` | Infrastructure team |
| **Purchase Order (PO) / Client Sign-off** | `To be obtained from Commercial` | Commercial team |
| **Organisation Policies & Certifications (ISO/CMMI)** | `To be obtained from Central Compliance` | Central compliance repository |

---

## F. GAPS

### F.1 Gap list

| # | Area | Gap Description | Category | Recommended Action | Owner |
| :- | :--- | :--- | :--- | :--- | :--- |
| 1 | **Secrets** | Hardcoded credentials and secret defaults committed in `.env.example` and `.env.local` (Section 25.2). | `Missing control — HIGH` | Purge real secrets from git history, rotate all database, SMS, PayU, and JWT credentials, replace with generic placeholders. | Tech Owner + DevOps |
| 2 | **Access** | Default desk password constant fallback in code (`PIO@ChangeMe1`) when creating posts. | `Missing control` | Enforce mandatory cryptographically secure random password generation and forced password change on first staff login. | Tech Owner |
| 3 | **Access** | No Multi-Factor Authentication (MFA) for administrative roles (`SUPERADMIN`, `PIO`, `FAA`). | `Missing control` | Implement TOTP (Google Authenticator) or SMS/email OTP second factor for all staff and admin logins. | Tech Owner |
| 4 | **Access** | No password expiry interval or password history tracking implemented. | `Missing control` | Implement 90-day password expiration and prevent reuse of last 3 previous passwords as per organizational security policy. | Tech Owner |
| 5 | **Access** | No account lockout mechanism after consecutive failed login attempts. | `Missing control` | Implement account lockout (e.g. lock account for 30 minutes after 5 consecutive failed attempts). | Tech Owner |
| 6 | **Data** | Aadhaar numbers and citizen PII stored in plain unencrypted columns in MySQL. | `Missing control — HIGH` | Implement column-level AES-256 encryption or tokenization for citizen Aadhaar and contact numbers. Review UIDAI compliance. | Tech Owner + Security |
| 7 | **Data** | No database migration framework (Flyway / Liquibase / TypeORM migrations); schema relies on ad-hoc SQL scripts. | `Needs update` | Implement versioned TypeORM migrations or Flyway scripts to guarantee deterministic schema reproduction across environments. | Tech Owner |
| 8 | **Data** | No formal ER diagram or updated data dictionary document maintained. | `Needs update` | Generate reverse-engineered ER diagram and schema dictionary from MySQL and maintain under `docs/`. | Tech Owner |
| 9 | **Data** | No data retention, archival, or secure purging policy implemented for audit events or discarded records. | `Missing control` | Define statutory retention schedule (e.g. 3 years as per RTI guidelines) and configure scheduled archival routines. | PM + Tech Owner |
| 10 | **Transport** | Plain HTTP configured for staging server (`http://14.97.141.54:7800`); MinIO configured with `MINIO_USE_SSL=false`. | `Needs confirmation` | Enforce strict HTTPS / TLS 1.3 across all client-facing endpoints and enable TLS for MinIO and MySQL in UAT/Production. | DevOps / Infra |
| 11 | **App Security** | Rate limiting disabled in configuration (`ENABLE_RATE_LIMITING=false`); throttler guard not enabled. | `Missing control — HIGH` | Enable `@nestjs/throttler` across all public endpoints (OTP dispatch, login, tracking) to prevent brute force and SMS exhaustion. | Tech Owner |
| 12 | **App Security** | Helmet and Content Security Policy (CSP) headers flags exist in env but middleware is not loaded in `main.ts`. | `Needs update` | Register `helmet()` middleware in `main.ts` with strict CSP, HSTS, and frame protection headers. | Tech Owner |
| 13 | **App Security** | JWT tokens stored in browser `sessionStorage`; accessible to client JavaScript. | `Needs review` | Evaluate moving authentication tokens to `HttpOnly`, `Secure`, `SameSite` cookies to eliminate XSS token theft risk. | Tech Owner |
| 14 | **App Security** | No antivirus / malware scanning on citizen file uploads; client MIME type trusted without magic-byte verification. | `Missing control` | Integrate ClamAV stream scanner before uploading to MinIO and implement file header magic-byte validation for PDFs/images. | Tech Owner |
| 15 | **App Security** | In-memory OTP store (`OtpStoreService`) does not scale horizontally across multiple backend instances. | `Needs update` | Migrate OTP store to distributed Redis cache with TTL to support multi-instance load balancing. | Tech Owner |
| 16 | **App Security** | Dev OTP bypass (`OTP_FIXED_CODE` / `dev_otp`) present in code. | `Needs guard` | Implement strict environment guard ensuring test OTP code can never execute when `NODE_ENV=production`. | Tech Owner |
| 17 | **SDLC** | No automated CI/CD pipeline (no GitHub Actions, Jenkins, or automated build/test/scan definitions). | `Missing control` | Implement GitHub Actions workflow for automated linting, test execution, container building, and deployment. | DevOps |
| 18 | **SDLC** | No automated tests in frontend; minimal starter unit tests in backend (no domain test coverage). | `Missing control` | Establish Vitest / Jest unit and integration tests covering critical RTI calculation, payment, and submission flows. | Tech Owner + QA |
| 19 | **Repository** | No git release tags, no version management in repositories (0 tags found). | `Needs update` | Establish semantic version tagging (e.g. `v1.0.0-rc1`) linked to deployment milestones. | Tech Owner |
| 20 | **Repository** | No `CODEOWNERS` file configured; commit message standards not enforced via pre-commit hooks. | `Needs update` | Add `CODEOWNERS` and setup `husky` with `commitlint`. | Tech Owner |
| 21 | **Testing** | No performance / load testing reports or scripts in repository. | `Missing` | Execute k6 / JMeter load test simulating expected citizen peak filing load and document results. | QA / DevOps |
| 22 | **Security Assurance** | No VAPT assessment report or CERT-In safe-to-host certificate available in project repository. | `To be obtained` | Schedule CERT-In empanelled VAPT audit once technical gaps 1–16 are remediated. | Security Team |
| 23 | **Infra** | Hosting architecture, WAF, DDoS protection, firewall, and backup logs not evidenced in repo. | `To be obtained` | Obtain architecture pack, hosting specifications, and backup evidence from Infrastructure team. | Infra Team |
| 24 | **Governance** | Organisational security policies, certifications, and commercial PO/contracts not in project repository. | `To be obtained` | Obtain from Central Compliance and Commercial teams. | Compliance Team |

---

### F.2 Summary by status

| Status | Areas |
| :--- | :--- |
| **Available** | Source repositories, technology stack (React 19, NestJS 11, MySQL 8, MinIO), RBAC authorization & roles, desk-centric seat binding, BCrypt password hashing, DTO input validation, PayU payment integration, BDAGOV SMS integration, bilingual EN/KN locales, PR merge history. |
| **Partially Available** | Database schema (entities present, migrations ad-hoc), SMS audit logging, health check endpoint, Redis configuration, frontend documentation, session management via sessionStorage. |
| **Missing / High Priority Gap** | MFA for administrators, account lockout, column-level PII encryption, rate limiting / throttling, malware scanning on uploads, CI/CD automated pipelines, comprehensive automated test suites, release tagging, committed secrets in configuration. |
| **Needs update** | Migrate in-memory OTP to Redis, enable Helmet & CSP in `main.ts`, add environment guard against dev OTP in production, remove secret defaults from tracked files, generate ER diagram and data dictionary. |
| **Needs confirmation from another team** | Production hosting model, TLS certificates, WAF / DDoS protection, database backup & restore logs, DR drills & RPO/RTO, VAPT reports & CERT-In certificate, organisational compliance policies, commercial contracts. |
| **Not Applicable** | Native mobile apps (responsive web only), AI/ML components, message brokers (Kafka/RabbitMQ), external Aadhaar/DigiLocker direct APIs. |

---

## 25. Repository Review — Mandatory Checks

### 25.1 Checklist

| Item | Present? | Location / Note |
| :--- | :--- | :--- |
| **README** | Yes | `BE/README.md`, `FE/README.md` (Framework starter instructions) |
| **package.json / build files** | Yes | `FE/package.json`, `BE/package.json` |
| **Dockerfile** | No | Not present in either repository |
| **docker-compose** | No | Not present in either repository |
| **Kubernetes manifests / Helm charts** | No | Not present in repository |
| **CI/CD pipelines** | No | No GitHub Actions or Jenkins pipelines |
| **Environment configuration** | Yes | `BE/.env.example`, `BE/.env.local`, `FE/.env.local` |
| **Infrastructure-as-Code** | No | Not present in repository |
| **API documentation** | Yes | `BE/docs/API_FRONTEND.md` (Comprehensive markdown documentation) |
| **Database schema / migrations** | Partial | 25 TypeORM entities; `BE/scripts/migrate-rti-application-status-mysql.sql` |
| **Authentication implementation** | Yes | `BE/src/auth/` (Staff login, Citizen OTP, JWT issuance) |
| **Authorization implementation** | Yes | `BE/src/auth/roles.guard.ts`, `roles.decorator.ts`, `jwt-auth.guard.ts` |
| **Logging** | Yes | NestJS console logging; `sms_audit` database logging |
| **Audit trail** | Yes | `sms_audit`, `post_person_mapping_history`, `rti_application_history` |
| **Security configuration** | Yes | `BE/src/main.ts` (ValidationPipe, CORS) |
| **Encryption configuration** | Hashing only | BCrypt password hashing; no TLS / at-rest database encryption in repo |
| **Certificate configuration** | No | Not present in repository |
| **Third-party integrations** | Yes | `BE/src/payu/` (PayU), `BE/src/sms/` (BDAGOV), `BE/src/documents/` (MinIO) |
| **Monitoring configuration** | Health only | `BE/src/app.controller.ts` (`/health`) |
| **Backup scripts** | No | Not present in repository |
| **Deployment documentation** | No | No production deployment guide in repository |

---

### 25.2 Secrets found in repository — report separately to Security/DevOps

> **MANDATORY SECURITY WARNING:** Actual credential values are intentionally omitted from this report to prevent further exposure. The files listed below contain committed passwords, private keys, API secrets, or default credentials and must be treated as compromised. They must be purged from git history and rotated immediately across all non-local environments.

| # | File (tracked in git) | Type of Secret Identified | Security Risk / Note |
| :- | :--- | :--- | :--- |
| 1 | `BE/.env.example` | Hardcoded MySQL database password (`DB_PASSWORD`) | Realistic credential committed in sample file; risk of deployment using default DB credentials. |
| 2 | `BE/.env.example` | Default JWT secret strings (`JWT_SECRET`, `JWT_ACCESS_SECRET`, `JWT_REFRESH_SECRET`) | If deployed without overriding, allows arbitrary forging of JWT tokens. |
| 3 | `BE/.env.example` | Live BDAGOV SMS gateway credentials (`SMS_USERNAME`, `SMS_PASSWORD`, `SMS_SECURE_KEY`) | Exposes government SMS gateway credentials; risk of unauthorized SMS dispatch and quota exhaustion. |
| 4 | `BE/.env.example` | PayU merchant credentials (`PAYU_MERCHANT_KEY`, `PAYU_SALT`) | Exposes payment gateway keys; risk of tampering with payment hashes or callbacks. |
| 5 | `BE/.env.example` | Default MinIO credentials (`MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`) | Standard default credentials (`minioadmin`). Must be changed in shared environments. |
| 6 | `BE/.env.local` | Full local environment file committed with real credentials | Tracked in repository; should be added to `.gitignore` and removed from index. |
| 7 | `BE/src/post-details/services/post-details.service.ts` | Hardcoded default staff desk password fallback (`PIO@ChangeMe1`) | Applied to newly created PIO desk seats if env variable is unset. |
| 8 | `BE/scripts/seed-superadmin.ts` | SuperAdmin seed credentials and hardcoded password strings | Hardcoded credentials used for database seeding. |

#### Recommended Remediation:
1. Immediately rotate BDAGOV SMS credentials and PayU merchant keys on the respective provider portals.
2. Remove `.env.local` from git tracking and replace sensitive entries in `.env.example` with dummy placeholders (e.g. `YOUR_SMS_KEY_HERE`).
3. Integrate an automated secret scanning tool (e.g. GitGuardian, Gitleaks, GitHub Secret Scanning) into the development workflow.
4. Purge sensitive commits from repository history using `git-filter-repo` or BFG Repo-Cleaner if mandated by the Security Officer.

---

*End of submission. Items marked "To be obtained" or "Not Verified" must be completed by the named organizational teams (PM, DevOps, Security, Compliance) before final consolidation into the Vendor Onboarding and Security Assessment checklist.*
