from pathlib import Path

from smart_label_scanner.ocr.extract_text import extract_label_text
from smart_label_scanner.rules_engine.classify_label_risk import classify_label_risk


def run_label_scanner():
    """
    Run smart label scanner on sample label texts.
    """

    labels_path = Path(__file__).resolve().parent / "sample_labels" / "sample_label_texts.txt"

    print("Running Smart Label Scanner...\n")

    with open(labels_path, "r") as f:
        raw_text = f.read()

    labels = raw_text.split("---")

    for idx, label in enumerate(labels, start=1):
        label = label.strip()
        if not label:
            continue

        print(f"Label {idx}")
        print("-" * 20)

        extracted_text = extract_label_text(label)
        result = classify_label_risk(extracted_text)

        print("Label text:")
        print(extracted_text)
        print("\nClassification result:")
        print(f"  Label type: {result['label_type']}")
        print(f"  Risk level: {result['risk_level']}")
        print(f"  Extracted expiry date: {result['extracted_expiry_date']}")
        print("\n")


if __name__ == "__main__":
    run_label_scanner()
