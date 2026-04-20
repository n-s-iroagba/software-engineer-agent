# Phase 8: Testing & Quality Assurance Baseline

## 1. Test Strategy Decision Matrix
| Criterion | Weight | Option A: [Name] | Option B: [Name] | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Coverage | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| Speed (CI) | [0.x] | [1-5] | [1-5] | [Res] | [Res] |
| **TOTAL** | **1.0** | | | **[Sum]** | **[Sum]** |

**Conclusion & Rationalization**: [Rationalization]

## 2. Test Case Inventory (Separated by Level)

### 2.1 Unit Tests (Logic & Component Isolation)
| Test ID | Description | Component | Expected Outcome | RTM Mapping |
| :--- | :--- | :--- | :--- | :--- |
| TC-UNIT-01| [Brief] | [Component] | [Success] | FRS-01 |

### 2.2 Integration Tests (Module/API Interactions)
| Test ID | Description | API Endpoint | Expected Outcome | RTM Mapping |
| :--- | :--- | :--- | :--- | :--- |
| TC-INT-01 | [Brief] | [POST /path] | [201 Created] | FRS-01 |

### 2.3 E2E & UAT (User Acceptance Flows)
| Test ID | User Journey | Actor | Interaction Target (data-testid) | Success Criteria |
| :--- | :--- | :--- | :--- | :--- |
| TC-UAT-01 | [e.g. Fund Account]| [Customer] | `fund-button`, `amount-input` | [Balance updated]|

## 3. Governance & Acceptance Gates

### 3.1 Formal RACI (QA Layer)
| Task | Responsible | Accountable | Consulted | Informed |
| :--- | :--- | :--- | :--- | :--- |
| Defect Triage | QA Lead | Lead Dev | Architect | Stakeholders |
| UAT Execution | Business User| Sponsor | QA Lead | Project Team |

### 3.2 Acceptance Gate Scorecard
| Criterion | Metric/Threshold | Result | Status |
| :--- | :--- | :--- | :--- |
| **FRS Coverage** | 100% | [Actual %] | [Pass/Fail] |
| **Critical Defects**| Zero Open | [Count] | [Pass/Fail] |
| **E2E/UAT Success** | 100% of P0 Flows | [Actual %] | [Pass/Fail] |

## 4. Defect Severity Matrix
| Severity | Definition | Response Time |
| :--- | :--- | :--- |
| Critical | App down / Data loss | 2 hours |
| High | Functional failure | 8 hours |

## 5. Human Review & Baseline Sign-off
> [!IMPORTANT]
> **AI Instruction**: STOP and WAIT for a human signature below before providing the next folder's output.

| Role | Name | Signature / Date | Status |
| :--- | :--- | :--- | :--- |
| **QA Lead** | [Name] | | [Pending] |
| **Project Sponsor** | [Name] | | [Pending] |

## 6. RTM Verification (Testing Layer)
| Req ID | Test Case ID | Status | Sign-off Date |
| :--- | :--- | :--- | :--- |
| FRS-01 | TC-01 | Pending | N/A |

## 7. Baseline Verification
- [ ] Every FRS has at least one test case.
- [ ] Every NFRS has at least one validation method.
- [ ] E2E tests use `data-testid` selectors from Phase 06.
- [ ] Test toolstack selected via Weighted Decision Matrix (not hardcoded).
- [ ] Acceptance Gate scorecard thresholds defined for all P0 criteria.
