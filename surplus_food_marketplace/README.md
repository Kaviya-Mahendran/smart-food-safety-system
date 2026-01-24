Surplus Food Marketplace (Prototype)

Safety constrained redistribution of surplus food

Purpose of this module

This module explores how surplus food could be redistributed without compromising safety, using the outputs of the wider system rather than ignoring them.

Surplus food platforms often focus on logistics and pricing while relying on minimal safety checks. This module was designed to test a different assumption:
surplus redistribution should be impossible unless safety criteria are met by design.

The result is a prototype marketplace concept that does not optimise for volume, but for trust, compliance, and consumer protection.

Why this is a prototype, not a full application

I deliberately kept this module at the prototype level.

The intention is to:

demonstrate product logic,

show how safety rules translate into user facing constraints,

and surface design trade offs clearly.

This is not a deployment or monetisation exercise. It is a design proof that connects data outputs to real world decisions.

Folder structure and intent
surplus_food_marketplace/
│
├─ prototypes/
├─ ui_mockups/
├─ logic/
└─ README.md


Each folder reflects a different layer of product thinking.

prototypes/ — conceptual flows

This folder contains high level representations of how surplus food would move through the system.

What is captured

item eligibility checks,

safety gatekeeping logic,

transitions between states (eligible, restricted, rejected).

These prototypes focus on decision flow, not visual polish.

ui_mockups/ — user facing communication

The mockups show how information would be presented to users.

Key elements displayed

Freshness Score,

safety classification,

allergen warnings,

eligibility status.

The design prioritises:

clarity over density,

warnings over persuasion,

and comprehension over aesthetics.

This reflects how safety information should be surfaced in consumer facing systems.

logic/ — enforcement, not suggestion

This folder contains the logic that enforces safety constraints.

Examples of enforced rules

items marked Unsafe cannot be listed,

items near expiry may be restricted or time limited,

allergen risks are always displayed and never suppressed.

Crucially, this logic does not negotiate with the ML score.
If a rule blocks an item, it stays blocked.

How this module uses upstream signals

This marketplace consumes outputs from:

the freshness scoring model,

the label scanner,

allergen detection,

ETL validation flags.

It does not reinterpret these signals. It respects them.

This separation ensures that product incentives cannot override safety logic.

Why safety is enforced at the product layer

Even the best data systems can fail if product design allows users to bypass safeguards.

By enforcing safety at the marketplace level:

unsafe behaviour is prevented by default,

trust does not depend on user vigilance,

and responsibility is shared by system design.

This reflects how regulated systems typically operate.

Reflection and trade offs

Several deliberate trade offs were made:

I accepted reduced resale volume to preserve safety.

I prioritised blocking behaviour over warning only messaging.

I chose not to include pricing or optimisation logic, as it distracts from safety goals.

If extended, this module could explore:

partnerships with regulated food charities,

audit logs for rejected items,

alignment with local food safety enforcement workflows.

Why this module matters

This module demonstrates:

product thinking grounded in real constraints,

respect for safety and regulation,

the ability to translate data outputs into enforceable decisions,

understanding that responsibility extends beyond modelling.

It completes the system by showing how data, rules, and ethics come together at the point where real people are affected.