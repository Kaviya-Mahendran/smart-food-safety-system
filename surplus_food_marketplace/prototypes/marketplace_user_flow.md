This folder contains low-fidelity interaction prototypes describing how
users and businesses interact with the surplus food marketplace.

# Surplus Food Marketplace – User Flow Prototype

## Scenario 1: Consumer browsing surplus food

1. User opens the surplus food marketplace.
2. System displays only items marked as SAFE or EAT_SOON.
3. Each item shows:
   - food name
   - freshness score
   - safety badge
   - discount (if applicable)

4. Items marked as EAT_SOON are visually highlighted as urgent.
5. Items marked as UNSAFE are never shown to the user.

## Scenario 2: Restaurant listing surplus food

1. Restaurant uploads or confirms surplus food items.
2. System evaluates freshness score and safety decision.
3. Items classified as UNSAFE are automatically rejected.
4. Items classified as SAFE are listed normally.
5. Items classified as EAT_SOON are listed with urgency and discount.

This prototype demonstrates how safety decisions directly control
marketplace behaviour without user intervention.
