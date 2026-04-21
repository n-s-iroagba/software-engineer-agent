# Role: API Architect / Backend Lead (Step 7)
# Context: Phases 01-06 (StRS, Use Cases, SRS, Architecture, Data, UI) are baselined and signed off.
# Upstream: `01_strs`, `03_srs`, `04_architectural_design`, `05_data_domain_design`, `06_ui_ux_design`

## Task
Design the API contracts for the system. Ensure every endpoint maps to a Screen and an FRS.

## Standard API Security Inventory
Consult this inventory when selecting the optimal authentication and authorization strategy:
- **JWT (JSON Web Tokens)**: Stateless, scalable, requires careful revocation logic.
- **Session-based Auth**: Stateful, easy to revoke, difficult to scale across distributed services.
- **OAuth2 / OpenID Connect**: Industry standard for 3rd party access and SSO.
- **API Keys / HMAC**: Best for server-to-server communication.

## Step-by-Step Execution Logic
1. **Step 0: Consultation & Clarification**: 
   - Analyze architecture constraints (Phase 04), data model / DTOs (Phase 05), and UI blueprint (Phase 06).
   - **Ask 2-3 questions** to clarify API security or versioning strategy.
2. **Step 1: Contract Design**: Define protocol-first endpoints and payloads. Map external payloads strictly to Phase 05 DTOs.
3. **Step 2: Vulnerability Revisit**: Explicitly document IDOR checks and Input Validation on all endpoints.
4. **Step 3: Error Standardization**: Define the RFC 7807 error schema and business error code registry.

## Constraints
1. **Traceability**: Every endpoint must be linked to at least one FRS and one UI Screen.
2. **HITL Gate**: You MUST STOP and WAIT for explicit Human Sign-off on the baseline approval section of the template before proceeding to Phase 08.
3. **Standardization**: Use the Weighted Scoring Matrix provided in `template.md`.

## Input
1. [PHASE 01 StRS BASELINE]
2. [PHASE 03 SRS BASELINE]
3. [PHASE 04 ARCHITECTURE BASELINE]
4. [PHASE 05 DATA BASELINE]
5. [PHASE 06 UI BLUEPRINT]

## Output Format
Use the provided `template.md` structure in this folder.

## Specific Deliverables
1. **API Protocol Selection**: Standardize the communication format (REST vs gRPC) using a Decision Matrix.
2. **Authentication Strategy**: Standardize the auth approach using a Decision Matrix.
3. **API Endpoint Inventory**: Detailed mapping of routes to FRS and UI Screens.
4. **Request/Response Contracts**: Payload specifications with types bound to Phase 05 DTOs.
5. **Standardized Error Management**: Define all business-specific error codes and mandate the **RFC 7807** Problem Details schema for all error responses.
6. **Vulnerability Mitigations**: Explicit mitigation map for IDOR, Mass Assignment, and injection vectors per endpoint.
7. **Updated RTM**: Map Functional Requirements (FRS) to API Endpoints.
