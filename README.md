**Project Overview **

Smart Food Safety & Freshness Scoring System is an innovation driven prototype that combines machine learning, rule based safety evaluation, OCR/NLP inspired label parsing, and a structured data engineering pipeline to assess food freshness and safety risk in a transparent, explainable way.

I designed this system after experiencing the clarity and consistency of food labelling and safety standards in the UK, and contrasting it with the ambiguity and inconsistency commonly seen elsewhere. The project explores how data, analytics, and responsible AI design can help consumers and food businesses make safer, better informed decisions.

This is not a collection of isolated scripts.
It is an end to end product concept from raw data ingestion, to scoring logic, to user facing safety decisions.

The project demonstrates my ability to:

design real world data systems,

balance ML with deterministic safety rules,

and think beyond models into product behaviour and user trust.

 Innovation Summary 

Most food safety applications today rely on:

static expiry reminders,

barcode lookups,

or purely rule based logic.

This system introduces predictive and explainable scoring, normally not applied in consumer food safety contexts.

What makes this system innovative:

Hybrid decision model combining ML driven freshness scoring with rule based safety enforcement

Configurable freshness engine using time since preparation, storage temperature, duration, and label metadata

Explainable outputs, where safety decisions can be traced back to contributing factors

Label understanding module that translates unstructured expiry text into structured risk signals

Privacy aware pipeline design, using synthetic and anonymised data for modelling

Product ready architecture that can extend to allergens, recalls, and surplus food redistribution

Rather than treating food safety as a binary “expired / not expired” problem, this system models risk as a spectrum, making safety information more transparent and actionable.

This comparative approach — blending prediction, rules, and product logic is the core innovation of the project.

System Architecture

The system is designed as a clear, layered architecture:

Input Layer

Cooking / packing timestamps

Storage temperature and duration

Ingredient and allergen text

Expiry label text

Data & Processing Layer

ETL pipeline with validation and quality checks

Feature engineering for freshness and risk modelling

Intelligence Layer

ML based Freshness Scoring Engine

Rule based Smart Label Scanner

Rule based Allergen Detection

Safety Decision Layer

Threshold based safety classification

Human readable decision outcomes (Safe / Eat Soon / Unsafe)

Product Layer

Consumer safety view

Surplus food marketplace eligibility logic

UI mockups demonstrating real world usage

Architecture diagrams are available in the /docs folder.

Repository Structure (Assessor Friendly)
smart food safety system/
│
├── etl_pipeline/                # Data ingestion, cleaning, validation, transformation
├── freshness_scoring_model/     # ML scoring logic, notebooks, explainability
├── smart_label_scanner/         # OCR inspired label parsing + rules engine
├── allergen_detection/          # Rule based allergen risk detection
├── surplus_food_marketplace/    # Marketplace eligibility logic + UI mockups
├── docs/                        # Architecture diagrams, schema, design notes
└── README.md                    # This document


Each module is runnable independently from the terminal and documented separately.

Technical Highlights (Mapped to Mandatory & Optional Criteria)

This project explicitly demonstrates:

Data Engineering

ETL pipeline design

Validation and quality checks

Feature transformation logic

Machine Learning

Freshness risk modelling

Scoring normalisation (0–100)

Model interpretability (feature importance / SHAP style reasoning)

NLP / OCR Inspired Processing

Label text parsing

Rule based expiry classification

Responsible AI & Ethics

Safety first decision logic

Explicit allergen risk flagging

Privacy aware synthetic data usage

System & Architecture Design

Modular, extensible structure

Clear separation of concerns

Product Thinking

Consumer facing safety explanations

Marketplace eligibility enforcement

UX mockups demonstrating real usage

These skills are deliberately surfaced so assessors do not need to infer them.

Deep Dive: Freshness Scoring Engine

At the core of the system is the Freshness Scoring Engine, which assigns a 0–100 freshness score to each food item.

The score is derived from:

time elapsed since cooking or packaging,

storage temperature,

duration at unsafe temperatures,

expiry label type (use by vs best before).

The model combines:

feature weighted scoring logic,

supervised learning for risk prediction,

safety thresholds that override model output when required.

Explainability was a priority. Feature contributions are logged and analysed so that:

low scores can be explained,

unsafe decisions are justifiable,

and outputs remain interpretable to non technical users.

This reflects real world safety systems where transparency is as important as accuracy.

Future Roadmap 

This prototype is intentionally designed to scale.

Potential future extensions include:

Adaptive scoring thresholds using reinforcement learning

Personalised safety curves based on user behaviour

Integration with government recall and safety alert APIs

Batch prediction for retail and food service chains

Analytics dashboards for food waste optimisation

Federated learning for privacy preserving model updates

These directions demonstrate how the system could evolve into a full product ecosystem, not just a technical demo.

Impact Statement

This project explores how data and AI can improve public safety and reduce food waste.

By making freshness and safety decisions more transparent, the system empowers consumers, supports responsible food redistribution, and encourages safer food handling practices.

It reflects my interest in applying analytics and machine learning to real societal problems, not just abstract technical challenges.

 Supporting Technical Writing

Detailed explanations of design decisions and technical trade offs are (or will be) covered in supporting blog posts, including:

Designing a Freshness Scoring Engine

Rule Based vs ML Based Safety Decisions

Label Understanding with NLP Techniques

Privacy Aware Data Modelling for Consumer Systems

These writings support recognition beyond employment and complement the technical work.

Demo Screens & UI Mockups

The /surplus_food_marketplace/ui_mockups folder contains low fidelity screens illustrating:

Consumer safety views

Freshness score presentation

Allergen risk warnings

Surplus food eligibility display

These mockups elevate the project from a technical exercise to a product prototype.

Final Note

This repository represents independent, original work demonstrating:

technical depth,

innovation,

and leadership potential in digital technology.

It is intentionally designed to be readable, explainable, and extensible the same qualities expected in real world data products.
