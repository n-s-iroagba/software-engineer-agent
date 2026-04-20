# Phase 3: Data & Domain Design Baseline (EXAMPLE)

## 1. Domain Entities
| Entity | Description | Attributes | Constraints |
| :--- | :--- | :--- | :--- |
| **Custodian** | An authorized user with signing rights. | email, pub_key_hash | Unique Email |
| **Asset** | Digital assets held in custody. | symbol, decimals, network | Unique Symbol |
| **TransferRequest** | A request to move assets. | asset_id, amount, status | Status belongs to [Pending, Approved, Failed] |

## 2. Data Dictionary

### Table: `custodians`
| Field | Data Type | PK/FK | Description |
| :--- | :--- | :--- | :--- |
| id | UUID | PK | Unique Custodian ID |
| email | String(255) | N/A | Business email |
| role | Enum | N/A | Admin or Approver |

### Table: `transfer_requests`
| Field | Data Type | PK/FK | Description |
| :--- | :--- | :--- | :--- |
| id | UUID | PK | Request ID |
| asset_id | UUID | FK | Links to `assets.id` |
| approval_count| Integer | N/A | Track Multi-Sig progress |

## 3. RTM Update (Data Layer)

| Req ID | Entity Name | Table Name | Status |
| :--- | :--- | :--- | :--- |
| FRS-AUTH-01 | Custodian | custodians | Designed |
| FRS-TRANS-01 | TransferRequest | transfer_requests | Designed |
