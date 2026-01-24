import pandas as pd

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Schema-aware validation for both operational and regulatory food data.
    """
    df = df.copy()
    df["validation_errors"] = ""

    # ---- Time reference validation ----
    if "cooked_at" in df.columns:
        missing_time = df["cooked_at"].isna()
        df.loc[missing_time, "validation_errors"] += "Missing cooked_at; "

    if "manufacture_date" in df.columns:
        missing_mfg = df["manufacture_date"].isna()
        df.loc[missing_mfg, "validation_errors"] += "Missing manufacture_date; "

    # ---- Temperature validation (only if present) ----
    if "storage_temperature_c" in df.columns:
        invalid_temp = (
            (df["storage_temperature_c"] < 0) |
            (df["storage_temperature_c"] > 15)
        )
        df.loc[invalid_temp, "validation_errors"] += "Temperature out of bounds; "

    # ---- Expiry logic (only when both dates exist) ----
    date_col = None
    if "cooked_at" in df.columns:
        date_col = "cooked_at"
    elif "manufacture_date" in df.columns:
        date_col = "manufacture_date"

    if date_col and "expiry_date" in df.columns:
        expiry_before_start = df["expiry_date"] < df[date_col]
        df.loc[expiry_before_start, "validation_errors"] += "Expiry before start date; "

    return df
