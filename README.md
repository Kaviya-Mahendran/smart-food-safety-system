Smart Food Safety & Freshness Scoring System

A machine learning driven food safety and waste reduction system inspired by UK standards

Why I built this

While living in the UK, I experienced food systems where safety, freshness, and allergen information are communicated clearly and consistently. “Use by” and “best before” labels are treated differently, allergen warnings are prominent, and surplus food redistribution is governed by clear safety rules.

Outside that environment, I noticed how unclear freshness indicators, inconsistent labelling, and over reliance on static expiry dates often lead to two outcomes:

people consume food without understanding real risk, or

food that is still safe is unnecessarily discarded.

After my employment ended in April 2024, I used that time to independently design and build a data driven system that explores how machine learning, structured pipelines, and explicit safety rules could improve both consumer safety and food waste outcomes.

This repository contains that system.

What this system does (in plain terms)

The system assigns a Freshness Score (0–100) to food items and uses that score, alongside strict safety rules, to decide whether food is:

safe to consume,

should be consumed soon, or

must be rejected.

It does this by combining:

time since cooking or packaging,

storage temperature behaviour,

expiry label interpretation,

ingredient and allergen text,

conservative rule based safety checks.

The goal is not to replace judgement, but to provide clearer, data informed signals that are easy to understand and difficult to misuse.

Design principles

This project was designed around a few deliberate principles:

Safety over optimisation
If the model is uncertain, the system defaults to caution.

Transparency over complexity
Rule based logic is preferred where explainability matters more than raw accuracy.

Probabilistic, not absolute decisions
Freshness is modelled as a score, not a binary outcome.

Separation of concerns
ML, OCR, ETL, and product logic are kept modular and auditable.

These principles reflect how safety critical systems are typically designed in regulated environments like the UK.

High level system flow

Inputs

Cooking or packaging timestamps

Storage and temperature logs

Expiry label text (“use by”, “best before”)

Ingredient and allergen information

Processing

Data validation and cleaning (ETL)

Feature engineering

ML based freshness scoring

Rule based safety classification

Allergen extraction and risk flags

Outputs

Freshness Score (0–100)

Safety status (Safe / Eat Soon / Unsafe)

Allergen warnings

Eligibility for surplus food resale

Architecture diagrams and schemas are provided in the /docs folder.

Repository structure and intent

This repository represents one integrated system, broken into focused modules to reflect real world system design.

smart food safety system/
│
├─ freshness_scoring_model/
│   → Feature engineering, ML modelling, scoring logic
│
├─ smart_label_scanner/
│   → OCR extraction and expiry based safety rules
|
├─ allergen_detection/
│   → Allergen profiles, parsing logic, risk flags
│
├─ etl_pipeline/
│   → Raw → clean → validate → transform → load pipeline
│
├─ surplus_food_marketplace/
│   → Product logic and UI prototypes for safe surplus resale
│
├─ docs/
│   → Architecture diagrams, data schema, ethics and safety notes
│
└─ README.md


Each module contains its own README.md explaining:

why the module exists,

how it is designed,

example logic or code,

why the design choices matter,

what trade offs were made.

Key components (briefly)
Freshness scoring model

A supervised ML model that estimates food safety and quality using time and condition based features. The output is a bounded score (0–100) designed for interpretation, not blind automation. Model explainability is included to support trust and auditability.

Smart label scanner

An OCR based component that extracts expiry information and applies explicit rules to classify risk. This ensures conservative decisions even when text is unclear or partially missing.

Allergen detection

A rule based allergen parser that prioritises reliability and clarity over complex NLP. This choice reflects the higher risk tolerance required in food safety contexts.

ETL pipeline

A structured pipeline with explicit validation and quality checks, designed to show how unsafe or inconsistent data is handled before it reaches the model.

Surplus food marketplace (prototype)

A conceptual product layer that demonstrates how freshness scores and safety rules could be surfaced to users while preventing unsafe resale by design.

Responsible and ethical design

This system is intentionally not fully automated.

ML predictions are treated as advisory signals.

Rule based overrides enforce safety thresholds.

Unsafe items are blocked regardless of potential value.

Human judgement is assumed at the final decision point.

A detailed discussion of these choices is available in /docs/ethics_and_safety.md.

Why this project is relevant to the UK

This project reflects approaches commonly used in UK digital and data systems:

emphasis on safety and governance,

transparent decision logic,

separation between prediction and enforcement,

responsible use of machine learning in regulated domains.

It demonstrates how skills in data architecture, ML, and product design can be applied to socially meaningful problems aligned with UK priorities around food safety and waste reduction.

Authorship and independence

This project was fully self initiated, designed, and implemented by me outside formal employment. It represents independent technical work, architectural decision making, and product thinking rather than academic or tutorial based experimentation.

Future directions

Potential extensions include:

calibration using real sensor data,

alignment with formal UK food safety standards,

controlled pilots with food service environments,

expanded explainability for consumer facing use.