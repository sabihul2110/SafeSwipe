# SafeSwipe/ml/train.py

import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

DATA_PATH = os.path.join("data", "creditcard.csv")
MODEL_PATH = os.path.join("model", "fraud_model.joblib")


def load_data():
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Download it from Kaggle first.")
    return pd.read_csv(DATA_PATH)


def train_and_evaluate(df):
    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Random Forest doesn't need feature scaling — it splits on raw
    # thresholds per feature, unlike distance-based models like Logistic
    # Regression, so we train directly on the unscaled data.
    model = RandomForestClassifier(class_weight="balanced", n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    return model


def save_artifacts(model):
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")


def main():
    df = load_data()
    model = train_and_evaluate(df)
    save_artifacts(model)


if __name__ == "__main__":
    main()