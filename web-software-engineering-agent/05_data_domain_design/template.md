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

## 5. Data Transfer Objects (DTO) Strategy
*Strict separation of internal Entities from external Request/Response boundaries to prevent Mass Assignment vulnerabilities.*

| Domain Entity | Inbound DTO (Creation/Update) | Outbound DTO (Response) | Ignored/Protected Fields |
| :--- | :--- | :--- | :--- |
| [Entity Name] | `Create[Entity]Dto`, `Update[Entity]Dto` | `[Entity]ResponseDto` | `id`, `created_at`, `roleId` |

## 6. Data Classification & Masking (PII)
*Data privacy controls governed by Compliance Officer (e.g., SOC2, PCI-DSS, GDPR, HIPAA, CCPA).*

| Table/Entity | Field | Classification | Masking Rule (App Layer) | Encryption (Rest/Transit) |
| :--- | :--- | :--- | :--- | :--- |
| [e.g. User] | `email` | PII (Confidential) | Mask except domain | TDE |
| [e.g. User] | `password_hash` | Secret | Fully Hidden | Arg2ID/Bcrypt |

## 7. NFR Compliance Matrix (Data Layer)
| NFR ID | Requirement | Persistence Mitigation | Status |
| :--- | :--- | :--- | :--- |
| NFRS-SEC-02 | Encryption at Rest| [e.g. TDE on PostgreSQL] | [Pass] |

## 8. World-Class RTM (Data Layer)
| Req ID | Entity Name | Table Name / Collection | Status | Priority |
| :--- | :--- | :--- | :--- | :--- |
| FRS-01 | [Entity x] | [Table y] | Designed | P0 |

---
## 9. Human Review & Baseline Sign-off
> [!IMPORTANT]
> **AI Instruction**: STOP and WAIT for a human signature below before providing the next folder's output.

| Role | Name | Signature / Date | Status |
| :--- | :--- | :--- | :--- |
| **Data Architect** | [Name] | | [Pending] |
| **Compliance Officer** | [Name] | | [Pending] |
| **Lead Developer** | [Name] | | [Pending] |

## 10. Baseline Verification
- [ ] Database selection justified by Read/Write Intensity (Ph03).
- [ ] ORM/ODM selection justified via Weighted Decision Matrix (not hardcoded).
- [ ] Ubiquitous Language terms from Ph01 mapped 1:1 to Domain Entities.
- [ ] Data Dictionary field types align with selected database engine.
