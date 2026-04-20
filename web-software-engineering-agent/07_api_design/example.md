# Phase 7: API Design Baseline (EXAMPLE)

## 1. API Protocol Decision Matrix
| Criterion | Weight | Option A: REST (OpenAPI) | Option B: gRPC (Proto) | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Integration | 0.5 | 5 | 2 | 2.5 | 1.0 |
| Performance | 0.3 | 3 | 5 | 0.9 | 1.5 |
| Tooling | 0.2 | 5 | 3 | 1.0 | 0.6 |
| **TOTAL** | **1.0** | | | **4.4** | **3.1** |

**Conclusion & Rationalization**: Choosing **REST** for the public-facing API to ensure maximum interoperability with customer systems and simplified browser-based integration (StRS-02), despite gRPC having lower latency for internal services.

## 2. API Endpoint Inventory

| Method | Endpoint | Description | Screen Mapping | RTM Mapping |
| :--- | :--- | :--- | :--- | :--- |
| POST | /v1/auth/login | Authenticate user via MFA | SCR-AUTH-01 | FRS-AUDIT-01 |
| POST | /v1/transfers | Initiate a Transfer | SCR-TRANS-01 | FRS-AUTH-01 |
| GET | /v1/assets | Fetch current asset balances | SCR-DASH-01 | FRS-BASE-01 |

## 2. Request/Response Contracts

### Endpoint: POST /v1/transfers
- **Request Body**:
  ```json
  {
    "asset_id": "uuid",
    "recipient_address": "string",
    "amount": "string",
    "memo": "string"
  }
  ```
- **Success Response (201 Created)**:
  ```json
  {
    "status": "success",
    "data": {
      "request_id": "uuid",
      "required_approvals": 3,
      "current_approvals": 0
    }
  }
  ```

## 3. Error Handling Specifications
| Code | Message | Scenario |
| :--- | :--- | :--- |
| 400 | INSUFFICIENT_FUNDS | Balance is lower than requested amount |
| 422 | INVALID_ADDRESS | Recipient address fails checksum validation |

## 4. RTM Update (API Layer)

| Req ID | Endpoint | Method | Status |
| :--- | :--- | :--- | :--- |
| FRS-AUTH-01 | /v1/transfers | POST | Designed |
| FRS-AUDIT-01 | /v1/auth/login| POST | Designed |
