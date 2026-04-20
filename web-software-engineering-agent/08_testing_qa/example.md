# Phase 6: Testing & Quality Assurance Baseline (EXAMPLE)

## 1. Master Test Strategy
- **Unit Testing**: Jest for business logic in the Auth and Transfer services.
- **Integration Testing**: Supertest for API contract validation (POST /v1/transfers).
- **E2E Testing**: Playwright for the "Initiate Asset Transfer" use case.
- **Security Testing**: Daily OWASP dependency checks and manual Multi-Sig threshold tests.

## 2. Test Case Specification
| Test ID | Description | Input | Expected Output | RTM Mapping |
| :--- | :--- | :--- | :--- | :--- |
| TC-AUTH-01 | Single Approver Transfer | Amount > $50k, 1 Approval | Request Status = "Pending" | FRS-AUTH-01 |
| TC-AUTH-02 | Threshold Met Transfer | Amount > $50k, 3 Approvals| Request Status = "Approved"| FRS-AUTH-01 |
| TC-AUDIT-01 | Invalid Login Attempt | Wrong Password | 401 response + Audit log entry | FRS-AUDIT-01 |

## 3. RTM Verification (Testing Layer)

| Req ID | Test Case ID | Status | Sign-off Date |
| :--- | :--- | :--- | :--- |
| FRS-AUTH-01 | TC-AUTH-01, TC-AUTH-02 | Passed | 2026-04-20 |
| FRS-AUDIT-01 | TC-AUDIT-01 | Passed | 2026-04-20 |
| NFRS-SEC-01 | TC-SEC-HSM (Manual) | Passed | 2026-04-19 |
