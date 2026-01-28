from allergen_detection.profiles.allergen_profiles import ALLERGEN_KEYWORDS

def detect_allergens(ingredient_text: str) -> dict:
    """
    Detect allergens present in ingredient text.
    """

    ingredient_text_lower = ingredient_text.lower()
    detected = []

    for allergen, keywords in ALLERGEN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in ingredient_text_lower:
                detected.append(allergen)
                break

    risk_level = "HIGH" if detected else "LOW"

    return {
        "detected_allergens": detected,
        "risk_level": risk_level
    }
