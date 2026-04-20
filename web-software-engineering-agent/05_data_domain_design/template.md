# Phase 5: Data & Domain Design Baseline

## 1. Database Selection (Weighted Scoring)
| Criterion | Weight | Option A: [Name] | Option B: [Name] | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Consistency | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| Scalability | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| **TOTAL** | **1.0** | | | **[Sum]** | **[Sum]** |

**Conclusion & Rationalization**: [Rationalization]

## 2. ORM/ODM Selection (Weighted Scoring)
| Criterion | Weight | Option A: [Name] | Option B: [Name] | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Type Safety | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| DX / Migration Support | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| **TOTAL** | **1.0** | | | **[Sum]** | **[Sum]** |

**Conclusion & Rationalization**: [Rationalization]

## 3. Domain Entities (Ubiquitous Language Formalized)
*Business entities translated from Phase 01 Glossary.*

| Entity | Description | Attributes | Constraints |
| :--- | :--- | :--- | :--- |
| [Entity Name] | [What it represents] | [field1, field2] | [Unique, Non-nullable] |

## 4. Data Dictionary
*Granular database-level mapping.*

### Table: [TableName]
| Field | Data Type | Primary/Foreign Key | Description |
| :--- | :--- | :--- | :--- |
| id | UUID | PK | Primary Identifier |
| created_at | Timestamp | N/A | Audit Trail |

## 5. NFR Compliance Matrix (Data Layer)
| NFR ID | Requirement | Persistence Mitigation | Status |
| :--- | :--- | :--- | :--- |
| NFRS-SEC-02 | Encryption at Rest| [e.g. TDE on PostgreSQL] | [Pass] |

## 6. World-Class RTM (Data Layer)
| Req ID | Entity Name | Table Name / Collection | Status | Priority |
| :--- | :--- | :--- | :--- | :--- |
| FRS-01 | [Entity x] | [Table y] | Designed | P0 |

---
## 7. Human Review & Baseline Sign-off
> [!IMPORTANT]
> **AI Instruction**: STOP and WAIT for a human signature below before providing the next folder's output.

| Role | Name | Signature / Date | Status |
| :--- | :--- | :--- | :--- |
| **Data Architect** | [Name] | | [Pending] |
| **Lead Developer** | [Name] | | [Pending] |

## 8. Baseline Verification
- [ ] Database selection justified by Read/Write Intensity (Ph03).
- [ ] ORM/ODM selection justified via Weighted Decision Matrix (not hardcoded).
- [ ] Ubiquitous Language terms from Ph01 mapped 1:1 to Domain Entities.
- [ ] Data Dictionary field types align with selected database engine.
