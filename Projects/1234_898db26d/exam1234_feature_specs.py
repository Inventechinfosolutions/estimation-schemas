"""Examination Module (project test1 / code 1234) — module and feature catalogue."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class FeatureDef:
    seq: int
    name: str
    description: str
    objective: str
    notes: str
    actors: str
    journey: List[str]
    capabilities: List[str]
    inputs: str
    outputs: str
    rules: List[str]
    validations: List[str]
    calculations: str
    workflow: str
    search: str
    documents: str
    reports: str
    notifications: str
    security: str
    integrations: str
    dependencies: str
    assumptions: List[str]
    risks: str
    nfr: str
    ui: List[Tuple[str, str]]
    api: List[Tuple[str, str]]
    db: List[Tuple[str, str]]
    integration: List[Tuple[str, str]]
    testing: str
    documentation: str


@dataclass(frozen=True)
class ModuleDef:
    nn: int
    name: str
    module_type: str
    summary: str
    features: List[FeatureDef]


def _j(applicant: str, create: str, edit: str, approval: str) -> List[str]:
    if approval:
        return [
            f"{applicant} initiates the activity through the relevant portal screen.",
            create,
            edit,
            "Submission for verification or approval applies only where the source SOW requires administrator review; otherwise the candidate completes self-service steps without an approver inbox.",
            "Where registration verification applies, the Examination Administrator reviews pending registrations from an administrator worklist; otherwise this step does not apply.",
            "The approver accepts or returns the registration with remarks when verification is in scope; pure self-service steps have no approver decision.",
            f"{applicant} views status, history and downloadable outputs from their login.",
            "Administrators and auditors review the same history through role-scoped registers and audit views.",
        ]
    return [
        f"{applicant} initiates the activity through the relevant portal screen.",
        create,
        edit,
        "No separate approval workflow applies; the action completes on successful validation.",
        "There is no approver inbox for this feature.",
        "There is no approver decision step.",
        f"{applicant} views outcomes and history from their login.",
        "Administrators and auditors review activity through audit and operational registers.",
    ]


def _f(
    seq: int,
    name: str,
    desc: str,
    objective: str,
    notes: str,
    *,
    actors: str,
    journey: List[str],
    caps: List[str],
    ui: List[Tuple[str, str]],
    api: List[Tuple[str, str]],
    db: List[Tuple[str, str]],
    integration: List[Tuple[str, str]] | None = None,
    testing: str = "Complex",
    documentation: str = "Medium",
    rules: List[str] | None = None,
    deps: str = "Prior modules as applicable.",
    integrations_text: str = "None unless stated in feature integrations row.",
) -> FeatureDef:
    return FeatureDef(
        seq=seq,
        name=name,
        description=desc,
        objective=objective,
        notes=notes,
        actors=actors,
        journey=journey,
        capabilities=caps,
        inputs="Values captured on the named screens and through integrated channels per the SOW.",
        outputs="Persisted records, status updates, downloadable artefacts and notifications as applicable.",
        rules=rules or ["Behaviour must align with the Examination Module business rules in the source SOW."],
        validations=["Mandatory fields, eligibility checks and role-scoped access enforced before commit."],
        calculations="As per configured fee, scoring or allocation rules where applicable; otherwise none.",
        workflow="Draft or in-progress → validated → completed (and verified where required).",
        search="List and filter on registers where a search register is named in UI screens.",
        documents="Upload and download of prescribed templates and evidence where the SOW requires.",
        reports="Operational extracts only where this feature owns a report named in the SOW.",
        notifications="Triggered through Module 11 when the business event requires candidate or staff notification.",
        security="Role-based access, session controls and audit logging for critical actions.",
        integrations=integrations_text,
        dependencies=deps,
        assumptions=["KGID, payment and notification channels are available in target environments when referenced."],
        risks="Integration or centre-enforcement mechanism changes may affect delivery effort.",
        nfr="Availability during examination windows; responsive conduct under concurrent candidates at centres.",
        ui=ui,
        api=api,
        db=db,
        integration=integration or [],
        testing=testing,
        documentation=documentation,
    )


def build_modules() -> List[ModuleDef]:
    m01 = ModuleDef(
        1,
        "User and Role Management",
        "Shared",
        "Manage examination administrators, centre or invigilator users, roles and permissions.",
        [
            _f(
                1,
                "Internal User Lifecycle",
                "Create and maintain staff and centre user accounts used by administration and centre operations.",
                "Ensure only authorised personnel operate examination administration and centre functions.",
                "User register and onboarding for admin and centre roles",
                actors="Examination Administrator; IT support (as configured)",
                journey=_j(
                    "Examination Administrator",
                    "Administrator opens the user register and creates a user with role assignment.",
                    "Administrator updates user details, activation status and role mapping until deactivation.",
                    False,
                ),
                caps=["User register with search", "Create and edit user profile", "Activate and deactivate users"],
                ui=[("User register and search screen", "Complex"), ("User create and edit form", "Medium")],
                api=[
                    ("Search and list users", "Medium"),
                    ("Create and update user", "Complex"),
                    ("Activate and deactivate user", "Easy"),
                ],
                db=[("User identity and role linkage persistence", "Medium")],
                testing="Complex",
            ),
            _f(
                2,
                "Role and Permission Matrix",
                "Define roles for Examination Administrator, Centre or Invigilator user and map functional permissions.",
                "Enforce segregation between candidate, centre and administrator capabilities.",
                "Role-to-permission mapping for examination operations",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator opens the role matrix and defines permissions per examination function.",
                    "Administrator adjusts permissions when policy changes.",
                    False,
                ),
                caps=["Role catalogue", "Permission matrix by function", "Assign roles to users"],
                ui=[("Role permission matrix screen", "Complex"), ("Role assignment screen", "Medium")],
                api=[
                    ("List roles and permissions", "Medium"),
                    ("Update role permissions", "Complex"),
                    ("Resolve effective permissions for session", "Medium"),
                ],
                db=[("Role and permission persistence", "Easy")],
            ),
            _f(
                3,
                "Staff Session and Access Control",
                "Secure login, session timeout and logout for administrator and centre channels.",
                "Protect administrative and centre interfaces from unauthorised access.",
                "Staff authentication and session handling",
                actors="Examination Administrator; Centre or Invigilator user",
                journey=_j(
                    "Staff user",
                    "User authenticates on the staff login screen.",
                    "Session expires on idle timeout; user re-authenticates.",
                    False,
                ),
                caps=["Staff login", "Session timeout", "Secure logout"],
                ui=[("Staff login screen", "Medium"), ("Session expired notice screen", "Simple")],
                api=[
                    ("Authenticate staff user", "Complex"),
                    ("Validate session and logout", "Medium"),
                ],
                db=[("Staff session metadata", "Easy")],
            ),
        ],
    )

    m02 = ModuleDef(
        2,
        "Examination Configuration",
        "Business",
        "Configure examinations, registration windows, fee rules, evaluation rules and examination parameters.",
        [
            _f(
                1,
                "Examination Catalogue and Registration Windows",
                "Maintain examinations open for registration with schedules and descriptive details.",
                "Control which examinations candidates may register for.",
                "Exam catalogue and open registration control",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator creates an examination record and sets registration open and close dates.",
                    "Administrator updates examination details or closes registration.",
                    False,
                ),
                caps=["Examination register", "Examination definition form", "Registration window control"],
                ui=[("Examination register screen", "Complex"), ("Examination definition form", "Complex")],
                api=[
                    ("Search examinations", "Medium"),
                    ("Save examination definition", "Complex"),
                    ("Publish registration window", "Medium"),
                ],
                db=[("Examination master persistence", "Medium")],
            ),
            _f(
                2,
                "Fee Rules and Attempt Eligibility",
                "Configure first-attempt free rules for government employees, subsequent attempt fees and mandatory fees for other categories.",
                "Determine applicable registration fees from attempt history and category.",
                "Fee and attempt eligibility configuration",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator configures fee rules by candidate category and attempt number.",
                    "Administrator revises fee amounts or eligibility rules.",
                    False,
                ),
                caps=["Fee rule configuration", "Attempt history linkage for government employees"],
                ui=[("Fee rule configuration screen", "Complex"), ("Attempt eligibility preview screen", "Medium")],
                api=[
                    ("Save fee rules", "Complex"),
                    ("Evaluate fee applicability for candidate", "Complex"),
                ],
                db=[("Fee rule and attempt history persistence", "Medium")],
            ),
            _f(
                3,
                "Evaluation Rules and Examination Parameters",
                "Configure scoring, negative marking, pass criteria, duration, security options and paper parameters.",
                "Drive automatic evaluation and secure conduct settings.",
                "Evaluation and conduct parameter setup",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator sets evaluation rules and examination duration and security parameters per exam.",
                    "Administrator updates parameters before a scheduled session.",
                    False,
                ),
                caps=["Evaluation rule setup", "Examination conduct parameters", "Version and randomisation flags"],
                ui=[("Evaluation rules form", "Complex"), ("Examination parameters form", "Complex")],
                api=[
                    ("Save evaluation configuration", "Complex"),
                    ("Save conduct and security parameters", "Complex"),
                ],
                db=[("Examination configuration persistence", "Medium")],
            ),
        ],
    )

    m03 = ModuleDef(
        3,
        "Candidate Access and Registration",
        "Business",
        "OTP-based candidate login and end-to-end registration for government and other organisation candidates.",
        [
            _f(
                1,
                "OTP-Based Candidate Login",
                "Candidates access the portal using mobile OTP with expiry, retry limits and session timeout.",
                "Provide secure candidate access without passwords.",
                "Mobile OTP login for candidates",
                actors="Candidate",
                journey=_j(
                    "Candidate",
                    "Candidate enters mobile number and requests OTP.",
                    "Candidate may request resend within configured limits.",
                    False,
                ),
                caps=["Mobile number entry", "OTP entry and validation", "Failed attempt tracking"],
                ui=[("Candidate mobile entry screen", "Easy"), ("OTP verification screen", "Medium")],
                api=[
                    ("Send OTP", "Medium"),
                    ("Verify OTP and establish session", "Complex"),
                ],
                db=[("OTP attempt and session persistence", "Medium")],
                integration=[("SMS OTP dispatch channel", "Easy")],
                integrations_text="SMS channel via Module 11 notification service.",
            ),
            _f(
                2,
                "Government Employee Registration with KGID",
                "Government department employees register using mandatory KGID with retrieved employee details and confirmation.",
                "Reduce manual data entry and validate government employment.",
                "KGID-driven government employee registration",
                actors="Candidate; Examination Administrator (verification if required)",
                journey=_j(
                    "Government employee candidate",
                    "Candidate selects government employee registration and enters KGID.",
                    "Candidate confirms retrieved details and completes additional fields.",
                    True,
                ),
                caps=["KGID entry", "Retrieved detail review", "Additional registration fields"],
                ui=[
                    ("Government registration type selection screen", "Easy"),
                    ("KGID entry and retrieved detail review screen", "Complex"),
                    ("Additional candidate detail form", "Medium"),
                ],
                api=[
                    ("Retrieve employee details by KGID", "Complex"),
                    ("Save government employee registration", "Complex"),
                ],
                db=[("Candidate registration persistence", "Medium")],
                integration=[("KGID employee lookup integration", "Medium")],
                integrations_text="KGID lookup via Module 11.",
                deps="F03-001; F11-001",
            ),
            _f(
                3,
                "Other Organisation Candidate Registration",
                "Manual capture of candidate and employment details for PSU, Board, Corporation, Society and other eligible organisations.",
                "Support non-government candidate registration with configurable fields.",
                "Manual registration for other organisation employees",
                actors="Candidate",
                journey=_j(
                    "Non-government candidate",
                    "Candidate selects organisation category and completes profile and employment details.",
                    "Candidate may edit draft registration before submission.",
                    True,
                ),
                caps=["Category selection", "Candidate and employment detail form"],
                ui=[("Organisation category selection screen", "Easy"), ("Other organisation detail form", "Complex")],
                api=[
                    ("Save other organisation registration draft", "Complex"),
                    ("Submit registration for verification", "Complex"),
                ],
                db=[("Other organisation candidate persistence", "Medium")],
            ),
            _f(
                4,
                "Competent Authority Document Handling",
                "Download prescribed competent authority format, upload digitally signed confirmation and associate with registration.",
                "Evidence employment status for non-government candidates.",
                "Competent authority template and upload",
                actors="Candidate; Examination Administrator",
                journey=_j(
                    "Non-government candidate",
                    "Candidate downloads the prescribed template and uploads the digitally signed document.",
                    "Administrator may verify or return the document from a verification worklist when required.",
                    True,
                ),
                caps=["Template download", "Document upload with format and size validation"],
                ui=[("Competent authority template download screen", "Simple"), ("Document upload screen", "Medium")],
                api=[
                    ("Download template", "Easy"),
                    ("Upload and attach competent authority document", "Complex"),
                ],
                db=[("Registration document metadata persistence", "Easy")],
            ),
            _f(
                5,
                "Examination and Centre Preference Selection",
                "Select examination and two preferred examination centres during registration.",
                "Capture preferences for downstream centre allocation.",
                "Exam and dual centre preference capture",
                actors="Candidate",
                journey=_j(
                    "Candidate",
                    "Candidate selects an open examination from the catalogue.",
                    "Candidate selects centre preference one and two from configured centres.",
                    False,
                ),
                caps=["Open examination picker", "Centre preference selection"],
                ui=[("Examination selection screen", "Medium"), ("Centre preference selection screen", "Medium")],
                api=[
                    ("List open examinations for candidate", "Medium"),
                    ("Save examination and centre preferences", "Medium"),
                ],
                db=[("Registration examination and preference persistence", "Easy")],
                deps="F02-001; F04-001",
            ),
        ],
    )

    m04 = ModuleDef(
        4,
        "Fee and Payment",
        "Business",
        "Determine applicable fees and collect payments where registration is not free.",
        [
            _f(
                1,
                "Registration Fee Determination and Payment",
                "Present applicable fee, initiate payment for paid registrations and confirm successful payment before registration completion.",
                "Collect fees per category and attempt rules.",
                "Fee presentation and payment initiation",
                actors="Candidate",
                journey=_j(
                    "Candidate",
                    "System displays applicable fee after eligibility check; candidate proceeds to payment when due.",
                    "Payment gateway callback updates registration payment status.",
                    False,
                ),
                caps=["Fee summary", "Payment initiation and return handling"],
                ui=[("Registration fee summary screen", "Medium"), ("Payment status and receipt screen", "Medium")],
                api=[
                    ("Calculate registration fee", "Complex"),
                    ("Initiate payment and record outcome", "Complex"),
                ],
                db=[("Fee transaction persistence", "Medium")],
                integration=[("Payment gateway integration", "Very High")],
                integrations_text="Payment gateway via Module 11.",
                deps="F02-002; F11-002",
            ),
            _f(
                2,
                "Payment Reconciliation Views",
                "Administrator views fee-paid, free and failed transactions for operational reconciliation.",
                "Support finance and examination administration oversight.",
                "Payment reconciliation register",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator opens the payment transaction register with filters.",
                    "Administrator exports or drills into failed transactions for follow-up.",
                    False,
                ),
                caps=["Payment transaction register", "Failed transaction filter"],
                ui=[("Payment transaction register screen", "Complex")],
                api=[("Search payment transactions", "Medium"), ("Export payment summary", "Medium")],
                db=[("Read payment and registration fee data", "Easy")],
            ),
        ],
    )

    m05 = ModuleDef(
        5,
        "Scheduling Allocation and Hall Ticket",
        "Business",
        "Schedule examinations, allocate centres and issue digital hall tickets.",
        [
            _f(
                1,
                "Examination Scheduling",
                "Plan examination dates, sessions and capacity-linked schedules.",
                "Coordinate when examinations are conducted.",
                "Examination schedule planning",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator creates schedules linked to examinations and centres.",
                    "Administrator adjusts schedules when capacity or policy changes.",
                    False,
                ),
                caps=["Schedule calendar or register", "Session definition"],
                ui=[("Examination schedule register screen", "Complex"), ("Session planning form", "Complex")],
                api=[("Save examination schedule", "Complex"), ("List schedules by examination", "Medium")],
                db=[("Examination schedule persistence", "Medium")],
            ),
            _f(
                2,
                "Centre Allocation",
                "Allocate candidates to examination centres using preferences, capacity and business rules.",
                "Assign final centre for hall ticket and conduct.",
                "Centre allocation against preferences",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator runs allocation for a schedule using preferences and capacity.",
                    "Administrator may override allocation with audit reason when permitted.",
                    False,
                ),
                caps=["Allocation run workspace", "Allocation outcome register"],
                ui=[("Centre allocation workspace screen", "Very High"), ("Allocation result register screen", "Complex")],
                api=[
                    ("Run centre allocation", "Very High"),
                    ("Manual allocation override", "Complex"),
                ],
                db=[("Candidate centre allocation persistence", "Medium")],
            ),
            _f(
                3,
                "Hall Ticket Generation",
                "Generate digital hall tickets after scheduling and allocation with candidate and centre details.",
                "Provide candidates authorised entry information.",
                "Digital hall ticket issuance",
                actors="Candidate; Examination Administrator",
                journey=_j(
                    "Candidate",
                    "Hall ticket becomes available after allocation; candidate downloads from portal.",
                    "Administrator may regenerate hall ticket when details change.",
                    False,
                ),
                caps=["Hall ticket generation", "Candidate download"],
                ui=[("Hall ticket preview and download screen", "Medium"), ("Administrator hall ticket register", "Medium")],
                api=[
                    ("Generate hall ticket", "Complex"),
                    ("Download hall ticket PDF", "Medium"),
                ],
                db=[("Hall ticket issuance persistence", "Easy")],
                deps="F05-001; F05-002",
            ),
        ],
    )

    m06 = ModuleDef(
        6,
        "Examination Centre Management and Enforcement",
        "Business",
        "Manage authorised centres, enforce centre-only access and support invigilator session activation.",
        [
            _f(
                1,
                "Examination Centre Master",
                "Maintain authorised examination centres, capacity and centre user mapping.",
                "Control where examinations may be conducted.",
                "Examination centre master data",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator creates centre records with capacity and authorised flag.",
                    "Administrator updates centre status or capacity.",
                    False,
                ),
                caps=["Centre register", "Centre profile form"],
                ui=[("Examination centre register screen", "Complex"), ("Centre profile form", "Medium")],
                api=[("Search centres", "Medium"), ("Save centre master", "Complex")],
                db=[("Examination centre persistence", "Medium")],
            ),
            _f(
                2,
                "Authorised Centre Access Enforcement",
                "Validate candidate, centre, device or network and session before examination access is granted.",
                "Prevent examination attempt outside allotted authorised centre.",
                "Centre-only access validation",
                actors="Candidate; System",
                journey=_j(
                    "Candidate at allotted centre",
                    "Candidate attempts examination login; system validates centre, schedule and authorisation rules.",
                    "Access denied with reason when validation fails.",
                    False,
                ),
                caps=["Pre-exam access validation", "Denial messaging"],
                ui=[("Examination access denied screen", "Simple"), ("Centre validation status screen", "Medium")],
                api=[
                    ("Validate authorised centre and session context", "Very High"),
                    ("Record access denial event", "Medium"),
                ],
                db=[("Centre access validation log persistence", "Medium")],
                testing="Very High",
            ),
            _f(
                3,
                "Centre Session Activation and Invigilator Controls",
                "Centre or invigilator user verifies candidate, activates examination session and monitors status.",
                "Operational control at the examination centre.",
                "Invigilator session activation",
                actors="Centre or Invigilator user; Candidate",
                journey=_j(
                    "Centre or Invigilator user",
                    "Invigilator verifies candidate identity against hall ticket and activates session.",
                    "Invigilator monitors active and submitted candidates on centre workspace.",
                    False,
                ),
                caps=["Candidate verification", "Session activation", "Live session monitor"],
                ui=[
                    ("Centre candidate verification screen", "Complex"),
                    ("Session activation screen", "Medium"),
                    ("Active session monitor screen", "Complex"),
                ],
                api=[
                    ("Verify candidate at centre", "Complex"),
                    ("Activate examination session", "Complex"),
                    ("List active sessions for centre", "Medium"),
                ],
                db=[("Centre session state persistence", "Medium")],
                deps="F06-001; F06-002",
            ),
        ],
    )

    m07 = ModuleDef(
        7,
        "Question Bank and Paper Generation",
        "Business",
        "Maintain question banks and generate randomised papers with multiple versions.",
        [
            _f(
                1,
                "Question Bank Maintenance",
                "Create and maintain questions with categories, difficulty and status for examinations.",
                "Supply content for randomised papers.",
                "Question bank administration",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator creates questions and assigns them to examination pools.",
                    "Administrator revises or deactivates questions with audit trail.",
                    False,
                ),
                caps=["Question register", "Question authoring form"],
                ui=[("Question bank register screen", "Complex"), ("Question authoring form", "Complex")],
                api=[
                    ("Search questions", "Medium"),
                    ("Save question", "Complex"),
                ],
                db=[("Question bank persistence", "Medium")],
            ),
            _f(
                2,
                "Random Paper Generation and Versions",
                "Generate examination papers with random question selection and multiple versions such as A/B/C/D.",
                "Reduce predictability and support parallel sessions.",
                "Randomised multi-version papers",
                actors="Examination Administrator; System",
                journey=_j(
                    "Examination Administrator",
                    "Administrator configures paper blueprint linked to examination.",
                    "System generates candidate-specific paper at session start.",
                    False,
                ),
                caps=["Paper blueprint configuration", "Runtime paper generation"],
                ui=[("Paper blueprint configuration screen", "Complex")],
                api=[
                    ("Save paper blueprint", "Complex"),
                    ("Generate candidate paper instance", "Very High"),
                ],
                db=[("Paper blueprint and instance persistence", "Complex")],
                testing="Very High",
            ),
            _f(
                3,
                "Question and Option Order Randomisation",
                "Randomise question order and answer option order per candidate paper.",
                "Further reduce collusion risk during CBT.",
                "Order randomisation controls",
                actors="System",
                journey=_j(
                    "System",
                    "Randomisation rules apply when paper instance is created for the candidate.",
                    "Administrators configure whether option shuffling applies per examination.",
                    False,
                ),
                caps=["Randomisation rule flags", "Shuffled delivery to examination interface"],
                ui=[("Randomisation settings screen", "Medium")],
                api=[
                    ("Apply question order randomisation", "Complex"),
                    ("Apply option order randomisation", "Complex"),
                ],
                db=[("Randomisation metadata on paper instance", "Easy")],
                deps="F07-002",
            ),
        ],
    )

    m08 = ModuleDef(
        8,
        "Computer-Based Examination Conduct",
        "Business",
        "Issue examination credentials, deliver secure CBT interface with timer, record activity and handle submission.",
        [
            _f(
                1,
                "Examination Credential Issuance and Exam Login",
                "Generate system examination credentials and authenticate candidate for the assigned session.",
                "Separate portal login from secure examination login.",
                "Examination credential lifecycle",
                actors="Candidate; System",
                journey=_j(
                    "Candidate",
                    "Credentials are issued after scheduling; candidate uses them at centre for examination login.",
                    "Credential invalid after submission or expiry.",
                    False,
                ),
                caps=["Credential generation", "Examination login screen"],
                ui=[("Examination credential display for candidate", "Easy"), ("Examination login screen", "Medium")],
                api=[
                    ("Generate examination credentials", "Complex"),
                    ("Authenticate examination login", "Complex"),
                ],
                db=[("Examination credential persistence", "Medium")],
                deps="F06-003; F05-003",
            ),
            _f(
                2,
                "Examination Interface and Timer",
                "Present questions, capture responses and enforce configured examination duration with auto-submit.",
                "Conduct timed computer-based examination.",
                "CBT delivery and timer",
                actors="Candidate",
                journey=_j(
                    "Candidate",
                    "Candidate answers questions within the timed interface.",
                    "Timer triggers auto-submit when duration elapses.",
                    False,
                ),
                caps=["Examination workspace", "Timer and auto-submit warning"],
                ui=[("Examination question workspace screen", "Very High"), ("Timer and submit confirmation dialog", "Medium")],
                api=[
                    ("Load examination paper for session", "Complex"),
                    ("Save response and heartbeat", "Complex"),
                    ("Auto-submit on timeout", "Complex"),
                ],
                db=[("Response capture persistence", "Complex")],
                testing="Very High",
            ),
            _f(
                3,
                "Examination Security Activity and Submission",
                "Record examination activity, apply security controls and process manual or automatic submission.",
                "Support audit, monitoring and integrity of conduct.",
                "Security logging and submission",
                actors="Candidate; Examination Administrator",
                journey=_j(
                    "Candidate",
                    "Candidate submits examination or system auto-submits.",
                    "Administrator monitors security events on operational views.",
                    False,
                ),
                caps=["Activity event capture", "Manual submit", "Security event register"],
                ui=[("Submit examination confirmation screen", "Simple"), ("Security event monitor screen", "Complex")],
                api=[
                    ("Record examination activity event", "Medium"),
                    ("Finalize submission", "Complex"),
                ],
                db=[("Examination activity log persistence", "Medium")],
            ),
        ],
    )

    m09 = ModuleDef(
        9,
        "Results Certificates and Verification",
        "Business",
        "Evaluate responses, publish results, generate QR-enabled certificates and provide public verification.",
        [
            _f(
                1,
                "Automatic Evaluation and Result Publication",
                "Score responses per configured rules and publish results to candidate login when allowed.",
                "Deliver timely results after submission.",
                "Evaluation and result views",
                actors="Candidate; Examination Administrator",
                journey=_j(
                    "System",
                    "Evaluation runs after submission using configured rules.",
                    "Candidate views result when publication rules allow.",
                    False,
                ),
                caps=["Evaluation engine run", "Candidate result view"],
                ui=[("Candidate result detail screen", "Medium"), ("Administrator result publication control screen", "Medium")],
                api=[
                    ("Run automatic evaluation", "Very High"),
                    ("Fetch result for candidate", "Medium"),
                ],
                db=[("Result persistence", "Medium")],
                deps="F02-003; F08-003",
            ),
            _f(
                2,
                "Certificate Generation with QR Code",
                "Generate downloadable certificates for eligible candidates embedding unique QR verification reference.",
                "Provide tamper-evident credential to successful candidates.",
                "Certificate issuance with QR",
                actors="Candidate; Examination Administrator",
                journey=_j(
                    "Candidate",
                    "Certificate becomes available after pass criteria met; candidate downloads PDF.",
                    "Administrator may revoke or cancel certificate when policy requires.",
                    False,
                ),
                caps=["Certificate template rendering", "QR embedding"],
                ui=[("Certificate download screen", "Medium"), ("Certificate administration register", "Complex")],
                api=[
                    ("Generate certificate with QR reference", "Complex"),
                    ("Download certificate", "Medium"),
                ],
                db=[("Certificate issuance persistence", "Medium")],
            ),
            _f(
                3,
                "Public Online Certificate Verification",
                "Public verification page validates certificate token from QR scan and shows approved disclosure.",
                "Allow third parties to confirm certificate genuineness.",
                "Public QR verification",
                actors="Verifier or Public user",
                journey=_j(
                    "Verifier or Public user",
                    "User scans QR code and lands on verification page.",
                    "System displays valid, invalid or revoked status.",
                    False,
                ),
                caps=["Public verification page", "Status display without over-disclosure"],
                ui=[("Public certificate verification page", "Medium")],
                api=[("Verify certificate token", "Complex")],
                db=[("Certificate verification lookup", "Easy")],
            ),
        ],
    )

    m10 = ModuleDef(
        10,
        "Dashboards Reports and Audit",
        "Business",
        "Administrator and centre dashboards, operational reports and audit trail inquiry.",
        [
            _f(
                1,
                "Administrator Dashboard",
                "Overall view of registrations, schedules, outcomes and certificate status.",
                "Support examination administration oversight.",
                "Administrator operational dashboard",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator opens dashboard for summary metrics.",
                    "Administrator drills into underlying registers where provided.",
                    False,
                ),
                caps=["Summary tiles and trends", "Drill-down links"],
                ui=[("Administrator dashboard screen", "Very High")],
                api=[("Load administrator dashboard metrics", "Complex")],
                db=[("Aggregated read models for dashboard", "Medium")],
            ),
            _f(
                2,
                "Examination Centre Dashboard",
                "Centre-specific view of today's examinations, attendance and session status.",
                "Support invigilator and centre management.",
                "Centre dashboard",
                actors="Centre or Invigilator user",
                journey=_j(
                    "Centre user",
                    "Centre user opens dashboard scoped to their centre only.",
                    "Metrics refresh for active sessions.",
                    False,
                ),
                caps=["Centre-scoped metrics", "Attendance and completion counts"],
                ui=[("Examination centre dashboard screen", "Very High")],
                api=[("Load centre dashboard metrics", "Complex")],
                db=[("Centre-scoped aggregates", "Medium")],
            ),
            _f(
                3,
                "Operational Reports and Export",
                "Candidate, fee, examination, result and certificate reports with export to Excel or PDF.",
                "Meet MIS and compliance reporting needs from the SOW.",
                "Standard report catalogue",
                actors="Examination Administrator",
                journey=_j(
                    "Examination Administrator",
                    "Administrator selects report and parameters.",
                    "Administrator exports output in approved format.",
                    False,
                ),
                caps=["Report parameter screen", "Report output and export"],
                ui=[("Report catalogue and parameter screen", "Complex"), ("Report preview and export screen", "Medium")],
                api=[
                    ("Run report query", "Complex"),
                    ("Export report file", "Medium"),
                ],
                db=[("Report query against operational data", "Medium")],
            ),
            _f(
                4,
                "Audit Trail Inquiry",
                "Capture and inquire audit logs for critical activities listed in the SOW.",
                "Support compliance and forensic review.",
                "Audit log inquiry",
                actors="Examination Administrator; Auditor",
                journey=_j(
                    "Auditor",
                    "Auditor searches audit log by user, activity and date range.",
                    "Auditor exports audit extract when permitted.",
                    False,
                ),
                caps=["Audit log search register", "Audit detail view"],
                ui=[("Audit trail search register screen", "Complex"), ("Audit event detail screen", "Medium")],
                api=[("Search audit events", "Medium"), ("Fetch audit event detail", "Easy")],
                db=[("Audit log persistence", "Medium")],
            ),
        ],
    )

    m11 = ModuleDef(
        11,
        "Integrations and Notifications",
        "Technical",
        "KGID employee lookup, payment gateway and multi-channel notifications to candidates and staff.",
        [
            _f(
                1,
                "KGID Integration Service",
                "Integrate with KGID to retrieve government employee details during registration.",
                "Automate government employee data capture.",
                "KGID lookup integration",
                actors="System; Candidate",
                journey=_j(
                    "System",
                    "Registration invokes KGID lookup when candidate enters KGID.",
                    "Mapped fields populate registration review screen.",
                    False,
                ),
                caps=["KGID request and response mapping", "Error handling when KGID unavailable"],
                ui=[("KGID integration monitor screen for administrators", "Medium")],
                api=[
                    ("Call KGID employee lookup", "Complex"),
                    ("Map KGID response to registration model", "Complex"),
                ],
                db=[("KGID integration log persistence", "Easy")],
                integration=[("External KGID API", "Medium")],
                integrations_text="External KGID system per department interface.",
            ),
            _f(
                2,
                "Payment Gateway Integration",
                "Integrate with configured payment gateway for registration fee collection and callback handling.",
                "Enable online fee collection.",
                "Payment gateway adapter",
                actors="Candidate; System",
                journey=_j(
                    "System",
                    "Payment initiation redirects to gateway and processes return callback.",
                    "Failed payments remain retryable per business rules.",
                    False,
                ),
                caps=["Payment initiation", "Callback verification", "Reconciliation hooks"],
                ui=[("Payment gateway status monitor screen", "Medium")],
                api=[
                    ("Initiate gateway payment", "Complex"),
                    ("Process payment callback", "Very High"),
                ],
                db=[("Gateway transaction log persistence", "Medium")],
                integration=[("External payment gateway", "Very High")],
            ),
            _f(
                3,
                "Notification Delivery Service",
                "Send SMS, email and portal notifications for registration, payment, schedule, hall ticket, credentials, results and certificates.",
                "Keep candidates informed across the examination lifecycle.",
                "Multi-channel notifications",
                actors="System; Candidate",
                journey=_j(
                    "System",
                    "Business events enqueue notification templates.",
                    "Candidate receives messages on configured channels.",
                    False,
                ),
                caps=["Template configuration consumption", "Channel dispatch", "Delivery status logging"],
                ui=[("Notification template and channel configuration screen", "Complex")],
                api=[
                    ("Send notification on business event", "Complex"),
                    ("Query notification delivery status", "Medium"),
                ],
                db=[("Notification queue and log persistence", "Medium")],
                integration=[("SMS provider", "Easy"), ("Email provider", "Easy")],
                integrations_text="SMS and email providers as configured by the department.",
            ),
        ],
    )

    return [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11]
