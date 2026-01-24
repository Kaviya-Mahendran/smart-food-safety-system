import pandas as pd

def engineer_features(df: pd.DataFrame, reference_time: pd.Timestamp) -> pd.DataFrame:
    """
    Feature engineering that adapts to operational vs regulatory schemas.
    """
    df = df.copy()

    # ---- Time-based feature (only for operational data) ----
    if "cooked_at" in df.columns:
        df["hours_since_prepared"] = (
            reference_time - df["cooked_at"]
        ).dt.total_seconds() / 3600
    else:
        df["hours_since_prepared"] = None

    # ---- Expiry type flag ----
    df["is_use_by"] = (df.get("expiry_type") == "use_by").astype(int)

    # ---- Temperature availability ----
    df["has_temperature_data"] = (
        1 if "storage_temperature_c" in df.columns else 0
    )

    return df
