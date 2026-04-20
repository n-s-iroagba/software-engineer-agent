# Phase 00: Project Input Data

> [!IMPORTANT]
> This is the **seed document** for the entire engineering pipeline. It is the ONLY document that does not reference an upstream phase. All other phases derive their work from this input, starting with Phase 01 (StRS).

## 1. Project Description
*A clear, concise description of the product or system to be built.*

- **Project Name**: [e.g., FinTrack — Personal Finance Dashboard]
- **One-Liner**: [e.g., A web application that helps users track expenses, set budgets, and visualize spending habits.]
- **Problem Statement**: [What problem does this solve? Who suffers from it?]
- **Target Audience**: [Who will use this? e.g., Young professionals aged 22-35]
- **Business Model**: [e.g., Freemium with Pro subscription at $9.99/month]

## 2. Important Flows & Features
*List the critical user journeys and features that define the product's core value.*

| Priority | Flow / Feature | Description | Actor |
| :--- | :--- | :--- | :--- |
| P0 | [e.g., User Registration] | [User signs up with email/password and verifies account] | [End User] |
| P0 | [e.g., Expense Logging] | [User logs a transaction with category, amount, and date] | [End User] |
| P1 | [e.g., Budget Alerts] | [System notifies user when spending exceeds 80% of budget] | [System] |
| P2 | [e.g., Admin Dashboard] | [Admin views user metrics and manages accounts] | [Admin] |

## 3. Design & Brand Inputs
*Visual identity and brand constraints that will drive the UI/UX design in Phase 06.*

- **Primary Color**: [e.g., #1A73E8 (Google Blue)]
- **Secondary Color**: [e.g., #34A853 (Success Green)]
- **Accent Color**: [e.g., #FBBC04 (Warning Amber)]
- **Brand Personality**: [e.g., Professional, Trustworthy, Modern]
- **Logo**: [Provide or describe — e.g., Abstract shield icon]
- **Inspiration / Reference Sites**: [e.g., stripe.com, linear.app, mercury.com]

## 4. Caveats, Constraints & Assumptions
*Things the engineering team must know before starting. Non-negotiable limits.*

| Type | Description |
| :--- | :--- |
| **Budget Constraint** | [e.g., MVP must be delivered within $15,000] |
| **Timeline** | [e.g., MVP launch in 8 weeks] |
| **Regulatory** | [e.g., Must comply with GDPR for EU users] |
| **Technical Constraint** | [e.g., Must integrate with Plaid API for bank connections] |
| **Assumption** | [e.g., Users will primarily access via mobile browser] |
| **Out of Scope** | [e.g., Native mobile apps are NOT included in MVP] |

## 5. Stakeholder Contacts
*Who to consult during the pipeline execution.*

| Role | Name | Contact | Decision Authority |
| :--- | :--- | :--- | :--- |
| **Project Sponsor** | [Name] | [Email] | Final budget & scope approval |
| **Product Owner** | [Name] | [Email] | Feature prioritization |
| **Domain Expert** | [Name] | [Email] | Business rule clarification |
