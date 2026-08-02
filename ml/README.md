<!-- SafeSwipe/ml/README.md -->

# SafeSwipe ML Pipeline

This folder holds the data pipeline and model training work — everything related to turning the Kaggle dataset into a working fraud-detection model.

## Status
Scaffolding only — no notebooks or scripts written yet.

## Stack
- Python 3
- pandas, scikit-learn (to start)

## Dataset
This project uses the Kaggle "Credit Card Fraud Detection" dataset. It's not included in the repo (too large, and shouldn't live in Git). To get it:
1. Download `creditcard.csv` from Kaggle.
2. Place it at `ml/data/creditcard.csv`.

## Setup
```bash
cd ml
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python train.py
```

Running `train.py` prints evaluation metrics (precision, recall, F1) and saves two files to `model/`:
- `fraud_model.joblib` — the trained logistic regression model
- `scaler.joblib` — the feature scaler, required to correctly scale any new transaction the same way training data was scaled

## Current model
Logistic Regression with `class_weight="balanced"`, on scaled features. Baseline result: ~92% recall (catches most fraud), ~6% precision (many false alarms) — a reasonable first model, not a final one. See `docs/private/changelog.md` for exact run history.