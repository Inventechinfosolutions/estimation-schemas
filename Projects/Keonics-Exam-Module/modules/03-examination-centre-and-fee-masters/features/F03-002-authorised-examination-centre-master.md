# F03-002 — Authorised Examination Centre Master

## Section 1 — Feature Specification

| Field | Value |
|---|---|
| **Feature ID** | F03-002 |
| **Feature Name** | Authorised Examination Centre Master |
| **Module** | 03 — Examination, Centre and Fee Masters |

### Description
Examination Administrators maintain the master of authorised examination centres: identity, address, capacity, infrastructure details, activate/deactivate, session mapping, and visibility of allocations against the centre. Only Active authorised centres are available for candidate preference selection and scheduling. Centre users are mapped to these centres under F01-002; this feature owns the centre record itself and operational views of capacity and allocations. Examination from unauthorised centres is out of scope for conduct (Module 07) and is prevented upstream by only listing authorised Active centres here.

### Business Objective
Ensure candidates can prefer and be scheduled only at Department-authorised, Active centres with known capacity and infrastructure, and give Administrators allocation visibility per centre.

### Actors
Examination Administrator (centre master owner); Centre / Invigilator users (consume centre identity via mapping in F01-002); Candidate (selects from Active centres during registration preferences); Auditor (read-only centre history).

### User Journey
1. Who creates: Examination Administrator with centre-master privilege.
2. How they create: Open Centre master register → New centre → enter centre code/name, address, district/city, capacity (seats), infrastructure notes (labs, systems, accessibility as required) → save → Activate when ready for preferences/scheduling.
3. How they edit: Search register → open centre → update capacity, address, infrastructure → save; deactivate to remove from preference and new scheduling while retaining history.
4. How they send for approval: Submit/approval does not apply by default; Administrator activates/deactivates directly with audit.
5. How the approver sees pending items: There is no approver inbox; Inactive or Draft centres appear via status filters on the register.
6. How the approver decides: There is no approval decision; activation is administrative. Session mapping and allocation visibility are maintained on the centre record/views without a separate approval inbox.
7. How the applicant / maker sees history: Administrator opens centre change history (capacity changes, activation, session mapping changes).
8. How the approver / auditor sees history: Auditor opens the same history and allocation visibility snapshots as available for the centre.

### Functional Capabilities
- Maintain authorised centre register with create, edit, search, activate and deactivate.
- Capture centre identity, full address and location attributes needed for hall tickets later.
- Capture seating capacity and infrastructure details relevant to examination conduct readiness.
- Activate/deactivate centres; only Active centres appear for preference selection and new schedules.
- Map examination sessions to centres (link centre to scheduled session slots as scheduling matures; maintain mapping view on the centre).
- View allocations against a centre (candidates allocated / seats used vs capacity) for operational control.
- Prevent preference/scheduling against Inactive or unauthorised centres.
- Enforce unique centre code.
- Support centre search by name, code, district/city, status and capacity range.
- Provide allocation visibility board filtered to one centre.
- Audit all master and activation changes.
- Retain deactivated centres for historical hall tickets and past sessions.

### UI Screens
Named screens estimated independently in Section 2. These are business screens, not wireframes.

| Screen | Complexity |
|---|---|
| Authorised centre master register and search | Complex |
| Centre create / edit form (capacity and infrastructure) | Complex |
| Centre activate / deactivate confirmation | Easy |
| Centre–session mapping view | Complex |
| Centre allocation visibility board | Complex |
| Centres available for preference (admin preview) | Medium |
| Centre master change history | Medium |

### Logical API operations
Named business operations estimated independently in Section 2. These are not REST paths, payloads or technical design.

| Operation | Complexity |
|---|---|
| Create authorised centre | Complex |
| Update centre particulars and capacity | Medium |
| Activate or deactivate centre | Medium |
| Map sessions to centre | Complex |
| Search centre master | Medium |
| View centre allocations vs capacity | Medium |
| List Active centres for preference/scheduling | Easy |
| Read centre change history | Easy |

### Inputs
Centre code; name; address lines; district/city/state/pin; capacity; infrastructure details; activation status; session mapping references; Administrator remarks.

### Outputs
Persisted authorised centre records; Active centre list for preferences and scheduling; session mapping; allocation visibility; change history.

### Business Rules
- Only Active authorised centres are available for preference selection and scheduling.
- Deactivation must not erase historical allocations, hall tickets or past sessions for that centre.
- Capacity is the business ceiling used later in allocation (Module 05); over-allocation rules are enforced there but visibility starts here.
- Centre user mapping (F01-002) may reference only centres that exist in this master.
- Unauthorised or home/personal locations are never centres in this master.

### Validations
- Code and name mandatory; code unique.
- Capacity must be a positive integer.
- Address fields mandatory to the Department-required minimum for hall ticket printing.
- Cannot activate without minimum identity and capacity.
- Cannot map sessions to an Inactive centre for new mappings.
- Deactivate confirmation required when centre has upcoming mapped sessions (warn or block per policy).

### Calculations
Seats used vs capacity on allocation visibility (count of allocated candidates for selected examination/session vs centre capacity).

### Workflow
Create centre → complete particulars → Activate → map sessions as schedules exist → monitor allocations → Deactivate when no longer authorised. No maker–checker inbox by default.

### Search Requirements
Code, name, district/city, status, capacity, updated date; allocation board filters by examination and session date.

### Documents
Optional infrastructure supporting notes; no mandatory document upload in SOW for centre create.

### Reports
Active centres list; capacity vs allocation summary per centre for Administrator operations.

### Notifications
Optional notify centre users on activation/deactivation if Module 09 configured; not required for master CRUD.

### Security
Only Administrators with centre-master privilege mutate centres; centre users read their mapped centre identity; allocation visibility is Administrator (and later centre-scoped views in Module 07); all changes audited.

### Integrations
None for this feature (no SMS/payment/KGID).

### Dependencies
Consumed by F01-002 (user mapping), Module 04 (two preferred centres), Module 05 (scheduling/allocation), Module 07 (centre conduct). Related to F03-001 examinations via session mapping.

### Assumptions
- Physical infrastructure, hardware and networking remain centre/client responsibility; this feature records business master data only.
- Final IP/device whitelist mechanisms are out of scope here (Module 07 / infrastructure).
- Hours use Estimation Master; each named screen and logical API billed independently.

### Risks
- Inflated capacity leading to over-crowding if allocation ignores visibility.
- Leaving deactivated centres selectable would break authorised-centre-only rule.
- Incomplete addresses would degrade hall ticket quality later.

### Non Functional Requirements
Centre register and allocation visibility must support examination-week operational use; Active centre list must be consistent for registration peaks; capacity calculations must reconcile to allocation counts for the selected session.

## Section 2 — Estimation Breakdown (Estimation Master)

| Artifact | Category | Complexity | Hours |
|---|---|---|---|
| Authorised centre master register and search | UI | Complex | 12 |
| Centre create / edit form (capacity and infrastructure) | UI | Complex | 12 |
| Centre activate / deactivate confirmation | UI | Easy | 4 |
| Centre–session mapping view | UI | Complex | 12 |
| Centre allocation visibility board | UI | Complex | 12 |
| Centres available for preference (admin preview) | UI | Medium | 6 |
| Centre master change history | UI | Medium | 6 |
| Create authorised centre | API | Complex | 8 |
| Update centre particulars and capacity | API | Medium | 6 |
| Activate or deactivate centre | API | Medium | 6 |
| Map sessions to centre | API | Complex | 8 |
| Search centre master | API | Medium | 6 |
| View centre allocations vs capacity | API | Medium | 6 |
| List Active centres for preference/scheduling | API | Easy | 4 |
| Read centre change history | API | Easy | 4 |
| Centre master and mapping persistence | DB | Complex | 6 |
| Authorised centre master feature tests | Testing | Complex | 8 |
| Authorised centre master implementation documentation | Documentation | Complex | 4 |
| **Total** | | | **130** |

### Estimation Assumptions
- Hours use the Estimation Master mapping only.
- Allocation visibility assumes allocation data produced by Module 05; this feature estimates the centre-side board and capacity comparison.
- No Integration row — no external channel.
- Each named UI screen and logical API estimated separately.
