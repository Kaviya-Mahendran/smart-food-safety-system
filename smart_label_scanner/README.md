Smart Label Scanner

OCR based expiry interpretation and safety classification

Purpose of this module

This module is responsible for interpreting expiry information directly from food labels and translating it into clear, conservative safety signals.

In many real world settings, expiry labels are:

inconsistently formatted,

partially obscured,

misunderstood by consumers,

treated as interchangeable even when they are not.

The purpose of this module is not simply to extract text, but to interpret expiry intent and classify food items into meaningful safety categories that people can act on.

Why this module exists separately

I intentionally designed expiry interpretation as a standalone module, rather than embedding it inside the ML model.

Expiry labels represent regulatory and safety intent, not probabilistic signals. Treating them as features alone would blur the distinction between:

what is legally or medically unsafe, and

what is statistically likely to be low risk.

By separating this logic, expiry rules remain:

explicit,

auditable,

and override ML predictions when required.

Folder structure and design intent
smart_label_scanner/
│
├─ ocr/
├─ rules_engine/
└─ README.md


Each folder reflects a distinct responsibility.

ocr/ — extracting expiry text

This component focuses solely on text extraction, not interpretation.

What it handles

Printed expiry dates

“Use by” and “Best before” phrases

Common date formats and separators

Design considerations

OCR output is often noisy. I treated OCR results as:

imperfect inputs,

requiring validation,

unsuitable for direct decision making.

For this reason, OCR output is passed forward as structured text rather than used immediately for safety classification.

rules_engine/ — interpreting expiry intent

This folder contains the logic that interprets OCR output and converts it into safety categories.

Core rule distinctions

Use by → strict safety cutoff

Best before → quality degradation, not immediate risk

The rules engine explicitly models these differences rather than collapsing them into a single “expiry date”.

Safety classification logic

The rules engine maps expiry interpretation into three outcomes:

Green – Safe
Food is within acceptable safety or quality limits.

Yellow – Eat Soon
Food is approaching expiry or quality degradation but not unsafe.

Red – Unsafe
Food exceeds safe consumption thresholds and must be rejected.

These categories are designed to be:

easy to understand,

difficult to misinterpret,

conservative by default.

Interaction with the ML freshness score

This module is designed to override, not compete with, the ML model.

Examples:

A high Freshness Score does not override a “Use by” violation.

OCR uncertainty results in stricter classification, not optimism.

This ensures that statistical signals never undermine explicit safety constraints.

Why this is rule based (not ML)

Expiry interpretation is not a pattern recognition problem. It is a domain rule problem.

I chose a rule based approach because:

it is explainable,

it aligns with regulatory reasoning,

errors are easier to detect and correct,

conservative behaviour is easier to enforce.

This reflects how safety critical systems are typically implemented in practice.

Limitations and assumptions

This module assumes:

labels are printed in a readable format,

OCR confidence is available or inferred,

conservative fallback is acceptable when uncertainty exists.

It is intentionally designed to fail safely rather than attempt to guess.

Reflection and trade offs

Several trade offs were made:

I prioritised clarity over coverage, accepting that some edge cases would default to caution.

I separated OCR from interpretation to avoid coupling text noise with safety decisions.

I chose rules over ML to reflect the nature of expiry logic.

If extended, this module could incorporate:

multilingual label handling,

confidence weighted OCR fallbacks,

alignment with jurisdiction specific food labelling standards.

Why this module matters

This module demonstrates:

understanding of regulatory intent,

conservative system design,

separation between extraction and decision making,

user centric safety communication.

It complements the ML model by grounding the system in explicit, non negotiable safety rules, which is essential in food related applications.