import pandas as pd

def clean_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning without making safety decisions.
    """
    df = df.copy()

    if "cooked_at" in df.columns:
        df["cooked_at"] = pd.to_datetime(df["cooked_at"], errors="coerce")

    if "manufacture_date" in df.columns:
        df["manufacture_date"] = pd.to_datetime(df["manufacture_date"], errors="coerce")

    if "expiry_date" in df.columns:
        df["expiry_date"] = pd.to_datetime(df["expiry_date"], errors="coerce")

    if "expiry_type" in df.columns:
        df["expiry_type"] = df["expiry_type"].astype(str).str.lower().str.strip()

    return df
