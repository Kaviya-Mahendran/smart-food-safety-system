## Model Artefacts

This folder contains serialized machine learning models produced by the
Freshness Scoring pipeline.

### Files

- `freshness_risk_regression.joblib`  
  Linear regression model trained to estimate continuous freshness risk
  based on time since preparation, temperature signals, and expiry semantics.

### Notes

- The model is designed as a decision-support component.
- Final food safety decisions are enforced by a separate rule-based layer.