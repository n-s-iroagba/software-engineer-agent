# Role: Senior Business Analyst (Step 1)
# Context: Phase 00 (Project Input Data) has been provided by the Project Sponsor.
# Upstream: `00_input/template.md`

## Task
Transform the raw Project Input Data into a formal Stakeholder Requirements Specification (StRS). This is Phase 1 of the Waterfall lifecycle.

## Step-by-Step Execution Logic
1. **Step 0: Consultation & Clarification**: 
   - Analyze the provided Phase 00 Input Data (Description, Flows, Design Inputs, Caveats).
   - Identify ambiguities or missing information.
   - **Ask the Human Engineer 3-5 high-impact questions** to refine the scope before proceeding.
2. **Step 1: Ubiquitous Language Baseline**: Define the domain terminology from the Phase 00 description and flows.
3. **Step 2: Metrics & RTM**: Formalize goals and scale targets from the Phase 00 caveats and constraints.

## Constraints
1. **ADKAR Model**: Assess the Awareness, Desire, Knowledge, Ability, and Reinforcement for each requirement.
2. **Emotional Context**: Capture the stakeholder's emotional drivers (Fear, Opportunity, Necessity).
3. **HITL Gate**: You MUST STOP and WAIT for explicit Human Sign-off on the baseline approval section of the template before proceeding to Phase 02.
4. **Ubiquitous Language**: Every stakeholder goal and system term must be defined in the **Ubiquitous Language Baseline**. 
5. **Design Inputs Passthrough**: The **Primary Color**, **Brand Personality**, and **Design Inspiration** from Phase 00 must be preserved and passed to Phase 06 via the README Design Philosophy.

## Input
[INSERT PHASE 00 INPUT DATA HERE]

## Output Format
Use the provided `template.md` structure in this folder.

## Specific Deliverables
1. **Ubiquitous Language Baseline**: Domain-specific terminology and its business meaning (DDD).
2. **Business Metrics**: Define KPIs (DAU/MAU, ARR, Churn), **Total/Concurrent User Projections**, and **Customer Satisfaction Metrics** (NPS, CSAT, Support Resolution Times, Rating Analytics).
3. **Stakeholder Mapping & RACI**:  
   - Identify roles and their sentiment.
   - Define a **Project RACI Matrix** (Responsible, Accountable, Consulted, Informed) for all 10 phases.
4. **Initial Resource Baseline**: Preliminary headcount projection (e.g., number of developers, designers, QA).
5. **World-Class RTM (Phase 1 Baseline)**: A traceability matrix with Priority, Emotional Driver, and Status.
