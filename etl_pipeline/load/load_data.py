def select_model_ready_rows(df):
    """
    Separates valid rows from rejected ones.
    """
    model_ready = df[df["validation_errors"] == ""].copy()
    rejected = df[df["validation_errors"] != ""].copy()

    return model_ready, rejected
