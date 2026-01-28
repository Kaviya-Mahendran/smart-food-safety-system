"""
Marketplace decision rules.

This module translates safety decisions into marketplace behaviour.
It does NOT make safety decisions and does NOT override them.
"""

def apply_marketplace_rules(safety_decision: str) -> dict:
    """
    Determine how an item should be treated in the surplus food marketplace
    based on its safety classification.

    Parameters
    ----------
    safety_decision : str
        One of: 'SAFE', 'EAT_SOON', 'UNSAFE'

    Returns
    -------
    dict
        Marketplace behaviour including listing eligibility,
        listing type, and discount percentage.
    """

    if safety_decision == "SAFE":
        return {
            "list_item": True,
            "listing_type": "STANDARD",
            "discount_pct": 0
        }

    if safety_decision == "EAT_SOON":
        return {
            "list_item": True,
            "listing_type": "URGENT",
            "discount_pct": 50
        }

    # Default / UNSAFE
    return {
        "list_item": False,
        "listing_type": "REJECTED",
        "discount_pct": 0
    }
