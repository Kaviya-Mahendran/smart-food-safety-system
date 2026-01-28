Surplus Food Marketplace

Purpose

The Surplus Food Marketplace module represents the product layer of the Smart Food Safety System.

Its purpose is to demonstrate how safety approved intelligence can be translated into real world marketplace behaviour that reduces food waste without compromising consumer safety.

This module answers a practical question:

Which food items can be offered for resale or redistribution, under what conditions, and with what restrictions?

It does not generate safety decisions itself. It consumes structured outputs from upstream safety and freshness layers and applies transparent, business facing rules.

Design Philosophy

In real food rescue and surplus platforms, safety decisions must always take priority over commercial incentives.

This module is designed with a strict hierarchy:

Safety decisions are enforced upstream

The marketplace never overrides safety outcomes

Commercial logic is applied only to items already deemed acceptable

This separation ensures that:

unsafe food is never listed

borderline food is handled cautiously

business logic remains explainable and auditable

The result is a marketplace that is safety first by design.

Inputs

The marketplace consumes a curated, structured dataset produced by the Safety Decision Layer.

Key inputs include:

Freshness score

Safety decision (Safe, Eat Soon, Unsafe)

Expiry status

Basic item identifiers and food type

For this project, a representative sample dataset is used to demonstrate how the marketplace behaves when receiving safety approved inputs.

This approach keeps the focus on system design and decision logic rather than data volume.

Marketplace Decision Logic

Marketplace behaviour is derived directly from the safety classification.

The logic is intentionally simple and explicit:

Items marked Safe are listed normally

Items marked Eat Soon are listed with urgency indicators and discounting

Items marked Unsafe are automatically rejected and never shown to users

These rules are implemented as a dedicated, reusable logic layer. They do not depend on machine learning and do not reinterpret safety signals.

This mirrors real world platforms where compliance and trust are critical.

Outputs

The primary output of this module is a marketplace ready dataset that includes:

Listing eligibility

Listing type (standard, urgent, rejected)

Discount indicators for urgent items

This dataset represents a clear contract between safety intelligence and product behaviour, making the system easy to extend into dashboards, APIs, or mobile applications.

Folder Structure
surplus_food_marketplace/
├── data/          # Marketplace ready sample datasets
├── logic/         # Marketplace decision rules and loaders
├── prototypes/    # Interaction flow descriptions
├── ui_mockups/    # Visual mockups illustrating user experience
└── README.md


Each subfolder represents a different aspect of how safety intelligence becomes a usable product.

Prototypes and UI Mockups

This module includes low fidelity prototypes and UI mockups to help non technical stakeholders visualise system behaviour.

The mockups illustrate:

Consumer views showing freshness scores and safety badges

Urgent items highlighted with discounts

Unsafe items excluded from listings

Admin style views showing listing eligibility and rejection reasons

These artefacts are intentionally simple and focus on clarity over polish.

Role Within the Overall System

This module sits downstream of:

Freshness Scoring

Safety Decision Logic

Allergen and label risk signals

It does not modify or reinterpret those signals. Instead, it translates them into marketplace actions that are consistent, predictable, and compliant.

This design ensures the system remains modular and easy to audit.

Why This Matters

Food waste reduction systems often fail because they prioritise recovery over safety or rely on manual judgement.

This module demonstrates how:

automated safety intelligence can support responsible redistribution

risk can be communicated clearly to consumers

surplus food can be handled without lowering safety standards

It shows how data driven systems can enable sustainable outcomes while preserving trust.

Reflection

This module reflects my approach to product oriented data systems.

Rather than stopping at analytics or modelling, the focus is on how intelligence changes behaviour in a real application. Safety decisions are respected, user trust is prioritised, and business logic remains transparent.

The Surplus Food Marketplace demonstrates how technical systems can be designed to create measurable social impact without compromising responsibility.
