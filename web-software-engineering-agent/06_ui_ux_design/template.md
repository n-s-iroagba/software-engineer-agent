# Phase 6: UI/UX Design Baseline (UIDD)

## 1. User Interface Design Document (UIDD) Core
*Design principles, Typography, Color Palette, and Accessibility standards.*

- **Design Philosophy**: [As defined in README Section 5 — e.g., Minimalist, High Contrast]
- **Responsive Strategy**: [As defined in README Section 5 — e.g., Mobile First]
- **Primary Color**: [Input from stakeholder — e.g., #1A73E8]
- **Design System**: [As decided in Phase 04 ADR — e.g., Material UI, Tailwind Custom]
- **Iconography**: [As decided in Phase 04 ADR — e.g., Lucide React - Component names]
- **Accessibility**: [As baselined in Phase 03 NFR-COMP — e.g., WCAG 2.1 AA]
- **Typography**: [e.g., Inter for UI, Roboto for Data]

## 2. Screen Inventory
*List of all screens to be developed.*

| Screen ID | Screen Name | Use Case Mapping | FRS Mapping |
| :--- | :--- | :--- | :--- |
| SCR-01 | [Dashboard Name] | UC-01 | FRS-01 |

## 3. Interaction Flow & Logic
| Action Trigger | Component/Element | Expected System Response |
| :--- | :--- | :--- |
| [e.g., Click 'Save']| [Save Button] | [Trigger API call and show success toast]|

## 4. Wireframe/UI Specs
*Describe the layout and key elements.*

- **Header**: [Logo, Search, User Profile]
- **Sidebar**: [Navigation items]
- **Main Content**: [Tables, Forms, Charts]

## 5. Technical Component Specification
| Component Name | Hooks Used | Props | Local State | data-testid |
| :--- | :--- | :--- | :--- | :--- |
| `TransferForm` | `useTransfer`, `useForm`| `onSuccess`, `onError`| `isLoading` | `transfer-form`|

## 6. Iconography Standards
*Mandatory: All icons must be implemented as framework-compatible components (e.g., `<SearchIcon />`, `<UserCircleIcon />`).*

| Icon Name | Usage Context | Library |
| :--- | :--- | :--- |
| [e.g., HomeIcon] | [Navigation] | [As decided in Phase 04 ADR] |

## 7. Error Feedback & UX Baseline
| Error Type | UI Presentation | Standard Action |
| :--- | :--- | :--- |
| **Authentication (401)** | Global Modal / Redirect | Clear Session & Login |
| **Validation (400)**| Inline Input Highlight | Show helper text |
| **Server Error (500)**| Global Toast Manager | Retry / Contact Support |
| **Conflict (409)**| Inline / Toast | Refresh Data |

## 8. NFR Compliance Matrix (UI Layer)
| NFR ID | Requirement | UI Mitigation | Status |
| :--- | :--- | :--- | :--- |
| NFRS-ACC-01 | WCAG 2.1 AA | [e.g. Radix UI Primitives] | [Pass] |

## 9. World-Class RTM (UI Layer)
| Req ID | Screen ID | Element/Action | Status | Priority |
| :--- | :--- | :--- | :--- | :--- |
| FRS-01 | SCR-01 | [Form Field x] | Designed | P0 |

---
## 10. Human Review & Baseline Sign-off
> [!IMPORTANT]
> **AI Instruction**: STOP and WAIT for a human signature below before providing the next folder's output.

| Role | Name | Signature / Date | Status |
| :--- | :--- | :--- | :--- |
| **UI/UX Architect** | [Name] | | [Pending] |
| **Lead Developer** | [Name] | | [Pending] |

## 11. Baseline Verification
- [ ] Every Screen ID maps to at least one FRS and Use Case.
- [ ] All interactive components have unique `data-testid` attributes.
- [ ] Design philosophy aligns with README Section 5 principles.
- [ ] Icon library matches Phase 04 ADR decision.
- [ ] Error UX Baseline covers all HTTP error categories.
- [ ] Primary color and typography defined and approved by stakeholder.
