"""HDFC Vendor Onboarding Checklist responses: one Word document per sheet (Vendor Assessment, Security Assessment).

Run from repo root:
    .venv/bin/python Projects/hdfc_enrollment/_build/build_checklist_docs.py
"""
from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

OUT = Path(__file__).resolve().parent.parent
NA = "No answer"
VENDOR = "Inventech Info Solutions Pvt. Ltd."
ADDRESS = "Jayanagar, Bengaluru 560011, Karnataka"
DATE = "9 October 2026"
NAVY = "1F3864"
LIGHT = "D9E2F3"

# ---------------------------------------------------------------------------
# Sheet 1: Vendor Assessment
# ---------------------------------------------------------------------------

PROJECTS = [
    ("KEONICS Portal", "KEONICS (Karnataka State Electronics Development Corporation Ltd.)", "Government",
     "An operations portal with modules for goods procurement, HR resources, training centres and students, facility and "
     "tenant management, service management, expenditure, plots and buyers, an infrastructure dashboard and a help desk. "
     "Most processes run through multi-level approvals.", "December 2024 to date", "Some modules live; others in progress"),
    ("BDA Grievance Redressal Portal", "Bangalore Development Authority, Government of Karnataka", "Government",
     "Citizens register grievances with a mobile OTP. The helpdesk verifies them and routes them zone-wise. The portal also "
     "handles Open House Meetings, SLA tracking and escalation, SMS alerts at every stage and MIS reports, in English and Kannada.",
     "September 2025 to date", "Live; under maintenance"),
    ("CA Site Allotment and Institution Registration Portal (CAS)", "Bangalore Development Authority, Government of Karnataka", "Government",
     "Institutions register and apply for civic amenity sites. Applications go through multi-level evaluation, online payment "
     "(Razorpay) and allotment, followed by renewals, refunds and digitally signed documents.", "February 2026 to date",
     "In progress (final stage)"),
    ("BDA Right to Information (RTI) Management Portal", "Bangalore Development Authority, Government of Karnataka", "Government",
     "Citizens file RTI applications online with an OTP login and pay the fee through PayU, or file at the helpdesk counter. "
     "Public Information Officers respond through a workflow, and first appeals are handled with hearings and summons. "
     "SMS alerts are sent in English and Kannada.", "April 2026 to date", "Live"),
    ("Correct Dimension Report Management System (CDRMS)", "Bangalore Development Authority, Government of Karnataka", "Government",
     "A web portal and mobile app for field engineers. They capture site dimensions with location checks, photos and video; "
     "officers verify them, and the system produces PDF reports and dashboards.", "July 2026 to date", "In progress"),
    ("Examination Management Portal (Computer Literacy Test)", "KEONICS, Government of Karnataka", "Government",
     "Covers the full exam cycle for Karnataka government employees: candidate registration, exam scheduling, exam centre "
     "operations, computer-based testing, automatic evaluation, results and certificates.", "September 2026 to date", "In progress"),
    ("IEBA V2", "Paperless Knowledge Inc., USA (end users: county agencies in California)", "Non-Government",
     "A multi-tenant application for time studies and administrative cost claiming. It handles time-study records, cost pools, "
     "payroll uploads, apportioning and statutory claiming reports.", "March 2026 to date", "Live"),
]

VENDOR_ITEMS = [
    dict(item="Company Profile",
         subs=[("Legal name", VENDOR),
               ("Year of incorporation", NA),
               ("Nature of business",
                "We are a software development and IT services company. We design, build, implement and support web and "
                "mobile applications, mainly for government departments and public-sector organisations."),
               ("Key services offered",
                "- Custom web application development\n"
                "- Mobile app development\n"
                "- e-Governance portals: grievance redressal, RTI, examinations, site allotment, procurement and field inspection\n"
                "- Integration with payment gateways, SMS gateways and digital signatures\n"
                "- Bilingual applications in English and Kannada\n"
                "- Deployment, maintenance and support")],
         docs=[("Company registration certificate", "Available")]),
    dict(item="Last 3 years’ balance sheet and ITR",
         subs=[("Disclose any financial liabilities or ongoing litigations", NA)],
         docs=[("Audited financial statements for the last 3 years", NA),
               ("Income Tax Returns (ITR) for the last 3 years, CA certified", NA)]),
    dict(item="Management Profile (qualifications / key persons / experience)",
         subs=[("Full name", NA), ("Designation", NA), ("Educational qualifications", NA), ("Overall experience", NA)],
         docs=[("Management details on company letterhead", NA)],
         note="Management details will be submitted on company letterhead."),
    dict(item="Share Holding Pattern (key stakeholders)",
         subs=[("Details of major shareholders and their respective stakes", NA),
               ("Foreign or institutional investors", "None")],
         docs=[("Shareholding certificate", NA), ("Latest ROC filings", NA)]),
    dict(item="Geographical Presence",
         subs=[("All office locations and delivery centres",
                f"Our office is in {ADDRESS}.\nOther offices and delivery centres: {NA}"),
               ("Presence in high-risk or regulated jurisdictions", NA)],
         docs=[("Office lease agreements / website link", NA)]),
    dict(item="Employee Strength (no of developers, support team, business team, sales)",
         subs=[("Development", NA), ("Support", NA), ("Security / Compliance", NA), ("Sales / Business etc.", NA)],
         docs=[("HR records (org chart)", NA),
               ("Department team allocation list (on letterhead, signed and stamped)", NA)],
         note="Headcount details will be submitted on company letterhead, signed and stamped."),
    dict(item="Projects implemented in government sector / Non-Government Sector",
         subs=[("Major projects in the government sector",
                "Six projects:\n"
                "- KEONICS Portal\n"
                "- BDA Grievance Redressal Portal\n"
                "- CA Site Allotment and Institution Registration Portal (CAS)\n"
                "- BDA RTI Management Portal\n"
                "- Correct Dimension Report Management System (CDRMS)\n"
                "- Examination Management Portal\n"
                "Details are in the table below."),
               ("Major projects in the non-government sector", "One project, IEBA V2. Details are in the table below."),
               ("Name of project, scope and duration", "Please see the table below.")],
         docs=[("PO copies", NA), ("Project completion certificates or details on letterhead", NA)],
         projects=True,
         note="Durations are counted from the start of development. Contract dates and values: No answer."),
    dict(item="Capability to provide Hardware and hosting services",
         subs=[("Infrastructure for hosting (cloud / on-premise)",
                "**Production:** Our government projects run at the Karnataka State Data Centre (KSDC). The KEONICS Portal is "
                "the exception and runs on the KEONICS office server. IEBA V2 runs on the client's own servers at their premises.\n"
                "**UAT:** We host UAT environments on our own servers.\n"
                "**Deployment:** Applications run on Linux servers, either in Docker containers (BDA Grievance Portal, CAS) or "
                "under the PM2 process manager with Jenkins (KEONICS Portal). Each uses MySQL for data, MinIO for files and "
                "Redis for caching."),
               ("Partnerships with data centres or cloud providers",
                "We host on infrastructure arranged by the client: KSDC, the KEONICS server or the client's own servers.\n"
                f"Direct partnership with a data centre or cloud provider: {NA}"),
               ("Physical security controls at hosting sites",
                "Physical security at production sites is managed by the hosting owner (KSDC, KEONICS or the client).\n"
                f"Physical security of our UAT servers: {NA}")],
         docs=[("Data centre ownership or co-location agreements", NA),
               ("Security architecture for hosted services (firewalls, IDS/IPS, SIEM)", NA)]),
    dict(item="Size of the biggest project handled (in terms of Man days, FP)",
         subs=[("Largest project",
                "The KEONICS Portal, in development since December 2024. It has more than 15 business modules, about 1,684 "
                "API endpoints across 214 controllers and about 173 database tables."),
               ("Man-days", "About 1,200 man-days on the KEONICS Portal."),
               ("Function Points (FP)", NA)],
         docs=[("Project scope and requirements with man-days effort",
                "Available. Please see the attached KEONICS Portal Project Scope and Effort document (IIS-PRJ-KEONICS-01)."),
               ("Architecture diagrams", NA)],
         note="Project details will be submitted on company letterhead."),
    dict(item="Quality certifications (ISO, CMMI Level 5, etc) if any",
         subs=[("ISO 9001", "We are ISO 9001 (Quality Management) certified. Certificate number and validity: to be confirmed."),
               ("ISO 27001 (Information Security)", NA),
               ("Other certifications (CMMI etc.)", "CMMI Level 3. Certificate number and validity: to be confirmed.")],
         docs=[("Valid certification copies", NA), ("Audit reports or assessment summaries", NA)]),
    dict(item="Security standards being adhered to (TLS 1.2, SHA 512, etc).",
         subs=[("TLS version (e.g., TLS 1.2/1.3)", "We use TLS 1.3 with SSL certificates."),
               ("Encryption standards (e.g., SHA-512, AES-256)",
                "- Passwords are stored as bcrypt hashes.\n"
                "- Login tokens (JWT) are signed with HMAC-SHA256.\n"
                "- OTPs and session tokens are stored as SHA-256 hashes (Examination Portal).\n"
                "- The production configuration file is encrypted with AES-256-CBC (KEONICS Portal).\n"
                "- SMS gateway request keys use SHA-512 (BDA Grievance Portal)."),
               ("Secure coding practices",
                "- Every request is validated on the server.\n"
                "- Database queries are parameterised; we never build SQL from strings.\n"
                "- User input is sanitised before it is displayed.\n"
                "- Secure HTTP headers and request rate limiting are in place.\n"
                "- Staff login is protected with a CAPTCHA.\n"
                "- Every API checks the user's role before it responds.\n"
                "- Code is merged only through reviewed pull requests, and lint checks run before each commit.")],
         docs=[("Security policy documents (encryption policy, key management policy)", NA),
               ("VAPT test reports", "Will be submitted. Our applications are audited by a CERT-In empanelled agency.")]),
    dict(item="Core technology area (J2EE/.net/Oracle)",
         subs=[("Programming languages",
                "- Back end: TypeScript on Node.js (NestJS) and Java 21 (Spring Boot 3.5)\n"
                "- Web front end: React with TypeScript\n"
                "- Mobile apps: React Native (Expo)"),
               ("Databases",
                "- MySQL 8 as the main database\n"
                "- Redis for cache and sessions\n"
                "- MinIO for documents and images")],
         docs=[("Technology stack document / policy", "Available. Technology Stack Document (IIS-STD-TS-01) attached."),
               ("SDLC policy", "Available. SDLC Policy (IIS-POL-SDLC-01) attached.")]),
    dict(item="For H/W related projects, if there is an established relationship with OEM's.",
         subs=[("OEMs partnered with", NA), ("Duration and nature of relationship", NA)],
         docs=[("Partnership certificates", NA), ("Procurement and supply (purchase orders)", NA)]),
    dict(item="Type of Company: - Sole Proprietorship, Trust, Partnership etc",
         subs=[("Type of company", "Private Limited Company")],
         docs=[("PAN card", "Available"), ("GST registration", "Available"), ("Udyog Aadhaar", "Available"),
               ("Partnership deed or incorporation certificate", "Available")]),
    dict(item="Per Man Days cost",
         subs=[("Standard per man-day rate for development", "₹12,000 per man-day"),
               ("Standard per man-day rate for support", NA),
               ("Whether rates vary by skill level or location", "Yes, rates vary with skill level and location.")],
         docs=[("Rate card", NA), ("Blended rate for man-days", NA)]),
    dict(item="Techno- commercial proposal",
         subs=[("Details about department, scope of work, technical implementation and commercials",
                "The department, scope of work and technical implementation of each project are set out in the table below.\n"
                "**Commercials:** Our development rate is ₹12,000 per man-day, and rates vary with skill level and location "
                "(see item 15).\n"
                f"Contract values of individual projects: {NA}")],
         docs=[("Techno-commercial proposal (as per techno-commercial template)",
                "A summary of our projects is given above. The full proposal in HDFC's techno-commercial template will be "
                "submitted separately.")],
         tech=True,
         note="Government projects are hosted at the Karnataka State Data Centre (KSDC), except the KEONICS Portal, which runs "
              "on the KEONICS office server. IEBA V2 runs on the client's servers. All applications use TLS 1.3 and role-based "
              "access control."),
]

TECHNO = [
    ("KEONICS Portal", "Government",
     "KEONICS (Karnataka State Electronics Development Corporation Ltd.), for procurement and operations",
     "Goods procurement, HR resources, training centres and students, facility and tenant management, service management, "
     "expenditure, plots and buyers, an infrastructure dashboard and a help desk, with multi-level approvals.",
     "- Web: React 18 and TypeScript, with Ant Design\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL (about 173 tables), Redis cache, MinIO for documents\n"
     "- Integrations: RabbitMQ mail queue, digital signature (DSC) validation\n"
     "- Deployment: Jenkins and PM2"),
    ("BDA Grievance Redressal Portal", "Government",
     "Bangalore Development Authority, Government of Karnataka, for public grievance redressal",
     "Grievance registration with a mobile OTP, helpdesk verification, zone-wise routing, Open House Meetings, SLA tracking "
     "and escalation, SMS alerts and MIS reports, in English and Kannada.",
     "- Web: React 19 and TypeScript, in English and Kannada\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL (about 54 tables), MinIO for documents, images, voice and video\n"
     "- Integrations: Karnataka Mobile Seva SMS gateway for OTPs and alerts\n"
     "- Deployment: Docker containers"),
    ("CA Site Allotment and Institution Registration Portal (CAS)", "Government",
     "Bangalore Development Authority, Government of Karnataka, for civic amenity site allotment",
     "Institution registration, site applications, multi-level evaluation, online payment, allotment, renewals, refunds "
     "and digital signing.",
     "- Web: React 19 and TypeScript, with Ant Design\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL, Redis, MinIO\n"
     "- Integrations: Razorpay payment gateway with webhooks, SMS, e-mail, DSC digital signing\n"
     "- Deployment: Docker containers"),
    ("BDA Right to Information (RTI) Management Portal", "Government",
     "Bangalore Development Authority, Government of Karnataka, for RTI Act applications and appeals",
     "Online filing with an OTP login, fee payment, helpdesk counter filing, the Public Information Officer response "
     "workflow, and first appeals with hearings and summons, in English and Kannada.",
     "- Web: React 19 and TypeScript\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL 8 (about 25 tables), MinIO for documents\n"
     "- Integrations: PayU payment gateway with hash verification, BDA SMS gateway for OTPs and status alerts"),
    ("Correct Dimension Report Management System (CDRMS)", "Government",
     "Bangalore Development Authority, Government of Karnataka, for field site inspection",
     "Field capture of site dimensions with location checks, photos and video, officer verification, PDF reports and "
     "dashboards.",
     "- Web: React 19\n"
     "- Mobile: React Native (Expo) app for field engineers\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL, MinIO for photos and video\n"
     "- Other: GPS location capture with maps, PDF report generation"),
    ("Examination Management Portal (Computer Literacy Test)", "Government",
     "KEONICS, Government of Karnataka, for examination and certification of government employees",
     "Candidate registration, exam scheduling, exam centre operations, computer-based testing, automatic evaluation, "
     "results and certificates.",
     "- Web: React 19 and TypeScript\n"
     "- Back end: Java 21 with Spring Boot 3.5\n"
     "- Data: MySQL 8 (about 46 tables, versioned Flyway scripts), Redis, MinIO for documents\n"
     "- Security: exam workstations restricted to an IP allow-list\n"
     "- Load tested before rollout"),
    ("IEBA V2", "Non-Government",
     "Paperless Knowledge Inc., USA. End users are county Health and Social Services agencies in California",
     "Time-study records, cost pools, payroll uploads, apportioning and statutory claiming reports, for several counties "
     "on one platform.",
     "- Web: React 19 and TypeScript\n"
     "- Back end: NestJS (Node.js)\n"
     "- Data: MySQL with a separate database for each county, Redis, MinIO for documents\n"
     "- Security: two-factor login with an e-mail OTP\n"
     "- Other: SMTP e-mail, PDF claiming reports"),
]

# ---------------------------------------------------------------------------
# Sheet 2: Security Assessment
# ---------------------------------------------------------------------------

DP = "Data Protection Policy (IIS-POL-DP-01)"
IR = "Incident Response Plan (IIS-POL-IR-01)"
DT = "Data Transmission Policy (IIS-POL-DT-01)"
PR = "Data Privacy Policy (IIS-POL-PR-01)"
DOC_CONTROL = ("The document control table at the start of the {0} shows its ID, version, owner, approval, effective date, "
               "review date and revision history.")
ENCRYPTION = ("Data in transit is encrypted with TLS 1.3 using SSL certificates. At rest, important fields are encrypted at "
              "application level. Department users in the KEONICS Portal sign with a digital signature (DSC).")
AUDIT = "Will be submitted with the audit report."

SECURITY_ITEMS = [
    dict(aspect="Security practices implemented like data protection policy, incident response plans, data transmission and data privacy policy",
         detail="Information on the standard practices and policies which are followed by the entity is required. Previous project "
                "information can be provided and can be generic in nature which will help analyze the extant process.",
         response="Our security policies are attached:\n"
                  f"- {DP}\n- {IR}\n- {DT}\n- {PR}\n"
                  "In the applications we have built, we follow these practices:\n"
                  "- Role-based access control\n"
                  "- Passwords stored as bcrypt hashes\n"
                  "- An audit trail of logins and data changes, with passwords, OTPs and tokens kept out of the audit records\n"
                  "- OTP-based login for citizens and a CAPTCHA on staff login\n"
                  "- Every code change reviewed through a pull request",
         policy=[("Data protection policy", [
                     ("Scope & purpose", f"Covered in sections 1 to 3 of the {DP}."),
                     ("Data classification schema", f"Section 4 of the {DP} classifies data as Public, Internal, Confidential or Restricted."),
                     ("Roles & responsibilities (RACI matrix)", f"Section 5 of the {DP}."),
                     ("Access control (RBAC, MFA)",
                      "All our applications use role-based access control, with roles, permissions and a mapping between them. "
                      "IEBA V2 also offers two-factor login with an e-mail OTP. Citizens log in with a mobile OTP."),
                     ("Encryption requirements (AES 256 at rest, TLS 1.3 in transit)", ENCRYPTION),
                     ("Awareness and training records", f"The training requirement is in section 10 of the {DP}.\nTraining records: {NA}"),
                     ("Document control of policy", DOC_CONTROL.format(DP))]),
                 ("Incident response plan", [
                     ("Incident response team, responsibilities of each team member, escalation matrix", f"Covered in sections 4 and 6 of the {IR}."),
                     ("Incident classification & severity", f"Section 5 of the {IR} sets four severity levels, S1 to S4, each with its own response time."),
                     ("Detection and reporting of incident", f"Section 7 of the {IR}. It includes reporting to CERT-In within 6 hours."),
                     ("SOP", f"Section 8 of the {IR}."),
                     ("Training and awareness records", f"The training requirement is in section 10 of the {IR}.\nTraining records: {NA}"),
                     ("Document control of policy", DOC_CONTROL.format(IR))]),
                 ("Data transmission", [
                     ("Scope and purpose", f"Covered in sections 1 and 2 of the {DT}."),
                     ("Encryption standards (AES 256 at rest, TLS 1.3 in transit etc.)", ENCRYPTION),
                     ("Training and awareness records", f"The training requirement is in section 6 of the {DT}.\nTraining records: {NA}"),
                     ("Document control of policy", DOC_CONTROL.format(DT))]),
                 ("Data privacy policy", [
                     ("Scope and purpose", f"Covered in sections 1 to 3 of the {PR}."),
                     ("Data collection (what data is collected and why)", f"Section 4 of the {PR}."),
                     ("Transparency & communication (available and understandable)", f"Section 5 of the {PR}."),
                     ("Third party / vendor contracts specifying privacy compliance", f"Section 7 of the {PR}.\nSigned vendor contracts: {NA}"),
                     ("Training and awareness records", f"The training requirement is in section 12 of the {PR}.\nTraining records: {NA}"),
                     ("Document control of policy", DOC_CONTROL.format(PR))])],
         evidence=[("Screenshot of tool / channel used for implementation of incident response plan", NA),
                   ("Training / awareness records (screenshots, attendance sheets)", NA),
                   ("Incident logs", NA)]),
    dict(aspect="Application/cloud security assessment based on the deployment architecture",
         detail="ASST/CSST reports are required for each solution and each instance. ASST report is for on-premise implementation. "
                "CSST report is for cloud implementation.",
         response="Every application is audited by an agency empanelled with CERT-In and C-DAC. We will submit the audit report "
                  "and safe-to-host certificate for each application.",
         policy=[("ASST / CSST report", [
                     ("Report summary (highlights)", AUDIT),
                     ("Scope (what was tested and in which environment)", AUDIT),
                     ("Methodology (testing approach, tools used)", AUDIT),
                     ("Findings / vulnerabilities (POC, likelihood and impact on business)", AUDIT),
                     ("Revalidation (if any)", AUDIT),
                     ("Safe to host certificate with validity and traceability in report", AUDIT)])],
         evidence=[("ILD declaration and timeline for submission (if pending)", "Will be submitted.")]),
    dict(aspect="Data dictionary/Data model",
         detail="Information on how the end-to-end process is taking place in the current projects which are implemented by the "
                "organization, along with the information for the current project. Information on data architecture, data "
                "storage, data retrieval etc. are required.",
         response="Each application uses a MySQL relational database.\n"
                  "- The schema is kept as entity models in the source code (TypeORM or JPA), along with version-controlled "
                  "database scripts. The Examination Portal, for example, has 33 Flyway migration scripts.\n"
                  "- Documents and photographs are stored in MinIO object storage, and Redis handles cache and sessions.\n"
                  "- Data is read and written only through authenticated REST APIs.\n"
                  "A data dictionary and an entity relationship diagram are available.",
         policy=[("Data dictionary and data model", [
                     ("General structure of data dictionary", "Available"),
                     ("Entity relationship diagram", "Available"),
                     ("Data model",
                      "Kept as entity models in the source code. For example, the Examination Portal has about 46 tables, the "
                      "RTI Portal about 25 and the BDA Grievance Portal about 54. A separate data model document is available.")])],
         evidence=[("Data dictionary (all fields, data types, validation rules)", "Available"),
                   ("Data model representing the relationship between data elements", "Available"),
                   ("Data dictionary and data model in a readable format, with matching tables", "Available"),
                   ("ILD declaration with timeline for submission (if submitted after development)",
                    "Not required, as the data dictionary and data model are already available.")]),
    dict(aspect="User Access Management Policies",
         detail="All user-specific information is to be made available, for example password acceptance, nomenclature and "
                "regeneration / renewal of passwords. Validity of password to be made available. Periodic review of all users "
                "who have access to the application is required.",
         response=f"User access management is covered in sections 5 and 6 of our {DP}, which is attached. In our applications:\n"
                  "- An administrator creates each user account and links it to a post and a role.\n"
                  "- Access is removed by deactivating the account or unmapping the post.\n"
                  "- Passwords are stored as bcrypt hashes.\n"
                  "- Password complexity, account lockout and session timeouts are enforced (details below).\n"
                  f"Password validity (expiry) and periodic user access review: {NA}",
         policy=[("User access management policy", [
                     ("Policy scope & objective", f"Covered in sections 1, 2 and 6 of the {DP}."),
                     ("User provisioning (RBAC aligned to job responsibilities) and de-provisioning (removal or deactivation process)",
                      "The administrator creates the person and the post, then maps the person to the post, which grants the "
                      "role. To remove access, the administrator deactivates the account or ends the post mapping. This applies "
                      "to the BDA Grievance, RTI, Examination and CDRMS applications."),
                     ("Access rights & roles, SOD matrix",
                      "Each application has its own roles and permissions, for example Super Admin, Examination Administrator, "
                      f"Centre Admin, Invigilator and Candidate.\nSOD matrix: {NA}"),
                     ("Authentication & password management (password policy, MFA, session timeout)",
                      "- Passwords of 10 to 16 characters, with upper case, lower case, a digit and a special character\n"
                      "- Account locked for 30 minutes after 5 failed attempts\n"
                      "- 15-minute login token with an 8-hour refresh (Examination Portal)\n"
                      "- Configurable idle timeout of 30 to 120 minutes in our other applications\n"
                      "- Two-factor login with an e-mail OTP (IEBA V2)"),
                     ("User activity logging (alerts generated for suspicious activity or privilege escalation)",
                      "The Examination Portal keeps an audit trail of logins, access denials and data changes, with the IP "
                      "address and browser details. IEBA V2 keeps a field-level history of who changed what and when.\n"
                      f"Alerts: {NA}"),
                     ("Privileged access control", f"The Super Admin role is limited to designated users.\nPAM tool: {NA}"),
                     ("Third-party / vendor access provisions",
                      f"Not applicable. We do not give vendors or third parties access to our systems or client applications (section 6 of the {DP})."),
                     ("Roles and responsibilities defined for access management", f"Section 5 of the {DP}, which includes a RACI matrix."),
                     ("Document control", DOC_CONTROL.format(DP))])],
         evidence=[("New user onboarding", "Available (screenshot of user creation and role assignment)"),
                   ("User deprovisioning", "Available (screenshot of user deactivation)"),
                   ("Privilege access review", NA),
                   ("Third-party user access review", "Not applicable. Vendors and third parties do not have access to our systems or client applications."),
                   ("Password policy settings (screenshots from AD / IAM tool)", "Available (Examination Portal password and lockout settings)"),
                   ("Password change / forgot password screen", "Available (screenshots)"),
                   ("Reminder for password expiry / password change notification evidence", NA)]),
    dict(aspect="Data storage and handling policies for customer data",
         detail="Policy regarding data backup, storage, archival and purging is required, with evidence that the policies are "
                "followed by the organisation, for example logs, screenshots and backup reports for each policy.",
         response="- Structured data is stored in MySQL, documents and images in MinIO object storage, and cache and session data in Redis.\n"
                  "- Access to data is role-based.\n"
                  "- Backups are taken daily and kept for 30 days.\n"
                  "- Most production systems are hosted at the Karnataka State Data Centre (KSDC), which provides backup systems and DR sites.\n"
                  f"Storage, retention and disposal are covered in sections 4, 7 and 9 of our {DP}, which is attached.\n"
                  f"Archival and purging SOP: {NA}",
         policy=[("Data storage policy", [
                     ("Storage locations & security (approved storage, authorised locations, additional security for sensitive data)",
                      "Data is held in MySQL, MinIO and Redis on the application servers.\n"
                      "**Production:** KSDC for government projects, the KEONICS office server for the KEONICS Portal, and the "
                      "client's servers for IEBA V2.\n"
                      "**UAT:** our own servers."),
                     ("Encryption: AES 256 for stored data, TLS 1.3 for data transfers",
                      "Data transfers use TLS 1.3 with SSL certificates. Important stored fields are encrypted at application "
                      "level. Department users in the KEONICS Portal sign with a digital signature (DSC)."),
                     ("Access & permissions: Role Based Access Control (RBAC)", "In place in all our applications."),
                     ("Access & permissions: Segregation of Duties (SOD) and access only on approval", NA),
                     ("Backups: schedule, frequency, type & method, storage & retention, backup logs",
                      f"Backups are taken daily and kept for 30 days. Production systems at KSDC are also covered by KSDC's "
                      f"backup systems and DR sites. See section 9 of the {DP}."),
                     ("Data retention & disposal", f"Section 9 of the {DP}."),
                     ("RACI matrix", f"Section 5 of the {DP}.")]),
                 ("Data archival policy", [
                     ("Data classification", f"Section 4 of the {DP} classifies data as Public, Internal, Confidential or Restricted."),
                     ("Archival process (retention period / storage location)", NA)]),
                 ("Data purging policy", [
                     ("Data classification & retention", f"Sections 4 and 9 of the {DP}."),
                     ("Purging methods", f"Section 9 of the {DP}. Data is securely deleted, and media that cannot be wiped are physically destroyed."),
                     ("SOP (review, approval, deletion; logged and verified by IT / Security team)", NA),
                     ("Disposal certificates (physical media)", NA)])],
         evidence=[("Backup logs", NA),
                   ("Evidence of backup folder on server with backup timestamp", NA),
                   ("DR test reports",
                    "Not applicable. Production is hosted at KSDC, which maintains backup systems and DR sites, and our clients "
                    "have not asked for a separate DR test."),
                   ("Retention screenshots", NA),
                   ("Archival logs", NA),
                   ("Purging certificates (if physical media destroyed)", NA)]),
    dict(aspect="Application Security, Code Review (from Cert-In empaneled auditor)",
         detail="Reports / certificates to be provided.",
         response="All our applications are audited by an agency empanelled with CERT-In and C-DAC. Depending on the application, "
                  "the audit covers source code review, application security testing (VAPT) or both. The Examination Portal was "
                  "audited with grey-box testing. We will submit the reports and safe-to-host certificates.",
         policy=[("Security audit, SCR", [
                     ("Report summary (highlights)", AUDIT),
                     ("Scope (what was tested and in which environment)", AUDIT),
                     ("Methodology (testing approach, tools used)", AUDIT),
                     ("Findings / vulnerabilities (POC, likelihood and impact on business)", AUDIT),
                     ("Revalidation (if any)", AUDIT),
                     ("Safe to host certificate with validity and traceability in report", AUDIT)])],
         evidence=[("ILD declaration and timeline for submission (if pending)", "Will be submitted.")]),
    dict(aspect="Security measures implemented (with evidence) to prevent any unauthorized attack such as WAF, DDoS.",
         detail="Information on the standard practices and policies which are followed by the entity is required. Previous project "
                "information can be provided and can be generic in nature which will help analyze the extant process.",
         response="For production applications, WAF and DDoS protection is provided by the hosting data centre (KSDC or the "
                  "client's data centre). Within the applications we also have:\n"
                  "- Request rate limiting (CAS, KEONICS Portal, BDA Grievance Portal)\n"
                  "- A CAPTCHA on staff login\n"
                  "- Secure HTTP headers\n"
                  "- An IP allow-list for examination workstations (Examination Portal)",
         policy=[("WAF and DDoS", [("Policy defined for WAF and DDoS implementation and evidence",
                                    "WAF and DDoS protection is provided by the hosting data centre (KSDC or the client's data "
                                    f"centre) under its own policy.\nEvidence: {NA}")])],
         evidence=[("Screenshot of WAF in blocking mode with timestamp", NA),
                   ("Screenshot showing DDoS protection dashboards", NA),
                   ("Inbound traffic logs", NA)]),
    dict(aspect="Data encryption standards, encoding, digital certificates and algorithms being used for integrations and authorizations",
         detail="",
         response="- Login tokens (JWT) are signed with HMAC-SHA256.\n"
                  "- Passwords are stored as bcrypt hashes.\n"
                  "- OTPs and session tokens are stored as SHA-256 hashes (Examination Portal).\n"
                  "- Digital signature (DSC) validation and signing are built into the KEONICS Portal and CAS.\n"
                  "- Data in transit is encrypted with TLS 1.3 using SSL certificates.",
         policy=[("Encryption standard", [
                     ("Integration: TLS 1.3", "TLS 1.3 with SSL certificates."),
                     ("Authorization: SHA-256", "Login tokens (JWT) are signed with HMAC-SHA256."),
                     ("Validity of digital certificate of 1 year or less", "Yes. Our SSL certificates are valid for one year and are renewed every three months."),
                     ("Data encryption standards at application level, encoding at API level, digital certificates and algorithms "
                      "used for integrations and authorizations",
                      "- Passwords: bcrypt\n"
                      "- OTPs and session tokens: SHA-256 hashes (Examination Portal)\n"
                      "- Production configuration file: AES-256-CBC (KEONICS Portal)\n"
                      "- SMS gateway request key: SHA-512 (BDA Grievance Portal)\n"
                      "- Digital signature (DSC) integration: KEONICS Portal and CAS")])],
         evidence=[("Encryption (TLS 1.3)", NA),
                   ("Encryption done at application level, data encryption", NA),
                   ("Signature algorithm (SHA 256)", NA),
                   ("API-level encryption screenshots", NA)]),
]

# ---------------------------------------------------------------------------
# Word helpers
# ---------------------------------------------------------------------------


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def repeat_header(row):
    tr_pr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    tr_pr.append(el)


def write_cell(cell, text, bold=False, color=None, italic=False, align=None):
    cell.text = ""
    lines = str(text).split("\n")
    for i, line in enumerate(lines):
        p = cell.paragraphs[0] if i == 0 else cell.add_paragraph()
        pf = p.paragraph_format
        pf.space_after = Pt(0 if i == len(lines) - 1 else 3)
        pf.line_spacing = 1.1
        if align:
            p.alignment = align
        if line.startswith("- "):
            line = line[2:]
            pf.left_indent = Cm(0.4)
            pf.first_line_indent = Cm(-0.3)
            p.add_run("•  ")
        for j, part in enumerate(re.split(r"\*\*(.+?)\*\*", line)):
            if not part:
                continue
            run = p.add_run(part)
            run.bold = bold or j % 2 == 1
            run.italic = italic
            if color:
                run.font.color.rgb = RGBColor.from_string(color)


def table(doc, headers, rows, widths, group_rows=()):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        write_cell(c, h, bold=True, color="FFFFFF")
        shade(c, NAVY)
    repeat_header(t.rows[0])
    for r_i, values in enumerate(rows):
        cells = t.add_row().cells
        if r_i in group_rows:
            merged = cells[0].merge(cells[-1])
            write_cell(merged, values[0], bold=True)
            shade(merged, LIGHT)
            continue
        for i, v in enumerate(values):
            centre = i == 0 and headers[0] == "Sl. No."
            write_cell(cells[i], str(v), align=WD_ALIGN_PARAGRAPH.CENTER if centre else None)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def base_document(title):
    doc = Document()
    zoom = doc.settings.element.find(qn("w:zoom"))
    if zoom is not None:
        zoom.set(qn("w:percent"), "100")
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    for side in ("left_margin", "right_margin"):
        setattr(sec, side, Cm(2))
    sec.top_margin = sec.bottom_margin = Cm(2)
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    for name, size in (("Heading 1", 14), ("Heading 2", 12)):
        st = doc.styles[name]
        st.font.name = "Calibri"
        st.font.size = Pt(size)
        st.font.color.rgb = RGBColor.from_string(NAVY)

    footer = sec.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.add_run(f"{VENDOR} | HDFC Vendor Onboarding | Page ").font.size = Pt(8)
    run = footer.add_run()
    run.font.size = Pt(8)
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            fld = OxmlElement("w:fldChar")
            fld.set(qn("w:fldCharType"), tag)
            run._r.append(fld)
        else:
            instr = OxmlElement("w:instrText")
            instr.set(qn("xml:space"), "preserve")
            instr.text = text
            run._r.append(instr)

    h = doc.add_paragraph()
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = h.add_run(title)
    r.bold = True
    r.font.size = Pt(18)
    r.font.color.rgb = RGBColor.from_string(NAVY)
    table(doc, ["Item", "Details"],
          [("Vendor name", VENDOR), ("Registered address", ADDRESS), ("Prepared for", "HDFC Bank"), ("Date", DATE)],
          [5, 12])
    doc.add_paragraph("Where information was not available at the time of preparing this document, the response is marked "
                      "“No answer”.")
    return doc


def status(answers):
    if all(a == NA for a in answers):
        return "No answer"
    return "Partly answered" if any(NA in a for a in answers) else "Answered"


def signature(doc):
    doc.add_heading("Declaration", level=1)
    doc.add_paragraph("The information given in this document is true to the best of our knowledge.")
    table(doc, ["Item", "Details"],
          [("Name of authorised signatory", ""), ("Designation", ""), ("Signature and company stamp", ""), ("Date", "")],
          [6, 11])


# ---------------------------------------------------------------------------
# Documents
# ---------------------------------------------------------------------------


def build_vendor():
    doc = base_document("HDFC Vendor Onboarding: Vendor Assessment")
    doc.add_heading("1. Summary", level=1)
    table(doc, ["Sl. No.", "Vendor Evaluation Checklist", "Sub-questions", "Documents required"],
          [(n, it["item"], status([a for _, a in it["subs"]]), status([a for _, a in it["docs"]]))
           for n, it in enumerate(VENDOR_ITEMS, 1)],
          [1.5, 8.5, 3.5, 3.5])

    doc.add_heading("2. Detailed Responses", level=1)
    for n, it in enumerate(VENDOR_ITEMS, 1):
        doc.add_heading(f"{n}. {it['item']}", level=2)
        table(doc, ["Sl. No.", "Sub-questions", "Response"],
              [(i, q, a) for i, (q, a) in enumerate(it["subs"], 1)], [1.5, 5.5, 10])
        if it.get("projects"):
            gov = [p for p in PROJECTS if p[2] == "Government"]
            non = [p for p in PROJECTS if p[2] != "Government"]
            rows, groups, k = [], [], 0
            for label, group in (("a. Government sector", gov), ("b. Non-Government sector", non)):
                groups.append(len(rows))
                rows.append((label,))
                for name, client, _, scope, dur, state in group:
                    k += 1
                    rows.append((k, name, client, scope, dur, state))
            table(doc, ["Sl. No.", "Name of project", "Client", "Scope", "Duration", "Status"], rows,
                  [1.2, 3.2, 3.0, 5.2, 2.2, 2.2],
                  group_rows=set(groups))
        if it.get("tech"):
            rows, groups, k = [], [], 0
            for label, sector in (("a. Government sector", "Government"), ("b. Non-Government sector", "Non-Government")):
                groups.append(len(rows))
                rows.append((label,))
                for name, sec, dept, scope, tech in TECHNO:
                    if sec == sector:
                        k += 1
                        rows.append((k, name, dept, scope, tech))
            table(doc, ["Sl. No.", "Name of project", "Department", "Scope of work", "Technical implementation"], rows,
                  [1.2, 2.8, 3.2, 4.6, 5.2],
                  group_rows=set(groups))
        table(doc, ["Sl. No.", "Documents required", "Response"],
              [(i, d, a) for i, (d, a) in enumerate(it["docs"], 1)], [1.5, 9.5, 6])
        if it.get("note"):
            p = doc.add_paragraph()
            r = p.add_run("Note: " + it["note"])
            r.italic = True
    signature(doc)
    path = OUT / "HDFC_Vendor_Assessment_Response.docx"
    doc.save(path)
    return path


def build_security():
    doc = base_document("HDFC Vendor Onboarding: Security Assessment")
    doc.add_heading("1. Summary", level=1)
    table(doc, ["Sl. No.", "Security Aspect Required for Assessment", "Policy points", "Evidences"],
          [(n, it["aspect"], status([a for _, pts in it["policy"] for _, a in pts]), status([a for _, a in it["evidence"]]))
           for n, it in enumerate(SECURITY_ITEMS, 1)],
          [1.5, 9.5, 3, 3])

    doc.add_heading("2. Detailed Responses", level=1)
    for n, it in enumerate(SECURITY_ITEMS, 1):
        doc.add_heading(f"{n}. {it['aspect']}", level=2)
        table(doc, ["Item", "Details"],
              [("Detail information", it["detail"] or "No further detail given in the checklist."), ("Response", it["response"])], [4, 13])
        rows, groups, k = [], [], 0
        for group, pts in it["policy"]:
            if len(it["policy"]) > 1:
                groups.append(len(rows))
                rows.append((group,))
            for point, ans in pts:
                k += 1
                rows.append((k, point, ans))
        table(doc, ["Sl. No.", "Policy points", "Response"], rows, [1.5, 7, 8.5], group_rows=set(groups))
        table(doc, ["Sl. No.", "Evidences", "Response"],
              [(i, e, a) for i, (e, a) in enumerate(it["evidence"], 1)], [1.5, 9.5, 6])
    signature(doc)
    path = OUT / "HDFC_Security_Assessment_Response.docx"
    doc.save(path)
    return path


if __name__ == "__main__":
    for p in (build_vendor(), build_security()):
        print("wrote", p.relative_to(OUT.parent.parent))
