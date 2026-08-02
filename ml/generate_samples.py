# SafeSwipe/ml/generate_samples.py

import os

import pandas as pd

DATA_PATH = os.path.join("data", "creditcard.csv")
OUTPUT_PATH = os.path.join("..", "backend", "data", "sample_transactions.csv")


def main():
    df = pd.read_csv(DATA_PATH)

    fraud_samples = df[df["Class"] == 1].sample(5, random_state=42)
    legit_samples = df[df["Class"] == 0].sample(5, random_state=42)

    samples = pd.concat([fraud_samples, legit_samples]).reset_index(drop=True)
    samples.insert(0, "sample_id", samples.index + 1)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    samples.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved {len(samples)} sample transactions to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()