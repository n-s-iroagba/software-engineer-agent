# Phase 02: Use Case Inventory Baseline (EXAMPLE)

## 1. Actor Identification
| Actor Name | Description | StRS Origin |
| :--- | :--- | :--- |
| Trader | Initiates and manages asset transfers. | StRS-02 |
| Custodian | Reviews and signs off on high-value transfers. | StRS-01 |

## 2. Use Case Inventory
| ID | Title | Primary Actor | Priority | StRS Mapping |
| :--- | :--- | :--- | :--- | :--- |
| UC-TRANS-01 | Initiate Asset Transfer | Trader | High | StRS-02 |
| UC-AUTH-01 | Approve Multi-Sig | Custodian | High | StRS-01 |

## 3. Detailed Use Case Specification
### UC-TRANS-01: Initiate Asset Transfer
- **Goal**: Transfer digital assets to a external address in < 60s.
- **Preconditions**: Trader is authenticated.
- **Main Success Scenario**:
  1. Trader selects Asset and enters Recipient Address.
  2. System validates balance and recipient format.
  3. System initiates transfer workflow.
  4. System notifies Custodians if threshold exceeded.

## 4. Updates Requirements Traceability Matrix (UC Layer)
| Req ID (StRS) | Use Case ID | Description | Status |
| :--- | :--- | :--- | :--- |
| StRS-01 | UC-AUTH-01 | Multi-Sig Sign-off | Derived |
| StRS-02 | UC-TRANS-01 | Instant Initiation | Derived |
