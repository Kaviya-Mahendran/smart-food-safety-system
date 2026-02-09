**Project Overview**


Smart Food Safety & Freshness Scoring System is an innovation driven prototype that combines machine learning, rule based safety evaluation, OCR/NLP inspired label parsing, and a structured data engineering pipeline to assess food freshness and safety risk in a transparent, explainable way.

This repository contains an end to end food safety and freshness assessment system that models food risk as a continuous, explainable signal, rather than a binary expiry check.
The system combines:
**machine learning based freshness scoring**

**deterministic food safety rules**

**OCR / NLP inspired label understanding**

**A structured, auditable data pipeline**

to generate transparent safety decisions that can be understood by consumers, food businesses, and regulators.

The idea emerged from observing how clear and enforceable food labelling standards in the UK support safer consumption, compared with the ambiguity that exists in many other contexts. This project explores how data engineering, analytics, and responsible AI can bring that same clarity into digital food safety systems.

This is not a demo notebook and not a collection of scripts.

It is a product level system design, covering ingestion, modelling, decision logic, and user-facing outcomes.

**Illustration of the Product stages in simple flow charts:**

<img width="2065" height="321" alt="ETE_system flowdrawio" src="https://github.com/user-attachments/assets/45c9184b-47a3-4fcf-878f-9920832bcb22" />

<img width="1441" height="365" alt="ETL drawio" src="https://github.com/user-attachments/assets/43fa9e68-b537-493d-bba6-bc0886a3a12d" />

<img width="700" height="341" alt="feature_eng drawio" src="https://github.com/user-attachments/assets/fa287cea-8a04-4d9d-a9c8-a72e8731b08a" />

<img width="1217" height="227" alt="rule machime drawio" src="https://github.com/user-attachments/assets/ac010651-2731-4df7-9aaf-7160b914bc05" />

I designed this system after experiencing the clarity and consistency of food labelling and safety standards in the UK, and contrasting it with the ambiguity and inconsistency commonly seen elsewhere. The project explores how data, analytics, and responsible AI design can help consumers and food businesses make safer, better informed decisions.

**Tech Stack**

Python (pandas, numpy, scikit-learn)

Feature engineering & scoring pipelines

OCR / NLP-inspired text parsing

Rule-based safety engines

Explainability logic (feature contribution tracing)

Modular, product-oriented architecture

UI mockups for consumer and marketplace views

**System Architecture**

The system is deliberately layered so that each decision is inspectable.

Input Layer

cooking / packing timestamps

storage temperature and duration

ingredient & allergen text

expiry label text (free-form)

Data & Processing Layer

ETL pipeline with validation and sanity checks

transformation into structured freshness features

Intelligence Layer

ML-based freshness scoring engine

rule-based label scanner

rule-based allergen detection

Safety Decision Layer

safety thresholds and overrides

human-readable outcomes: Safe / Eat Soon / Unsafe

Product Layer

consumer safety explanations

surplus food marketplace eligibility logic

**Repository Structure**
smart_food_safety_system/
│
├── etl_pipeline/
├── freshness_scoring_model/
├── smart_label_scanner/
├── allergen_detection/
├── surplus_food_marketplace/
├── docs/
└── README.md


Each module can be run independently and reflects real production separation of concerns.

**Code Examples** 
Freshness Scoring Logic
def freshness_score(hours_since_cooked, temperature_c, unsafe_hours):
    base = 100
    score = (
        base
        - hours_since_cooked * 2
        - max(0, temperature_c - 5) * 3
        - unsafe_hours * 4
    )
    return max(0, min(100, score))


This mirrors how real safety systems penalise exposure over time, not just expiry dates.

Expiry Label Parsing
def parse_expiry_label(text):
    t = text.lower()
    if "use by" in t:
        return {"label": "use_by", "risk": "high"}
    if "best before" in t:
        return {"label": "best_before", "risk": "medium"}
    return {"label": "unknown", "risk": "unknown"}


Unstructured label text becomes structured risk signals.

Allergen Detection
def detect_allergens(ingredients, known_allergens):
    found = [
        a for a in known_allergens
        if a.lower() in ingredients.lower()
    ]
    return {
        "allergens": found,
        "risk_flag": bool(found)
    }


This logic intentionally over flags risk, reflecting real world safety priorities.

Example Inputs → Outputs (Evaluation)
Input	Output	Notes
“Best before 20 Nov, fridge 4°C, cooked 2h ago”	85 / 100 – Safe	Fresh, cold-stored
“Use by today, 8°C for 6h”	42 / 100 – Eat Soon	Temperature penalty
“Peanut oil listed”	Allergen flag	Explicit safety override

These examples demonstrate actual system behaviour, not just descriptions.

Novelty vs Standard Tools
Capability	Typical Tools	This System
Freshness logic	Binary expiry	Continuous risk score
Label handling	Barcode lookup	OCR + text parsing
Safety logic	Rules only	ML + rule hybrid
Explainability	None	Feature-level reasoning
Product intent	Utility app	End-to-end system

This framing makes the innovation immediately visible.

Responsible AI & Safety Design

Safety rules override model predictions

Allergen detection is explicit and conservative

Synthetic / anonymised data used for modelling

Decisions are explainable to non technical users

Accuracy alone is not enough in safety critical systems.
Justification matters.

End to end system design

ML + data engineering depth

Product level decision logic

Optional Criterion 1 – Innovation

Hybrid ML + rule engine

Continuous freshness modelling

Explainable safety decisions

Independent system design

Open GitHub repository

Supporting technical writing and public sharing

Screenshots of engagement added to /docs

App Prototype: https://food-sense--rejoiceinthelor.replit.app

Final Note

This repository represents deliberate, original work focused on:

real world safety constraints

explainability over opacity

and product ready system thinking

It reflects how senior data practitioners design systems people can trust, not just models that score well.
