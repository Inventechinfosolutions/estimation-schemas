# Claim Management System

# Clarifications sought by Hon’ble SPLOCA — simple explanations

**To:** Special Officer & Competent Authority (SPLOCA)  
**From:** InvenTech  
**Subject:** Plain-language reply to remarks on the Claim Management System Statement of Work  
**Date:** 7 September 2026  
**Reference:** Communication of Changes / Modifications in Statement of Work – Claim Management System  

---

## Purpose of this note

Hon’ble SPLOCA reviewed the Claim Management System Statement of Work and asked for clearer wording on some terms, and directed that some items **should not** be part of this software.

This note explains each remark in simple language, so that the Authority and InvenTech mean the same thing. After confirmation, the Statement of Work will be updated to match.

This note does **not** change Legal Management or Valuation. Those remain separate.

---

## Reply matrix

Please confirm this matrix. Detail for each row follows in the next sections.

| Sl. | Area (as in the SoW) | Remark of Hon’ble SPLOCA / IT-2 | InvenTech reply (simple) | Proposed action |
| --- | -------------------- | ------------------------------- | ------------------------ | --------------- |
| 1 | Channels | *(no remark)* | Staff web for official work; counter intake by staff; no mobile app. | **Keep** as stated. |
| 2 | Access and identity — joiner–mover–leaver | Need clarity on joiner–mover–leaver. | **Joiner:** new officer gets a new login and post mapping; never uses the old person’s password. **Mover:** same officer changes post; history kept. **Leaver:** account switched off; records not deleted; login not reused. This is staff accounts only, not claimants. | **Keep.** Write this definition in the SoW. |
| 3 | Access and identity — two-factor authentication | What is second factor authentication? Mention. | Login has two checks: (1) username and password; (2) **OTP** on the officer’s registered official mobile or official email. Account is also activated only after OTP. | **Keep.** Name the second factor as **OTP** in the SoW. |
| 4 | FE reference data | Need clarity on FE Details and FE Management application. | **FE** = fraudulent company/scheme. **FE Management** = the **existing** Authority system (full FE file). **FE details** in Claim Management = a **read-only import** of FE identity, directors/promoters and investment schemes only. Officers select an FE; they cannot create an FE file here. | **Keep** import-only. Existing FE application **not rebuilt**. |
| 5 | Assets and recovery | Assets and recovery are not part of this. | Attached assets, attachment orders, title/e-Khata/dues, valuation summary, auction and recovered-amount register will **not** sit in Claim Management. Those remain with Legal / Valuation / existing recovery work. | **Remove** from Claim Management SoW. |
| 6 | Depositor master — structured registration and OCR | Define structured registration; detail OCR (modifiable or not; machine learning or not). | **Structured registration** = depositor stored as **fields** (name, Aadhaar, PAN, address, bank, nominee), not PDF-only. **OCR** = computer **suggests** text from the scan. Staff **may correct** every field. Original scan is not altered. Ordinary page-reading only; **no** generative AI; **no** identity decision by machine. Officer must save after check. | **Keep** with this definition. |
| 7 | Investment portfolio — cross-FE | Define “cross-FE”. | One person may have deposits in **more than one** fraudulent entity. The system keeps **one depositor profile** and shows claims/investments across those entities (four matching parameters as the Authority specifies). Stops double payment under two FE names. | **Keep** with this definition. |
| 8 | Investment portfolio — excess payment | Define “excess payment”. | A check that the person has **already received more** than the allowed principal/interest rule. The system **flags** it; the officer decides. It does **not** mean paying extra. Result is stored in the log. | **Keep** with this definition. |
| 9 | Claim lifecycle | Define it; also define additional-document loop and stage audit. **Online submission is not part of this.** | **Lifecycle (staff only):** open claim window → claimant at counter → staff enter claim and papers → officers verify in stages → Competent Authority approve/reject → status and history kept. **Additional-document loop:** officer asks for more papers; staff attach; checklist continues; earlier ticks not erased. **Stage audit:** who, what, status, remarks, date/time, documents at each stage. **Online filing by claimants is out.** | **Keep** staff path and definitions. **Remove** online submission. |
| 10 | Special situations | Not for software as there are court decisions. | Software will **not** decide ineligible depositor, legal heir, joint deposit, third-party payment, lost receipt or cash investment. Staff may **record** the court / Competent Authority order and the resulting status only. | **Remove** automatic rules. Record order only. |
| 11 | Outputs | Format to be defined. Decision dashboard is irrelevant in Outputs. | Equitable distribution and Special Court files will use **formats SPLOCA will issue**. Parameterised lists and operational reports remain. **Decision dashboard is not an output.** | **Remove** decision dashboard from Outputs. **Formats to be given by the Authority.** |
| 12 | Integrations | *(no remark)* | Business-level links only: existing FE application, legacy web application, document software in use, penny-drop, bank-officer email, NEFT/RTGS, Aadhaar and PAN verification. No interface contracts in the SoW. | **Keep** as stated. |
| 13 | Document handling and workflow | *(no remark)* | Documents and workflow stay **inside** claim screens. Not a separate document-management product. | **Keep** as stated. |
| 14 | Forensic audit (Module 01 / Legal / Valuation) | SPLOCA: Forensic audit does not enter Legal or Valuation. Tracking expert process; only some parts IT-enabled; should be standalone; existing IDEA is there. IT-2: Keep standalone; name IT-enabled parts; retain IDEA; avoid duplication. | Full forensic audit stays **outside** Claim, Legal and Valuation. **IDEA software is retained** and not rebuilt. Claim Management keeps only **activity logs** (login/OTP, who changed a record, verification ticks, penny-drop, excess-payment flag, approval/payment/closure). Module 01 is access control and logs, not a forensic-audit product. | **Keep** logs only. **Do not** put forensic audit in Legal or Valuation. **Do not** duplicate IDEA. |

---

## How to read the detailed items

Each matrix row is explained below in the same order.

For every remark we state:

1. **What was asked**  
2. **Simple meaning**  
3. **What we will do in Claim Management** (keep, define, or remove)

---

## 1. Joiner–mover–leaver

**What was asked:** Need clarity on joiner–mover–leaver.

**Simple meaning:** This is only about **staff logins**, not about claimants.

| Situation | What happens |
| --------- | ------------ |
| **Joiner** | A new officer joins. The Administrator creates a **new** user for that person, maps the correct post and role, and issues **new** username and password. The new officer never uses the previous occupant’s login. |
| **Mover** | The same officer changes post or role. The mapping is updated. Old work stays against the old post. History is kept. |
| **Leaver** | The officer leaves. The account is **switched off**. Past records are **not deleted**. That login cannot be given to the next person. |

**What we will do:** Keep this in Claim Management. Write it in the Statement of Work in the words above. Sharing passwords between staff will remain forbidden.

---

## 2. Second-factor authentication (2FA)

**What was asked:** What is second-factor authentication? Mention it.

**Simple meaning:** Login has two checks.

- **First factor:** username and password.  
- **Second factor:** a **one-time password (OTP)** sent to the officer’s **registered official mobile number or official email**, entered after the password. Without this OTP, the officer cannot enter the system.

A new account is also activated only after an OTP is completed (OTP before first use).

**What we will do:** Keep 2FA for staff. The Statement of Work will **name** the second factor as **OTP on registered official mobile / email**, unless the Authority later specifies another method.

---

## 3. FE details and FE Management application

**What was asked:** Need clarity on FE Details and FE Management application.

**Simple meaning:**

**Financial Establishment (FE)** is the company or scheme declared fraudulent (for example IMA or any other entity notified under the KPID Act).

**FE Management application** is the **existing** system already used by the Authority. It already holds the full FE file (FIR, court papers, seized documents, company bank accounts, case status). **Claim Management will not rebuild that system.**

**FE details** in Claim Management means a **read-only list** copied from that existing application, limited to what claim work needs:

- FE identity (unique id, name and aliases)  
- Directors and promoters  
- Investment schemes  

Officers **choose** an FE from this list when they work on a claim. They **cannot** create a new FE file inside Claim Management.

**What we will do:** Keep import-only FE reference data. Spell out the three items above. State clearly that FE Management stays in the existing application.

---

## 4. Assets and recovery

**What was asked:** Assets and recovery are not part of this.

**Simple meaning:** Claim Management should **not** keep:

- attached-asset register  
- attachment orders  
- title, e-Khata and dues  
- valuation summary from the Valuation application  
- auction tracking  
- a recovered-amount register inside this claim software  

Those matters belong to **Legal / Valuation / existing recovery work**, not to this Claim Management System.

**What we will do:** **Remove** assets and recovery from the Claim Management Statement of Work. If settlement later needs a total recovered figure, the Authority will supply that figure from the proper source. Claim Management will not run asset or auction work.

---

## 5. Structured registration and OCR

**What was asked:** Define structured registration. Detail OCR technology — whether it is modifiable; whether it is machine learning or not.

**Simple meaning:**

**Structured registration** means the depositor is stored as **filled fields** (name, Aadhaar, PAN, address, bank, nominee, and so on), not only as a scanned PDF that nobody can search or filter.

**OCR** means the computer **reads** a scan or photo and **suggests** text into those fields.

Our proposal, for confirmation:

| Point | Proposed rule |
| ----- | ------------- |
| Original scan | Kept unchanged. It remains the evidence. |
| OCR result | **Staff may correct** every suggested field. The officer is responsible for the saved data. |
| Machine learning / generative AI | **Not used** to invent text or decide identity. OCR is ordinary reading of the page. Any later “learning” tool would be only if the Authority separately approves it. |
| Human check | Mandatory before the profile is treated as verified. |

**What we will do:** Keep structured registration and staff-correctable OCR. Write the table above into the Statement of Work. We will not treat OCR output as final without an officer’s save.

---

## 6. “Cross-FE” and “excess payment”

**What was asked:** Define “cross-FE” and “excess payment”.

**Simple meaning:**

**Cross-FE:** One real person may have put money in **more than one** fraudulent entity. Claim Management keeps **one depositor profile** for that person and shows investments and claims **across all those entities**. Matching uses **four parameters** as the Authority specifies (for example name and identity numbers). This stops the same person being treated as two people and paid twice.

**Excess payment:** A check that the person has **already received more** than the allowed principal / interest rule. The system **flags** it for the officer. It does **not** mean paying extra. The officer records the outcome. The check is stored in the audit trail.

**What we will do:** Keep both, with these definitions written in the Statement of Work. The four matching parameters will be those the Authority confirms.

---

## 7. Claim lifecycle, additional-document loop, stage audit, and online submission

**What was asked:** Define the claim lifecycle. Also define additional-document loop and stage audit. **Online submission is not part of this.**

**Simple meaning:**

**Online submission by claimants is out of this software.** In-Karnataka and out-of-Karnataka claimants will not file claims themselves on a public or limited online form under this Statement of Work. Claims are taken **at the counter by staff**.

**Claim lifecycle** (staff only):

1. The Authority publishes the claim notice and **opens the claim window**.  
2. The claimant comes to the office. **Staff** enter the claim and take documents.  
3. Documents are checked.  
4. Officers **verify** the claim in stages.  
5. If papers are missing or unclear, the officer starts an **additional-document loop** (see below).  
6. The Competent Authority **approves or rejects** the claim.  
7. Status and history remain visible to authorised staff.

**Additional-document loop:** The officer asks for further papers. Staff attach them. The officer **continues from the same checklist**. Earlier ticks are **not erased**.

**Stage audit:** For each verification stage the system stores **who** acted, **what** was done, **status**, **remarks**, **date and time**, and **documents**. This is a log inside claim work. It is not a separate forensic-audit product.

**What we will do:** Keep staff intake, verification, additional-document loop, stage audit, approval/rejection and history. **Remove** constrained online filing by out-of-Karnataka claimants from this Statement of Work.

---

## 8. Special situations (heirs, joint deposits, cash, lost receipts, and similar)

**What was asked:** Not for software, as there are court decisions.

**Simple meaning:** The software must **not decide** by itself whether a person is ineligible, a legal heir, a joint depositor, a third-party payee, or whether a lost receipt or cash investment is accepted. Those outcomes come from **court or Competent Authority orders**.

**What we will do:** **Remove automatic rules** for these situations. Staff may **record** the court / Authority order and the claim status that follows. The software will not classify the case on its own.

---

## 9. Outputs, formats, and decision dashboard

**What was asked:** Format to be defined. Decision dashboard is irrelevant in Outputs.

**Simple meaning:**

- Equitable distribution statement and Special Court output will follow **formats the Authority will issue**. We will not invent those layouts in the Statement of Work.  
- **Decision dashboard** will **not** be listed as an output.  
- **Parameterised lists** and **structured operational reports** remain, once the Authority confirms the columns.

**What we will do:** Keep lists and operational reports. Drop “decision dashboard” from Outputs. Court and distribution **formats to be given by SPLOCA**.

---

## 10. Forensic audit (standalone; existing IDEA software)

**What was asked (Hon’ble SPLOCA):** Forensic audit does not enter Legal or Valuation modules. It is a tracking expert process. Only certain components can be IT-enabled. It should be standalone. Existing IDEA software is there.

**What IT-2 added:** Keep forensic audit standalone. Do not put it inside Legal or Valuation. Say clearly which parts are IT-enabled. Retain existing **IDEA** software. Do not duplicate it.

**Simple meaning:** Full forensic audit is **expert work**, not a new product inside Claim, Legal or Valuation. **IDEA** stays as it is.

In Claim Management we only keep **ordinary system logs** that officers and auditors need for claim work, for example:

- login success and failure, and OTP / 2FA events  
- who created or changed a depositor or claim  
- verification ticks (stage audit)  
- penny-drop result  
- excess-payment flag and officer decision  
- approval, payment and closure events  

We will **not** rebuild IDEA, and we will **not** put a forensic-audit module into Legal Management or Valuation.

**What we will do:** Rename / describe Module 01 as **access control, person–post–role, and claim activity logs** — not as a forensic-audit system. List only the log items above as IT-enabled. IDEA remains outside this software.

---

## Items with no change requested in the remark sheet

The following were listed in the “In scope” table **without** a SPLOCA comment. We treat them as **still included**, unless the Authority says otherwise:

- Staff **web** application for official claim work  
- Staff-mediated **counter** intake  
- **No mobile application** under this document  
- Integrations at **business** level (existing FE application, legacy web application, document software in use, bank penny-drop, bank-officer email, NEFT/RTGS, Aadhaar and PAN verification)  
- Document handling and workflow **inside** claim screens (not a separate document-management product)

---

## Summary of changes we will make after your confirmation

| Topic | Action |
| ----- | ------ |
| Joiner–mover–leaver | Keep. Explain in plain words. |
| Second-factor authentication | Keep. Name it as OTP on official mobile / email. |
| FE details / FE Management | Keep. Import-only; existing application not rebuilt. |
| Assets and recovery | **Remove** from Claim Management. |
| Structured registration and OCR | Keep. Staff can correct OCR. No generative AI. Not a substitute for officer check. |
| Cross-FE and excess payment | Keep. Use the definitions in this note. |
| Online claim submission | **Remove** from this Statement of Work. |
| Additional-document loop and stage audit | Keep. Use the definitions in this note. |
| Special situations as software rules | **Remove**. Record court / CA orders only. |
| Decision dashboard as an output | **Remove**. |
| Court / distribution formats | **To be given by the Authority.** |
| Forensic audit / IDEA | Standalone expert process. IDEA retained. Claim software keeps activity logs only. Not part of Legal or Valuation. |

---

## Request for confirmation

Kindly confirm that this reading of the remarks is correct.

On confirmation, InvenTech will issue a revised Claim Management Statement of Work incorporating the table above.

If any item should be read differently, please mark it on this note and we will correct it before revising the Statement of Work.

---

**End of note**
