import re
from datetime import datetime

def classify_label_risk(label_text: str) -> dict:
    """
    Classify food safety risk based on expiry-related label text.
    """

    label_text_lower = label_text.lower()

    # Detect expiry keywords
    if "use by" in label_text_lower:
        risk_level = "HIGH"
        label_type = "USE_BY"
    elif "best before" in label_text_lower:
        risk_level = "MEDIUM"
        label_type = "BEST_BEFORE"
    else:
        risk_level = "UNKNOWN"
        label_type = "UNKNOWN"

    # Attempt to extract a date
    date_match = re.search(r"\d{1,2}\s\w+\s\d{4}", label_text)
    expiry_date = None

    if date_match:
        try:
            expiry_date = datetime.strptime(date_match.group(), "%d %b %Y")
        except ValueError:
            pass

    return {
        "label_type": label_type,
        "risk_level": risk_level,
        "extracted_expiry_date": expiry_date
    }
