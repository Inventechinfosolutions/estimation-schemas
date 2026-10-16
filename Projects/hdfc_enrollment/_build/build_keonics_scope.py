"""Build the KEONICS project scope and man-days effort document (Word) for HDFC vendor onboarding.

Run from repo root:
    .venv/bin/python Projects/hdfc_enrollment/_build/build_keonics_scope.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_policies import approval, new_document, render  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "KEONICS_Project_Scope_and_Effort.docx"

MODULES = [
    ("User administration and masters", "Users, user types, roles and permissions; master data used across modules; "
     "login with CAPTCHA.", 70),
    ("Approval workflow engine", "Configurable multi-level approval flows used by all business modules (purchase order, "
     "invoice, work order, HR, training, facility, expenditure, service and tenant invoice).", 90),
    ("Goods procurement", "Goods catalogue, cart and pre-orders, purchase orders, invoices and payments, with approval at "
     "each level.", 200),
    ("Vendor management and expenditure", "Vendor registration and resources, work orders, expenditure entry, tracking "
     "and approval.", 130),
    ("HR resources", "HR resource requests and approvals for departments.", 90),
    ("Training centres and students", "Training centre registration and approval, student enrolment, training "
     "dashboard.", 150),
    ("Facility and tenant management", "Facilities, tenants, tenant invoices, and tenant help desk with automatic daily "
     "escalation.", 140),
    ("Service management", "Service indents and service orders with approval.", 90),
    ("Plots and buyers", "Plot records and buyer management.", 60),
    ("Infrastructure mapping and dashboard", "Mapping of infrastructure assets and a management dashboard.", 70),
    ("Help desk", "Raising and tracking of support requests.", 40),
    ("Common services", "Email notifications through a message queue, document storage, PDF and Excel reports, and "
     "digital signature (DSC) signing and validation.", 70),
]

PHASES = [
    ("Requirements study and design", "Requirement discussions with KEONICS, module design, data model, screen design",
     10),
    ("Development", "Frontend, backend, approval flows, integrations", 55),
    ("Testing and QA", "Functional, regression and integration testing", 15),
    ("UAT support and fixes", "Support during KEONICS user testing, defect fixing", 8),
    ("Deployment and go-live support", "UAT and production deployment, data setup, user handholding", 7),
    ("Project management", "Planning, tracking, client meetings, reporting", 5),
]

TOTAL = sum(m[2] for m in MODULES)
assert TOTAL == 1200, TOTAL

SPEC = dict(
    title="KEONICS Portal: Project Scope and Effort",
    doc_id="IIS-PRJ-KEONICS-01",
    owner="Project Manager",
    blocks=[
        ("h", "1. Project overview"),
        ("t", ["Item", "Details"], [
            ("Project name", "KEONICS Portal"),
            ("Client", "KEONICS (Karnataka State Electronics Development Corporation Ltd.), Government of Karnataka"),
            ("Sector", "Government"),
            ("Objective", "A single web portal for KEONICS operations: goods procurement, vendors and expenditure, HR "
             "resources, training centres and students, facility and tenant management, service management, plots and "
             "buyers, infrastructure mapping and help desk, all with multi-level approvals."),
            ("Duration", "December 2024 to date"),
            ("Status", "Some modules live; others in progress"),
            ("Hosting", "KEONICS office server (production); Company servers (UAT)"),
            ("Technology", "React 18 with TypeScript and Ant Design (frontend); NestJS 10 on Node.js (backend); MySQL, "
             "Redis, MinIO object storage and RabbitMQ"),
            ("Total effort", f"About {TOTAL:,} man-days (1 man-day = 8 hours)"),
        ], [4.5, 12.5]),
        ("h", "2. Size of the application"),
        ("t", ["Sl. No.", "Measure", "Value"], [
            (1, "Functional modules", f"{len(MODULES)}"),
            (2, "User types", "8 (KEONICS staff, departments, vendors, evaluators, training centres, students, tenants, "
             "facility managers)"),
            (3, "Database tables", "About 173"),
            (4, "API endpoints", "About 1,684, across 214 controllers"),
            (5, "Approval workflows", "More than 10 configurable multi-level flows"),
        ], [1.2, 5, 10.8]),
        ("h", "3. Scope of work"),
        ("t", ["Sl. No.", "Module", "Scope", "Effort (man-days)"],
         [(i, m, s, d) for i, (m, s, d) in enumerate(MODULES, 1)] + [("", "Total", "", f"{TOTAL:,}")],
         [1.2, 4.4, 8.6, 2.8]),
        ("h", "4. User types"),
        ("t", ["Sl. No.", "User type", "Main use"], [
            (1, "KEONICS staff and administrators", "Configure masters, approve requests, monitor dashboards"),
            (2, "Departments", "Raise indents, purchase and service requests"),
            (3, "Vendors", "Register, supply goods and resources, submit invoices"),
            (4, "Evaluators", "Evaluate and approve as per workflow"),
            (5, "Training centres", "Register centres, enrol students"),
            (6, "Students", "Enrol in training programmes"),
            (7, "Tenants", "View invoices, raise help-desk requests"),
            (8, "Facility managers", "Manage facilities and tenant requests"),
        ], [1.2, 5.4, 10.4]),
        ("h", "5. Integrations"),
        ("b", ["Email (SMTP) through a RabbitMQ mail queue.",
               "MinIO (S3-compatible) object storage for documents.",
               "Redis for caching and session control.",
               "Digital signature (DSC) signing and validation for department users.",
               "PDF and Excel report generation."]),
        ("h", "6. Non-functional requirements"),
        ("b", ["Security: JWT login with refresh tokens, CAPTCHA, bcrypt password hashing, role-based access, request rate "
               "limiting, secure HTTP headers, TLS 1.3 in transit.",
               "Audit: created-by and updated-by details on every record, and approval history for every workflow.",
               "Logging: daily rotating application logs and health-check endpoints.",
               "Usability: responsive web interface for desktop and tablet."]),
        ("h", "7. Effort by phase"),
        ("t", ["Sl. No.", "Phase", "Activities", "Share", "Man-days"],
         [(i, p, a, f"{s}%", f"{round(TOTAL * s / 100):,}") for i, (p, a, s) in enumerate(PHASES, 1)]
         + [("", "Total", "", "100%", f"{TOTAL:,}")],
         [1.2, 4.2, 7.4, 1.8, 2.4]),
        ("h", "8. Notes"),
        ("b", [f"The total effort of about {TOTAL:,} man-days is as recorded by the Company. The split by module and by "
               "phase is estimated from the relative size of each module and the Company's usual phase ratios.",
               "Scope is described as implemented in the application. The contract scope document from KEONICS is not "
               "included."]),
    ])


def main():
    doc = new_document(SPEC)
    render(doc, SPEC["blocks"])
    approval(doc)
    doc.save(OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
