import pandas as pd

def apply_safety_decision(row):
    """
    Apply rule-based safety decisions on top of ML freshness score.
    ML informs the decision but does not override safety rules.
    """

    # Hard safety overrides
    if pd.notna(row.get("validation_errors")) and row["validation_errors"] != "":
        return "UNSAFE"

    if row.get("is_expired", False):
        return "UNSAFE"

    score = row["freshness_score"]

    # Score-based decision
    if score < 40:
        return "UNSAFE"
    elif score < 70:
        return "EAT_SOON"
    else:
        return "SAFE"
    
