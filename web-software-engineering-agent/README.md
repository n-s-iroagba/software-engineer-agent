# Agentic Software Engineering Pipeline

Standardized 10-phase Waterfall lifecycle for high-fidelity software engineering. This pipeline functions as a rational decision-making framework, ensuring every architectural, data, and testing choice is objectively justified.

## 0. The Engineering Workflow
Every phase in this pipeline follows a strict **"Consult -> Design -> Review -> Sign-off"** loop to eliminate guesswork:

1.  **Step 0: Consultation**: The AI analyzes the previous baseline and asks the Human Engineer for guidance on ambiguities.
2.  **Design Baseline**: The AI generates the technical artifacts using the standard templates.
3.  **Human Review**: The Human Engineer audits the baseline for alignment with requirements and NFRs.
4.  **Sign-off Gate**: The Human Engineer signs the "Baseline Approval" section. **The AI must not proceed until this gate is passed.**

## 1. Pipeline Phases

| Phase | Folder | Primary Deliverable | Upstream Dependency | Goal |
| :--- | :--- | :--- | :--- | :--- |
| **00** | `00_input` | Project Input Data | **None (Root)** | Raw business case, flows, brand, caveats |
| **01** | `01_strs` | Ubiquitous Language | Phase 00 | Stakeholder Requirement Baseline |
| **02** | `02_use_cases` | Scenario Mappings | Phase 01 | Mapping human goals to system behavior |
| **03** | `03_srs` | Technical FRS/NFRS | Phases 01-02 | Formalizing testable requirements |
| **04** | `04_architectural_design` | ADRs & Topology | Phases 01-03 | Macro/Micro architectural decisions |
| **05** | `05_data_domain_design` | Data Dictionary | Phases 01, 03-04 | Persistence & Domain modeling |
| **06** | `06_ui_ux_design` | Tech Component Specs | Phases 01-05 | Frontend blueprint (Props/Hooks/State) |
| **07** | `07_api_design` | API Specification | Phases 01, 03-06 | Contract-first communication design |
| **08** | `08_testing_qa` | Test Strategy | Phases 01, 03-04, 06-07 | 100% RTM coverage & UAT gates |
| **09** | `09_implementation` | Versioned Codebase | Phases 01, 03-08 | Strict traceability implementation |
| **10** | `10_deployment_ops` | Handover Baseline | Phases 01, 03-04, 08-09 | Observability & Operational visibility |

### Dependency Chain
```
00_input (Root: Business Case, Flows, Colors, Caveats)
  └── 01_strs (Ubiquitous Language, Scale Targets)
        └── 02_use_cases (Actor-Goal Scenarios)
              └── 03_srs (FRS, NFRS, Workload, Compliance)
                    └── 04_architectural_design (ADRs, Stack, Topology)
                          ├── 05_data_domain_design (Entities, Schema)
                          │     └── 06_ui_ux_design (Screens, Components)
                          │           └── 07_api_design (Endpoints, Contracts)
                          │                 └── 08_testing_qa (Test Strategy, Cases)
                          │                       └── 09_implementation (Code, Tests)
                          │                             └── 10_deployment_ops (CI/CD, Handover)
                          └────────────────────────────────────────────┘
```


## 2. Governance Principles
- **Zero Hardcoding**: All technical choices (stack, DB, auth) must be selected from provided inventories using a Weighted Decision Matrix. No magic string literals allowed in business logic; use Constants/Enums.
- **Traceability (RTM)**: Every requirement must be tracked from Phase 01 to Phase 10 via the living Requirements Traceability Matrix.
- **Security Vulnerability Audits**: All designs must explicitly check and mitigate business logic vulnerabilities, Insecure Direct Object References (IDOR), and Injection flaws.
- **DTO Mandate (Mass Assignment Prevention)**: Explicit Data Transfer Objects (DTOs) MUST be used to decouple external payload structures from internal domain entities.
- **Service Code Specification**: All implementation methods must use JSDoc tags for `@req` (Requirement), `@layer` (Architectural Layer), and `@screen` (UI Screen ID).
- **Ubiquitous Language**: Terminology defined in Phase 01 is immutable across all code and database artifacts.
- **NFR Compliance**: Every design step (Phases 04-07) must audit against the NFRs (Security, Performance, Scale) defined in Phase 03.
- **Compliance First**: All industry standards (e.g., ISO, GDPR, WCAG) are formally baselined in **Phase 03 (NFR-COMP)**. Compliance is not an afterthought; every subsequent phase includes a mandatory audit against these regulatory standards.

## 3. Global Project RACI
| Phase | Accountable | Responsible | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| **01-03 Requirements**| Product Owner | Business Analyst | Stakeholders, Security & Compliance Officers | Dev Team |
| **04-07 Design** | Lead Architect | Assigned Leads | Security Officer, Compliance Officer | Stakeholders |
| **08-09 Engineering** | Lead Developer | Dev/QA Team | Architect, Security Officer | Product Owner |
| **10 Operations** | DevOps Lead | SRE Team | Architect, Compliance Officer | All Hands |

## 4. Documentation Inventory & Standards
- **Architectural Documentation**: Mandatory ADRs for every non-trivial technical decision (Phase 04).
- **Code Documentation**: Mandatory JSDoc with `@req`, `@layer`, and `@screen` (Phase 09).
- **API Documentation**: OpenAPI/Swagger contract-first baseline (Phase 07).
- **Operational Runbooks**: Mandatory Incident Response & Maintenance guides (Phase 10).

## 5. Design Aesthetics & UX Philosophy
- **Minimalist**: Focus on essential elements; eliminate clutter to reduce cognitive load.
- **High Contrast**: Ensure visual clarity and accessibility through harmonious yet distinct color pairings.
- **Mobile First**: Design for the smallest screen first to ensure functional integrity across all viewports.

## 6. Quality Gates & Pre-commit Enforcement
- **Automated Linting**: All source code (TS/JS/SQL) and artifacts (Markdown) MUST pass linting before any commit is accepted.
- **Pre-commit Hooks**: Mandatory use of **Husky** and **lint-staged** to enforce style guides, template integrity, and formatting (ESLint, Prettier, markdownlint).
- **Template Integrity**: Technical artifacts (SRS, ADR, UIDD) must follow the provided `template.md` structure or they will be rejected by the pre-commit gate.

## 7. Change Management & Synchronicity
- **Baseline Drift Check**: Before any implementation step, the developer MUST verify that no upstream baselines (Requirements/Design) have changed.
- **Change Request (CR) Lifecycle**: Any modification to a signed baseline must follow the **Request -> Impact Analysis -> Design Update -> Propagation** workflow.
- **Single Source of Truth (SSoT)**: Design artifacts are the definitive truth. Code is always a downstream projection of the design. If code and design diverge, the code is considered defective.
- **Propagation Mandate**: All changes in Requirements or Design MUST be propagated to the RTM and implementation code before the next sprint/phase sign-off.

---
*This pipeline is designed for world-class technical discipline.*
