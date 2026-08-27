# SafeSwipe/ml/tune_threshold.py

import os

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

DATA_PATH = os.path.join("data", "creditcard.csv")


def main():
    df = pd.read_csv(DATA_PATH)
    X = df.drop("Class", axis=1)
    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(class_weight="balanced", n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    probabilities = model.predict_proba(X_test)[:, 1]

    print(f"{'Threshold':<12}{'Precision':<12}{'Recall':<12}{'F1':<12}")
    for threshold in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
        predictions = (probabilities >= threshold).astype(int)
        precision = precision_score(y_test, predictions)
        recall = recall_score(y_test, predictions)
        f1 = f1_score(y_test, predictions)
        print(f"{threshold:<12}{precision:<12.2f}{recall:<12.2f}{f1:<12.2f}")


if __name__ == "__main__":
    main()
