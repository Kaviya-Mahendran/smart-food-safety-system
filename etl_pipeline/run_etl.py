import pandas as pd
from pathlib import Path

from etl_pipeline.clean.clean_data import clean_raw_data
from etl_pipeline.validate.validate_data import validate_data
from etl_pipeline.transform.feature_engineering import engineer_features
from etl_pipeline.load.load_data import select_model_ready_rows

# Base paths
BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"

# Fixed reference time for reproducibility
REFERENCE_TIME = pd.Timestamp("2024-10-03 12:00")


def run_pipeline(csv_name: str):
    print(f"\nRunning ETL for: {csv_name}")

    # ---- Load raw data ----
    df_raw = pd.read_csv(RAW_DIR / csv_name)
    print(f"Raw rows: {len(df_raw)}")

    # ---- ETL steps ----
    df_clean = clean_raw_data(df_raw)
    df_validated = validate_data(df_clean)
    df_features = engineer_features(df_validated, REFERENCE_TIME)

    model_ready, rejected = select_model_ready_rows(df_features)

    print(f"Model-ready rows: {len(model_ready)}")
    print(f"Rejected rows: {len(rejected)}")

    # ---- Save model-ready data ONLY for generic dataset ----
    if "generic" in csv_name:
        output_path = (
            BASE_DIR.parent
            / "freshness_scoring_model"
            / "data"
            / "model_ready_generic.csv"
        )

        # Ensure folder exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save CSV
        model_ready.to_csv(output_path, index=False)

        print(f"Saved model-ready data to: {output_path}")

    return model_ready, rejected


if __name__ == "__main__":
    run_pipeline("generic_food_data.csv")
    run_pipeline("fssai_inspired_food_data.csv")
