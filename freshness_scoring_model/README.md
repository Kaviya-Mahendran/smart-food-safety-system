Freshness Scoring Model

Purpose

The Freshness Scoring Model is the core intelligence component of the Smart Food Safety System.

Its purpose is to estimate the current freshness and safety risk of a food item using a continuous score between 0 and 100, rather than relying on binary expiry logic. This allows food safety to be assessed as a gradient, reflecting real world storage and handling conditions.

The model answers a practical question:
How fresh and safe is this food item right now, given how it has been stored and handled?

The output of this module is intentionally designed to inform safety decisions, not replace them.

Design Rationale

Most consumer food safety tools rely on static expiry dates or simple countdown timers. These approaches fail to account for how food degrades in practice, where factors such as temperature, time, and handling conditions significantly affect safety.

This module was designed to:

Treat freshness as a spectrum rather than a binary state

Combine predictive modelling with deterministic safety logic downstream

Prioritise explainability over opaque accuracy gains

The design reflects how real food safety systems operate, where risk estimation must be transparent, auditable, and defensible.

Data Inputs

The model consumes validated, model ready data produced by the ETL pipeline.

Typical input features include:

Time elapsed since cooking or packaging

Storage temperature in degrees Celsius

Duration of storage under those conditions

Expiry label type (use by vs best before)

Basic food category indicators

All datasets used are synthetic and anonymised, created to mirror realistic distributions without exposing real consumer or business data.

Feature Engineering

Feature engineering focuses on clarity and interpretability.

Examples include:

Time based decay features

Temperature risk bands

Categorical encoding for expiry types

Combined indicators capturing time temperature interaction

Features are intentionally simple, allowing each contribution to be explained clearly. This is important in safety related contexts where decisions must be justified to non technical stakeholders.

Model Selection and Scoring Logic

A lightweight supervised learning approach is used to estimate freshness risk, which is then mapped to a standardised 0–100 freshness score.

Key design choices include:

Preference for stable, interpretable models

Explicit score normalisation

Deterministic post processing to enforce safety constraints

Score interpretation:

Scores close to 100 indicate very fresh, low risk items

Lower scores indicate increasing degradation and safety risk

The freshness score is not a final decision. It is a signal used by downstream safety and marketplace logic.

Explainability and Interpretability

Explainability is treated as a core requirement.

This module includes:

Feature contribution analysis

Model coefficient inspection

Saved artefacts demonstrating how inputs influence outputs

The goal is that any low score can be explained in plain language, supporting transparency and trust. This mirrors real world safety systems where explainability is essential.

Folder Structure
freshness_scoring_model/
├── data/        # Model ready datasets produced by the ETL pipeline
├── notebooks/   # Exploration, training, and evaluation
├── scripts/     # Reusable scoring and safety logic
├── models/      # Saved model artefacts and coefficients
└── README.md


The separation ensures that experimentation, production logic, and artefacts remain clearly organised.

Role Within the Overall System

This module:

Does not make final safety decisions

Does not override expiry rules

Does not interact with users directly

Instead, it provides an interpretable freshness signal that feeds into the Safety Decision Layer, where rule based logic enforces conservative safety outcomes.

This separation of concerns improves maintainability and auditability.

Why This Matters

From a technical perspective, this module demonstrates:

Applied machine learning for real world risk estimation

Feature engineering grounded in domain logic

Explainability in a safety critical context

From a product perspective, it shows how predictive scoring can reduce unnecessary food waste while maintaining safety and user trust.

Reflection

This module reflects my approach to applied machine learning: start from the real world problem, prioritise interpretability, and embed ML within a broader system rather than treating it as an isolated solution.

The Freshness Scoring Model is designed to be practical, explainable, and extensible, aligning with how safety focused digital systems are built in production environments.

When you’re ready, we can move on to the README for:

smart_label_scanner

allergen_detection

etl_pipeline (more technical)

Just tell me the next folder.
