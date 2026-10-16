"""Build draft Technology Stack Document and SDLC Policy (Word) for HDFC vendor onboarding.

Run from repo root:
    .venv/bin/python Projects/hdfc_enrollment/_build/build_engineering_docs.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_policies import OUT, approval, new_document, render, review  # noqa: E402

TECH_STACK = dict(
    file="IIS_Technology_Stack_Document.docx",
    title="Technology Stack Document",
    doc_id="IIS-STD-TS-01",
    owner="Technical Architect",
    blocks=[
        ("h", "1. Purpose"),
        ("p", "This document describes the standard technologies the Company uses to build web, mobile and backend "
              "applications, and the rules for choosing, updating and retiring them."),
        ("h", "2. Scope"),
        ("p", "It applies to every application the Company develops or maintains, for government and private clients."),
        ("h", "3. Standard technology stack"),
        ("t", ["Sl. No.", "Layer", "Standard technology", "Notes"], [
            (1, "Web frontend", "React 18 / 19 with TypeScript, built with Vite", "Single-page applications. UI libraries "
             "(for example Tailwind CSS) chosen per project."),
            (2, "Backend (primary)", "NestJS with TypeScript on Node.js LTS (20 / 22)", "Modular monolith with REST APIs."),
            (3, "Backend (Java)", "Spring Boot 3 on Java 21 LTS", "Used where the project needs Java (Examination Portal)."),
            (4, "Mobile", "React Native with Expo (TypeScript)", "Android builds (APK / AAB) through Expo EAS."),
            (5, "Database", "MySQL 8", "TypeORM for NestJS; Spring Data JPA with Flyway migrations for Java."),
            (6, "Cache and sessions", "Redis", "OTP, session and permission caching."),
            (7, "File and object storage", "MinIO (S3-compatible)", "Documents, photographs and generated reports."),
            (8, "Messaging", "RabbitMQ", "Email and notification queues where volume needs it."),
            (9, "API style", "REST over HTTPS with JSON; OpenAPI (Swagger) documentation", "API documentation is "
             "disabled in production."),
            (10, "Source control", "Git on the Company's GitHub organisation", "Private repositories only."),
            (11, "Build and deployment", "Docker containers, PM2 process manager, Jenkins pipelines", "Choice depends on "
             "the hosting environment."),
            (12, "Transport security", "TLS 1.3 at the reverse proxy or load balancer", "Provided at the hosting layer "
             "(KSDC, client or Company server)."),
        ], [1.2, 3.4, 6, 6.4]),
        ("h", "4. Technology used in current projects"),
        ("t", ["Sl. No.", "Project", "Frontend", "Backend", "Mobile", "Data and storage"], [
            (1, "KEONICS Portal", "React 18, TypeScript, Vite", "NestJS 10, Node.js 22", "–",
             "MySQL, Redis, MinIO, RabbitMQ"),
            (2, "BDA Grievance Redressal Portal", "React 19, TypeScript, Vite", "NestJS 10", "–", "MySQL 8, MinIO"),
            (3, "CA Site Allotment and Institution Registration (CAS)", "React 19, TypeScript, Vite",
             "NestJS 10, Node.js 20", "–", "MySQL, Redis, MinIO"),
            (4, "BDA RTI Management Portal", "React 19, TypeScript, Vite, Tailwind CSS", "NestJS 11", "–",
             "MySQL 8, MinIO"),
            (5, "CDRMS", "React 19, TypeScript, Vite", "NestJS 11", "React Native (Expo)", "MySQL, Redis, MinIO"),
            (6, "Examination Management Portal", "React 19, TypeScript, Vite", "Spring Boot 3.5, Java 21", "–",
             "MySQL, Redis, MinIO"),
            (7, "IEBA V2", "React 19, TypeScript, Vite", "NestJS 10", "–", "MySQL, Redis, MinIO"),
        ], [1.2, 4, 3.6, 3, 2, 3.2]),
        ("h", "5. Security components"),
        ("t", ["Sl. No.", "Area", "Standard"], [
            (1, "Authentication", "JWT access tokens signed with HMAC-SHA256, short expiry, with refresh tokens. OTP login "
             "for citizens and candidates."),
            (2, "Password storage", "bcrypt salted hashes."),
            (3, "OTP and session tokens", "Stored as SHA-256 hashes, with expiry and attempt limits."),
            (4, "Authorisation", "Role-based access control enforced on the server (guards / Spring Security)."),
            (5, "Input validation", "class-validator (NestJS) and Bean Validation (Java) on every request."),
            (6, "Database access", "ORM with parameterised queries. No string-built SQL."),
            (7, "Digital signatures", "DSC integration for signing and validation where the client process needs it."),
            (8, "Secrets", "Held in environment-specific configuration outside source code."),
        ], [1.2, 4, 11.8]),
        ("h", "6. Third-party integrations"),
        ("t", ["Sl. No.", "Service", "Used for", "Projects"], [
            (1, "Karnataka Mobile Seva SMS gateway", "OTP and status SMS", "BDA Grievance, RTI and other BDA projects"),
            (2, "PayU payment gateway", "Online fee payment", "BDA RTI"),
            (3, "Razorpay payment gateway", "Online fee payment", "CAS"),
            (4, "SMTP email", "Email notifications and OTP", "KEONICS Portal, IEBA V2 and others"),
            (5, "Digital signature (DSC)", "Document signing and validation", "KEONICS Portal, CAS"),
        ], [1.2, 5, 4.6, 6.2]),
        ("h", "7. Environments and hosting"),
        ("t", ["Sl. No.", "Environment", "Where", "Purpose"], [
            (1, "Development", "Developer machines", "Coding and unit testing. Synthetic data only."),
            (2, "UAT", "Company servers", "QA testing and client acceptance testing."),
            (3, "Production", "Karnataka State Data Centre (government projects), KEONICS office server (KEONICS "
             "Portal), client servers (IEBA V2)", "Live use."),
        ], [1.2, 3, 7.4, 5.4]),
        ("h", "8. Technology selection and version policy"),
        ("b", ["Only supported versions are used. Runtimes (Node.js, Java) must be on a long-term support (LTS) release.",
               "A new framework, library or service needs approval from the Technical Architect after checking security, "
               "licence, support and community activity.",
               "Only open-source components with permissive licences (MIT, Apache 2.0, BSD) or properly licensed commercial "
               "products are used.",
               "Dependencies are scanned for known vulnerabilities (for example npm audit or OWASP Dependency-Check) before "
               "every release.",
               "Critical security patches are applied within 7 days and high-severity patches within 30 days.",
               "Dependencies are reviewed every quarter. Components nearing end of life are replaced before that date."]),
        ("h", "9. Roles and responsibilities"),
        ("t", ["Sl. No.", "Role", "Responsibility"], [
            (1, "Technical Architect", "Owns this document, approves new technologies and sets version baselines."),
            (2, "Project Manager", "Makes sure each project follows the approved stack or records an exception."),
            (3, "Development team", "Builds with the approved stack and keeps dependencies up to date."),
            (4, "DevOps / Infrastructure team", "Maintains build and deployment tooling, runtimes and servers."),
        ], [1.2, 4.6, 11.2]),
        *review(10),
    ])

SDLC = dict(
    file="IIS_SDLC_Policy.docx",
    title="Software Development Life Cycle (SDLC) Policy",
    doc_id="IIS-POL-SDLC-01",
    owner="Head of Delivery",
    blocks=[
        ("h", "1. Purpose"),
        ("p", "This policy sets out how the Company plans, builds, tests, secures, releases and maintains software, so that "
              "every project delivers working, secure software in a repeatable way."),
        ("h", "2. Scope"),
        ("p", "It applies to every application the Company develops or maintains, and to everyone who works on them: "
              "employees and contractors."),
        ("h", "3. Development model"),
        ("p", "Projects follow an iterative model. Work is planned in sprints of two to three weeks, and each sprint ends "
              "with a working build on the UAT server. Government projects also follow the milestones in the SOW."),
        ("h", "4. SDLC phases"),
        ("t", ["Sl. No.", "Phase", "Activities", "Output", "Approved by"], [
            (1, "Requirements", "Gather requirements with the client; prepare the SOW / SRS, feature list and estimate.",
             "Signed SOW / SRS", "Client, Project Manager"),
            (2, "Design", "Architecture, data model, ER diagram and data dictionary, screen designs, roles and "
             "permissions, data classification.", "Design document, ER diagram, UI designs",
             "Technical Architect; client for UI"),
            (3, "Development", "Code to the Company's standards on feature branches; every change reviewed through a "
             "pull request.", "Reviewed code merged to the dev branch", "Technical Lead"),
            (4, "Testing", "Unit tests, functional and regression testing by QA, performance testing where needed.",
             "Test cases, test report, closed defects", "QA Lead"),
            (5, "User acceptance testing (UAT)", "Client tests on the UAT server; defects fixed and retested.",
             "UAT sign-off", "Client"),
            (6, "Security testing", "Security audit by a CERT-In empanelled auditor (VAPT, source code review or both); "
             "fixes and revalidation.", "Audit report, safe-to-host certificate", "Information Security Officer"),
            (7, "Release and deployment", "Release notes, deployment checklist, database backup before deployment, "
             "rollback plan.", "Release notes, deployment record", "Project Manager, client"),
            (8, "Maintenance and support", "Defect fixes to the agreed SLA, security patches, change requests.",
             "Support tickets, change log", "Project Manager"),
        ], [1.2, 2.6, 6.4, 3.8, 3]),
        ("h", "5. Source code management"),
        ("t", ["Sl. No.", "Branch", "Purpose"], [
            (1, "feature/*, bug/*", "One branch per feature or fix, created from dev."),
            (2, "dev", "Integration branch for the next build."),
            (3, "release/uat", "Code deployed to the UAT server."),
            (4, "main / prod", "Code deployed to production."),
        ], [1.2, 4, 11.8]),
        ("b", ["All code is kept in private repositories in the Company's GitHub organisation.",
               "Every change reaches dev, UAT and production only through a pull request reviewed by at least one person "
               "other than the author. Direct pushes to these branches are blocked.",
               "Each production release is tagged with a version number (for example v1.4.0).",
               "Repositories must never contain passwords, keys, production configuration or personal data."]),
        ("h", "6. Secure coding standards"),
        ("b", ["Code is written to avoid the OWASP Top 10 risks.",
               "Every input is validated on the server. Database access uses the ORM with parameterised queries.",
               "Every API requires authentication and role checks, except endpoints that are public by design.",
               "Error messages shown to users never include stack traces or internal details.",
               "Logs never contain passwords, OTPs, tokens or full personal identifiers.",
               "API documentation (Swagger) and debug features are disabled in production.",
               "Dependencies are scanned for known vulnerabilities before each release."]),
        ("h", "7. Testing standards"),
        ("b", ["Business logic has unit tests. The coverage target is agreed at the start of each project.",
               "QA prepares test cases from the SRS and records results in a test report.",
               "Test data is synthetic or masked. Production personal data is never used for testing.",
               "No release goes to production with open critical or high-severity defects."]),
        ("h", "8. Environments"),
        ("b", ["Development, UAT and production are kept separate, each with its own database and credentials.",
               "Only the DevOps team has access to production servers.",
               "Production data is not copied to development or UAT."]),
        ("h", "9. Change management"),
        ("b", ["Every change to agreed scope is raised as a change request, with its impact and estimate.",
               "Work on a change request starts only after the client and the Project Manager approve it.",
               "An emergency fix may be deployed first and approved within two working days. It is recorded in the change "
               "log."]),
        ("h", "10. Release and deployment"),
        ("b", ["Builds and deployments use the project's pipeline (for example Jenkins) or a documented deployment script.",
               "The database is backed up before every production deployment.",
               "Database changes are applied through versioned migration scripts.",
               "Every release has a rollback plan and a deployment record (date, version, who deployed, result).",
               "The client is told in advance about any planned downtime."]),
        ("h", "11. Documentation"),
        ("p", "Each project keeps: SOW / SRS, design document, ER diagram and data dictionary, API documentation, user "
              "manual, deployment guide, test reports and release notes."),
        ("h", "12. Roles and responsibilities"),
        ("t", ["Sl. No.", "Role", "Responsibility"], [
            (1, "Head of Delivery", "Owns this policy and checks that projects follow it."),
            (2, "Project Manager", "Plans the project, manages scope and change requests, and gets client sign-offs."),
            (3, "Technical Architect / Technical Lead", "Owns design, code review standards and technical quality."),
            (4, "Developers", "Write, test and review code as per this policy."),
            (5, "QA team", "Tests each build and reports defects."),
            (6, "DevOps / Infrastructure team", "Manages environments, pipelines, deployments and backups."),
            (7, "Information Security Officer", "Arranges security audits and approves security exceptions."),
        ], [1.2, 5, 10.8]),
        ("h", "13. Training"),
        ("b", ["Developers attend secure coding training once a year.",
               "New joiners are trained on this policy during induction.",
               "Training records are kept for at least three years."]),
        *review(14),
    ])


def main():
    OUT.mkdir(exist_ok=True)
    for spec in (TECH_STACK, SDLC):
        doc = new_document(spec)
        render(doc, spec["blocks"])
        approval(doc)
        path = OUT / spec["file"]
        doc.save(path)
        print("wrote", path)


if __name__ == "__main__":
    main()
