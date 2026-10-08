# EXAM — Estimation Summary (Feature-Wise)

Internal detail. Hours from module `_index.md` files.

## Grand totals

| Item | Hours |
|------|------:|
| All features | 4090 |
| Recommended go-live | 4090 |
| Optional / conditional | 0 |

## Module-wise summary

| # | Module | Type | Features | Hours | % of go-live |
|---|--------|------|---------:|------:|-------------:|
| 01 | Access Control and Staff User Management | Shared | 2 | 228 | 5.6% |
| 02 | Candidate Portal Access (OTP Login) | Shared | 2 | 229 | 5.6% |
| 03 | Examination, Centre and Fee Masters | Business | 4 | 494 | 12.1% |
| 04 | Candidate Registration and Fee Payment | Business | 6 | 656 | 16.0% |
| 05 | Scheduling, Allocation, Hall Tickets and Examination Credentials | Business | 4 | 409 | 10.0% |
| 06 | Question Bank and Paper Versions | Business | 2 | 256 | 6.3% |
| 07 | Secure Centre-Based Examination Conduct | Business | 6 | 794 | 19.4% |
| 08 | Evaluation, Results and Certificates | Business | 4 | 459 | 11.2% |
| 09 | Dashboards, Reports, Notifications and Audit | Shared | 4 | 565 | 13.8% |

## Feature-wise detail

### 01 — Access Control and Staff User Management

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F01-001 | Administrator Accounts and Privileges | 105 | Admin users, privilege matrix, activate/deactivate |
| F01-002 | Centre and Invigilator User Mapping | 123 | Centre mapping and centre-scoped access enforcement |

**Module total: 228 hours**

### 02 — Candidate Portal Access (OTP Login)

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F02-001 | Mobile OTP Login | 89 | Portal mobile OTP login; SMS Integration Medium |
| F02-002 | OTP Security Controls | 140 | Expiry, retry, resend, lock, session timeout; SMS Integration Complex |

**Module total: 229 hours**

### 03 — Examination, Centre and Fee Masters

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F03-001 | Examination Catalogue | 101 | Examinations open for registration and published details |
| F03-002 | Authorised Examination Centre Master | 130 | Centre identity, capacity, activation, session mapping, allocations |
| F03-003 | Fee Rules and Attempt History Basis | 121 | Category/attempt fee rules and attempt-history fee basis |
| F03-004 | Examination Parameter Configuration | 142 | Duration, marks, pass, randomisation, versions, result/certificate rules |

**Module total: 494 hours**

### 04 — Candidate Registration and Fee Payment

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F04-001 | Government Employee Registration with KGID | 140 | KGID Integration Very High (40) |
| F04-002 | Other Organisation Registration and Competent Authority Document | 95 | Embedded document upload; no DMS |
| F04-003 | Examination Selection and Centre Preferences | 70 | Two preferred centres |
| F04-004 | Fee Calculation and Payment | 164 | Payment Gateway Integration Very High (40) |
| F04-005 | Registration Confirmation and Status | 88 | Unique registration number and status |
| F04-006 | Administrator Registration Verification | 99 | Admin verify/approve where configured |

**Module total: 656 hours**

### 05 — Scheduling, Allocation, Hall Tickets and Examination Credentials

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F05-001 | Examination Schedule Management | 109 | Schedule date/time/centres/capacity |
| F05-002 | Centre Allocation | 132 | Preferences, capacity and rules |
| F05-003 | Hall Ticket Generation and Download | 79 | After schedule and allocation |
| F05-004 | Examination Credential Generation | 89 | Login ID/Password + secure communicate |

**Module total: 409 hours**

### 06 — Question Bank and Paper Versions

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F06-001 | Question Bank Maintenance | 126 | CRUD, categorise, import, activate |
| F06-002 | Random Paper Generation and Versions | 130 | A/B/C/D with key integrity |

**Module total: 256 hours**

### 07 — Secure Centre-Based Examination Conduct

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F07-001 | Authorised Centre Access Enforcement | 111 | Gate chain + denial register |
| F07-002 | Centre Dashboard and Invigilator Activation | 184 | VH dashboard and live monitor |
| F07-003 | Examination Login at Centre | 97 | Exam credentials + single session |
| F07-004 | Secure Examination Interface and Timer | 178 | VH CBT UI + central timer |
| F07-005 | Examination Submission and Response Lock | 107 | Confirm, lock, evaluation handoff |
| F07-006 | Examination Activity Recording | 117 | Append-only exam-day trail |

**Module total: 794 hours**

### 08 — Evaluation, Results and Certificates

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F08-001 | Automatic Objective Evaluation | 136 | Version-aware scoring engine |
| F08-002 | Result Publication | 101 | Publish / withhold / portal view |
| F08-003 | Certificate Generation and Download | 127 | Issue, render, download, cancel |
| F08-004 | QR Code and Public Certificate Verification | 95 | Token/QR + public status page |

**Module total: 459 hours**

### 09 — Dashboards, Reports, Notifications and Audit

| Feature ID | Feature Name | Hours | Notes |
|------------|--------------|------:|-------|
| F09-001 | Administrator Operational Dashboard | 152 | VH admin KPI dashboard |
| F09-002 | Operational and Statutory Reports | 154 | VH Excel/PDF export APIs |
| F09-003 | Candidate and Staff Notifications | 158 | SMS Complex + Email Medium integrations |
| F09-004 | System Audit Trail | 101 | Cross-module critical action audit |

**Module total: 565 hours**

## Effort profile — top features

| Feature ID | Name | Hours |
|------------|------|------:|
| F07-002 | Centre Dashboard and Invigilator Activation | 184 |
| F07-004 | Secure Examination Interface and Timer | 178 |
| F04-004 | Fee Calculation and Payment | 164 |
| F09-003 | Candidate and Staff Notifications | 158 |
| F09-002 | Operational and Statutory Reports | 154 |
| F09-001 | Administrator Operational Dashboard | 152 |
| F03-004 | Examination Parameter Configuration | 142 |
| F02-002 | OTP Security Controls | 140 |
| F04-001 | Government Employee Registration with KGID | 140 |
| F08-001 | Automatic Objective Evaluation | 136 |

## Hours by module type

| Type | Hours |
|------|------:|
| Business | 3068 |
| Shared | 1022 |

## Indicative phasing (from SOW)

| Phase | Content |
| ----- | ------- |
| Phase A | Access, masters, OTP portal, registration, fee payment |
| Phase B | Scheduling, allocation, hall tickets, credentials, question bank |
| Phase C | Centre CBT, evaluation, results, certificates, QR verification |
| Phase D | Dashboards, reports, notifications, audit, UAT |

## Exclusions (not in feature hours)

- Physical centre hardware, networking and seating
- KGID system rebuild
- Payment gateway merchant fees / bank setup
- Hosting/AMC unless separately ordered
- Legacy examination history migration (unless later ordered)
