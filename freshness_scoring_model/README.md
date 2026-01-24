Freshness Scoring Model

Machine learning model for estimating food safety and freshness

Purpose of this module

This module is the core analytical component of the system.

Its purpose is to estimate how safe and fresh a food item is at a given point in time, using a combination of time based decay, storage conditions, and handling signals. Rather than producing a binary “expired / not expired” outcome, the model outputs a Freshness Score between 0 and 100, designed to reflect gradual risk increase rather than sudden failure.

I intentionally designed this as a decision support model, not an automated enforcement mechanism. The score is later combined with explicit safety rules elsewhere in the system.

How this module fits into the wider system

This model sits downstream of the ETL pipeline and upstream of safety classification and product logic.

It only consumes validated and cleaned data

It does not make final safety decisions

It provides a transparent, explainable signal that other modules can interpret conservatively

This separation ensures that model uncertainty never directly results in unsafe outcomes.

Folder structure and design intent
freshness_scoring_model/
│
├── data/
├── notebooks/
├── scripts/
├── models/
└── README.md


Each resource exists for a specific reason, not convenience.

data/ — controlled, realistic input data

This folder contains synthetic but realistic datasets representing food items and their storage conditions.

What is included

Food preparation or packaging timestamps

Storage temperature readings over time

Expiry label type (use by vs best before)

Handling duration and exposure indicators

Why this matters

I deliberately avoided toy datasets. Even though the data is simulated, it mirrors real operational patterns such as:

temperature fluctuations during storage,

gradual risk accumulation,

incomplete or imperfect logging.

This allows the model to be tested against messy but realistic scenarios, which is closer to how food systems operate in practice.

notebooks/ — reasoning, not just results

The notebooks document the thinking process behind the model, not just the final outcome.

Typical notebooks include

data exploration and sanity checks

feature engineering decisions

model selection experiments

scoring calibration

explainability analysis

Why notebooks are used here

I used notebooks intentionally for this stage because they:

make assumptions visible,

show how features were chosen,

allow reviewers to follow the logic step by step.

This is especially important in safety related modelling, where understanding why a model behaves a certain way is more important than marginal accuracy gains.

scripts/ — reusable, auditable logic

This folder contains Python scripts that extract reusable logic from the notebooks.

What lives here

feature transformation functions

scoring normalisation logic

helper utilities for model evaluation

Why this separation matters

Notebooks are useful for exploration, but production oriented logic should be:

version controlled,

readable without execution,

easy to audit.

By moving core logic into scripts, I made the model easier to reason about and reuse without relying on interactive notebooks.

models/ — trained artefacts and metadata

This folder contains the trained model artefacts and related metadata.

What is stored

trained model files

configuration or parameter snapshots

evaluation summaries

Why models are stored separately

This separation reflects real ML workflows, where:

data,

training logic,

and trained artefacts

are treated as distinct concerns.

It also makes it clear that the model is an output, not a black box embedded directly in application code.

Scoring logic (conceptual overview)

The Freshness Score is designed to behave intuitively:

Starts near 100 shortly after cooking or packaging

Gradually decays as time passes

Decays faster under poor storage conditions

Is bounded and interpretable

The model estimates risk, and the score is then:

scaled to a 0–100 range,

calibrated to avoid sharp drops,

designed to be conservative near unsafe thresholds.

This avoids misleading precision and supports downstream safety rules.

Model choice and explainability

I prioritised models that balance:

interpretability,

stability,

and reasonable performance.

Rather than optimising aggressively for accuracy, I focused on:

feature importance,

monotonic behaviour where appropriate,

and explainability using feature contribution analysis.

This aligns with how ML is typically used in regulated or safety sensitive contexts.

What this module intentionally does not do

This model does not:

make final safety decisions

override expiry rules

approve food for resale

operate without validation

Those responsibilities belong to other modules by design.

This boundary is deliberate and reflects how ML systems should be used responsibly.

Reflection and trade offs

Several conscious trade offs were made here:

Rule based safety is prioritised over model confidence

Interpretability is prioritised over complex deep models

Synthetic data is used carefully to demonstrate logic, not claim real world deployment

If this system were extended, the first priority would be calibration with real sensor data, not adding more model complexity.