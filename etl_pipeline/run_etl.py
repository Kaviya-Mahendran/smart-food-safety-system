import pandas as pd
from clean.clean_data import clean_raw_data
from validate.validate_data import validate_data
from transform.feature_engineering import engineer_features
from load.load_data import select_model_ready_rows

REFERENCE_TIME = pd.Timestamp("2024-10-03 12:00")

def run_pipeline(csv_path: str):
    print(f"\nRunning ETL for: {csv_path}")

    df_raw = pd.read_csv(csv_path)
    print(f"Raw rows: {len(df_raw)}")

    df_clean = clean_raw_data(df_raw)
    df_validated = validate_data(df_clean)

    df_features = engineer_features(df_validated, REFERENCE_TIME)
    model_ready, rejected = select_model_ready_rows(df_features)

    print(f"Model-ready rows: {len(model_ready)}")
    print(f"Rejected rows: {len(rejected)}")

    return model_ready, rejected


if __name__ == "__main__":
    run_pipeline("raw/generic_food_data.csv")
    run_pipeline("raw/fssai_inspired_food_data.csv")
