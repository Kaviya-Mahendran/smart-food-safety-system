# Smart Food Safety & Freshness Scoring System

> A product-oriented decision-support prototype combining data engineering, machine learning and deterministic safety rules to produce transparent food freshness and risk signals.

## Why this project exists

Food safety decisions are often reduced to a binary expiry-date check. This prototype explores a richer approach using continuous freshness scoring, structured safety rules, and explainable signals.

This is a decision-support prototype, not a replacement for food-safety regulation or expert judgement.

## System at a glance

```text
Raw Inputs
   ↓
ETL + Validation
   ↓
Structured Features
   ↓
Freshness Model ─────┐
Label / Allergen Rules ─┤
                       ↓
              Safety Decision Layer
                       ↓
          Safe / Eat Soon / Unsafe
                       ↓
          Human-readable explanation
```

## Core capabilities

- ETL and input validation
- Freshness feature engineering
- ML-based freshness scoring
- Deterministic safety rules and overrides
- OCR/NLP-inspired expiry-label parsing
- Allergen detection
- Explainable feature contribution tracing
- Consumer and marketplace-oriented decision outputs

## Responsible AI and safety

- Safety rules can override model outputs.
- Allergen detection is explicit and conservative.
- Synthetic/anonymised data is used for modelling.
- Outputs are intended as decision support.
- Feature importance describes model behaviour, not causality.

## Repository structure

```text
smart_food_safety_system/
├── etl_pipeline/
├── freshness_scoring_model/
├── smart_label_scanner/
├── allergen_detection/
├── surplus_food_marketplace/
├── docs/
└── README.md
```

## Evaluation

The repository contains example inputs and outputs demonstrating system behaviour. Formal model evaluation should be reported with reproducible metrics and a clearly documented dataset split before deployment claims are made.

## Future roadmap

- Formal benchmark dataset and evaluation protocol
- Model calibration and uncertainty estimates
- Automated data-quality tests
- Containerised deployment
- API layer
- Model and data drift monitoring
- Expanded food-category validation

**Focus:** applied ML · data engineering · explainable AI · decision support · responsible analytics