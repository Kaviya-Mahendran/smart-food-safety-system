from datetime import datetime

def calculate_risk_state(
    expiry_type,
    expiry_date,
    prep_datetime,
    storage_type,
    allergen_detected,
    current_time=None
):
    """
    Deterministic, heuristic-based risk scoring engine
    """

    if current_time is None:
        current_time = datetime.now()

    explanation = []
    risk_score = 0

    # Rule 1: Allergens override freshness
    if allergen_detected is True:
        explanation.append("Allergen detected, overriding freshness checks")
        return "HIGH", explanation

    # Rule 2: Expiry logic
    if expiry_date:
        if expiry_type == "use_by" and current_time > expiry_date:
            explanation.append("Use-by date exceeded")
            return "HIGH", explanation

        if expiry_type == "best_before" and current_time > expiry_date:
            risk_score += 2
            explanation.append("Best-before date exceeded")

    # Rule 3: Preparation time decay
    if prep_datetime:
        hours_elapsed = (current_time - prep_datetime).total_seconds() / 3600

        if storage_type == "ambient" and hours_elapsed > 4:
            risk_score += 3
            explanation.append("Prepared over 4 hours ago at ambient temperature")

        if storage_type == "refrigerated" and hours_elapsed > 24:
            risk_score += 2
            explanation.append("Prepared over 24 hours ago under refrigeration")

    # Rule 4: Ambiguity handling
    if expiry_date is None or expiry_type is None:
        risk_score += 1
        explanation.append("Incomplete expiry information")

    # Final risk state
    if risk_score >= 4:
        return "HIGH", explanation
    elif risk_score >= 2:
        return "MEDIUM", explanation
    else:
        return "LOW", explanation
if __name__ == "__main__":
    from datetime import datetime

    risk, explanation = calculate_risk_state(
        expiry_type="best_before",
        expiry_date=datetime(2026, 1, 10),
        prep_datetime=datetime(2026, 1, 9, 14, 0),
        storage_type="ambient",
        allergen_detected=False
    )

    print("Risk State:", risk)
    print("Explanation:")
    for line in explanation:
        print("-", line)
