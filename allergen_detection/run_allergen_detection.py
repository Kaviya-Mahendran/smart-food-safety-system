from pathlib import Path

from allergen_detection.parser.extract_allergens import detect_allergens


def run_allergen_detection():
    inputs_path = Path(__file__).resolve().parent / "sample_inputs" / "sample_ingredients.txt"

    print("Running Allergen Detection...\n")

    with open(inputs_path, "r") as f:
        raw_text = f.read()

    samples = raw_text.split("---")

    for idx, text in enumerate(samples, start=1):
        text = text.strip()
        if not text:
            continue

        result = detect_allergens(text)

        print(f"Sample {idx}")
        print("-" * 20)
        print("Ingredient text:")
        print(text)
        print("\nDetection result:")
        print(f"  Detected allergens: {result['detected_allergens']}")
        print(f"  Risk level: {result['risk_level']}")
        print("\n")


if __name__ == "__main__":
    run_allergen_detection()
