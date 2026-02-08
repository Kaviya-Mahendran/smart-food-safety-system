## FoodSense Risk Scoring Engine (Reference Implementation)

This repository contains a reference implementation of the
deterministic, heuristic-based risk scoring logic used in the
FoodSense prototype.

The logic was originally implemented and validated within a
low-code prototyping environment (Thunkable) to enable rapid
iteration during an SME pilot.

This codebase exists to:
- Document the core decision logic independently of platform
- Demonstrate the design of the safety decision engine
- Enable review of the scoring rules and explainability layer

The scoring engine is platform-agnostic and can be reused across
mobile, web, or backend implementations.
