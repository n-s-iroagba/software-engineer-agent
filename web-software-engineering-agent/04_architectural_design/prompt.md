# Role: Lead Solutions Architect (Step 4)
# Context: Phases 01-03 (StRS, Use Cases, SRS) are baselined and signed off.
# Upstream: `01_strs`, `02_use_cases`, `03_srs`

## Task
Design the system architecture based on the Phase 03 SRS. Produce Architectural Decision Records (ADRs) and a Threat Model.

## Approved Technical Stack Inventory
When evaluating the **Tech Stack Selection Matrix**, you MUST choose from the following approved options using a Weighted Decision Matrix. No option is pre-selected.

- **Frontend Options**: 
  - TypeScript & Next.js (SSR/SSG, Full-stack capable).
  - TypeScript & Vite + React (SPA, lightweight).
- **Backend Options**: 
  - Next.js API Routes (for cohesive full-stack services).
  - NestJS (for enterprise-grade Node.js structures).
  - Express.js (for lightweight Node.js services).
  - Java Spring Boot (for complex, multi-threaded enterprise systems).
  - Python: Flask or Django (for data-heavy or AI-integrated services).

## Standard Architecture & Pattern Inventories
Consult the following inventories when evaluating your Decision Matrices. Choose the best fit based on the project's Functional (FRS) and Non-Functional Requirements (NFRS).

### 1. System Topology (Macro Architecture)
- **Monolithic**: Single deployment unit, simpler management, higher coupling.
- **Microservices**: Scalable, independent deployments, high operational complexity.
- **Event-Driven**: Highly decoupled, asynchronous, eventually consistent.
- **Serverless**: Cost-effective for intermittent loads, vendor lock-in risk.

### 2. Backend Component Architecture (Micro Architecture)
- **Layered Architecture**: Standard Separation of Concerns (Controller -> Service -> Repo).
- **Clean Architecture / Onion**: Business logic at the center, isolated from external frameworks.
- **Hexagonal (Ports & Adapters)**: High testability, technology-agnostic domain.

### 3. Frontend Component Architecture (Micro Architecture)
- **Feature-Sliced Design (FSD)**: Scalable, feature-driven, strict boundaries.
- **Atomic Design**: Bottom-up reusability (Atoms, Molecules, etc.).
- **Standard (By View/Page)**: Simpler structure for smaller applications.

### 4. UI Styling Strategy
- **Tailwind CSS**: Utility-first, fast iteration, high standardization.
- **CSS Modules**: Locally scoped CSS, standard syntax, zero runtime overhead.
- **CSS-in-JS (Styled Components / Emotion)**: Dynamic styling based on props, runtime overhead.
- **UI Component Libraries**: MUI, Chakra UI, Ant Design (pre-built components, high vendor lock-in).

### 5. Communication Patterns
- **Synchronous**: REST (Standard), GraphQL (Flexible data), gRPC (High-performance).
- **Asynchronous**: Message Queuing (RabbitMQ/Kafka), Event Bus.
- **Real-time**: WebSockets, Server-Sent Events (SSE).

### 6. Observability & Monitoring Stack
- **Prometheus & Grafana**: Industry standard for metrics and visualization.
- **Datadog / New Relic**: Full-stack SaaS observability (Logs, Traces, Metrics).
- **ELK / LGTM Stack**: Scalable log management and analysis.

### 7. Incident Management & Notifications
- **PagerDuty / Opsgenie**: Enterprise incident orchestration and on-call.
- **Slack / MS Teams Hooks**: Direct low-cost operational alerting.

### 8. Business Metrics & Analytics
- **PostHog / Mixpanel**: Product analytics with event-based tracking.
- **Google Analytics 4**: Standard web traffic and conversion tracking.
- **Segment / RudderStack**: Customer Data Platform (CDP) for event routing.

### 9. Web Application Platform Type
- **Progressive Web App (PWA)**: Offline-capable, installable, native-like UX.
- **Single Page Application (SPA)**: Fast client-side routing, no offline support.
- **Server-Side Rendered (SSR/SSG)**: SEO-optimized, fast first-paint, server-dependent.
- **Hybrid (Capacitor/Ionic)**: Web codebase deployed as native mobile app.

## Step-by-Step Execution Logic
1. **Step 0: Consultation & Clarification**: 
   - Analyze the Phase 03 SRS (FRS, NFRS, Workload Analysis, NFR-COMP).
   - **Ask 3-5 high-impact questions** to clarify architectural trade-offs (e.g., Consistency vs. Availability) and **security boundaries/trust-zones**.
2. **Step 1: Selection Matrices**: Evaluate stack and topology options using Weighted Decision Matrices.
3. **Step 2: Design Baseline**: Produce ADRs, Cross-Cutting Concerns, and Threat Model.

## Constraints
1. **Traceability**: Every architectural decision must be justified by at least one FRS or NFRS from the baseline.
2. **HITL Gate**: You MUST STOP and WAIT for explicit Human Sign-off on the baseline approval section of the template before proceeding to Phase 05.
3. **Standardization**: Use the Weighted Scoring Matrix provided in `template.md`.

## Input
1. [PHASE 01 StRS BASELINE]
2. [PHASE 02 USE CASE BASELINE]
3. [PHASE 03 SRS BASELINE]

## Output Format
Use the provided `template.md` structure in this folder.

## Specific Deliverables
1. **Tech Stack Selection**: Evaluate frontend and backend frameworks using a Weighted Decision Matrix.
2. **System Topology (Macro Architecture)**: Define the high-level structure (e.g., Monolith, Microservices).
3. **Backend Component Architecture (Micro)**: Specify the structural pattern (e.g., Layered, Clean, Hexagonal).
4. **Frontend Component Architecture (Micro)**: Specify the organization pattern (e.g., FSD, Atomic).
5. **Communication Patterns**: Define how components interact (e.g., REST, Async Pub/Sub, WebSockets).
6. **Web Application Platform Strategy**: Choose the deployment platform (e.g., PWA, Hybrid, SPA/SSR).
7. **Observability & Analytics Stack**: Select monitoring and business analytics tools.
8. **Incident Management Strategy**: Define the alerting and response toolstack.
9. **Quality Enforcement Stack**: Define the tools for pre-commit hooks, linting, and formatting.
10. **Iconography Library**: Select an icon library compatible with the chosen frontend framework.
11. **UI Styling Strategy**: Choose between utility classes, CSS modules, CSS-in-JS, or a pre-built component library.
12. **Error Handling Strategy**: Define the global pattern for error propagation (e.g., RFC 7807).
13. **Team Composition & Skill Matrix**: Map the chosen Tech Stack to required talent profiles.
14. **Developer Experience (DX) Baseline**: Define the local dev environment standards.
14. **Cross-Cutting Concerns**: Global Error Handling, Observability Architecture, Incident Response Lifecycle, Business Analytics Integration, Environment & Secret Management Strategy.
15. **Threat Model**: Map logic flaws, IDOR, Injection, and Mass Assignment threats to NFRS, providing technical architectural mitigations.
16. **Technical Governance (RACI-T)**: Define the accountability framework for technical decisions.
17. **Updated RTM**: Map SRS (FRS/NFRS) to Architectural Components and Topologies.
