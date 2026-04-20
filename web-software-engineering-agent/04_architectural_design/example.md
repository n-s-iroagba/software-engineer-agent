## 1. Architectural Decision Matrices (Weighted Scoring)

### 1.1 Tech Stack Selection
| Criterion | Weight | Option A: NestJS (Node) | Option B: Java Spring Boot | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Performance | 0.4 | 4 | 5 | 1.6 | 2.0 |
| Security | 0.3 | 4 | 5 | 1.2 | 1.5 |
| Ecosystem | 0.2 | 5 | 4 | 1.0 | 0.8 |
| Enterprise | 0.1 | 3 | 5 | 0.3 | 0.5 |
| **TOTAL** | **1.0** | | | **4.1** | **4.8** |

**Conclusion & Rationalization**: Choosing **Java Spring Boot** for the backend core due to its mature Thread-safety models, robust support for Hardware Security Modules (HSM) via JCE/JCA, and industry-standard security posture required for SOC II compliance (STRS-01). **Next.js & TypeScript** are mandated for the frontend to ensure a type-safe, high-performance user experience.

### 1.2 System Topology (Macro Architecture)
| Criterion | Weight | Option A: Monolith | Option B: Microservices | Score A (W) | Score B (W) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Isolation | 0.5 | 2 | 5 | 1.0 | 2.5 |
| Complexity | 0.3 | 5 | 2 | 1.5 | 0.6 |
| Deployment | 0.2 | 4 | 3 | 0.8 | 0.6 |
| **TOTAL** | **1.0** | | | **3.3** | **3.7** |

**Conclusion & Rationalization**: Choosing **Microservices** for OmniVault to ensure cryptographic services (HSM Connector) are logically and physically isolated from the UI gateway, mitigating risk of broad system compromise.

### 1.3 Communication Patterns
Rationalization: Choosing **REST** for external client communication and **Event-Driven (Kafka)** for internal audit trail synchronization to satisfy high-throughput logging requirements.

## 2. System Topology (Macro) Overview
The OmniVault platform utilizes a **Micro-Perimeter Architecture** with localized security zones.

## 3. Component Architecture (Micro) detail
Utilizes **Clean Architecture** for the backend to separate business logic from external drivers, and **Feature-Sliced Design (FSD)** for the frontend to ensure modular scalability.

### 3.1 Backend Component Specification (Pattern: Clean Architecture)
| Component | Responsibility | Pattern Used |
| :--- | :--- | :--- |
| **Auth Gateway** | Handles MFA and Session tokens. | Layered |
| **Transfer Domain**| Core Multi-Sig logic. | Clean/Hexagonal |
| **Audit Ledger** | Append-only event store. | Event Sourcing |

### 3.2 Frontend Component Specification (Pattern: FSD)
| Layer | Responsibility | Pattern Used |
| :--- | :--- | :--- |
| **Pages/Dashboard**| View composition | FSD Page |
| **Features/MultiSig**| Complex transaction signing | FSD Feature |

## 4. Cross-Cutting Concerns
### 4.1 Global Error Handling
Standardized error codes (Omni-ERR-XXX) with automated retry logic for idempotent operations.

### 4.2 Observability Architecture
Full OpenTelemetry integration. Metrics (Prometheus), Logs (Elastic), and Distributed Tracing (Jaeger) for all transfer flows.

## 2. Architecture Decision Records (ADRs)

### ADR-01: Use of HSM-Backed Key Custody
- **Status**: Accepted
- **Context**: Private keys must be protected from logical extraction.
- **Decision**: All signing keys will reside within Hardware Security Modules (HSM).
- **Consequences**: Higher cost, but meets NFRS-SEC-01 compliance.

## 3. Threat Model
| Threat | Mitigation Strategy | NFRS Mapping |
| :--- | :--- | :--- |
| Database Breach | Data at rest encryption + Audit Ledger integrity checks. | NFRS-SEC-01 |
| Privileged User Abuse | Multi-Sig required for all administrative actions. | FRS-AUTH-01 |

## 4. RTM Update (Architecture Layer)

| Req ID | ADR ID | Component ID | Status |
| :--- | :--- | :--- | :--- |
| FRS-AUTH-01 | ADR-01 | Auth Gateway | Mitigated |
| FRS-AUDIT-01 | N/A | Audit Ledger | Mitigated |
| NFRS-SEC-01 | ADR-01 | HSM Connector | Mitigated |
