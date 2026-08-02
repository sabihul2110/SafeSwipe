# SafeSwipe/ml/train.py

import pandas as pd
import os

DATA_PATH = os.path.join("data", "creditcard.csv")


def main():
    if not os.path.exists(DATA_PATH):
        print(f"Dataset not found at {DATA_PATH}. Download it from Kaggle first.")
        return

    df = pd.read_csv(DATA_PATH)
    print(f"Loaded dataset with {len(df)} rows and {len(df.columns)} columns.")
    print(df.head())


if __name__ == "__main__":
    main()