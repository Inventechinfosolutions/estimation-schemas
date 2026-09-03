"""Rich KSAAD feature catalogue: actors, full user flow, named screens, logical APIs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Sequence, Tuple


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
    estimate: List[Tuple[str, str, str]] = field(default_factory=list)


@dataclass(frozen=True)
class ModuleDef:
    nn: int
    name: str
    module_type: str
    summary: str
    features: List[FeatureDef]


def _bullets(items: Sequence[str]) -> List[str]:
    return [i for i in items if i]


_RANK = {"Simple": 0, "Easy": 1, "Medium": 2, "Complex": 3, "Very High": 4}


def _highest(values: Sequence[str], default: str) -> str:
    chosen = default
    for value in values:
        if value in _RANK and _RANK[value] > _RANK[chosen]:
            chosen = value
    return chosen


def _from_pairs(pairs: Optional[Sequence[Tuple[str, str]]], default: str = "Simple") -> str:
    if not pairs:
        return default
    return _highest([complexity for _, complexity in pairs], default)


def capability_estimate(
    *,
    name: str,
    noun: str,
    kind: str,
    form_complexity: str = "Complex",
    extra_screens: Optional[List[Tuple[str, str]]] = None,
    extra_apis: Optional[List[Tuple[str, str]]] = None,
    testing: str = "Complex",
    documentation: str = "Medium",
    db_complexity: str = "Medium",
    db_name: str = "",
    integration_name: str = "",
    integration_complexity: str = "Simple",
    include_integration: bool = False,
    primary_ui: str = "",
    secondary_ui: str = "",
    api_name: str = "",
) -> List[Tuple[str, str, str]]:
    """Fraud-grain artefacts: 2 UI + 1 API + DB + optional Integration + Test + Doc."""
    extra_ui = _from_pairs(extra_screens, "Simple")
    extra_api = _from_pairs(extra_apis, "Simple")

    if kind == "master":
        ui1_name = primary_ui or f"{noun.capitalize()} register + search"
        ui2_name = secondary_ui or f"{noun.capitalize()} create/edit form"
        api_label = api_name or f"{noun.capitalize()} uniqueness and lifecycle operations"
        db_label = db_name or f"{noun.capitalize()} identity persistence"
        ui1_c = "Complex"
        ui2_c = "Very High" if form_complexity == "Very High" or extra_ui == "Very High" else "Medium"
        include_integration = True
        if not integration_name:
            integration_name = f"Internal handoff of {noun} to consuming modules"
            integration_complexity = integration_complexity or "Simple"
    elif kind == "txn":
        ui1_name = primary_ui or f"{noun.capitalize()} form and applicant history"
        ui2_name = secondary_ui or f"Approver {noun} inbox and decision"
        api_label = api_name or f"{noun.capitalize()} submit, decide and history operations"
        db_label = db_name or f"{noun.capitalize()} record and status history"
        ui1_c = form_complexity if form_complexity in ("Complex", "Very High") else "Complex"
        ui2_c = "Complex" if extra_ui in ("Complex", "Very High") else "Medium"
        if extra_ui == "Very High":
            ui1_c = _highest([ui1_c, "Very High"], ui1_c)
            ui2_c = "Medium" if ui1_c == "Very High" else ui2_c
    else:
        ui1_name = primary_ui or f"{noun.capitalize()} register"
        ui2_name = secondary_ui or f"{noun.capitalize()} form"
        api_label = api_name or f"{noun.capitalize()} operations"
        db_label = db_name or f"{noun.capitalize()} persistence"
        ui1_c = form_complexity if form_complexity in ("Complex", "Very High") else "Complex"
        ui2_c = "Complex" if extra_ui in ("Complex", "Very High") else "Medium"
        if extra_ui == "Very High" and ui1_c != "Very High":
            ui1_c = "Very High"
            ui2_c = "Complex" if extra_ui == "Very High" else ui2_c

    api_c = "Complex"
    if extra_api == "Very High" or ui1_c == "Very High" or ui2_c == "Very High":
        api_c = "Very High"
    elif kind in ("txn", "master") and extra_api == "Complex":
        api_c = "Very High"

    db_c = db_complexity
    if ui1_c == "Very High" and db_c == "Medium":
        db_c = "Complex"

    test_c = testing
    if test_c == "Complex" and (api_c == "Very High" or ui1_c == "Very High"):
        test_c = "Very High"

    doc_c = documentation
    if doc_c == "Medium" and (ui1_c == "Very High" or ui2_c == "Very High"):
        doc_c = "Complex"

    rows: List[Tuple[str, str, str]] = [
        (ui1_name, "UI", ui1_c),
        (ui2_name, "UI", ui2_c),
        (api_label, "API", api_c),
        (db_label, "DB", db_c),
    ]
    if include_integration or integration_name:
        rows.append(
            (
                integration_name or f"Internal service for {noun}",
                "Integration",
                integration_complexity if integration_complexity in _RANK else "Simple",
            )
        )
    rows.append((f"{name} tests", "Testing", test_c))
    rows.append((f"{name} guide", "Documentation", doc_c))
    return rows


def txn(
    seq: int,
    name: str,
    *,
    noun: str,
    description: str,
    objective: str,
    notes: str,
    applicant: str,
    approver: str,
    others: str,
    create_how: str,
    edit_how: str,
    submit_how: str,
    inbox_how: str,
    decide_how: str,
    applicant_history: str,
    approver_history: str,
    fields: str,
    extra_rules: Optional[List[str]] = None,
    extra_validations: Optional[List[str]] = None,
    calculations: str,
    documents: str,
    reports: str,
    extra_screens: Optional[List[Tuple[str, str]]] = None,
    extra_apis: Optional[List[Tuple[str, str]]] = None,
    testing: str = "Complex",
    documentation: str = "Medium",
    db_name: str = "",
    db_complexity: str = "Medium",
    integration_name: str = "",
    integration_complexity: str = "Simple",
    include_integration: bool = False,
    dependencies: str = "Module 01 Person–Post–Role mapping (current Post and supervising Post). Notifications use the mapped Person of the supervising Post.",
    assumptions: Optional[List[str]] = None,
    risks: str = "Wrong supervising Post mapping would send the request to the wrong approver.",
    register_complexity: str = "Medium",
    form_complexity: str = "Complex",
    inbox_complexity: str = "Complex",
    decision_complexity: str = "Medium",
    history_complexity: str = "Medium",
) -> FeatureDef:
    ui = [
        (f"My {noun} register", register_complexity),
        (f"{noun.capitalize()} form (create and edit)", form_complexity),
        ("Submit confirmation", "Simple"),
        (f"Approver {noun} inbox", inbox_complexity),
        (f"{noun.capitalize()} decision panel (approve / reject / return)", decision_complexity),
        (f"My {noun} history", history_complexity),
        (f"Team {noun} history (approver)", history_complexity),
    ]
    if extra_screens:
        ui.extend(extra_screens)
    api = [
        (f"Save draft {noun}", "Medium"),
        (f"Update draft {noun}", "Medium"),
        (f"Submit {noun} for approval", "Complex"),
        (f"Withdraw {noun}", "Easy"),
        (f"Approver inbox query", "Medium"),
        (f"Approve, reject or return {noun}", "Complex"),
        (f"Applicant history query", "Medium"),
        (f"Team history query", "Medium"),
    ]
    if extra_apis:
        api.extend(extra_apis)
    journey = [
        f"Who creates: {applicant}",
        f"How they create: {create_how}",
        f"How they edit: {edit_how}",
        f"How they send for approval: {submit_how}",
        f"How the approver sees pending items: {inbox_how}",
        f"How the approver decides: {decide_how}",
        f"How the applicant sees history: {applicant_history}",
        f"How the approver sees history: {approver_history}",
    ]
    rules = [
        f"The applicant cannot approve their own {noun}.",
        "Draft and Returned records may be edited; Submitted, Approved and Rejected records cannot be edited.",
        "Every status change stores actor Person, acting Post, timestamp, previous status, new status and remarks.",
        "Approval routes to the Person currently mapped to the supervising Post of the applicant's current Post, unless a specific routing rule is stated.",
    ]
    if extra_rules:
        rules.extend(extra_rules)
    validations = [
        "Mandatory fields must be complete before Submit.",
        "Submit is blocked if the applicant has no current Post mapping.",
        "Submit is blocked if no supervising Post / approver can be resolved.",
        "Approver can act only on items in their inbox (Posts they currently supervise).",
    ]
    if extra_validations:
        validations.extend(extra_validations)
    return FeatureDef(
        seq=seq,
        name=name,
        description=description,
        objective=objective,
        notes=notes,
        actors=f"Applicant: {applicant} Approver: {approver} Other: {others}",
        journey=journey,
        capabilities=_bullets(
            [
                f"Applicant creates, edits draft, submits, withdraws and views own {noun} history.",
                f"Approver sees a pending inbox, opens the record, and approves, rejects or returns with remarks.",
                "Status timeline is visible to both applicant and approver on the same record.",
            ]
        ),
        inputs=fields,
        outputs=f"Persisted {noun} with status; inbox item for the approver; notifications; searchable history for applicant and approver.",
        rules=rules,
        validations=validations,
        calculations=calculations,
        workflow=f"Draft → Submitted → (Returned → Draft) or Approved or Rejected. Withdraw allowed from Submitted before decision.",
        search=f"Applicant register: own records by status, period and type. Approver inbox: pending by office, period, person and type. History: status, actor, period.",
        documents=documents,
        reports=reports,
        notifications=f"Applicant is notified on return, approve, reject. Approver is notified on submit. Notifications go to the Person mapped to the relevant Post.",
        security="Only the applicant (or authorised HR acting on their behalf) may create/edit/submit. Only the resolved approver Post may decide. History is need-to-know.",
        integrations=integration_name or "Internal identity (Module 01) and notification service. Document store when attachments are required.",
        dependencies=dependencies,
        assumptions=assumptions
        or [
            "Supervising Post is maintained on the Post master (Module 01).",
            "Hours use Estimation Master values only, at capability grain (primary and secondary UI, one logical API, persistence, tests, documentation).",
        ],
        risks=risks,
        nfr="Inbox and history screens remain usable under concurrent office load. Status history is immutable after write.",
        ui=ui,
        api=api,
        db=[(db_name or f"{noun.capitalize()} record, status history and attachments metadata", db_complexity)],
        integration=[
            (
                integration_name or f"Notify applicant and approver on {noun} status change",
                integration_complexity,
            )
        ],
        testing=testing,
        documentation=documentation,
        estimate=capability_estimate(
            name=name,
            noun=noun,
            kind="txn",
            form_complexity=form_complexity,
            extra_screens=extra_screens,
            extra_apis=extra_apis,
            testing=testing,
            documentation=documentation,
            db_complexity=db_complexity,
            db_name=db_name or f"{noun.capitalize()} record and status history",
            integration_name=integration_name,
            integration_complexity=integration_complexity,
            include_integration=include_integration,
        ),
    )


def master(
    seq: int,
    name: str,
    *,
    noun: str,
    description: str,
    objective: str,
    notes: str,
    admin: str,
    checker: str,
    create_how: str,
    edit_how: str,
    submit_how: str,
    inbox_how: str,
    decide_how: str,
    applicant_history: str,
    approver_history: str,
    fields: str,
    extra_rules: Optional[List[str]] = None,
    extra_validations: Optional[List[str]] = None,
    calculations: str = "None beyond uniqueness and effective-date overlap checks.",
    documents: str = "None required unless the administrator attaches a supporting office order.",
    reports: str = "Register export for administrators and auditors.",
    extra_screens: Optional[List[Tuple[str, str]]] = None,
    extra_apis: Optional[List[Tuple[str, str]]] = None,
    testing: str = "Complex",
    documentation: str = "Medium",
    db_complexity: str = "Medium",
    integration_complexity: str = "Simple",
    form_complexity: str = "Complex",
    register_complexity: str = "Medium",
    needs_approval: bool = True,
) -> FeatureDef:
    ui = [
        (f"{noun.capitalize()} register and search", register_complexity),
        (f"{noun.capitalize()} create / edit form", form_complexity),
        (f"{noun.capitalize()} change history", "Medium"),
    ]
    if needs_approval:
        ui.extend(
            [
                (f"{noun.capitalize()} maker–checker inbox", "Medium"),
                (f"{noun.capitalize()} approval panel", "Easy"),
            ]
        )
    if extra_screens:
        ui.extend(extra_screens)
    api = [
        (f"Create {noun}", "Medium"),
        (f"Update {noun}", "Medium"),
        (f"Search {noun} register", "Medium"),
        (f"Read {noun} change history", "Easy"),
    ]
    if needs_approval:
        api.extend(
            [
                (f"Submit {noun} change for checker", "Complex"),
                (f"Approve or reject {noun} change", "Complex"),
            ]
        )
    if extra_apis:
        api.extend(extra_apis)
    journey = [
        f"Who creates: {admin}",
        f"How they create: {create_how}",
        f"How they edit: {edit_how}",
        f"How they send for approval: {submit_how}",
        f"How the approver sees pending items: {inbox_how}",
        f"How the approver decides: {decide_how}",
        f"How the maker sees history: {applicant_history}",
        f"How the checker / auditor sees history: {approver_history}",
    ]
    rules = [
        "Create and edit are restricted to authorised administrator Posts.",
        "Historical values are retained; records are deactivated, not physically deleted, unless policy allows delete with reason.",
        "Every change stores actor Person, acting Post, timestamp and before/after values.",
    ]
    if extra_rules:
        rules.extend(extra_rules)
    validations = [
        "Mandatory identity fields are required.",
        "Duplicate unique identifiers are refused.",
    ]
    if extra_validations:
        validations.extend(extra_validations)
    return FeatureDef(
        seq=seq,
        name=name,
        description=description,
        objective=objective,
        notes=notes,
        actors=f"Maker: {admin} Checker: {checker}",
        journey=journey,
        capabilities=_bullets(
            [
                f"Authorised administrator creates and updates the {noun}.",
                "Searchable register and replayable change history.",
                "Checker approval where maker–checker is required.",
            ]
        ),
        inputs=fields,
        outputs=f"Current {noun} record; searchable register; change history.",
        rules=rules,
        validations=validations,
        calculations=calculations,
        workflow=submit_how,
        search=f"Search by identifier, name, office, status and effective date.",
        documents=documents,
        reports=reports,
        notifications="Checker is notified when a change is submitted. Maker is notified on approve or reject.",
        security="Need-to-know. Only authorised Posts may create, edit or approve. History is read-only for auditors.",
        integrations="Consumed by later modules as the system of record for this master.",
        dependencies="Module 01 access. Downstream modules consume this master; they do not recreate it.",
        assumptions=[
            "Hours use Estimation Master values only, at capability grain (not one billed row per screen).",
            "Named screens in the journey are not billed one-for-one; Section 2 uses capability artefacts.",
        ],
        risks=f"Poor unique-identity control on the {noun} would split later transactions across duplicate records.",
        nfr="Register search remains responsive. History is immutable after write.",
        ui=ui,
        api=api,
        db=[(f"{noun.capitalize()} record and change history", db_complexity)],
        integration=[(f"Internal handoff of {noun} to consuming modules", integration_complexity)],
        testing=testing,
        documentation=documentation,
        estimate=capability_estimate(
            name=name,
            noun=noun,
            kind="master",
            form_complexity=form_complexity,
            extra_screens=extra_screens,
            extra_apis=extra_apis,
            testing=testing,
            documentation=documentation,
            db_complexity=db_complexity,
            integration_name=f"Internal handoff of {noun} to consuming modules",
            integration_complexity=integration_complexity,
            include_integration=True,
        ),
    )


def work(
    seq: int,
    name: str,
    *,
    noun: str,
    description: str,
    objective: str,
    notes: str,
    who: str,
    create_how: str,
    edit_how: str,
    submit_how: str,
    inbox_how: str,
    decide_how: str,
    applicant_history: str,
    approver_history: str,
    fields: str,
    extra_rules: Optional[List[str]] = None,
    extra_validations: Optional[List[str]] = None,
    calculations: str,
    documents: str,
    reports: str,
    extra_screens: Optional[List[Tuple[str, str]]] = None,
    extra_apis: Optional[List[Tuple[str, str]]] = None,
    testing: str = "Complex",
    documentation: str = "Medium",
    form_complexity: str = "Complex",
    register_complexity: str = "Medium",
    needs_approval: bool = True,
    db_complexity: str = "Medium",
    integration_complexity: str = "Simple",
    include_integration: bool = False,
    integration_name: str = "",
    dependencies: str = "Module 01 Person–Post–Role. Document store where attachments are required.",
) -> FeatureDef:
    if needs_approval:
        return txn(
            seq,
            name,
            noun=noun,
            description=description,
            objective=objective,
            notes=notes,
            applicant=who,
            approver="Person currently mapped to the supervising Post, unless stated otherwise.",
            others="Auditor (read-only history).",
            create_how=create_how,
            edit_how=edit_how,
            submit_how=submit_how,
            inbox_how=inbox_how,
            decide_how=decide_how,
            applicant_history=applicant_history,
            approver_history=approver_history,
            fields=fields,
            extra_rules=extra_rules,
            extra_validations=extra_validations,
            calculations=calculations,
            documents=documents,
            reports=reports,
            extra_screens=extra_screens,
            extra_apis=extra_apis,
            testing=testing,
            documentation=documentation,
            db_complexity=db_complexity,
            integration_complexity=integration_complexity,
            include_integration=include_integration,
            integration_name=integration_name,
            dependencies=dependencies,
            register_complexity=register_complexity,
            form_complexity=form_complexity,
        )
    ui = [
        (f"{noun.capitalize()} register", register_complexity),
        (f"{noun.capitalize()} form (create and edit)", form_complexity),
        (f"{noun.capitalize()} history", "Medium"),
    ]
    if extra_screens:
        ui.extend(extra_screens)
    api = [
        (f"Create {noun}", "Medium"),
        (f"Update {noun}", "Medium"),
        (f"Search {noun}", "Medium"),
        (f"Read {noun} history", "Easy"),
    ]
    if extra_apis:
        api.extend(extra_apis)
    return FeatureDef(
        seq=seq,
        name=name,
        description=description,
        objective=objective,
        notes=notes,
        actors=f"User: {who} Auditor: read-only history.",
        journey=[
            f"Who creates: {who}",
            f"How they create: {create_how}",
            f"How they edit: {edit_how}",
            f"How they send for approval: {submit_how}",
            f"How the approver sees pending items: {inbox_how}",
            f"How the approver decides: {decide_how}",
            f"How the user sees history: {applicant_history}",
            f"How the supervisor / auditor sees history: {approver_history}",
        ],
        capabilities=_bullets(
            [
                f"Authorised user creates, edits and searches {noun} records.",
                "Status/change history is visible to the user and to authorised supervisors.",
            ]
        ),
        inputs=fields,
        outputs=f"Persisted {noun}; searchable register; history.",
        rules=extra_rules
        or [
            "Only authorised Posts may create or edit.",
            "History is append-only.",
        ],
        validations=extra_validations or ["Mandatory fields required before save."],
        calculations=calculations,
        workflow=submit_how,
        search="Search by identifier, person, office, period and status.",
        documents=documents,
        reports=reports,
        notifications="On-screen confirmation. Optional notice to the user on save failure.",
        security="Need-to-know by Post. Actions attributed to Person acting in a Post.",
        integrations="Module 01 identity. Document store if attachments are used.",
        dependencies=dependencies,
        assumptions=["Hours use Estimation Master values only, at capability grain (not one billed row per screen)."],
        risks="Unscoped access would expose records outside the user's office.",
        nfr="Register and history remain searchable during office hours.",
        ui=ui,
        api=api,
        db=[(f"{noun.capitalize()} record and history", db_complexity)],
        integration=[(f"Internal identity/document hooks for {noun}", integration_complexity)],
        testing=testing,
        documentation=documentation,
        estimate=capability_estimate(
            name=name,
            noun=noun,
            kind="work",
            form_complexity=form_complexity,
            extra_screens=extra_screens,
            extra_apis=extra_apis,
            testing=testing,
            documentation=documentation,
            db_complexity=db_complexity,
            integration_name=integration_name,
            integration_complexity=integration_complexity,
            include_integration=include_integration,
        ),
    )


def build_modules() -> List[ModuleDef]:
    m01 = ModuleDef(
        nn=1,
        name="Person, Post, Role & Access Governance",
        module_type="Shared",
        summary="Shared identity and access model: Person, Post, Post-to-Person mapping, Role-to-Post and audit-grade access controls.",
        features=[
            master(
                1,
                "Person Master",
                noun="Person",
                description="An Administrator maintains each official as a unique Person. Later privileged actions are stored against this Person, not a shared login.",
                objective="Ensure every official action is attributable to one named Person.",
                notes="Foundational person identity directory.",
                admin="Access Administrator (Post with Person-administration Role).",
                checker="Access Checker Post (maker–checker on Person create/update).",
                create_how="Administrator opens Person register → New Person, enters legal name, unique ID, official email and mobile, and saves. Duplicate unique ID is refused.",
                edit_how="Administrator searches the Person, opens the record, edits particulars. Unique ID cannot be reused on another Person. Deactivation does not delete the Person.",
                submit_how="Create/update is submitted to the Access Checker. The Person is not usable for login mapping until approved.",
                inbox_how="Access Checker opens Person approval inbox listing pending creates/updates.",
                decide_how="Checker opens the Person, sees before/after values, Approves or Rejects with remarks. Reject returns to the Administrator for correction.",
                applicant_history="Administrator opens the Person and views change history (who changed what, when).",
                approver_history="Checker and auditor open the same Person history. Login and mapping events are in F01-008.",
                fields="Legal name, unique ID, official email, official mobile, status (Active / Inactive), remarks.",
                extra_rules=[
                    "One Person per official. A second Person for the same unique ID is refused.",
                    "Person is the identity consumed by Post-to-Person mapping (F01-003).",
                ],
                extra_validations=["Unique ID is mandatory and unique.", "Official email, when entered, must be unique."],
                extra_screens=[("Person uniqueness conflict dialog", "Simple")],
                extra_apis=[("Refuse duplicate Person", "Easy")],
            ),
            master(
                2,
                "Post Master and Organisational Placement",
                noun="Post",
                description="Administrator maintains the Post catalogue: office, designation and supervising Post used for approval routing.",
                objective="Provide the organisational Post that Roles and Persons are mapped to.",
                notes="Foundational post catalogue.",
                admin="Access Administrator.",
                checker="Access Checker.",
                create_how="Administrator opens Post register → New Post, enters post code, designation, office (HO/RO/LAC), and supervising Post, then saves.",
                edit_how="Administrator updates office placement or supervising Post with effective dates. Past mappings remain in history.",
                submit_how="Create/update of a Post is submitted to the Access Checker before the Post can be used in mapping.",
                inbox_how="Checker opens Post approval inbox.",
                decide_how="Checker approves or rejects. Reject returns the Post to draft.",
                applicant_history="Administrator opens Post history (placement and supervising-Post changes).",
                approver_history="Checker and auditor open the same history.",
                fields="Post code, designation, office, supervising Post, effective from/to, status.",
                extra_rules=[
                    "A Post cannot supervise itself.",
                    "Approval routing in later modules uses the current supervising Post.",
                ],
                extra_validations=["Post code unique.", "Office mandatory.", "Supervising Post, when entered, must be an existing Post."],
                extra_screens=[("Supervising Post lookup", "Easy")],
            ),
            txn(
                3,
                "Post-to-Person Mapping with Effective Dates",
                noun="Post-to-Person mapping",
                description="Administrator maps a Person to a Post with effective dates. The Person then acts in that Post.",
                objective="Bind a Person to a Post for a period so menus and approvals follow the current mapping.",
                notes="Explicit Person-to-Post mapping.",
                applicant="Access Administrator creates the mapping.",
                approver="Access Checker approves the mapping before it becomes effective.",
                others="The mapped Person (read of own current Posts). Auditor (full history).",
                create_how="Administrator opens Mapping register → New mapping, selects Person, Post, effective from (and optional to), then Save draft.",
                edit_how="Draft or Returned mappings can be edited. An Approved current mapping is ended by setting effective-to or by a new mapping; it is not silently overwritten.",
                submit_how="Administrator clicks Submit. Checker must approve before the Person can sign in under that Post.",
                inbox_how="Checker opens Mapping inbox: pending mappings by office, Person and Post.",
                decide_how="Checker opens the mapping, confirms Person and Post, Approves or Rejects with remarks.",
                applicant_history="Administrator opens mapping history for a Person or a Post (who held which Post, when, who mapped).",
                approver_history="Checker and auditor open the same history. Relinquishment/transfer is also in F01-007.",
                fields="Person, Post, effective from, effective to, mapping reason, remarks.",
                extra_rules=[
                    "A Person may hold more than one Post only if policy allows; overlapping same-Post mappings are refused.",
                    "After approval, the Person's menus follow Roles on that Post (F01-004).",
                ],
                extra_validations=["Person and Post mandatory.", "Effective-from mandatory.", "Overlap on the same Post is refused."],
                extra_apis=[("Check mapping overlap", "Medium")],
                extra_screens=[("Current holders of a Post (read-only)", "Easy")],
                calculations="None beyond overlap of effective-date ranges.",
                documents="Optional office order attachment for the mapping.",
                reports="Current Post-holder report; mapping history export.",
            ),
            master(
                4,
                "Role-to-Post Mapping and Permission Matrix",
                noun="Role-to-Post mapping",
                description="Administrator assigns Roles to Posts and maintains the permission matrix (module, action, data scope).",
                objective="Permissions attach to the Post, not to the Person. The Person inherits them through mapping.",
                notes="Role assignment is at Post level.",
                admin="Access Administrator.",
                checker="Access Checker.",
                create_how="Administrator opens Role–Post matrix, selects a Post, ticks Roles / permissions (view, create, approve, download) per module, Save draft.",
                edit_how="Draft matrix edits are allowed. Approved matrix changes require a new submission. Removing Approve from a Post immediately stops that Post appearing as approver after checker approval.",
                submit_how="Submit sends the matrix change to the Access Checker.",
                inbox_how="Checker opens Role-matrix inbox with before/after permission summary.",
                decide_how="Checker approves or rejects. On approve, Persons currently mapped to the Post get the new menus on next session refresh.",
                applicant_history="Administrator opens permission change history for a Post.",
                approver_history="Checker and auditor open the same history.",
                fields="Post, Role, module, action (view/create/edit/submit/approve/download), data scope (own office / subordinate offices / all).",
                extra_rules=[
                    "Persons are not granted permissions directly.",
                    "Institution users (F01-006) are not given staff Post Roles.",
                ],
                extra_screens=[("Permission matrix grid for a Post", "Very High")],
                form_complexity="Very High",
                extra_apis=[("Resolve effective permissions for a Person's current Post", "Complex")],
            ),
            work(
                5,
                "Authentication, Session and MFA Controls",
                noun="login session",
                description="The Person signs in with official credentials, completes MFA, and works under a selected current Post.",
                objective="Only an activated Person mapped to an Active Post may use the staff application.",
                notes="Explicit authentication and MFA.",
                who="The Person (staff). Access Administrator may unlock or reset per policy.",
                create_how="Person opens login, enters official user ID and password. System challenges MFA (OTP to official email/mobile). On success, Person selects current Post if more than one mapping is Active.",
                edit_how="Person changes password from profile after re-authentication. Administrator may force reset. Person cannot edit MFA target away from official contacts on the Person master.",
                submit_how="Not an approval workflow. Login success creates a session bound to Person + selected Post.",
                inbox_how="Not applicable — no approver inbox. Failed logins appear on the security log (F01-008).",
                decide_how="Not applicable.",
                applicant_history="Person sees own last successful login time on the home page. Full login history is not a self-service dump.",
                approver_history="Access Administrator / auditor opens login and MFA history for a Person (success, fail, lock, unlock).",
                fields="User ID, password, MFA OTP, selected Post.",
                extra_rules=[
                    "Login is refused if Person is Inactive or has no current Post mapping.",
                    "Session carries Person and Post; APIs authorise against Roles on that Post.",
                ],
                extra_validations=["Password policy. OTP expiry. Lock after configured failed attempts."],
                calculations="None.",
                documents="None.",
                reports="Login success/fail counts for administrators.",
                extra_screens=[
                    ("Login screen", "Medium"),
                    ("MFA OTP screen", "Easy"),
                    ("Post selection after login", "Easy"),
                    ("Change password", "Easy"),
                ],
                extra_apis=[
                    ("Authenticate Person", "Complex"),
                    ("Verify MFA OTP", "Medium"),
                    ("Create/end session", "Medium"),
                    ("Unlock / force password reset", "Easy"),
                ],
                needs_approval=False,
                testing="Very High",
                include_integration=True,
                integration_name="OTP / MFA channel delivery",
                integration_complexity="Medium",
            ),
            txn(
                6,
                "Institution and External Identity with Scoped Access",
                noun="institution user registration",
                description="Institution Administrator requests access for an auditee-institution user. Access is scoped to that institution, not to staff Posts.",
                objective="Give auditee institutions a constrained login without mixing them into staff Person–Post mappings.",
                notes="External access is isolated from staff Posts.",
                applicant="Institution Administrator (once the institution is onboarded) or KSAAD Access Administrator for the first institution admin.",
                approver="KSAAD Access Checker / designated institutional-access Post.",
                others="Institution user (uses the login after activation). Auditor.",
                create_how="KSAAD Administrator (first admin) or Institution Administrator opens Institution users → New user, enters name, official email, institution, and requested functions (submit AFS, reply to para, view report/fee).",
                edit_how="Draft registrations can be edited. After approval, profile updates (email) go through the same checker. Institution users cannot be mapped to staff Posts.",
                submit_how="Submit sends the registration to the KSAAD Access Checker.",
                inbox_how="Checker opens Institution-user inbox filtered by institution.",
                decide_how="Checker approves (activation credentials issued) or rejects with remarks.",
                applicant_history="Institution Administrator sees users of their institution and status history.",
                approver_history="KSAAD Checker/auditor sees all institution-user decisions and cannot see staff Person internals from this screen.",
                fields="Name, email, mobile, institution, requested functions, status.",
                extra_rules=[
                    "Institution users never inherit staff Post Roles.",
                    "Data scope is the linked auditee institution only.",
                ],
                extra_validations=["Institution mandatory.", "Email unique within institution users."],
                calculations="None.",
                documents="Optional authorisation letter.",
                reports="Active institution users by institution.",
            ),
            txn(
                7,
                "Joiner-Mover-Leaver and Post Reassignment Governance",
                noun="joiner–mover–leaver request",
                description="Administrator processes joiner (new mapping), mover (end one Post, start another) and leaver (deactivate Person / end mappings) with history retained.",
                objective="Prevent orphaned access when people join, move office or leave.",
                notes="JML and post reassignment.",
                applicant="Access Administrator or HR Establishment Officer raising the JML request against a Person.",
                approver="Access Checker.",
                others="The Person concerned (notified). Auditor.",
                create_how="Administrator opens JML → New request, selects Person, event type (Joiner / Mover / Leaver), target Post(s), effective date, reason.",
                edit_how="Draft/Returned requests can be edited. After Submit, only Withdraw (before decision) is allowed.",
                submit_how="Submit sends to Access Checker. On approval, mappings are ended/created and leaver Person is set Inactive.",
                inbox_how="Checker opens JML inbox by event type and office.",
                decide_how="Checker confirms the Person, Posts and effective date, Approves or Rejects with remarks.",
                applicant_history="Administrator opens the Person's JML history (all join/move/leave events).",
                approver_history="Checker/auditor open the same history including who approved.",
                fields="Person, event type, from Post, to Post, effective date, reason, remarks.",
                extra_rules=[
                    "Leaver ends all current mappings and sets Person Inactive; historical actions remain attributable.",
                    "Mover sets effective-to on the old mapping and creates a new mapping; credentials are not copied between Persons.",
                ],
                extra_validations=["Effective date mandatory.", "Mover requires from and to Post.", "Leaver requires reason."],
                extra_apis=[("Apply mapping end/start on approval", "Complex")],
                calculations="None.",
                documents="Joining/relieving order attachment.",
                reports="Joiners, movers, leavers in a period.",
            ),
            work(
                8,
                "Access Audit, Logging and Periodic Recertification",
                noun="access recertification campaign",
                description="The system records access events. Periodically, a supervising Post recertifies that current mappings under them are still valid.",
                objective="Provide forensic access logs and a controlled recertification cycle.",
                notes="Logging plus recertification.",
                who="Access Administrator opens/starts a recertification campaign. Supervising Posts complete recertification. Auditor reads logs.",
                create_how="Administrator opens Recertification → New campaign, selects office/Posts, due date, then Start. The system lists current mappings in scope.",
                edit_how="Campaign header (due date) can be edited before Start. After Start, mappings in the campaign cannot be deleted from the list; they must be certified or flagged.",
                submit_how="Each supervising Post opens their recertification inbox and Submit-certifies each mapping (Confirm or Revoke with reason). Revoke raises a JML leaver/mover draft (F01-007).",
                inbox_how="Supervising Post sees pending mappings to recertify. Administrator sees overdue campaigns.",
                decide_how="Supervisor marks Confirm or Revoke. Administrator closes the campaign when all items are decided or overdue items are escalated.",
                applicant_history="Administrator opens campaign history and per-mapping decisions.",
                approver_history="Supervisor sees their past recertification decisions. Auditor opens the access log (login, mapping change, permission change, recertification) filtered by Person, Post, period.",
                fields="Campaign name, office scope, due date, mapping, decision, remarks.",
                extra_rules=["Access logs are append-only and cannot be edited by Administrators.", "Recertification does not itself map a Person; Revoke triggers F01-007."],
                extra_validations=["Campaign due date in the future.", "Confirm/Revoke requires identity of acting supervisor."],
                calculations="Overdue = now > due date and item still pending.",
                documents="None.",
                reports="Access log export; recertification completion by office.",
                extra_screens=[
                    ("Access log search (auditor)", "Complex"),
                    ("Recertification campaign form", "Medium"),
                    ("Supervisor recertification inbox", "Complex"),
                ],
                extra_apis=[
                    ("Write access log event", "Complex"),
                    ("Search access log", "Medium"),
                    ("Start recertification campaign", "Complex"),
                    ("Record recertification decision", "Complex"),
                ],
                needs_approval=False,
                testing="Very High",
                form_complexity="Complex",
            ),
        ],
    )

    m02 = ModuleDef(
        nn=2,
        name="Master Data & System Configuration",
        module_type="Business",
        summary="Organisation setup, reference catalogues and configuration used by platform workflows.",
        features=[
            master(
                1,
                "Organisation Hierarchy and Office Master",
                noun="office",
                description="Administrator maintains HO, RO and LAC offices and their parent hierarchy.",
                objective="Give every Post and transaction an office scope.",
                notes="Organisation and office setup.",
                admin="Master Data Administrator.",
                checker="Master Data Checker.",
                create_how="Opens Office register → New office, enters code, name, type (HO/RO/LAC), parent office, then Save.",
                edit_how="Draft edits allowed. Approved offices can be renamed or re-parented via a checked change. Offices in use cannot be deleted.",
                submit_how="Submit to checker before the office can be selected on Posts.",
                inbox_how="Checker office-change inbox.",
                decide_how="Approve or reject with remarks.",
                applicant_history="Office change history on the record.",
                approver_history="Same history for checker/auditor.",
                fields="Office code, name, type, parent office, status.",
                extra_validations=["Code unique.", "LAC must have a parent RO unless type is HO."],
            ),
            master(
                2,
                "Department, Post and Designation Masters",
                noun="designation catalogue item",
                description="Administrator maintains departments and designations used when creating Posts. This does not replace the Post master in Module 01.",
                objective="Keep designation and department lists consistent for Post creation.",
                notes="Supports governance and HR processes.",
                admin="Master Data Administrator.",
                checker="Master Data Checker.",
                create_how="Opens Designation / Department register → New, enters code and name.",
                edit_how="Edit draft or submit a change to rename. Items in use on Posts cannot be deleted.",
                submit_how="Submit to checker.",
                inbox_how="Checker inbox for catalogue changes.",
                decide_how="Approve or reject.",
                applicant_history="Catalogue item history.",
                approver_history="Same for checker.",
                fields="Code, name, department (for designation), status.",
                extra_rules=["Post master (F01-002) selects from this catalogue; it does not free-type designation."],
            ),
            master(
                3,
                "Reference Data Catalogues",
                noun="reference catalogue item",
                description="Administrator maintains shared lists: leave types, statuses, document types, para types, fee heads.",
                objective="Stop free-text codes in transactions.",
                notes="Shared system catalogues.",
                admin="Master Data Administrator.",
                checker="Master Data Checker.",
                create_how="Opens Catalogue by type → New item, code, name, sort order, effective dates.",
                edit_how="Edit draft. Deactivate items instead of delete when already used on transactions.",
                submit_how="Submit to checker.",
                inbox_how="Checker catalogue inbox.",
                decide_how="Approve or reject.",
                applicant_history="Item history including deactivation.",
                approver_history="Same for checker.",
                fields="Catalogue type, code, name, sort order, effective from/to, status.",
            ),
            master(
                4,
                "Workflow Templates and Rule Configuration",
                noun="workflow template",
                description="Administrator defines which supervising Post (or Role) approves which transaction type, including SLA hours.",
                objective="Make approval routing configurable without changing each module.",
                notes="Commercial configurability of routing.",
                admin="Workflow Administrator.",
                checker="Workflow Checker.",
                create_how="Opens Workflow templates → New, selects transaction type (leave, TA/DA, indent, audit report), default route (supervising Post), optional amount threshold, SLA hours.",
                edit_how="Version the template; in-flight transactions keep the version they were submitted on.",
                submit_how="Submit new version to checker before it applies to new submissions.",
                inbox_how="Checker template inbox.",
                decide_how="Approve or reject the new version.",
                applicant_history="Template version history.",
                approver_history="Same for checker.",
                fields="Transaction type, route rule, threshold, SLA hours, version, status.",
                extra_rules=["Existing submitted records do not silently change route when a new version is approved."],
                extra_screens=[("Template version comparison", "Medium")],
                form_complexity="Very High",
            ),
            master(
                5,
                "Reporting and MIS Parameters",
                noun="MIS parameter set",
                description="Administrator sets default filters, export formats and alert thresholds used by Module 14.",
                objective="Standardise MIS defaults per office/role.",
                notes="Supports standardised reporting.",
                admin="MIS Administrator.",
                checker="MIS Checker.",
                create_how="Opens MIS parameters → New set for an office or Role, sets default period, export format, alert thresholds.",
                edit_how="Edit draft; submit to checker.",
                submit_how="Checker approval before defaults apply.",
                inbox_how="Checker MIS-parameter inbox.",
                decide_how="Approve or reject.",
                applicant_history="Parameter change history.",
                approver_history="Same for checker.",
                fields="Office/Role scope, default period, export format, alert thresholds.",
            ),
        ],
    )

    m03 = ModuleDef(
        nn=3,
        name="HRMS Core Personnel Management",
        module_type="Business",
        summary="Employee lifecycle and core HRMS: service details, leave, diary, attendance, training and communications.",
        features=[
            master(
                1,
                "Employee Master and Service Details",
                noun="employee service record",
                description="HR Establishment Officer maintains service particulars on the Person (joining date, cadre, office of posting as HR data). This is not a second login identity.",
                objective="Hold HR service data against the same Person used for access.",
                notes="Core HR employee records on the Person.",
                admin="HR Establishment Officer.",
                checker="HR Checker / Establishment supervisor.",
                create_how="Officer opens Employee register, searches the Person (F01-001). If none, they must request Person create first. Then opens Service details and enters joining date, cadre, GPF/PRAN, current office (HR view).",
                edit_how="Draft service updates can be edited. Approved fields (joining date) change only via checked amendment.",
                submit_how="Submit service-data changes to HR Checker.",
                inbox_how="HR Checker inbox of pending service amendments.",
                decide_how="Approve or reject with remarks.",
                applicant_history="Officer opens the Person's service history tab.",
                approver_history="Checker/auditor open the same tab.",
                fields="Person, joining date, cadre, GPF/PRAN, HR office, remarks.",
                extra_rules=["Does not create a login. Login identity remains Person + Post mapping.", "Post occupancy remains F01-003; this screen stores HR service attributes."],
                extra_validations=["Person must already exist.", "Joining date mandatory."],
            ),
            work(
                2,
                "Post and Vacancy Management",
                noun="vacancy position",
                description="HR Establishment Officer maintains sanctioned strength vs occupied Posts (from Module 01 mappings) and vacancy.",
                objective="Show vacancy without duplicating the Post master.",
                notes="Vacancy uses Post master + current mappings.",
                who="HR Establishment Officer updates sanctioned numbers. Occupied count is derived from approved Post-to-Person mappings.",
                create_how="Officer opens Vacancy register by office/designation, enters sanctioned strength for that Post/designation, Save.",
                edit_how="Sanctioned strength changes are edited on the same register (checked if policy requires). Occupied is not typed; it comes from current mappings.",
                submit_how="If maker–checker is on, sanctioned-strength change is submitted to HR Checker. Occupied/vacant figures are calculated, not submitted.",
                inbox_how="HR Checker sees pending sanctioned-strength changes. There is no inbox for occupied counts.",
                decide_how="Checker approves sanctioned-strength change.",
                applicant_history="Officer sees history of sanctioned-strength changes.",
                approver_history="Checker/auditor see the same plus derived occupied snapshots in the vacancy report.",
                fields="Office, designation/Post, sanctioned strength, effective date.",
                extra_rules=["Occupied = count of current approved mappings to that Post.", "Vacant = sanctioned − occupied (not below zero without a warning)."],
                extra_validations=["Sanctioned strength integer ≥ 0."],
                calculations="Occupied from F01-003; Vacant = sanctioned − occupied.",
                documents="Optional sanction order.",
                reports="Vacancy statement by office.",
                extra_screens=[("Vacancy register (sanctioned vs occupied)", "Complex")],
                extra_apis=[("Derive occupied count from mappings", "Medium")],
                needs_approval=True,
            ),
            txn(
                3,
                "Leave Management System",
                noun="leave application",
                description="The staff member applies for leave against their current Post. The reporting officer (Person mapped to the supervising Post) sees an inbox and approves, rejects or returns. Both see history.",
                objective="Replace informal leave with a Post-routed application, decision and history.",
                notes="Full leave create / edit / submit / approve / history.",
                applicant="The staff member — the Person currently mapped to a Post — applies for their own leave. HR Establishment Officer may raise an application on behalf of a Person only with a recorded reason (e.g. person on medical emergency).",
                approver="The Person currently mapped to the supervising Post of the applicant's Post (Module 01). If that Person is on leave, the workflow template may route to the next supervising Post.",
                others="HR Establishment Officer (balances, on-behalf apply). Auditor (read-only).",
                create_how="Applicant opens My Leave Applications → New. System shows Person name, current Post and leave balances. Applicant selects leave type, from date, to date (or first/second session), reason, optional attachment (medical certificate). Applicant clicks Save draft. The application is not visible in the approver inbox yet.",
                edit_how="Applicant opens a Draft or Returned application from My Leave Applications, changes dates/type/reason/attachment, Save. Submitted, Approved and Rejected applications cannot be edited. Applicant may Withdraw a Submitted application before the approver decides; Withdrawn applications are not decided.",
                submit_how="On the form, applicant clicks Submit. System checks: balance sufficient (or 'without balance' type allowed), no overlapping approved/pending leave, supervising Post resolved. On success, status becomes Submitted and the reporting officer receives an inbox item and notification. Applicant cannot submit if they are also the only mapped Person on the supervising Post (self-approval blocked); HR must route to the next Post.",
                inbox_how="Approver opens Approver Leave Inbox. Default filter: Pending, for Posts they currently supervise. Columns: applicant Person, Post, leave type, period, days, submitted on. Approver may filter by office, type and period. Approver clicks a row to open the read-only application plus balances and overlapping leave.",
                decide_how="On the decision panel the approver selects Approve, Reject or Return for correction. Reject and Return require remarks. Approve deducts balance (unless type does not debit). Return sets status Returned; applicant edits and resubmits. Approver cannot edit the applicant's dates; they decide or return.",
                applicant_history="Applicant opens My Leave History (or the History tab on an application). Timeline shows Draft saved, Submitted, Returned, resubmitted, Approved/Rejected/Withdrawn — each with Person, Post, date-time and remarks. Applicant also sees year-wise balance (opening, credited, taken, closing).",
                approver_history="Approver opens Team Leave History: applications they decided, and current pending for their Posts. They do not see leave of Persons outside their supervised Posts. Auditor with the access-log Role can see all leave decisions.",
                fields="Leave type, from date, to date, session, reason, attachment, on-behalf flag and reason (if HR applies), applicant Person and Post (system), current balance (system).",
                extra_rules=[
                    "Balance is computed from credited leave and approved applications; pending applications reserve balance until decided.",
                    "Overlapping periods with another pending or approved leave of the same Person are refused.",
                    "Cancelled after approval is a separate action (if policy allows) and restores balance; it is not a silent edit.",
                ],
                extra_validations=[
                    "From date ≤ to date.",
                    "Leave type mandatory and from the leave-type catalogue.",
                    "Medical certificate mandatory when leave type requires it.",
                    "Submit blocked when reserved+requested days exceed balance for debiting types.",
                ],
                extra_screens=[
                    ("Leave balance panel on the form", "Medium"),
                    ("Overlap warning dialog", "Simple"),
                ],
                extra_apis=[
                    ("Get leave balance for Person", "Medium"),
                    ("Check overlapping leave", "Medium"),
                    ("Debit or restore leave balance", "Complex"),
                ],
                calculations="Days = inclusive calendar days minus configured weekly offs/holidays when the leave type says so. On Submit, requested days are reserved. On Approve, reserved becomes taken. On Reject/Withdraw/Return, reserved is released. On Approve of a debiting type, closing balance decreases.",
                documents="Medical certificate or other proof when the leave type requires it, stored via DMS and linked to the application.",
                reports="Leave register by Person/office/type; pending inbox ageing; balance statement.",
                testing="Very High",
                documentation="Complex",
                db_name="Leave application, status history, balance ledger and attachment links",
                db_complexity="Complex",
            ),
            txn(
                4,
                "Work Diary Submission",
                noun="work diary",
                description="The staff member records work done for a date or week and submits it to the supervising Post for acknowledgement.",
                objective="Supervisors see field/office work without paper diaries.",
                notes="Work diary create / submit / acknowledge / history.",
                applicant="Person mapped to a Post (typically field auditor or office staff required to file a diary).",
                approver="Person mapped to the supervising Post.",
                others="Auditor (read-only).",
                create_how="Applicant opens My Work Diaries → New, selects period (date or week), enters work description, place of work, optional link to tour/audit assignment, Save draft.",
                edit_how="Draft or Returned diaries can be edited. Submitted/Acknowledged cannot be edited.",
                submit_how="Submit sends to supervising Post. Duplicate diary for the same Person and date is refused.",
                inbox_how="Supervisor opens Work Diary inbox (pending acknowledgement).",
                decide_how="Supervisor Acknowledge, Return for correction, or Record exception (with remarks). Acknowledge is not a financial approval.",
                applicant_history="My Work Diary history with statuses and supervisor remarks.",
                approver_history="Team diary history for supervised Posts.",
                fields="Period, work description, place, linked assignment (optional), remarks.",
                extra_validations=["Period mandatory.", "Description mandatory.", "One diary per Person per date."],
                calculations="None.",
                documents="Optional supporting note.",
                reports="Diary compliance (submitted vs expected days).",
            ),
            work(
                5,
                "Attendance Management",
                noun="attendance exception",
                description="Attendance is recorded (manual mark or imported punch). The staff member or HR raises exceptions; the supervisor decides. Everyone sees history.",
                objective="Keep an attributable attendance register with exception workflow.",
                notes="Attendance capture plus exception approval.",
                who="HR/office clerk records or imports daily attendance. Staff member raises an exception (missed punch, on-duty). Supervisor decides exceptions.",
                create_how="Clerk opens Attendance register for a date/office, marks Present/Absent/On leave (leave comes from approved leave) or runs import. Staff member opens My Attendance → Raise exception for a date, states reason, Save draft.",
                edit_how="Clerk can correct a day's mark only before freeze. Exception drafts can be edited. Frozen days require an exception request.",
                submit_how="Staff submits the exception to the supervising Post. Clerk freeze of a day may require HR Checker if configured.",
                inbox_how="Supervisor opens Attendance exception inbox.",
                decide_how="Supervisor Approve exception (updates the day's mark) or Reject with remarks.",
                applicant_history="Staff opens My Attendance calendar and drill-down history of marks and exceptions.",
                approver_history="Supervisor sees team attendance and exception decisions. Auditor sees freeze and exception log.",
                fields="Date, Person, mark, exception reason, remarks.",
                extra_rules=["Approved leave automatically marks On leave for those dates.", "Frozen attendance is not silently overwritten."],
                extra_validations=["One mark per Person per date.", "Exception requires a date and reason."],
                calculations="None beyond counts of present/absent in the register.",
                documents="Optional duty order for on-duty exception.",
                reports="Daily attendance by office; exception register.",
                extra_screens=[
                    ("Attendance register (day/office grid)", "Complex"),
                    ("My Attendance calendar", "Medium"),
                    ("Exception form", "Medium"),
                    ("Exception inbox", "Medium"),
                ],
                extra_apis=[
                    ("Save daily attendance mark", "Medium"),
                    ("Import attendance file", "Very High"),
                    ("Submit attendance exception", "Complex"),
                    ("Decide exception", "Complex"),
                ],
                needs_approval=False,
                testing="Very High",
            ),
            txn(
                6,
                "Training and Capacity Building Management",
                noun="training nomination",
                description="HR or a supervisor nominates a Person to a training programme; the nominee's supervising Post (or Training Officer) approves; attendance/completion is recorded.",
                objective="Track nominations, approvals and completion.",
                notes="Training nomination workflow.",
                applicant="HR Training Officer or the staff member's supervisor creates a nomination. Staff member may self-nominate if policy allows.",
                approver="Training Officer Post or supervising Post per workflow template.",
                others="Nominee (sees own nominations). Auditor.",
                create_how="Applicant opens Training programmes (catalogue) → Nominate, selects Person, programme, dates, Save draft.",
                edit_how="Draft/Returned nominations can be edited. After approval, completion is recorded separately (not by editing the nomination).",
                submit_how="Submit to the configured approver.",
                inbox_how="Approver Training nomination inbox.",
                decide_how="Approve, reject or return. After the event, Training Officer records Completed / Not attended with dates.",
                applicant_history="Nominator and nominee see nomination and completion history.",
                approver_history="Approver sees decisions and completion status for programmes they own.",
                fields="Person, programme, dates, nomination remarks, completion status.",
                extra_screens=[("Training programme catalogue (read/admin)", "Medium"), ("Completion recording form", "Easy")],
                extra_apis=[("Record training completion", "Easy")],
                extra_validations=["Programme and Person mandatory.", "Dates within programme window."],
                calculations="None.",
                documents="Optional course material via knowledge centre.",
                reports="Nominations and completions by programme/office.",
            ),
            txn(
                7,
                "Retirement and Pension Tracking",
                noun="retirement case",
                description="HR opens a retirement case from the Person's service dates; the case is submitted through establishment approvals; pension checklist progress is recorded.",
                objective="Track retirement milestones without running a full pension disbursement engine unless later ordered.",
                notes="Retirement lifecycle tracking.",
                applicant="HR Establishment Officer creates the case when the Person is within the configured notice window of superannuation (or on voluntary retirement request).",
                approver="Establishment supervisor / competent Post per template.",
                others="The retiring Person (read of their case status). Auditor.",
                create_how="Officer opens Retirement register → New, selects Person; system fills likely retirement date from service data; officer confirms type (superannuation / VRS), Save draft.",
                edit_how="Draft/Returned cases editable. After Submit, checklist items are updated without changing identity fields.",
                submit_how="Submit for establishment approval of the case opening. Later checklist completions may be maker–checker per item.",
                inbox_how="Approver retirement-case inbox.",
                decide_how="Approve case opening or reject. Officer then ticks checklist (pension papers, NOC) with dates; checker may confirm completed items.",
                applicant_history="Officer and Person see case timeline and checklist history.",
                approver_history="Approver sees cases decided and pending checklist ageing.",
                fields="Person, retirement type, retirement date, checklist items, remarks.",
                extra_rules=["Does not itself calculate pension amounts unless a later ordered interface exists.", "Person is not auto-deactivated; leaver is F01-007 on the retirement date."],
                extra_screens=[("Retirement checklist panel", "Complex")],
                extra_apis=[("Update checklist item", "Medium")],
                extra_validations=["Person mandatory.", "Retirement date mandatory."],
                calculations="Notice window = retirement date − configured months; case can be opened when today is inside the window.",
                documents="Pension papers checklist attachments.",
                reports="Upcoming retirements; pending checklist.",
            ),
            txn(
                8,
                "Rewards and Recognition Register",
                noun="reward proposal",
                description="A supervisor proposes a reward for a Person; competent Post approves; the register and history are visible to HR and the Person.",
                objective="Record rewards with approval, not informal notes.",
                notes="Rewards register with approval.",
                applicant="Supervising Post (or HR) raises the proposal against a Person.",
                approver="Competent authority Post per workflow template.",
                others="Nominee Person (sees approved rewards). Auditor.",
                create_how="Applicant opens Rewards → New, selects Person, reward type, citation, date, Save draft.",
                edit_how="Draft/Returned editable. Approved entries are not rewritten; cancellations are a new action with reason.",
                submit_how="Submit to competent Post.",
                inbox_how="Approver rewards inbox.",
                decide_how="Approve or reject with remarks.",
                applicant_history="Proposer sees proposal history. Person sees own approved rewards.",
                approver_history="Approver sees decided proposals.",
                fields="Person, reward type, citation, proposed date, remarks.",
                extra_validations=["Person and reward type mandatory.", "Citation mandatory."],
                calculations="None.",
                documents="Optional citation attachment.",
                reports="Rewards by office and year.",
            ),
            work(
                9,
                "Circulars, Notifications and Internal Communication",
                noun="circular",
                description="An authorised officer drafts a circular, submits for release approval, publishes to selected Posts/offices; staff acknowledge if required; history of publish and acknowledgement is kept.",
                objective="Controlled internal communication with audience and acknowledgement.",
                notes="Circular publish workflow.",
                who="Communications / Establishment Officer drafts. Competent Post approves release. Staff in audience read and acknowledge.",
                create_how="Officer opens Circulars → New, enters title, body or attachment, audience (office, Role, Post), acknowledgement required yes/no, Save draft.",
                edit_how="Draft/Returned editable. After Publish, content is frozen; only expire/withdraw with reason.",
                submit_how="Submit for release approval. On approve, system publishes to audience.",
                inbox_how="Release-approver inbox. Staff see My Circulars inbox of unpublished-to-them items (published circulars).",
                decide_how="Approver Approves release or Rejects. Staff click Acknowledge when required.",
                applicant_history="Author sees versions, publish time, acknowledgement counts.",
                approver_history="Approver sees release decisions. Author/auditor see who acknowledged and when.",
                fields="Title, body/attachment, audience, acknowledgement required, effective from/to.",
                extra_rules=["Withdrawn circulars remain in history.", "Audience is Post/office based, not ad-hoc email lists only."],
                extra_validations=["Title mandatory.", "Audience not empty."],
                calculations="Acknowledgement % = acknowledged / audience size.",
                documents="Circular PDF/attachment via DMS.",
                reports="Unacknowledged circulars by office.",
                extra_screens=[
                    ("Circular draft form", "Complex"),
                    ("Release approver inbox", "Medium"),
                    ("My Circulars (staff)", "Medium"),
                    ("Acknowledgement register", "Medium"),
                ],
                extra_apis=[
                    ("Submit circular for release", "Complex"),
                    ("Publish to audience", "Complex"),
                    ("Record acknowledgement", "Easy"),
                ],
                needs_approval=False,
                testing="Very High",
            ),
        ],
    )

    from ksaad_feature_specs_rest import rest_modules

    return [m01, m02, m03] + rest_modules()
