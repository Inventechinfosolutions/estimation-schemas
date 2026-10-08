# ChatGPT Visualization Brief — Programme Overview (All Modules)

**How to use:** Copy PROMPT START → PROMPT END into ChatGPT for **cross-module** visuals. For deep detail, open the per-module files in this folder.

**Source:** EXAM feature pack — 12 modules, 87 features  
**DB:** `EXAM_Database_Design.md` v2.1

---

## PROMPT START

You are a solutions architect. Generate programme-level visuals for the KEONICS Examination Module platform. Prefer Mermaid.

**Produce:**
1. 12-module platform context map with primary data flows
2. Candidate end-to-end journey swimlane: OTP → register → pay → allocate → hall ticket → exam → result → certificate
3. Centre exam-day journey: centre master → schedule → ops dashboard → verify/attend → activate → conduct → submit
4. Admin configuration spine: IAM → Integration Hub → Centre → Q-Bank/Config → Notifications
5. External systems map: KGID API, Payment Gateway, SMS/Email providers
6. High-level ERD domains (13 schemas: iam, integration, centre, qbank, registration, schedule, notify, ops_centre, conduct, result, certificate, mis, audit)

### Module map

| # | Module | Features |
|---|--------|----------|
| 01 | User & Role Management | 12 |
| 02 | API Integration Hub | 4 |
| 03 | Examination Centre Management | 11 |
| 04 | Question Bank & Examination Configuration | 7 |
| 05 | Candidate Registration | 14 |
| 06 | Examination Scheduling & Allocation | 5 |
| 07 | Notification Service | 7 |
| 08 | Centre Operations | 5 |
| 09 | Secure Examination Conduct | 8 |
| 10 | Evaluation & Results | 5 |
| 11 | Certificate Management | 6 |
| 12 | Examination Administration & Reporting | 3 |

### Flow (text)

```text
[01 IAM] staff/roles/hooks
    │
[02 Integration] KGID + Payment + logs
    │
[03 Centre] capacity/network/device/bindings
    │
[04 Q-Bank + Exam Config] questions, rules, fees, security policy
    │
[05 Registration] OTP, govt/other, prefs, pay, confirm
    │
[06 Schedule] session → allocation → seat → hall ticket → credential
    │
[07 Notify] templates/channels/dispatch/inbox
    │
[08 Centre Ops] verify, attendance, activate, live monitor
    │
[09 Conduct] login gate, paper, timer, security, submit lock
    │
[10 Results] evaluate, score, publish
    │
[11 Certificate] issue, PDF/QR, public verify, cancel
    │
[12 MIS] centre / category-dept / certificate reports
```

### Key external actors
- Government KGID API
- Payment gateway
- SMS / Email providers
- Public certificate verifier (anonymous)

Do not invent modules. Keep labels short; detail in notes.

## PROMPT END
