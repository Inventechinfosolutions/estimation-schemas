# Proceedings of Meeting – Review of Existing SPLOCA Website

**Subject:** Assessment of Existing SPLOCA Website, Functional Gaps and Recommendations  

**Submitted to:** Special Officer & Competent Authority (SPLOCA), Government of Karnataka  

**Website reviewed:** SPLOCA – [https://sploca.org/](https://sploca.org/)  

**Date of review / meeting:** 12 August 2026  

**Document type:** Proceedings of Meeting (Client Submission)  

**Version:** 2.0  

---

## 1. Meeting objective

A meeting was conducted to review the existing SPLOCA website and understand the functionalities currently available in the system. The existing application was assessed from the perspective of:

- User management, role management, and post / person mapping  
- Login, registration, verification, and security  
- Data management (FE, Depositor, Asset, Claims)  
- Workflow, verification, claims, and reporting  
- User interface / usability  
- Domain suitability for a Government of Karnataka application  
- Actual readiness as demonstrated to employees / end users  
- Future scope for automation  

Based on the review, discussion, and live demonstration of the existing website, the following observations and recommendations were identified.

---

## 2. Existing system – observations and functional gaps

| Sl. No. | Area | Existing system / observation | Requirement / recommendation |
|--------:|------|-------------------------------|------------------------------|
| 1 | Role-Based Access Control | A comprehensive role-based access control mechanism is not available in the existing website. | Role-Based Access Control (RBAC) should be implemented so that users can access only the modules and functionalities assigned to their respective roles. |
| 2 | Two-Factor Authentication | Login is currently not supported with an additional authentication factor. **No 2FA / MFA** was observed during the demo. | Two-Factor Authentication (2FA) should be implemented to improve system security for all staff access. |
| 3 | Post & Role Management | There is no comprehensive provision for creating **Posts**, assigning **Roles to Posts**, mapping **Posts to Users / Persons**, and maintaining the mapping history. **Person**, **Post**, **Role–Post**, **Post–Person**, and **Permission** scenarios are not handled. | A structured Post and Role Management module should be introduced. Posts should be created, roles assigned to Posts, and Posts subsequently mapped to Users/Persons. Complete mapping history should be maintained for audit purposes. |
| 4 | Department user registration | During sign-up / login, **department users are asked to register using a personal email**. | Department users should register / be provisioned through **official or administered staff identity**, not personal consumer email as the primary path. |
| 5 | Aadhaar-related identity fields | Registration collects **Name as in Aadhaar** and **Aadhaar-linked mobile number**, but **no verification** was observed. | Unverified Aadhaar attributes must not be treated as identity proof. Either remove unverified capture or implement an approved verification mechanism before relying on such fields. |
| 6 | OTP sequencing | OTP for email and mobile is triggered **after registration is already successful**. | Email and mobile OTP verification should be completed **before** account activation / successful registration closure. |
| 7 | Credential practice for new joiners | When a new employee joins, **the same old user credentials are shared** with the new joiner. | Credential sharing must be prohibited. Each person should have a unique account; relieved staff should be deactivated; joiners should receive new accounts mapped to the correct Post/Role. |
| 8 | Website functionality | The existing website is primarily limited to adding content/documents in the form of **PDFs** for particular sections. These documents can then be accessed from the **Home Page** of the portal. | The website should be enhanced into a comprehensive application with structured modules, workflows, data capture, approvals, verification, reporting, and dashboards instead of being limited primarily to PDF-based content publishing. |
| 9 | FE Master Data | FE names are available as master data; however, there is no provision to create and maintain **complete FE details**. | A dedicated FE Management module should be provided to capture and maintain complete FE information. This data should serve as the base for automated reports, assessment, verification, and other related processes. |
| 10 | Depositor Data | There is no provision in the existing system to capture and maintain structured Depositor data. | A dedicated Depositor Management module should be introduced to capture, maintain, verify, and track complete Depositor information. |
| 11 | Asset Data | There is no provision to capture and maintain structured Asset data in the system. | A dedicated Asset Management module should be introduced to maintain complete asset details, supporting documents, status, ownership/association information, and history. |
| 12 | Claim Registration | There is currently no functionality available for registering and processing claims. | A Claim Registration and Management module should be introduced, including claim submission, document upload, verification, processing, approval/rejection, status tracking, and reporting. |
| 13 | Reports & Automation | Since structured operational data is not being captured across the required areas, comprehensive automated reporting and assessment/verification are limited. | Structured data should be captured at the source so that reports, assessments, verification, dashboards, and other processes can be automated. |
| 14 | Claimed vs demonstrated module status | It was earlier indicated (including via higher-level messaging) that **a few modules were working**. During the **demo with employees**, usable module functionality was **not demonstrated**; nothing was found working in a functionally usable manner for end users. | Written module-wise status should be provided. A re-demonstration with employee roles and evidence should be conducted before any “module complete” claim is accepted. |
| 15 | Domain suitability | The application is hosted on a **`.org`** domain ([sploca.org](https://sploca.org/)). | For a Government of Karnataka application, `.org` is not an appropriate primary official domain. Migration to an approved government domain / hosting identity (e.g. suitable `.gov.in` / State-approved arrangement) is recommended. |
| 16 | User interface / usability | The UI is not user-friendly in design or usage. Example: large dropdowns **without search / type-ahead**. Broader industry-standard UX gaps were observed. | UX remediation should be treated as mandatory — searchable dropdowns, practical filters, clearer navigation, and task-oriented screens for staff use. |

---

## 3. Login, identity and access control – combined finding

The review of login / registration together with access-control design shows that the existing website does not meet the baseline expected for a departmental SPLOCA application.

**Observed together:**

1. Department users registering with **personal email**  
2. **Aadhaar name / Aadhaar mobile** captured **without verification**  
3. **No Two-Factor Authentication**  
4. **OTP after** successful registration (instead of before activation)  
5. Absence of **Person / Post / Role–Post / Post–Person / Permission** management  
6. **Sharing of old credentials** when a new employee joins  

These are not isolated defects. Together they mean that identity, accountability, need-to-know access, and auditability cannot be reliably enforced.

**Required direction:**

- Unique **Person** identity per employee  
- **Post** catalogue and **Role-to-Post** mapping  
- **Post-to-User (Person)** mapping with effective dates and **full mapping history**  
- Role-based menu and functionality access  
- Official / administered identity for department users  
- Verified contact channels; OTP before activation  
- 2FA for staff login  
- No credential sharing; proper joiner–mover–leaver process  

---

## 4. FE data management – key observation

One of the major gaps identified is the absence of a comprehensive **FE Data Management** mechanism.

At present, the system contains FE master names, but complete FE details are not captured and maintained in a structured manner. Merely maintaining FE names is not sufficient for operational activities, assessment, verification, and reporting.

A proper FE master should capture and maintain all required information and the complete lifecycle of each FE.

Once structured FE data is available, the same data can be used for:

- FE-wise reports  
- Assessment and evaluation  
- Verification processes  
- FE performance tracking  
- Historical records  
- Status monitoring  
- Dashboard generation  
- Automated report generation  
- Future workflow and approval processes  

**Therefore, FE data management should be considered one of the key components of the proposed system enhancement.**

---

## 5. Depositor and Asset data management

The existing system does not currently provide functionality to capture and maintain structured **Depositor** data and **Asset** data.

The system is primarily being used for adding content/documents under particular sections, with the uploaded documents being made available for access through the Home Page of the portal.

There is no structured transaction-based data management for Depositors and Assets. This limits the ability to perform automated assessment, verification, tracking, reporting, and analysis.

It is therefore recommended that dedicated modules be provided for:

- Depositor registration and profile management  
- Depositor-wise details and history  
- Asset registration and management  
- Asset-wise details and supporting documents  
- Asset status and lifecycle tracking  
- Depositor-to-Asset association, wherever applicable  
- Verification and approval workflows  
- Reports and dashboards based on structured data  

---

## 6. Recommended functional modules

Based on the assessment (functional gaps + demo observations), the SPLOCA system can be developed as an integrated application with the following major components:

### A. User & Access Management

- User / Person creation and management  
- Role creation and management  
- Post creation and management  
- Role-to-Post mapping  
- Post-to-User (Person) mapping  
- User activation / deactivation  
- Mapping history  
- Role-based menu and functionality access  
- Official / administered staff identity (no personal-email primary registration for department users)  
- Verified email / mobile with OTP **before** activation  
- Two-Factor Authentication  
- Login and security audit logs  
- Prohibition of shared credentials for joiners / leavers  

### B. FE Management

- FE master creation  
- Complete FE profile / details  
- FE document management  
- FE status management  
- FE history  
- FE verification  
- FE-wise assessment  
- FE-wise reporting  

### C. Depositor Management

- Depositor registration  
- Depositor profile management  
- Depositor details and documents  
- Depositor verification  
- Depositor status tracking  
- Depositor history  
- Depositor-wise reports  

### D. Asset Management

- Asset registration  
- Asset details and classification  
- Asset document management  
- Asset verification  
- Asset status tracking  
- Asset history  
- Depositor / FE association, wherever applicable  
- Asset-wise reports  

### E. Claim Management

- Claim registration  
- Claim details capture  
- Supporting document upload  
- Claim verification  
- Claim processing workflow  
- Approval / rejection  
- Status tracking  
- Claim history  
- Claim-wise and FE / Depositor-wise reports  

### F. Workflow & Approval Management

The system should provide configurable workflows based on the actual SPLOCA business process.

Each workflow stage should have:

- Defined role / user  
- Action  
- Status  
- Remarks  
- Date and time  
- Supporting documents  
- Approval / rejection details  
- Complete audit trail  

### G. Reports & Dashboard

Once structured data is captured across all modules, dashboards and reports can be generated automatically.

Reports may include:

- FE-wise reports  
- Depositor-wise reports  
- Asset-wise reports  
- Claim-wise reports  
- Assessment reports  
- Verification reports  
- User / activity reports  
- Status-wise reports  
- Historical reports  
- Role / Post mapping reports  
- Management dashboards  

### H. Platform, domain and usability

- Migration from `.org` to an approved Government of Karnataka domain / hosting identity  
- User-friendly UI / UX (including searchable dropdowns, filters, and practical staff workflows)  
- Evidence-based module completion / UAT demonstration to employees  

---

## 7. Overall opinion on the existing website

Based on the review, the existing SPLOCA website currently functions primarily as an **information and content publishing platform**.

The existing functionality is mainly focused on adding content/documents in PDF format under specific sections and making those documents accessible through the Home Page of the portal.

However, from an application perspective, there is limited functionality for:

- Structured data capture  
- User and role management  
- Post / Person management and permissions  
- Secure registration and verification (official identity, verified contacts, 2FA)  
- FE management  
- Depositor management  
- Asset management  
- Claim registration  
- Workflow management  
- Verification  
- Transaction processing  
- Automated assessment  
- Automated reporting  
- Dashboards  
- Audit trail  

Further, the employee demonstration did not substantiate earlier indications that modules were already working in a usable form, and basic usability / official domain expectations were not met.

Therefore, significant scope exists for transforming the existing website into a secure, role-based, structured and workflow-driven application.

The enhancement should not be limited to adding more pages or PDF documents. The focus should be on capturing structured data at the source and using that data across different processes, workflows, reports, assessments, and verification activities — on a proper access-control and security foundation.

---

## 8. Overall recommendation

It is recommended that the SPLOCA platform be considered for **end-to-end redevelopment / enhancement** covering all required modules and business processes rather than implementing isolated functionalities.

The system should follow an integrated approach:

**Master Data → User & Role / Post–Person Management → Secure Login & 2FA → Structured Data Capture → Workflow → Verification → Claims / Transactions → Approval → Reports & Dashboards → Audit Trail**

This approach will ensure that information entered in one module can be effectively utilized by other relevant modules, reducing manual effort and enabling automation, while also ensuring accountability of each user action.

---

## 9. Key priority areas

The following areas should be considered as key priorities for the proposed system:

1. Role-Based Access Control  
2. Two-Factor Authentication  
3. Post, Role and User / Person mapping with complete mapping history  
4. Stop personal-email registration for department users  
5. Proper identity verification (no unverified Aadhaar reliance; OTP before activation)  
6. End credential sharing for new joiners; unique accounts per person  
7. FE Master and comprehensive FE data management  
8. Depositor data management  
9. Asset data management  
10. Claim Registration and Claim Management  
11. Structured data capture instead of dependency on PDF-based information  
12. Workflow and approval management  
13. Assessment and verification automation  
14. Dashboards and automated reports  
15. Complete audit trail and historical data  
16. Approved government domain / hosting identity (exit from `.org` as primary)  
17. User-friendly UI / UX remediation  
18. Evidence-based module status and employee-role re-demonstration  
19. Integration of all modules into a single end-to-end application  

---

## 10. Conclusion

The existing SPLOCA website currently serves primarily as a content/document publishing platform and provides limited application-level functionality. The review and employee demonstration together established that:

- Critical **login, identity, 2FA, OTP, Person/Post/Role/Permission**, and **credential-sharing** gaps exist  
- Core operational modules for **FE (complete details), Depositor, Asset, and Claim** management are not available in structured form  
- The platform is largely limited to **PDF / content publishing** rather than transaction processing, workflow, verification, and automated reporting  
- Earlier indications that modules were working were **not demonstrated** as usable functionality to employees  
- **Domain (`.org`)** and **UI usability** also require correction for a Government of Karnataka context  

There is significant scope to enhance the platform into a comprehensive application capable of managing structured data, users, roles, posts, FEs, Depositors, Assets, Claims, workflows, verification, assessment, reporting, and dashboards.

The SPLOCA system should be developed as a comprehensive end-to-end solution covering all required modules and workflows. Building the system end-to-end and integrating all modules will make the platform easier and more effective to use, enable seamless data flow and automation across processes, reduce manual dependency, and ultimately ensure that the intended purpose of the SPLOCA platform is achieved.

---

## 11. Request for action

SPLOCA is requested to:

1. Take these proceedings on record.  
2. Direct the implementing agency to submit a written response to all items in Section 2, with corrective action and timelines.  
3. Confirm whether the preferred path is **end-to-end redevelopment / enhancement** as recommended in Sections 6–8.  
4. Schedule a follow-up review after receipt of the corrective plan and module-wise status.  

---

**Submitted by:** _______________________________  

**Designation / Organisation:** _______________________________  

**Date:** 12 August 2026  

**Signature:** _______________________________  
