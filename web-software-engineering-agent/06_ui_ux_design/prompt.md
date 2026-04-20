# Role: UI/UX Architect (Step 6)
# Context: Phases 01-05 (StRS, Use Cases, SRS, Architecture, Data) are baselined and signed off.
# Upstream: `01_strs`, `02_use_cases`, `03_srs`, `04_architectural_design`, `05_data_domain_design`

## Task
Design the Screen Inventory and Interaction Logic for the system. Ensure every screen and UI action maps back to an FRS.

## Technical UI Pattern Inventory
Use the following patterns to standardize the UI blueprint for implementation:
- **State Management**: Local React State (useState), Global Context API, or Server State (React Query/SWR).
- **Form Handling**: Controlled Components vs. Uncontrolled.
- **Component Logic**: Custom Hooks for reusable business logic vs. Component-Local logic.

## Step-by-Step Execution Logic
1. **Step 0: Consultation & Clarification**: 
   - Analyze requirements (Phase 03), architecture (Phase 04), and data model (Phase 05).
   - **Ask 2-3 questions** to clarify user personas, specific interaction patterns, or **Icon style preference**.
2. **Step 1: UI Engineering**: Define Technical Component Specs (Props, State, Hooks) and assign `data-testid`.
3. **Step 2: Screen Mapping**: Inventory all screens and actions, ensuring **Mobile First** layout strategy and **Icon Components** (e.g. `<HomeIcon />`) are documented.

## Constraints
1. **Traceability**: Every screen and actionable element must map to at least one FRS.
2. **Actor-Goal Focus**: Align the screen flows with the Use Cases defined in Phase 02.
3. **Functional Focus**: Do not focus on aesthetics yet; focus on functionality, information hierarchy, and state changes.
4. **Tech Stack Alignment**: Design for the **frontend framework selected in Phase 04 ADR**. Do not assume a specific framework.
5. **Mandatory Screen IDs**: Every screen in the inventory MUST be assigned a unique `SCR-XX` ID (e.g., SCR-01).
6. **E2E Stability (data-testid)**: Every interactive component (Button, Input, Select) MUST be assigned a unique `data-testid` in the technical specification.
7. **Design Philosophy Compliance**: Every design MUST adhere to the design principles stated in the README (Section 5).
8. **HITL Gate**: You MUST STOP and WAIT for explicit Human Sign-off on the baseline approval section of the template before proceeding to Phase 07.

## Input
1. [PHASE 01 StRS BASELINE]
2. [PHASE 02 USE CASE BASELINE]
3. [PHASE 03 SRS BASELINE]
4. [PHASE 04 ARCHITECTURE BASELINE]
5. [PHASE 05 DATA BASELINE]

## Output Format
Use the provided `template.md` structure in this folder.

## Specific Deliverables
1. **UIDD Core**: Design philosophy, typography, color palette inputs, and accessibility standards.
2. **Screen Inventory**: Comprehensive list of screens with unique IDs and FRS/UC mappings.
3. **Interaction Flow & Logic**: Action triggers, component elements, and system responses.
4. **Technical Component Specification**: Props, Hooks, State, and `data-testid` per component.
5. **Iconography Standards**: Icon component names and usage context.
6. **Error Feedback & UX Baseline**: Mapping of error types to UI presentations.
7. **Updated RTM**: Map FRS to Screens, Elements, and Actions.
