# SafeSwipe/ml/train.py

import os

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = os.path.join("data", "creditcard.csv")
MODEL_PATH = os.path.join("model", "fraud_model.joblib")
SCALER_PATH = os.path.join("model", "scaler.joblib")


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

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(class_weight="balanced", max_iter=1000)
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    return model, scaler


def save_artifacts(model, scaler):
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
    print(f"Saved model to {MODEL_PATH}")
    print(f"Saved scaler to {SCALER_PATH}")


def main():
    df = load_data()
    model, scaler = train_and_evaluate(df)
    save_artifacts(model, scaler)


if __name__ == "__main__":
    main()