Allergen Detection
Purpose

The Allergen Detection module is designed to identify potential allergen risks from ingredient text and surface them as clear, interpretable safety signals.

Its purpose is to support consumer safety and informed decision making, particularly for individuals with food allergies, by flagging known allergens early in the data pipeline.

This module answers a straightforward but critical question:

Does this food item contain ingredients that may pose an allergen risk?

Design Philosophy

Allergen detection is a safety critical problem where false negatives are unacceptable.

Rather than using probabilistic or opaque models, this module deliberately adopts a rule based approach that is:

conservative

explainable

easy to audit

The goal is not to predict sensitivity levels, but to reliably flag the presence of known allergens based on declared ingredient text.

This mirrors how allergen handling is implemented in regulated food systems.

Input Data

Inputs to this module are unstructured ingredient lists, typically extracted from packaging or product descriptions.

Examples include:

ingredient declarations on prepared foods

packaged food labels

menu style ingredient text

Sample inputs are provided to demonstrate behaviour across different food types without relying on real consumer data.

Allergen Profiles

Known allergens are defined explicitly using keyword based profiles.

These profiles represent common allergen categories such as:

nuts

dairy

gluten

soy

shellfish

Each category maps to a set of representative ingredient keywords.
This design allows profiles to be:

easily reviewed

extended

updated as regulations or requirements change

Detection Logic

The detection process follows a simple and transparent flow:

ingredient text is normalised

allergen keywords are matched deterministically

detected allergens are collected

a conservative risk level is assigned

If any known allergen is detected, the risk level is flagged as high.
If none are detected, the risk level is flagged as low.

No attempt is made to infer severity or exposure thresholds. This is a deliberate safety decision.

Outputs

The module produces structured outputs including:

a list of detected allergen categories

a high level allergen risk flag

These outputs are designed to integrate cleanly with:

safety decision logic

user facing warnings

marketplace eligibility rules

They are intentionally simple and human readable.

Folder Structure
allergen_detection/
├── profiles/         # Allergen keyword definitions
├── parser/           # Ingredient text parsing and detection logic
├── samples_inputs/   # Sample ingredient text inputs
├── run_allergen_detection.py
└── README.md


Each component has a single responsibility, keeping the module easy to understand and maintain.

Terminal Execution

The module can be executed directly from the command line to demonstrate behaviour.

Running the script prints:

the raw ingredient text

detected allergen categories

the resulting risk flag

This makes the detection logic easy to inspect, test, and explain without additional tooling.

Role Within the Overall System

The Allergen Detection module provides supporting safety signals to the wider system.

Its outputs can:

inform safety decisions

trigger user visible warnings

restrict marketplace listings where appropriate

It does not override freshness or expiry logic. Instead, it complements them by addressing a different dimension of food safety.

Why This Matters

Food allergies are a significant public health concern, and allergen mislabelling is a common source of risk.

This module demonstrates how:

simple, well designed rules can meaningfully reduce risk

safety logic can be made transparent and auditable

ethical considerations can be embedded directly into system design

It highlights the importance of responsible data use in consumer facing systems.

Reflection

This module reflects a cautious, safety first engineering mindset.

Rather than optimising for sophistication, the focus is on reliability, clarity, and trust. All assumptions are explicit, and detection logic is easy to reason about.

The Allergen Detection module shows how responsible AI and data systems often rely on clear rules and strong defaults, especially in safety critical domains.

