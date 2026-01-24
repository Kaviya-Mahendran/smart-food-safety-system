Allergen Detection

Rule based allergen identification and risk flagging

Purpose of this module

This module is designed to help identify potential allergen risks from ingredient and label text and surface them clearly to users.

Food allergens represent a high risk domain, where false negatives can have serious consequences. For that reason, this module is intentionally conservative and prioritises clarity and reliability over cleverness or model complexity.

The goal is not to infer or predict allergies, but to flag known allergen indicators so that users can make informed decisions.

Why allergen detection is handled separately

I designed allergen detection as a standalone module, rather than folding it into the ML freshness model or OCR logic.

Allergen risk is:

not probabilistic in nature,

not suitable for optimisation based prediction,

and often governed by explicit labelling requirements.

Keeping this logic separate ensures allergen handling remains:

auditable,

easy to extend,

and independent of model behaviour.

Folder structure and design intent
allergen_detection/
│
├── profiles/
├── parser/
└── README.md


Each folder reflects a specific responsibility within the allergen detection flow.

profiles/ — structured allergen knowledge

This folder contains structured representations of known allergens.

What is included

common allergen names (e.g. milk, peanuts, shellfish),

known variations and synonyms,

grouped categories for easier extension.

Why this matters

Instead of hard coding allergen terms into logic, I externalised them into profiles to ensure:

easier updates,

clearer review,

reduced risk of hidden logic errors.

This approach mirrors how domain knowledge is typically managed in safety sensitive systems.

parser/ — interpreting ingredient text

The parser processes ingredient and label text to identify allergen indicators.

What the parser does

normalises text for comparison,

scans for allergen keywords and variants,

applies simple contextual checks where appropriate.

The parser does not attempt semantic inference or language modelling. Its role is to reliably surface explicit signals, not guess intent.

Risk flagging logic

When allergen indicators are detected, the module:

flags the allergen clearly,

associates it with the relevant ingredient or label section,

passes the information forward as a risk signal, not a decision.

The output is intentionally simple so it can be:

displayed directly to users,

consumed by downstream safety logic,

audited without ambiguity.

Why this module is rule based

I deliberately avoided machine learning or deep NLP for allergen detection.

The reasons are practical:

rule based logic is predictable,

failures are easier to identify,

updates can be reviewed without retraining models,

conservative behaviour is easier to guarantee.

In allergen handling, missing a known allergen is far worse than over flagging. The design reflects that reality.

Handling uncertainty and limitations

This module is designed to fail safely.

If:

text is incomplete,

formatting is unclear,

or confidence is low,

the system errs on the side of flagging potential risk rather than suppressing warnings.

The module does not claim completeness or medical authority. It is a support tool, not a diagnostic system.

Reflection and trade offs

Several trade offs were made consciously:

I prioritised reliability over language coverage.

I accepted higher false positives to reduce false negatives.

I avoided complex NLP to maintain auditability.

If extended, this module could:

incorporate multilingual ingredient lists,

align with jurisdiction specific allergen regulations,

integrate confidence scores for UI presentation.

These would be incremental improvements rather than structural changes.

Why this module matters

This module demonstrates:

responsible handling of high risk information,

separation between knowledge and logic,

conservative system design,

respect for real world consequences of errors.

It reinforces the overall system’s emphasis on safety, transparency, and trust, and complements the ML and OCR components by grounding them in explicit domain rules.