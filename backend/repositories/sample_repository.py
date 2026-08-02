# SafeSwipe/backend/repositories/sample_repository.py

import os

import pandas as pd

SAMPLES_PATH = os.path.join("data", "sample_transactions.csv")

_samples_df = None


def get_samples():
    global _samples_df
    if _samples_df is None:
        if not os.path.exists(SAMPLES_PATH):
            raise FileNotFoundError(f"Samples not found at {SAMPLES_PATH}. Run ml/generate_samples.py first.")
        _samples_df = pd.read_csv(SAMPLES_PATH)
    return _samples_df


def get_sample_by_id(sample_id: int):
    df = get_samples()
    row = df[df["sample_id"] == sample_id]
    if row.empty:
        return None
    return row.iloc[0]