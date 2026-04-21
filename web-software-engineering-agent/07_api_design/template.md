# Phase 7: API Design Baseline

## 1. API Protocol Decision Matrix
| Criterion | Weight | Option A: REST | Option B: gRPC | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Latency | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| Ecosystem | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| **TOTAL** | **1.0** | | | **[Sum]** | **[Sum]** |

**Conclusion & Rationalization**: [Rationalization]

## 2. Authentication Strategy Selection (Weighted Scoring)
| Criterion | Weight | Option A: [Name] | Option B: [Name] | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Security | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| Scalability | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| **TOTAL** | **1.0** | | | **[Sum]** | **[Sum]** |

**Conclusion & Rationalization**: [Rationalization]

## 3. API Endpoint Inventory
*Inventory of all backend routes.*

| Method | Endpoint | Description | Screen Mapping | RTM Mapping |
| :--- | :--- | :--- | :--- | :--- |
| POST | /v1/[endpoint] | [Description] | SCR-01 | FRS-01 |

## 4. Request/Response Contracts
*Describe the payload structure.*

### Endpoint: [Name]
- **Request Body**:
  ```json
  {
    "field": "type"
  }
  ```
- **Success Response (200/201)**:
  ```json
  {
    "status": "success",
    "data": {}
  }
  ```

## 5. Standardized API Error Specifications
*All errors must follow the RFC 7807 (Problem Details) schema.*

### Global Error Schema
```json
{
  "type": "URI identifying the error type",
  "title": "Short, human-readable summary",
  "status": 400,
  "detail": "Detailed explanation of the error",
  "instance": "URI identifying the specific occurrence",
  "errors": [] // Optional array for validation errors
}
```

### Business Error Code Registry
| Error Code | HTTP Status | Description | User Message |
| :--- | :--- | :--- | :--- |
| ERR-AUTH-001 | 401 | Invalid Credentials | The email or password provided is incorrect. |
| ERR-TRAN-002 | 409 | Insufficient Funds | Your account balance is too low for this transfer. |

## 6. Business Logic & Vulnerability Mitigations
*Explicitly document endpoint-level mitigations against OWASP Top 10 API vulnerabilities (e.g., IDOR, Mass Assignment).*

| Endpoint / Method | Vulnerability Vector | Technical Mitigation |
| :--- | :--- | :--- |
| `PATCH /v1/users/:id` | IDOR (AuthZ bypass) | Verify `session.userId == :id` or `session.role == ADMIN` |
| `POST /v1/assets` | Mass Assignment | Bind request strictly to `CreateAssetDto`, ignore extra fields |
| `POST /v1/transfers` | Business Logic Flaw | Atomic transaction boundary, negative balance check before db commit |

## 7. NFR Compliance Matrix (API Layer)
| NFR ID | Requirement | API Mitigation | Status |
| :--- | :--- | :--- | :--- |
| NFRS-SEC-03 | Rate Limiting | [e.g. Redis sliding window] | [Pass] |

## 8. World-Class RTM (API Layer)
| Req ID | Endpoint / Hook | Method | Status | Priority |
| :--- | :--- | :--- | :--- | :--- |
| FRS-01 | `GET /assets` | `REST` | Designed | P0 |

---
## 9. Human Review & Baseline Sign-off
> [!IMPORTANT]
> **AI Instruction**: STOP and WAIT for a human signature below before providing the next folder's output.

| Role | Name | Signature / Date | Status |
| :--- | :--- | :--- | :--- |
| **API Architect** | [Name] | | [Pending] |
| **Security Officer** | [Name] | | [Pending] |
| **Lead Developer** | [Name] | | [Pending] |

## 10. Baseline Verification
