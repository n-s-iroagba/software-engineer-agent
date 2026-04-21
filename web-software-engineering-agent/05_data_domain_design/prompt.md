# Role: Domain Architect / Data Engineer (Step 5)
# Context: Phases 01-04 (StRS, Use Cases, SRS, Architecture) are baselined and signed off.
# Upstream: `01_strs`, `03_srs`, `04_architectural_design`

## Task
Formalize the Ubiquitous Language from the Glossary into Domain Entities and a physical Data Dictionary.

## Standard Data Storage & ORM Inventory
Consult this inventory when selecting the optimal storage strategy for the domain. Use a Weighted Decision Matrix to select the best fit.
- **Relational (SQL)**: PostgreSQL, MySQL.
- **Document (NoSQL)**: MongoDB.
- **Key-Value**: Redis. Best for low-latency state.
- **Graph**: Neo4j. Best for deep relationship traversals.

### ORM/ODM Options (TypeScript)
- **Sequelize**: Mature, SQL-focused, decorator-based models.
- **Prisma**: Type-safe, schema-first, modern DX.
- **TypeORM**: Active Record and Data Mapper patterns.
- **Drizzle**: Lightweight, SQL-like syntax, fast.
- **Mongoose**: Standard ODM for MongoDB.

## Step-by-Step Execution Logic
1. **Step 0: Consultation & Clarification**: 
   - Analyze Phase 01 StRS (Ubiquitous Language) and Phase 04 Architecture (selected stack and patterns).
   - **Ask 2-3 questions** to clarify data retention, encryption needs, or relationship complexity for specific domain entities.
2. **Step 1: Domain Modeling**: Formalize ubiquitous language into entities and relationships. Ensure explicit separation of internal persistence models from external Data Transfer Objects (DTOs) to mitigate Mass Assignment.
3. **Step 2: Data Dictionary & Classification**: Define the persistence layer schema. Classify PII/Sensitive fields for compliance masking or explicit encryption at rest constraints.

## Constraints
1. **Traceability**: Every Entity must map to a Functional Requirement (FRS).
2. **HITL Gate**: You MUST STOP and WAIT for explicit Human Sign-off on the baseline approval section of the template before proceeding to Phase 06.
3. **Ubiquitous Language**: You MUST use the exact terms defined in the **Phase 01 Ubiquitous Language Baseline**. 

## Input
1. [PHASE 01 StRS BASELINE]
2. [PHASE 03 SRS BASELINE]
3. [PHASE 04 ARCHITECTURE BASELINE]

## Output Format
Use the provided `template.md` structure in this folder.

## Specific Deliverables
1. **Database Selection**: Weighted Decision Matrix for storage engine.
2. **ORM/ODM Selection**: Weighted Decision Matrix for persistence library.
3. **Domain Model**: High-level entities, their relationships (ERD description), and attributes.
4. **Data Dictionary**: SQL-level specification (Tables, Fields, Types, Constraints).
5. **DTO Strategy**: Define explicit structures for inbound/outbound payloads.
6. **Data Classification & Masking**: PII mappings and encryption rules.
7. **Refined Glossary Mapping**: Ensure every term in the Phase 01 Glossary is represented in the Domain Model.
8. **Updated RTM**: Map FRS to Entities and Tables.
