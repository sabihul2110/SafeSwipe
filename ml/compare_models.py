# SafeSwipe/ml/compare_models.py

import os

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = os.path.join("data", "creditcard.csv")


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Download it from Kaggle first.")
    return pd.read_csv(DATA_PATH)


def main():
    df = load_data()
    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("=== Logistic Regression ===")
    lr = LogisticRegression(class_weight="balanced", max_iter=1000)
    lr.fit(X_train_scaled, y_train)
    print(classification_report(y_test, lr.predict(X_test_scaled)))

    print("=== Random Forest ===")
    # Random Forest doesn't need scaled features (it's not distance-based like
    # Logistic Regression), so we train it on the original, unscaled data.
    rf = RandomForestClassifier(class_weight="balanced", n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    print(classification_report(y_test, rf.predict(X_test)))


if __name__ == "__main__":
    main()