import pandas as pd
from pathlib import Path

def load_marketplace_items():
    """
    Load marketplace-ready items produced by the safety
    and freshness scoring pipeline.
    """
    base_path = Path(__file__).resolve().parents[1]
    data_path = base_path / "data" / "marketplace_ready_items.csv"

    df = pd.read_csv(data_path)
    return df


if __name__ == "__main__":
    df = load_marketplace_items()
    print("Marketplace items loaded:")
    print(df.head())
